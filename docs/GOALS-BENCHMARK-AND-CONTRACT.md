# AI-Verse Persistent Goals Benchmark and Contract

**Status:** Canonical benchmarked public-beta contract  
**Date:** 2026-09-13  
**Owner split:** Brain owns goal truth; Gateway/host owns continuation execution; Automations may wake suspended/background work; Multiple Bots owns delegated coordination.

## 1. Why this contract exists

AI-Verse Persistent Goals must not be invented from a vague "keep going" feature request.

This contract synthesizes current real implementations:

- OpenAI Codex current `/goal` implementation in `openai/codex`;
- Hermes Agent Persistent Goals;
- OpenClaw Goal.

The common pattern is clear:

> A durable objective survives across turns, remains visible, has explicit lifecycle controls, uses bounded autonomous continuation, and cannot silently redefine user intent.

AI-Verse adopts that pattern while preserving AI-Verse ownership boundaries.

## 2. Benchmark findings

### OpenAI Codex

Current Codex source contains a dedicated Goal extension and goal-state migrations.

Observed current behavior includes:

- thread-scoped durable Goal state;
- `/goal [<objective>|clear|edit|pause|resume]` UI;
- statuses equivalent to active, paused, blocked, usage-limited, budget-limited and complete;
- token-budget accounting;
- time/usage reporting;
- continuation steering;
- explicit goal APIs in the app-server protocol;
- completion guidance requiring current evidence rather than intent or partial progress;
- a blocked state that is not meant to be used on the first ordinary difficulty;
- concurrent/accounting controls around goal progress.

Primary evidence:

- https://github.com/openai/codex/tree/main/codex-rs/ext/goal
- https://github.com/openai/codex/blob/main/codex-rs/state/src/model/thread_goal.rs
- https://github.com/openai/codex/blob/main/codex-rs/tui/src/goal_display.rs
- https://github.com/openai/codex/blob/main/codex-rs/ext/goal/templates/goals/continuation.md

### Hermes Agent

Hermes implements one standing Goal in a session and automatically continues after each turn.

Strong patterns:

- `/goal <text>`, draft/show/status/pause/resume/clear;
- a judge after every turn returns done, continue, blocked or wait;
- bounded continuation turn budget;
- completion contracts with outcome, verification, constraints, boundaries and stop conditions;
- mid-run subgoals/criteria;
- deterministic quality gates that must pass before an LLM judge may call work done;
- wait barriers for long-running background processes;
- user messages preempt automatic continuation;
- state persists through resume;
- new Goal replacement is protected against mid-run races;
- judge failure continues rather than wedges the session, while the hard turn budget remains the final backstop.

Primary evidence:

- https://hermes-agent.nousresearch.com/docs/user-guide/features/goals
- https://hermes-agent.nousresearch.com/docs/reference/slash-commands

### OpenClaw

OpenClaw treats Goal as durable session state, not as cron/task-queue state.

Strong patterns:

- one Goal per session;
- start/edit/status/pause/resume/complete/block/clear;
- active, paused, blocked, budget-limited, usage-limited and complete statuses;
- optional token budget;
- operator controls are stronger than model controls;
- the model may read a Goal and report complete/blocked, but it may not silently pause/resume/clear/replace it;
- start/resume are tied to run admission;
- structured Gateway mutations use goal IDs, operation IDs, timestamps and idempotent receipts;
- retries with changed payload under the same operation ID are rejected;
- stale UI controls target a Goal ID rather than whichever Goal happens to be current;
- Goal state does not itself grant tools, delivery authority, scheduling or connection permission.

Primary evidence:

- https://docs.openclaw.ai/tools/goal

## 3. What AI-Verse should copy

AI-Verse should combine:

From Codex:

- durable canonical Goal state;
- explicit lifecycle states;
- usage/budget accounting;
- continuation steering;
- strong evidence requirement for completion.

From Hermes:

- completion contracts;
- judge/evaluator loop;
- deterministic quality gates;
- subgoal/criterion tightening;
- wait/park semantics;
- bounded continuation;
- user preemption.

From OpenClaw:

- strong operator/model control separation;
- stable Goal IDs;
- idempotent Goal operations;
- stale-request protection;
- Goal not implying scheduler/tool/permission authority.

## 4. What AI-Verse should not copy

Do not copy:

- session state as the only canonical Goal store;
- automatic replacement of one user Goal with another;
- Goal state granting tool or external-action permission;
- an LLM judge as the sole completion proof when deterministic verification exists;
- unlimited continuation;
- a scheduler hidden inside Brain;
- a separate Goal database in Gateway, Dashboard or Multiple Bots;
- silent mutation of the objective by the model;
- hidden deletion of completed Goal provenance.

## 5. AI-Verse canonical ownership

### Brain owns

- Goal identity;
- objective/user intent;
- completion contract;
- additional criteria/subgoals;
- constraints and boundaries;
- declared verification requirements;
- canonical Goal lifecycle status;
- goal-level policy/budget declaration;
- progress/evaluation summaries;
- completion/block evidence references;
- provenance and version.

### Gateway/host owns

- the active run/session;
- executing continuation turns;
- run checkpoints;
- wait barriers tied to processes/provider work;
- model invocation;
- tool execution;
- cancellation;
- actual usage counters before they are committed/referenced by Brain;
- execution-time enforcement of budget/deadline;
- admission/idempotency for run operations.

### Automations owns

- future scheduled wake;
- recurring Goal review/wake if configured;
- timer/event wake for a parked background Goal.

### Multiple Bots owns

- delegated Tasks, Team Runs and temporary Workers created to advance a Goal;
- their leases, budgets, approvals and coordination.

A Bot Task may reference a Brain Goal ID. It does not become the Goal owner.

## 6. Canonical Goal model

A public-beta Goal should have at least:

```json
{
  "goal_id": "goal_...",
  "scope": {
    "system_id": "...",
    "workspace_id": "... optional",
    "operator_id": "... optional"
  },
  "objective": "...",
  "status": "active",
  "completion_contract": {
    "outcome": "...",
    "verification": [],
    "constraints": [],
    "boundaries": [],
    "stop_when": []
  },
  "criteria": [],
  "budget_policy": {
    "max_turns": null,
    "max_tokens": null,
    "max_cost": null,
    "deadline": null
  },
  "progress": {
    "attempts": 0,
    "last_evaluation": null
  },
  "version": 1,
  "created_at": "...",
  "updated_at": "...",
  "provenance": {}
}
```

Exact storage schema remains Brain-owned implementation detail.

## 7. Lifecycle

Canonical public statuses:

```text
active
paused
blocked
budget_limited
usage_limited
complete
cleared
```

`cleared` is a retained terminal/provenance state, not required to mean physical deletion.

Transitions must be deterministic and version checked.

Expected user UX:

```text
/goal <objective>
/goal draft <objective>
/goal status
/goal show
/goal edit <objective>
/goal pause [note]
/goal resume [note]
/goal block [note]
/goal complete [note]
/goal clear
/subgoal <criterion>
/subgoal remove <n>
/subgoal clear
```

Natural-language equivalents may call the same owner API.

## 8. Operator versus model authority

### Operator/client may

- create;
- edit objective;
- pause;
- resume;
- clear;
- add/remove criteria;
- change verification contract;
- change declared budgets within outer policy.

### Agent/model may

- read current Goal;
- propose a Goal only when user/system policy explicitly allows;
- submit progress evidence;
- request evaluation;
- propose `complete`;
- propose `blocked`;
- request a wait/park state from Gateway.

### Agent/model may not

- silently replace objective;
- clear the Goal;
- weaken constraints;
- broaden boundaries;
- increase permissions;
- increase outer budget/policy;
- auto-resume an operator pause without a valid wake/resume authority.

Brain's deterministic policy decides whether a model proposal changes canonical Goal state.

## 9. Completion and continuation

The loop is:

```text
Goal active
-> Gateway admits one bounded run/turn
-> work executes
-> evidence/result returned
-> Brain evaluates current Goal against contract
-> deterministic gates evaluated where available
-> Brain verdict
     CONTINUE
     COMPLETE
     BLOCKED
     WAIT
-> Gateway either continues, parks, or stops
```

Brain's evaluator output is not hidden reasoning. It is a bounded structured verdict with evidence references and rationale.

Recommended verdict envelope:

```json
{
  "goal_id": "...",
  "goal_version": 7,
  "verdict": "continue|complete|blocked|wait",
  "reason": "...",
  "evidence_refs": [],
  "unmet_criteria": [],
  "wait_hint": null
}
```

## 10. Deterministic verification gates

Where completion can be tested mechanically, Goal should support declared gates such as:

- command/test exits 0;
- required artifact exists;
- owner-reported state equals desired value;
- CI/release status succeeds;
- structured Data query satisfies condition.

Brain owns the verification requirement.

Gateway/host executes the permitted check through owner/tool boundaries.

A failing deterministic gate blocks `complete` regardless of an LLM evaluator's opinion.

## 11. Budget and loop controls

Public beta must support bounded continuation.

At least one hard backstop is mandatory.

Recommended independent limits:

- maximum continuation turns;
- token budget;
- cost budget when Token is available;
- wall-clock deadline;
- no-progress detection;
- repeated blocker threshold;
- human pause/cancel.

Hitting a budget pauses/limits the Goal. It must never be reclassified as complete merely because resources ended.

## 12. Wait/park behavior

Waiting is execution state, not a new Goal owner.

Gateway may park an active Goal on:

- background process;
- CI/build completion;
- provider task;
- explicit timer;
- external event handle.

The Goal remains canonical in Brain.

A future wake is owned by Automations when a scheduler/event wake is required.

Stale waits must have expiry/recovery behavior.

## 13. Idempotency and races

Every mutating public Goal operation should carry:

- goal ID when one exists;
- operation/request ID;
- expected Goal version or equivalent optimistic concurrency token;
- issue timestamp/expiry where remote;
- actor/principal provenance.

Replaying an identical successful request should not duplicate mutation.

Reusing an operation ID with changed payload must fail.

A stale client must not edit/clear a replacement Goal.

## 14. Gateway API contract

Gateway should consume owner APIs equivalent to:

```text
goal.get(scope/context)
goal.create(request)
goal.edit(goal_id, expected_version, request)
goal.transition(goal_id, expected_version, action, note)
goal.criteria.add/remove/clear(...)
goal.evaluate(goal_id, expected_version, evidence)
```

Exact transport names may vary.

Gateway does not write Brain storage directly.

## 15. Multiple Goals

Brain may own many strategic Goals across scopes.

The interactive `/goal` UX should bind at most one **standing execution Goal per user-facing session/run context** at a time.

This preserves the successful Codex/Hermes/OpenClaw UX while allowing Brain's broader strategic model to contain multiple long-horizon objectives.

## 16. Public-beta acceptance

The Goal feature is ready only when tests prove:

- create/status/edit/pause/resume/block/complete/clear;
- restart persistence;
- objective cannot be silently replaced;
- user message/control preempts continuation;
- bounded continuation;
- budget-limit behavior;
- deterministic gate blocks false completion;
- stale/idempotent requests;
- completion evidence requirement;
- blocked behavior;
- wait/park/recovery;
- no permission expansion;
- no second Goal store in Gateway/Bots/Dashboard;
- one real end-to-end Goal finishes through the supported Gateway/runtime path.

## 17. Sources

- OpenAI Codex current repository: https://github.com/openai/codex
- Hermes Persistent Goals: https://hermes-agent.nousresearch.com/docs/user-guide/features/goals
- Hermes Slash Commands: https://hermes-agent.nousresearch.com/docs/reference/slash-commands
- OpenClaw Goal: https://docs.openclaw.ai/tools/goal
