# AI-Verse Purpose Context v1 Contract

**Status:** IN PROGRESS — Slice 2.1 contract freeze  
**Parent plan:** `docs/PURPOSE-CONTEXT-IMPLEMENTATION-PLAN.md`  
**Canonical owner:** `AI-Verse-System`  
**Implementation owner:** `AI-Verse-OS` after contract freeze

Purpose Context is a derived, read-only, disposable projection over canonical owner state. It never becomes a second strategic, Data, Memory, runtime, or Dashboard authority.

> Editorial note: frozen semantics are kept compact here for maintainability; compaction does not weaken earlier task contracts.

---

## Task 1 — `schema_version` — FROZEN

Every envelope emits `schema_version: "1.0"`. Unsupported major versions fail closed; minor v1 changes may add backward-compatible optional material only; breaking semantics require a new major version.

---

## Task 2 — supported scope kinds — FROZEN

Supported scopes are exactly `operator` and `workspace:<id>` with matching `scope_kind: operator|workspace`. Workspace IDs use `^[a-z0-9][a-z0-9-]{0,127}$`. No implicit all-workspace/global/system scope, no cross-workspace fallback, and Dashboard `systemId` is never a Purpose scope.

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

Absent optional section means not relevant/applicable/requested. Present empty means owner-backed known empty. Attempted unknown/unavailable reads use explicit state metadata. No placeholders and no projected field is independently editable.

---

## Task 4 — provenance format — FROZEN

Every projection records `projection_owner: ai-verse-os`, `generated_at`, and all attempted `owner_reads` with owner, operation, exact scope, status, observed time, freshness, and canonical refs. Every authoritative claim has source refs; derived claims also have stable derivation-rule identity. Generation/read time never proves freshness. Claims must remain verifiable back to canonical owner record/version.

---

## Task 5 — freshness format — FROZEN

Leaf states are `current | stale | unknown | unavailable`, each with `as_of`; optional source update time, age policy, and reason code may be carried. `current` requires owner/source evidence. Aggregate query time alone never proves currentness. Derived freshness cannot be stronger than relevant source freshness. Projection summary may additionally use `mixed`.

---

## Task 6 — canonical ref format — FROZEN

Canonical ref identity is `(owner, scope, kind, id)` with an exact string `version` for mutable authoritative claims when the owner exposes meaningful revision identity. Registered v1 owners: OS, Brain, Data, Memory, Gateway. Refs grant no authority, never expose private paths/secrets/SQL/systemId, come only from owner APIs, and never fuzzy-rebind when stale/deleted.

---

## Task 7 — deterministic ordering rules — FROZEN

- Owner-backed semantic priority/rank/order wins when present.
- Otherwise collections sort by canonical ref `(owner, scope, kind, id)`, then version, then deterministic generated ID.
- Recent material changes sort by owner-backed event/effective time descending then canonical ref.
- Trajectory sorts by source ref, relation, target ref, evidence refs.
- Owner reads sort by owner, operation, scope, then observed time.
- Arrival/storage iteration order is never semantic unless owner-declared.
- Rebuild and budget pruning use deterministic order.

---

## Task 8 — unknown/unavailable field behavior — FROZEN

Purpose distinguishes: not emitted, known empty, unknown, unavailable, plus explicit error/partial states.

Exceptional section state uses:

```yaml
section_states:
  kpis:
    state: partial | unknown | unavailable | error
    reason: <stable code>
    owner: ai-verse-data
    operation: purpose_kpi_values
```

Exceptional individual field state uses:

```yaml
field_states:
  current_value:
    state: unknown | unavailable | stale
    reason: <stable code>
```

No silent fallback to Memory-as-current, stale OS strategy under Brain ownership, another workspace/database, similarly named records, or model inference. `false`, `0`, empty string/list and `null` are not automatic unknown markers.

---

## Task 9 — bounded size/budget rules — FROZEN

Purpose Context v1 is always budgeted. A projection request MAY supply an explicit `max_bytes`; otherwise the OS Purpose composer uses the v1 default.

### Byte budget

- default `max_bytes`: **16384** serialized UTF-8 bytes;
- supported caller range: **4096–65536** bytes;
- values outside the supported range fail validation rather than being silently clamped;
- the budget applies to the complete serialized envelope, including provenance/state metadata;
- runtime/Gateway may impose a smaller downstream context budget; a larger Purpose read budget never forces the runtime to inject all returned content.

This budget is a safety/anti-bloat ceiling, not a target size. Producers SHOULD return materially less when the useful projection is smaller.

### Deterministic pruning order

When the full eligible projection exceeds `max_bytes`, pruning MUST be deterministic and preserve the core trajectory before optional richness.

Prune in this order, stopping as soon as the envelope fits:

1. optional rich workspace extensions not required for the current question/profile (`customers`, `infrastructure`, `team/resources`, budget/cost-style extensions when later enabled);
2. low-relevance `risks`, `narratives`, `recent_material_changes`, and non-current-state supporting detail beyond configured per-section caps;
3. lower-ranked items within retained optional sections using Task 7 ordering/rank semantics;
4. non-essential descriptive text/excerpts while retaining IDs, relation/evidence refs, state, and required provenance needed to interpret retained claims;
5. lower-relevance secondary trajectory branches, while preserving the best verified path(s) needed for the requested/current-work explanation.

The producer MUST NOT prune by nondeterministic arrival order.

### Never-prune-without-failure core

A successful envelope must always retain:

- required shell: version/scope/scope_kind/identity/provenance;
- state metadata needed to distinguish unknown/unavailable/error for retained sections;
- source refs and freshness needed to interpret every retained authoritative claim;
- the canonical identity of every retained graph node/edge;
- enough trajectory context to avoid turning a retained child claim into an invented/ambiguous explanation.

If even the required shell plus minimum truthful metadata cannot fit the requested budget, the read MUST fail explicitly with a budget-too-small condition. It must not emit an invalid/truth-weakened envelope.

### Budget diagnostics

`provenance.budget` MAY be emitted and, when pruning occurred, MUST be emitted:

```yaml
budget:
  max_bytes: 16384
  serialized_bytes: 12140
  truncated: true
  omitted_sections: [narratives, risks]
  omitted_item_counts:
    recent_material_changes: 12
```

Rules:

- diagnostics reveal projection-shaping facts only, not hidden reasoning/chain-of-thought;
- `serialized_bytes` measures the final UTF-8 envelope;
- omission counts are deterministic and section-scoped;
- budget pressure never widens scope, weakens owner authority, fabricates summaries, or upgrades stale/unknown data to current.

### Per-section hard bounds

Implementation MUST define deterministic finite caps for every unbounded list before runtime release. The exact numeric caps may be tuned during implementation/value-gate testing without changing v1 semantics provided they stay within `max_bytes`, preserve Task 7 ordering, and are observable in diagnostics. No v1 section may return an unbounded list.

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
9. [x] bounded size/budget rules
10. [ ] rebuildability contract
