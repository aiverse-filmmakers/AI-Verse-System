# AI-Verse Purpose Context v1 Contract

**Status:** IN PROGRESS — Slice 2.1 contract freeze  
**Parent plan:** `docs/PURPOSE-CONTEXT-IMPLEMENTATION-PLAN.md`  
**Scope:** derived/read-only Purpose Context projection only  
**Canonical owner of this contract:** `AI-Verse-System`  
**Implementation owner:** `AI-Verse-OS` after the contract is frozen

Purpose Context is a disposable, rebuildable projection over canonical owner state. Nothing in this document creates a second strategic, Data, Memory, or runtime authority.

---

## Task 1 — `schema_version` — FROZEN

The v1 serialized envelope MUST emit:

```yaml
schema_version: "1.0"
```

Contract rules:

- `schema_version` is a required UTF-8 string in `MAJOR.MINOR` decimal form.
- The initial Purpose Context contract version is exactly `"1.0"`.
- Producers MUST emit the version explicitly; consumers MUST NOT infer it from file names, repository refs, runtime version, or transport metadata.
- An unsupported major version MUST fail closed as an unsupported Purpose Context contract. It must not be interpreted as v1 by best effort.
- A minor-version increase within major `1` may add backward-compatible optional fields or enum values only when the owning contract explicitly permits them. It may not change the meaning of an existing field, make an optional field required, weaken scope/isolation rules, or change owner authority.
- Any incompatible semantic change requires a new major version.
- Repository/component release versions and `schema_version` are independent. A newer OS/Brain/Data/Memory/Gateway build may still emit Purpose Context `"1.0"`.
- The version applies to the complete Purpose Context envelope, including its provenance/freshness/reference substructures unless a later contract explicitly versions one of those substructures separately.

### Compatibility law

A consumer may accept a Purpose Context envelope only when it understands the declared major version and all required fields for that version. Unknown fields must never grant authority or silently override known owner-backed fields.

---

## Task 2 — supported scope kinds — FROZEN

Purpose Context v1 supports exactly two strategic scope kinds:

```yaml
scope_kind: operator
scope: operator
```

or:

```yaml
scope_kind: workspace
scope: workspace:<workspace-id>
```

Contract rules:

- `scope_kind` is required and MUST be exactly `operator` or `workspace`.
- `scope` is required and MUST be exactly `operator` for operator scope or `workspace:<id>` for workspace scope.
- `scope_kind` is a deterministic projection of `scope`; the two fields MUST agree. A mismatch is an invalid envelope and must fail closed.
- Canonical workspace IDs use the existing OS/Data/Gateway contract: lowercase ASCII alphanumeric plus hyphen, beginning with an alphanumeric character, maximum 128 characters total. The v1 workspace-id pattern is `^[a-z0-9][a-z0-9-]{0,127}$`.
- `operator` is a strategic/global operator scope sentinel, not a workspace ID and not a hidden aggregate over all workspaces.
- `workspace:<id>` reads are bound to that exact workspace. They MUST NOT silently import strategic state from another workspace.
- Workspace type (`project`, `product`, `client`, `team`, `business`, `case`, etc.) belongs in identity metadata; it does not create a new Purpose scope kind.
- v1 does not support `system`, `global`, `all-workspaces`, `organization`, `team`, `client`, `project`, or arbitrary custom values as `scope_kind`.
- Cross-scope relationships, when later allowed by the trajectory contract, must be explicit, provenance-bearing and authorized. They never widen the projection's bound scope by implication.
- The Dashboard-local `systemId` is transport/connection identity only and MUST NOT appear as a Purpose strategic scope.

### Scope authority law

The Purpose composer receives an already-resolved canonical scope. It may validate that scope, but it may not invent, broaden, substitute, or auto-fallback to a different strategic scope when an owner read is unavailable.

---

## Task 3 — required vs optional fields — FROZEN

### Required top-level fields

Every valid Purpose Context v1 envelope MUST contain exactly these contract-required top-level fields:

```yaml
schema_version: "1.0"
scope: operator | workspace:<id>
scope_kind: operator | workspace
identity: {...}
provenance: {...}
```

`identity` is required because OS owns the bound operator/workspace identity even when no strategic content exists yet. Its required minimum is:

```yaml
identity:
  kind: operator | workspace
  id: operator | <workspace-id>
```

Optional identity fields such as `name`, `type`, `status`, or other owner-backed descriptive metadata may be emitted only when supplied by the canonical identity owner.

`provenance` is always required because Purpose is a derived projection and every projection must declare how it was assembled. Its exact format is frozen in Task 4.

### Optional semantic sections

The following top-level semantic sections are optional in v1 and MUST be emitted only when relevant, applicable, requested by the projection profile, or necessary to represent an explicit owner-read state:

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

`purpose`, when present, may contain owner-backed `mission` and `desired_outcomes` fields. Neither subfield is individually required simply because the `purpose` section exists; explicit unknown/unavailable semantics are frozen in Task 8.

### Presence semantics

- **Absent optional section** means the section was not emitted because it was not relevant/applicable/requested for this bounded projection. Absence MUST NOT be interpreted as `unknown`, `unavailable`, or `known empty`.
- **Present empty collection** means the relevant owner read succeeded for that section and the owner-backed result is known to contain zero items under the requested bounds.
- A producer MUST NOT emit meaningless empty rich-corporate sections merely to fill a template.
- A producer MUST NOT invent placeholder records so that a section appears populated.
- If an owner read was attempted but its truth could not be obtained, the producer must use the explicit unknown/unavailable representation frozen in Task 8 rather than silently omitting the failure.
- Optional fields within emitted items follow the same law: omission means not emitted/not applicable; it does not automatically mean unknown or false.

### Mutability law

No top-level or nested Purpose field is independently editable merely because it appears in the projection. Any durable change must route to that field's canonical owner under the existing authority/confirmation rules.

---

## Slice 2.1 freeze progress

1. [x] `schema_version`
2. [x] supported scope kinds
3. [x] required vs optional fields
4. [ ] provenance format
5. [ ] freshness format
6. [ ] canonical ref format
7. [ ] deterministic ordering rules
8. [ ] unknown/unavailable field behavior
9. [ ] bounded size/budget rules
10. [ ] rebuildability contract
