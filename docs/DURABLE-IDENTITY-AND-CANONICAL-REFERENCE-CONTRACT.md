# AI-Verse Durable Identity and Canonical Reference Contract v1

**Status:** canonical System contract  
**Contract ID:** `ai-verse.durable-identity-reference/v1`  
**Owner:** AI-Verse-System  
**Purpose:** define the minimum shared law for durable identity and cross-owner references without taking ownership of component identities.

## 1. Scope

This contract applies when an AI-Verse entity must retain identity across time or when another canonical owner must durably reference it.

It does not require IDs for ordinary files, generated projections, caches, temporary outputs, transient executions or other implementation artifacts that are not durable first-class entities.

AI-Verse-System owns this shared contract only. It does not own component entity IDs, provide a global ID allocator, operate a central identity database, or maintain a global registry of owner objects.

## 2. Canonical identity law

1. A durable first-class entity that needs long-lived or cross-owner references MUST have a stable ID controlled by its canonical owner.
2. Identity MUST be separate from display name, label, title and other mutable descriptive properties.
3. The canonical owner retains authority over ID generation, format, validation, lookup, migration, collision handling and lifecycle semantics.
4. Owners MAY use different ID formats. This contract does not impose UUIDs or any other universal ID syntax on owner `id` values.
5. Display-name equality, filesystem-path equality, content similarity or model inference MUST NOT be used to silently establish durable identity when the owner has not guaranteed that equivalence.
6. Ambiguous, malformed, duplicate or conflicting identity evidence MUST fail closed. It MUST NOT be guessed, merged or rebound automatically.
7. Update, upgrade, recovery and restore logic MAY rely only on identity guarantees explicitly published by the canonical owner.

## 3. Minimal durable-reference envelope

The common cross-owner durable-reference envelope is:

```json
{
  "owner": "ai-verse-brain",
  "kind": "brain-object",
  "id": "5b3bb42e-b423-4f68-8349-d8db64800f55"
}
```

`scope` is added only when the canonical owner requires it for correct identity resolution:

```json
{
  "owner": "ai-verse-memory",
  "kind": "memory-record",
  "id": "mem-20261012-120000-000000-a1b2c3d4",
  "scope": "workspace:film"
}
```

The v1 envelope contains only:

- `owner`: canonical owner responsible for resolving the entity;
- `kind`: owner-defined entity kind within that owner boundary;
- `id`: the owner-controlled durable ID, preserved verbatim;
- `scope`: optional owner-defined resolution scope, present only when required for correct lookup.

The envelope version is defined by this contract/schema version. A per-reference `version` field is intentionally not added.

The envelope is a reference shape, not a registry record. It does not copy canonical entity state and does not create a second source of truth.

## 4. Resolution authority

A consumer resolving a durable reference MUST:

1. route the reference to the declared canonical `owner`;
2. let that owner interpret `kind`, `id` and, when present, `scope`;
3. accept only one unambiguous canonical result;
4. fail closed if the owner reports missing, duplicate, conflicting, malformed or unsupported identity evidence.

Consumers MUST NOT reinterpret another owner's ID format or replace an owner lookup with display-name/path inference.

A durable reference does not itself grant authorization, execution permission, connection access or action approval.

## 5. Identity is distinct from lifecycle and representation

The following concepts MUST remain distinct unless the canonical owner explicitly defines otherwise:

- durable entity ID;
- display name or label;
- filesystem/storage path;
- schema version;
- entity revision/version;
- content digest;
- package version;
- installation generation;
- request, event, transaction, receipt, run, invocation, correlation and idempotency IDs.

A lifecycle or representation change MUST NOT be treated as an identity change unless the owner contract says it is.

Conversely, a changed path or scope MUST NOT be assumed identity-preserving merely because content is similar.

## 6. Workspace law

Workspace identity is owned by AI-Verse-OS.

Current canonical Workspace identity is `WORKSPACE.yaml:id`.

Current supported physical storage remains:

```text
workspaces/<workspace-id>
```

Filesystem independence is not universal. Current OS, Brain, Memory and Data integration intentionally derives the supported Workspace slot from the Workspace ID.

An arbitrary/nested relocation is therefore unsupported today. This contract does not create an ID-to-location registry or relocation resolver.

A future architecture amendment MAY add owner-controlled relocation support, but until then consumers MUST fail closed rather than treating a Workspace found at another path as the same supported Workspace.

## 7. Skill and capability law

AI-Verse-OS owns capability provider scope, ranking and resolution. AI-Verse-Skills owns lifecycle and identity inside the managed `aiverse-skills` distribution provider. Personal reusable capabilities remain user-owned. Workspace-local capabilities remain Workspace-owned.

Current qualified capability identities retain their existing provider semantics:

```text
os:<name>
aiverse-skills:<name>
local:<name>
workspace:<workspace-id>:<name>
```

Provider/scope is therefore part of current qualified capability identity.

A cross-provider move or re-scope MUST NOT be assumed to preserve qualified identity unless a future canonical owner contract explicitly defines and tests that operation.

For managed Skills, these concepts remain distinct:

- managed package identity;
- qualified capability identity;
- immutable generation ID;
- package version;
- content digest.

A generation/version/digest change does not by itself remint the managed package identity.

## 8. Owner-specific implementations are retained

This contract standardizes composition law, not internal owner implementation.

Existing mature owner identity implementations remain canonical, including Workspace, Brain objects, Memory records, Data records, Automations, Multiple Bots, Connections, Gateway-local identities, Dashboard-local connection identity and Token identity-resolution semantics.

Owners are not required to rewrite valid internal IDs into a shared System format.

Apps is the known owner that still requires its own durable App identity implementation. That implementation belongs in AI-Verse-Apps and must conform to this contract without becoming a System-owned registry.

## 9. Update, upgrade, recovery and restore

Cross-owner infrastructure MUST preserve durable identities and durable references according to the guarantees published by each canonical owner.

Infrastructure MUST NOT:

- mint replacement IDs for preserved user-owned entities merely because software changed;
- infer a new identity from a path/name when canonical identity evidence is missing;
- claim a scope/path transfer preserved identity when the owner does not guarantee that;
- treat a generated projection, cache or lifecycle receipt as canonical entity identity.

If identity continuity cannot be proven from owner-guaranteed evidence, the operation MUST stop or report the unresolved condition instead of silently rebinding references.

## 10. Schema

The normative machine-readable envelope schema is:

`contracts/durable-entity-reference-v1.schema.json`

The schema intentionally constrains only the shared envelope. Owner-specific `id` and `scope` semantics remain with their canonical owners.

## 11. Compatibility rule

Additive owner-specific identity evolution is permitted without changing this contract when the v1 envelope remains sufficient.

A breaking change to the shared envelope or its resolution semantics requires a new contract major version. Owner-internal ID-format changes remain owner-controlled and require owner migration guarantees where durable references are affected.

## 12. Non-goals

This contract does not create:

- a global identity service;
- a UUID service;
- a central entity registry;
- an installation-wide AI-Verse instance ID;
- universal filesystem independence;
- automatic Workspace relocation;
- universal identity-preserving re-scope;
- duplicated owner state in AI-Verse-System.
