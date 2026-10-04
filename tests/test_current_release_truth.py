import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
TRACKER = (ROOT / "docs" / "PUBLIC-BETA-TRACKER.md").read_text(encoding="utf-8")
ACCEPTED_REVISIONS = (
    "924a21a3dc1094d0fb6cc422f55fdfc714634e4d",
    "6f986e8d06c7f9c069fbf05aa92ae7b7a1af9bf4",
    "406b14fb4398eb1b16dd5f30e50520e8c3540972",
    "71264af6b2b9a575812fe18858d75a54ea2ff545",
    "8edde7dca5afa34e300130cc6b8ee2b4170ad40f",
    "46c15ee58b028dd7fb8b310327ea705ef618805e",
    "caaed83b98026dd955640fc015d181529b91a1c6",
    "c600e2bc014351a61e1c0e2673fc63f5d5fa54ec",
    "23b7b8ecbc9d9ef267f5e10449f785eb11107dd4",
)


class CurrentReleaseTruthTests(unittest.TestCase):
    def test_tracker_contains_exact_accepted_owner_refs(self):
        for revision in ACCEPTED_REVISIONS:
            self.assertIn(revision, TRACKER, revision)

    def test_gateway_evidence_record_exists(self):
        gateway = ROOT / "components" / "ai-verse-gateway"
        for name in ("COMPONENT-SPEC.md", "SOURCE-MAP.md", "QC.md"):
            self.assertTrue((gateway / name).is_file(), name)


if __name__ == "__main__":
    unittest.main()
