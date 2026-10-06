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
- `supersedes`: same semantic node kind only.

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

- Source is the newer owner-confirmed replacement; target is the older object.
- Source/target semantic kinds must match.
- Owner-native supersession or a frozen deterministic adapter is required; timestamps, version numbers, names, similarity or model judgment are insufficient.
- Supersession is acyclic; older records remain historical/provenance-addressable.
- Currentness comes from the active canonical owner, never merely from being the end of a supersession chain.
- Ambiguous competing replacements remain ambiguous unless the owner resolves currentness.
- `supersedes` may appear in explanation as replacement/history context but is not a normal causal ascent edge.

## Task 6 — orphan initiative/current-work behavior — FROZEN

An **orphan** is a valid current/relevant `initiative` or `current_work` node for which no valid causal parent edge is declared after graph validation. It is not the same as a broken/missing parent ref.

### Orphans are allowed

- An orphan initiative/current-work node is not invalid merely because it lacks a strategy/goal parent.
- Purpose MUST preserve a valid orphan when it is relevant to the requested projection rather than hiding it to make the trajectory look complete.
- Purpose MUST NOT invent `executes`, `advances`, `serves`, or any other edge to repair an orphan.
- Model inference, text similarity, shared labels/tags, name matching, neighboring work, or workspace type cannot promote a guessed parent into the authoritative graph.

### State and diagnostics

A retained orphan node receives trajectory linkage state:

```yaml
linkage_state: orphan
linkage_reason: no_valid_parent_relation
```

If a declared parent relation existed but failed target resolution, Task 4 applies instead; that node is not classified as a pure orphan.

An orphan may still have valid non-parent contextual edges such as `addresses`, `blocks`, or `affects`. Those do not make it causally linked to a higher-level goal/mission unless a valid structural/cause path exists.

### Explain behavior

When `purpose.explain` starts from or reaches an orphan:

- return the verified node and any already-verified path below it;
- stop causal ascent at that node;
- state that no validated higher-level parent relationship is available;
- mark the branch incomplete with stable reason `trajectory_orphan`;
- do not claim that the work serves a mission/goal merely because such a relation is plausible.

### Product behavior

Orphans are useful diagnostics. Dashboard/agent surfaces may say that work is currently unlinked and optionally offer a **proposal** to connect it later, but any durable relationship creation belongs to the canonical strategic owner and its normal confirmation/write path. The read-only Purpose projection never fixes the orphan itself.

### Small-workspace law

A small workspace may legitimately contain only current work or one initiative with no richer strategic graph yet. Purpose must remain useful in that state and must not force fake mission/strategy/KPI bureaucracy merely to eliminate orphans.

---

## Slice 2.2 progress

1. [x] relation vocabulary
2. [x] allowed source/target kinds
3. [x] cycle behavior
4. [x] missing-parent behavior
5. [x] supersession behavior
6. [x] orphan initiative/current-work behavior
7. [ ] explain traversal rules
8. [ ] deterministic graph ordering
