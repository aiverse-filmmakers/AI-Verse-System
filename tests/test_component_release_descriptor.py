import copy
import importlib.util
import json
import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
VALID = ROOT / "contracts" / "examples" / "component-release-descriptor.valid.json"
VALID_INFRA = ROOT / "contracts" / "examples" / "component-release-descriptor.valid-infrastructure-upgrade.json"
INVALID_FLOATING = ROOT / "contracts" / "examples" / "component-release-descriptor.invalid-floating-ref.json"
SCHEMA = ROOT / "contracts" / "component-release-descriptor.schema.json"
VALIDATOR_PATH = ROOT / "scripts" / "validate_component_release_descriptor.py"

spec = importlib.util.spec_from_file_location("release_validator", VALIDATOR_PATH)
release_validator = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(release_validator)


class ComponentReleaseDescriptorTests(unittest.TestCase):
    def setUp(self):
        self.valid = json.loads(VALID.read_text(encoding="utf-8"))
        self.valid_infra = json.loads(VALID_INFRA.read_text(encoding="utf-8"))

    def assertInvalid(self, descriptor, contains):
        errors = release_validator.validate_descriptor(descriptor)
        self.assertTrue(errors, "descriptor unexpectedly validated")
        self.assertTrue(any(contains in error for error in errors), errors)

    def test_schema_json_is_well_formed_and_versioned(self):
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        self.assertEqual(schema["properties"]["schema_version"]["const"], "ai-verse.component-release/v1")
        self.assertEqual(schema["properties"]["revision"]["pattern"], "^[0-9a-f]{40}$")
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(
            schema["properties"]["migration"]["properties"]["infrastructure"]["$ref"],
            "#/$defs/infrastructure_upgrade",
        )
        self.assertEqual(
            schema["$defs"]["infrastructure_upgrade"]["properties"]["contract_version"]["const"],
            "ai-verse.infrastructure-upgrade/v1",
        )

    def test_legacy_valid_fixture_still_passes_without_infrastructure_block(self):
        self.assertEqual(release_validator.validate_descriptor(self.valid), [])

    def test_valid_infrastructure_upgrade_fixture_passes(self):
        self.assertEqual(release_validator.validate_descriptor(self.valid_infra), [])

    def test_floating_revision_fails(self):
        descriptor = json.loads(INVALID_FLOATING.read_text(encoding="utf-8"))
        self.assertInvalid(descriptor, "$.revision")

    def test_evidence_must_match_exact_revision(self):
        descriptor = copy.deepcopy(self.valid)
        descriptor["evidence"]["ci"][0]["revision"] = "f" * 40
        self.assertInvalid(descriptor, "must equal descriptor revision")

    def test_live_health_truth_is_forbidden(self):
        descriptor = copy.deepcopy(self.valid)
        descriptor["semantics"]["live_health_truth"] = True
        self.assertInvalid(descriptor, "live_health_truth")

    def test_unknown_top_level_health_field_is_forbidden(self):
        descriptor = copy.deepcopy(self.valid)
        descriptor["healthy"] = True
        self.assertInvalid(descriptor, "unknown keys")

    def test_authority_expansion_is_forbidden(self):
        descriptor = copy.deepcopy(self.valid)
        descriptor["authority"]["grants_permissions"] = True
        self.assertInvalid(descriptor, "grants_permissions")

    def test_update_preservation_claim_must_be_true(self):
        descriptor = copy.deepcopy(self.valid)
        descriptor["state"]["preserve_on_update"] = False
        self.assertInvalid(descriptor, "preserve_on_update")

    def test_explicit_migration_flags_must_agree(self):
        descriptor = copy.deepcopy(self.valid)
        descriptor["migration"]["compatibility"] = "explicit-migration"
        descriptor["migration"]["requires_explicit_migration"] = False
        self.assertInvalid(descriptor, "explicit-migration requires")

    def test_blocked_release_cannot_be_accepted(self):
        descriptor = copy.deepcopy(self.valid)
        descriptor["migration"]["compatibility"] = "blocked"
        descriptor["migration"]["from_versions"] = []
        descriptor["release_status"] = "accepted"
        self.assertInvalid(descriptor, "cannot have release_status=accepted")

    def test_evidence_arrays_are_required(self):
        descriptor = copy.deepcopy(self.valid)
        descriptor["evidence"]["acceptance"] = []
        self.assertInvalid(descriptor, "expected non-empty evidence array")

    def test_infrastructure_owner_must_equal_component_owner(self):
        descriptor = copy.deepcopy(self.valid_infra)
        descriptor["migration"]["infrastructure"]["owner"] = "ai-verse-other"
        self.assertInvalid(descriptor, "must equal descriptor component_id")

    def test_recipe_target_revision_must_equal_descriptor_revision(self):
        descriptor = copy.deepcopy(self.valid_infra)
        descriptor["migration"]["infrastructure"]["recipes"][0]["target_binding"]["component_revision"] = "f" * 40
        self.assertInvalid(descriptor, "must equal descriptor revision")

    def test_free_form_shell_command_is_not_a_valid_owner_operation(self):
        descriptor = copy.deepcopy(self.valid_infra)
        descriptor["migration"]["infrastructure"]["recipes"][0]["apply_operation"] = "mv old new && rm -rf old"
        self.assertInvalid(descriptor, "without whitespace or command syntax")

    def test_optional_required_are_the_only_executable_dispositions(self):
        descriptor = copy.deepcopy(self.valid_infra)
        descriptor["migration"]["infrastructure"]["recipes"][0]["disposition"] = "BLOCKED/REVIEW"
        self.assertInvalid(descriptor, "expected OPTIONAL or REQUIRED")

    def test_no_match_must_fail_closed_to_blocked_review(self):
        descriptor = copy.deepcopy(self.valid_infra)
        descriptor["migration"]["infrastructure"]["no_match_disposition"] = "OPTIONAL"
        self.assertInvalid(descriptor, "must be BLOCKED/REVIEW")

    def test_duplicate_source_generation_is_rejected_as_ambiguous(self):
        descriptor = copy.deepcopy(self.valid_infra)
        descriptor["migration"]["infrastructure"]["recipes"][1]["from_generations"] = ["example-layout/v0"]
        self.assertInvalid(descriptor, "ambiguous paths are forbidden")

    def test_direct_recipe_must_reach_current_generation(self):
        descriptor = copy.deepcopy(self.valid_infra)
        descriptor["migration"]["infrastructure"]["recipes"][0]["to_generation"] = "example-layout/v2"
        self.assertInvalid(descriptor, "direct recipe must target current_generation")

    def test_current_generation_cannot_be_a_recipe_source(self):
        descriptor = copy.deepcopy(self.valid_infra)
        descriptor["migration"]["infrastructure"]["recipes"][0]["from_generations"] = ["example-layout/v3"]
        self.assertInvalid(descriptor, "current_generation cannot be a migration source")

    def test_dangling_chain_is_rejected(self):
        descriptor = copy.deepcopy(self.valid_infra)
        descriptor["migration"]["infrastructure"]["recipes"][1]["to_generation"] = "example-layout/v2-missing"
        self.assertInvalid(descriptor, "does not have a complete unique chain")

    def test_chain_cycle_is_rejected(self):
        descriptor = copy.deepcopy(self.valid_infra)
        descriptor["migration"]["infrastructure"]["recipes"][2]["to_generation"] = "example-layout/v1"
        self.assertInvalid(descriptor, "cycle detected")

    def test_whole_install_lkg_is_mandatory(self):
        descriptor = copy.deepcopy(self.valid_infra)
        descriptor["migration"]["infrastructure"]["recipes"][0]["recovery"]["whole_install_lkg_required"] = False
        self.assertInvalid(descriptor, "whole_install_lkg_required: must be true")

    def test_owner_checkpoint_requirement_must_match_descriptor_policy(self):
        descriptor = copy.deepcopy(self.valid_infra)
        descriptor["migration"]["checkpoint_policy"] = "not-required"
        self.assertInvalid(descriptor, "checkpoint_policy must be owner-evidence-required")

    def test_unsupported_checkpoint_policy_cannot_publish_recipes(self):
        descriptor = copy.deepcopy(self.valid_infra)
        descriptor["migration"]["checkpoint_policy"] = "unsupported"
        self.assertInvalid(descriptor, "recipes cannot be published")

    def test_recipe_must_be_idempotent(self):
        descriptor = copy.deepcopy(self.valid_infra)
        descriptor["migration"]["infrastructure"]["recipes"][0]["idempotent"] = False
        self.assertInvalid(descriptor, "idempotent: must be true")

    def test_idempotency_evidence_kind_must_exist_in_acceptance_evidence(self):
        descriptor = copy.deepcopy(self.valid_infra)
        descriptor["evidence"]["acceptance"] = [descriptor["evidence"]["acceptance"][0]]
        self.assertInvalid(descriptor, "must name passing descriptor acceptance evidence")

    def test_identity_contract_cannot_be_redefined_by_recipe(self):
        descriptor = copy.deepcopy(self.valid_infra)
        descriptor["migration"]["infrastructure"]["recipes"][0]["identity_contract"] = "example.identity/v1"
        self.assertInvalid(descriptor, "ai-verse.durable-identity-reference/v1")

    def test_required_reference_repair_needs_owner_operation(self):
        descriptor = copy.deepcopy(self.valid_infra)
        repair = descriptor["migration"]["infrastructure"]["recipes"][1]["reference_repair"]
        repair["operations"] = []
        self.assertInvalid(descriptor, "required repair needs at least one owner operation")

    def test_non_required_reference_repair_cannot_smuggle_operations(self):
        descriptor = copy.deepcopy(self.valid_infra)
        repair = descriptor["migration"]["infrastructure"]["recipes"][0]["reference_repair"]
        repair["operations"] = [
            {"owner": "ai-verse-example", "operation": "references.repair.unexpected"}
        ]
        self.assertInvalid(descriptor, "must be empty when repair is not required")

    def test_unknown_recipe_field_is_rejected(self):
        descriptor = copy.deepcopy(self.valid_infra)
        descriptor["migration"]["infrastructure"]["recipes"][0]["shell_command"] = "echo unsafe"
        self.assertInvalid(descriptor, "unknown keys")


if __name__ == "__main__":
    unittest.main()
