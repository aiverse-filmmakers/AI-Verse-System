import copy
import importlib.util
import json
import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "governance" / "repository-registry.json"
SCHEMA = ROOT / "contracts" / "repository-registry.schema.json"
VALIDATOR_PATH = ROOT / "scripts" / "validate_repository_registry.py"

spec = importlib.util.spec_from_file_location("registry_validator", VALIDATOR_PATH)
registry_validator = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(registry_validator)


class RepositoryRegistryTests(unittest.TestCase):
    def setUp(self):
        self.registry = json.loads(REGISTRY.read_text(encoding="utf-8"))

    def assertInvalid(self, registry, contains):
        errors = registry_validator.validate_registry(registry)
        self.assertTrue(errors, "registry unexpectedly validated")
        self.assertTrue(any(contains in error for error in errors), errors)

    def test_schema_json_is_well_formed_and_versioned(self):
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        self.assertEqual(schema["properties"]["schema_version"]["const"], "ai-verse.repository-registry/v1")
        self.assertEqual(schema["properties"]["admission_policy"]["properties"]["identity_key"]["const"], "repository_id")
        self.assertEqual(
            schema["properties"]["admission_policy"]["properties"]["unregistered_first_class_release"]["const"],
            "block",
        )
        self.assertFalse(schema["additionalProperties"])

    def test_registered_wave1_to_wave3_registry_passes(self):
        self.assertEqual(registry_validator.validate_registry(self.registry), [])
        self.assertEqual(len(self.registry["repositories"]), 14)
        self.assertEqual(
            {entry["repository_id"] for entry in self.registry["repositories"]},
            {
                1367664026,
                1350081263,
                1361862361,
                1362233598,
                1361910454,
                1362243580,
                1364457521,
                1368762130,
                1368762786,
                1362278774,
                1368748835,
                1364458279,
                1362252045,
                1364456634,
            },
        )
        apps = next(entry for entry in self.registry["repositories"] if entry["component_id"] == "ai-verse-apps")
        self.assertEqual(apps["lifecycle"], "experimental")
        self.assertEqual(apps["rollout_wave"], 3)
        self.assertEqual(apps["release_profiles"], [])
        self.assertFalse(apps["distribution_ships"])
        self.assertIsNone(apps["component_release_descriptor_path"])
        self.assertEqual(apps["surface_classification"], "governance")

    def test_repository_name_can_change_without_changing_identity(self):
        registry = copy.deepcopy(self.registry)
        os_entry = next(entry for entry in registry["repositories"] if entry["component_id"] == "ai-verse-os")
        stable_id = os_entry["repository_id"]
        os_entry["repository_full_name"] = "aiverse-filmmakers/AI-Verse-OS-Renamed"
        self.assertEqual(os_entry["repository_id"], stable_id)
        self.assertEqual(registry_validator.validate_registry(registry), [])

    def test_duplicate_stable_repository_id_fails(self):
        registry = copy.deepcopy(self.registry)
        registry["repositories"][1]["repository_id"] = registry["repositories"][0]["repository_id"]
        self.assertInvalid(registry, "duplicate stable repository ID")

    def test_duplicate_component_id_fails(self):
        registry = copy.deepcopy(self.registry)
        registry["repositories"][1]["component_id"] = registry["repositories"][0]["component_id"]
        self.assertInvalid(registry, "duplicate canonical component id")

    def test_dynamic_state_field_is_forbidden(self):
        registry = copy.deepcopy(self.registry)
        registry["repositories"][2]["live_head"] = "f" * 40
        self.assertInvalid(registry, "unknown keys")

    def test_shipped_component_requires_descriptor(self):
        registry = copy.deepcopy(self.registry)
        os_entry = next(entry for entry in registry["repositories"] if entry["component_id"] == "ai-verse-os")
        os_entry["component_release_descriptor_path"] = None
        self.assertInvalid(registry, "requires component release descriptor path")

    def test_shipped_component_requires_release_profile(self):
        registry = copy.deepcopy(self.registry)
        os_entry = next(entry for entry in registry["repositories"] if entry["component_id"] == "ai-verse-os")
        os_entry["release_profiles"] = []
        self.assertInvalid(registry, "requires at least one release profile")

    def test_shipped_component_requires_component_native_acceptance(self):
        registry = copy.deepcopy(self.registry)
        os_entry = next(entry for entry in registry["repositories"] if entry["component_id"] == "ai-verse-os")
        os_entry["owner_acceptance"]["kind"] = "distribution-native"
        self.assertInvalid(registry, "requires component-native owner acceptance")

    def test_unregistered_first_class_release_policy_is_fail_closed(self):
        registry = copy.deepcopy(self.registry)
        registry["admission_policy"]["unregistered_first_class_release"] = "allow"
        self.assertInvalid(registry, "must be block")

    def test_distribution_cannot_be_registry_authority(self):
        registry = copy.deepcopy(self.registry)
        registry["admission_policy"]["distribution_registry_authority"] = True
        self.assertInvalid(registry, "must be false")

    def test_non_runtime_control_plane_cannot_publish_component_descriptor(self):
        registry = copy.deepcopy(self.registry)
        system = next(entry for entry in registry["repositories"] if entry["component_id"] == "ai-verse-system")
        system["component_release_descriptor_path"] = "release/component-release.json"
        self.assertInvalid(registry, "must not declare component release descriptor")

    def test_declared_compatibility_dependency_must_be_registered(self):
        registry = copy.deepcopy(self.registry)
        os_entry = next(entry for entry in registry["repositories"] if entry["component_id"] == "ai-verse-os")
        os_entry["direct_compatibility_dependencies"] = ["ai-verse-not-registered"]
        self.assertInvalid(registry, "unregistered component dependency")


if __name__ == "__main__":
    unittest.main()
