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
- **Completed Slice 7.2 tasks:** 1 of 6
- **NEXT:** **Slice 7.2 / Task 2 - define truncation priority**
- Execute Slice 7.2 in exact task order. Do not begin Task 2 until Task 1 is complete, tested, and persisted. Task 1 is now complete and persisted; continuation begins with Task 2.

## Slice 7.2 task checklist

1. [x] define maximum envelope size - runtime Purpose is now explicitly capped at **16,384 bytes** through `gateway.purpose-runtime-policy.v1`, matching the existing OS Purpose composer default. Gateway passes `--max-bytes 16384` to the OS owner and independently measures the returned logical projection before admission; owner output above the hard runtime cap fails closed with `PURPOSE_CONTEXT_BUDGET_EXCEEDED` rather than silently entering model context. This task deliberately does not prune or truncate; priority order remains Task 2. PR #42 exact head `f7065cfa294f1458e3eaca5341922d9d0532186f` merged to Gateway main as `24012566a8bbc866c681d51e2e5920569e67f25c`. Gateway CI `37825398472` PASS across Ubuntu, macOS, and Windows on Node 20/22 including the Ubuntu Node 22 benchmark. Context Ladder Integrated Acceptance `37825398733` PASS; Permanent Bot Composition `37825398632` PASS; Automation Recommendation Boundary `37825398458` PASS; Temporary Worker Composition `37825399734` PASS.
2. [ ] define truncation priority
3. [ ] preserve trajectory-critical fields ahead of optional rich context
4. [ ] define refresh conditions
5. [ ] define unavailable-owner behavior
6. [ ] ensure stale cached UI/output cannot outrank a fresh owner read

## Slice 7.1 closure

**COMPLETE / ACCEPTED FOR CONTINUATION** at Gateway head `8ec510c381c22bf45056d837a6a387c9aa6c09b2`.

1. [x] deterministic Purpose relevance classification, separate from historical-depth semantics - PR #38 head `185c5960720df1a5f7ddf76881b41c1a3d9c739b`, merged `45262d1532841bb2f0118c0a83aa3085b5ca9f88`, CI `37801663497` PASS.
2. [x] irrelevant/trivial tasks perform zero Purpose reads - PR #39 head `deec866c150508d9f27c5c64ddef3b08cca24155`, merged `d4e332214d79f3fe36cfb47735497ef4c9c27d2c`; Context Ladder `37802156671` PASS plus runtime boundaries PASS.
3. [x] relevant tasks request Purpose only for the run's already-bound scope and inject the validated OS-owned projection into the existing owner-context bundle - PR #40 head `47e86d7b515fa37be3e0aaeffc11fbf8f908bba0`, merged `e7cc14531e9edcff382101e594348b6911244cb7`; CI `37824268092` PASS across Ubuntu/macOS/Windows Node 20/22 including benchmark; Context Ladder `37824268043` PASS; Permanent Bot `37824268013`, Automation Boundary `37824268046`, Temporary Worker `37824268045` PASS.
4. [x] record Purpose relevance/read/skip/size/freshness/version diagnostics without creating a second Purpose authority - `gateway.purpose-runtime-diagnostics.v1` records metadata-only relevance/read/skip, scope, projection size, OS owner, schema/profile version, generated time, owner-read count, and bounded freshness summaries. PR #41 head `ecc5349c48d80e258404a9aaa95f23c500ec8c25`, merged/final Gateway head `8ec510c381c22bf45056d837a6a387c9aa6c09b2`; Context Ladder `37824830402` PASS plus runtime boundaries PASS. CI `37824830376` passed macOS 20/22, Ubuntu 20/22 including benchmark, and Windows 22; Windows 20 stalled in GitHub `setup-node` before project execution.

Durable closure record: `docs/PURPOSE-CONTEXT-SLICE-7.1-CLOSURE.md`, created at System commit `4a589ac3f93ef327cff02f4608400159c2a6b471`.

## Active runtime contract for Slice 7.2

1. Gateway remains runtime/context assembler only; OS remains Purpose projection owner.
2. Runtime Purpose has a hard maximum logical envelope size of **16,384 bytes**.
3. The OS request and Gateway admission boundary both enforce that same limit.
4. Oversized owner output fails closed until Task 2 defines deterministic truncation priority.
5. Irrelevant tasks continue to perform zero Purpose reads.
6. No later budget policy may create a second Purpose authority or allow optional rich context to outrank owner-backed trajectory-critical context.

## Prior accepted closures

- Slice 6.2: `docs/PURPOSE-CONTEXT-SLICE-6.2-CLOSURE.md`
- Slice 6.1: `docs/PURPOSE-CONTEXT-SLICE-6.1-CLOSURE.md`
- Earlier closures remain preserved in checkpoint lineage and their closure records.

## Carried repair register

1. Dashboard workspace-ID contract must align with canonical lowercase alnum/hyphen max 128 before Purpose Dashboard qualification.
2. OS workspace manifest schema max length should align with runtime max 128.
3. Data aggregate freshness must never be inferred from query execution time. **RESOLVED for the Purpose current-value path in Slice 5.1:** freshness is sourced from canonical Data record `updatedAt`.
4. Final qualification must pin exact component refs.

## Resume instructions

Continue only with **Slice 7.2 / Task 2 - define truncation priority**. Do not begin Task 3 until Task 2 is complete, tested, and persisted.