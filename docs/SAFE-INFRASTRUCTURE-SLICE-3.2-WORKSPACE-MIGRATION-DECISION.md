# Safe Infrastructure Slice 3.2 - Workspace Migration / Reference Repair Decision

**Status:** COMPLETE - NO WORKSPACE RELOCATION MIGRATION IS CURRENTLY ADMITTED OR REQUIRED  
**Slice:** 3.2 - Implement admitted OS Workspace migration/reference repair only if required  
**Date:** 2026-10-12

## Refreshed evidence refs

- `aiverse-filmmakers/AI-Verse-System@ed98c92028dc7b0659ffb11a237976e924705034` at audit refresh
- Slice 3.2 task list recorded at `aiverse-filmmakers/AI-Verse-System@8fe317453fd4f535d9cc1954e6a4f803008c2dbc`
- `aiverse-filmmakers/AI-Verse-OS@88ce41a95554e1323ba34aa71b536b9e98475808`
- `aiverse-filmmakers/AI-Verse-Data@f8978f8f7a1bc94edecddc2662112233289159a3`
- `aiverse-filmmakers/AI-Verse-Brain@69f7912eeb35f0178f6952ff0554aec8d7f2c496`
- `aiverse-filmmakers/AI-Verse-Memory@f1327be48ba2ee0043959021365e6dbb9dcb1d3a`

## Decision

**Do not implement a Workspace relocation/move/reference-repair handler in Slice 3.2.**

The current canonical owner architecture has one supported Workspace physical slot:

```text
workspaces/<workspace-id>
```

The canonical logical identity remains:

```text
WORKSPACE.yaml:id
```

There is no second admitted Workspace location model, no previous structural generation that is authorized to migrate into `workspace-id-slot-v1`, no ID-to-location locator/registry, and no owner contract that permits arbitrary/nested relocation while preserving the same Workspace identity.

Creating a relocation handler now would invent a new architecture rather than migrate an admitted old architecture. It would violate the protected requirements that migration semantics come from canonical owners, identity continuity may rely only on owner guarantees, and arbitrary Workspace relocation must not be assumed.

## Canonical contract evidence

The System durable-identity contract explicitly states:

- Workspace identity is owned by AI-Verse-OS;
- current identity is `WORKSPACE.yaml:id`;
- current physical storage is `workspaces/<workspace-id>`;
- OS, Brain, Memory and Data intentionally derive that slot from the Workspace ID;
- arbitrary/nested relocation is unsupported;
- the contract does not create an ID-to-location registry or relocation resolver;
- consumers must fail closed when a Workspace appears at another path rather than assuming it is the same supported Workspace.

Therefore there is no canonical identity-continuity guarantee for a physical move away from the current ID-derived slot.

## OS owner evidence

Slice 3.1 established OS generation `workspace-id-slot-v1` and a read-only detector.

OS defines a Workspace as current only when its real direct-child slot and `WORKSPACE.yaml:id` agree. The detector explicitly classifies nested/relocated structures as `BLOCKED/REVIEW`; it does not move them or infer identity from similar content.

The destructive-negative tests prove:

- legitimate direct-child Workspaces remain current with arbitrary custom/user content;
- changing semantic domain metadata does not relocate the Workspace;
- ID/slot mismatch fails closed;
- duplicate identity evidence fails closed;
- nested/domain-first Workspace manifests fail closed and are not moved into a new slot;
- symlinked Workspace slots fail closed;
- missing/invalid identity is not guessed;
- every detection scenario is snapshot-checked to perform no filesystem mutation.

No OS migration code is therefore missing for an admitted current transition. The existing `scripts/workspace-owner.mjs` remains the create/evolve primitive, while `scripts/workspace-infrastructure.mjs` remains the read-only structural detector.

## Current reference-consumer evidence

### AI-Verse-OS current context

`AI-Verse-OS/scripts/current-context.mjs` resolves `workspace:<id>` directly to:

```text
workspaces/<id>/context/CURRENT.md
```

It requires the Workspace to occupy that expected real physical slot and rejects symlink/escape conditions.

### AI-Verse-OS Workspace capability provider

`AI-Verse-OS/scripts/capability-resolver-core.mjs` maps `workspace:<id>` directly to:

```text
workspaces/<id>/skills/
```

It verifies the Workspace is beneath the real OS `workspaces` root and requires `WORKSPACE.yaml` before exposing Workspace-local capabilities.

### AI-Verse-Data

`AI-Verse-Data/src/native/workspace-resolver.ts` derives the Workspace from:

```text
workspaces/<workspace-id>/WORKSPACE.yaml
```

and its database from:

```text
workspaces/<workspace-id>/data/ai-verse-data.sqlite
```

A manifest ID that differs from the requested Workspace ID fails closed as `WORKSPACE_ID_MISMATCH` with copied/misplaced Workspace wording.

### AI-Verse-Brain

`AI-Verse-Brain/engine/aiverse_brain/direction_ownership.py` derives Workspace current-direction sources and OS handback targets from:

```text
workspaces/<workspace-id>/context/CURRENT.md
```

It does not expose an alternate Workspace locator.

### AI-Verse-Memory

`AI-Verse-Memory/scripts/memory_engine.py` discovers native Workspaces as direct children of `workspaces/` containing `WORKSPACE.yaml`, normalizes native scope to `workspace:<id>`, stores Workspace atomic memories under:

```text
workspaces/<id>/memory/atomic/
```

and maps native source ownership from paths rooted under `workspaces/<id>`.

These owners are intentionally aligned on the same current slot. None is resolving a deprecated alternative that requires repair or retirement.

## Reference repair determination

Reference repair is **not applicable in the current architecture** because Slice 3.2 performs no physical path change and retires no writable route.

No owner reference can be left pointing only at a retired slot because no slot is being retired.

This is stronger and safer than introducing compatibility shims or duplicate routes for a move the owner contract does not admit.

If a future System/OS architecture amendment introduces owner-controlled relocation, that future migration must explicitly update or prove unaffected at least:

1. OS Workspace discovery/creation;
2. OS current-context resolution;
3. OS Workspace capability provider roots;
4. Data Workspace manifest/database resolution;
5. Memory Workspace discovery/scope/source/storage resolution;
6. Brain Workspace direction/current-context paths;
7. any owner-declared durable relative Workspace path reference;
8. connections/automations only where their canonical owner proves path dependence.

That future contract must preserve the Workspace ID and complete the full declared repair graph before an old writable route can retire.

## Acceptance mapping

- **migration is idempotent:** NOT APPLICABLE. No migration is admitted or executed, so repeated detection remains read-only rather than inventing mutation.
- **files/content are preserved:** PASS. No Workspace file is moved, rewritten or deleted.
- **owner-defined Workspace identity continuity rules are satisfied:** PASS. `WORKSPACE.yaml:id` remains coupled to `workspaces/<id>` exactly as currently guaranteed.
- **affected owner references are repaired or proven unaffected:** PASS. They are proven unaffected because no path or identity changes occur.
- **no supported owner is left resolving only a retired slot:** PASS. No supported slot is retired.
- **old writable structure retires only after verification:** NOT APPLICABLE. There is no admitted old writable Workspace structure to retire.
- **ambiguous/custom layouts fail safely or require practical review:** PASS. Slice 3.1 detector returns `BLOCKED/REVIEW` and does not auto-relocate them.
- **default output explains practical effect without exposing internal paths unless details are requested:** NO NEW MEMBER-FACING MIGRATION OUTPUT REQUIRED. There is no migration operation for the member to invoke in this slice; plain-English aggregation remains a later Distribution UX concern.

## Implementation classification

- current `workspaces/<id>` storage model: **REUSE**;
- `workspace-id-slot-v1` detector: **REUSE**;
- current OS/Data/Brain/Memory path-coupled consumers: **REUSE**;
- Workspace relocation resolver/registry: **NOT ADMITTED / DO NOT CREATE**;
- Workspace move handler: **NOT REQUIRED / DO NOT CREATE**;
- cross-owner reference-repair transaction for Workspace move: **NOT REQUIRED until a relocation contract exists**;
- compatibility route for an invented alternate Workspace layout: **DO NOT CREATE**.

## Result

Slice 3.2 closes without owner code changes. This is an evidence-backed no-op, not skipped work.

The roadmap made the migration conditional. Current evidence proves that the condition for implementing a move is false. Preserving the current architecture is therefore the correct implementation result.

Next execution unit is Slice 3.3, which must be derived separately from current OS capability-provider and Skills lifecycle evidence.
