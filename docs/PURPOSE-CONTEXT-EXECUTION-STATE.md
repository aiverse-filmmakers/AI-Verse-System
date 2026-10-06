# Purpose Context — Task-Level Execution State

**Purpose:** durable continuation checkpoint for `docs/PURPOSE-CONTEXT-IMPLEMENTATION-PLAN.md`  
**Execution law:** read the implementation plan, then this file, then active contract/closure docs. Execute in exact task order. For a bounded user-requested batch, persist each task before beginning the next.  
**Current admitted Core baseline:** `core-repaired-public-beta-2026-10-06`  
**Last updated:** 2026-10-07

## Current execution pointer

- **Phase:** 2 — Freeze the Purpose Context v1 contract
- **Current slice:** **2.2 — Trajectory graph contract**
- **Slice state:** NOT STARTED
- **Completed slices:** 0.1, 1.1, 1.2, 1.3, **2.1**
- **NEXT:** **Slice 2.2 / Task 1 — freeze relation vocabulary**
- Do not start Task 2 until Task 1 is complete and recorded here.
- No Purpose runtime/owner implementation code exists yet; Phase 2 remains contract-only.

Frozen envelope contract: `docs/PURPOSE-CONTEXT-V1-CONTRACT.md`.

## Slice 2.1 closure

**Status:** COMPLETE / CONTRACT FROZEN  
**Final contract commit:** `c784436ecaafc2f19da58782f8802247a235c1db`

Frozen results:

1. `schema_version = "1.0"` with unsupported-major fail-closed behavior.
2. exact scopes `operator` / `workspace:<id>` only.
3. required shell + relevance-driven optional semantic sections.
4. owner-read/claim provenance with exact canonical refs.
5. explicit freshness: current/stale/unknown/unavailable.
6. canonical ref identity `(owner, scope, kind, id)` + version where meaningful.
7. deterministic ordering independent of storage/API arrival order.
8. explicit absent/known-empty/partial/unknown/unavailable/error field/section behavior with no silent fallback.
9. bounded projection: default 16384 UTF-8 bytes, supported request range 4096–65536, deterministic pruning, no unbounded lists.
10. projection is disposable/rebuildable, has no canonical Purpose state, and stale cache can never override owner truth.

Slice 2.1 acceptance: PASS on versioning, absent-vs-unknown semantics, stale-state representation, read-only ownership, boundedness and rebuildability.

## Completed earlier audits / exact refs

- 0.1 plan: PR #189, merge `b0b4a356ee33d86161e4ec9b3a6f9ed95b958c8e`.
- 1.1 OS audit: `docs/PURPOSE-CONTEXT-SLICE-1.1-AUDIT.md`; OS `e74a4e05b1f891e6f871f34a298bf10363a11d88`.
- 1.2 Brain audit: `docs/PURPOSE-CONTEXT-SLICE-1.2-AUDIT.md`; Brain `7c77b053df627e61b3d7f11d029500ab61095c9c`.
- 1.3 integration audit: `docs/PURPOSE-CONTEXT-SLICE-1.3-AUDIT.md`; Data `6e8781ff1dcd96a35dfb27868bd60605361483d0`, Memory `b0cae8cd8da38aa657fbc736c575177aa75e5ec7`, Gateway `089aaa6440bbbbb9f41195eafe123ad2e06d5625`, Dashboard `2c1d1a57f7cb27eec166d4fea10dbb335250c518`.

## Carried repair register

1. Brain release descriptor invalid/unreachable revision; repair before Purpose Brain acceptance/Core vNext.
2. Dashboard workspace-ID contract must align with canonical lowercase alnum/hyphen max 128 before Purpose Dashboard qualification.
3. OS workspace manifest schema max length should align with runtime max 128.
4. Brain trajectory refs must validate target existence/kind/scope/status before authoritative Purpose edges.
5. Data aggregate freshness must never be inferred from query execution time.
6. Final qualification must pin exact component refs.

## Slice 2.2 task order

1. [ ] relation vocabulary
2. [ ] allowed source/target kinds
3. [ ] cycle behavior
4. [ ] missing-parent behavior
5. [ ] supersession behavior
6. [ ] orphan initiative/current-work behavior
7. [ ] explain traversal rules
8. [ ] deterministic graph ordering

## Resume instructions

1. Read plan.
2. Read this file.
3. Read `docs/PURPOSE-CONTEXT-V1-CONTRACT.md` for Slice 2.1.
4. Continue only with **Slice 2.2 / Task 1 — relation vocabulary**.
5. Persist this file after Task 1 before Task 2.
