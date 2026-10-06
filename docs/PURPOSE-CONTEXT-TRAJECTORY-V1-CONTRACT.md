# AI-Verse Purpose Context Trajectory v1 Contract

**Status:** COMPLETE — Slice 2.2 contract frozen  
**Parent contract:** `docs/PURPOSE-CONTEXT-V1-CONTRACT.md`  
**Canonical owner:** `AI-Verse-System`

This contract defines the bounded, explainable relationship graph used by Purpose Context. The graph is a derived projection over owner-backed refs; it is not a second strategic database.

---

## Task 1 — relation vocabulary — FROZEN

V1 relations are exactly `addresses`, `serves`, `advances`, `blocks`, `executes`, `measures`, `affects`, `supersedes`. No free-form relation is valid. Edges require canonical evidence; similarity, embeddings, shared tags/names, co-occurrence, or model inference alone cannot create an authoritative edge.

## Task 2 — allowed source/target kinds — FROZEN

V1 node kinds: `problem`, `mission`, `desired_outcome`, `goal`, `challenge`, `strategy`, `initiative`, `kpi`, `risk`, `current_work`, `material_change`.

Allowed relation matrix:
- `addresses`: mission→problem; strategy→problem|challenge; initiative→problem|challenge.
- `serves`: goal→mission|desired_outcome; initiative→goal.
- `advances`: strategy|initiative|current_work→goal|desired_outcome.
- `blocks`: challenge|risk→goal|strategy|initiative|current_work.
- `executes`: initiative→strategy; current_work→initiative|strategy.
- `measures`: kpi→goal|desired_outcome.
- `affects`: risk→mission|desired_outcome|goal|strategy|initiative|current_work; material_change→problem|mission|desired_outcome|goal|challenge|strategy|initiative|risk|current_work.
- `supersedes`: same semantic node kind only.

Invalid kind pairs never enter the authoritative graph and are never coerced.

## Task 3 — cycle behavior — FROZEN

Any self-edge is invalid. Structural ancestry relations are `serves`, `advances`, `executes`, `supersedes`; their authoritative subgraph must be acyclic. Structural edges inside a multi-node strongly connected component are excluded from authoritative traversal and reported as partial with stable diagnostics. Purpose never silently reverses/deletes owner state or invents replacement edges.

## Task 4 — missing-parent behavior — FROZEN

Target states are `resolved`, `stubbed`, `unavailable`, `missing`, `forbidden`, `invalid`; only `resolved` and `stubbed` targets participate in authoritative traversal. Bounded pruning retains identity stubs for retained edges. Broken targets never fuzzy-match, cross workspace boundaries, substitute Memory as current truth, or invoke model inference. Explanation stops at the last verified node of a broken branch.

## Task 5 — supersession behavior — FROZEN

`supersedes` is owner-confirmed historical replacement evidence only. Same-kind source/target required; timestamps, version numbers, titles, similarity and model judgment never infer replacement. Currentness remains defined by the active canonical owner, not chain position. Competing unresolved replacements remain ambiguous. Supersession may be explanation context but is not normal causal ascent.

## Task 6 — orphan initiative/current-work behavior — FROZEN

A valid initiative/current-work node with no valid parent relation is allowed and remains visible when relevant. It is marked `linkage_state: orphan` / `linkage_reason: no_valid_parent_relation`. Purpose never invents a parent. Explain stops causal ascent at the orphan and returns stable reason `trajectory_orphan`. Tiny workspaces may legitimately remain this simple.

## Task 7 — explain traversal rules — FROZEN

Explain starts from one exact node and ascends only validated causal edges. Normal parent-relation priority is `executes`, then `serves`, then `advances`, then `addresses`; `measures` participates only for KPI starts/branches. `blocks`, `affects`, and `supersedes` are contextual attachments, not normal causal parents.

Multiple valid parents create multiple branches. One deterministic branch may be labeled primary, but no valid branch is deleted merely for convenience. Branches terminate at legitimate roots, orphans, broken parents, cycle rejection, authority/scope boundary, or traversal budget. Returned branches distinguish `complete`, `partial`, and `orphan`. No prose or model inference may add a relationship absent from the verified graph.

## Task 8 — deterministic graph ordering — FROZEN

Graph materialization, pruning, diffing, explain output, and tests MUST use deterministic order independent of storage/API arrival order.

### Node kind order

Top-level graph node order is:

```text
problem
mission
desired_outcome
goal
challenge
strategy
initiative
kpi
risk
current_work
material_change
```

Within a kind:

1. canonical owner-declared priority/rank/order, when the owner explicitly exposes one for those objects;
2. canonical ref identity tuple `(owner, scope, kind, id)` ascending;
3. ref `version` ascending only as a final deterministic tie-breaker for duplicate observed revisions;
4. derived nodes: stable derivation-rule ID, then ordered source-ref identities, then deterministic `node_id`.

Owner/API arrival order, filesystem order, database row order, model generation order, and map/object iteration order are never semantic ordering.

### Edge relation order

Canonical graph edge order is:

```text
addresses
serves
advances
blocks
executes
measures
affects
supersedes
```

Within the same relation:

1. source node deterministic order;
2. target node deterministic order;
3. ordered canonical evidence refs;
4. deterministic derivation-rule ID when applicable.

This serialization order does not redefine explain primary-parent priority from Task 7.

### Explain branch order

For causal ascent, parent branches sort by:

1. Task 7 parent-relation priority: `executes`, `serves`, `advances`, `addresses`, then KPI `measures`;
2. owner-declared strategic rank/priority when applicable;
3. target node deterministic order;
4. edge evidence-ref order.

The first branch after that ordering may be labeled `primary`. The label is a deterministic rendering choice, not stronger strategic authority.

### Context attachment order

Contextual attachments sort by relation order, then source node order. `material_change` attachments may use canonical owner event/effective time descending only when that timestamp is owner-backed; ties fall back to canonical ref ordering.

### Deterministic pruning

When budget requires graph pruning:

- use the frozen envelope pruning policy;
- prune secondary/context branches in deterministic reverse-priority order;
- retained edges keep minimum target identity stubs where required;
- identical owner inputs + scope + profile + budget produce the same retained graph and same omission decisions, excluding volatile observation timestamps.

### Equality/deduplication

Two owner-backed nodes are the same logical node only when their canonical identity tuple matches. Two edges are duplicates only when source identity, relation, target identity, and authoritative evidence/derivation identity are equivalent. Display text equality alone never deduplicates graph objects.

---

## Slice 2.2 final status

1. [x] relation vocabulary
2. [x] allowed source/target kinds
3. [x] cycle behavior
4. [x] missing-parent behavior
5. [x] supersession behavior
6. [x] orphan initiative/current-work behavior
7. [x] explain traversal rules
8. [x] deterministic graph ordering

**Slice 2.2: COMPLETE / CONTRACT FROZEN.**

Acceptance verdict:
- graph can trace verified current work upward without inventing missing relationships: PASS;
- relation kinds and source/target semantics bounded: PASS;
- broken/orphan/cycle paths fail visibly rather than being repaired by inference: PASS;
- explain traversal deterministic and bounded: PASS;
- graph remains derived and owner-backed: PASS.

**NEXT:** Slice 2.3 / Task 1 — freeze operator default shape.
