import copy
import importlib.util
import json
import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
REGISTRY = json.loads((ROOT / "governance" / "repository-registry.json").read_text(encoding="utf-8"))
STATE = json.loads((ROOT / "governance" / "repository-state.json").read_text(encoding="utf-8"))
LEDGER = ROOT / "docs" / "REPOSITORY-STATE-LEDGER.md"
SCRIPT = ROOT / "scripts" / "refresh_repository_state.py"

spec = importlib.util.spec_from_file_location("state_projection", SCRIPT)
state_projection = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(state_projection)


class RepositoryStateProjectionTests(unittest.TestCase):
    def test_render_is_deterministic(self):
        first = state_projection.render_ledger(copy.deepcopy(REGISTRY), copy.deepcopy(STATE))
        second = state_projection.render_ledger(copy.deepcopy(REGISTRY), copy.deepcopy(STATE))
        self.assertEqual(first, second)

    def test_committed_ledger_is_exact_generated_projection(self):
        expected = state_projection.render_ledger(REGISTRY, STATE)
        self.assertEqual(LEDGER.read_text(encoding="utf-8"), expected)

    def test_ledger_declares_it_is_generated_and_non_authoritative(self):
        rendered = state_projection.render_ledger(REGISTRY, STATE)
        self.assertIn("GENERATED FILE. Do not hand-edit.", rendered)
        self.assertIn("This ledger is a projection only and is never machine authority.", rendered)

    def test_dynamic_state_change_changes_projection(self):
        state = copy.deepcopy(STATE)
        state["repositories"][2]["observed_head"] = "f" * 40
        rendered = state_projection.render_ledger(REGISTRY, state)
        self.assertIn("`ffffffffffff`", rendered)

    def test_static_name_is_resolved_from_registry_not_state(self):
        registry = copy.deepcopy(REGISTRY)
        registry["repositories"][2]["repository_full_name"] = "aiverse-filmmakers/AI-Verse-OS-Renamed"
        rendered = state_projection.render_ledger(registry, STATE)
        self.assertIn("AI-Verse-OS-Renamed", rendered)
        self.assertNotIn("repository_full_name", STATE["repositories"][2])


if __name__ == "__main__":
    unittest.main()
