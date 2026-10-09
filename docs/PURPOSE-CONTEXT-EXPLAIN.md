# Purpose Context Explain and Trajectory Behavior

**Status:** Core admitted  
**Core release:** `core-purpose-context-public-beta-2026-10-09`  
**Purpose Context schema:** `1.0`  
**Admitted OS contract:** `4f03849444b1d01ad81317bf0fece082d5a30e79`

Purpose Context `explain` answers how one exact semantic object connects upward through the owner-backed trajectory that is available in the requested scope. It is a read-only explanation surface. It does not invent missing relationships, mutate strategic state, or resolve foreign workspaces implicitly.

## CLI usage

```bash
node scripts/purpose-context.mjs explain \
  --scope workspace:ai-verse \
  --ref initiative:<id>
```

`--ref` is required and must be one exact semantic selector in the form:

```text
<semantic_kind>:<id>
```

Admitted semantic kinds are:

- `problem`
- `mission`
- `desired_outcome`
- `goal`
- `challenge`
- `strategy`
- `initiative`
- `kpi`
- `risk`
- `current_work`
- `material_change`

The ID must be a non-empty canonical selector ID accepted by the OS contract. Invalid selectors and selectors that do not resolve to a node in the composed Purpose projection fail closed.

## What the explanation returns

The admitted explanation result is schema `1.0` and includes:

- the requested `scope`;
- the normalized `selector`;
- the exact starting semantic object and canonical ref;
- explicit retained trajectory edges;
- reached refs and terminal refs;
- one or more deterministic explanation paths;
- explicit missing-link diagnostics;
- explicit structural-cycle rejections.

Every emitted hop preserves the exact relation plus its `from_ref`, `to_ref`, and source evidence. When the corresponding semantic nodes are present, human-readable selectors are also included for the hop endpoints.

## Upward causal explanation

The explanation path uses a bounded causal vocabulary rather than free-form inference. The admitted upward causal relations are prioritized as:

1. `executes`
2. `serves`
3. `advances`
4. `addresses`
5. `measures`

`measures` participates as an explanatory parent relation for KPI nodes. Other explicit trajectory edges may still be retained in the traversal result, but the upward explanation path is limited to the admitted causal path rules.

The purpose is explainable lineage such as:

```text
Current Work -> Initiative -> Strategy -> Goal -> Mission / higher outcome
```

The exact path depends entirely on owner-backed edges that actually exist.

## Path states and termination

A path is reported explicitly rather than silently repaired.

### Complete

A path is `complete` when traversal reaches a valid trajectory root using available owner-backed relations.

### Orphan

An `initiative` or `current_work` item with no valid parent relation is reported as an `orphan` with `trajectory_orphan` / `no_valid_parent_relation` diagnostics. Purpose does not fabricate a strategy or goal merely to make the chain look complete.

### Partial: missing parent

If an explicit edge points to a parent ref that is not available in the composed projection, the path is `partial` with termination reason `missing_parent`. The missing link is also returned separately with its exact evidence.

### Partial: scope boundary

If an explicit trajectory edge points outside the currently requested scope, the path is `partial` with termination reason `scope_boundary`. The foreign ref may be shown as the terminal ref, but Purpose does not automatically load or enumerate the foreign scope.

### Partial: cycle rejected

Structural cycles are not followed as if they were valid strategy lineage. Structural relations including `serves`, `advances`, `executes`, and `supersedes` are cycle-checked. Rejected cycle edges are exposed explicitly and affected paths terminate as `cycle_rejected`.

## Determinism and safety bounds

- relationships are sorted deterministically;
- traversal is bounded to prevent unbounded graph walks;
- selectors must resolve unambiguously;
- malformed/noncanonical relationships are filtered by the Purpose scope/relationship contract before explanation;
- workspace isolation continues to apply during explanation;
- no explanation result becomes canonical state.

## Ownership rule

`explain` first composes the current profiled Purpose Context from canonical owners, then traverses only the explicit trajectory available in that projection. It cannot create a missing goal, infer a hidden cross-workspace relationship, promote Memory history to current authority, or substitute stale OS strategy when Brain is the declared owner but unavailable.

The key rule is: **missing trajectory is reported, not hallucinated.**
