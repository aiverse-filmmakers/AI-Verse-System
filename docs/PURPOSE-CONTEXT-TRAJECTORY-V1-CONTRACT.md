# AI-Verse Purpose Context Trajectory v1 Contract

**Status:** IN PROGRESS — Slice 2.2  
**Parent contract:** `docs/PURPOSE-CONTEXT-V1-CONTRACT.md`  
**Canonical owner:** `AI-Verse-System`

This contract defines the bounded, explainable relationship graph used by Purpose Context. The graph is a derived projection over owner-backed refs; it is not a second strategic database.

---

## Task 1 — relation vocabulary — FROZEN

Purpose Context v1 admits exactly these trajectory relation tokens:

- `addresses`
- `serves`
- `advances`
- `blocks`
- `executes`
- `measures`
- `affects`
- `supersedes`

No arbitrary/free-form edge type is valid in v1.

Directional meanings:

- `addresses`: source responds to/reduces target problem or challenge.
- `serves`: source exists in service of a higher-level mission/goal/outcome.
- `advances`: source contributes progress toward target goal/outcome.
- `blocks`: source impedes target progress/feasibility.
- `executes`: source is concrete execution of a higher-level plan.
- `measures`: KPI/metric measures target goal/outcome.
- `affects`: source changes feasibility/priority/risk/state of target without asserting stronger hierarchy.
- `supersedes`: newer confirmed owner-backed object replaces older object; never inferred from similarity/timestamps alone.

Authoritative relations require canonical evidence. Text similarity, embeddings, co-occurrence, shared tags, matching names, or model inference alone cannot create a v1 edge.

---

## Task 2 — allowed source/target kinds — FROZEN

### Purpose graph node kinds

The v1 trajectory graph admits exactly these semantic node kinds:

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

`narrative`, `priority`, `constraint`, and `current_state` may inform/explain a trajectory but are not first-class graph node kinds in v1. They may remain semantic sections/evidence.

### Node identity

An owner-backed node MUST carry:

```yaml
node_id: <deterministic Purpose node id>
kind: goal
canonical_ref: <Slice 2.1 canonical ref>
source_refs:
  - <canonical ref>
```

A derived node, such as a derived `challenge`, MUST carry:

```yaml
node_id: <deterministic Purpose node id>
kind: challenge
derivation:
  rule: <stable rule id>
  source_refs:
    - <canonical ref>
source_refs:
  - <canonical ref>
```

Rules:

- owner-backed `node_id` is deterministically derived from semantic kind + canonical ref identity;
- derived `node_id` is deterministically derived from semantic kind + derivation rule + ordered source-ref identities;
- generated node IDs never become canonical owner IDs;
- a node with neither canonical owner ref nor valid deterministic derivation provenance is not authoritative.

Edges therefore use Purpose node IDs while retaining evidence refs:

```yaml
from: <node_id>
relation: serves
to: <node_id>
source_refs:
  - <canonical ref>
```

This refines Task 1 endpoint representation without changing the frozen relation vocabulary.

### Allowed relation matrix

`addresses`
- `mission` → `problem`
- `strategy` → `problem | challenge`
- `initiative` → `problem | challenge`

`serves`
- `goal` → `mission | desired_outcome`
- `initiative` → `goal`

`advances`
- `strategy` → `goal | desired_outcome`
- `initiative` → `goal | desired_outcome`
- `current_work` → `goal | desired_outcome`

`blocks`
- `challenge` → `goal | strategy | initiative | current_work`
- `risk` → `goal | strategy | initiative | current_work`

`executes`
- `initiative` → `strategy`
- `current_work` → `initiative | strategy`

`measures`
- `kpi` → `goal | desired_outcome`

`affects`
- `risk` → `mission | desired_outcome | goal | strategy | initiative | current_work`
- `material_change` → `problem | mission | desired_outcome | goal | challenge | strategy | initiative | risk | current_work`

`supersedes`
- source and target MUST have the same semantic node kind;
- additional owner/scope/revision rules are frozen in Task 5.

### Validation law

- A relation whose source/target semantic kinds are not allowed by this matrix is invalid and MUST NOT enter the authoritative trajectory graph.
- Purpose MUST NOT coerce a node kind merely to make an edge fit.
- Canonical owner record kind and Purpose semantic node kind are distinct concepts. Example: Brain may expose canonical `kind: intent` while the owner-backed semantic classification is Purpose `goal` or `mission`.
- Semantic kind classification must come from the owner API/contract or a frozen deterministic derivation rule; it may not be guessed from free-text labels.
- An invalid edge may be reported in content-free diagnostics with its evidence ref identity, but it cannot participate in explanation/traversal.

---

## Slice 2.2 progress

1. [x] relation vocabulary
2. [x] allowed source/target kinds
3. [ ] cycle behavior
4. [ ] missing-parent behavior
5. [ ] supersession behavior
6. [ ] orphan initiative/current-work behavior
7. [ ] explain traversal rules
8. [ ] deterministic graph ordering
