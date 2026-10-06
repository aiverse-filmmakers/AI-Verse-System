# Purpose Context — Task-Level Execution State

**Purpose:** durable continuation checkpoint for `docs/PURPOSE-CONTEXT-IMPLEMENTATION-PLAN.md`  
**Execution law:** read the implementation plan, then this file, then the active contract/closure docs. Execute in exact task order. When the user requests a bounded batch, complete and persist each task before starting the next.  
**Current admitted Core baseline:** `core-repaired-public-beta-2026-10-06`  
**Last updated:** 2026-10-07

---

## Current execution pointer

- **Phase:** 2 — Freeze the Purpose Context v1 contract
- **Current slice:** **2.1 — Versioned envelope schema**
- **Slice state:** IN PROGRESS
- **Completed slices:** 0.1, 1.1, 1.2, 1.3
- **Completed Slice 2.1 tasks:** 1–7 of 10
- **NEXT:** **Slice 2.1 / Task 8 — freeze unknown/unavailable field behavior**
- Do not start Task 9 until Task 8 is complete and recorded here.
- No Purpose Context runtime/owner implementation code has been written yet; Phase 2 remains contract-only.

Active contract: `docs/PURPOSE-CONTEXT-V1-CONTRACT.md`.

---

## Completed slice closures / audited refs

- **0.1:** canonical implementation plan, PR #189, merge `b0b4a356ee33d86161e4ec9b3a6f9ed95b958c8e`.
- **1.1 OS audit:** `docs/PURPOSE-CONTEXT-SLICE-1.1-AUDIT.md`; OS `e74a4e05b1f891e6f871f34a298bf10363a11d88`.
- **1.2 Brain audit:** `docs/PURPOSE-CONTEXT-SLICE-1.2-AUDIT.md`; Brain `7c77b053df627e61b3d7f11d029500ab61095c9c`.
- **1.3 Data/Memory/Gateway/Dashboard audit:** `docs/PURPOSE-CONTEXT-SLICE-1.3-AUDIT.md`; Data `6e8781ff1dcd96a35dfb27868bd60605361483d0`, Memory `b0cae8cd8da38aa657fbc736c575177aa75e5ec7`, Gateway `089aaa6440bbbbb9f41195eafe123ad2e06d5625`, Dashboard `2c1d1a57f7cb27eec166d4fea10dbb335250c518`.

Retained owner/API direction:

- OS: scope/current-context/direction-owner + Purpose composer/read/explain.
- Brain: strategic snapshot + only genuinely missing strategic semantics frozen by Phase 2.
- Data: existing bounded query/provenance surfaces; optional thin KPI binding wrapper only if required.
- Memory: existing recall/orientation/progressive recall; optional thin material-change evidence adapter only if required.
- Gateway: relevance-gated Purpose owner read/injection + diagnostics; trivial tasks = zero Purpose reads.
- Dashboard: read-only Purpose projection first; owner-routed commands only after Phase 8.
- Distribution: final exact-ref Core descendant qualification/admission.

Frozen audit-level Telos mapping:

- Problem → minimal new strategic semantic, prefer `intent:problem`.
- Mission → minimal new strategic semantic, prefer `intent:mission`.
- Narrative → derived in v1.
- Goal → strategic `intent:goal`; execution Goal remains separate.
- Challenge → derived in v1.
- Strategy → minimal new strategic semantic, prefer `intent:strategy`; never `strategy_rule`.
- Initiative → existing canonical `initiative`.

---

## Carried repair register

1. Brain release descriptor has a pre-existing invalid/unreachable declared revision; repair before Purpose Brain acceptance/Core vNext.
2. Dashboard workspace-ID contract must align with canonical lowercase alnum/hyphen IDs up to 128 before Purpose Dashboard qualification.
3. OS workspace manifest schema max length should align with runtime max 128.
4. Brain trajectory refs must validate target existence/kind/scope/status before becoming authoritative Purpose edges.
5. Data aggregate freshness must never be inferred from query execution time.
6. Final qualification must pin exact component refs; moving-main workflows are insufficient release evidence.

---

## Phase 2 / Slice 2.1 checklist

1. [x] `schema_version` — `"1.0"`; unsupported major fails closed. Commit `3cf8c48fde4950ac69ff30e11e22d308210fab43`.
2. [x] scope kinds — exactly `operator` / `workspace:<id>`; canonical workspace IDs max 128. Commit `95ba626b02de0c7d62a16060d1c228eeaa1548ed`.
3. [x] required vs optional fields — required shell: version/scope/scope_kind/identity/provenance; semantic sections relevance-driven. Commit `2a17d8fbfefc8699685af831150f40a453a0d2ce`.
4. [x] provenance — every attempted owner read recorded; every authoritative claim traces to exact owner refs. Commit `3eaae415ac02714a1c2960c1f193af44828de7ca`.
5. [x] freshness — `current|stale|unknown|unavailable`; read time never proves freshness. Commit `84b6fd49c7f400724ac1f55b47acbe5a4de72be6`.
6. [x] canonical refs — `(owner, scope, kind, id)` plus exact mutable version where supported/required. Commit `bbfe9bb9daaddeadd10eb15177aae21193855cd6`.
7. [x] deterministic ordering — owner semantic rank first; otherwise canonical-ref order; recent changes use owner event time desc; serialization and pruning deterministic. Commit `f478e5bfba82ba6feac88098a6e65f542cd0109e`.
8. [ ] unknown/unavailable field behavior
9. [ ] bounded size/budget rules
10. [ ] rebuildability contract

Slice 2.1 acceptance still requires: versioned schema; absence distinct from unknown/unavailable; stale reads explicit; no projected field independently editable.

---

## Resume instructions

1. Read `docs/PURPOSE-CONTEXT-IMPLEMENTATION-PLAN.md`.
2. Read this file for the authoritative pointer.
3. Read `docs/PURPOSE-CONTEXT-V1-CONTRACT.md` for frozen v1 semantics.
4. Continue only with **Slice 2.1 / Task 8 — unknown/unavailable field behavior**.
5. Persist this file after Task 8 before Task 9.
