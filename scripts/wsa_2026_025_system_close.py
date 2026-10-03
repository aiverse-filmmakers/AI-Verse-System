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
    "**Current active finding:** `WSA-2026-025`",
    "**Current active finding:** `WSA-2026-034`",
    "tracker active finding",
)
tracker = one(
    tracker,
    "| R3.7 | WSA-2026-025 Token pricing transactionality | ai-verse-token | **ACTIVE** |",
    "| R3.7 | WSA-2026-025 Token pricing transactionality | ai-verse-token | **CLOSED** |",
    "tracker R3.7 row",
)
tracker = one(
    tracker,
    "| R3.8 | WSA-2026-034 Distribution lifecycle receipt concurrency | ai-verse-distribution | PENDING |",
    "| R3.8 | WSA-2026-034 Distribution lifecycle receipt concurrency | ai-verse-distribution | **ACTIVE** |",
    "tracker R3.8 row",
)
tracker = one(
    tracker,
    "**R3 progress: 6 / 10 CLOSED = 60%.**",
    "**R3 progress: 7 / 10 CLOSED = 70%.**",
    "tracker R3 progress",
)
tracker = one(
    tracker,
    "- R3: 10 findings, 4 remaining",
    "- R3: 10 findings, 3 remaining",
    "tracker R3 remaining",
)
ledger_anchor = "| R3.6 | WSA-2026-014 | Memory | #32 | `3f715bf43c8dc5f0ad8888e07d857b581482569e` | `WSA-2026-014-MEMORY-MIGRATION-HANDOFF-ATOMICITY.md` |"
tracker = one(
    tracker,
    ledger_anchor,
    ledger_anchor + "\n| R3.7 | WSA-2026-025 | Token | #2 | `69b15e59ad117e147730dbc30dfef7cbc083c8de` | `WSA-2026-025-TOKEN-PRICING-TRANSACTIONALITY.md` |",
    "tracker ledger",
)
marker = "## 28. Current task - R3.7 / WSA-2026-025"
pos = tracker.find(marker)
if pos < 0:
    raise SystemExit("tracker current-task marker not found")
tracker = tracker[:pos] + '''## 28. R3.7 closure record - WSA-2026-025

**Owner:** `ai-verse-token`  
**Accepted pre-repair Token:** `1a85d0da0e529b659b62d3c9a3e2d40c853d67d3`  
**Baseline product tree:** `486cc2da61648e02179e2dbeb0b0c9d448ec6d1f`  
**Repair PR:** `ai-verse-token#2`  
**Final tested head:** `d59aa7a8e74bb73eeb23aee123793e2901a200cb`  
**Merged Token:** `69b15e59ad117e147730dbc30dfef7cbc083c8de`  
**Tested/merged product tree:** `7f388e99a1d2694e688dc09f23932498ac502388`  
**Status:** **CLOSED**

Acceptance:

- new immutable snapshot batches stage outside normal pricing authority: PASS;
- full staged batch and manifest are validated before publication: PASS;
- one atomic directory rename publishes the whole batch: PASS;
- `get` and `list` ignore incomplete staging artifacts: PASS;
- legacy immutable snapshot files remain readable: PASS;
- committed manifests bind snapshot IDs to canonical-content SHA-256 digests: PASS;
- successful `updated` sync truth is embedded in the same atomic batch publication: PASS;
- `syncState` consumes committed-batch success observations and legacy state observations: PASS;
- cross-process publication is serialized by a token/PID/hostname-bound lock: PASS;
- live local holders are never reclaimed by age alone: PASS;
- dead local holders are re-read and identity-checked before reclaim: PASS;
- later staged-member I/O failure exposes zero members of the failed batch: PASS;
- real competing-process conflicting batch race publishes exactly one whole winner: PASS;
- writer crash after first staged member leaves its subset invisible and permits safe dead-holder recovery: PASS;
- full synchronizer success publishes new snapshots and success observation together: PASS;
- synchronizer manifest-write failure returns failed / `SYNC_INVALID` with zero new snapshots visible: PASS;
- exact-head Pricing Transactionality `37151667552`: Ubuntu/macOS/Windows, 3 / 3 PASS;
- exact-head CI `37151667585`: Ubuntu/macOS/Windows x Node 22/24, 6 / 6 PASS;
- representative exact-head canonical suite: 268 / 268 PASS;
- exact-head release acceptance: 3 / 3 PASS;
- merged-main Pricing Transactionality `37151877209`: Ubuntu/macOS/Windows, 3 / 3 PASS;
- merged-main CI `37151877242`: Ubuntu/macOS/Windows x Node 22/24, 6 / 6 PASS;
- representative merged-main canonical suite: 268 / 268 PASS, 0 fail, 0 skipped;
- merged-main release acceptance: 3 / 3 PASS;
- all six dedicated WSA-2026-025 regression cases are present and PASS after merge;
- exact tested PR tree and merged Token product tree: identical;
- open Token PRs after merge: 0;
- C-A1.8-002: RESOLVED for WSA-2026-025.

## 29. Current task - R3.8 / WSA-2026-034

**Owner:** `ai-verse-distribution`  
**Status:** **ACTIVE**  
**Execution state:** not yet implemented.

The next repair session must first recheck Distribution `main`, open PRs and the exact WSA-2026-034 lifecycle-receipt concurrency evidence before creating any owner repair branch.

This repair remains separate from the completed Token pricing-transactionality repair.

No later finding may become ACTIVE until WSA-2026-034 reaches CLOSED or an explicitly recorded BLOCKED state.

## 30. Program progress

- R0: **4 / 4 CLOSED = 100%**
- R1: **13 / 13 CLOSED = 100%**
- R2: **5 / 5 CLOSED = 100%**
- R3: **7 / 10 CLOSED = 70%**
- Findings: **29 / 63 CLOSED = 46.03%**
- Remaining: **34 / 63 OPEN = 53.97%**
- Open BLOCKERs: **0**
- Whole-system verdict: **NO-GO**
- Dashboard MC1.4: paused
- Owner dogfood: paused
'''
tracker_path.write_text(tracker, encoding="utf-8")

register = register_path.read_text(encoding="utf-8")
register = one(
    register,
    "**Live repair-state checkpoint:** R3.6 / `WSA-2026-014` closure, 2026-10-03",
    "**Live repair-state checkpoint:** R3.7 / `WSA-2026-025` closure, 2026-10-03",
    "register checkpoint",
)
register = one(register, "| OPEN | **35** |", "| OPEN | **34** |", "register open count")
register = one(register, "| CLOSED | **28** |", "| CLOSED | **29** |", "register closed count")
register = one(
    register,
    "`WSA-2026-022`, `WSA-2026-023`, `WSA-2026-024`, `WSA-2026-026`",
    "`WSA-2026-022`, `WSA-2026-023`, `WSA-2026-024`, `WSA-2026-025`, `WSA-2026-026`",
    "register closed list",
)
register = one(
    register,
    "`WSA-2026-001`, `002`, `003`, `004`, `005`, `011`, `015`, `018`, `019`, `021`, `025`, `034`,",
    "`WSA-2026-001`, `002`, `003`, `004`, `005`, `011`, `015`, `018`, `019`, `021`, `034`,",
    "register open list",
)
accepted_anchor = "| `WSA-2026-024` | `ai-verse-token` | `#1` | `1a85d0da0e529b659b62d3c9a3e2d40c853d67d3` | `../repairs/WSA-2026-024-TOKEN-TRUSTED-ACTUAL-ADMISSION.md` |"
register = one(
    register,
    accepted_anchor,
    accepted_anchor + "\n| `WSA-2026-025` | `ai-verse-token` | `#2` | `69b15e59ad117e147730dbc30dfef7cbc083c8de` | `../repairs/WSA-2026-025-TOKEN-PRICING-TRANSACTIONALITY.md` |",
    "register accepted closure",
)
suffix = "`WSA-2026-025` is now the next dependency-safe finding and was not modified.\n\n## 28. Current repair position"
pos = register.find(suffix)
if pos < 0:
    raise SystemExit("register tail marker not found")
register = register[:pos] + '''## 28. WSA-2026-025 closure overlay

**Transition:** `OPEN -> CLOSED`  
**Severity/confidence:** MEDIUM / PROVEN, unchanged  
**Accepted pre-repair Token ref:** `1a85d0da0e529b659b62d3c9a3e2d40c853d67d3`  
**Repair PR:** `ai-verse-token#2`  
**Final tested PR head:** `d59aa7a8e74bb73eeb23aee123793e2901a200cb`  
**Merged Token ref:** `69b15e59ad117e147730dbc30dfef7cbc083c8de`  
**Tested/merged product tree:** `7f388e99a1d2694e688dc09f23932498ac502388`

Closure evidence:

- new pricing batches stage outside normal read authority and become visible only through one atomic directory rename;
- committed manifests bind each snapshot ID to its canonical-content SHA-256 digest;
- normal `get` / `list` reads ignore all incomplete staging artifacts;
- successful `updated` synchronization truth is embedded in the same committed batch publication as newly visible snapshots;
- legacy snapshot and sync-state formats remain readable;
- publication is serialized through a token/PID/hostname-bound cross-process lock;
- live holders are protected regardless of lock age and dead local holders are identity-checked before reclaim;
- deterministic later staged-member failure leaves the entire candidate batch invisible;
- a real two-process conflicting race publishes exactly one complete winner and no losing unique member;
- a process crash after its first staged member leaves no pricing authority and permits safe dead-holder recovery;
- full synchronizer failure before publication records failure without exposing new snapshots;
- exact-head Pricing Transactionality `37151667552`: 3 / 3 PASS;
- exact-head CI `37151667585`: 6 / 6 PASS with representative 268 / 268 canonical tests and 3 / 3 release acceptance;
- merged-main Pricing Transactionality `37151877209`: 3 / 3 PASS;
- merged-main CI `37151877242`: 6 / 6 PASS with representative 268 / 268 canonical tests and 3 / 3 release acceptance;
- all six dedicated WSA-2026-025 regressions pass on exact head and merged main;
- exact tested and merged product trees are identical;
- open Token PRs after merge: 0;
- C-A1.8-002: RESOLVED for WSA-2026-025.

`WSA-2026-034` is now the next dependency-safe finding and was not modified.

## 29. Current repair position

- R0: **4 / 4 CLOSED = 100%**.
- R1: **13 / 13 CLOSED = 100%**.
- R2: **5 / 5 CLOSED = 100%**.
- R3: **7 / 10 CLOSED = 70%**.
- Total: **29 / 63 CLOSED = 46.03%**.
- Remaining: **34 / 63 OPEN = 53.97%**.
- Open BLOCKERs: **0**.
- Current ACTIVE repair: `R3.8 / WSA-2026-034`.
- WSA-2026-034 implementation has **not begun** in this closure.
- Whole-system verdict: **NO-GO**.

## 30. Navigation rule

Use this file for current state. Use the preserved detailed registers for historical audit evidence and prior overlays. Use the exact closure packet for each CLOSED finding, and use `../repairs/REPAIR-EXECUTION-TRACKER-2026-09-17.md` plus `../synthesis/A6.4-ORDERED-REPAIR-PROGRAM.md` for execution order.
'''
register_path.write_text(register, encoding="utf-8")
