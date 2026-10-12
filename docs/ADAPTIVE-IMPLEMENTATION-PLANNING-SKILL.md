# Adaptive Implementation Planning Skill

**Purpose:** Build implementation plans that are structured enough to stay safe and resumable, but adaptive enough to discover the real work as implementation proceeds.

Use this when starting a substantial new AI-Verse feature, subsystem, cross-repo change, migration, audit or architecture program.

## Core model

Plan at four levels:

```text
Permanent laws / non-negotiables
        ↓
Phases
        ↓
Slices with fixed outcomes + acceptance criteria
        ↓
Adaptive tasks generated/refined when each slice begins
```

Do **not** fully pre-plan every low-level task for a complex program before inspecting reality.

The plan should be stable at the level of intent and acceptance, adaptive at the level of execution.

## 1. Start from reality, not invention

Before designing implementation:

1. inspect current source, docs, contracts, tests and shipped behavior;
2. identify what already exists;
3. classify each need as `REUSE`, `EXTEND`, `CREATE`, `RETIRE` or `BLOCK/UNKNOWN`;
4. remove duplicate mechanisms from the proposed design;
5. identify canonical owners before assigning work.

Never create a new subsystem merely because the plan originally imagined one.

## 2. Define permanent laws first

Write only the non-negotiable outcomes that should survive future implementation changes.

Examples:

- preserve user-owned state;
- canonical ownership remains canonical;
- fail safely when evidence is missing;
- no silent regression;
- no duplicated source of truth.

These laws are harder to change than implementation tasks.

## 3. Build dependency-safe phases

Order phases so later work consumes proven outputs from earlier work.

Typical pattern:

```text
Audit reality
→ freeze architecture/contracts
→ build canonical control plane
→ integrate owners
→ enforce composition/delivery
→ prove end-to-end
→ close out
```

Do not automate assumptions before the audit proves them.

## 4. Make slices stable acceptance milestones

Each slice should have:

- one clear outcome;
- explicit dependencies;
- bounded repository/surface scope;
- acceptance criteria;
- required evidence;
- explicit next slice.

A slice should be small enough to reason about independently but meaningful enough that completion proves something real.

## 5. Discover tasks at slice start

Do **not** freeze all tasks for all future slices up front.

At the start of each slice:

1. read the latest plan and previous findings;
2. refresh only the live state relevant to this slice;
3. inspect existing implementation before proposing work;
4. derive the smallest task list needed to satisfy the slice acceptance criteria;
5. record that task list in the plan;
6. begin implementation only after the task list reflects current evidence.

A good first task for substantial slices is:

`X.Y.1 - Refresh current state and derive the execution tasks for this slice.`

## 6. Allow tasks to evolve from evidence

Tasks are provisional execution units.

They may be added, removed, split, merged or reordered when findings justify it.

A task should exist only because at least one is true:

- required by slice acceptance criteria;
- required by a verified finding;
- required to resolve a blocker/drift condition;
- required to test/prove an important claim;
- required to reuse/extend an existing mechanism safely.

Avoid speculative tasks whose only justification is that they sound sophisticated.

Changing tasks must not silently weaken the slice outcome or acceptance criteria.

## 7. Keep progress honest

Use slice completion for overall program percentage:

`completed slices / total slices * 100`

Use task counts only for local slice progress.

Example:

```text
Task progress: 4/7 in Slice 2.1
Slice: IN PROGRESS
Phase: 1/3 slices complete
Overall: 6/20 slices complete (30.0%)
```

If discovery adds tasks, local task progress may change. Overall program progress does not move backward because the stable unit is the slice.

## 8. Make the plan self-maintaining

Before a slice starts, update the plan with:

- `IN PROGRESS`;
- starting refs/state;
- derived task list;
- task count;
- current phase/program counters.

Before a slice can become `COMPLETE`, update the plan with:

- completed task list;
- exact implementation evidence;
- exact tests/validation;
- blockers/drift found and resolved;
- changed assumptions;
- completed/total counters and percentage;
- next slice.

The plan update itself is part of the acceptance gate.

## 9. Protect against plan drift

If implementation reveals that the roadmap itself is wrong:

- do not force reality into the old roadmap;
- stop the affected work;
- record the finding;
- change the relevant slice/phase/denominator transparently;
- preserve completed history;
- explain why the roadmap changed.

Never manipulate the denominator or task list merely to make progress look better.

## 10. Completion report

After every completed slice report:

```text
Completed: Slice X.Y - <title>
Tasks: <completed>/<derived total>
Overall: <completed>/<total> slices (<percent>%)
Phase: <phase number> - <title>
Phase progress: <completed>/<total>
Until next phase: <N> slice(s)
Next: <next slice/task>
Blockers/drift: <none or concise status>
```

## Planning principle

> **Fix the destination. Discover the safest route from current reality.**

The plan should give future agents strong boundaries and measurable outcomes without pretending that unknown implementation details are already known.