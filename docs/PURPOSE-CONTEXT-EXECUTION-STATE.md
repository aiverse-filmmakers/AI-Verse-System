# Purpose Context — Task-Level Execution State

**Purpose:** durable continuation checkpoint for `docs/PURPOSE-CONTEXT-IMPLEMENTATION-PLAN.md`  
**Execution law:** read the implementation plan, then this file, then active contract/closure docs. Execute in exact task order. For a bounded user-requested batch, persist each task before beginning the next.  
**Current admitted Core baseline:** `core-repaired-public-beta-2026-10-06`  
**Last updated:** 2026-10-07

## Current execution pointer

- **Phase:** 3 — Brain canonical strategic read surface
- **Current slice:** **3.1 — Purpose/strategy snapshot API**
- **Slice state:** IN PROGRESS
- **Completed slices:** 0.1, 1.1, 1.2, 1.3, 2.1, 2.2, 2.3
- **Completed Slice 3.1 tasks:** 1 of 6
- **NEXT:** **Slice 3.1 / Task 2 — expose source/evidence refs**
- Do not start Task 3 until Task 2 is complete and recorded here.

Contracts:
- envelope: `docs/PURPOSE-CONTEXT-V1-CONTRACT.md`
- trajectory: `docs/PURPOSE-CONTEXT-TRAJECTORY-V1-CONTRACT.md`
- profiles: `docs/PURPOSE-CONTEXT-PROFILES-V1-CONTRACT.md`

## Slice closures

- Slice 2.1 COMPLETE / CONTRACT FROZEN at `c784436ecaafc2f19da58782f8802247a235c1db`.
- Slice 2.2 COMPLETE / CONTRACT FROZEN at `7e2193451894b7e5b6f8b3d1def9c04afd2a2f31`.
- Slice 2.3 COMPLETE / CONTRACT FROZEN at `46bf0f4d50895b678873715fd8bb91d07619a7de`.
- **Phase 2 COMPLETE / V1 CONTRACT FROZEN.**

## Phase 3 / Slice 3.1 task checklist

Starting Brain ref: `7c77b053df627e61b3d7f11d029500ab61095c9c`.

1. [x] expose confirmed/current strategic objects only — added read-only `purpose_snapshot.py`; current intents/gaps/initiatives only; draft/proposed/terminal state excluded. Brain commit `159fe862e3728e36a48de32ac4e88fc0d3b90964`.
2. [ ] expose source/evidence refs
3. [ ] expose relationships needed by trajectory graph
4. [ ] preserve direction-owner authority
5. [ ] expose unavailable/partial state explicitly
6. [ ] avoid leaking internal storage layout into OS

Acceptance: read-only stable JSON, scope-safe, no write side effects, no duplicate Purpose store, existing Brain direction/goal tests remain green.

## Carried repair register

1. Brain release descriptor invalid/unreachable revision; repair before Purpose Brain acceptance/Core vNext.
2. Dashboard workspace-ID contract must align with canonical lowercase alnum/hyphen max 128 before Purpose Dashboard qualification.
3. OS workspace manifest schema max length should align with runtime max 128.
4. Brain trajectory refs must validate target existence/kind/scope/status before authoritative Purpose edges.
5. Data aggregate freshness must never be inferred from query execution time.
6. Final qualification must pin exact component refs.

## Resume instructions

Continue only with **Slice 3.1 / Task 2 — expose source/evidence refs**, then persist this file before Task 3.
