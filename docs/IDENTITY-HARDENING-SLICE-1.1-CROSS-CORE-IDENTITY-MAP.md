# Identity Hardening Slice 1.1 - Cross-Core Identity Map

**Program:** `docs/AI-VERSE-IDENTITY-HARDENING-IMPLEMENTATION-PLAN.md`  
**Slice:** 1.1 - Refresh the cross-Core identity map  
**Date:** 2026-10-12  
**Nature:** audit/evidence only. No component identity implementation is changed by this slice.

## 1. Authority and evidence reuse

Authority order used by this audit:

1. verified current source, shipped contracts and tests;
2. canonical component ownership;
3. approved System contracts;
4. roadmap assumptions.

Safe Infrastructure Phase 1 had already audited OS, Brain, Memory, Data, Skills and Distribution identity-sensitive infrastructure. Their heads remained unchanged at Identity Slice 1.1 start, so the following completed evidence is reused instead of repeated:

- `docs/SAFE-INFRASTRUCTURE-SLICE-1.2-INVENTORY.md`
- `docs/SAFE-INFRASTRUCTURE-SLICE-1.3-ARCHITECTURE-FREEZE.md`
- `docs/SAFE-INFRASTRUCTURE-UPGRADE-AND-RECOVERY-IMPLEMENTATION-PLAN.md`, Phase 1 final decisions

Focused Identity-only reads were added where Safe Infrastructure had not needed to prove the durable entity ID itself, for example Brain objects, Memory records and Data records.

## 2. Exact refs inspected

Identity Slice 1.1 refreshed these repository heads before relying on evidence:

- `aiverse-filmmakers/AI-Verse-System@423e04917a9f1a9b4f012fa9daf4366fc8135e8c` at slice start; concurrent repository-governance work later advanced System without touching this Identity plan or the frozen owner conclusions
- `aiverse-filmmakers/AI-Verse-OS@64f7325444d18f94c9d4755d32eb89f3468bda6b`
- `aiverse-filmmakers/AI-Verse-Brain@69f7912eeb35f0178f6952ff0554aec8d7f2c496`
- `aiverse-filmmakers/AI-Verse-Memory@f1327be48ba2ee0043959021365e6dbb9dcb1d3a`
- `aiverse-filmmakers/AI-Verse-Data@f8978f8f7a1bc94edecddc2662112233289159a3`
- `aiverse-filmmakers/AI-Verse-Skills@afde5c06307fba7d074de2929c2eb6c3dc6bdab8`
- `aiverse-filmmakers/AI-Verse-Automations@287ce9d6718ef06e4589a2a3e767c6a9ba376755`
- `aiverse-filmmakers/AI-Verse-Multiple-Bots@ddf70ac19736f6ca7f8d604901c20af9e46614fe`
- `aiverse-filmmakers/AI-Verse-Connections@602a1c52ab782cc9a8b7a4caa60ccb29efe403d1`
- `aiverse-filmmakers/AI-Verse-Apps@db5b0115bf59d6eae9149137a40e891968f3a637`
- `aiverse-filmmakers/AI-Verse-Gateway@1772b75e2add73a524715f746e87b3a6b5561bf6`
- `aiverse-filmmakers/AI-Verse-Dashboard@bd26986e202d4b911d0c5f64659db71363bfccfa`
- `aiverse-filmmakers/ai-verse-token@d36916323abb5f396bd8fd6b7f5c3ef84af519d0`
- `aiverse-filmmakers/ai-verse-distribution@fd11b4a95487638d47ff55472a3703b03892d0e8`

System advanced concurrently after the slice-start record through repository-network-governance work. The inspected concurrent commits did not alter the Identity plan or owner identity contracts. The Identity audit therefore keeps the exact owner refs above while refetching System before each write.

## 3. Classification vocabulary

- `REUSE`: owner identity already satisfies the shared direction; do not redesign it.
- `EXTEND`: existing mechanism is sound but needs a bounded shared-contract/preservation integration.
- `CREATE`: a required durable identity mechanism is materially absent.
- `RETIRE`: an existing duplicate/unsafe identity mechanism should be removed after proof.
- `BLOCK/UNKNOWN`: current evidence does not admit the capability or continuity claim; fail closed rather than inventing semantics.

## 4. Final cross-Core identity matrix

| Identity surface | Canonical owner | Classification | Evidence-backed conclusion |
| --- | --- | --- | --- |
| Workspace logical identity | AI-Verse-OS | `REUSE` | `WORKSPACE.yaml:id` is required independently from `name`. |
| Workspace current physical storage | AI-Verse-OS, consumed by OS/Data/Brain/Memory | `REUSE` | Current canonical slot remains `workspaces/<workspace-id>`; storage is ID-derived and operationally coupled today. |
| Arbitrary Workspace relocation / ID-to-location lookup | AI-Verse-OS plus future System contract only if admitted | `BLOCK/UNKNOWN` | No current owner contract resolves the same Workspace ID at arbitrary/nested paths. Relocation is unsupported, not guessed. |
| OS current-context canonical reference precedent | AI-Verse-OS | `EXTEND` | Existing output already uses `{owner, scope, kind, id}`; Slice 1.2 may standardize the minimum common envelope without replacing OS identity. |
| Capability provider scope/resolution/ranking | AI-Verse-OS | `REUSE` | OS owns provider scope, ranking, resolution and authorized roots. |
| Managed `aiverse-skills` package identity/lifecycle | AI-Verse-Skills | `REUSE` | Skills owns package IDs/metadata/provenance, immutable generations and lifecycle. Package identity is separate from generation/version/digest. |
| Personal reusable capability provider | User, resolved by OS | `REUSE` | User-owned `local:<name>` provider; outside Skills distribution ownership. |
| Workspace-local capability provider | Workspace owner, resolved by OS | `REUSE` | Workspace-owned `workspace:<workspace-id>:<name>` provider. |
| Cross-provider capability/Skill identity-preserving re-scope | OS placement semantics plus source/destination owners | `BLOCK/UNKNOWN` | Provider/scope is part of current qualified identity. Scope transfer must not be treated as identity-preserving unless a future owner/System contract explicitly supports and tests it. |
| Brain durable objects/goals | AI-Verse-Brain | `REUSE` | `BrainObject.id` is durable UUID identity; `kind`, `scope`, payload and `revision` remain separate. |
| Memory records | AI-Verse-Memory | `REUSE` | Atomic memories carry durable `mem-*` IDs; scope/path/provenance are separate metadata/storage concerns. |
| Data records | AI-Verse-Data | `REUSE` | Records have owner-generated `rec_*` IDs; record identity is distinct from `schemaVersion`, record `version`, request IDs and transaction IDs. |
| Data spaces/entities | AI-Verse-Data | `REUSE` | Data already distinguishes `DataSpaceId`, `EntityId`, `RecordId`, request/event/transaction/receipt IDs. |
| Automation definitions/triggers/runs/invocations | AI-Verse-Automations | `REUSE` | Automation/trigger/run IDs are durable store keys; invocation identity is immutable and occurrence identity is deterministic for retry/deduplication. |
| Multiple Bots first-class entities | AI-Verse-Multiple-Bots | `REUSE` | Typed UUID IDs are distinct from names/handles; collisions fail closed and archived addresses remain reserved. |
| Connections | AI-Verse-Connections | `REUSE` | Explicit validated connection IDs are registry keys, system-bound and duplicate-safe; provider metadata is separate. |
| Gateway sessions/runs | AI-Verse-Gateway | `REUSE` | Gateway owns local session/run IDs while binding to external `system_id`, `workspace_id` and domain-owner references. It is not a global identity authority. |
| Dashboard registered-system connection identity | AI-Verse-Dashboard | `REUSE` | Dashboard `systemId` is explicitly local registry identity for an approved OS root and owns zero domain truth; root-identity drift fails closed. |
| Token model/provider identity resolution | ai-verse-token | `REUSE` | Runtime, billing platform, provider, requested model, resolved model/version and provider-native model ID remain distinct; conflicts resolve to `ambiguous`, not guessed rebinding. |
| App durable identity | AI-Verse-Apps | `CREATE` | Stable App identity is required by intended architecture but executable App registry/manifest/identity lifecycle is not implemented yet. |
| System-wide cross-owner durable-reference contract | AI-Verse-System | `EXTEND` | Strong owner patterns exist, especially OS `{owner, scope, kind, id}`, but no single canonical System contract yet standardizes the minimum common envelope. |
| Distribution identity preservation across Core update | ai-verse-distribution | `EXTEND` | Existing update preservation machinery is mature; later Identity Slice 3.2 should add explicit durable-ID/reference before/after proof, not a second updater. |
| Repository-network governance repository IDs | AI-Verse-System governance | `REUSE` | GitHub repository IDs are stable for repository governance only. They are not an AI-Verse runtime/global entity registry. |

### No `RETIRE` item

Slice 1.1 found no competing global durable-identity service, duplicate runtime identity registry or owner identity implementation that should be retired. Creating one merely for uniformity would violate the anti-bloat boundary.

### Installation-wide AI-Verse instance ID

No canonical installation-wide AI-Verse instance ID is required by current evidence. It remains out of scope rather than being created for symmetry. Dashboard `systemId` and Gateway `system_id` must not be promoted into such a role without separate evidence and an explicit architecture decision.

## 5. Confirmed Workspace conclusions

1. Workspace logical identity is `WORKSPACE.yaml:id`.
2. Workspace `id` and `name` are separate required manifest properties.
3. Current storage remains `workspaces/<workspace-id>`.
4. Filesystem independence is not universal. Current OS/Data/Brain/Memory consumers intentionally derive the storage slot from Workspace ID.
5. A Workspace moved away from that slot does not currently resolve as the same supported Workspace.
6. Workspace relocation therefore remains unsupported unless a future explicit owner/System contract adds an ID-to-location resolution mechanism.
7. If such relocation is ever admitted, the existing Workspace ID must survive and owner-declared references must be repaired before the old writable route retires.

No Workspace relocation capability is introduced by Identity Hardening Slice 1.1.

## 6. Confirmed Skill/capability conclusions

Shipped qualified identities remain:

- `os:<name>`
- `aiverse-skills:<name>`
- `local:<name>`
- `workspace:<workspace-id>:<name>`

Frozen ownership remains:

- OS owns provider scope/resolution/ranking and authorized placement semantics;
- Skills owns the managed `aiverse-skills` provider lifecycle;
- personal reusable capabilities are user-owned;
- Workspace-local capabilities are Workspace-owned.

Package version and content digest are explicitly separate from qualified ID. Managed Skills generation identity is also a separate lifecycle binding. Thus a managed package can retain its package/qualified ID across generation changes while generation/version/digest change.

Because provider identity is a prefix of the current qualified capability ID, moving between Workspace, local and managed distributed providers changes the current qualified identity. Identity Hardening must not universalize identity continuity across a re-scope operation.

## 7. Mature owner identity implementations to preserve

### Brain

`engine/aiverse_brain/models.py` defines `BrainObject.id` independently from `kind`, `scope`, payload and revision. New objects receive UUIDv4 IDs; persisted objects restore their existing ID. Classification: `REUSE`.

### Memory

`scripts/memory_engine.py` stores `id` as record metadata and generates `mem-*` IDs. Storage path is derived from scope, timestamp and memory ID rather than being treated as the identity itself. Classification: `REUSE`.

### Data

`src/protocol/types.ts` distinguishes `DataSpaceId`, `EntityId`, `RecordId`, `RequestId`, `EventId`, `TransactionId` and `ReceiptId`. `src/records/engine.ts` allocates unique `rec_*` record IDs and keeps schema/version separately. Purpose/current-value references use Data owner + space + entity + record ID rather than copying canonical rows. Classification: `REUSE`.

### Automations

`docs/ARCHITECTURE.md` and `src/aiverse_automations/db.py` distinguish automation, trigger, run and invocation identities. Store schemas key durable entities explicitly, and invocation/occurrence IDs provide retry/idempotency continuity. Classification: `REUSE`.

### Multiple Bots

`src/id.ts`, `src/types.ts` and bot registry tests show typed owner IDs separate from human names/handles. Duplicate/colliding durable addresses fail safely. Classification: `REUSE`.

### Connections

`src/service-registry.js` validates explicit connection IDs, keys registry entries by them and refuses duplicate creation. Connection identity remains separate from provider/capability metadata. Classification: `REUSE`.

### Gateway

`src/store.mjs` and `docs/ARCHITECTURE.md` maintain Gateway-local session/run identities while preserving explicit bindings to external system/workspace/domain references. Gateway does not become the owner of Brain, Workspace or System identity. Classification: `REUSE`.

### Dashboard

`packages/registry/src/registry.ts` explicitly states the local registry owns zero domain truth. `packages/registry/src/root-identity.ts` uses filesystem identity only to prove an already-registered Dashboard connection still points to the same OS root. Dashboard `systemId` stays local. Classification: `REUSE`.

### Token

`docs/IDENTITY-RESOLUTION-V0.1.md` intentionally separates runtime/provider/model/billing identities and fails closed on conflicting exact rules by returning `ambiguous`. Classification: `REUSE`.

## 8. Apps gap

Apps remains the only known required durable-identity implementation gap in this map.

Evidence at `AI-Verse-Apps@db5b0115...`:

- repository README says implementation status is `Not started`;
- App manifest/registry identity is described as intended architecture rather than shipped implementation;
- the schema is not frozen.

System `components/ai-verse-apps/COMPONENT-SPEC.md` likewise records the intended platform boundary but no executable App registry/manifest/stable-identity lifecycle.

Classification: `CREATE` using the existing Apps architecture, not a generic System registry.

## 9. System shared-contract gap

No current System document/schema is the canonical shared durable-entity identity/reference contract across all owners.

There are useful precedents, especially OS current-context output:

```json
{
  "owner": "ai-verse-os",
  "scope": "workspace:example",
  "kind": "current-context",
  "id": "active"
}
```

Slice 1.2 should standardize only the smallest common cross-owner envelope and laws. It must not become a central identity store, translate every owner ID into one global format, or force internal owner rewrites.

Classification: `EXTEND` existing owner reference patterns into canonical System law.

## 10. Duplicate/competing mechanism review

No competing identity owner was found that conflicts with the intended shared contract:

- System repository governance IDs belong to repository governance, not runtime entities;
- Dashboard `systemId` is a local connection key, not an installation identity;
- Gateway session/run IDs belong to Gateway client-edge lifecycle;
- Data request/transaction/receipt IDs are not Data record IDs;
- Skills generation/version/digest are not package identity;
- Token provider/model resolution identities are domain-specific and must remain distinct;
- execution/correlation/idempotency IDs are not silently promoted into durable entity identity.

Therefore:

- no global identity registry is justified;
- no universal UUID format is justified;
- no existing mature owner ID implementation should be redesigned for stylistic consistency;
- no `RETIRE` action is justified by Slice 1.1.

## 11. Slice 1.2 handoff

The minimum shared contract can now be defined without architectural guessing. It must encode these frozen facts:

1. durable long-lived/cross-owner entities use stable owner-controlled IDs;
2. identity is distinct from display name, path, revision and temporary execution IDs;
3. owners retain ID formats and lifecycle semantics;
4. no global identity service/registry;
5. filesystem independence is owner-defined, not universal;
6. current Workspace storage stays `workspaces/<id>`;
7. arbitrary Workspace relocation is unsupported unless a later explicit contract adds location resolution;
8. current provider-qualified capability identity retains provider/scope semantics;
9. scope transfer is owner-defined and not automatically identity-preserving;
10. package identity, qualified identity, generation, version and digest remain distinct;
11. ambiguity/duplicates/conflicts fail closed;
12. common durable references use the smallest envelope needed, with `scope` present only when required for correct owner resolution;
13. update/upgrade/restore may rely only on guarantees the canonical owner actually publishes.

## 12. Acceptance closure

- every durable first-class identity surface required by Slice 1.1 is accounted for: **PASS**;
- every canonical owner is identified: **PASS**;
- duplicate/competing identity mechanisms are identified: **PASS - none require retirement**;
- path/name couplings are recorded only where real current architecture proves them: **PASS**;
- mature owner implementations are classified `REUSE`: **PASS**;
- Apps remains the single known `CREATE` implementation gap: **PASS**;
- unsupported Workspace relocation and cross-provider identity continuity fail closed as `BLOCK/UNKNOWN`: **PASS**;
- no product/component implementation change occurred in Slice 1.1: **PASS**.
