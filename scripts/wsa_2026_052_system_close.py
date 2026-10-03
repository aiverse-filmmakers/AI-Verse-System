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
    "**Current active finding:** `WSA-2026-052`",
    "**Current active finding:** `WSA-2026-014`",
    "tracker active finding",
)
tracker = one(
    tracker,
    "| R3.5 | WSA-2026-052 OS semantic migration source concurrency | AI-Verse-OS | **ACTIVE** |",
    "| R3.5 | WSA-2026-052 OS semantic migration source concurrency | AI-Verse-OS | **CLOSED** |",
    "tracker R3.5 row",
)
tracker = one(
    tracker,
    "| R3.6 | WSA-2026-014 Memory migration handoff atomicity | AI-Verse-Memory | PENDING |",
    "| R3.6 | WSA-2026-014 Memory migration handoff atomicity | AI-Verse-Memory | **ACTIVE** |",
    "tracker R3.6 row",
)
tracker = one(
    tracker,
    "**R3 progress: 4 / 10 CLOSED = 40%.**",
    "**R3 progress: 5 / 10 CLOSED = 50%.**",
    "tracker R3 progress",
)
tracker = one(
    tracker,
    "- R3: 10 findings, 6 remaining",
    "- R3: 10 findings, 5 remaining",
    "tracker R3 remaining",
)
ledger_anchor = "| R3.4 | WSA-2026-053 | Data + OS | Data #18 / OS #45 | `5cbf9908440ca7e11506991ba1dd7d3344f2b1fd` / `53c6806bf4c8205062096ab7d6247c732823df41` | `WSA-2026-053-DATA-NATURAL-KEY-UNIQUENESS.md` |"
tracker = one(
    tracker,
    ledger_anchor,
    ledger_anchor
    + "\n| R3.5 | WSA-2026-052 | OS | #46 | `9effe3869a87fb2c11287ae4821f93620abcc055` | `WSA-2026-052-OS-SEMANTIC-MIGRATION-SOURCE-CONCURRENCY.md` |",
    "tracker ledger",
)
marker = "## 26. Current task - R3.5 / WSA-2026-052"
pos = tracker.find(marker)
if pos < 0:
    raise SystemExit("tracker current-task marker not found")
tracker = tracker[:pos] + '''## 26. R3.5 closure record - WSA-2026-052

**Owner:** `AI-Verse-OS`  
**Repair PR:** `AI-Verse-OS#46`  
**Final tested head:** `ab9e10abd44417707761f8479e46c9ea8f7c3f59`  
**Merged OS:** `9effe3869a87fb2c11287ae4821f93620abcc055`  
**Tested/merged product tree:** `3868653c83d22f3f43f09f113ef18b8341dd6357`  
**Status:** **CLOSED**

Acceptance:

- normal semantic imports serialize on one cross-process lock per source digest before owner effects: PASS;
- first admission writes durable `in-progress` source state before any owner action: PASS;
- source reservation binds the winning plan digest and import idempotency identity: PASS;
- concurrent same-source / same-plan first import produces one owner effect, one receipt and replay: PASS;
- concurrent same-source / different-plan first import produces one winning plan and one owner effect; the contender source-replays the winner: PASS;
- interrupted source recovery accepts only the originally bound plan/import identity: PASS;
- a different plan during interrupted recovery fails closed: PASS;
- crash after owner effect but before receipt recovers through the same owner idempotency identity without duplicating the already-fired effect: PASS;
- committed receipt can be adopted after crash-before-reservation-finalization: PASS;
- multiple pre-existing receipts for one source fail closed for reconciliation: PASS;
- migration Data candidate timestamp remains stable across interrupted-plan recovery: PASS;
- clarification-resolution imports preserve their prior independent path: PASS;
- first-run coordination directory races are tolerated and revalidated for directory/symlink safety: PASS;
- exact-head Migration Source Concurrency `37127337259`: Ubuntu/macOS/Windows, 3 / 3 PASS;
- all 11 exact-head triggered workflow groups: PASS;
- merged-main Migration Source Concurrency `37127474697`: Ubuntu/macOS/Windows, 3 / 3 PASS;
- all 8 merged-main triggered workflow groups: PASS;
- focused merged-main jobs pass `Prove source-level serialization and crash recovery` on Windows, macOS and Ubuntu;
- exact tested PR tree and merged product tree: identical;
- A4.2 / C-A4.2-007: RESOLVED for WSA-2026-052.

## 27. Current task - R3.6 / WSA-2026-014

**Owner:** `AI-Verse-Memory`  
**Status:** **ACTIVE**  
**Execution state:** not yet implemented.

The next repair session must first recheck Memory `main`, open PRs and the exact WSA-2026-014 migration-handoff atomicity evidence before creating any owner repair branch.

This repair remains separate from the completed OS semantic migration source-concurrency repair.

No later finding may become ACTIVE until WSA-2026-014 reaches CLOSED or an explicitly recorded BLOCKED state.

## 28. Program progress

- R0: **4 / 4 CLOSED = 100%**
- R1: **13 / 13 CLOSED = 100%**
- R2: **5 / 5 CLOSED = 100%**
- R3: **5 / 10 CLOSED = 50%**
- Findings: **27 / 63 CLOSED = 42.86%**
- Remaining: **36 / 63 OPEN = 57.14%**
- Open BLOCKERs: **0**
- Whole-system verdict: **NO-GO**
- Dashboard MC1.4: paused
- Owner dogfood: paused
'''
tracker_path.write_text(tracker, encoding="utf-8")

register = register_path.read_text(encoding="utf-8")
register = one(
    register,
    "**Live repair-state checkpoint:** R3.4 / `WSA-2026-053` closure, 2026-10-03",
    "**Live repair-state checkpoint:** R3.5 / `WSA-2026-052` closure, 2026-10-03",
    "register checkpoint",
)
register = one(register, "| OPEN | **37** |", "| OPEN | **36** |", "register open count")
register = one(register, "| CLOSED | **26** |", "| CLOSED | **27** |", "register closed count")
register = one(
    register,
    "`WSA-2026-051`, `WSA-2026-053`.",
    "`WSA-2026-051`, `WSA-2026-052`, `WSA-2026-053`.",
    "register closed list",
)
register = one(
    register,
    "`049`, `050`, `052`, `054`, `055`",
    "`049`, `050`, `054`, `055`",
    "register open list",
)
accepted_anchor = "| `WSA-2026-053` | `AI-Verse-Data` + `AI-Verse-OS` | `Data #18 / OS #45` | `5cbf9908440ca7e11506991ba1dd7d3344f2b1fd` / `53c6806bf4c8205062096ab7d6247c732823df41` | `../repairs/WSA-2026-053-DATA-NATURAL-KEY-UNIQUENESS.md` |"
register = one(
    register,
    accepted_anchor,
    accepted_anchor
    + "\n| `WSA-2026-052` | `AI-Verse-OS` | `#46` | `9effe3869a87fb2c11287ae4821f93620abcc055` | `../repairs/WSA-2026-052-OS-SEMANTIC-MIGRATION-SOURCE-CONCURRENCY.md` |",
    "register accepted closure",
)
suffix = "`WSA-2026-052` is now the next dependency-safe finding and was not modified.\n\n## 26. Current repair position"
pos = register.find(suffix)
if pos < 0:
    raise SystemExit("register tail marker not found")
register = register[:pos] + '''## 26. WSA-2026-052 closure overlay

**Transition:** `OPEN -> CLOSED`  
**Severity/confidence:** HIGH / PROVEN, unchanged  
**Repair PR:** `AI-Verse-OS#46`  
**Final tested PR head:** `ab9e10abd44417707761f8479e46c9ea8f7c3f59`  
**Merged OS ref:** `9effe3869a87fb2c11287ae4821f93620abcc055`  
**Tested/merged product tree:** `3868653c83d22f3f43f09f113ef18b8341dd6357`

Closure evidence:

- source identity now serializes normal semantic migration before any owner effect;
- first admission writes durable source reservation state before owner actions and binds the winning plan/import identity;
- concurrent same-source / same-plan imports produce one owner effect and replay;
- concurrent same-source / different-plan imports produce one winner while the contender source-replays the committed result;
- interrupted source state can recover only through the originally bound plan/import identity;
- a different plan during interrupted recovery fails closed;
- crash after an owner effect but before receipt publication recovers with the same owner idempotency identity without duplicating the fired effect;
- committed receipt adoption repairs crash-before-reservation-finalization;
- multiple pre-existing same-source receipts fail closed for reconciliation;
- clarification-resolution imports preserve their separate existing path;
- permanent `Migration Source Concurrency` regression runs on Ubuntu, macOS and Windows;
- exact-head focused run `37127337259`: 3 / 3 PASS;
- all 11 exact-head triggered OS workflow groups: PASS;
- merged-main focused run `37127474697`: 3 / 3 PASS;
- all 8 merged-main triggered OS workflow groups: PASS;
- exact tested and merged product tree: identical;
- A4.2 / C-A4.2-007: RESOLVED for WSA-2026-052.

`WSA-2026-014` is now the next dependency-safe finding and was not modified.

## 27. Current repair position

- R0: **4 / 4 CLOSED = 100%**.
- R1: **13 / 13 CLOSED = 100%**.
- R2: **5 / 5 CLOSED = 100%**.
- R3: **5 / 10 CLOSED = 50%**.
- Total: **27 / 63 CLOSED = 42.86%**.
- Remaining: **36 / 63 OPEN = 57.14%**.
- Open BLOCKERs: **0**.
- Current ACTIVE repair: `R3.6 / WSA-2026-014`.
- WSA-2026-014 implementation has **not begun** in this closure.
- Whole-system verdict: **NO-GO**.

## 28. Navigation rule

Use this file for current state. Use the preserved detailed registers for historical audit evidence and prior overlays. Use the exact closure packet for each CLOSED finding, and use `../repairs/REPAIR-EXECUTION-TRACKER-2026-09-17.md` plus `../synthesis/A6.4-ORDERED-REPAIR-PROGRAM.md` for execution order.
'''
register_path.write_text(register, encoding="utf-8")
