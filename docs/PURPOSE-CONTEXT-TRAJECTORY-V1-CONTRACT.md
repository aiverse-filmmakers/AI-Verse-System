# AI-Verse Purpose Context Trajectory v1 Contract

**Status:** IN PROGRESS — Slice 2.2  
**Parent contract:** `docs/PURPOSE-CONTEXT-V1-CONTRACT.md`  
**Canonical owner:** `AI-Verse-System`

This contract defines the bounded, explainable relationship graph used by Purpose Context. The graph is a derived projection over owner-backed refs; it is not a second strategic database.

---

## Task 1 — relation vocabulary — FROZEN

V1 relations are exactly `addresses`, `serves`, `advances`, `blocks`, `executes`, `measures`, `affects`, `supersedes`.

No free-form relation is valid. Edges require canonical evidence; similarity, embeddings, shared tags/names, co-occurrence, or model inference alone cannot create an authoritative edge.

## Task 2 — allowed source/target kinds — FROZEN

V1 node kinds: `problem`, `mission`, `desired_outcome`, `goal`, `challenge`, `strategy`, `initiative`, `kpi`, `risk`, `current_work`, `material_change`.

`narrative`, `priority`, `constraint`, `current_state` may be evidence/semantic sections but are not first-class graph nodes in v1.

Owner-backed nodes carry deterministic Purpose `node_id`, semantic kind, canonical ref and source refs. Derived nodes carry deterministic node ID, stable derivation rule and ordered source refs. Generated IDs never become canonical owner IDs.

Allowed relation matrix:

- `addresses`: mission→problem; strategy→problem|challenge; initiative→problem|challenge.
- `serves`: goal→mission|desired_outcome; initiative→goal.
- `advances`: strategy|initiative|current_work→goal|desired_outcome.
- `blocks`: challenge|risk→goal|strategy|initiative|current_work.
- `executes`: initiative→strategy; current_work→initiative|strategy.
- `measures`: kpi→goal|desired_outcome.
- `affects`: risk→mission|desired_outcome|goal|strategy|initiative|current_work; material_change→problem|mission|desired_outcome|goal|challenge|strategy|initiative|risk|current_work.
- `supersedes`: same semantic node kind only; further rules in Task 5.

Invalid kind pairs never enter the authoritative graph and are never coerced.

## Task 3 — cycle behavior — FROZEN

- Any self-edge is invalid.
- Structural ancestry relations are `serves`, `advances`, `executes`, `supersedes`; their authoritative subgraph MUST be acyclic.
- `addresses`, `blocks`, `measures`, `affects` do not define parentage, but traversal always uses visited guards.
- Cycle detection is graph-based, not “first edge wins”. Structural edges inside a multi-node strongly connected component are all cycle-involved.
- Cycle-involved structural edges are excluded from authoritative traversal; evidence refs remain in validation diagnostics; the trajectory may be marked `partial` with stable reason `trajectory_cycle_detected`.
- Purpose never silently reverses/deletes owner state or invents replacement edges.
- Explanations terminate before rejected cycle edges and disclose incomplete trajectory.
- Any `supersedes` cycle is invalid; timestamps alone cannot choose a winner.

---

## Task 4 — missing-parent behavior — FROZEN

A **missing parent** occurs when a relationship points to a target node/ref that cannot be resolved and validated under the current scope/authority contract. This is different from an **orphan** that has no parent relationship at all; orphan behavior is frozen in Task 6.

### Target resolution states

For a declared edge target, Purpose recognizes:

- `resolved` — exact target identity exists and passes kind/scope/version validation;
- `stubbed` — exact target is validated but only minimum identity/provenance is materialized because bounded projection detail was not requested or was pruned;
- `unavailable` — exact target cannot currently be read/revalidated from its owner;
- `missing` — owner confirms the exact target identity no longer exists;
- `forbidden` — target exists outside allowed scope/visibility/authority;
- `invalid` — target identity/kind/version conflicts with the edge contract.

Only `resolved` and `stubbed` targets may participate in authoritative trajectory traversal.

### Bounded identity stubs

Budget/relevance pruning MUST NOT create a fake missing-parent condition for a retained edge. If an edge is retained while target detail is pruned, retain a minimum target stub containing:

```yaml
node_id: <deterministic id>
kind: <semantic kind>
canonical_ref: <exact canonical ref>   # owner-backed node
state: stubbed
```

For a derived node, the stub retains deterministic derivation identity + source refs instead of a canonical ref.

A stub proves identity only. It MUST NOT fabricate the omitted target's descriptive content/status.

### Broken-reference handling

When the target is `unavailable`, `missing`, `forbidden`, or `invalid`:

1. the edge MUST NOT enter the authoritative traversal graph;
2. Purpose retains safe evidence/ref identity in validation diagnostics when visibility permits;
3. the trajectory section is marked `partial` if the rejected edge affects emitted trajectory content;
4. use a stable reason such as `trajectory_parent_unavailable`, `trajectory_parent_missing`, `trajectory_parent_forbidden`, or `trajectory_parent_invalid`;
5. Purpose MUST NOT fuzzy-match another node by title/name, jump to another workspace, substitute Memory history as current parent, or ask the model to invent the missing relation;
6. the canonical owner is not mutated merely because Purpose found the broken reference.

### Cross-scope privacy rule

If a target is outside the current scope and the later cross-scope contract/owner authorization does not explicitly allow visibility, classify it as `forbidden`. The projection/explanation may state that a relationship cannot be resolved under the current scope, but MUST NOT leak the hidden target's content.

### Explain behavior

If an explanation reaches a source node whose declared parent edge is rejected because the target is missing/unavailable/forbidden/invalid:

- return the verified path accumulated so far;
- terminate that branch;
- mark it incomplete with the safe resolution reason;
- do not claim the path reaches mission/problem merely because that would be likely.

If other independently valid parent branches exist, they may continue. A broken branch does not invalidate unrelated verified branches.

### Missing relation vs missing target

- **No declared parent relation exists:** not a broken ref; defer to Task 6 orphan rules.
- **Declared relation exists but target fails resolution:** this Task 4 behavior applies.

---

## Slice 2.2 progress

1. [x] relation vocabulary
2. [x] allowed source/target kinds
3. [x] cycle behavior
4. [x] missing-parent behavior
5. [ ] supersession behavior
6. [ ] orphan initiative/current-work behavior
7. [ ] explain traversal rules
8. [ ] deterministic graph ordering
