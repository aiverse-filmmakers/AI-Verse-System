# Purpose Context - Task-Level Execution State

**Purpose:** durable continuation checkpoint for `docs/PURPOSE-CONTEXT-IMPLEMENTATION-PLAN.md`  
**Execution law:** read the implementation plan, then this file, then active contract/closure docs. Execute in exact task order. For a bounded user-requested batch, persist each task before beginning the next.  
**Current admitted Core baseline:** `core-repaired-public-beta-2026-10-06`  
**Last updated:** 2026-10-08

> Historical evidence through prior slices remains preserved in checkpoint lineage and per-slice closure records. This file is intentionally compact.

## Current execution pointer

- **Phase:** 7 - Relevance gates and context-budget roll-in
- **Current slice:** **7.2 - Context budget/freshness policy**
- **Slice state:** IN PROGRESS
- **Completed slices:** 0.1, 1.1, 1.2, 1.3, 2.1, 2.2, 2.3, 3.1, 3.2, 4.1, 4.2, 4.3, 5.1, 5.2, 6.1, 6.2, 7.1
- **Closed slices:** 17 of 34
- **Closed phases:** 0, 1, 2, 3, 4, 5, 6 = 7 of 14
- **Completed Slice 7.2 tasks:** 5 of 6
- **NEXT:** **Slice 7.2 / Task 6 - ensure stale cached UI/output cannot outrank a fresh owner read**
- Task 5 is complete, tested, merged, and persisted. Do not begin Slice 7.3 until Task 6 is complete, tested, persisted, and Slice 7.2 is formally closed.

## Slice 7.2 task checklist

1. [x] define maximum envelope size - runtime Purpose hard cap **16,384 bytes**. Gateway PR #42 head `f7065cfa294f1458e3eaca5341922d9d0532186f`, merged `24012566a8bbc866c681d51e2e5920569e67f25c`.
2. [x] define truncation priority - `os.purpose-budget-policy.v1`. OS PR #53 head `1bb4ea254b060021d65ae6d6ef4dcc672e652b01`, merged `45f3734fa4bbaf64e0d72b25b694770e736b9cc1`.
3. [x] preserve trajectory-critical fields ahead of optional rich context - final OS budget pass after enrichment. OS PR #54 head `fe544c6c99d0a2ce2f1a4067fdf7aee00f64a139`, merged `b2e1b531402bc492e40eafbbcacddb78ec7a46b6`.
4. [x] define refresh conditions - `gateway.purpose-refresh-policy.v1`; every Purpose-relevant assembly requires a fresh owner read and Gateway cache reuse is forbidden. Gateway PR #43 head `bec27fd4ed0aba569fb1618985b12f5a4b2318a2`, merged `0d784147c71695803b311c403003d964e59ec27f`.
5. [x] define unavailable-owner behavior - `gateway.purpose-unavailable-policy.v1`; genuine owner/process availability failures allow ordinary runtime context assembly to continue with Purpose absent, never with a stale Purpose substitute. Scope/authority/budget contract violations still fail closed. Gateway PR #44 exact head `6586e471b191ab1caa947564d4da5292cbf3f6eb`, merged `a41fce18aefd0719d416f6100a247aa427d4de00`. Gateway CI `37840314915` PASS across Ubuntu/macOS/Windows Node 20/22 including Ubuntu benchmark; Context Ladder `37840315167`, Permanent Bot `37840315025`, Automation Boundary `37840315148`, Temporary Worker `37840315146` PASS.
6. [ ] ensure stale cached UI/output cannot outrank a fresh owner read

## Active runtime contract for Slice 7.2

1. Gateway remains runtime/context assembler only; OS remains Purpose projection owner.
2. Runtime Purpose maximum logical envelope size is **16,384 bytes**.
3. OS truncation priority is frozen by `os.purpose-budget-policy.v1` and final composition re-applies it after enrichment.
4. Every relevant runtime assembly requires a fresh Purpose owner read; Gateway projection-cache reuse is forbidden.
5. Irrelevant tasks perform zero Purpose reads.
6. When the Purpose owner/process is genuinely unavailable, ordinary task execution continues without Purpose and without any stale Purpose substitute.
7. Scope, authority, provenance, and budget violations are not treated as availability failures and remain fail-closed.
8. No budget/freshness/fallback policy may create a second Purpose authority.

## Closed slice records

- Slice 7.1: `docs/PURPOSE-CONTEXT-SLICE-7.1-CLOSURE.md`
- Slice 6.2: `docs/PURPOSE-CONTEXT-SLICE-6.2-CLOSURE.md`
- Slice 6.1: `docs/PURPOSE-CONTEXT-SLICE-6.1-CLOSURE.md`

## Carried repair register

1. Dashboard workspace-ID contract must align with canonical lowercase alnum/hyphen max 128 before Purpose Dashboard qualification.
2. OS workspace manifest schema max length should align runtime max 128.
3. Data aggregate freshness must never be inferred from query execution time. **RESOLVED for the Purpose current-value path in Slice 5.1:** freshness is sourced from canonical Data record `updatedAt`.
4. Final qualification must pin exact component refs.

## Resume instructions

Continue only with **Slice 7.2 / Task 6 - ensure stale cached UI/output cannot outrank a fresh owner read**. After Task 6 passes, close Slice 7.2 and Phase 7 remains open for the 7.3 value gate.