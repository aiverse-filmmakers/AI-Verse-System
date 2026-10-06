# AI-Verse Purpose Context v1 Contract

**Status:** IN PROGRESS — Slice 2.1 contract freeze  
**Parent plan:** `docs/PURPOSE-CONTEXT-IMPLEMENTATION-PLAN.md`  
**Canonical owner:** `AI-Verse-System`  
**Implementation owner:** `AI-Verse-OS` after contract freeze

Purpose Context is a derived, read-only, disposable projection over canonical owner state. It never becomes a second strategic, Data, Memory, runtime, or Dashboard authority.

> Editorial note: Tasks 1–6 below preserve the already-frozen semantics from their earlier detailed form; wording is compacted only to keep the canonical contract maintainable.

---

## Task 1 — `schema_version` — FROZEN

- Every envelope MUST emit `schema_version: "1.0"`.
- Version is a required UTF-8 `MAJOR.MINOR` string.
- Producers emit it explicitly; consumers never infer it from file/repo/runtime versions.
- Unsupported major versions fail closed.
- Minor v1 increases may add backward-compatible optional material only; they may not change existing meaning, owner authority, scope/isolation, or make an optional field required.
- Breaking semantics require a new major version.

---

## Task 2 — supported scope kinds — FROZEN

Supported scopes are exactly:

```yaml
scope_kind: operator
scope: operator
```

or:

```yaml
scope_kind: workspace
scope: workspace:<workspace-id>
```

Rules:

- `scope_kind` and `scope` are required and MUST agree.
- Workspace IDs use `^[a-z0-9][a-z0-9-]{0,127}$`.
- `operator` is a strategic operator sentinel, not a workspace and not an aggregate over all workspaces.
- `workspace:<id>` is bound to exactly that workspace; no implicit cross-workspace reads.
- Workspace type belongs to identity metadata, not `scope_kind`.
- No `global`, `system`, `all-workspaces`, `organization`, `team`, `client`, `project`, or custom scope kind exists in v1.
- Dashboard `systemId` is transport/connection identity only, never a Purpose scope.
- The composer validates the supplied canonical scope but never broadens, substitutes, or falls back to another scope.

---

## Task 3 — required vs optional fields — FROZEN

Required top-level fields:

```yaml
schema_version: "1.0"
scope: operator | workspace:<id>
scope_kind: operator | workspace
identity:
  kind: operator | workspace
  id: operator | <workspace-id>
provenance: {...}
```

Optional owner-backed identity fields may include `name`, `type`, and `status`.

Optional semantic sections:

- `problems`
- `purpose`
- `narratives`
- `goals`
- `priorities`
- `challenges`
- `strategies`
- `initiatives`
- `constraints`
- `kpis`
- `risks`
- `current_state`
- `current_work`
- `recent_material_changes`
- `trajectory`

Presence semantics:

- absent optional section = not emitted because not relevant/applicable/requested;
- present empty collection = owner read succeeded and result is known empty under the requested bounds;
- unavailable/unknown attempted reads use the explicit state contract from Task 8, never silent omission;
- no placeholder records or meaningless empty corporate sections;
- no projected field becomes independently editable.

---

## Task 4 — provenance format — FROZEN

Every envelope carries:

```yaml
provenance:
  projection_owner: ai-verse-os
  generated_at: <RFC3339 UTC>
  owner_reads:
    - owner: ai-verse-brain
      operation: strategic_snapshot
      scope: workspace:example
      status: ok | partial | unavailable | error
      observed_at: <RFC3339 UTC>
      freshness: {...}
      refs: [...]
```

Rules:

- `projection_owner` is exactly `ai-verse-os` in v1.
- `generated_at` is projection assembly time, never freshness evidence.
- Every attempted owner read is recorded, including partial/unavailable/error reads.
- `observed_at` is read time only.
- `refs` use Task 6 canonical refs; no private paths, DB paths, secrets, SQL, or private transport internals.
- Every emitted owner-backed factual/strategic claim has non-empty `source_refs`.
- Every derived claim additionally carries a stable `derivation.rule` and its source refs.
- A derived claim cannot outrank or create authority beyond its owner inputs.
- Trajectory edges/material-change effects retain their own evidence refs.
- Any emitted claim must be traceable back to the canonical owner record/version that supports it.

---

## Task 5 — freshness format — FROZEN

Every attempted owner read carries:

```yaml
freshness:
  state: current | stale | unknown | unavailable
  as_of: <RFC3339 UTC>
  source_updated_at: <RFC3339 UTC>   # optional
  max_age_seconds: <non-negative int> # optional
  reason: <stable reason code>        # optional
```

Rules:

- `current` requires owner assertion or sufficient source/version evidence under a declared policy.
- `stale` means available but known too old/superseded for current use.
- `unknown` means the read succeeded but trustworthy recency evidence is insufficient.
- `unavailable` means the requested source/value itself cannot be obtained.
- Adapter/query/generation/render time alone never proves source freshness.
- Aggregate-backed current values without source watermarks are `unknown`, not `current`.
- Item-level freshness may override the owner-read summary where needed.
- Derived freshness cannot be stronger than the weakest source relevant to the derived claim.
- Optional projection summary may use `current | mixed | stale | unknown | unavailable`; `mixed` is summary-only.

---

## Task 6 — canonical ref format — FROZEN

Canonical ref:

```yaml
owner: ai-verse-brain
scope: workspace:ai-verse
kind: intent
id: goal-public-beta
version: "7"
```

Rules:

- registered v1 owner IDs: `ai-verse-os`, `ai-verse-brain`, `ai-verse-data`, `ai-verse-memory`, `ai-verse-gateway`;
- identity tuple is `(owner, scope, kind, id)`;
- `version` identifies an observed revision, not durable logical identity;
- mutable authoritative claims require an exact version token when the owner supports one;
- if a mutable owner cannot provide a version token, verification limits stay explicit rather than pretending the revision is pinned;
- refs never contain raw filesystem/DB paths, credentials, secrets, raw SQL, private transport addresses, or Dashboard `systemId`;
- refs grant no authority and still require normal owner scope/authorization checks;
- Purpose obtains refs from owner APIs, never by reverse-engineering private storage;
- stale/deleted refs never fuzzy-rebind to similarly named records;
- all Purpose source/evidence/ref fields use this same structure.

---

## Task 7 — deterministic ordering rules — FROZEN

Purpose Context v1 MUST produce deterministic semantic ordering so the same owner state does not churn merely because an API/storage iterator returned items in a different order.

### Canonical top-level serialization order

When serialized to an order-preserving format, emit recognized fields in this order:

1. `schema_version`
2. `scope`
3. `scope_kind`
4. `identity`
5. `problems`
6. `purpose`
7. `narratives`
8. `goals`
9. `priorities`
10. `challenges`
11. `strategies`
12. `initiatives`
13. `constraints`
14. `kpis`
15. `risks`
16. `current_state`
17. `current_work`
18. `recent_material_changes`
19. `trajectory`
20. contract metadata introduced by later v1 tasks, if present
21. `provenance`

Object key order is a serialization convention only; consumers MUST use field names, not positional assumptions.

### Collection ordering

For semantic collections:

1. if the canonical owner supplies an explicit semantic priority/rank/order field, sort by that owner-backed value first;
2. otherwise sort by canonical ref identity tuple `(owner, scope, kind, id)` using bytewise ascending UTF-8 comparison;
3. if two entries share the same identity tuple, sort by `version` bytewise ascending, with absent version before present version;
4. deterministic generated records use their deterministic generated ID as the final tie-breaker.

Purpose MUST NOT invent a priority score merely to obtain ordering.

### Special collections

- `priorities`: owner-backed priority/rank first, then canonical ref order.
- `recent_material_changes`: effective/source event time descending when owner-backed; ties use canonical ref order. Read/ingestion time never substitutes for missing event time.
- `current_work`: owner-backed execution priority/order first; otherwise canonical ref order.
- `trajectory`: sort by source canonical identity, then relation token, then target canonical identity, then evidence-ref tuple.
- `source_refs`, derivation refs, and owner-read `refs`: canonical ref tuple order.
- `provenance.owner_reads`: `owner`, then `operation`, then `scope`, all bytewise ascending; multiple reads of the same tuple then sort by `observed_at` ascending.

### Stability law

- Array order from databases, filesystems, maps, API responses, or concurrent completion order is never authoritative unless the owner contract explicitly declares it semantic.
- Rebuilding from semantically identical inputs MUST yield the same semantic ordering.
- Budget pruning later in Task 9 must operate on this deterministic ordered representation, not nondeterministic arrival order.
- Deterministic ordering may never override explicit owner priority semantics.

---

## Slice 2.1 freeze progress

1. [x] `schema_version`
2. [x] supported scope kinds
3. [x] required vs optional fields
4. [x] provenance format
5. [x] freshness format
6. [x] canonical ref format
7. [x] deterministic ordering rules
8. [ ] unknown/unavailable field behavior
9. [ ] bounded size/budget rules
10. [ ] rebuildability contract
