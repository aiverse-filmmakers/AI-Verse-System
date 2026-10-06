# AI-Verse Purpose Context v1 Contract

**Status:** IN PROGRESS — Slice 2.1 contract freeze  
**Parent plan:** `docs/PURPOSE-CONTEXT-IMPLEMENTATION-PLAN.md`  
**Canonical owner:** `AI-Verse-System`  
**Implementation owner:** `AI-Verse-OS` after contract freeze

Purpose Context is a derived, read-only, disposable projection over canonical owner state. It never becomes a second strategic, Data, Memory, runtime, or Dashboard authority.

> Editorial note: frozen semantics are kept compact here for maintainability; compaction does not weaken the earlier task contracts.

---

## Task 1 — `schema_version` — FROZEN

- Every envelope MUST emit `schema_version: "1.0"`.
- Version is a required UTF-8 `MAJOR.MINOR` string.
- Producers emit it explicitly; consumers never infer it.
- Unsupported major versions fail closed.
- Minor v1 increases may add backward-compatible optional material only; they may not change existing meaning, authority, scope/isolation, or make optional fields required.
- Breaking semantics require a new major version.

---

## Task 2 — supported scope kinds — FROZEN

Supported scopes are exactly `operator` and `workspace:<id>` with `scope_kind: operator|workspace`.

- `scope_kind` and `scope` are required and MUST agree.
- Workspace IDs use `^[a-z0-9][a-z0-9-]{0,127}$`.
- `operator` is not a workspace and not an all-workspace aggregate.
- No implicit cross-workspace reads or scope fallback.
- Workspace type belongs to identity metadata, not scope kind.
- No `global`, `system`, `all-workspaces`, organization/team/client/project/custom scope kind in v1.
- Dashboard `systemId` is never a Purpose scope.

---

## Task 3 — required vs optional fields — FROZEN

Required shell:

```yaml
schema_version: "1.0"
scope: operator | workspace:<id>
scope_kind: operator | workspace
identity:
  kind: operator | workspace
  id: operator | <workspace-id>
provenance: {...}
```

Optional semantic sections: `problems`, `purpose`, `narratives`, `goals`, `priorities`, `challenges`, `strategies`, `initiatives`, `constraints`, `kpis`, `risks`, `current_state`, `current_work`, `recent_material_changes`, `trajectory`.

Presence semantics:

- absent optional section = not emitted because not relevant/applicable/requested;
- present empty collection = owner read succeeded and is known empty under requested bounds;
- attempted unknown/unavailable reads use Task 8 explicit state, never silent omission;
- no placeholders or meaningless empty corporate sections;
- no projected field is independently editable.

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
- generation/read time is never freshness evidence.
- every attempted owner read is recorded.
- refs use Task 6 canonical refs only.
- every authoritative owner-backed claim has non-empty `source_refs`.
- derived claims additionally carry stable `derivation.rule` + source refs.
- derived claims never outrank owner inputs.
- trajectory/material-change claims retain their own evidence refs.
- any emitted claim must be traceable to canonical owner record/version.

---

## Task 5 — freshness format — FROZEN

Leaf freshness:

```yaml
freshness:
  state: current | stale | unknown | unavailable
  as_of: <RFC3339 UTC>
  source_updated_at: <RFC3339 UTC>    # optional
  max_age_seconds: <non-negative int> # optional
  reason: <stable code>               # optional
```

- `current` requires owner assertion or sufficient source/version evidence under policy.
- `stale` = available but too old/superseded for current use.
- `unknown` = read succeeded but recency evidence is insufficient.
- `unavailable` = requested source/value cannot be obtained.
- aggregate values without source watermarks are `unknown`, not `current`.
- derived freshness cannot be stronger than relevant source freshness.
- optional projection summary may use `current|mixed|stale|unknown|unavailable`; `mixed` is summary-only.

---

## Task 6 — canonical ref format — FROZEN

```yaml
owner: ai-verse-brain
scope: workspace:ai-verse
kind: intent
id: goal-public-beta
version: "7"
```

- registered v1 owners: `ai-verse-os`, `ai-verse-brain`, `ai-verse-data`, `ai-verse-memory`, `ai-verse-gateway`;
- identity tuple is `(owner, scope, kind, id)`;
- `version` identifies observed revision and is required for mutable authoritative claims when the owner provides meaningful revision identity;
- refs never contain private paths, DB paths, credentials, secrets, SQL, private transport addresses, or Dashboard `systemId`;
- refs grant no authority and still pass owner scope/authorization checks;
- refs come from owner APIs, never private-storage inference;
- stale/deleted refs never fuzzy-rebind;
- all Purpose evidence/ref fields use this same structure.

---

## Task 7 — deterministic ordering rules — FROZEN

Canonical serialization order: version, scope, scope kind, identity, semantic sections in trajectory order (`problems` through `trajectory`), later v1 contract metadata, then `provenance`.

Collection order:

1. explicit owner-backed semantic priority/rank/order when supplied;
2. otherwise canonical ref identity `(owner, scope, kind, id)` bytewise ascending;
3. then `version`, absent before present;
4. generated deterministic ID as final tie-breaker.

Special cases:

- `priorities`: owner priority/rank, then canonical ref.
- `recent_material_changes`: owner-backed effective/event time descending, then canonical ref; retrieval time never substitutes.
- `current_work`: owner-backed execution priority/order, then canonical ref.
- `trajectory`: source identity, relation token, target identity, evidence refs.
- source/derivation/owner-read refs: canonical ref order.
- owner reads: owner, operation, scope, then observed time ascending.

Rebuilds and budget pruning MUST use deterministic order; arrival/storage iteration order is never semantic unless owner-declared.

---

## Task 8 — unknown/unavailable field behavior — FROZEN

Purpose Context v1 distinguishes four different situations and MUST NOT collapse them:

1. field/section not emitted because irrelevant/not requested;
2. known empty/known absent owner result;
3. unknown truth because evidence is insufficient;
4. unavailable truth because the owner/source cannot currently provide it.

### Section state metadata

When a semantic section was relevant/requested and an owner read was attempted but the section cannot be represented as a normal successful result, emit top-level metadata:

```yaml
section_states:
  kpis:
    state: partial | unknown | unavailable | error
    reason: <stable reason code>
    owner: ai-verse-data
    operation: purpose_kpi_values
```

`section_states` is optional contract metadata introduced by this task. It is emitted only for exceptional/non-complete section states.

Rules:

- `partial` = valid bounded content exists but the owner explicitly reports incompleteness.
- `unknown` = relevant truth may exist, but current evidence is insufficient to determine it.
- `unavailable` = the owner/source cannot currently provide the requested truth.
- `error` = unexpected owner/contract failure; it MUST NOT be converted to `unknown` merely to hide failure.
- `reason` is a stable machine-readable code; optional human text may be added later but is not authoritative.
- `owner` and `operation` identify the failed/partial owner read and must correspond to `provenance.owner_reads`.

### Field state metadata

For an otherwise valid emitted object whose individual field could not be populated, omit the value and emit:

```yaml
field_states:
  current_value:
    state: unknown | unavailable | stale
    reason: source_watermark_missing
```

Rules:

- `field_states` is optional per-object metadata.
- A field with a `field_states` entry MUST NOT simultaneously carry a contradictory concrete current value.
- A stale historical value may be emitted only if clearly represented as stale/historical and not mistaken for current truth.
- Boolean `false`, numeric `0`, empty string, empty collection, and `null` are never automatic synonyms for unknown/unavailable.
- `null` may be used only when the canonical owner explicitly owns `null` as the actual value; otherwise omit the field and use state metadata.

### No-fallback law

Unknown/unavailable current truth MUST NOT trigger silent fallback to:

- Memory history as current truth;
- stale OS strategy when Brain owns direction;
- another workspace;
- another Data database;
- a similarly named object/ref;
- model inference presented as owner fact.

A consumer may still use explicitly historical/contextual evidence for reasoning, but it must remain labeled as such and cannot overwrite the missing current owner truth.

### Explainability law

When unknown/unavailable state affects a strategic answer, the agent/UI must be able to disclose that limitation without exposing private implementation details. Example: “The current KPI value is unavailable; the goal and target are still known.”

---

## Slice 2.1 freeze progress

1. [x] `schema_version`
2. [x] supported scope kinds
3. [x] required vs optional fields
4. [x] provenance format
5. [x] freshness format
6. [x] canonical ref format
7. [x] deterministic ordering rules
8. [x] unknown/unavailable field behavior
9. [ ] bounded size/budget rules
10. [ ] rebuildability contract
