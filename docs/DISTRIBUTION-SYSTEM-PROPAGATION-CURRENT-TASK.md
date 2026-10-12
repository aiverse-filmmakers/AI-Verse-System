# Repository Network Propagation - Current Task Cursor

This is the lightweight execution entrypoint for `docs/DISTRIBUTION-SYSTEM-PROPAGATION-IMPLEMENTATION-PLAN.md`.

The long-form implementation plan remains canonical for program scope, permanent laws, acceptance criteria, completed evidence and progress accounting. This cursor exists only to prevent every execution run from loading and re-reasoning over the entire roadmap.

## Mandatory single-task execution mode

1. Read this cursor first.
2. Work on exactly one active task per run.
3. Do not pre-work later tasks or later slices.
4. Load only the files, contracts, repositories and evidence named under `Required context for this task` unless new evidence proves one more source is necessary.
5. Prefer scoped repository checks. Do not perform a full-network refresh unless the active task explicitly requires one for acceptance.
6. Do not re-audit already accepted earlier slices unless fresh evidence directly conflicts with them.
7. If live repository state disagrees with this cursor, stop implementation, record the mismatch and repair the cursor/tracker truth before advancing.
8. A task is complete only when its own acceptance is proven. Then update the canonical roadmap bookkeeping and this cursor to the next single task. Stop after that task unless explicitly asked to continue.
9. Separate AI-Verse programs may write to `AI-Verse-System/main`. Their commits are not progress in this propagation program unless this roadmap explicitly adopts them as evidence.

## Current recovery state

Program: Repository Network Governance, Release Safety and Self-Checking Implementation Plan

- Canonical roadmap: `docs/DISTRIBUTION-SYSTEM-PROPAGATION-IMPLEMENTATION-PLAN.md`
- Program progress recorded by roadmap: 11/20 slices, 55.0%
- Current slice: 4.2 - Wave 1/Core maintainer handoff
- 4.2-T1: complete
- 4.2-T2 implementation/documentation: complete in repository evidence, but canonical roadmap bookkeeping is stale
- 4.2-T3 through 4.2-T5: not proven complete

### T2 evidence already landed

- System merge commit: `7bf5e77988a866ec3c8d900c18a5bf101756a578`
- Commit purpose: exact owner adoption contract for release descriptors
- Contract Validation run: `38288410208`
- Validation result: success

The T2 merge defines the minimal owner-local acceptance/handoff pattern required by 4.2-T2: canonical descriptor validation, immutable exact-revision binding, successful native owner CI on that exact revision, fail-closed evidence handling, no duplicate acceptance system, and explicit separation from Distribution/member-release authority.

No later Core-owner adoption work has been proven as part of 4.2-T3 by the recovery check that created this cursor.

## ONE ACTIVE TASK

### 4.2-T2 bookkeeping reconciliation

Do only this:

1. Re-read the current 4.2 section of the canonical roadmap, not the whole roadmap unless required to preserve counters or protected wording.
2. Verify merge `7bf5e77988a866ec3c8d900c18a5bf101756a578` still exists on the current System lineage and workflow run `38288410208` is successful.
3. Mark 4.2-T2 complete in the canonical roadmap.
4. Change Slice 4.2 task progress from `1/5` to `2/5`.
5. Record the T2 merge and successful validation run as evidence.
6. Set the next task to `4.2-T3`.
7. Update this cursor so its ONE ACTIVE TASK becomes 4.2-T3.
8. Stop. Do not begin owner-repository implementation in the same run.

### Acceptance

- Canonical roadmap truth matches already-landed T2 evidence.
- No other task is marked complete.
- No Core owner repository is modified.
- No Repository State/ledger refresh is performed early.
- Next execution pointer is exactly 4.2-T3.

## Required context for this task

Load only:

- this cursor;
- the Slice 4.2 section and current execution pointer from `docs/DISTRIBUTION-SYSTEM-PROPAGATION-IMPLEMENTATION-PLAN.md`;
- System commit `7bf5e77988a866ec3c8d900c18a5bf101756a578`;
- Contract Validation run `38288410208`.

Do not load all five Core repositories for this bookkeeping task.

## Next task after successful reconciliation

`4.2-T3 - Implement the proven owner-local pattern in OS, Brain, Memory, Skills and Data.`

That next run must still operate as one task only. It may inspect the five owners because T3 explicitly requires them, but it must not continue into T4 or T5 in the same run.
