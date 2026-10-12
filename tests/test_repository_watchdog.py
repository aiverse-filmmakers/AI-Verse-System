import copy
import importlib.util
import json
import pathlib
import sys
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

spec = importlib.util.spec_from_file_location("repository_watchdog", SCRIPTS / "run_repository_watchdog.py")
repository_watchdog = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(repository_watchdog)

REGISTRY = json.loads((ROOT / "governance" / "repository-registry.json").read_text(encoding="utf-8"))
STATE = json.loads((ROOT / "governance" / "repository-state.json").read_text(encoding="utf-8"))


def global_refresh(state, revision="b" * 40, status="complete"):
    value = copy.deepcopy(state)
    ids = [item["repository_id"] for item in REGISTRY["repositories"]]
    registry_by_id = {item["repository_id"]: item for item in REGISTRY["repositories"]}
    record = {
        "scope": "global",
        "status": status,
        "evidence_revision": revision,
        "observed_at": None,
    }
    value["refresh"] = {
        "mode": "full-refresh",
        "scope": "global",
        "status": status,
        "repository_ids": ids,
        "evidence_revision": revision,
        "last_scoped_refresh": copy.deepcopy(record),
        "last_full_refresh": copy.deepcopy(record),
    }
    for index, item in enumerate(value["repositories"]):
        registry_entry = registry_by_id[item["repository_id"]]
        if status == "complete" and item["access"] == "unverified":
            synthetic_head = f"{index + 1:040x}"[-40:]
            item["access"] = "verified"
            item["observed_head"] = synthetic_head
            if registry_entry["surface_classification"] == "runtime-component":
                item["descriptor"] = {
                    "status": "observed",
                    "revision": synthetic_head,
                    "release_status": "candidate",
                    "blob_sha": f"{index + 101:040x}"[-40:],
                    "evidence_refs": [f"synthetic-descriptor-{item['repository_id']}"],
                }
                item["distribution_pin"] = {
                    "status": "unpinned",
                    "revision": None,
                    "release_id": None,
                    "evidence_refs": ["synthetic-release-set-scan"],
                }
        item["freshness"] = {
            "scope": "global",
            "status": "fresh" if item["access"] == "verified" else "unknown",
            "evidence_revision": revision,
        }
    return value


def stale_bootstrap(state):
    value = copy.deepcopy(state)
    value["watchdog"] = {
        "status": "WATCHDOG-STALE",
        "heartbeat_revision": None,
        "last_successful_full_scan": None,
        "reason": "Synthetic bootstrap-stale fixture.",
    }
    found = False
    for item in value["drift"]:
        if item["id"] == "repository-watchdog-stale":
            item["status"] = "open"
            item["severity"] = "WARNING"
            item["scope"] = "global"
            found = True
    if not found:
        value["drift"].append(
            {
                "id": "repository-watchdog-stale",
                "marker": "CANONICAL-DRIFT-DETECTED",
                "status": "open",
                "severity": "WARNING",
                "scope": "global",
                "repository_ids": [REGISTRY["repositories"][0]["repository_id"]],
                "reason": "Synthetic bootstrap-stale fixture.",
                "evidence_refs": ["synthetic-test-fixture"],
                "required_action": "Run a successful full watchdog refresh.",
            }
        )
    return value


class RepositoryWatchdogTests(unittest.TestCase):
    def setUp(self):
        self.registry = copy.deepcopy(REGISTRY)
        self.state = copy.deepcopy(STATE)

    def test_successful_global_scan_sets_current_heartbeat_and_resolves_watchdog_drift(self):
        refreshed = global_refresh(self.state)
        result, successful, failures = repository_watchdog.apply_watchdog_transition(
            self.registry,
            self.state,
            refreshed,
            observed_at="2026-10-12T16:50:00Z",
        )
        self.assertTrue(successful)
        self.assertEqual(failures, [])
        self.assertEqual(result["watchdog"]["status"], "WATCHDOG-CURRENT")
        self.assertEqual(result["watchdog"]["heartbeat_revision"], "b" * 40)
        self.assertEqual(result["watchdog"]["last_successful_full_scan"]["scope"], "global")
        self.assertEqual(result["watchdog"]["last_successful_full_scan"]["observed_at"], "2026-10-12T16:50:00Z")
        self.assertEqual(result["refresh"]["last_full_refresh"]["observed_at"], "2026-10-12T16:50:00Z")
        watchdog_drift = [item for item in result["drift"] if item["id"].startswith("repository-watchdog-")]
        self.assertTrue(watchdog_drift)
        self.assertTrue(all(item["status"] == "resolved" for item in watchdog_drift))

    def test_first_failure_after_current_is_failed_then_second_is_stale(self):
        current, _, _ = repository_watchdog.apply_watchdog_transition(
            self.registry,
            self.state,
            global_refresh(self.state, revision="b" * 40),
            observed_at="2026-10-12T16:50:00Z",
        )

        first = global_refresh(current, revision="c" * 40, status="partial")
        repo = first["repositories"][2]
        repo["access"] = "failed"
        repo["observed_head"] = None
        repo["freshness"]["status"] = "failed"
        first_result, successful, failures = repository_watchdog.apply_watchdog_transition(
            self.registry,
            current,
            first,
            observed_at="2026-10-13T16:50:00Z",
        )
        self.assertFalse(successful)
        self.assertTrue(failures)
        self.assertEqual(first_result["watchdog"]["status"], "WATCHDOG-FAILED")
        self.assertEqual(first_result["watchdog"]["heartbeat_revision"], "b" * 40)

        second = global_refresh(first_result, revision="d" * 40, status="partial")
        repo = second["repositories"][2]
        repo["access"] = "failed"
        repo["observed_head"] = None
        repo["freshness"]["status"] = "failed"
        second_result, successful, _ = repository_watchdog.apply_watchdog_transition(
            self.registry,
            first_result,
            second,
            observed_at="2026-10-14T16:50:00Z",
        )
        self.assertFalse(successful)
        self.assertEqual(second_result["watchdog"]["status"], "WATCHDOG-STALE")
        open_watchdog = [
            item for item in second_result["drift"]
            if item["id"] == "repository-watchdog-stale" and item["status"] == "open"
        ]
        self.assertEqual(len(open_watchdog), 1)

    def test_bootstrap_stale_never_becomes_green_on_failed_attempt(self):
        prior = stale_bootstrap(self.state)
        refreshed = global_refresh(prior, status="partial")
        refreshed["repositories"][1]["access"] = "unavailable"
        refreshed["repositories"][1]["observed_head"] = None
        refreshed["repositories"][1]["freshness"]["status"] = "unknown"
        result, successful, _ = repository_watchdog.apply_watchdog_transition(
            self.registry,
            prior,
            refreshed,
            observed_at="2026-10-12T16:50:00Z",
        )
        self.assertFalse(successful)
        self.assertEqual(result["watchdog"]["status"], "WATCHDOG-STALE")

    def test_missed_daily_window_plus_failed_attempt_is_stale(self):
        current, _, _ = repository_watchdog.apply_watchdog_transition(
            self.registry,
            self.state,
            global_refresh(self.state, revision="b" * 40),
            observed_at="2026-10-12T00:00:00Z",
        )
        refreshed = global_refresh(current, revision="c" * 40, status="partial")
        refreshed["repositories"][1]["access"] = "failed"
        refreshed["repositories"][1]["observed_head"] = None
        refreshed["repositories"][1]["freshness"]["status"] = "failed"
        result, successful, _ = repository_watchdog.apply_watchdog_transition(
            self.registry,
            current,
            refreshed,
            observed_at="2026-10-14T00:00:00Z",
        )
        self.assertFalse(successful)
        self.assertEqual(repository_watchdog.missed_expected_scans(current, "2026-10-14T00:00:00Z"), 1)
        self.assertEqual(result["watchdog"]["status"], "WATCHDOG-STALE")

    def test_current_age_check_fails_after_two_expected_daily_windows(self):
        current, successful, failures = repository_watchdog.apply_watchdog_transition(
            self.registry,
            self.state,
            global_refresh(self.state, revision="b" * 40),
            observed_at="2026-10-12T00:00:00Z",
        )
        self.assertTrue(successful)
        self.assertEqual(failures, [])
        ok, _ = repository_watchdog.watchdog_is_current(current, now="2026-10-13T23:59:59Z")
        self.assertTrue(ok)
        ok, reason = repository_watchdog.watchdog_is_current(current, now="2026-10-14T00:00:00Z")
        self.assertFalse(ok)
        self.assertIn("two expected daily windows", reason)

    def test_scoped_refresh_metadata_does_not_erase_successful_watchdog_heartbeat(self):
        current, _, _ = repository_watchdog.apply_watchdog_transition(
            self.registry,
            self.state,
            global_refresh(self.state, revision="b" * 40),
            observed_at="2026-10-12T00:00:00Z",
        )
        scoped = copy.deepcopy(current)
        scoped["refresh"]["mode"] = "scoped-refresh"
        scoped["refresh"]["scope"] = "Core"
        scoped["refresh"]["evidence_revision"] = "c" * 40
        scoped["refresh"]["last_scoped_refresh"] = {
            "scope": "Core",
            "status": "complete",
            "evidence_revision": "c" * 40,
            "observed_at": None,
        }
        self.assertEqual(scoped["watchdog"], current["watchdog"])
        self.assertEqual(scoped["refresh"]["last_full_refresh"]["evidence_revision"], "b" * 40)

    def test_failure_collection_covers_repository_descriptor_and_pin_surfaces(self):
        value = global_refresh(self.state, status="partial")
        value["repositories"][1]["access"] = "unavailable"
        value["repositories"][2]["descriptor"]["status"] = "missing"
        value["repositories"][2]["descriptor"]["revision"] = None
        value["repositories"][2]["descriptor"]["release_status"] = None
        value["repositories"][2]["descriptor"]["blob_sha"] = None
        value["repositories"][2]["distribution_pin"]["status"] = "failed"
        failures = repository_watchdog.collect_watchdog_failures(value)
        surfaces = {(item["repository_id"], item["surface"], item["kind"]) for item in failures}
        self.assertIn((value["repositories"][1]["repository_id"], "repository", "unavailable"), surfaces)
        self.assertIn((value["repositories"][2]["repository_id"], "descriptor", "failed"), surfaces)
        self.assertIn((value["repositories"][2]["repository_id"], "distribution-pin", "failed"), surfaces)

    def test_unrelated_drift_is_preserved(self):
        before = {
            item["id"]: item["status"]
            for item in self.state["drift"]
            if not item["id"].startswith("repository-watchdog-")
        }
        result, _, _ = repository_watchdog.apply_watchdog_transition(
            self.registry,
            self.state,
            global_refresh(self.state),
            observed_at="2026-10-12T16:50:00Z",
        )
        after = {
            item["id"]: item["status"]
            for item in result["drift"]
            if not item["id"].startswith("repository-watchdog-")
        }
        self.assertEqual(after, before)

    def test_non_global_refresh_is_rejected(self):
        refreshed = copy.deepcopy(self.state)
        refreshed["refresh"]["mode"] = "scoped-refresh"
        refreshed["refresh"]["scope"] = "Core"
        refreshed["refresh"]["last_scoped_refresh"]["scope"] = "Core"
        for repo in refreshed["repositories"]:
            repo["freshness"]["scope"] = "Core"
        with self.assertRaises(ValueError):
            repository_watchdog.apply_watchdog_transition(
                self.registry,
                self.state,
                refreshed,
                observed_at="2026-10-12T16:50:00Z",
            )


if __name__ == "__main__":
    unittest.main()
