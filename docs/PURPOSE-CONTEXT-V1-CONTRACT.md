# AI-Verse Purpose Context v1 Contract

**Status:** COMPLETE — Slice 2.1 contract frozen  
**Parent plan:** `docs/PURPOSE-CONTEXT-IMPLEMENTATION-PLAN.md`  
**Canonical owner:** `AI-Verse-System`  
**Implementation owner:** `AI-Verse-OS`

Purpose Context is a derived, read-only, disposable projection over canonical owner state. It never becomes a second strategic, Data, Memory, runtime, or Dashboard authority.

---

## Task 1 — `schema_version` — FROZEN

Every envelope emits `schema_version: "1.0"`. Unsupported major versions fail closed; minor v1 changes may add backward-compatible optional material only; breaking semantics require a new major version.

## Task 2 — supported scope kinds — FROZEN

Supported scopes are exactly `operator` and `workspace:<id>` with matching `scope_kind: operator|workspace`. Workspace IDs use `^[a-z0-9][a-z0-9-]{0,127}$`. No implicit global/all-workspace/system scope, no cross-workspace fallback, and Dashboard `systemId` is never a Purpose scope.

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

## Task 4 — provenance format — FROZEN

Every projection records `projection_owner: ai-verse-os`, `generated_at`, and all attempted `owner_reads` with owner, operation, exact scope, status, observed time, freshness, and canonical refs. Every authoritative claim has source refs; derived claims also have stable derivation-rule identity. Generation/read time never proves freshness. Claims remain verifiable to canonical owner record/version.

## Task 5 — freshness format — FROZEN

Leaf states are `current | stale | unknown | unavailable`, each with `as_of`; optional source update time, age policy, and reason code may be carried. `current` requires owner/source evidence. Aggregate query time alone never proves currentness. Derived freshness cannot be stronger than relevant source freshness. Projection summary may additionally use `mixed`.

## Task 6 — canonical ref format — FROZEN

Canonical ref identity is `(owner, scope, kind, id)` with exact string `version` for mutable authoritative claims when the owner exposes meaningful revision identity. Registered v1 owners: OS, Brain, Data, Memory, Gateway. Refs grant no authority, never expose private paths/secrets/SQL/systemId, come only from owner APIs, and never fuzzy-rebind.

## Task 7 — deterministic ordering rules — FROZEN

Owner-backed semantic priority/rank/order wins when present; otherwise collections sort by canonical ref identity, then version, then deterministic generated ID. Recent material changes use owner event/effective time descending; trajectory uses source/ref relation/target/evidence order. Rebuild and pruning use deterministic order; storage/API arrival order is never semantic unless owner-declared.

## Task 8 — unknown/unavailable field behavior — FROZEN

Purpose distinguishes not-emitted, known-empty, unknown, unavailable, partial, error, and stale. Exceptional section state uses `section_states`; exceptional individual field state uses `field_states`. No silent fallback to Memory-as-current, stale OS strategy under Brain ownership, another workspace/database, similarly named records, or model inference.

## Task 9 — bounded size/budget rules — FROZEN

- default projection ceiling: **16384 serialized UTF-8 bytes**;
- caller-supported range: **4096–65536 bytes**; outside values fail validation;
- runtime may impose a smaller injection budget;
- all lists are finite and implementation defines deterministic per-section caps;
- deterministic pruning removes optional richness/lower-ranked branches before core trajectory truth;
- required shell, truth-state metadata, refs/freshness for retained claims, and canonical graph identity cannot be silently pruned;
- if the truthful minimum cannot fit, fail explicitly;
- when pruning occurs, `provenance.budget` records maximum bytes, final bytes, truncation and deterministic omission diagnostics.

---

## Task 10 — rebuildability contract — FROZEN

Purpose Context v1 has **no canonical Purpose state**. Canonical truth remains entirely in the existing owners.

### Rebuild law

Given the same:

- Purpose contract major/minor version;
- exact scope;
- projection profile/relevance request;
- byte budget;
- owner responses and their canonical refs/versions/freshness metadata;
- deterministic derivation rules;

the composer MUST produce semantically equivalent Purpose content and deterministic ordering.

The following volatile observation metadata is excluded from semantic-equivalence comparison when the underlying inputs are unchanged:

- `provenance.generated_at`;
- owner-read `observed_at`;
- freshness `as_of` evaluation time;
- runtime timing/latency diagnostics.

Volatile timestamps may differ across rebuilds; owner-backed claims, refs, versions, relation identities, ordering, omission decisions under the same budget, and truth-state classifications MUST NOT drift nondeterministically.

### Disposable projection law

- Deleting any generated Purpose output/cache/index MUST destroy no canonical user state.
- A clean restart with unchanged owner state MUST require no migration/recovery of Purpose canonical data because none exists.
- Re-reading after cache deletion MUST rebuild from owner APIs/contracts.
- No Purpose read may mutate canonical owner state merely to make the projection complete.
- No generated ID may become the only durable identifier for an owner-backed object.

### Cache law

A cache is not required for v1. If a later implementation introduces one for performance:

- it is explicitly derived/disposable;
- cache keys include at least scope, contract version, projection profile and budget class;
- cached owner-backed claims retain source refs/versions;
- cached content cannot be served as current authoritative truth after its owner versions/freshness can no longer be revalidated;
- owner drift invalidates or downgrades the cached projection rather than being hidden;
- cache loss is always recoverable by re-reading owners.

### Input drift / concurrent owner change

Purpose is not a new cross-owner transaction manager. If canonical owners change during composition:

- each retained claim keeps the exact observed owner ref/version;
- the composer MUST NOT merge two revisions into one claim without explicit derivation provenance;
- if a critical owner changes between initial read and required verification, the composer retries/rebuilds or returns explicit stale/partial/unavailable state rather than pretending one coherent current snapshot existed;
- an older cached projection never overrules a newer owner read.

### Rebuild verification

Implementation tests MUST prove at minimum:

1. delete/rebuild preserves semantic content from unchanged owner inputs;
2. repeated reads do not create duplicate Purpose state;
3. owner mutation changes the rebuilt projection and/or freshness/version evidence deterministically;
4. stale cache cannot override current owner state;
5. workspace A rebuild never consumes workspace B owner state;
6. Brain-owned direction rebuild never resurrects stale OS strategy;
7. budget pruning is deterministic across rebuilds;
8. no Purpose artifact is required to restore canonical owner truth after clean-machine restart.

### Authority law

A generated Purpose projection may be useful, cached, displayed, injected, or explained, but it is never an authority source for reconstructing Brain, OS, Data, or Memory canonical state.

---

## Slice 2.1 final status

1. [x] `schema_version`
2. [x] supported scope kinds
3. [x] required vs optional fields
4. [x] provenance format
5. [x] freshness format
6. [x] canonical ref format
7. [x] deterministic ordering rules
8. [x] unknown/unavailable field behavior
9. [x] bounded size/budget rules
10. [x] rebuildability contract

**Slice 2.1: COMPLETE / CONTRACT FROZEN.**

Acceptance verdict:

- versioned schema contract exists: PASS;
- absent optional fields distinct from unknown/unavailable: PASS;
- stale owner reads represented explicitly: PASS;
- no generated field independently editable: PASS;
- projection bounded and rebuildable/disposable: PASS.

**NEXT:** Slice 2.2 / Task 1 — freeze trajectory relation vocabulary.
