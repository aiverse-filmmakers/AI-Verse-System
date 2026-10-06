# Purpose Context — Slice 1.3 Data, Memory, Runtime, Dashboard Integration Audit

**Status:** COMPLETE / ACCEPTED FOR CONTINUATION WITH CARRIED REPAIRS  
**Date:** 2026-10-06  
**Parent plan:** `docs/PURPOSE-CONTEXT-IMPLEMENTATION-PLAN.md`

Audited exact refs:

- Data: `aiverse-filmmakers/AI-Verse-Data@6e8781ff1dcd96a35dfb27868bd60605361483d0`
- Memory: `aiverse-filmmakers/AI-Verse-Memory@b0cae8cd8da38aa657fbc736c575177aa75e5ec7`
- Gateway: `aiverse-filmmakers/AI-Verse-Gateway@089aaa6440bbbbb9f41195eafe123ad2e06d5625`
- Dashboard: `aiverse-filmmakers/AI-Verse-Dashboard@2c1d1a57f7cb27eec166d4fea10dbb335250c518`
- Carried owner-contract refs: OS `e74a4e05b1f891e6f871f34a298bf10363a11d88`; Brain `7c77b053df627e61b3d7f11d029500ab61095c9c`

No Purpose Context behavior was implemented in this slice. This was an owner/interface audit only.

---

## 1. Audit outcome

Slice 1.3 confirms that Purpose Context can be implemented without bypassing any current owner or reading private storage directly.

The required architecture is:

```text
Brain / OS strategy       Data current truth       Memory history
          \                      |                      /
           \                     |                     /
            -----> OS Purpose Context composer <-----
                         |
                         | bounded read-only projection
                         v
                    Gateway runtime
                         |
                         v
                  model / agent context
                         |
                         +----> Dashboard read surface
```

Dashboard remains presentation/control only. Gateway remains runtime/context assembly only. OS owns the Purpose composition layer but not the underlying canonical truths. Brain/Data/Memory keep their existing ownership.

---

## 2. Data current truth

### Existing usable owner surfaces

Data already exposes public read surfaces for:

- records;
- bounded queries;
- aggregates;
- schemas/spaces;
- provenance events/receipts;
- health;
- a read-only Brain adapter;
- a read-only Dashboard projection adapter.

### Purpose rule

Current KPI or operational values may come from Data only when the strategic definition resolves to an explicit Data binding.

A valid binding may identify, for example:

- workspace;
- space;
- entity;
- field/natural key;
- filter;
- aggregate operation.

Purpose must not search arbitrary Data fields and infer that a number is the KPI the strategy meant.

Strategic definition/target remains owned by the strategic direction owner. Data supplies current measured truth/evidence.

### Freshness

Data records expose version/created/updated metadata. Immutable events/receipts expose commit time, before/after versions, actor, trusted workspace binding and integrity-checked provenance.

Important distinction:

- adapter `answeredAt` = time the read happened;
- record/event timestamp = source recency.

A freshly executed aggregate is not automatically fresh evidence about the source data. Aggregate-backed KPI values therefore need companion source-freshness evidence/watermarks or must report freshness as unknown.

### Required Purpose addition

No second Data query engine is justified.

At most, Phase 5 may need a thin typed Purpose/Data binding wrapper that:

1. validates the declared KPI binding;
2. executes existing bounded Data reads;
3. returns value + source/provenance/freshness metadata;
4. fails closed/unavailable if the binding cannot be resolved.

---

## 3. Memory historical context and material-change evidence

Memory is already explicit that historical state does not outrank newer current owner state.

Existing useful reads include:

- bounded `recall()`;
- orientation map;
- progressive `catalog -> summary -> detail -> source` recall;
- session-digest recall;
- rebuildable relationship projection.

Progressive source descent revalidates scope, canonical path, identity and version before returning exact historical evidence. Stale/unavailable evidence remains explicit.

Session digests provide bounded significant outcomes, unresolved items, source coverage, source fingerprint/version and completion metadata without turning raw Gateway transcripts into Memory truth.

### Material-change conclusion

Memory does not currently own the semantic question:

> Did this historical change materially affect a current goal, priority, strategy, blocker, or feasibility?

That is correct.

Phase 6 should add only a bounded material-change **evidence candidate** read over existing Memory surfaces. Purpose/Brain compares those historical candidates with current owner state to decide materiality.

No new Memory event store or Purpose history database is justified.

---

## 4. Runtime/context-ladder integration

Gateway is the current runtime/context assembly owner.

`RunEngine` binds every run to a scope, asks the host for owner context, and injects the result as a bounded Gateway system message. The existing progressive ladder already escalates historical evidence only when user intent needs it.

The current context bundle already composes:

- current owner context;
- bounded Memory orientation/history;
- capabilities;
- connections.

The Context Governor separately manages invocation pressure and protects recent canonical raw conversation while compacting older runtime context under pressure.

### Correct Purpose insertion

Gateway should not become a Purpose composer.

After OS Purpose P1/P2 exists, add a small owner-routed host read such as an eventual `read_purpose_context` equivalent. Gateway should:

1. classify whether the current task is Purpose-relevant;
2. make **zero Purpose reads** for trivial/unrelated tasks;
3. request Purpose only for the run's already-bound scope;
4. add the bounded projection to the existing owner-context bundle;
5. let the existing Context Governor account for its token pressure;
6. record diagnostics for reads/skips/bytes/tokens/freshness/version.

Purpose relevance belongs beside the existing historical-depth classifier, not inside it. `aiverse_context` is currently a Memory/deep-history escalation mechanism and should not be casually overloaded with strategic semantics.

### Anti-bloat confirmation

Gateway's prior I1 evaluation already rejected creating a second cross-owner orientation graph because existing canonical owner projections cover the information domains. Purpose should respect that result.

Purpose adds a new causal/trajectory answer, not another persisted cross-owner cache.

---

## 5. Dashboard boundaries

Dashboard's declared laws align with Purpose:

- owns zero domain truth;
- caches only disposable projections;
- isolates registered OS installations by `systemId`;
- validates workspace selection server-side;
- browser sends IDs, not raw roots;
- canonical mutation must go through selected OS command boundaries.

Current Dashboard Gateway is deliberately query-only. Command method names exist but are blocked until the command boundary is enabled.

### Purpose Dashboard read path

Phase 10 should add a direct versioned Purpose query, conceptually:

```text
purpose.get
purpose.explain
```

The Dashboard Gateway should resolve the selected `systemId` and Purpose scope, then ask the selected OS for the derived projection. It must not use `source.preview` against a generated `PURPOSE.md`/`TELOS.md` file.

### Purpose Dashboard write path

Once Phase 8 owner-routed Purpose mutation proposals exist:

```text
Dashboard
  -> selected OS command boundary
  -> Purpose mutation proposal/router
  -> active strategic owner
  -> required confirmation/authority gate
  -> canonical owner mutation
  -> Purpose projection rebuild/read
```

Dashboard never writes a local/cached Purpose object.

### Operator surface gap

Current Dashboard protocol makes almost every non-system method workspace-scoped. Purpose also supports operator scope.

Phase 10 therefore needs a deliberate operator/global Purpose query form. Do not create a fake workspace named `operator` inside Dashboard merely to fit the current protocol shape.

---

## 6. Exact scope/isolation map

| Component | Purpose-relevant scope law |
|---|---|
| OS | `operator` or exact `workspace:<id>`; canonical IDs lowercase alnum/hyphen, max 128; exact workspace isolation. |
| Brain | same strategic scope model; operator/workspace state kept separate; one active direction owner per scope. |
| Data | native Data is workspace-bound; canonical ID lowercase alnum/hyphen, max 128; DB binding stores workspace identity. Standalone storage exists but is not an implicit operator aggregate. |
| Memory | operator/workspace; workspace historical visibility may include operator context but never another workspace unless explicit legacy all-workspace recall is used; progressive recall has no all-workspace mode. |
| Gateway | incoming run scope is literal `operator` or canonical lowercase/hyphen workspace ID up to 128; translated to `operator` or `workspace:<id>` before owner calls. Workspace progressive evidence may use visible operator history but not unrelated workspace evidence. |
| Dashboard | system-bound plus usually workspace-bound; selected system/workspace resolved server-side. Current workspace ID protocol is inconsistent with canonical OS IDs. |

### Important scope distinctions

**Data operator scope:** there is no justified automatic “operator = aggregate every workspace DB” interpretation. Operator Purpose gets Data only from an explicit operator/current-truth source contract; otherwise those fields remain unavailable.

**Memory operator overlay:** Memory allowing workspace recall to see appropriate operator historical context does not mean workspace strategy inherits operator mission/goals. Strategic cross-scope Purpose edges remain explicit.

**Gateway `operator` transport sentinel:** Gateway stores `workspace_id: "operator"` to represent operator runs, then translates it to strategic scope `operator`. It is not a real workspace.

**Dashboard `systemId`:** this is Dashboard-local connection identity, never a canonical Purpose scope or Data owner identity.

---

## 7. Carried compatibility defect: Dashboard workspace IDs

The current Dashboard protocol defines workspace IDs as:

```text
[A-Za-z0-9][A-Za-z0-9-_]{0,63}
```

Canonical OS/Data/Gateway workspaces use:

```text
[a-z0-9][a-z0-9-]{0,127}
```

Consequences:

- Dashboard accepts uppercase and underscore forms canonical OS workspaces reject;
- Dashboard rejects otherwise valid canonical workspace IDs longer than 64 characters.

Server-side workspace resolution prevents this mismatch from automatically granting access to another workspace, so this is primarily a compatibility/contract defect rather than evidence of an isolation bypass.

It must be aligned before the Purpose Dashboard surface is considered qualified, and preferably as a general Dashboard contract repair rather than a Purpose-only workaround.

---

## 8. Required API map after Phase 1

| Owner | Existing surface Purpose can reuse | Minimal new surface currently justified |
|---|---|---|
| OS | current-context, scope validator, direction-owner contract | Purpose composer/read/explain API |
| Brain | Goal reads, direction ownership, canonical strategic objects | bounded strategic snapshot with validated relationship refs; minimal strategic intent semantics frozen in Phase 2 |
| Data | public client/query/provenance; Brain/Dashboard read adapters | optional thin typed KPI/current-value binding wrapper only if Phase 5 needs it |
| Memory | recall/orientation/progressive recall/session digests | thin bounded material-change evidence query/adapter only if Phase 6 needs it |
| Gateway | progressive context assembly, context governor, host client | Purpose relevance gate + owner-routed Purpose host read/injection + diagnostics |
| Dashboard | system/workspace registry, query protocol, disposable read projections | read-only Purpose queries; later owner-routed commands only after canonical write path exists |

No Purpose implementation is authorized to parse another owner's private storage merely because doing so would be faster.

---

## 9. Repositories required by the current P1-P5 plan

Confirmed required:

1. `AI-Verse-System` — canonical contracts/planning/acceptance
2. `AI-Verse-OS` — Purpose projection composer and OS-owned strategy adapter
3. `AI-Verse-Brain` — strategic snapshot + minimal missing strategic semantics if Phase 2 freezes them
4. `AI-Verse-Data` — mapped current KPI/operational truth
5. `AI-Verse-Memory` — bounded historical/material-change evidence
6. `AI-Verse-Gateway` — relevance-gated runtime injection
7. `AI-Verse-Dashboard` — Phase 10 product surface
8. `ai-verse-distribution` — final Core descendant qualification/admission

Skills, Automations, Multiple Bots, Connections and other components are not required merely to call Purpose Context complete. They remain optional future sources only when a later bounded requirement proves value.

---

## 10. Carried repairs/findings

1. Brain release descriptor currently has a pre-existing red integrity gate; repair before Purpose Brain descendant acceptance/Core vNext.
2. Dashboard workspace-ID contract must align with canonical OS/Data/Gateway IDs before Purpose Dashboard qualification.
3. OS workspace manifest schema max-length mismatch from Slice 1.1 remains carried: schema should eventually match runtime max 128.
4. Final cross-owner qualification must pin exact component refs; moving-main integration workflows are useful but insufficient as final release evidence.
5. Data aggregate-backed KPI freshness must never be fabricated from query execution time.
6. Brain trajectory refs must be validated before Purpose exposes them as authoritative edges.

---

## 11. Slice acceptance verdict

- Every planned P1-P5 integration has an existing owner read surface or one bounded required new API: **PASS**.
- No private storage parsing is required: **PASS**.
- Exact required repositories are known before implementation: **PASS**.
- Operator/workspace scope differences are understood and bounded: **PASS**.
- Cross-workspace isolation can be preserved without a new federation layer: **PASS**.
- Dashboard scope contract has one carried compatibility repair: **PASS WITH REPAIR REQUIRED BEFORE DASHBOARD QUALIFICATION**.

**Slice 1.3: COMPLETE / ACCEPTED FOR CONTINUATION WITH CARRIED REPAIRS.**

---

## 12. NEXT

**Phase 2 / Slice 2.1 / Task 1 — freeze the Purpose Context `schema_version` contract.**

Do not begin implementation by editing Brain/OS objects first. Phase 2 freezes the versioned projection and relationship semantics before owner code changes.
