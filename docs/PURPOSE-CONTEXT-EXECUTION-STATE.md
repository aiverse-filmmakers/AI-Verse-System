# Purpose Context - Task-Level Execution State

**Purpose:** durable continuation checkpoint for `docs/PURPOSE-CONTEXT-IMPLEMENTATION-PLAN.md`  
**Execution law:** read the implementation plan, then this file, then active contract/closure docs. Execute in exact task order. For a bounded user-requested batch, persist each task before beginning the next.  
**Current admitted Core baseline:** `core-repaired-public-beta-2026-10-06`  
**Last updated:** 2026-10-08

> Historical task-level evidence through Slice 6.2 remains preserved in prior checkpoints and per-slice closure records. This checkpoint is intentionally compact so future continuation reads stay bounded.

## Current execution pointer

- **Phase:** 7 - Relevance gates and context-budget roll-in
- **Current slice:** **7.2 - Context budget/freshness policy**
- **Slice state:** IN PROGRESS
- **Completed slices:** 0.1, 1.1, 1.2, 1.3, 2.1, 2.2, 2.3, 3.1, 3.2, 4.1, 4.2, 4.3, 5.1, 5.2, 6.1, 6.2, 7.1
- **Closed slices:** 17 of 34
- **Closed phases:** 0, 1, 2, 3, 4, 5, 6 = 7 of 14
- **Completed Slice 7.2 tasks:** 4 of 6
- **NEXT:** **Slice 7.2 / Task 5 - define unavailable-owner behavior**
- Task 4 is complete, tested, merged, and persisted. Do not begin Task 6 until Task 5 is complete, tested, and persisted.

## Slice 7.2 task checklist

1. [x] define maximum envelope size - runtime Purpose is explicitly capped at **16,384 bytes** through `gateway.purpose-runtime-policy.v1`, matching the OS composer default. PR #42 head `f7065cfa294f1458e3eaca5341922d9d0532186f`, merged Gateway `24012566a8bbc866c681d51e2e5920569e67f25c`; Gateway CI `37825398472` PASS across Ubuntu/macOS/Windows Node 20/22 including benchmark; Context Ladder `37825398733` PASS plus runtime boundaries PASS.
2. [x] define truncation priority - OS exposes `os.purpose-budget-policy.v1` with the exact low-to-high retention order: recent material changes, risks, KPIs, narratives, current state, current work, constraints, priorities, challenges, initiatives, strategies, problems, goals, desired outcomes, missions, then trajectory. PR #53 exact head `1bb4ea254b060021d65ae6d6ef4dcc672e652b01`, merged OS `45f3734fa4bbaf64e0d72b25b694770e736b9cc1`; Direction Ownership `37828582547` PASS plus relevant OS checks PASS.
3. [x] preserve trajectory-critical fields ahead of optional rich context - OS runs a final Purpose budget pass after Data/current-state and profile enrichment, using the frozen Task-2 priority. Optional rich/material sections absorb byte pressure before retained mission, goals, strategies, initiatives, and trajectory; retained Brain canonical refs remain synchronized. PR #54 exact head `fe544c6c99d0a2ce2f1a4067fdf7aee00f64a139`, merged OS `b2e1b531402bc492e40eafbbcacddb78ec7a46b6`. Direction Ownership `37829015241` PASS including tight-budget trajectory-preservation proof.
4. [x] define refresh conditions - Gateway now enforces `gateway.purpose-refresh-policy.v1` at the Purpose read gate. Every Purpose-relevant context assembly requires a fresh owner read and Gateway projection-cache reuse is explicitly disallowed; irrelevant assemblies require no Purpose refresh/read. Repeated relevant gate invocations are proven to perform separate reads. PR #43 exact head `bec27fd4ed0aba569fb1618985b12f5a4b2318a2`, merged Gateway main as `0d784147c71695803b311c403003d964e59ec27f`. Gateway CI `37829416492` PASS across Ubuntu/macOS/Windows Node 20/22 including Ubuntu Node 22 benchmark; Context Ladder `37829416435`, Permanent Bot `37829416433`, Automation Boundary `37829416441`, and Temporary Worker `37829416608` PASS.
5. [ ] define unavailable-owner behavior
6. [ ] ensure stale cached UI/output cannot outrank a fresh owner read

## Slice 7.1 closure

**COMPLETE / ACCEPTED FOR CONTINUATION** at Gateway head `8ec510c381c22bf45056d837a6a387c9aa6c09b2`.

1. [x] deterministic Purpose relevance classification, separate from historical-depth semantics - PR #38 head `185c5960720df1a5f7ddf76881b41c1a3d9c739b`, merged `45262d1532841bb2f0118c0a83aa3085b5ca9f88`, CI `37801663497` PASS.
2. [x] irrelevant/trivial tasks perform zero Purpose reads - PR #39 head `deec866c150508d9f27c5c64ddef3b08cca24155`, merged `d4e332214d79f3fe36cfb47735497ef4c9c27d2c`; Context Ladder `37802156671` PASS plus runtime boundaries PASS.
3. [x] relevant tasks request Purpose only for the run's already-bound scope and inject the validated OS-owned projection into the existing owner-context bundle - PR #40 head `47e86d7b515fa37be3e0aaeffc11fbf8f908bba0`, merged `e7cc14531e9edcff382101e594348b6911244cb7`; CI `37824268092` PASS across Ubuntu/macOS/Windows Node 20/22 including benchmark; Context Ladder `37824268043` PASS; Permanent Bot `37824268013`, Automation Boundary `37824268046`, Temporary Worker `37824268045` PASS.
4. [x] record Purpose relevance/read/skip/size/freshness/version diagnostics without creating a second Purpose authority - `gateway.purpose-runtime-diagnostics.v1` records metadata-only relevance/read/skip, scope, projection size, OS owner, schema/profile version, generated time, owner-read count, and bounded freshness summaries. PR #41 head `ecc5349c48d80e258404a9aaa95f23c500ec8c25`, merged/final Gateway head `8ec510c381c22bf45056d837a6a387c9aa6c09b2`; Context Ladder `37824830402` PASS plus runtime boundaries PASS.

Durable closure record: `docs/PURPOSE-CONTEXT-SLICE-7.1-CLOSURE.md`, created at System commit `4a589ac3f93ef327cff02f4608400159c2a6b471`.

## Active runtime contract for Slice 7.2

1. Gateway remains runtime/context assembler only; OS remains Purpose projection owner.
2. Runtime Purpose has a hard maximum logical envelope size of **16,384 bytes**.
3. The OS request and Gateway admission boundary both enforce that same limit.
4. OS truncation priority is frozen by `os.purpose-budget-policy.v1`.
5. Final OS composition re-applies the budget after enrichment, so optional rich/material context cannot displace trajectory-critical strategic context merely because it was added later.
6. Every relevant runtime assembly requires a fresh Purpose owner read; Gateway Purpose projection-cache reuse is forbidden.
7. Irrelevant tasks continue to perform zero Purpose reads.
8. No later budget/freshness policy may create a second Purpose authority.

## Prior accepted closures

- Slice 6.2: `docs/PURPOSE-CONTEXT-SLICE-6.2-CLOSURE.md`
- Slice 6.1: `docs/PURPOSE-CONTEXT-SLICE-6.1-CLOSURE.md`
- Earlier closures remain preserved in checkpoint lineage and their closure records.

## Carried repair register

1. Dashboard workspace-ID contract must align with canonical lowercase alnum/hyphen max 128 before Purpose Dashboard qualification.
2. OS workspace manifest schema max length should align runtime max 128.
3. Data aggregate freshness must never be inferred from query execution time. **RESOLVED for the Purpose current-value path in Slice 5.1:** freshness is sourced from canonical Data record `updatedAt`.
4. Final qualification must pin exact component refs.

## Resume instructions

Continue only with **Slice 7.2 / Task 5 - define unavailable-owner behavior**. Do not begin Task 6 until Task 5 is complete, tested, and persisted.