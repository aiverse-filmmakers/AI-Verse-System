# AI-Verse Purpose Context Trajectory v1 Contract

**Status:** IN PROGRESS — Slice 2.2  
**Parent contract:** `docs/PURPOSE-CONTEXT-V1-CONTRACT.md`  
**Canonical owner:** `AI-Verse-System`

This contract defines the bounded, explainable relationship graph used by Purpose Context. The graph is a derived projection over owner-backed refs; it is not a second strategic database.

---

## Task 1 — relation vocabulary — FROZEN

Purpose Context v1 admits exactly:

- `addresses`
- `serves`
- `advances`
- `blocks`
- `executes`
- `measures`
- `affects`
- `supersedes`

No free-form edge type is valid. Edges require canonical evidence; similarity, embeddings, co-occurrence, shared tags, matching names, or model inference alone cannot create an authoritative edge.

Directional meanings:

- `addresses`: source responds to target problem/challenge.
- `serves`: source exists in service of higher-level mission/goal/outcome.
- `advances`: source contributes progress toward goal/outcome.
- `blocks`: source impedes target progress/feasibility.
- `executes`: source is concrete execution of a higher-level plan.
- `measures`: KPI measures goal/outcome.
- `affects`: source changes feasibility/priority/risk/state without asserting stronger hierarchy.
- `supersedes`: newer confirmed owner-backed object replaces older object; never inferred from similarity/timestamps alone.

---

## Task 2 — allowed source/target kinds — FROZEN

V1 graph node kinds:

`problem`, `mission`, `desired_outcome`, `goal`, `challenge`, `strategy`, `initiative`, `kpi`, `risk`, `current_work`, `material_change`.

`narrative`, `priority`, `constraint`, `current_state` remain evidence/semantic sections, not graph nodes in v1.

Owner-backed nodes carry deterministic `node_id`, semantic `kind`, canonical ref and source refs. Derived nodes carry deterministic `node_id`, semantic kind, stable derivation rule and ordered source refs. Generated node IDs never become canonical owner IDs.

Allowed relation matrix:

- `addresses`: mission→problem; strategy→problem|challenge; initiative→problem|challenge.
- `serves`: goal→mission|desired_outcome; initiative→goal.
- `advances`: strategy|initiative|current_work→goal|desired_outcome.
- `blocks`: challenge|risk→goal|strategy|initiative|current_work.
- `executes`: initiative→strategy; current_work→initiative|strategy.
- `measures`: kpi→goal|desired_outcome.
- `affects`: risk→mission|desired_outcome|goal|strategy|initiative|current_work; material_change→problem|mission|desired_outcome|goal|challenge|strategy|initiative|risk|current_work.
- `supersedes`: same semantic node kind only; further rules in Task 5.

Invalid kind pairs never enter the authoritative graph and are never coerced to fit.

---

## Task 3 — cycle behavior — FROZEN

### Self-cycle rule

Any edge where `from == to` is invalid for every v1 relation and MUST NOT enter the authoritative graph.

### Structural ancestry relations

For cycle validation, these relations define structural/temporal ancestry:

- `serves`
- `advances`
- `executes`
- `supersedes`

The authoritative subgraph formed by those relations MUST be acyclic.

`addresses`, `blocks`, `measures`, and `affects` are contextual/impact relations rather than parentage. They do not define structural ancestry, but traversal still uses a visited-node/visited-edge guard so malformed data can never cause infinite traversal.

### Deterministic cycle detection

- Cycle detection is graph-based, not “first edge wins”.
- If a structural strongly connected component contains more than one node, every structural edge wholly inside that component is considered cycle-involved.
- A structural self-loop is cycle-involved by definition.
- Purpose MUST NOT arbitrarily keep one cycle edge based on storage/API arrival order.

### Cycle handling

When an owner-backed or deterministically derived cycle is detected:

1. retain the underlying evidence refs in validation diagnostics;
2. exclude all cycle-involved structural edges from the **authoritative traversal graph**;
3. mark the trajectory section `partial` through the Slice 2.1 `section_states` mechanism when the rejected cycle affects emitted graph content;
4. emit a stable content-free reason such as `trajectory_cycle_detected`;
5. do not rewrite, reverse, or invent replacement relationships;
6. do not mutate the canonical owner merely because Purpose detected the inconsistency.

The non-cyclic remainder of the graph may still be returned if it remains truthful and useful.

### Explain behavior under a cycle

An explanation path MUST terminate before a rejected cyclic edge. It may return the verified path accumulated so far plus an explicit incomplete/cycle limitation. It MUST NOT loop, choose an arbitrary edge to “break” the cycle silently, or claim a complete upward trajectory.

### Supersession safety

Any cycle containing `supersedes` is invalid. A→B→A supersession can never be interpreted as “latest wins” based only on timestamps. The owner must resolve the contradiction through its canonical semantics; Purpose only reports/excludes it.

### Validation vs owner authority

Cycle rejection from the Purpose traversal graph does **not** delete or supersede the owner records. It means only that Purpose cannot present those relationships as a coherent authoritative trajectory until the canonical owner state is consistent.

---

## Slice 2.2 progress

1. [x] relation vocabulary
2. [x] allowed source/target kinds
3. [x] cycle behavior
4. [ ] missing-parent behavior
5. [ ] supersession behavior
6. [ ] orphan initiative/current-work behavior
7. [ ] explain traversal rules
8. [ ] deterministic graph ordering
