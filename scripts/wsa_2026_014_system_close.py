from pathlib import Path

tracker_path = Path("docs/public-beta-audit/repairs/REPAIR-EXECUTION-TRACKER-2026-09-17.md")
register_path = Path("docs/public-beta-audit/findings/FINDING-REGISTER.md")


def one(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected one occurrence, found {count}")
    return text.replace(old, new, 1)


tracker = tracker_path.read_text(encoding="utf-8")
tracker = one(
    tracker,
    "**Current active finding:** `WSA-2026-014`",
    "**Current active finding:** `WSA-2026-025`",
    "tracker active finding",
)
tracker = one(
    tracker,
    "| R3.6 | WSA-2026-014 Memory migration handoff atomicity | AI-Verse-Memory | **ACTIVE** |",
    "| R3.6 | WSA-2026-014 Memory migration handoff atomicity | AI-Verse-Memory | **CLOSED** |",
    "tracker R3.6 row",
)
tracker = one(
    tracker,
    "| R3.7 | WSA-2026-025 Token pricing transactionality | ai-verse-token | PENDING |",
    "| R3.7 | WSA-2026-025 Token pricing transactionality | ai-verse-token | **ACTIVE** |",
    "tracker R3.7 row",
)
tracker = one(
    tracker,
    "**R3 progress: 5 / 10 CLOSED = 50%.**",
    "**R3 progress: 6 / 10 CLOSED = 60%.**",
    "tracker R3 progress",
)
tracker = one(
    tracker,
    "- R3: 10 findings, 5 remaining",
    "- R3: 10 findings, 4 remaining",
    "tracker R3 remaining",
)
ledger_anchor = "| R3.5 | WSA-2026-052 | OS | #46 | `9effe3869a87fb2c11287ae4821f93620abcc055` | `WSA-2026-052-OS-SEMANTIC-MIGRATION-SOURCE-CONCURRENCY.md` |"
tracker = one(
    tracker,
    ledger_anchor,
    ledger_anchor + "\n| R3.6 | WSA-2026-014 | Memory | #32 | `3f715bf43c8dc5f0ad8888e07d857b581482569e` | `WSA-2026-014-MEMORY-MIGRATION-HANDOFF-ATOMICITY.md` |",
    "tracker ledger",
)
marker = "## 27. Current task - R3.6 / WSA-2026-014"
pos = tracker.find(marker)
if pos < 0:
    raise SystemExit("tracker current-task marker not found")
tracker = tracker[:pos] + '''## 27. R3.6 closure record - WSA-2026-014

**Owner:** `AI-Verse-Memory`  
**Accepted pre-repair Memory:** `cbc6651d60d42c63015bc1b25b5cd8f0c49d5904`  
**Restored repair baseline:** `fb4b1871bab73be22336d05b8aa3db5782ef641e`  
**Baseline product tree:** `4444ff070fd55c604a80c072081068bb265ccde6`  
**Repair PR:** `AI-Verse-Memory#32`  
**Final tested head:** `860d55d4dc72307d59063a245b0e8d4f1f58b082`  
**Merged Memory:** `3f715bf43c8dc5f0ad8888e07d857b581482569e`  
**Tested/merged product tree:** `1c890c174e8c38c0b8b0aa150f3a6daf1365aeee`  
**Status:** **CLOSED**

Acceptance:

- accidental temporary `noop` main commit was immediately reverted before repair branching: PASS;
- restored baseline tree exactly equals the accepted WSA-2026-013 tree: PASS;
- stable handoff ID binds the reviewed source fingerprint and target root: PASS;
- target authority stages through `prepared -> pending -> complete`: PASS;
- native normal writes remain blocked before verified `complete`: PASS;
- `complete` without `source_retirement_verified=true` remains non-authoritative: PASS;
- source enters `retiring` before target `pending`: PASS;
- legacy executable is backed up and replaced by the retirement stub before source retirement completes: PASS;
- source Memory bytes are reverified under the source mutation lock: PASS;
- source `retired` state is re-read and verified before target `complete`: PASS;
- faults after all six explicit cross-root transitions never expose two writable canonical routes: PASS;
- interrupted prepared/pending handoffs recover idempotently: PASS;
- historical premature target `complete` without retirement proof is fenced and repaired: PASS;
- target-only prepared crash followed by reviewed source drift can safely replace the stale prepared reservation only before source-side handoff state exists: PASS;
- replaced prepared handoff identity remains recorded through completion: PASS;
- mismatched handoff identity fails closed: PASS;
- migration-complete rejects receipts without verified source retirement: PASS;
- exact-head Migration Handoff Atomicity `37134074299`: Ubuntu/macOS/Windows, 3 / 3 PASS;
- exact-head Test `37134074348`: 12 / 12 jobs PASS;
- representative exact-head suite: 130 tests, 129 pass, 0 fail, 1 pre-existing skip;
- all three dedicated WSA-2026-014 adversarial regressions present and PASS on exact head;
- merged-main Migration Handoff Atomicity `37134269429`: Ubuntu/macOS/Windows, 3 / 3 PASS;
- merged-main Test `37134269425`: 12 / 12 jobs PASS;
- representative merged-main suite: 130 tests, 129 pass, 0 fail, 1 pre-existing skip;
- all three dedicated WSA-2026-014 regressions present and PASS after merge;
- exact tested PR tree and merged Memory product tree: identical;
- open Memory PRs after merge: 0;
- C-A1.4-003: RESOLVED for WSA-2026-014.

## 28. Current task - R3.7 / WSA-2026-025

**Owner:** `ai-verse-token`  
**Status:** **ACTIVE**  
**Execution state:** not yet implemented.

The next repair session must first recheck Token `main`, open PRs and the exact WSA-2026-025 pricing-transactionality evidence before creating any owner repair branch.

This repair remains separate from the completed Memory migration-handoff atomicity repair.

No later finding may become ACTIVE until WSA-2026-025 reaches CLOSED or an explicitly recorded BLOCKED state.

## 29. Program progress

- R0: **4 / 4 CLOSED = 100%**
- R1: **13 / 13 CLOSED = 100%**
- R2: **5 / 5 CLOSED = 100%**
- R3: **6 / 10 CLOSED = 60%**
- Findings: **28 / 63 CLOSED = 44.44%**
- Remaining: **35 / 63 OPEN = 55.56%**
- Open BLOCKERs: **0**
- Whole-system verdict: **NO-GO**
- Dashboard MC1.4: paused
- Owner dogfood: paused
'''
tracker_path.write_text(tracker, encoding="utf-8")

register = register_path.read_text(encoding="utf-8")
register = one(
    register,
    "**Live repair-state checkpoint:** R3.5 / `WSA-2026-052` closure, 2026-10-03",
    "**Live repair-state checkpoint:** R3.6 / `WSA-2026-014` closure, 2026-10-03",
    "register checkpoint",
)
register = one(register, "| OPEN | **36** |", "| OPEN | **35** |", "register open count")
register = one(register, "| CLOSED | **27** |", "| CLOSED | **28** |", "register closed count")
register = one(
    register,
    "`WSA-2026-012`, `WSA-2026-013`, `WSA-2026-016`",
    "`WSA-2026-012`, `WSA-2026-013`, `WSA-2026-014`, `WSA-2026-016`",
    "register closed list",
)
register = one(
    register,
    "`WSA-2026-001`, `002`, `003`, `004`, `005`, `011`, `014`, `015`,",
    "`WSA-2026-001`, `002`, `003`, `004`, `005`, `011`, `015`,",
    "register open list",
)
accepted_anchor = "| `WSA-2026-013` | `AI-Verse-Memory` | `#31` | `cbc6651d60d42c63015bc1b25b5cd8f0c49d5904` | `../repairs/WSA-2026-013-MEMORY-WRITE-LIFECYCLE-AUTHORITY.md` |"
register = one(
    register,
    accepted_anchor,
    accepted_anchor + "\n| `WSA-2026-014` | `AI-Verse-Memory` | `#32` | `3f715bf43c8dc5f0ad8888e07d857b581482569e` | `../repairs/WSA-2026-014-MEMORY-MIGRATION-HANDOFF-ATOMICITY.md` |",
    "register accepted closure",
)
suffix = "`WSA-2026-014` is now the next dependency-safe finding and was not modified.\n\n## 27. Current repair position"
pos = register.find(suffix)
if pos < 0:
    raise SystemExit("register tail marker not found")
register = register[:pos] + '''## 27. WSA-2026-014 closure overlay

**Transition:** `OPEN -> CLOSED`  
**Severity/confidence:** HIGH / PROVEN, unchanged  
**Accepted pre-repair Memory ref:** `cbc6651d60d42c63015bc1b25b5cd8f0c49d5904`  
**Restored repair baseline:** `fb4b1871bab73be22336d05b8aa3db5782ef641e`  
**Repair PR:** `AI-Verse-Memory#32`  
**Final tested PR head:** `860d55d4dc72307d59063a245b0e8d4f1f58b082`  
**Merged Memory ref:** `3f715bf43c8dc5f0ad8888e07d857b581482569e`  
**Tested/merged product tree:** `1c890c174e8c38c0b8b0aa150f3a6daf1365aeee`

Closure evidence:

- restored repair baseline tree exactly equals the accepted WSA-2026-013 product tree after immediate cleanup of one accidental temporary file;
- one stable handoff ID binds source and target authority state;
- target progresses through `prepared`, `pending`, then `complete` and normal native writes stay fenced until completion proves source retirement;
- source enters `retiring`, the old executable writer is backed up and stubbed, source bytes are reverified, and source is durably `retired` before target completion;
- all source and target handoff records must match the stable handoff identity;
- six deterministic cross-root fault points prove no crash exposes two writable canonical routes and all interrupted states recover;
- baseline-style premature target completion without verified source retirement remains fenced and is recovered through the new protocol;
- a target-only prepared crash may adopt a newly reviewed source fingerprint after legitimate source drift only while no source-side handoff state exists, with replacement provenance retained;
- migration-complete requires a complete receipt matching the reviewed source and `source_retirement_verified=true`;
- exact-head Migration Handoff Atomicity `37134074299`: Ubuntu/macOS/Windows, 3 / 3 PASS;
- exact-head Test `37134074348`: 12 / 12 jobs PASS, representative suite 130 tests with 129 pass, 0 fail, 1 pre-existing skip;
- merged-main Migration Handoff Atomicity `37134269429`: Ubuntu/macOS/Windows, 3 / 3 PASS;
- merged-main Test `37134269425`: 12 / 12 jobs PASS, representative suite 130 tests with 129 pass, 0 fail, 1 pre-existing skip;
- all three dedicated WSA-2026-014 regressions pass on exact head and merged main;
- exact tested and merged product trees are identical;
- open Memory PRs after merge: 0;
- C-A1.4-003: RESOLVED for WSA-2026-014.

`WSA-2026-025` is now the next dependency-safe finding and was not modified.

## 28. Current repair position

- R0: **4 / 4 CLOSED = 100%**.
- R1: **13 / 13 CLOSED = 100%**.
- R2: **5 / 5 CLOSED = 100%**.
- R3: **6 / 10 CLOSED = 60%**.
- Total: **28 / 63 CLOSED = 44.44%**.
- Remaining: **35 / 63 OPEN = 55.56%**.
- Open BLOCKERs: **0**.
- Current ACTIVE repair: `R3.7 / WSA-2026-025`.
- WSA-2026-025 implementation has **not begun** in this closure.
- Whole-system verdict: **NO-GO**.

## 29. Navigation rule

Use this file for current state. Use the preserved detailed registers for historical audit evidence and prior overlays. Use the exact closure packet for each CLOSED finding, and use `../repairs/REPAIR-EXECUTION-TRACKER-2026-09-17.md` plus `../synthesis/A6.4-ORDERED-REPAIR-PROGRAM.md` for execution order.
'''
register_path.write_text(register, encoding="utf-8")
