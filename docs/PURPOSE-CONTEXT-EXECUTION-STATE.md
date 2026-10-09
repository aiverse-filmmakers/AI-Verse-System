# Purpose Context - Task-Level Execution State

**Purpose:** durable continuation checkpoint for `docs/PURPOSE-CONTEXT-IMPLEMENTATION-PLAN.md`  
**Execution law:** execute in exact task order and persist each task before beginning the next.  
**Current admitted Core baseline:** `core-repaired-public-beta-2026-10-06`  
**Last updated:** 2026-10-09

## Current execution pointer

- **Phase:** 12 - Full Core requalification and new release admission
- **Current slice:** **12.3 - Cross-platform Core qualification**
- **Slice state:** IN PROGRESS
- **Completed slices:** 0.1, 1.1, 1.2, 1.3, 2.1, 2.2, 2.3, 3.1, 3.2, 4.1, 4.2, 4.3, 5.1, 5.2, 6.1, 6.2, 7.1, 7.2, 7.3, 8.1, 8.2, 9.1, 10.1, 10.2, 11.1, 11.2, 11.3, 12.1, 12.2
- **Closed slices:** 29 of 34
- **Closed phases:** 0 through 11 = 12 of 14
- **Slice 12.1:** COMPLETE / ACCEPTED
- **Slice 12.2:** COMPLETE / ACCEPTED
- **Slice 12.2 closure:** `docs/PURPOSE-CONTEXT-SLICE-12.2-CLOSURE.md`
- **NEXT:** requested batch Task 3 - Clean Machine Core Acceptance on Linux against the exact frozen Purpose candidate.

## Final frozen candidate refs

- OS: `4f03849444b1d01ad81317bf0fece082d5a30e79`
- Brain: `69f7912eeb35f0178f6952ff0554aec8d7f2c496`
- Memory: `f1327be48ba2ee0043959021365e6dbb9dcb1d3a`
- Skills: `afde5c06307fba7d074de2929c2eb6c3dc6bdab8` (unchanged)
- Data: `f8978f8f7a1bc94edecddc2662112233289159a3`

## Slice 12.1 closure evidence

- Moving-head qualification guard: Distribution PR #23, CI `37911041350` 6/6 green, merge `59e58d2c87d6d9c6a112f9e0e80765b37aa780c2`.
- OS workspace-ID repair: schema and runtime now both enforce max 128; 128 accepted and 129 rejected. OS PR #72 Repository QC `37911504828` passed all three jobs; merge `4f03849444b1d01ad81317bf0fece082d5a30e79`.
- Refreshed candidate freeze: Distribution PR #24 CI `37911706836` passed all six Ubuntu/macOS/Windows x Python 3.11/3.12 jobs; merge `4d1fb196fe163306aeedb864841a9e77440b133d`.
- Exact-SHA qualification is machine-enforced. Data dependency lock remains frozen.

## Slice 12.2 component-test evidence

- **OS COMPLETE / ACCEPTED:** exact frozen OS SHA has seven green push workflows; Direction Ownership `37911609710`, Repository QC `37911609654`.
- **Brain COMPLETE / ACCEPTED:** CI `37584271057`, OS Direction Ownership Contract `37584271029`, Skills Receipt Contract `37584271047` green.
- **Memory COMPLETE / ACCEPTED:** Test `37686666851` and Migration Handoff Atomicity `37686666811` green.
- **Data COMPLETE / ACCEPTED:** CI `37645269881`, six Node 22/24 x Ubuntu/macOS/Windows jobs green.
- **Purpose Context COMPLETE / ACCEPTED:** Direction Ownership `37911609710` broad suite and hardening `37876335706` Ubuntu/macOS/Windows green.
- **Direction/current-context/isolation COMPLETE / ACCEPTED:** exact frozen owner/isolation gates green.

## Slice 12.3 qualification evidence

**Task 1 - Distribution CI COMPLETE / ACCEPTED.** Candidate-refresh Distribution CI `37911706836` passed all six Ubuntu/macOS/Windows x Python 3.11/3.12 jobs after the final OS ref was frozen. This is the Distribution gate for the exact candidate set.

**Task 2 - Core Lineage Guard COMPLETE / ACCEPTED.** Distribution PR #25 head `f1ec32843b817308318ab683058175768bd2cddd` adds a qualification-only exact-ref lineage proof without admitting the candidate. Core Lineage Guard `37915951234` passed both the existing append-only Core lineage guard and fresh actual Git `merge-base --is-ancestor` checks for every frozen Purpose candidate component. The canonical candidate remains blocked/unreleased.

Qualification-only harness on Distribution PR #25:
- `scripts/verify-purpose-candidate-lineage.py` checks fresh ancestry from repaired baseline to each frozen component SHA.
- `scripts/prepare-purpose-candidate-qualification.py` stages the blocked candidate only inside the CI working tree as an explicit-install-only test set; no channel/default/Core-lineage admission is committed.
- `Purpose Context Core Candidate Qualification` run `37915951425` is the authoritative Linux/macOS/Windows exact-candidate clean-machine + bootstrap matrix for Tasks 3-8.

## Carried repair register

1. Dashboard workspace-ID contract alignment max 128. **RESOLVED.**
2. OS workspace manifest schema max length align runtime max 128. **RESOLVED.**
3. Data aggregate freshness path. **RESOLVED for Purpose current values.**
4. Final qualification pin exact component refs. **RESOLVED and machine-gated.**

## Current requested eight-task batch - Slice 12.3 first eight qualification checks

1. [x] Distribution CI against final frozen candidate set
2. [x] Core Lineage Guard + fresh candidate same-or-descendant verification
3. [ ] Clean Machine Core Acceptance - Linux
4. [ ] Clean Machine Core Acceptance - macOS
5. [ ] Clean Machine Core Acceptance - Windows
6. [ ] member/project bootstrap acceptance - Linux
7. [ ] member/project bootstrap acceptance - macOS
8. [ ] member/project bootstrap acceptance - Windows

**Batch progress:** 2 of 8 complete; 6 remain.

## Resume instructions

Continue only with requested batch **Task 3**. Use `Purpose Context Core Candidate Qualification` run `37915951425` as the authoritative Tasks 3-8 evidence because it stages and installs the exact frozen Purpose candidate without admitting it. Stop after Task 8; do not begin the remaining Slice 12.3 checks until the user requests continuation.
