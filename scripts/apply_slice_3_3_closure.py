#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROADMAP = ROOT / "docs" / "DISTRIBUTION-SYSTEM-PROPAGATION-IMPLEMENTATION-PLAN.md"
WORKFLOW = ROOT / ".github" / "workflows" / "slice-3-3-close.yml"
SELF = Path(__file__)


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected exactly one match, found {count}")
    return text.replace(old, new, 1)


def main() -> None:
    text = ROADMAP.read_text(encoding="utf-8")

    old_header = '''**Program size:** 20 slices  
**Completed:** 9  
**Remaining:** 11  
**Overall progress:** 45.0%  
**Current execution phase:** Phase 3 - Build System self-checking machinery and synchronize current truth  
**Current phase progress:** 2/3 slices complete  
**Slices until next phase:** 1  
**Current slice:** 3.3 - Reconcile current System truth and known drift  
**Current slice status:** IN PROGRESS  
**Task progress:** 1/5  
**Next slice:** 4.1 - Extend/reuse Component Release Descriptor
'''
    new_header = '''**Program size:** 20 slices  
**Completed:** 10  
**Remaining:** 10  
**Overall progress:** 50.0%  
**Current execution phase:** Phase 4 - Integrate canonical component owners  
**Current phase progress:** 0/3 slices complete  
**Slices until next phase:** 3  
**Current slice:** 4.1 - Extend/reuse Component Release Descriptor  
**Current slice status:** NOT STARTED  
**Next slice:** 4.2 - Wave 1/Core maintainer handoff
'''
    text = replace_once(text, old_header, new_header, "roadmap header")

    text = replace_once(
        text,
        "**Current phase progress:** 2/3\n\n## Slice 3.1",
        "**Current phase progress:** 3/3\n\n## Slice 3.1",
        "phase 3 progress",
    )

    start = text.index("## Slice 3.3 - Reconcile current System truth and known drift")
    end = text.index("\n---\n\n# Phase 4 - Integrate canonical component owners", start)
    replacement = '''## Slice 3.3 - Reconcile current System truth and known drift

**Status:** COMPLETE  
**Dependencies:** 3.2  
**Tasks:** 5/5 complete

### Outcome

System truth was reconciled evidence-first using Purpose Context as the mandatory stale-document regression fixture. The living blueprint now reflects immutable accepted/admitted Purpose Context v1 truth instead of regressing accepted implementation to the older October 5 prose. Newer branch movement was not treated as acceptance by recency alone.

Only `purpose-context-blueprint-lag` was resolved. The exact-current-owner-acceptance gap remains `BLOCKING`; Core maintainer handoff and Distribution adapter shadow risk remain `WARNING`; compact release receipt remains `INFO`. No sibling repository, runtime behavior, release composition or member payload was changed.

### Evidence

- Slice start / boundary: `13700889f1bf37f3fdc5c576804f7aff39129471`
- Evidence-first reconciliation matrix: `df18f2d20ec65a65b93f9a323e0c1fa0d1301447`
- Purpose reconciliation regression coverage: `ffc72e88093a642d88ac04ca963427599694bb13`
- Exact-match workflow staging: `9401e825a510fdad822e76fc2902614336373ca7`
- Reconciled living blueprint + System changelog: `84320b46a964c22c16f35a68207d9e1a388bee8a`
- One-shot machinery removed: `3cd2340f62d4b04dc7b9dd8522ac590941f73272`
- Clean reconciliation validation: 100 tests passed on Python 3.11 and 3.13, live Core refresh passed.
- Repository State/ledger with Purpose drift resolved: `fe480e194a92e358f4ec914f458df9f3b8f1d2c0`
- Exact State CI: run `38283624914`, Python 3.11 and 3.13 passed, including live read-only Core refresh.
- Final closure State/ledger snapshot: direct child of this closure bookkeeping commit, changing only `governance/repository-state.json` and `docs/REPOSITORY-STATE-LEDGER.md`.

### Reconciliation laws proven

- stale System prose cannot regress accepted implementation;
- a newer branch head cannot become accepted truth merely because it is newer;
- immutable accepted/released evidence and ancestry determine reconciliation direction;
- System blueprint remains cross-component synthesis, not a duplicate component implementation spec;
- later-slice drift stays visible and is not silently pulled forward;
- Repository State remains the dynamic drift authority and ledger remains generated projection only.

No plan amendment was required.
'''
    text = text[:start] + replacement + text[end:]

    change_marker = "# Program Change Log\n\n"
    entry = '''## 2026-10-12 - Slice 3.3 and Phase 3 completed

- Reconciled the stale Purpose Context blueprint forward to accepted/admitted v1 evidence.
- Added durable reconciliation evidence and permanent regression coverage.
- Resolved only `purpose-context-blueprint-lag`; all later-slice drift remains visible.
- Pre-closure State/ledger `fe480e194a92e358f4ec914f458df9f3b8f1d2c0` passed Contract Validation run `38283624914`.
- Final exact-head State/ledger snapshot is the direct child of this closure commit.
- Phase 3 is complete at 3/3 slices; program progress is 10/20, 50.0%.
- No protected roadmap change and no plan amendment.

'''
    text = replace_once(text, change_marker, change_marker + entry, "change log marker")

    pointer_start = text.index("# Current execution pointer")
    pointer = '''# Current execution pointer

**Completed:** 10/20  
**Overall:** 50.0%  
**Phase:** Phase 4 - Integrate canonical component owners  
**Phase progress:** 0/3  
**Until Phase 5:** 3 slices  
**Current slice:** Slice 4.1 - Extend/reuse Component Release Descriptor (`NOT STARTED`)  
**Next:** start Slice 4.1 with fresh State/owner-descriptor/contract inspection and exact-ref evidence  
**Blockers/drift/amendments:** Core exact-owner-acceptance gap BLOCKING; Core maintainer handoff WARNING; Distribution adapter shadow-risk WARNING; compact release receipt INFO; watchdog CURRENT; Purpose blueprint lag RESOLVED. No plan amendment required.
'''
    text = text[:pointer_start] + pointer

    ROADMAP.write_text(text, encoding="utf-8")
    if WORKFLOW.exists():
        WORKFLOW.unlink()
    if SELF.exists():
        SELF.unlink()


if __name__ == "__main__":
    main()
