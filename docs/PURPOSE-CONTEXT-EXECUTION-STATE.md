# Purpose Context - Task-Level Execution State

**Purpose:** durable continuation checkpoint for `docs/PURPOSE-CONTEXT-IMPLEMENTATION-PLAN.md`  
**Execution law:** execute in exact task order and persist each task before beginning the next.  
**Current admitted Core baseline:** `core-repaired-public-beta-2026-10-06`  
**Last updated:** 2026-10-09

## Current execution pointer

- **Phase:** 12 - Full Core requalification and new release admission
- **Current slice:** **12.2 - Component tests**
- **Slice state:** IN PROGRESS
- **Completed slices:** 0.1, 1.1, 1.2, 1.3, 2.1, 2.2, 2.3, 3.1, 3.2, 4.1, 4.2, 4.3, 5.1, 5.2, 6.1, 6.2, 7.1, 7.2, 7.3, 8.1, 8.2, 9.1, 10.1, 10.2, 11.1, 11.2, 11.3, 12.1
- **Closed slices:** 28 of 34
- **Closed phases:** 0 through 11 = 12 of 14
- **Slice 12.1:** COMPLETE / ACCEPTED
- **Slice 12.1 closure:** `docs/PURPOSE-CONTEXT-SLICE-12.1-CLOSURE.md`
- **NEXT:** requested batch Task 8 - all direction-owner/current-context/workspace-isolation regressions

## Final frozen candidate refs

- OS: `4f03849444b1d01ad81317bf0fece082d5a30e79`
- Brain: `69f7912eeb35f0178f6952ff0554aec8d7f2c496`
- Memory: `f1327be48ba2ee0043959021365e6dbb9dcb1d3a`
- Skills: `afde5c06307fba7d074de2929c2eb6c3dc6bdab8` (unchanged)
- Data: `f8978f8f7a1bc94edecddc2662112233289159a3`

## Slice 12.1 closure evidence

- Moving-head qualification guard: Distribution PR #23, CI `37911041350` 6/6 green, merge `59e58d2c87d6d9c6a112f9e0e80765b37aa780c2`.
- OS workspace-ID repair: schema and runtime now both enforce max 128; 128 accepted and 129 rejected. OS PR #72 Repository QC `37911504828` passed all three jobs; merge `4f03849444b1d01ad81317bf0fece082d5a30e79`.
- Refreshed OS lineage: baseline `e74a4e05b1f891e6f871f34a298bf10363a11d88` -> frozen candidate `4f03849444b1d01ad81317bf0fece082d5a30e79`, ahead 164 / behind 0.
- Refreshed candidate freeze: Distribution PR #24 CI `37911706836` passed all six Ubuntu/macOS/Windows x Python 3.11/3.12 jobs; merge `4d1fb196fe163306aeedb864841a9e77440b133d`.
- Exact-SHA policy remains machine-enforced and Data dependency lock remains unchanged/frozen.

## Slice 12.2 component-test evidence

**OS regression suite COMPLETE / ACCEPTED.** Frozen OS SHA `4f03849444b1d01ad81317bf0fece082d5a30e79` has exactly seven push-triggered workflow runs and all seven are completed successfully. The exact-SHA success query returned `total_count: 7`, matching the unfiltered exact-SHA run count of 7. This includes Direction Ownership run `37911609710`. In addition, repair PR Repository QC `37911504828` passed all three jobs (`qc`, `adapter-integration`, `skills-provider-integration`).

**Brain regression suite COMPLETE / ACCEPTED.** Frozen Brain SHA `69f7912eeb35f0178f6952ff0554aec8d7f2c496` has exactly three push-triggered workflow runs and all three are completed successfully: CI `37584271057`, OS Direction Ownership Contract `37584271029`, and Skills Receipt Contract `37584271047`. The exact-SHA success count is 3, matching the unfiltered exact-SHA run count of 3.

**Memory regression suite COMPLETE / ACCEPTED.** Frozen Memory SHA `f1327be48ba2ee0043959021365e6dbb9dcb1d3a` has exactly two push-triggered workflow runs and both are completed successfully: Test `37686666851` and Migration Handoff Atomicity `37686666811`. The exact-SHA success count is 2, matching the unfiltered exact-SHA run count of 2.

**Data regression suite COMPLETE / ACCEPTED.** Frozen Data SHA `f8978f8f7a1bc94edecddc2662112233289159a3` has one exact-SHA CI run, `37645269881`, and it completed successfully. Its full matrix is six green jobs: Node 22 and Node 24 across Ubuntu, macOS, and Windows. Every matrix job passed build/test, package smoke, CLI smoke, and install smoke.

**Purpose Context regression suite COMPLETE / ACCEPTED for Slice 12.2.** The exact frozen OS SHA Direction Ownership run `37911609710` passed every Purpose regression carried by that workflow: ownership-aware reads, envelope, budget/truncation, final budget, no-cache, fail-closed owner behavior, delete/rebuild/restart, profiles, rich domains, initiative operational status, explicit relationships, workspace boundary attacks, explain traversal, Data current-value/current-state/source descent, Memory history boundary/bounded read, material-change classifier/provenance/relevance, and canonical strategic writer/reader gates. The final Purpose hardening matrix `37876335706` passed on Ubuntu, macOS, and Windows and covers rebuildability hardening, security hardening, Data/Memory scope boundaries, exact-source permission descent, action permissions, and semantic acceptance Scenarios 1-12. That hardening run is on final Purpose head `e67b321c9d09c320eddc8121f18efa3fbd8ba621`; compare-to-frozen evidence proves the only later OS changes are `system/schemas/workspace.schema.yaml` and `scripts/test-workspace-owner.mjs`, with zero Purpose implementation/test changes. Those two later files are themselves green in exact frozen OS regression evidence. No Purpose regression remains open. Final same-head composed qualification is still required in Slice 12.3 and is not being claimed here.

## Carried repair register

1. Dashboard workspace-ID contract alignment max 128. **RESOLVED.**
2. OS workspace manifest schema max length align runtime max 128. **RESOLVED.**
3. Data aggregate freshness path. **RESOLVED for Purpose current values.**
4. Final qualification pin exact component refs. **RESOLVED and machine-gated.**

## Current requested eight-task batch

1. [x] enforce exact-SHA-only qualification, never moving branch heads
2. [x] resolve OS workspace manifest ID max-length mismatch and refresh frozen OS candidate/ref evidence
3. [x] full OS regression suite
4. [x] full Brain regression suite
5. [x] full Memory regression suite
6. [x] full Data regression suite
7. [x] all Purpose Context tests
8. [ ] all direction-owner/current-context/workspace-isolation regressions

**Batch progress:** 7 of 8 complete; 1 remains.

## Resume instructions

Continue only with requested batch **Task 8**. All qualification evidence must correspond to the exact frozen candidate refs above.
