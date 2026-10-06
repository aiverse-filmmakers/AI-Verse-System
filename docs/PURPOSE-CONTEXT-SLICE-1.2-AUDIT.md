# Purpose Context — Slice 1.2 Brain Strategic Model Audit

**Status:** COMPLETE / ACCEPTED FOR CONTINUATION WITH CARRIED FINDINGS  
**Date:** 2026-10-06  
**Audited repo:** `aiverse-filmmakers/AI-Verse-Brain`  
**Exact audited ref:** `7c77b053df627e61b3d7f11d029500ab61095c9c`  
**Brain `main` at closure:** same exact ref  
**Parent plan:** `docs/PURPOSE-CONTEXT-IMPLEMENTATION-PLAN.md`  
**Previous slice:** `docs/PURPOSE-CONTEXT-SLICE-1.1-AUDIT.md`

---

## 1. Purpose of this audit

Before Purpose Context creates any new Brain contract, inspect the repaired Core Brain baseline and determine:

- what strategic semantics already exist;
- which existing objects can safely supply Purpose Context;
- which existing interfaces are public/stable versus private storage details;
- where trajectory refs are currently weak/untyped;
- whether Telos concepts fit existing Brain semantics or genuinely require a minimal extension;
- what existing tests/CI protect these boundaries.

No Brain behavior was changed during this slice.

---

## 2. Audited object model

At the audited ref Brain admits these canonical object kinds:

- `intent`
- `practice`
- `gap`
- `opportunity`
- `initiative`
- `objective`
- `goal`
- `model_belief`
- `evaluation`
- `learning`
- `learning_candidate`
- `strategy_rule`
- `policy`

Every `BrainObject` already has exact scope, lifecycle status, revision, timestamps, source refs, evidence refs, and optional supersession links.

Important semantic distinctions:

- `intent` is the existing strategic-direction primitive when Brain owns direction. Existing subtypes are `desired_state`, `goal`, `boundary`, `constraint`, and `success_definition`.
- `goal` is a separate durable execution/continuation contract with objective, completion contract, criteria, resource budget, progress, evidence, activation epoch and optimistic versioning.
- `objective` is a bounded Action Loop outcome beneath longer-horizon strategic direction.
- `gap` is a Brain interpretation of the difference between desired-state refs and canonical current-state refs; it is not itself current-state truth.
- `opportunity` is a ranked hypothesis for reducing one or more active gaps.
- `initiative` is a proposed/accepted portfolio item traceable to a qualified opportunity and active gaps.
- `strategy_rule` belongs to Brain learning/self-improvement and represents learned operating doctrine. It is **not** the product/business/project Strategy concept from Telos.

Purpose Context must preserve these distinctions instead of flattening every object into generic “goals and strategy.”

---

## 3. Direction chain already present

Brain already contains a useful deterministic direction chain:

```text
confirmed desired state
        +
canonical current state
        ↓
       gap
        ↓
   opportunity
        ↓
   initiative
```

`DirectionService` enforces active-gap checks, eligibility/ranking, dedupe/cooldown and promotion continuity. Initiative proposal remains distinct from initiative acceptance.

However, the existing chain is **not yet a typed Purpose trajectory graph**:

- `gap.desired_state_refs` / `current_state_refs` are string refs and are not fully referentially validated when the gap is created;
- `initiative.serves` requires non-empty string refs but does not prove target kind, target existence, target lifecycle status, or same-scope validity;
- raw `source_refs` are provenance pointers rather than automatically trusted semantic edges.

Therefore a future Purpose snapshot must resolve and validate graph relationships before presenting them as authoritative lineage.

---

## 4. Goal API findings

`GoalService` is already a strong public-style service boundary.

Stable reads:

- `get(scope, goal_id)`
- `list(scope, statuses=None)`

Supported lifecycle/mutation operations include:

- create;
- edit;
- pause/resume;
- block;
- complete/clear;
- criteria add/remove/clear;
- progress;
- evaluate;
- continuation contract.

Important guarantees:

- operation-ID idempotency;
- optimistic expected-version checks;
- deterministic IDs on create;
- evidence-gated completion;
- model inference alone cannot pass a material criterion;
- budget/no-progress boundaries stop or block work rather than self-declaring success;
- continuation contracts do not grant tools, scheduling, connections or permissions.

Important Purpose limitation:

Brain currently has both strategic `intent:goal` semantics and the execution-grade `goal` service. Purpose must not merge them merely because both use the word “goal.” For the Telos strategic trajectory, the existing strategic intent subtype is the closer canonical semantic; execution Goals can be projected separately as current work/execution state when relevant.

---

## 5. Strategic ownership findings

In native AI-Verse mode, Brain participates in the existing single-owner strategic-direction contract.

Key guarantees:

- exact scope is `operator` or `workspace:<id>`;
- absence of a native ownership record means OS owns direction;
- Brain installation does not steal strategic ownership;
- OS→Brain handover requires explicit confirmation;
- imported OS direction carries source path + SHA-256 provenance;
- Brain→OS handback exports Brain strategic intent before flipping ownership;
- Brain canonical state remains provenance after handback;
- Brain unavailability never silently reactivates frozen OS strategy;
- interrupted handovers/handbacks have bounded recovery behavior.

Purpose must use this owner contract as the sole authority selector. It must never infer owner from available files, Brain process health, object presence, or model judgment.

---

## 6. Source/evidence/provenance findings

`source_refs` and `evidence_refs` are not interchangeable.

### `source_refs`

Use for provenance/lineage pointers. Their existence alone does not prove a typed semantic relation or current truth.

### `evidence_refs`

Carry structured semantics including:

- evidence class;
- optional claim;
- observation/expiry time;
- scope;
- integrity metadata;
- source kind/ref;
- evaluator independence.

Purpose should preserve these owner/evidence distinctions and descend to exact owner evidence for sensitive claims rather than treating every ref as equally authoritative.

---

## 7. Supersession and revision findings

Three concepts must remain distinct:

1. **Object revision** — optimistic concurrency/current version of the same stored object.
2. **Lifecycle supersession** — one durable semantic object replacing another.
3. **Strategy revision lineage** — dedicated learned `strategy_rule` previous-revision and rollback behavior.

Generic Brain `supersedes` / `superseded_by` fields exist but are not automatically maintained as a complete bidirectional lineage system.

Purpose must not invent historical versions from an object's revision counter.

---

## 8. Strategy rollback findings

`StrategyRevisionService` is strong for its intended purpose but its intended purpose is **learned Brain operating strategy**, not the Telos business/project Strategy node.

It provides:

- candidate→known-good previous revision linking;
- previous revision snapshotting;
- lock-protected promotion;
- compensation if promotion cannot retire the prior rule cleanly;
- explicit-user-authority rollback;
- restoration transaction receipts;
- known partial-state reconciliation;
- fail-closed operator review for inconsistent states.

Purpose may surface relevant active `strategy_rule` context as learned method/operating doctrine, but must not use its revision chain as the primary `Mission -> Goal -> Strategy -> Initiative` trajectory.

---

## 9. Existing read surfaces

### Safe/useful existing service-level reads

- `GoalService.get/list`
- `DirectionOwnershipService.owner/status/plan`
- `direction_owner_for()` for ownership coordination
- `BrainController.orientation(scope)` for bounded orientation use cases

### Existing internal reads that Purpose must not couple to directly

- `ObjectStore.load/list`
- Brain on-disk kind directories
- raw `ContextAssembler` implementation details

`ContextAssembler` is still important evidence for the desired architecture because it already loads bounded Brain state by cognition purpose and only retrieves history/capabilities for relevant cognition modes.

There is currently **no dedicated exported strategic snapshot service** that returns normalized strategic intent + gaps + initiatives + execution state + validated relationships + provenance.

Therefore Phase 3's planned Brain snapshot contract is necessary rather than redundant.

---

# 10. Final Telos → Brain mapping

This mapping deliberately avoids fake one-to-one equivalence.

| Telos concept | Slice 1.2 decision | Brain v1 interpretation |
|---|---|---|
| **Problem** | **Minimal new canonical strategic semantic required** | Existing `objective.problem` is bounded execution context and `gap` is a current desired-vs-observed interpretation; neither is a durable top-level root problem. Prefer extending strategic `intent` semantics with an explicit user-confirmed `problem` subtype before considering a new object kind. |
| **Mission** | **Minimal new canonical strategic semantic required** | `intent:desired_state` describes destination, not enduring mission/purpose. Prefer an explicit user-confirmed `intent:mission` semantic rather than overloading desired state. |
| **Narrative** | **Derived from existing owner-backed state for v1** | Build a non-canonical narrative projection from confirmed strategic intent, current state and relevant Memory provenance. Do not create a durable Brain narrative object merely to mirror Telos terminology. |
| **Goal** | **Use existing canonical Brain strategic object** | Use confirmed/active `intent` with subtype `goal` for the strategic trajectory. Keep execution-grade `goal` service objects distinct and project them as execution/current-work state when relevant. |
| **Challenge** | **Derived from existing Brain objects for v1** | Derive from active `gap` objects plus blocked/stalled initiatives/objectives and relevant confirmed constraints. Do not add a challenge object until real usage proves derived semantics insufficient. |
| **Strategy** | **Minimal new canonical strategic semantic required** | Existing `strategy_rule` is the wrong semantic. Prefer an explicit user-confirmed strategic `intent:strategy` semantic (with typed relation refs in the new contract) before adding another top-level object kind. |
| **Initiative** | **Use existing canonical Brain object** | Existing `initiative` already has appropriate proposal/acceptance/lifecycle semantics and links to gaps/source opportunity. Purpose must validate its trajectory refs before surfacing them as graph edges. |

### Architectural consequence

The audit does **not** justify adding separate canonical object kinds for every Telos noun.

The smallest coherent Brain extension currently appears to be:

```text
extend strategic intent semantics where explicit durable user intent is genuinely missing:
  problem
  mission
  strategy

reuse:
  intent:goal
  initiative

derive:
  narrative
  challenge
```

Phase 2 must freeze this contract before any Brain schema/code mutation. If Phase 2 finds a semantic or lifecycle requirement that cannot safely fit `intent`, it may deliberately promote a concept to a dedicated kind, but that must be justified by behavior rather than Telos vocabulary alone.

---

## 11. CI and test evidence

### Primary CI

Workflow: `.github/workflows/ci.yml`

Exact-ref run:

- **CI #159** — run `37183204509` — **SUCCESS**

Coverage at this exact ref:

- Ubuntu + Python 3.9
- Ubuntu + Python 3.12
- macOS + Python 3.9
- macOS + Python 3.12
- Windows + Python 3.9
- Windows + Python 3.12
- Ubuntu wheel build / clean install / CLI smoke

Ubuntu/Python 3.12 reports:

- **242 tests**
- **242 passed**

Relevant suites cover:

- strategic authority and state-machine gates;
- exact workspace scope/storage isolation;
- direction ownership, concurrent handovers and interrupted recovery;
- frozen-strategy read boundaries;
- gap/opportunity/initiative Direction behavior;
- evidence/freshness/evaluation;
- Goal lifecycle, idempotency, version conflicts and completion gates;
- strategy rollback;
- bounded retrieval/context behavior;
- native path containment and write readiness.

### Cross-owner direction contract

- **OS Direction Ownership Contract #75** — run `37183204505` — **SUCCESS**

It proves OS/Brain ownership marker interoperability, explicit transfer, provenance import, strategic write fencing and no stale-strategy fallback after Brain loss.

Caveat: the workflow clones moving `AI-Verse-OS/main`; final Purpose qualification must use pinned exact component refs rather than relying on this workflow alone.

### Skills/evidence contract

- **Skills Receipt Contract #65** — run `37183204511` — **SUCCESS**

Not a Purpose-specific gate, but confirms receipt/evidence boundaries remain green at the audited Brain ref.

### Pre-existing red release metadata gate

- **Release Descriptor #6** — run `37183204489` — **FAILURE**

Root cause is not Brain runtime behavior. The checked-in development descriptor declares:

`revision = 5d29b42a337bd078898c2e2ec876831a9ea421fa`

The release workflow requires the declared revision to resolve to a Git commit. Even after full-history checkout, `git cat-file -e "$REVISION^{commit}"` fails because the declared object is not present in reachable repository history.

This is a real repository-integrity finding. The audited Brain runtime/cross-owner test baseline is green, but the repository cannot truthfully be called all-green while this descriptor gate is red.

**Repair requirement:** fix this pre-existing release-descriptor integrity issue on or before the first Purpose-related Brain descendant is accepted, and certainly before Core vNext qualification.

---

## 12. Carried findings into implementation

1. Add a stable bounded Brain strategic snapshot service/API before OS Purpose composition depends on Brain strategic state.
2. Do not expose Brain private storage layout as the cross-component contract.
3. Validate typed trajectory relations; raw `serves`/source refs are insufficient.
4. Keep strategic `intent:goal` distinct from execution-grade `goal` service semantics.
5. Do not map Telos Strategy to `strategy_rule`.
6. Prefer minimal strategic-intent extensions (`problem`, `mission`, `strategy`) over new object kinds unless Phase 2 proves dedicated lifecycles are necessary.
7. Derive Narrative and Challenge in v1 rather than creating canonical stores pre-emptively.
8. Preserve single-owner direction semantics and fail closed when the active owner is unavailable.
9. Final cross-owner Purpose tests must pin exact component refs.
10. Repair the pre-existing Brain release-descriptor red gate before a Purpose Brain descendant can be treated as fully qualified.

---

## 13. Slice verdict

**Slice 1.2: COMPLETE / ACCEPTED FOR CONTINUATION WITH CARRIED FINDINGS.**

The audit found no architectural reason to abandon Purpose Context. It did find that Brain already contains more of the required strategic machinery than a naive Telos port would suggest, so the correct implementation is smaller and more disciplined than adding one object type per Telos heading.

No Purpose behavior has been implemented yet.

---

## 14. NEXT

**Phase 1 / Slice 1.3 / Task 1 — audit Data current KPI values and operational truth read interfaces.**

Continue one task at a time and persist the execution state after each task.
