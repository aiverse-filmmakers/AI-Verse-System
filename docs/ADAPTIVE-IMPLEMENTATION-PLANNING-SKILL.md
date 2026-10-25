# Adaptive Implementation Planning Skill

**Purpose:** Produce implementation plans that guide the smallest maintainable change that fully resolves the agreed problem, while preserving existing infrastructure, user state and authority boundaries.

Use for AI-Verse features, repairs, integrations, migrations and architecture work. One living plan may serve as the product brief, architecture decision and execution record; do not create separate documents merely to satisfy a format. Planning does not grant implementation, test, publication or release permission.

## 1. Choose the depth before the structure

Use the shortest plan that covers the actual decisions and risks. This rule governs every section below, including task tracking, reviews and completion reports.

| Depth | Use when | Sufficient content |
|---|---|---|
| Compact | A bounded change with a known owner and no material contract, state, permission or recovery change | Problem, existing path, smallest change, preserved behavior, relevant verification and next action |
| Standard | New behavior or several interacting modules | Compact content plus the important requirements, design choice, dependencies and necessary slices |
| Extended | Multiple owners, persistent-state migration, public contracts, permissions or difficult recovery | Standard content plus the affected contracts, compatibility, preservation/recovery and owner/composed acceptance |

A compact plan can be short prose. Use phases, requirement IDs, tables, counters and formal reports only when they improve execution of a substantial program. Omit irrelevant fields without filling them with N/A explanations. Do not impose word counts, line-of-code targets or a minimum number of tasks.

The [Implementation Plan Template](IMPLEMENTATION-PLAN-TEMPLATE.md) is a starting point, not a form to complete. Link existing rules and evidence rather than copying them.

## 2. Start from observed behavior

Before choosing a design:

1. Identify the user's problem, intended behavior, scope and non-goals.
2. Inspect the relevant source, callers, tests, contracts and prior accepted work. Retrieve only what the decision needs.
3. Trace the current caller through validation, owner effects and result/error. Identify the canonical owner and useful code entry points.
4. Distinguish confirmed observations from assumptions, unresolved decisions and genuinely unavailable evidence.
5. Classify the needed work as `REUSE`, `EXTEND`, `CREATE`, `RETIRE` or `BLOCK/UNKNOWN`.

Do not infer working behavior from a plan, registry entry, interface name or passing unrelated test. Do not reconstruct accepted infrastructure merely because an earlier proposal imagined something different.

Inspect bounded implementation questions before asking the operator. Make routine choices within existing authority; ask when a material product, ownership, permission, preservation or external-action decision remains unresolved.

## 3. Choose the smallest complete change

Prefer configuration, correction, wiring or extension at the existing owner. A verified no-code resolution is valid when existing behavior already satisfies the requirement.

Add a dependency, service, store, abstraction or configuration surface only when a current requirement cannot be met adequately by the existing mechanisms. Explain that reason and the simpler alternative briefly. Apply a deletion test: if removing a proposed layer still meets the requirement safely, omit it.

Exclude unrelated cleanup, speculative refactors, generic frameworks and capabilities for hypothetical future needs. Record useful follow-up ideas separately; they do not become required implementation work.

Optimize for the smallest maintainable change that fully meets acceptance, not the fewest literal lines. A shortcut that hides errors, breaks another caller or bypasses authority is not a complete fix. Follow established codebase patterns and address the actual cause rather than masking symptoms.

State the important behavior, contracts and data that must survive. Preserve canonical ownership, user-owned state, workspace/member isolation, authorization and recovery guarantees. Link established laws instead of restating them in each slice.

## 4. Define observable acceptance once

Record the important requirements and how to prove them. Use stable IDs for multi-slice work so slices can reference the same acceptance rather than repeat it.

For each relevant behavior, identify the successful result, meaningful failure/regression and the existing command or user action that can verify it. Include the expected outcome. For user-facing changes, exercise the real caller or user journey where needed; unit tests alone may not establish the product behavior.

Improve verification of agreed requirements and concrete risks within the authorized change. Better proof is not permission to add product obligations: extra features, platforms, infrastructure, benchmarks or quality targets require an explicit scope decision before becoming mandatory.

Screen applicable risks once, beside the affected design: ownership/permissions, privacy/untrusted input, persistence/concurrency, compatibility/platforms and failure/recovery. Include AI-specific scope, context-budget or evaluation risks only where relevant. Risk discovery must not turn into an unsolicited feature checklist.

Use established performance, accessibility, resource and cost requirements when they apply. If a necessary target is unknown, plan a bounded measurement or decision; do not invent a number or a benchmark program.

## 5. Sequence useful, complete increments

A neutral default is:

`inspect -> smallest complete change -> integrate and verify -> deliver`

Architecture, migration or qualification stages belong only where the actual work needs them. Where useful, prove an early narrow path from the real caller to the actual result before expanding the implementation. Do not create foundations without an evidenced requirement.

For substantial work, organize the plan as:

`non-negotiable outcomes -> necessary phases -> stable slices -> adaptive tasks`

Each slice has one meaningful outcome, dependencies, a bounded owner/surface, referenced acceptance, required evidence and a next step. State rollout/recovery details only where they differ from the established plan. Shared evidence may prove several criteria; do not repeat the same check merely to fill several rows.

Keep distant slices at outcome/dependency level. Do not freeze speculative implementation tasks for the whole program.

## 6. Derive tasks when a slice starts

At the start of a substantial slice:

1. Read its current checkpoint and refresh only relevant source/evidence.
2. Reuse existing implementation and accepted work before proposing additions.
3. Record the smallest task list that satisfies the slice outcome and mark it `IN PROGRESS`.
4. Identify the first useful behavior to implement or characterize and its verification path.

Tasks may be added, removed, split, combined or reordered when evidence warrants it. Every task must serve agreed acceptance, a concrete risk/defect, a real dependency or a useful verification. Prefer `REUSE` or `EXTEND` when discovery removes the need for `CREATE`.

Task adaptation may change the route; it must not silently move the finish line.

## 7. Preserve direction and authority

Routine implementation choices and stronger proof of existing requirements can adapt within scope. An agent must not silently:

- change product intent, canonical ownership or permissions;
- weaken acceptance, safety, preservation, isolation or required evidence;
- add new product obligations under the label of stricter acceptance;
- change a phase/slice outcome, remove a required slice or alter a program denominator or major ordering;
- promote an experimental finding into canonical architecture without the relevant acceptance.

First inspect whether an apparent conflict can be resolved within existing rules. If a material directional change remains necessary, stop only the affected implementation path and record `BLOCKED - PLAN AMENDMENT REQUIRED` with:

- the observed finding and current requirement/law;
- the proposed change, affected owners/slices and preservation/compatibility impact;
- the smaller alternatives and recommended resolution.

Resolve the amendment through the program's existing approval process, then update the plan/changelog and affected counters before resuming. Preserve the earlier decision and evidence. Do not create new approval ceremonies for routine choices or ignore authorization already supplied by the operator.

**Discovery may reduce unnecessary work. It may not reduce safety, ownership, preservation, member isolation or required evidence.**

## 8. Implement and verify proportionally

Respect the operator's authorization for commands and checks. A planned check is not an executed check; if checks are deferred or forbidden, record that limit and do not claim verified completion.

For a defect, use a meaningful failing regression before the fix when practical. Then implement the smallest complete behavior, verify and simplify. Do not manufacture failing tests for documentation or pure cleanup. Reuse useful existing tests; add only those needed to establish the changed behavior or a concrete regression risk.

When the cause is uncertain, reproduce the behavior, probe one falsifiable explanation at a time, remove temporary diagnostics and rerun the original case. Do not weaken assertions, swallow errors or substitute success-shaped fallbacks to make checks pass.

Run required owner checks and the checks justified by the change. Broaden or repeat them only when new edits, failures or unresolved risks warrant it. Separate source acceptance, composed qualification and member release; none implies the others. Preserve existing rollback and user-state guarantees.

## 9. Keep one useful execution record

Update the living plan with what changed, what was actually verified, unresolved material decisions and the next action. Link detailed logs and exact relevant refs; avoid accumulating repetitive narration or a second handoff document.

For multi-slice programs, report completed slices over the fixed total. Task counts describe only the current slice. Do not manipulate denominators, acceptance or task lists to improve the apparent percentage. A blocked amendment is not completed work.

A completed slice records implementation and acceptance evidence, remaining limitations and its next step. Use a concise report scaled to the program; compact changes do not require phase percentages or a fixed report template. A fresh agent should be able to resume without re-reading the entire history.

Issue drafts may be derived from accepted slices when useful. Publishing them, making external changes and promoting releases still follow existing authorization. This method creates no new permissions.

## Planning principle

**Fix the destination. Discover the smallest safe route from current reality.**
