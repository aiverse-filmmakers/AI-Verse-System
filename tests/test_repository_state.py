import copy
import importlib.util
import json
import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
STATE = ROOT / "governance" / "repository-state.json"
REGISTRY = ROOT / "governance" / "repository-registry.json"
SCHEMA = ROOT / "contracts" / "repository-state.schema.json"
VALIDATOR_PATH = ROOT / "scripts" / "validate_repository_state.py"

spec = importlib.util.spec_from_file_location("state_validator", VALIDATOR_PATH)
state_validator = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(state_validator)


class RepositoryStateTests(unittest.TestCase):
    def setUp(self):
        self.state = json.loads(STATE.read_text(encoding="utf-8"))
        self.registry = json.loads(REGISTRY.read_text(encoding="utf-8"))

    def validate(self, state=None, registry=None):
        return state_validator.validate_state(
            state if state is not None else self.state,
            registry if registry is not None else self.registry,
            registry_path=REGISTRY,
        )

    def assertInvalid(self, state, contains):
        errors = self.validate(state=state)
        self.assertTrue(errors, "state unexpectedly validated")
        self.assertTrue(any(contains in error for error in errors), errors)

    def test_schema_json_is_well_formed_and_versioned(self):
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        self.assertEqual(schema["properties"]["schema_version"]["const"], "ai-verse.repository-state/v1")
        self.assertFalse(schema["additionalProperties"])

    def test_current_state_passes(self):
        self.assertEqual(self.validate(), [])

    def test_registry_binding_must_match_exact_registry_blob(self):
        state = copy.deepcopy(self.state)
        state["registry_binding"]["blob_sha"] = "f" * 40
        self.assertInvalid(state, "does not match Registry content")

    def test_state_must_cover_registered_repository_ids_exactly_once(self):
        state = copy.deepcopy(self.state)
        state["repositories"].pop()
        self.assertInvalid(state, "missing registered repository IDs")

        state = copy.deepcopy(self.state)
        state["repositories"][1]["repository_id"] = state["repositories"][0]["repository_id"]
        self.assertInvalid(state, "duplicate State repository ID")

    def test_unregistered_repository_fails_closed(self):
        state = copy.deepcopy(self.state)
        state["repositories"][0]["repository_id"] = 9999999999
        self.assertInvalid(state, "unregistered repository")

    def test_static_registry_fields_are_forbidden_in_state(self):
        state = copy.deepcopy(self.state)
        state["repositories"][0]["repository_full_name"] = "example/renamed"
        self.assertInvalid(state, "static Registry fields are forbidden in State")

    def test_accepted_owner_evidence_requires_exact_revision_and_refs(self):
        state = copy.deepcopy(self.state)
        acceptance = state["repositories"][2]["owner_acceptance"]
        acceptance["status"] = "accepted"
        acceptance["revision"] = None
        self.assertInvalid(state, "accepted evidence requires exact revision")

    def test_distribution_pin_requires_exact_revision_release_and_evidence(self):
        state = copy.deepcopy(self.state)
        pin = state["repositories"][2]["distribution_pin"]
        pin["revision"] = None
        self.assertInvalid(state, "pinned state requires exact revision")

    def test_non_shipped_control_plane_cannot_claim_distribution_pin(self):
        state = copy.deepcopy(self.state)
        pin = state["repositories"][0]["distribution_pin"]
        pin["status"] = "pinned"
        pin["revision"] = "a" * 40
        pin["release_id"] = "invented-release"
        pin["evidence_refs"] = ["invented"]
        self.assertInvalid(state, "non-shipped repository must be not-applicable")

    def test_observed_descriptor_requires_revision_status_blob_and_refs(self):
        state = copy.deepcopy(self.state)
        state["repositories"][2]["descriptor"]["blob_sha"] = None
        self.assertInvalid(state, "observed descriptor requires revision")

    def test_runtime_component_descriptor_cannot_be_not_applicable(self):
        state = copy.deepcopy(self.state)
        descriptor = state["repositories"][2]["descriptor"]
        descriptor.update(
            status="not-applicable",
            revision=None,
            release_status=None,
            blob_sha=None,
            evidence_refs=[],
        )
        self.assertInvalid(state, "runtime component descriptor cannot be not-applicable")

    def test_unavailable_and_failed_are_distinct_supported_evidence_states(self):
        for status in ("unavailable", "failed"):
            state = copy.deepcopy(self.state)
            state["refresh"]["status"] = "partial"
            repo = state["repositories"][1]
            repo["access"] = status
            repo["observed_head"] = None
            repo["owner_acceptance"]["status"] = status
            repo["owner_acceptance"]["revision"] = None
            repo["system_sync"]["status"] = status
            repo["system_sync"]["checkpoint_revision"] = None
            repo["freshness"]["status"] = "unknown" if status == "unavailable" else "failed"
            self.assertEqual(self.validate(state=state), [], status)

    def test_complete_core_refresh_must_cover_exact_registered_core_scope(self):
        state = copy.deepcopy(self.state)
        state["refresh"]["mode"] = "scoped-refresh"
        state["refresh"]["scope"] = "Core"
        state["refresh"]["last_scoped_refresh"]["scope"] = "Core"
        for repo in state["repositories"]:
            repo["freshness"]["scope"] = "Core"
        state["refresh"]["repository_ids"].pop()
        self.assertInvalid(state, "complete Core refresh must contain exactly")

    def test_complete_agent_full_and_global_scopes_follow_nested_registry_semantics(self):
        for scope in ("Agent", "Full", "global"):
            state = copy.deepcopy(self.state)
            state["refresh"]["scope"] = scope
            state["refresh"]["last_scoped_refresh"]["scope"] = scope
            if scope == "global":
                state["refresh"]["mode"] = "full-refresh"
                state["refresh"]["last_full_refresh"] = copy.deepcopy(state["refresh"]["last_scoped_refresh"])
            else:
                state["refresh"]["mode"] = "scoped-refresh"
            for repo in state["repositories"]:
                repo["freshness"]["scope"] = scope
            self.assertEqual(self.validate(state=state), [], scope)

    def test_complete_global_refresh_requires_every_registered_repository(self):
        state = copy.deepcopy(self.state)
        state["refresh"]["scope"] = "global"
        state["refresh"]["mode"] = "full-refresh"
        state["refresh"]["last_scoped_refresh"]["scope"] = "global"
        state["refresh"]["last_full_refresh"] = copy.deepcopy(state["refresh"]["last_scoped_refresh"])
        state["refresh"]["repository_ids"].pop()
        for repo in state["repositories"]:
            repo["freshness"]["scope"] = "global"
        self.assertInvalid(state, "complete global refresh must contain exactly")

    def test_repository_in_complete_refresh_must_bind_current_freshness_revision(self):
        state = copy.deepcopy(self.state)
        state["repositories"][2]["freshness"]["evidence_revision"] = "f" * 40
        self.assertInvalid(state, "must equal current refresh evidence revision")

    def test_watchdog_current_requires_real_heartbeat_and_full_scan(self):
        state = copy.deepcopy(self.state)
        state["watchdog"]["status"] = "WATCHDOG-CURRENT"
        state["watchdog"]["heartbeat_revision"] = None
        self.assertInvalid(state, "WATCHDOG-CURRENT requires heartbeat")

    def test_stale_watchdog_cannot_hide_without_global_warning_or_blocker(self):
        state = copy.deepcopy(self.state)
        state["watchdog"]["status"] = "WATCHDOG-STALE"
        state["watchdog"]["reason"] = "Synthetic stale fixture for validator coverage."
        state["drift"] = [item for item in state["drift"] if not item["id"].startswith("repository-watchdog-")]
        self.assertInvalid(state, "stale/failed watchdog requires open global WARNING/BLOCKING drift")

    def test_human_ledger_is_never_authority(self):
        state = copy.deepcopy(self.state)
        state["semantics"]["human_ledger_authority"] = True
        self.assertInvalid(state, "human_ledger_authority")


if __name__ == "__main__":
    unittest.main()
