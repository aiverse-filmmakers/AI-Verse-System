import json
import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
BLUEPRINT = ROOT / "docs" / "FINAL-AI-VERSE-BLUEPRINT.md"
RECONCILIATION = ROOT / "docs" / "REPOSITORY-TRUTH-RECONCILIATION-2026-10-12.md"
STATE = ROOT / "governance" / "repository-state.json"


class SystemTruthReconciliationTests(unittest.TestCase):
    def setUp(self):
        self.blueprint = BLUEPRINT.read_text(encoding="utf-8")
        self.reconciliation = RECONCILIATION.read_text(encoding="utf-8")
        self.state = json.loads(STATE.read_text(encoding="utf-8"))

    def test_blueprint_records_accepted_purpose_v1_without_second_truth_store(self):
        required = [
            "core-purpose-context-public-beta-2026-10-09",
            "COMPLETE / ACCEPTED / CORE ADMITTED",
            "VALUE PROVEN",
            "owner-backed",
            "read-only",
            "operator",
            "workspace:<id>",
            "no stale fallback",
            "no Memory authority promotion",
            "no second Purpose truth store",
        ]
        for phrase in required:
            self.assertIn(phrase, self.blueprint, phrase)

    def test_blueprint_no_longer_describes_purpose_as_future_intent(self):
        self.assertNotIn(
            "This is an **INTENDED derived context layer**, not a new component and not a new canonical owner.",
            self.blueprint,
        )
        self.assertNotIn("### EARLY P1: Purpose Context / Telos-inspired deep context", self.blueprint)

    def test_blueprint_preserves_evidence_first_reconciliation_boundary(self):
        required = [
            "Accepted Purpose ancestry does not by itself prove exact owner acceptance of every later descendant revision.",
            "newer branch movement is not acceptance evidence merely because it is newer",
            "docs/PURPOSE-CONTEXT-EXECUTION-STATE.md",
            "docs/REPOSITORY-TRUTH-RECONCILIATION-2026-10-12.md",
        ]
        for phrase in required:
            self.assertIn(phrase, self.blueprint, phrase)

    def test_reconciliation_defers_unowned_future_slice_drift(self):
        required = [
            "core-owner-acceptance-exact-ref-gap",
            "CARRY BLOCKING",
            "core-maintainer-handoff-uneven",
            "distribution-adapter-compatibility-shadow-risk",
            "compact-release-receipt-not-yet-implemented",
        ]
        for phrase in required:
            self.assertIn(phrase, self.reconciliation, phrase)

    def test_current_owner_acceptance_gap_is_resolved_by_phase4_handoff(self):
        matches = [
            item for item in self.state["drift"]
            if item["id"] == "core-owner-acceptance-exact-ref-gap"
        ]
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0]["status"], "resolved")
        self.assertEqual(matches[0]["severity"], "BLOCKING")
        self.assertEqual(matches[0]["scope"], "Core")
        self.assertIn("Resolved in Slice 4.2", matches[0]["reason"])

    def test_later_slice_drift_remains_open_after_core_owner_handoff(self):
        by_id = {item["id"]: item for item in self.state["drift"]}
        self.assertEqual(by_id["distribution-adapter-compatibility-shadow-risk"]["status"], "open")
        self.assertEqual(by_id["compact-release-receipt-not-yet-implemented"]["status"], "open")


if __name__ == "__main__":
    unittest.main()
