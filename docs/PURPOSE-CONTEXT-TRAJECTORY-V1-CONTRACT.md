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

No arbitrary/free-form edge type is valid in v1. Adding a new relation requires a contract revision.

### Directional semantics

`addresses`
- source is intended to reduce, resolve, mitigate, or directly respond to the target problem/challenge.
- Examples: mission → problem; strategy → challenge; initiative → challenge.

`serves`
- source exists in service of a higher-level target purpose/goal.
- Examples: goal → mission; initiative → goal.

`advances`
- source contributes measurable/meaningful progress toward the target goal/outcome without necessarily being its sole execution mechanism.
- Examples: strategy → goal; initiative → goal; current work → goal.

`blocks`
- source impedes, prevents, or materially constrains progress toward the target.
- Examples: challenge → goal; risk → initiative.

`executes`
- source is concrete execution of a higher-level plan.
- Examples: initiative → strategy; current work → initiative; current work → strategy when no initiative layer exists.

`measures`
- source KPI/metric measures progress/state of the target goal or desired outcome.

`affects`
- source changes feasibility, priority, risk, state, or expected outcome of the target without asserting a stronger parent/child relation.
- Examples: risk → strategy; material change → initiative.

`supersedes`
- source is the newer confirmed owner-backed replacement/revision of the target object when the canonical owner already supports that semantic.
- It is never inferred merely from timestamps, names, or similarity.

### Edge authority

Every authoritative trajectory edge MUST contain:

```yaml
from: <canonical ref>
relation: <one frozen token>
to: <canonical ref>
source_refs:
  - <canonical ref proving the relationship>
```

Rules:

- relation direction is semantic and MUST NOT be auto-reversed;
- an inverse view may be rendered for humans, but it is derived UI/explanation only and never stored as a second authoritative edge;
- source and target refs use the Slice 2.1 canonical ref format;
- edge evidence must come from canonical owner APIs/records or a deterministic derivation rule backed by canonical refs;
- textual similarity, embeddings, model inference, co-occurrence, shared tags, or matching names are insufficient to create an authoritative edge;
- if a relationship is plausible but not owner-backed/derivable under a frozen rule, omit it or present it only as a non-authoritative suggestion outside the v1 trajectory graph.

---

## Slice 2.2 progress

1. [x] relation vocabulary
2. [ ] allowed source/target kinds
3. [ ] cycle behavior
4. [ ] missing-parent behavior
5. [ ] supersession behavior
6. [ ] orphan initiative/current-work behavior
7. [ ] explain traversal rules
8. [ ] deterministic graph ordering
