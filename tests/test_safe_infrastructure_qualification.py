import copy
import importlib.util
import json
import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
VALID = ROOT / "contracts" / "examples" / "safe-infrastructure-qualification.valid.json"
SCHEMA = ROOT / "contracts" / "safe-infrastructure-qualification-v1.schema.json"
VALIDATOR_PATH = ROOT / "scripts" / "validate_safe_infrastructure_qualification.py"

spec = importlib.util.spec_from_file_location("safe_infra_qualification_validator", VALIDATOR_PATH)
validator = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(validator)


class SafeInfrastructureQualificationTests(unittest.TestCase):
    def setUp(self):
        self.valid = json.loads(VALID.read_text(encoding="utf-8"))

    def assertInvalid(self, payload, contains):
        errors = validator.validate_qualification(payload)
        self.assertTrue(errors, "qualification unexpectedly validated")
        self.assertTrue(any(contains in error for error in errors), errors)

    def test_schema_is_versioned_and_closed(self):
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        self.assertEqual(
            schema["properties"]["schema_version"]["const"],
            "ai-verse.safe-infrastructure-qualification/v1",
        )
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(
            set(schema["properties"]["sections"]["required"]),
            {"convergence", "restore", "doctor", "member_ux"},
        )

    def test_valid_fixture_passes(self):
        self.assertEqual(validator.validate_qualification(self.valid), [])

    def test_overall_pass_requires_every_section_pass(self):
        payload = copy.deepcopy(self.valid)
        payload["sections"]["restore"]["status"] = "FAIL"
        self.assertInvalid(payload, "cannot PASS when restore is not PASS")

    def test_convergence_pass_requires_target_equivalence_and_preservation(self):
        payload = copy.deepcopy(self.valid)
        payload["sections"]["convergence"]["user_state_preserved"] = False
        self.assertInvalid(payload, "user_state_preserved")

    def test_restore_pass_requires_exact_software_and_retained_target(self):
        payload = copy.deepcopy(self.valid)
        payload["sections"]["restore"]["software_exact"] = False
        payload["sections"]["restore"]["retained_target_survived"] = False
        self.assertInvalid(payload, "software_exact")
        self.assertInvalid(payload, "retained_target_survived")

    def test_pass_section_cannot_rely_on_failed_evidence(self):
        payload = copy.deepcopy(self.valid)
        payload["sections"]["convergence"]["evidence"][0]["result"] = "FAIL"
        self.assertInvalid(payload, "cannot rely on failed evidence")

    def test_doctor_requires_every_required_owner_result(self):
        payload = copy.deepcopy(self.valid)
        payload["sections"]["doctor"]["owner_results"] = payload["sections"]["doctor"]["owner_results"][:-1]
        self.assertInvalid(payload, "missing required owner result")

    def test_doctor_duplicate_owner_results_fail_closed(self):
        payload = copy.deepcopy(self.valid)
        payload["sections"]["doctor"]["owner_results"].append(
            {"owner": "ai-verse-os", "status": "PASS"}
        )
        self.assertInvalid(payload, "duplicate owner result")

    def test_doctor_pass_cannot_hide_required_owner_failure(self):
        payload = copy.deepcopy(self.valid)
        payload["sections"]["doctor"]["owner_results"][0]["status"] = "FAIL"
        self.assertInvalid(payload, "required owner ai-verse-os must PASS")

    def test_doctor_injected_required_owner_failure_must_fail_aggregate(self):
        payload = copy.deepcopy(self.valid)
        payload["sections"]["doctor"]["failure_injection"]["aggregate_ok"] = True
        self.assertInvalid(payload, "must make aggregate_ok=false")

    def test_doctor_failure_injection_must_name_required_owner(self):
        payload = copy.deepcopy(self.valid)
        payload["sections"]["doctor"]["failure_injection"]["injected_owner"] = "not-a-required-owner"
        self.assertInvalid(payload, "must name a required owner")

    def test_doctor_must_remain_read_only(self):
        payload = copy.deepcopy(self.valid)
        payload["sections"]["doctor"]["read_only"] = False
        self.assertInvalid(payload, "doctor must remain read-only")

    def test_default_summary_rejects_git_sha(self):
        payload = copy.deepcopy(self.valid)
        payload["sections"]["member_ux"]["default_summary"] += "\nRevision: " + "a" * 40
        self.assertInvalid(payload, "must not expose Git SHA")

    def test_default_summary_rejects_internal_path_and_generation_jargon(self):
        payload = copy.deepcopy(self.valid)
        payload["sections"]["member_ux"]["default_summary"] = (
            "Move workspaces/demo after infrastructure generation 3."
        )
        self.assertInvalid(payload, "internal architecture jargon")

    def test_default_summary_is_bounded_for_small_screen(self):
        payload = copy.deepcopy(self.valid)
        payload["sections"]["member_ux"]["default_summary"] = "\n".join(
            f"Line {index}" for index in range(13)
        )
        self.assertInvalid(payload, "exceeds 12 non-empty lines")

    def test_contract_ids_are_imported_not_replaced(self):
        payload = copy.deepcopy(self.valid)
        payload["identity_contract"] = "invented.identity/v1"
        self.assertInvalid(payload, "identity_contract")
        payload = copy.deepcopy(self.valid)
        payload["upgrade_contract"] = "invented.upgrade/v1"
        self.assertInvalid(payload, "upgrade_contract")

    def test_failure_record_is_allowed_when_overall_is_fail(self):
        payload = copy.deepcopy(self.valid)
        payload["overall"] = "FAIL"
        payload["sections"]["restore"]["status"] = "FAIL"
        payload["sections"]["restore"]["covered_state_exact"] = False
        payload["sections"]["restore"]["evidence"][0]["result"] = "FAIL"
        self.assertEqual(validator.validate_qualification(payload), [])


if __name__ == "__main__":
    unittest.main()
