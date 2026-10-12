from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = ROOT / "scripts" / "validate_durable_entity_reference.py"
SCHEMA_PATH = ROOT / "contracts" / "durable-entity-reference-v1.schema.json"
EXAMPLES_PATH = ROOT / "contracts" / "examples" / "durable-entity-references.valid.json"
CONTRACT_PATH = ROOT / "docs" / "DURABLE-IDENTITY-AND-CANONICAL-REFERENCE-CONTRACT.md"

spec = importlib.util.spec_from_file_location("durable_entity_reference_validator", VALIDATOR_PATH)
assert spec is not None and spec.loader is not None
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class DurableEntityReferenceContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        cls.examples = json.loads(EXAMPLES_PATH.read_text(encoding="utf-8"))
        cls.contract = CONTRACT_PATH.read_text(encoding="utf-8")

    def test_schema_is_minimal_v1_envelope(self) -> None:
        self.assertEqual(self.schema["required"], ["owner", "kind", "id"])
        self.assertEqual(set(self.schema["properties"]), {"owner", "kind", "id", "scope"})
        self.assertFalse(self.schema["additionalProperties"])
        self.assertNotIn("version", self.schema["properties"])
        self.assertNotIn("display_name", self.schema["properties"])
        self.assertNotIn("path", self.schema["properties"])

    def test_required_owner_examples_are_valid(self) -> None:
        expected = {
            "workspace",
            "skill_capability",
            "brain_object",
            "automation",
            "bot",
            "connection",
            "data_record",
            "memory_record",
        }
        self.assertEqual(set(self.examples), expected)
        for name, reference in self.examples.items():
            with self.subTest(name=name):
                self.assertEqual(validator.validate_reference(reference), [])

    def test_scope_is_optional(self) -> None:
        reference = {"owner": "owner-x", "kind": "thing", "id": "opaque-id"}
        self.assertEqual(validator.validate_reference(reference), [])

    def test_owner_specific_ids_remain_opaque(self) -> None:
        reference = {
            "owner": "owner-x",
            "kind": "thing",
            "id": "owner/native:id/format#v7",
            "scope": "owner-defined:scope/value",
        }
        self.assertEqual(validator.validate_reference(reference), [])

    def test_missing_required_identity_fails_closed(self) -> None:
        errors = validator.validate_reference({"owner": "ai-verse-os", "kind": "workspace"})
        self.assertTrue(any("missing keys: id" in error for error in errors))

    def test_empty_identity_field_fails_closed(self) -> None:
        errors = validator.validate_reference({"owner": "", "kind": "workspace", "id": "film"})
        self.assertTrue(any("owner" in error and "non-empty" in error for error in errors))

    def test_extra_representation_fields_are_rejected(self) -> None:
        reference = {
            "owner": "ai-verse-os",
            "kind": "workspace",
            "id": "film",
            "display_name": "Film Workspace",
            "path": "workspaces/film",
            "version": 7,
        }
        errors = validator.validate_reference(reference)
        self.assertTrue(any("unknown keys" in error for error in errors))
        self.assertTrue(any("display_name" in error for error in errors))
        self.assertTrue(any("path" in error for error in errors))
        self.assertTrue(any("version" in error for error in errors))

    def test_ambiguous_candidate_shape_is_not_a_valid_reference(self) -> None:
        reference = {
            "owner": "ai-verse-os",
            "kind": "workspace",
            "id": "film",
            "candidates": ["film", "film-copy"],
        }
        errors = validator.validate_reference(reference)
        self.assertTrue(any("candidates" in error for error in errors))
        self.assertIn("Ambiguous, malformed, duplicate or conflicting identity evidence MUST fail closed", self.contract)
        self.assertIn("accept only one unambiguous canonical result", self.contract)

    def test_workspace_and_skill_constraints_remain_normative(self) -> None:
        self.assertIn("workspaces/<workspace-id>", self.contract)
        self.assertIn("aiverse-skills:<name>", self.contract)
        self.assertIn("A cross-provider move or re-scope MUST NOT be assumed to preserve qualified identity", self.contract)

    def test_contract_forbids_global_identity_registry(self) -> None:
        self.assertIn("It does not become a global ID allocator", self.contract)
        self.assertIn("a central entity registry", self.contract)


if __name__ == "__main__":
    unittest.main()
