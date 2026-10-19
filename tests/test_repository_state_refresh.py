import base64
import copy
import hashlib
import importlib.util
import json
import pathlib
import sys
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
REGISTRY = json.loads((ROOT / "governance" / "repository-registry.json").read_text(encoding="utf-8"))
STATE = json.loads((ROOT / "governance" / "repository-state.json").read_text(encoding="utf-8"))
EXAMPLE_DESCRIPTOR = json.loads(
    (ROOT / "contracts" / "examples" / "component-release-descriptor.valid.json").read_text(encoding="utf-8")
)
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

spec = importlib.util.spec_from_file_location("state_refresh", SCRIPTS / "refresh_repository_state.py")
state_refresh = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(state_refresh)

from validate_repository_state import validate_state


def git_blob_sha(text):
    raw = text.encode("utf-8")
    return hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw).hexdigest()


def content_payload(data):
    text = json.dumps(data, sort_keys=True)
    return {
        "sha": git_blob_sha(text),
        "encoding": "base64",
        "content": base64.b64encode(text.encode("utf-8")).decode("ascii"),
    }


def descriptor(component_id, repository, revision, release_status):
    value = copy.deepcopy(EXAMPLE_DESCRIPTOR)
    value["component_id"] = component_id
    value["package"]["repository"] = repository
    value["revision"] = revision
    value["release_status"] = release_status
    for group in ("ci", "acceptance"):
        for item in value["evidence"][group]:
            item["revision"] = revision
    return value


class FakeClient:
    def __init__(self, registry, *, evidence_revision):
        self.registry = registry
        self.evidence_revision = evidence_revision
        self.repo_modes = {}
        self.calls = []
        self.entries = {item["component_id"]: item for item in registry["repositories"]}
        state_by_id = {item["repository_id"]: item for item in STATE["repositories"]}
        self.heads = {}
        for item in registry["repositories"]:
            if item["component_id"] == "ai-verse-system":
                self.heads[item["repository_full_name"]] = evidence_revision
            elif item["repository_id"] in state_by_id and state_by_id[item["repository_id"]]["observed_head"]:
                self.heads[item["repository_full_name"]] = state_by_id[item["repository_id"]]["observed_head"]
            else:
                self.heads[item["repository_full_name"]] = ("a" * 39) + str(item["repository_id"] % 10)

        self.files = {}
        for item in registry["repositories"]:
            path = item.get("component_release_descriptor_path")
            if not path:
                continue
            full_name = item["repository_full_name"]
            head = self.heads[full_name]
            accepted_revision = "2" * 40 if item["component_id"] == "ai-verse-os" else head
            status = "accepted" if item["component_id"] == "ai-verse-os" else "candidate"
            self.files[(full_name, path, head)] = content_payload(
                descriptor(item["component_id"], full_name, accepted_revision, status)
            )

        distribution = self.entries["ai-verse-distribution"]
        distribution_name = distribution["repository_full_name"]
        distribution_head = self.heads[distribution_name]
        release_path = "release-sets/test-core-default.json"
        release = {
            "schema_version": 1,
            "id": "test-core-default",
            "profile": "core",
            "status": "released",
            "promotion": {"default_channel": True},
            "components": [
                {
                    "id": item["component_id"],
                    "revision": self.heads[item["repository_full_name"]],
                }
                for item in registry["repositories"]
                if item.get("distribution_ships") is True
            ],
        }
        self.release_paths = [release_path]
        self.files[(distribution_name, release_path, distribution_head)] = content_payload(release)

    def repository(self, full_name):
        self.calls.append(("repository", full_name))
        mode = self.repo_modes.get(full_name)
        if mode == "unavailable":
            raise state_refresh.EvidenceUnavailable(full_name)
        if mode == "failed":
            raise state_refresh.EvidenceFailed(full_name)
        entry = next(item for item in self.registry["repositories"] if item["repository_full_name"] == full_name)
        live_id = entry["repository_id"] + 1 if mode == "wrong-id" else entry["repository_id"]
        return {"id": live_id, "default_branch": "main"}

    def branch(self, full_name, branch):
        self.calls.append(("branch", full_name, branch))
        return {"commit": {"sha": self.heads[full_name]}}

    def contents(self, full_name, path, ref):
        self.calls.append(("contents", full_name, path, ref))
        key = (full_name, path, ref)
        if key not in self.files:
            raise state_refresh.EvidenceMissing(path)
        return self.files[key]

    def list_contents(self, full_name, path, ref):
        self.calls.append(("list", full_name, path, ref))
        if path != "release-sets":
            raise state_refresh.EvidenceMissing(path)
        return [{"type": "file", "path": release_path} for release_path in self.release_paths]


class RepositoryStateRefreshTests(unittest.TestCase):
    def setUp(self):
        self.registry = copy.deepcopy(REGISTRY)
        self.state = copy.deepcopy(STATE)
        self.evidence_revision = "1" * 40

    def refresh(self, client=None, scope="Core", component_id=None):
        client = client or FakeClient(self.registry, evidence_revision=self.evidence_revision)
        return state_refresh.refresh_state(
            self.registry,
            self.state,
            client=client,
            scope=scope,
            component_id=component_id,
            evidence_revision=self.evidence_revision,
            registry_blob_sha=self.state["registry_binding"]["blob_sha"],
        )

    def test_current_core_scope_is_exact_control_plane_plus_core(self):
        expected = [
            item["repository_id"]
            for item in self.registry["repositories"]
            if item["component_id"] in {"ai-verse-system", "ai-verse-distribution"}
            or (item["lifecycle"] == "active" and "Core" in item["release_profiles"])
        ]
        self.assertEqual(state_refresh.resolve_scope(self.registry, "Core"), expected)

    def test_component_scope_adds_controls_and_declared_dependency_closure(self):
        registry = copy.deepcopy(self.registry)
        os_entry = next(item for item in registry["repositories"] if item["component_id"] == "ai-verse-os")
        os_entry["direct_compatibility_dependencies"] = ["ai-verse-brain"]
        ids = state_refresh.resolve_scope(registry, "component", component_id="ai-verse-os")
        by_component = {item["component_id"]: item["repository_id"] for item in registry["repositories"]}
        self.assertEqual(
            ids,
            [
                by_component["ai-verse-system"],
                by_component["ai-verse-distribution"],
                by_component["ai-verse-os"],
                by_component["ai-verse-brain"],
            ],
        )

    def test_agent_full_and_global_scopes_are_registry_derived(self):
        by_component = {item["component_id"]: item["repository_id"] for item in self.registry["repositories"]}
        core_components = [
            "ai-verse-system",
            "ai-verse-distribution",
            "ai-verse-os",
            "ai-verse-brain",
            "ai-verse-memory",
            "ai-verse-skills",
            "ai-verse-data",
        ]
        agent_components = core_components + [
            "ai-verse-gateway",
            "ai-verse-automations",
            "ai-verse-multiple-bots",
            "ai-verse-token",
        ]
        full_components = agent_components + [
            "ai-verse-connections",
            "ai-verse-dashboard",
        ]
        global_components = full_components + ["ai-verse-apps"]

        self.assertEqual(
            state_refresh.resolve_scope(self.registry, "Agent"),
            [by_component[component] for component in agent_components],
        )
        self.assertEqual(
            state_refresh.resolve_scope(self.registry, "Full"),
            [by_component[component] for component in full_components],
        )
        self.assertEqual(
            state_refresh.resolve_scope(self.registry, "global"),
            [by_component[component] for component in global_components],
        )
        self.assertNotIn(by_component["ai-verse-apps"], state_refresh.resolve_scope(self.registry, "Full"))

    def test_live_core_refresh_uses_exact_heads_descriptors_and_default_release_pins(self):
        client = FakeClient(self.registry, evidence_revision=self.evidence_revision)
        refreshed = self.refresh(client)
        self.assertEqual(refreshed["refresh"]["status"], "complete")
        self.assertEqual(refreshed["refresh"]["mode"], "scoped-refresh")
        by_id = {item["repository_id"]: item for item in refreshed["repositories"]}
        by_component = {item["component_id"]: item for item in self.registry["repositories"]}
        os_state = by_id[by_component["ai-verse-os"]["repository_id"]]
        brain_state = by_id[by_component["ai-verse-brain"]["repository_id"]]
        self.assertEqual(os_state["owner_acceptance"]["status"], "accepted")
        self.assertEqual(os_state["owner_acceptance"]["revision"], "2" * 40)
        self.assertNotEqual(os_state["owner_acceptance"]["revision"], os_state["observed_head"])
        self.assertEqual(brain_state["owner_acceptance"]["status"], "unverified")
        self.assertEqual(os_state["distribution_pin"]["revision"], os_state["observed_head"])
        self.assertEqual(os_state["distribution_pin"]["release_id"], "test-core-default")
        descriptor_calls = [call for call in client.calls if call[0] == "contents" and call[2] == "release/component-release.json"]
        self.assertTrue(descriptor_calls)
        for _, full_name, _, ref in descriptor_calls:
            self.assertEqual(ref, client.heads[full_name])

    def test_distribution_owner_descriptor_is_observed_without_creating_a_member_release_pin(self):
        distribution = next(item for item in self.registry["repositories"] if item["component_id"] == "ai-verse-distribution")
        distribution["component_release_descriptor_path"] = "release/component-release.json"
        if "release/component-release.json" not in distribution["owner_acceptance"]["discovery_paths"]:
            distribution["owner_acceptance"]["discovery_paths"].append("release/component-release.json")
        client = FakeClient(self.registry, evidence_revision=self.evidence_revision)
        head = client.heads[distribution["repository_full_name"]]
        accepted_revision = "2" * 40
        client.files[(distribution["repository_full_name"], "release/component-release.json", head)] = content_payload(
            descriptor("ai-verse-distribution", distribution["repository_full_name"], accepted_revision, "accepted")
        )

        refreshed = self.refresh(client)
        item = next(value for value in refreshed["repositories"] if value["repository_id"] == distribution["repository_id"])
        self.assertEqual(item["observed_head"], head)
        self.assertEqual(item["owner_acceptance"]["status"], "accepted")
        self.assertEqual(item["owner_acceptance"]["revision"], accepted_revision)
        self.assertNotEqual(item["owner_acceptance"]["revision"], item["observed_head"])
        self.assertEqual(item["distribution_pin"]["status"], "not-applicable")
        self.assertEqual(item["descriptor"]["status"], "observed")
        self.assertEqual(validate_state(refreshed, self.registry), [])

        other_registry = copy.deepcopy(self.registry)
        other_distribution = next(value for value in other_registry["repositories"] if value["repository_id"] == distribution["repository_id"])
        other_distribution["component_id"] = "another-release-orchestrator"
        self.assertIn(
            "$.repositories[1].descriptor: control-plane repository descriptor must be not-applicable",
            validate_state(refreshed, other_registry),
        )

    def test_invalid_development_descriptor_is_observed_but_not_owner_accepted(self):
        client = FakeClient(self.registry, evidence_revision=self.evidence_revision)
        brain = next(item for item in self.registry["repositories"] if item["component_id"] == "ai-verse-brain")
        head = client.heads[brain["repository_full_name"]]
        development = descriptor("ai-verse-brain", brain["repository_full_name"], head, "candidate")
        development["release_status"] = "development"
        client.files[(brain["repository_full_name"], "release/component-release.json", head)] = content_payload(development)
        refreshed = self.refresh(client)
        item = next(value for value in refreshed["repositories"] if value["repository_id"] == brain["repository_id"])
        self.assertEqual(item["descriptor"]["status"], "observed")
        self.assertEqual(item["descriptor"]["release_status"], "development")
        self.assertEqual(item["owner_acceptance"]["status"], "unverified")

    def test_unavailable_and_failed_repository_fetches_remain_distinct_and_refresh_is_partial(self):
        client = FakeClient(self.registry, evidence_revision=self.evidence_revision)
        memory = next(item for item in self.registry["repositories"] if item["component_id"] == "ai-verse-memory")
        data = next(item for item in self.registry["repositories"] if item["component_id"] == "ai-verse-data")
        client.repo_modes[memory["repository_full_name"]] = "unavailable"
        client.repo_modes[data["repository_full_name"]] = "failed"
        refreshed = self.refresh(client)
        self.assertEqual(refreshed["refresh"]["status"], "partial")
        by_id = {item["repository_id"]: item for item in refreshed["repositories"]}
        self.assertEqual(by_id[memory["repository_id"]]["access"], "unavailable")
        self.assertEqual(by_id[memory["repository_id"]]["freshness"]["status"], "unknown")
        self.assertEqual(by_id[data["repository_id"]]["access"], "failed")
        self.assertEqual(by_id[data["repository_id"]]["freshness"]["status"], "failed")

    def test_multiple_default_release_pins_fail_closed(self):
        client = FakeClient(self.registry, evidence_revision=self.evidence_revision)
        distribution = client.entries["ai-verse-distribution"]
        distribution_name = distribution["repository_full_name"]
        distribution_head = client.heads[distribution_name]
        second_path = "release-sets/ambiguous-default.json"
        os_entry = client.entries["ai-verse-os"]
        second_release = {
            "schema_version": 1,
            "id": "ambiguous-default",
            "profile": "core",
            "status": "released",
            "promotion": {"default_channel": True},
            "components": [{"id": "ai-verse-os", "revision": client.heads[os_entry["repository_full_name"]]}],
        }
        client.release_paths.append(second_path)
        client.files[(distribution_name, second_path, distribution_head)] = content_payload(second_release)
        refreshed = self.refresh(client)
        os_state = next(item for item in refreshed["repositories"] if item["repository_id"] == os_entry["repository_id"])
        self.assertEqual(refreshed["refresh"]["status"], "partial")
        self.assertEqual(os_state["distribution_pin"]["status"], "failed")
        self.assertIsNone(os_state["distribution_pin"]["revision"])

    def test_same_exact_evidence_produces_identical_state_without_timestamp_lineage(self):
        first_client = FakeClient(self.registry, evidence_revision=self.evidence_revision)
        second_client = FakeClient(self.registry, evidence_revision=self.evidence_revision)
        first = self.refresh(first_client)
        second = self.refresh(second_client)
        self.assertEqual(first, second)
        self.assertIsNone(first["refresh"]["last_scoped_refresh"]["observed_at"])

    def test_system_head_concurrency_fails_refresh(self):
        client = FakeClient(self.registry, evidence_revision=self.evidence_revision)
        system = client.entries["ai-verse-system"]
        client.heads[system["repository_full_name"]] = "3" * 40
        with self.assertRaises(state_refresh.EvidenceFailed):
            self.refresh(client)

    def test_stable_repository_id_mismatch_cannot_produce_complete_refresh(self):
        client = FakeClient(self.registry, evidence_revision=self.evidence_revision)
        os_entry = client.entries["ai-verse-os"]
        client.repo_modes[os_entry["repository_full_name"]] = "wrong-id"
        refreshed = self.refresh(client)
        item = next(value for value in refreshed["repositories"] if value["repository_id"] == os_entry["repository_id"])
        self.assertEqual(refreshed["refresh"]["status"], "partial")
        self.assertEqual(item["access"], "failed")
        self.assertIsNone(item["observed_head"])


if __name__ == "__main__":
    unittest.main()
