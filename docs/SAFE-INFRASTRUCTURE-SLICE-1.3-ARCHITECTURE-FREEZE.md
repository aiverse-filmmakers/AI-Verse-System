# Safe Infrastructure Slice 1.3 Architecture and Acceptance Freeze

**Program:** `docs/SAFE-INFRASTRUCTURE-UPGRADE-AND-RECOVERY-IMPLEMENTATION-PLAN.md`  
**Slice:** 1.3 - Freeze implementation architecture and acceptance matrix  
**Date:** 2026-10-12  
**Input evidence:** Slice 1.1 audit plus `docs/SAFE-INFRASTRUCTURE-SLICE-1.2-INVENTORY.md`  
**Nature:** architecture freeze only. Phase 2 implementation is intentionally not started.

## 1. Starting refs

Slice 1.3 consumes the Slice 1.2 evidence set and current System planning state. No owner implementation is changed by this slice.

Primary evidence refs:

- System starting ref for Phase 1 continuation: `11940b87838afa0f46570ecdd8f8e00f74b7de5a`
- Distribution: `fd11b4a95487638d47ff55472a3703b03892d0e8`
- OS: `64f7325444d18f94c9d4755d32eb89f3468bda6b`
- Skills: `afde5c06307fba7d074de2929c2eb6c3dc6bdab8`
- Brain: `69f7912eeb35f0178f6952ff0554aec8d7f2c496`
- Memory: `f1327be48ba2ee0043959021365e6dbb9dcb1d3a`
- Data: `f8978f8f7a1bc94edecddc2662112233289159a3`
- Slice 1.2 evidence commit: `d9920be2727a550266086b84b73aafbc397c07de`

## 2. Derived task list

- [x] **1.3-T1** Freeze update versus upgrade activation semantics without changing shipped `aiverse update` behavior.
- [x] **1.3-T2** Freeze owner boundaries for Workspace structure, Skill provider scope, managed Skills lifecycle and Distribution orchestration.
- [x] **1.3-T3** Freeze Workspace and Skill identity assumptions that infrastructure migrations may and may not rely on.
- [x] **1.3-T4** Freeze owner doctor fan-out, failure aggregation and read-only preview contracts.
- [x] **1.3-T5** Freeze Last-Known-Good ownership, private location class, coverage classes, exclusions, rotation and restore transaction invariants.
- [x] **1.3-T6** Freeze plain-English UX and cross-runtime lifecycle routing requirements.
- [x] **1.3-T7** Freeze Phase 2/3 dependency gates and the handoff to the separate Identity Hardening plan.

## 3. Final ownership decisions

### 3.1 System

System owns cross-repository laws and acceptance contracts only. It does not become a migration engine, Workspace registry, Skill registry, backup engine or global identity store.

### 3.2 Distribution

Distribution remains the sole member-facing lifecycle orchestrator for:

- released software update selection/application;
- one-command doctor aggregation;
- structural upgrade preview/orchestration;
- Last-Known-Good coordination;
- restore preview/apply;
- activation gating and whole-install verification.

Distribution may consume owner identity and migration contracts but may not invent Workspace hierarchy or Skill scope semantics.

### 3.3 OS

OS owns:

- Workspace schema/creation/storage semantics;
- Workspace logical identity interpretation;
- OS-owned Workspace references;
- capability provider scope, ranking and resolution;
- cross-provider placement semantics for workspace/local/distributed/OS capabilities;
- contextual execution permission and routing.

### 3.4 Skills

Skills owns the managed `aiverse-skills` provider:

- package identity and package metadata;
- source pins and provenance;
- profiles;
- immutable generations;
- install/update/rollback/uninstall;
- package integrity verification;
- provider manifest/index publication;
- migrations wholly internal to that managed provider.

Skills does not own OS provider ordering or the placement of user/workspace capabilities into other providers.

### 3.5 Other owners

Brain, Memory and Data continue owning their canonical state and identity semantics. Any future Workspace storage migration must coordinate with those owners because current implementations bind Workspace scope to the canonical OS storage slot.

## 4. Final Workspace identity/storage decision

### 4.1 Logical identity

`WORKSPACE.yaml:id` is the current canonical Workspace logical identity.

### 4.2 Storage path

The current canonical storage rule is `workspaces/<workspace-id>`.

The path is not a second independent logical identity, but it is intentionally derived from and coupled to the ID by current shipped owners. Filesystem independence is therefore **not** an available migration guarantee today.

### 4.3 Relocation

Safe Infrastructure Phase 1 does **not** admit a Workspace relocation away from `workspaces/<id>`.

The earlier roadmap example `workspaces/YouTube/<ChannelName>/` is retired as an assumed physical target. A future canonical amendment may introduce relocatable Workspace storage only after the Identity Hardening/System contract defines how stable Workspace ID resolves to a changed physical location and all affected owners have compatible migration paths.

### 4.4 Identity continuity rule

If future architecture deliberately admits relocation, the existing Workspace ID must survive the move. A storage move may not mint a new Workspace merely because its filesystem address changes.

Until such a contract exists, the safe operation is **no physical move**.

### 4.5 Reference-repair floor for any future move

Any future admitted move must repair or prove unaffected at least:

- OS Workspace discovery/creation;
- OS current-context resolution;
- OS Workspace capability provider roots;
- Data Workspace manifest/database resolution;
- Memory Workspace scope discovery and canonical Workspace memory storage;
- Brain Workspace direction/current-context reads and writes;
- every owner-declared durable relative-path/source reference into the Workspace;
- any scoped connection/automation/reference whose owner proves path dependence.

A move cannot be considered successful while any supported owner still resolves only the old slot.

## 5. Final Skill scope/identity decision

### 5.1 Shipped qualified identities

The current contract names:

- `os:<name>`;
- `aiverse-skills:<name>`;
- `local:<name>`;
- `workspace:<workspace-id>:<name>`.

These are the Phase 1 source-of-truth forms. Display name and filesystem path are not substitutes for qualified identity.

### 5.2 Managed package continuity

Within the `aiverse-skills` provider, package ID/qualified ID remains stable across immutable generation changes. Generation ID, version and content digest are separate bindings and may change without changing package identity.

### 5.3 Cross-provider scope transfer

Under the current shipped provider contract, provider/scope participates in qualified identity. Therefore:

- Workspace-local -> personal/local promotion changes qualified identity;
- personal/local -> distributed publication changes qualified identity;
- Workspace A -> Workspace B changes qualified identity because Workspace ID is embedded in the provider-qualified ID.

Content provenance/history can and should link source and destination, but identity preservation across those scope transfers is **not** assumed.

Any future identity-preserving scope-transfer model requires an explicit System/owner contract from Identity Hardening before Safe Infrastructure implements it.

### 5.4 Scope decision ownership

OS owns the decision about which provider/scope is authorized and appropriate. Skills owns lifecycle only when the managed distributed provider is involved.

## 6. Update and structural-upgrade architecture freeze

### `aiverse update`

- remains the already-shipped mutating safe software update;
- selects the newest admitted Core release through Distribution;
- preserves owner/user state and fails closed on unsafe local ambiguity;
- may not silently perform OPTIONAL structural convergence;
- before future mutating execution, Phase 4 must secure the retained Last-Known-Good point defined below.

### `aiverse update --plan`

- remains read-only;
- may report REQUIRED structural prerequisites but does not apply them.

### `aiverse upgrade`

- is the read-only structural convergence preview;
- consumes owner-published findings/recipes;
- reports OPTIONAL / REQUIRED / REVIEW-BLOCKED in plain English;
- cannot invent a migration from AI reasoning.

### `aiverse upgrade --apply`

- may execute only admitted owner-controlled recipes;
- requires the Last-Known-Good precondition;
- revalidates source state/fingerprint immediately before apply;
- verifies reference repair/postconditions after apply;
- cannot run Workspace relocation or cross-provider Skill re-scope work until the relevant identity owner contract exists.

## 7. One-command doctor freeze

Reuse the existing Distribution doctor fan-out.

Frozen behavior:

1. operate against the locked admitted release/profile;
2. verify exact owner source/runtime binding before trusting its check;
3. invoke each relevant owner doctor in deterministic release/dependency order;
4. isolate each result;
5. continue remaining safe read-only checks when one owner fails unless dependency evidence makes continuation invalid;
6. run the OS composed-system doctor after owner checks when available;
7. aggregate to PASS only if every required included check passes;
8. never duplicate the owner's domain-specific diagnosis logic inside Distribution.

`doctor`, `update --plan`, `upgrade`, and `restore` preview are read-only.

## 8. Last-Known-Good and restore architecture freeze

### 8.1 Owner and location class

Distribution owns the whole-install recovery transaction and metadata.

Recovery material must live in **Distribution-owned private state outside the live OS project tree**, rooted under the existing private Distribution state home (`StateStore.home`, default `~/.aiverse/distribution`). Phase 4 may choose exact subdirectory names, but it must not place the retained recovery point inside a canonical live owner store or a Workspace.

### 8.2 Recovery representation

The retained Last-Known-Good point is a verified manifest-backed recoverable representation, not necessarily a byte-for-byte duplicate of every directory.

It must contain or durably bind:

- exact Distribution release set and component receipts/revisions;
- exact owner/software reconstruction evidence where reconstruction is used;
- captured canonical/user-created local state required for restore;
- file/integrity inventory sufficient to verify the recovery point;
- explicit coverage and exclusion metadata;
- creation time and source-state fingerprint/evidence.

### 8.3 Coverage classes

Every local surface must resolve to one of four classes before recovery rotation:

1. **CAPTURE**: canonical/user state that must be retained because it is not safely reconstructible.
2. **RECONSTRUCT**: exact software/material reproducible from immutable verified refs/receipts and durable source evidence.
3. **REBUILD**: disposable derived state explicitly declared rebuildable by its owner.
4. **EXTERNAL/EXCLUDED**: external/security-sensitive state not truthfully rewindable by local restore.

Unknown ownership defaults toward preservation/review, never disposal.

### 8.4 Large assets and outputs

Current Workspace boundaries make `assets/` and `outputs/` user-owned. They cannot be silently classified REBUILD merely due to size.

Phase 4 must use an evidence-backed storage strategy such as deduplication/content-addressing/filesystem snapshot semantics or an explicit externally-backed representation. If any such surface is excluded, restore preview must say so and must not claim full local recovery for it.

### 8.5 Secrets and credentials

Credentials, API keys, passwords, private keys, recovery codes, session tokens and external credential stores are excluded from blind capture. Current OS connection registry explicitly must not contain these secrets.

A later implementation may include a security-sensitive surface only if it has an explicit secure capture/restore contract. Remote side effects remain outside local restore.

### 8.6 Rotation

Before update or upgrade mutation:

1. assess whether the current installation is sufficiently healthy/unambiguous to become the next recovery point;
2. stage a candidate recovery representation without changing the retained Last-Known-Good;
3. verify candidate completeness/integrity and reconstruction bindings;
4. atomically promote the verified candidate;
5. only after promotion may the superseded retained recovery point be deleted;
6. retain exactly one usable Last-Known-Good point after successful rotation.

A failed candidate creation cannot destroy the prior known-good point.

### 8.7 Restore

`aiverse restore` is preview-only and reports:

- retained point time;
- broad covered categories;
- explicit exclusions;
- whether newer covered local changes will be replaced;
- whether the recovery point is currently verifiable/applicable.

`aiverse restore --apply`:

- takes a temporary transaction checkpoint of the current covered state sufficient to avoid a partial failed restore;
- never replaces/deletes the retained restore target before success;
- restores captured state and reconstructs exact admitted software as declared;
- verifies owner/System health and recovery-point identity after restore;
- reports external effects it cannot rewind.

## 9. Structural finding semantics

Every owner finding is one of:

- `OPTIONAL`: supported current state, recommended improvement;
- `REQUIRED`: target release cannot safely activate/remain supported without owner migration;
- `BLOCKED/REVIEW`: automatic safety cannot be proved or user/custom ambiguity exists.

An OPTIONAL finding is never hidden inside `update`. A REQUIRED finding may gate activation but must remain explicit. A BLOCKED/REVIEW finding preserves state and requests a practical decision rather than an internal path/generation choice.

## 10. Cross-runtime lifecycle freeze

Supported Claude/Codex/Gateway-compatible adapters must converge on the same canonical member intents:

- update -> `aiverse update`;
- check/health -> `aiverse doctor`;
- setup improvements -> `aiverse upgrade` preview;
- explicit confirmed structural mutation -> `aiverse upgrade --apply`;
- restore impact -> `aiverse restore` preview;
- explicit confirmed restore -> `aiverse restore --apply`.

Runtime adapters may phrase confirmations naturally but cannot invent different lifecycle semantics.

## 11. Member UX freeze

Default output must remain short and practical. Technical IDs, paths, generation IDs, hashes and recipe IDs belong in details/JSON unless needed to explain a conflict that has no friendlier identifier.

The user-facing promises are about:

- healthy/not healthy;
- safe improvements available;
- required setup change;
- item needing review;
- what will be preserved/replaced;
- whether recovery is ready.

## 12. Phase 2/3 dependency gates

The following work is explicitly blocked at the Phase 1 pause point:

- Workspace filesystem relocation implementation;
- Workspace reference-repair implementation for a relocation;
- cross-provider Skill re-scoping/promotion implementation that assumes identity continuity;
- any generic identity migration engine;
- Safe Infrastructure Phase 2 contract implementation.

Before those paths continue, the separate Identity Hardening Phase 1 must refresh current identity reality and define the System-wide identity/reference contract.

This does not merge the roadmaps. Safe Infrastructure consumes the later canonical identity contract as a dependency.

## 13. Acceptance matrix

| Invariant | Frozen proof/owner |
| --- | --- |
| Shipped update semantics preserved | Distribution Core updater/CLI, Slice 1.1 evidence |
| Update preview/read-only lifecycle previews | Distribution + future extension, no new updater |
| One doctor command | Existing Distribution doctor fan-out |
| Owner logic not shadowed | Owner doctor adapters; Distribution aggregation only |
| Workspace ID | OS `WORKSPACE.yaml:id` |
| Workspace current physical slot | OS/Data/Brain/Memory `workspaces/<id>` consumers |
| Workspace arbitrary relocation | NOT ADMITTED until later canonical amendment |
| Workspace future move identity continuity | must preserve `WORKSPACE.yaml:id` if relocation is ever admitted |
| Skill provider scope owner | OS |
| Managed Skill package lifecycle owner | Skills |
| Managed Skill identity across generation | preserved package/qualified ID; generation/digest separate |
| Cross-provider Skill scope transfer identity | identity-changing under current contract unless later amended |
| Structural recipes | canonical owner publishes, Distribution coordinates |
| Last-Known-Good owner | Distribution |
| Recovery live-source duplication | prohibited; recovery material non-canonical |
| Runtime cache/index recovery | rebuild instead of blind copy when owner proves derivation |
| Workspace assets/outputs | preserve or truthfully declare evidence-backed external coverage; never silently discard |
| Credentials/secrets | excluded unless explicit secure restore contract exists |
| Failed recovery rotation | cannot destroy existing Last-Known-Good |
| Failed restore | cannot destroy retained restore target |
| External effects | never falsely claimed restored |
| Member output | plain English, technical evidence opt-in |

## 14. Identity Hardening handoff

Before Safe Infrastructure Phase 2 continues, the separate Identity Hardening Phase 1 should turn these observations into canonical shared law:

- Workspace stable ID versus current ID-derived storage slot;
- minimum cross-owner durable-reference envelope;
- whether any future Workspace relocation is needed and, if so, canonical ID-to-location lookup semantics;
- exact scope-transfer identity semantics;
- exact provider-qualified capability vocabulary and compatibility aliases, if any;
- distinction between Skill package ID, provider-qualified ID, generation ID, version and digest;
- fail-closed duplicate/conflicting identity rules;
- identity preservation requirements for update/restore evidence.

Safe Infrastructure must then consume that law, not pre-empt it.

## 15. Slice 1.3 acceptance closure

- every new mechanism has one canonical owner: **PASS**;
- unresolved source-of-truth duplication removed from the architecture freeze: **PASS**;
- shipped Core Update v1 behavior preserved: **PASS**;
- recovery promise is truthful and storage-bounded by explicit coverage classes: **PASS**;
- one-command doctor remains aggregation rather than shadow owner logic: **PASS**;
- member experience requires no architecture knowledge: **PASS**;
- Phase 2 can proceed later without architecture guessing, after Identity Hardening Phase 1 supplies the shared identity contract: **PASS**.

**Slice 1.3 can close. Phase 1 is complete. STOP before Phase 2.**
