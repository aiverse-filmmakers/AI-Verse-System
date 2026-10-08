import json
import unittest
from pathlib import Path

from scripts.validate_purpose_context_value_gate import validate


ROOT = Path(__file__).resolve().parents[1]
GATE = ROOT / "contracts" / "purpose-context-value-gate.json"


class PurposeContextValueGateTests(unittest.TestCase):
    def test_committed_gate_is_valid_and_allows_phase_8_only_for_value_proven(self):
        payload = json.loads(GATE.read_text(encoding="utf-8"))
        self.assertEqual(validate(payload), [])
        self.assertEqual(payload["outcome"], "VALUE PROVEN")
        self.assertIs(payload["phase_8_allowed"], True)

    def test_phase_8_is_blocked_for_partial_or_not_proven(self):
        base = json.loads(GATE.read_text(encoding="utf-8"))
        for outcome in ("PARTIALLY PROVEN", "NOT PROVEN"):
            payload = dict(base)
            payload["outcome"] = outcome
            payload["phase_8_allowed"] = True
            errors = validate(payload)
            self.assertTrue(any("phase_8_allowed" in error for error in errors), outcome)

    def test_value_proven_fails_if_core_safety_or_value_proof_is_missing(self):
        base = json.loads(GATE.read_text(encoding="utf-8"))
        cases = [
            ("prioritization_improvement", False),
            ("trivial_task_zero_purpose_reads", False),
            ("purpose_envelope_within_16384_bytes", False),
            ("workspace_isolation_regression", True),
            ("authority_regression", True),
        ]
        for key, value in cases:
            with self.subTest(key=key):
                payload = json.loads(json.dumps(base))
                payload["proofs"][key] = value
                errors = validate(payload)
                self.assertTrue(any(key in error for error in errors), errors)

    def test_unmeasured_provider_metrics_do_not_get_coerced_to_zero_or_true(self):
        payload = json.loads(GATE.read_text(encoding="utf-8"))
        self.assertIs(payload["proofs"]["provider_cost_measured"], False)
        self.assertIs(payload["proofs"]["production_model_output_measured"], False)
        self.assertGreaterEqual(len(payload["measurement_caveats"]), 2)


if __name__ == "__main__":
    unittest.main()
