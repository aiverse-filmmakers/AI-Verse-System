# Safe Infrastructure Slice 1.2 Ownership, Identity, Reference, Migration, Health and Recovery Inventory

**Program:** `docs/SAFE-INFRASTRUCTURE-UPGRADE-AND-RECOVERY-IMPLEMENTATION-PLAN.md`  
**Slice:** 1.2 - Build ownership, identity, reference, migration, health and recovery inventory  
**Date:** 2026-10-12  
**Nature:** evidence/inventory only. No Workspace migration, Skill re-scoping, reference repair, recovery engine or Phase 2/3 implementation is performed here.

## 1. Starting refs

Refs refreshed before this slice inventory was frozen:

- `aiverse-filmmakers/AI-Verse-System@11940b87838afa0f46570ecdd8f8e00f74b7de5a`
- `aiverse-filmmakers/ai-verse-distribution@fd11b4a95487638d47ff55472a3703b03892d0e8`
- `aiverse-filmmakers/AI-Verse-OS@64f7325444d18f94c9d4755d32eb89f3468bda6b`
- `aiverse-filmmakers/AI-Verse-Skills@afde5c06307fba7d074de2929c2eb6c3dc6bdab8`
- `aiverse-filmmakers/AI-Verse-Brain@69f7912eeb35f0178f6952ff0554aec8d7f2c496`
- `aiverse-filmmakers/AI-Verse-Memory@f1327be48ba2ee0043959021365e6dbb9dcb1d3a`
- `aiverse-filmmakers/AI-Verse-Data@f8978f8f7a1bc94edecddc2662112233289159a3`

The separate Identity Hardening plan was inspected only for reconciliation boundaries. It remains a separate roadmap and is not implemented by this slice.

## 2. Derived task list

This is the smallest evidence-backed task list required by Slice 1.2 acceptance criteria.

- [x] **1.2-T1** Resolve the Slice 1.1 Skill ownership amendment against shipped OS/Skills provider contracts.
- [x] **1.2-T2** Freeze Workspace logical identity, current canonical storage semantics and relocation support from OS/Data/Brain/Memory source.
- [x] **1.2-T3** Inventory proven cross-owner/path-derived Workspace consumers that would be affected by any future path relocation.
- [x] **1.2-T4** Freeze Skill provider identities, scope ownership, managed package identity/lifecycle ownership and scope-transfer identity rules from shipped contracts.
- [x] **1.2-T5** Inventory owner doctor/check fan-out and classify migration/update/recovery machinery as `REUSE`, `EXTEND`, `CREATE`, `RETIRE` or `BLOCK/UNKNOWN`.
- [x] **1.2-T6** Classify recovery material into capture, exact reconstruction, rebuildable/disposable and external/security-sensitive categories, including large workspace assets/outputs and credentials.
- [x] **1.2-T7** Record Phase 1 identity/recovery handoff items that the separate Identity Hardening plan must reconcile before Safe Infrastructure Phase 2.

## 3. Resolved plan amendments

### 3.1 Skill scope/provider ownership amendment: APPROVED FROM EVIDENCE

The Slice 1.1 blocker is resolved using shipped contracts as higher authority than the roadmap assumption.

**Canonical decision for this program:**

- **OS owns provider scope, provider resolution/ranking, workspace authorization, connection/permission context and execution routing.**
- **Skills owns the managed `aiverse-skills` distribution provider:** package IDs/metadata, source pins/provenance, profiles, immutable generations, install/update/rollback/uninstall, package integrity and provider index publication.
- **Workspace Skills remain workspace-owned user state.**
- **Personal reusable Skills remain user-owned state in the OS-configured local provider.**
- **Distribution coordinates admitted lifecycle/migration operations but does not decide Skill placement/scope.**

Therefore the old Safe Infrastructure wording that assigned cross-provider Skill scope/re-scoping semantics to Skills is amended. Cross-provider placement is an OS semantic decision; Skills remains authoritative for lifecycle and identity inside its managed distribution provider.

Evidence:

- OS `system/contracts/capability-provider-v1/README.md` at `64f7325...`, sections 1, 2 and 6.
- Skills `docs/AI_VERSE_OS_INTEGRATION.md` at `afde5c0...`, especially Separation and ownership.

### 3.2 Workspace physical hierarchy assumption amendment: APPROVED FROM EVIDENCE

The roadmap's motivating example suggested a possible physical target such as `workspaces/YouTube/<ChannelName>/`. Verified current architecture does not support that as an admitted Workspace location.

**Canonical decision for this program:**

- Workspace logical identity is the manifest `WORKSPACE.yaml:id`.
- Current canonical physical storage is derived from that identity as `workspaces/<workspace-id>`.
- The path string is not a separate logical identity, but the current resolver contract intentionally couples the ID to that physical slot.
- A Workspace at a different nested/arbitrary path is not currently a supported equivalent location.
- Safe Infrastructure therefore MUST NOT implement or assume domain-first physical relocation in Phase 2/3 unless a later canonical identity/storage amendment explicitly changes this contract.
- Domain/category meaning may continue to live in semantic metadata such as Workspace `domains`; this program does not invent a new physical hierarchy merely for aesthetics.

Evidence:

- OS `system/schemas/workspace.schema.yaml` at `64f7325...` gives the first-class required `id`.
- OS `scripts/workspace-owner.mjs` creates `workspaces/<desired.id>` and preserves an existing manifest ID during additive evolution.
- OS `scripts/test-workspace-owner.mjs` proves rediscovery/evolution preserves the existing logical ID and avoids duplicate creation.
- Data `src/native/workspace-resolver.ts` at `f8978f8...` resolves `workspaces/<workspaceId>/WORKSPACE.yaml`, derives Data storage below that slot and fails closed on `WORKSPACE_ID_MISMATCH`, explicitly treating a copied/misplaced workspace as invalid.
- OS `scripts/current-context.mjs`, OS capability resolver, Brain direction ownership and Memory native scope code all derive workspace state from `workspaces/<id>`.

This amendment does not weaken stable identity law. It clarifies that filesystem independence is not currently an implemented Workspace capability.

## 4. Ownership inventory

| Surface | Canonical owner | Classification | Frozen Phase 1 conclusion |
| --- | --- | --- | --- |
| Cross-repo lifecycle/recovery law | System | `REUSE/EXTEND` | System defines invariant, not owner data. |
| Software update/release activation | Distribution | `REUSE/EXTEND` | Existing Core updater remains canonical. |
| Whole-install doctor aggregation | Distribution | `REUSE/EXTEND` | Existing fan-out calls owner doctors; extend rather than duplicate. |
| Whole-install Last-Known-Good/restore | Distribution | `CREATE` on existing transaction substrate | No product-level restore exists yet. |
| Workspace structure/manifest semantics | OS | `REUSE/EXTEND` | OS owns Workspace creation, schema and any future structural migration. |
| Workspace logical ID | OS | `REUSE` | `WORKSPACE.yaml:id`. |
| Workspace canonical storage slot | OS contract, consumed cross-owner | `REUSE/CLARIFY` | `workspaces/<workspace-id>` remains current contract. |
| Workspace Data database | Data | `REUSE` | Data binds database to validated Workspace ID and canonical slot. |
| Workspace Brain direction handover | Brain using OS scope | `REUSE` | Brain consumes `workspace:<id>` and current OS slot. |
| Workspace Memory records | Memory | `REUSE` | Memory scope is `workspace:<id>` and native storage is current Workspace slot. |
| OS capability provider scope/resolution | OS | `REUSE/EXTEND` | OS owns scope/ranking/selection. |
| Managed distributed Skill package lifecycle | Skills | `REUSE/EXTEND` | Immutable generations/package IDs/provenance already mature. |
| Personal reusable Skill storage/provider | User, resolved by OS | `REUSE` | Outside Skills distribution ownership. |
| Workspace-local Skill storage/provider | Workspace owner, resolved by OS | `REUSE` | Outside Skills distribution ownership. |
| Cross-provider Skill re-scoping/promotion decision | OS | `EXTEND` | Placement/scope semantics belong to OS, not Skills distribution. |
| Managed provider internal migration | Skills | `REUSE/EXTEND` | Skills owns migrations wholly inside `aiverse-skills`. |
| Cross-provider move implementation | Not admitted yet | `BLOCK/UNKNOWN` | Requires identity/scope-transfer contract before implementation. |
| Legacy writable-route retirement | Owner-specific | `BLOCK/UNKNOWN` | No retirement justified yet. |

## 5. Workspace identity and path inventory

### 5.1 What is the Workspace identity?

The stable logical identity is `WORKSPACE.yaml:id`.

Evidence that it is more than a display label:

- it is schema-required and constrained independently from `name`;
- workspace-owner preserves the existing manifest ID when a proposed duplicate/evolution is recognized by name/source evidence;
- scopes across OS, Brain and Memory use `workspace:<id>`;
- Data validates that the requested Workspace ID and manifest identity agree.

### 5.2 Is Workspace path part of identity?

**Frozen answer:** path is **storage derived from identity**, not a second independent logical identity. However, current shipped architecture intentionally requires the stable ID to occupy the physical slot `workspaces/<id>`. Therefore identity and storage are operationally coupled today.

A migration may rely on the stable manifest ID, but it may not assume arbitrary path independence that current owners do not implement.

### 5.3 Must identity survive a legitimate relocation?

**Yes, if a future canonical contract admits relocation.** A legitimate storage relocation must not mint a different Workspace ID merely because bytes moved.

**But current shipped architecture does not yet define a legitimate relocation away from `workspaces/<id>`.** Therefore Safe Infrastructure has no admitted Workspace-move operation to implement now.

### 5.4 How are moved Workspaces resolved today?

They are not. Current resolution reconstructs the canonical path from Workspace ID and expects the manifest there. An arbitrary/nested move makes current consumers fail or treat the expected Workspace as absent/misplaced.

A future relocation contract would need an owner-controlled ID-to-location resolver/registry or another explicit canonical mechanism before moves are permitted. Phase 1 does not invent that mechanism.

### 5.5 Proven references/consumers affected by a future Workspace path change

These are proven current edges that would require owner changes/reference repair or explicit proof of location independence before a move could be admitted:

1. **OS workspace owner discovery/creation**: scans direct children of `workspaces/` and creates `workspaces/<id>`.
2. **OS current context**: opens `workspaces/<id>/context/CURRENT.md` and enforces the expected physical slot.
3. **OS Workspace capability provider**: resolves `workspace:<id>` to `workspaces/<id>/skills/`.
4. **Data Workspace resolver/database**: resolves `workspaces/<id>/WORKSPACE.yaml` and `workspaces/<id>/data/ai-verse-data.sqlite`; ID/path mismatch fails closed.
5. **Memory native Workspace scopes**: enumerates direct Workspace children, normalizes to `workspace:<id>`, and stores Workspace memory under `workspaces/<id>/memory/atomic`.
6. **Brain direction ownership/handover**: reads/writes Workspace current context at `workspaces/<workspace-id>/context/CURRENT.md` for `workspace:<id>` scopes.
7. **Any generated or durable source reference that stores a relative Workspace path** must be repaired or regenerated if its owner declares it durable. The move cannot be considered complete merely because the manifest appears elsewhere.

Connection and automation records can be scoped by Workspace identity, but Slice 1.2 does not assume they are path-independent unless their owner contract proves it. Any future move recipe must publish its complete owner-declared reference graph.

## 6. Skill scope and identity inventory

### 6.1 Current provider identities

The shipped Capability Provider Contract v1 defines:

- `os:<name>` for OS capabilities;
- `aiverse-skills:<name>` for managed distributed capabilities;
- `local:<name>` for user-owned personal reusable capabilities;
- `workspace:<workspace-id>:<name>` for workspace-owned capabilities.

Provider identities are `os`, `aiverse-skills`, `local`, and `workspace:<workspace-id>`.

These exact shipped names are the Safe Infrastructure Phase 1 evidence baseline. The separate Identity Hardening plan must reconcile any different vocabulary before creating a System-wide identity contract.

### 6.2 Managed Skill package identity/lifecycle

Skills owns the managed provider's package `id`, package metadata/provenance, source pin, version/content digest, immutable `generation_id`, index publication and install/update/rollback/uninstall lifecycle.

For execution, identity binding is not just a path. The host binds the qualified capability ID to generation and content digest.

### 6.3 Does a scope change preserve identity?

**Frozen answer:** not by assumption.

Current provider-qualified identity includes provider/scope. Therefore moving a capability from `workspace:<workspace-id>:<name>` to `local:<name>` or `aiverse-skills:<name>` changes the canonical qualified capability identity under the shipped provider contract.

The underlying content/provenance may be migrated and linked, but Safe Infrastructure MUST NOT claim it is the same canonical qualified identity unless a later owner/System identity contract explicitly defines an identity-preserving scope transfer.

Consequences:

- a Workspace-local -> personal reusable promotion is currently a **migration to a different provider-qualified identity**;
- a personal -> managed distributed publication is a separate promotion/publication with provenance/privacy review and a **different provider-qualified identity**;
- moving a managed distributed package between immutable generations **does preserve its package/qualified ID** while generation/version/digest change separately;
- path movement within one managed immutable generation is not an identity decision by itself because the manifest package ID is canonical, but generation manifests/indexes/digests must remain coherent.

### 6.4 Who owns a cross-provider scope change?

OS owns the scope/provider placement decision and resolution semantics. The source/destination owners preserve their own state/integrity. Skills participates only where the managed distributed provider is a source or destination and only within its lifecycle authority.

No generic cross-provider re-scope engine is admitted yet.

## 7. Migration and identity guarantees infrastructure work may rely on

Safe Infrastructure migrations may rely on these current guarantees only:

1. Workspace canonical logical ID is `WORKSPACE.yaml:id`.
2. Current Workspace storage is `workspaces/<id>`; arbitrary relocation is unsupported.
3. Workspace scopes use `workspace:<id>` across current OS/Brain/Memory/Data integration.
4. Managed distributed Skill package IDs are stable across Skills immutable generations; version, generation and digest are separate bindings.
5. Provider-qualified Skill/capability ID includes provider/scope, so cross-provider transfer is identity-changing unless a later canonical contract says otherwise.
6. Display name is not sufficient evidence of identity.
7. Filesystem path alone must never be used to invent or rebind identity where an owner-controlled ID exists.
8. Any ambiguous/duplicate/conflicting evidence must fail closed.
9. Cross-owner references may only be repaired by the canonical owner or an admitted owner-defined migration contract.

Safe Infrastructure migrations may **not** rely on:

- arbitrary Workspace filesystem independence;
- domain-first Workspace nesting;
- name equality as identity equality;
- automatic identity preservation across Skill providers;
- path-based inference of Skill scope;
- free-form AI inference to rebind durable references.

## 8. Doctor/health inventory

Distribution already implements the desired one-command fan-out model:

- it iterates the locked release/profile components;
- verifies exact owner source first;
- invokes each owner's `doctor` adapter independently;
- records an individual result for each owner;
- continues through other safe owner checks after an owner error by recording that failure rather than turning it into a false aggregate PASS;
- optionally runs the OS composed-system doctor;
- aggregate `ok` is true only if all included checks pass.

Classification: `REUSE/EXTEND`. Phase 4 should add convergence/recovery findings and plain-English aggregation around this mechanism, not create duplicate owner health logic.

## 9. Recovery coverage inventory

### 9.1 Must be captured or otherwise durably represented

Current OS ownership evidence treats these as durable/user-owned and therefore they cannot be silently discarded by restore design:

- `operator/` user state: profile, context, memory, inbox, decisions;
- shared user `knowledge/`;
- real `workspaces/*` including manifests, context, decisions, memory, skills, automations, assets and outputs;
- user-owned `connections/registry.yaml` metadata;
- user-owned `agents/registry.yaml` and local agent data;
- user-owned automation definitions;
- `.aiverse/extensions/` local extension state;
- `.aiverse/direction/` durable direction ownership coordination;
- `.aiverse/os/` setup state where needed to reproduce the local installation;
- generated/private app data that is actually canonical user state rather than disposable output;
- unknown/custom files whose package ownership cannot be proven.

Large `workspaces/<id>/assets` and `outputs` are user-owned by current OS boundaries. They may be storage-expensive, but size alone does not make them disposable. The recovery implementation must either cover them or establish an explicit evidence-backed external/content-addressed coverage policy and report exclusions truthfully. It may not silently omit them.

### 9.2 Exactly reconstructible when proof exists

Candidate reconstructible material includes:

- Distribution-managed software component checkouts selected by immutable release-set commit SHAs and receipts;
- dependency trees backed by exact Distribution companion locks/digests;
- managed Skills package generations only where their exact source pins/manifest/digests plus durable source availability are sufficient to reproduce the generation exactly.

Reconstruction is allowed only when exact reproducibility is proven. If exact bytes cannot be guaranteed at restore time, the required bytes must instead be retained in recovery material.

### 9.3 Rebuildable/disposable

OS `runtime/` is explicitly derived/rebuildable and must not become recovery bloat. The same principle applies to proven caches, generated indexes, health reports, temporary files, dependency caches and other material whose owner contract states it is reproducible.

### 9.4 External/security-sensitive

- connection registries explicitly must not contain credentials, API keys, passwords, private keys, recovery codes or session tokens;
- external credential stores and secrets are outside recovery scope unless a later explicit secure mechanism proves capture/restore semantics;
- remote service state and already-executed external side effects are not rewound by local restore;
- `.env` and similar secret-bearing local environment material must not be blindly copied into recovery simply to claim completeness.

Restore preview must state these exclusions plainly.

## 10. Identity Hardening reconciliation handoff

The separate `docs/AI-VERSE-IDENTITY-HARDENING-IMPLEMENTATION-PLAN.md` must remain separate and should reconcile these Phase 1 facts before Safe Infrastructure Phase 2 continues:

1. confirm System-wide Workspace identity law around `WORKSPACE.yaml:id` while preserving current canonical slot `workspaces/<id>` unless separately amended;
2. define the minimum cross-owner reference envelope without creating a global registry;
3. decide whether any future Workspace relocation is actually required; if yes, explicitly define lookup/location semantics and migration compatibility before Safe Infrastructure may move Workspaces;
4. canonically state scope-transfer identity semantics for capabilities/Skills;
5. reconcile exact shipped capability vocabulary (`aiverse-skills:*`, `local:*`, `workspace:<id>:*`, `os:*`) with any System identity examples/aliases;
6. ensure provider-qualified identity, package ID, generation ID, version and content digest remain distinct concepts;
7. preserve owner authority: OS resolves provider scope, Skills owns managed provider lifecycle;
8. define durable reference behavior for identity-changing promotions rather than assuming path/scope moves preserve identity.

No Identity Hardening implementation is performed here.

## 11. Slice 1.2 acceptance closure

- Distribution shadow-domain logic prohibited/identified: **PASS**.
- Path-identity risks explicit: **PASS**.
- One-command doctor fan-out ownership explicit: **PASS**.
- Exact recovery coverage classes needed for truthful restore known: **PASS**.
- Recovery design does not assume blind copy of all bytes: **PASS**.
- No duplicate migration/backup/update framework planned where existing machinery can be extended: **PASS**.
- Ordinary user output can remain free of paths/generations/IDs while machine evidence remains available: **PASS**.

**Slice 1.2 can close.**
