# Purpose Context — Task-Level Execution State

**Purpose:** durable continuation checkpoint for `docs/PURPOSE-CONTEXT-IMPLEMENTATION-PLAN.md`  
**Execution law:** read the implementation plan, then this file, then active contract/closure docs. Execute in exact task order. For a bounded user-requested batch, persist each task before beginning the next.  
**Current admitted Core baseline:** `core-repaired-public-beta-2026-10-06`  
**Last updated:** 2026-10-07

## Current execution pointer

- **Phase:** 2 — Freeze the Purpose Context v1 contract
- **Current slice:** **2.2 — Trajectory graph contract**
- **Slice state:** IN PROGRESS
- **Completed slices:** 0.1, 1.1, 1.2, 1.3, 2.1
- **Completed Slice 2.2 tasks:** 1 of 8
- **NEXT:** **Slice 2.2 / Task 2 — freeze allowed source/target kinds**
- Do not start Task 3 until Task 2 is complete and recorded here.
- No Purpose runtime/owner implementation code exists yet.

Contracts:
- envelope: `docs/PURPOSE-CONTEXT-V1-CONTRACT.md`
- trajectory: `docs/PURPOSE-CONTEXT-TRAJECTORY-V1-CONTRACT.md`

## Slice 2.1 closure

**COMPLETE / CONTRACT FROZEN** at `c784436ecaafc2f19da58782f8802247a235c1db`.

Frozen envelope: schema v1.0; operator/workspace scopes; bounded required shell; provenance; freshness; canonical refs; deterministic ordering; explicit unknown/unavailable semantics; 16KB default / 4–64KB supported budgets; no unbounded lists; disposable/rebuildable projection with no canonical Purpose state.

## Slice 2.2 progress

1. [x] relation vocabulary — exactly `addresses`, `serves`, `advances`, `blocks`, `executes`, `measures`, `affects`, `supersedes`; authoritative edges require canonical from/to/evidence refs; no similarity/model-inferred edges. Commit `b871db6a4849c5d76cee0181d4c890895d6fde6a`.
2. [ ] allowed source/target kinds
3. [ ] cycle behavior
4. [ ] missing-parent behavior
5. [ ] supersession behavior
6. [ ] orphan initiative/current-work behavior
7. [ ] explain traversal rules
8. [ ] deterministic graph ordering

## Carried repair register

1. Brain release descriptor invalid/unreachable revision; repair before Purpose Brain acceptance/Core vNext.
2. Dashboard workspace-ID contract must align with canonical lowercase alnum/hyphen max 128 before Purpose Dashboard qualification.
3. OS workspace manifest schema max length should align with runtime max 128.
4. Brain trajectory refs must validate target existence/kind/scope/status before authoritative Purpose edges.
5. Data aggregate freshness must never be inferred from query execution time.
6. Final qualification must pin exact component refs.

## Resume instructions

1. Read plan.
2. Read this file.
3. Read both frozen/active contract docs above.
4. Continue only with **Slice 2.2 / Task 2 — allowed source/target kinds**.
5. Persist this file after Task 2 before Task 3.
