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
- **Completed Slice 2.2 tasks:** 1–4 of 8
- **NEXT:** **Slice 2.2 / Task 5 — freeze supersession behavior**
- Do not start Task 6 until Task 5 is complete and recorded here.
- No Purpose runtime/owner implementation code exists yet.

Contracts:
- envelope: `docs/PURPOSE-CONTEXT-V1-CONTRACT.md`
- trajectory: `docs/PURPOSE-CONTEXT-TRAJECTORY-V1-CONTRACT.md`

## Slice 2.1 closure

**COMPLETE / CONTRACT FROZEN** at `c784436ecaafc2f19da58782f8802247a235c1db`.

Frozen envelope: schema v1.0; exact operator/workspace scopes; bounded required shell; provenance; freshness; canonical refs; deterministic ordering; explicit unknown/unavailable semantics; 16KB default / 4–64KB supported budgets; no unbounded lists; disposable/rebuildable projection with no canonical Purpose state.

## Slice 2.2 progress

1. [x] relation vocabulary — exactly eight evidence-backed relation tokens. `b871db6a4849c5d76cee0181d4c890895d6fde6a`
2. [x] source/target kinds — bounded semantic node kinds + exact relation matrix + deterministic owner-backed/derived node identity. `164d57b00eaa5a5e6d942a824d68eba57fcdea18`
3. [x] cycle behavior — self-edges invalid; structural `serves|advances|executes|supersedes` graph acyclic; cycle SCC edges excluded from authoritative traversal, no silent repair. `1d9b7de2631d3328bfa7771584d2b095a4bcc90e`
4. [x] missing-parent behavior — explicit resolved/stubbed/unavailable/missing/forbidden/invalid target states; retained edges keep identity stubs under pruning; broken refs never fuzzy-fallback; explanations stop at verified boundary. `271891898cf94fefb11388e46a7cee4fc0877d1c`
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
3. Read both contract docs.
4. Continue only with **Slice 2.2 / Task 5 — supersession behavior**.
5. Persist this file after Task 5 before Task 6.
