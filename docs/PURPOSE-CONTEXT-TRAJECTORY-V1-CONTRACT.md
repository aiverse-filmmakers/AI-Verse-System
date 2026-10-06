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

## Task 4 — missing-parent behavior — FROZEN

A missing parent is a declared relationship whose target cannot be resolved and validated. It differs from an orphan, which has no parent relation at all.

Target states are exactly `resolved`, `stubbed`, `unavailable`, `missing`, `forbidden`, `invalid`. Only `resolved` and `stubbed` targets participate in authoritative traversal.

If bounded pruning removes target detail for a retained edge, Purpose keeps a minimum identity stub rather than creating a fake missing parent. A broken target never fuzzy-matches by title/name, crosses workspace boundaries, substitutes Memory as current truth, or invokes model inference to repair the path.

When a broken parent is encountered, explanation returns the verified path so far, stops that branch, and marks the branch incomplete with a stable reason. Other independently valid branches may continue.

## Task 5 — supersession behavior — FROZEN

`supersedes` is historical replacement evidence, not a generic “newer than” relation.

Rules:

- The source node is the newer confirmed owner-backed replacement; the target node is the older object it supersedes.
- Source and target MUST have the same Purpose semantic node kind.
- A `supersedes` edge is authoritative only when the canonical owner explicitly exposes supersession/replacement semantics or a frozen deterministic owner adapter maps an owner-native supersession record without guessing.
- Timestamps, higher revision numbers, matching titles, semantic similarity, model judgment, or “latest-looking” state are insufficient to create a supersession edge.
- Supersession is acyclic. A cycle invalidates every cycle-involved supersession edge for authoritative use.
- Superseded objects remain historical/provenance-addressable; replacement never erases the older canonical ref from history.
- Purpose does not mutate the older object, rewrite owner history, or manufacture a reciprocal `superseded_by` edge unless the owner itself exposes one.

### Current-object selection

Purpose MUST NOT decide the active/current strategic object merely by walking to the end of a supersession chain. Currentness comes from the active canonical strategic owner and its status/current-selection semantics.

A supersession chain may corroborate why an older object is no longer current, but it cannot override owner state.

If two candidate replacements supersede the same object and the owner does not identify which is current, Purpose keeps the ambiguity explicit and MUST NOT choose a winner by timestamp, version, ordering, or model inference.

### Explain behavior

`supersedes` is not a normal upward “why are we doing this?” parent edge. Explain may surface it as replacement/history context, for example “Strategy S2 replaced S1,” but must continue causal ascent through valid `serves`, `advances`, `executes`, or `addresses` relationships of the current node.

If the only available context is an older superseded node, Purpose may show it as historical evidence but MUST NOT silently treat it as current strategy/goal/mission.

---

## Slice 2.2 progress

1. [x] relation vocabulary
2. [x] allowed source/target kinds
3. [x] cycle behavior
4. [x] missing-parent behavior
5. [x] supersession behavior
6. [ ] orphan initiative/current-work behavior
7. [ ] explain traversal rules
8. [ ] deterministic graph ordering
