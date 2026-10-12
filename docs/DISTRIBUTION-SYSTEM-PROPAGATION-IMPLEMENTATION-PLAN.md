# AI-Verse Repository Network Governance, Release Safety and Self-Checking Implementation Plan

**Status:** ACTIVE  
**Canonical planning repo:** `aiverse-filmmakers/AI-Verse-System`  
**Primary implementation repo:** `aiverse-filmmakers/ai-verse-distribution`  
**Affected repos:** AI-Verse-System, ai-verse-distribution, all releasable AI-Verse component repositories  
**Started:** 2026-10-12  
**Program size:** 20 slices  
**Completed:** 5  
**Remaining:** 15  
**Overall progress:** 25.0%  
**Current execution phase:** Phase 2 - Define the canonical System control plane  
**Current phase progress:** 1/3 slices complete  
**Slices until next phase:** 2  
**Current slice:** 2.1 - Create the repository-network governance, invariant and tombstone contract  
**Current slice status:** COMPLETE  
**Task progress:** 5/5  
**Next slice:** 2.2 - Create the machine-readable Repository Registry  
**Next slice task list:** NOT YET DERIVED - generate from live evidence when Slice 2.2 starts

> This file is the execution tracker. It must update before and after every implementation slice. A slice is not COMPLETE until implementation, tests/evidence, tracker update and progress accounting are committed.

## Tracker history preservation

The detailed Phase 0/1 execution history that previously lived inline in this file is durably preserved in Git at Slice 1.3 closure commit:

`acabfba8031421438747fed69bcbc65ba844787e`

That commit is the immutable archive for the verbose Slice 0.1, 1.1, 1.2 and 1.3 start/completion records. Their canonical evidence documents and commit refs remain summarized below. Tracker compaction changes presentation only, not program laws, ownership, slice outcomes, acceptance criteria, ordering, denominator or evidence requirements.

---

# 0. Program mission

Make the AI-Verse repository network behave as one controlled, self-checking product without collapsing the repositories into one codebase.

The finished system must satisfy all of the following:

1. System stays current with meaningful architecture, ownership, lifecycle and readiness truth.
2. Canonical component owners remain canonical implementation authorities.
3. Distribution ships only exact owner-accepted compositions that pass whole-product qualification.
4. Live HEAD, owner-accepted revision, Distribution-shipped revision and System-synchronized truth remain distinguishable.
5. Stale documentation cannot regress newer accepted implementation, and newer unvalidated code cannot rewrite System intent automatically.
6. Existing safe-update and user-state preservation floors are never weakened.
7. Maintainer governance remains outside member installs.
8. Every admitted release is reconstructable from durable immutable evidence.
9. Repository drift and watchdog decay become visible failures rather than silent drift.
10. Execution adapts at task/implementation level from evidence.
11. Adaptive discovery cannot silently change product intent, canonical ownership, permanent laws, slice outcomes, acceptance floors, rollout order or denominator.

Central rule:

> **Define centrally. Enforce at the canonical owner. Verify again at composition.**

Execution rule:

> **Fix the destination. Discover the safest route from current reality.**

Adaptive-authority rule:

> **Discovery may adapt the route. It may not silently change the destination.**

Reusable planning method: `docs/ADAPTIVE-IMPLEMENTATION-PLANNING-SKILL.md`.

---

# 1. Canonical roles

## AI-Verse-System

Owns architecture/product intent, component responsibility/ownership, system invariants, cross-repo governance contracts, Repository Registry, Repository State model, generated human ledger, architecture tombstones/history, shared release/compatibility semantics, current-versus-intended truth, changelog and readiness/QC truth.

System is not a second implementation home and is not the member installer.

## Component repositories

Each component repo owns its implementation, local tests/CI/acceptance, interfaces/contracts/schemas, local migrations/recovery, component release descriptor/evidence and implementation provenance.

A component repo does not decide by itself that a revision ships to members.

## ai-verse-distribution

Owns exact release sets, immutable refs, composition compatibility, candidate admission, source acquisition, install/setup/update/rollback orchestration, member payload boundary, whole-product qualification, promotion/channels, release receipts/reconstructability and Distribution-specific recovery evidence.

Distribution does not own sibling component domain logic or canonical user state.

## Member installation

Receives only admitted runtime/product artifacts plus legitimate generated member-facing files. Internal repository-network governance remains source-only unless narrowly required runtime metadata is explicitly admitted.

---

# 2. Existing contracts to reuse, not duplicate

The program must reuse and extend existing canonical contracts where they already own the concern:

- `docs/SAFE-UPDATE-AND-STATE-PRESERVATION-CONTRACT.md`
- `docs/COMPONENT-RELEASE-DESCRIPTOR-CONTRACT.md`
- `docs/WHOLE-RELEASE-PRESERVATION-RESULT-CONTRACT.md`
- `docs/LIVING-SPEC-PROTOCOL.md`
- `docs/OWNER-PRODUCT-INTENT.md`
- `docs/FINAL-AI-VERSE-BLUEPRINT.md`

Consequences:

- no second safe-update system;
- no second component release/compatibility metadata format when the existing descriptor can be extended;
- no second whole-release acceptance database;
- no duplicate canonical user-state ownership in Distribution;
- no same global repository truth manually maintained in multiple files.

---

# 3. Permanent laws

## 3.1 Canonical owner routing

Discovery location never determines ownership.

```text
Discover change
-> determine canonical owner
-> fix owner repo
-> owner CI/acceptance passes
-> record exact immutable owner revision
-> Distribution adopts exact accepted revision
-> Distribution qualifies exact composition
-> System synchronizes meaningful product truth
-> release may be admitted
```

Ambiguous ownership: `BLOCKED - OWNER UNRESOLVED`.

## 3.2 Two validation layers

Owner validation asks whether the component revision satisfies its own contract. Distribution qualification asks whether those exact accepted revisions work together as AI-Verse. A SHA existing is never acceptance evidence by itself.

## 3.3 Static Registry versus dynamic Repository State

- Repository Registry = stable identity, ownership and declared role.
- Repository State = current observed/reconciled state.
- `docs/REPOSITORY-STATE-LEDGER.md` = generated human projection only.

Target shape:

```text
governance/repository-registry.json
        ↓
governance/repository-state.json
        ↓
docs/REPOSITORY-STATE-LEDGER.md
```

## 3.4 Scoped freshness

Use scoped refreshes for scoped decisions. Full scans are reserved for decisions that actually require full-network evidence or the scheduled watchdog.

## 3.5 Git exact identity and ancestry

Use stable repository identity, exact immutable refs and Git ancestry/compare evidence. Dates are display/context information, not lineage authority.

## 3.6 Canonical drift/non-regression

Use `CANONICAL-DRIFT-DETECTED`. Freeze automatic correction, compare exact refs, owner evidence, Distribution truth, System intent/history and migration impact, then reconcile evidence-first. Stale docs cannot revert accepted implementation; newer unvalidated code cannot auto-rewrite canonical System intent.

## 3.7 Drift severity and scope

Every drift record carries:

```text
severity: INFO | WARNING | BLOCKING
scope: component | Core | Agent | Full | global
reason
relevant refs
required action
```

Blocking applies only when severity and release scope intersect, or drift is global.

## 3.8 Member isolation

Maintainer governance, Registry/State/Ledger, drift reports, tombstones, plans and internal qualification evidence do not enter member installs. Prefer deterministic inclusion over broad copy then delete. Unknown/user files remain protected.

## 3.9 Immutable candidate evidence

Every composed release qualification must bind exact Distribution candidate revision, System contract ref, Registry ref, scoped State evidence, exact component refs, component descriptors, owner acceptance evidence, compatibility/migration metadata, preservation evidence and required toolchain/lock facts. Bound-input change requires re-evaluation/requalification.

## 3.10 Durable release evidence

Admitted releases require compact durable receipts sufficient to reconstruct shipped software composition without relying only on expiring CI logs/artifacts.

## 3.11 Emergency safety release

Urgent security, corruption or user-data-protection fixes may use a bounded emergency path, but may not bypass owner validation, exact refs, preservation, compatibility/migration requirements, Distribution whole-product qualification or member isolation. The only allowed temporary debt is explicit non-safety `SYSTEM-SYNC-DEBT`, which blocks later normal promotion until reconciled.

## 3.12 Architecture tombstones

Retired/replaced/prohibited architectures leave durable System-owned evidence so stale docs, audits or future agents cannot resurrect them silently. Component-local tombstones are only for component-owned APIs/schemas/migrations.

## 3.13 No silent contract deletion

A depended-on API/schema/interface cannot be silently removed/redefined because local tests pass. Breaking changes require compatible replacement, versioned coexistence or coordinated breaking release/migration with affected owners and Distribution qualification.

## 3.14 Rollout waves

- Wave 1: System + Distribution + Core (OS, Brain, Memory, Skills, Data).
- Wave 2: Registry-confirmed active Agent-profile repos.
- Wave 3: Registry-confirmed active Full/future ecosystem repos.

Wave 1 must prove the pattern before propagation.

## 3.15 Adaptive execution boundary

Adaptive execution may change tasks and implementation technique inside a fixed slice outcome. It may not silently change permanent laws, product intent, canonical ownership, phase/slice purpose, acceptance criteria in a weaker direction, preservation/safety/member-isolation/evidence floors, major ordering or program denominator.

Protected directional change requires:

`BLOCKED - PLAN AMENDMENT REQUIRED`

Non-degradation law:

> **Discovery may reduce unnecessary work. It may never reduce safety, ownership, preservation, validation, member-isolation or required evidence on its own authority.**

---

# 4. Protection placement map

| Protection | Canonical definition | Local enforcement/publication | Composition verification |
|---|---|---|---|
| Repository Registry | System | System | Distribution consumes relevant subset |
| Repository State + Ledger | System | System refresh tooling | Distribution checks scoped freshness |
| Drift Watchdog | System | System automation | Distribution consumes relevant blocking drift |
| Architecture Tombstones | System | component-local only when needed | System/Distribution inspect when relevant |
| System Invariants | System | canonical owner of each behavior | Distribution verifies cross-component invariants |
| Compatibility metadata | System contract/schema | component release descriptor | Distribution validates selected exact set |
| Promotion | System policy | Distribution | Distribution |
| Reproducibility | System | component immutable refs/metadata | Distribution release receipt |
| No silent contract deletion | System law | interface-owning component | Distribution composed compatibility |
| Decision/recovery provenance | System law | each layer owns its provenance | cross-repo validation |

---

# 5. Required evidence model

Meaningful work records the applicable owner, exact implementation/CI refs, Distribution adoption/qualification refs, System impact/destinations, repository-state refresh scope/drift, member payload impact/isolation, reproducibility impact and plan-amendment impact. A required `NO` decision needs a reason. Missing mandatory evidence blocks completion.

---

# 6. Mandatory execution bookkeeping

Before every substantial slice:

- read latest plan + adaptive planning skill;
- refresh only relevant live state;
- inspect existing implementation/contracts first;
- classify needs as `REUSE`, `EXTEND`, `CREATE`, `RETIRE` or `BLOCK/UNKNOWN`;
- derive the smallest evidence-backed task list;
- update this plan to `IN PROGRESS` with exact refs/tasks before substantive implementation;
- verify no protected roadmap element is silently changed.

Before `COMPLETE`:

- final task list closed/superseded with evidence;
- exact commits/tests/reports recorded;
- blockers/drift/changed assumptions recorded;
- plan-amendment status explicit;
- counters/percentage/next slice updated and committed.

Overall progress = completed slices / 20. Task count is local execution detail only.

Completion report format:

```text
Completed: Slice X.Y - <title>
Tasks: <completed>/<final task total>
Overall: <completed>/20 slices complete (<percent>%)
Phase: <phase number> - <title>
Phase progress: <completed>/<total>
Until next phase: <N> slice(s)
Next: <next slice; first task adaptive until derived>
Blockers/drift/amendments: <concise status>
```

---

# Phase 0 - Persistent program foundation

## Slice 0.1 - Create and normalize the canonical implementation program

**Status:** COMPLETE  
**Evidence:** canonical plan + `docs/ADAPTIVE-IMPLEMENTATION-PLANNING-SKILL.md`  
**Archived detailed record:** commit `acabfba8031421438747fed69bcbc65ba844787e`

Acceptance: canonical resumable plan, roles/laws, reuse constraints, dependency-safe order, bounded adaptive execution, progress bookkeeping and reusable planning skill exist.

---

# Phase 1 - Audit and normalize current reality

**Phase size:** 3 slices  
**Status:** COMPLETE  
**Phase progress:** 3/3

## Slice 1.1 - Audit live repository network and safety machinery

**Status:** COMPLETE  
**Canonical evidence:** `docs/REPOSITORY-NETWORK-AUDIT-2026-10-12.md`  
**Audit commit:** `08e593c9f3b74cae57ab5bf22dbebc33a2a6c176`  
**Start commit:** `20515a27625ca8924a40c01db2fc964ffaa798c0`

Accepted findings carried forward: exact-owner-acceptance descriptor split is BLOCKING for future Core release governance; Purpose Context Blueprint lag is WARNING; Core maintainer handoff gap is WARNING; existing Distribution update/preservation/release machinery is reuse-first.

## Slice 1.2 - Build reuse, ownership, payload and drift inventory

**Status:** COMPLETE  
**Canonical evidence:** `docs/REPOSITORY-NETWORK-REUSE-OWNERSHIP-INVENTORY-2026-10-12.md`  
**Inventory commit:** `8a45649276023ecc6626e5f8b25a76f0403c2912`  
**Start commit:** `6f539af43230dc2c7d96d43dba2d4984d031632f`  
**Closure commit:** `bd3f5a4bc14d88ab5076b74b1226512728b327e0`

Accepted decisions: keep one Component Release Descriptor format; reuse Distribution updater/preservation/candidate/qualification/promotion; create System Registry and Repository State later; generated Markdown ledger only; reject duplicate safe-update, fingerprint, acceptance DB and hand-maintained state mechanisms.

## Slice 1.3 - Freeze implementation architecture and acceptance matrix

**Status:** COMPLETE  
**Canonical evidence:** `docs/REPOSITORY-NETWORK-IMPLEMENTATION-ARCHITECTURE-2026-10-12.md`  
**Start commit:** `819f87aa111aaf6c7c0401e658b4420934a9f4e4`  
**Architecture commit:** `7450247a1d039bd6464e74e58babb6e80d90063a`  
**Closure commit:** `acabfba8031421438747fed69bcbc65ba844787e`

Frozen architecture: System machine control plane under `governance/`; schemas under `contracts/`; refresh tool under `scripts/`; watchdog under `.github/workflows/`; generated ledger under `docs/`; existing descriptor only; existing Distribution release machinery only; candidate evidence at `qualification/<id>/candidate-evidence.json`; admitted receipt at `qualification/<release-id>/release-receipt.json`; deterministic member isolation; daily watchdog with two-missed-run stale rule; Wave 1 acceptance matrix defined.

---

# Phase 2 - Define the canonical System control plane

**Phase size:** 3 slices  
**Current phase progress:** 1/3

## Slice 2.1 - Create the repository-network governance, invariant and tombstone contract

**Status:** COMPLETE  
**Dependencies:** 1.3  
**Task progress:** 5/5

### Slice start record

Slice 2.1 began from the completed Phase 1 architecture freeze, the latest adaptive planning skill and fresh inspection of the existing System safety/release contracts. The slice was limited to permanent governance and architecture-history surfaces. It did not implement Registry, Repository State, watchdog tooling, component handoff files, Distribution gates or runtime behavior.

Starting refs:

- AI-Verse-System `main`: `1da8f5f6187fd8c265e10188b0b5c2d486f01df2`
- ai-verse-distribution `main`: `fd11b4a95487638d47ff55472a3703b03892d0e8`
- AI-Verse-OS `main`: `64f7325444d18f94c9d4755d32eb89f3468bda6b`
- AI-Verse-Brain `main`: `69f7912eeb35f0178f6952ff0554aec8d7f2c496`
- AI-Verse-Memory `main`: `f1327be48ba2ee0043959021365e6dbb9dcb1d3a`
- AI-Verse-Skills `main`: `afde5c06307fba7d074de2929c2eb6c3dc6bdab8`
- AI-Verse-Data `main`: `f8978f8f7a1bc94edecddc2662112233289159a3`

Freshness delta since Slice 1.3 closure:

- Distribution and all five Core owner HEADs were unchanged;
- System advanced from `acabfba8031421438747fed69bcbc65ba844787e` to direct child `1da8f5f6187fd8c265e10188b0b5c2d486f01df2`;
- compare evidence proved that child added only `docs/SAFE-INFRASTRUCTURE-SLICE-1.1-AUDIT.md`, so it did not conflict with this program or the architecture freeze;
- known descriptor, Purpose Context, maintainer-handoff, adapter-knowledge and future-release-receipt findings remained assigned to their later slices.

Existing contracts inspected before task derivation:

- `SAFE-UPDATE-AND-STATE-PRESERVATION-CONTRACT` already owns update/migration/user-state/authority/rollback/fail-closed safety law;
- `COMPONENT-RELEASE-DESCRIPTOR-CONTRACT` already owns component release metadata and owner-vs-Distribution validation separation;
- `WHOLE-RELEASE-PRESERVATION-RESULT-CONTRACT` already owns executable whole-release preservation-result semantics;
- `LIVING-SPEC-PROTOCOL` already owns System synchronization/documentation propagation expectations;
- `OWNER-PRODUCT-INTENT` is product-direction authority but explicitly does not override implementation evidence, ownership, security or migration safety.

Final derived adaptive tasks:

1. **2.1.1 - Refresh current state, inspect the frozen architecture and existing canonical contracts, and derive/refine the execution tasks for this slice.** `COMPLETE`
2. **2.1.2 - Create `docs/REPOSITORY-NETWORK-GOVERNANCE-CONTRACT.md` as the permanent cross-repo governance/invariant contract, referencing existing preservation/release laws rather than copying them.** `COMPLETE`
3. **2.1.3 - Create `docs/ARCHITECTURE-TOMBSTONES.md` using the frozen tombstone format and seed it with Phase 1 rejected duplicate architectures so stale plans/agents cannot resurrect them silently.** `COMPLETE`
4. **2.1.4 - Make the permanent rules discoverable without this program history by linking the governance contract and tombstone ledger from `README.md`, then verify no competing ownership or duplicated safety law was introduced.** `COMPLETE`
5. **2.1.5 - Validate Slice 2.1 acceptance, refresh final refs, record exact evidence and close without runtime/member-payload or protected-roadmap changes.** `COMPLETE`

Protected-boundary check: PASS. The slice implemented the already-frozen permanent governance surface and architecture history only. It did not change canonical ownership, product intent, preservation/safety floors, rollout order, member isolation, runtime behavior or denominator. No plan amendment was required.

### Slice completion record

Permanent governance now exists independently of this implementation program at:

`docs/REPOSITORY-NETWORK-GOVERNANCE-CONTRACT.md`

It defines canonical owner routing, component/System/Distribution handoffs, two-layer validation, exact evidence requirements, canonical drift/non-regression, Registry/State authority, drift scope, no-silent-contract-deletion, member isolation, decision/recovery provenance, architecture tombstones, bounded emergency safety release, least-privilege cross-repo write rules, rollout waves and 20 permanent system invariants.

The governance contract explicitly delegates existing domains to their already-canonical contracts instead of reimplementing them. Detailed update/migration/user-state/rollback/authority safety stays in `SAFE-UPDATE-AND-STATE-PRESERVATION-CONTRACT`; component release metadata stays in `COMPONENT-RELEASE-DESCRIPTOR-CONTRACT`; whole-release preservation result semantics stay in `WHOLE-RELEASE-PRESERVATION-RESULT-CONTRACT`.

Architecture history now exists at:

`docs/ARCHITECTURE-TOMBSTONES.md`

The initial ledger contains eight `prohibited-resurrection` entries for:

1. second component compatibility fingerprint format;
2. second safe-update/state-preservation subsystem;
3. separate whole-release acceptance database;
4. hand-maintained canonical Markdown Repository State ledger;
5. Distribution-owned sibling component acceptance truth;
6. broad member payload copy followed by governance-file deletion;
7. watchdog-owned second Repository State database;
8. parallel promotion/ring database unsupported by Distribution reality.

Each entry uses the frozen tombstone fields and identifies the active replacement architecture plus resurrection condition.

`README.md` now links the permanent governance contract and tombstone ledger under a dedicated repository-network governance section, so future maintainers/agents can find the rules without reading this implementation program.

Validation/evidence:

- Slice start tracker commit: `0da8e768128d905821b8ef9b6c5e0b4d4571f980`.
- Governance contract commit: `0c9cc5034a1165389410e7524af9a8c3d7586ba0`.
- Architecture tombstone commit: `acb47e6178cd3c4bce898c422f615525f7e03fac`.
- README discoverability commit: `5005c3a49802556f72d94f1fd70c274bd795ae20`.
- Compare from Slice 2.1 start to pre-closure head shows only `README.md`, `docs/ARCHITECTURE-TOMBSTONES.md` and `docs/REPOSITORY-NETWORK-GOVERNANCE-CONTRACT.md` changed after the start tracker commit.
- Direct file inspection verified the governance contract references existing canonical safety/release contracts and the tombstone ledger contains the required frozen fields.
- No commit status or workflow run was attached to `5005c3a49802556f72d94f1fd70c274bd795ae20`; no executable test result is claimed for these documentation-only changes.

Final scoped freshness before closure:

- AI-Verse-System pre-closure head: `5005c3a49802556f72d94f1fd70c274bd795ae20`.
- ai-verse-distribution remained `fd11b4a95487638d47ff55472a3703b03892d0e8`.
- AI-Verse-OS remained `64f7325444d18f94c9d4755d32eb89f3468bda6b`.
- AI-Verse-Brain remained `69f7912eeb35f0178f6952ff0554aec8d7f2c496`.
- AI-Verse-Memory remained `f1327be48ba2ee0043959021365e6dbb9dcb1d3a`.
- AI-Verse-Skills remained `afde5c06307fba7d074de2929c2eb6c3dc6bdab8`.
- AI-Verse-Data remained `f8978f8f7a1bc94edecddc2662112233289159a3`.

Drift carried forward:

- `BLOCKING`, Core release-governance evidence: current owner descriptors still do not certify the exact currently shipped refs and four owners use noncanonical `development`; repair remains assigned to later descriptor/handoff slices.
- `WARNING`, Core/System: Purpose Context Blueprint lag remains assigned to Slice 3.3.
- `WARNING`, Core maintainer governance: owner-local handoff remains assigned to Slice 4.2.
- `WARNING`, Distribution/component handoff: hard-coded adapter revision knowledge must remain routing support rather than acceptance authority.
- `INFO`, Distribution reproducibility: compact `release-receipt.json` remains Slice 5.4 implementation work.
- U35/U36 remain `RESOLVED/PASS`.

Owner/component change required: NO.  
Distribution adoption required: NO.  
System impact: YES, permanent governance/tombstone/README/tracker surfaces only.  
Repository-state impact: NO runtime State exists yet; governance semantics only.  
Member payload impact: NO; source-only docs only.  
Reproducibility impact: governance law only; receipt implementation remains later.  
Plan-amendment impact: NO.

Acceptance disposition: PASS. Permanent law is separate from the plan, existing safety/release contracts are referenced rather than replaced, permanent rules are discoverable from README, and tombstones now prevent silent resurrection of the rejected architectures.

### NEXT

**Slice 2.2 - Create the machine-readable Repository Registry and initial Wave 1 registry.**

---

## Slice 2.2 - Create the machine-readable Repository Registry

**Status:** NOT STARTED  
**Dependencies:** 2.1

Create a versioned System-owned machine Registry (`ai-verse.repository-registry/v1`) at the frozen `governance/repository-registry.json` path with schema `contracts/repository-registry.schema.json`. It separates stable identity/ownership/role from dynamic state and registers Wave 1/Core first.

### Acceptance criteria

- one canonical global registry exists;
- stable repo identity survives owner/name rename where available;
- Distribution has no competing registry;
- unknown first-class repos cannot silently enter release composition.

### NEXT

**Slice 2.3 - Define Repository State, generated ledger and maintainer entrypoint.**

---

## Slice 2.3 - Define Repository State, generated ledger and maintainer entrypoint

**Status:** NOT STARTED  
**Dependencies:** 2.2

Create versioned dynamic Repository State (`ai-verse.repository-state/v1`) at `governance/repository-state.json`, schema `contracts/repository-state.schema.json`, generated `docs/REPOSITORY-STATE-LEDGER.md` and `docs/MAINTAINER-START-HERE.md` semantics.

### Acceptance criteria

- Markdown ledger is generated, not canonical editable state;
- Registry facts are not copied as competing truth;
- scoped freshness is explicit;
- `WATCHDOG-STALE`/equivalent prevents silence from masquerading as CLEAN.

### NEXT

**Phase 3 / Slice 3.1 - Implement repository refresh tooling and generated ledger.**

---

# Phase 3 - Build System self-checking machinery and synchronize current truth

**Phase size:** 3 slices

## Slice 3.1 - Implement scoped/full repository refresh and generated ledger

**Status:** NOT STARTED  
**Dependencies:** 2.3

Implement `scripts/refresh_repository_state.py` to consume Registry, resolve exact refs/ancestry, read owner acceptance and Distribution pins, record System sync state, write Repository State and generate the ledger with scoped/full refresh modes.

### Acceptance criteria

- deterministic evidence-backed refresh;
- inaccessible repos become `ACCESS-UNVERIFIED` or equivalent, never CLEAN;
- dates are informational only;
- generated ledger reflects machine state;
- no member-facing files affected.

### NEXT

**Slice 3.2 - Implement Drift Watchdog and heartbeat.**

## Slice 3.2 - Implement Drift Watchdog and heartbeat

**Status:** NOT STARTED  
**Dependencies:** 3.1

Implement scheduled/manual full scans using the same refresh engine, heartbeat/version/scanned-repo/failure evidence, severity/scope drift classification and least-privilege read/validation behavior.

### Acceptance criteria

- stale watchdog cannot present as green;
- unrelated warnings do not block unrelated releases;
- no broad cross-repo write token required;
- watchdog does not duplicate refresh/state logic.

### NEXT

**Slice 3.3 - Reconcile current System truth and known drift.**

## Slice 3.3 - Reconcile current System truth and known drift

**Status:** NOT STARTED  
**Dependencies:** 3.2

Reconcile actual drift evidence-first. Purpose Context remains the mandatory regression fixture. Accepted implementation cannot be reverted because docs lag; unvalidated newer code cannot be promoted because it is newer.

### Acceptance criteria

- non-regression behavior proven;
- Blueprint remains architecture-focused;
- meaningful reconciliation enters changelog/tombstones;
- reconciled Repository State becomes truthful.

---

# Phase 4 - Integrate canonical component owners

**Phase size:** 3 slices

## Slice 4.1 - Extend/reuse the existing Component Release Descriptor

**Status:** NOT STARTED  
**Dependencies:** 3.3

Version/extend only the existing descriptor where evidence proves missing compatibility fields are required. Do not create a second fingerprint format.

### Acceptance criteria

- one component release metadata format remains canonical;
- metadata is bound to exact immutable component revision;
- it does not become live health/readiness/authority truth;
- breaking changes cannot masquerade as ordinary compatible updates.

## Slice 4.2 - Add Wave 1/Core maintainer handoff rules

**Status:** NOT STARTED  
**Dependencies:** 4.1

Add minimal source-only owner handoff semantics for OS, Brain, Memory, Skills and Data using repo-local conventions.

### Acceptance criteria

- all Core owners have discoverable handoff rules;
- owner acceptance ties to exact candidate revision where technically possible;
- no duplicate global governance docs copied into owners;
- local CI alone cannot claim member release.

## Slice 4.3 - Extend handoff governance to Wave 2/3 repos

**Status:** NOT STARTED  
**Dependencies:** 4.2

Propagate the proven semantics only to Registry-confirmed active release-relevant repos.

### Acceptance criteria

- active first-class release repos are registered and have valid handoff paths;
- retired/experimental/external status is explicit;
- CI gaps remain visible;
- no broad cross-repo write authority introduced.

---

# Phase 5 - Enforce safe composition and delivery in Distribution

**Phase size:** 4 slices

## Slice 5.1 - Add immutable candidate evidence snapshot and owner-adoption gates

**Status:** NOT STARTED  
**Dependencies:** 4.3

Extend existing Distribution candidate/release machinery so arbitrary SHAs cannot enter admitted releases and candidate qualification binds exact owner/System/Registry/State evidence.

## Slice 5.2 - Enforce member payload isolation

**Status:** NOT STARTED  
**Dependencies:** 5.1

Enforce deterministic member payload boundaries across fresh install/setup/update/rollback while preserving unknown/user files and existing zero-loss tests.

## Slice 5.3 - Formalize promotion and qualification

**Status:** NOT STARTED  
**Dependencies:** 5.2

Build on existing candidate/released/preservation/promotion mechanics. Owner failure blocks adoption; whole-product failure blocks promotion; scope-relevant BLOCKING drift blocks; break-glass keeps owner/preservation/qualification mandatory; unresolved `SYSTEM-SYNC-DEBT` blocks normal promotion.

## Slice 5.4 - Implement durable reproducibility/release receipts

**Status:** NOT STARTED  
**Dependencies:** 5.3

Persist `qualification/<release-id>/release-receipt.json` as a compact immutable reconstruction binding that references exact release composition/evidence and contains no user secrets/state.

---

# Phase 6 - Prove the whole repository network and close the program

**Phase size:** 3 slices

## Slice 6.1 - Add cross-repo regression and evidence validation

**Status:** NOT STARTED  
**Dependencies:** 5.4

Automate permanent-invariant regressions: owner routing, owner failure, Distribution failure, wrong pin, stale System non-regression, unregistered repo, stale watchdog, breaking contract, candidate snapshot drift, member leakage, user-state survival and receipt validation.

## Slice 6.2 - Run end-to-end qualification

**Status:** NOT STARTED  
**Dependencies:** 6.1

Prove Distribution-originated, component-originated, sibling-defect, stale-doc, breaking-contract and emergency-safety paths end to end with exact refs, preservation, member isolation, provenance and reconstructability.

## Slice 6.3 - Canonical closeout and program handoff

**Status:** NOT STARTED  
**Dependencies:** 6.2

Close only after all 20 slices pass, all required rollout waves are governed, no duplicate source of truth remains, admitted releases use accepted owner refs plus whole-product qualification, preservation/member isolation pass, and Registry/State/watchdog/receipt evidence is operational.

---

# Program Change Log

## 2026-10-12 - Slice 2.1 permanent repository-network governance completed

- Created `docs/REPOSITORY-NETWORK-GOVERNANCE-CONTRACT.md` as permanent cross-repo law independent of this implementation plan.
- Defined canonical owner routing, required handoffs, two-layer validation, exact evidence, non-regression, permanent invariants, breaking-change law, member isolation, decision/recovery provenance, emergency safety release and least-privilege cross-repo write rules.
- Reused existing safe-update, Component Release Descriptor and Whole-Release Preservation Result contracts rather than duplicating their detailed domains.
- Created `docs/ARCHITECTURE-TOMBSTONES.md` and seeded eight Phase 1 rejected duplicate architectures as `prohibited-resurrection`.
- Added README discoverability so future maintainers/agents can find permanent governance without reading program history.
- No runtime, Distribution composition, component repository or member payload changed.
- No protected roadmap amendment was required.

## 2026-10-12 - Tracker compacted at Phase 2 start without changing roadmap semantics

- Full verbose Phase 0/1 tracker history is preserved at commit `acabfba8031421438747fed69bcbc65ba844787e`.
- Live tracker retains permanent laws, roles, existing-contract reuse rules, all 20 slice outcomes/acceptance direction, exact completed-slice evidence refs, current counters and adaptive tasks.
- Compaction was required to keep the canonical tracker safely writable through the GitHub connector and did not change program direction, denominator or acceptance floors.

## 2026-10-12 - Slice 1.3 architecture frozen

- Canonical evidence: `docs/REPOSITORY-NETWORK-IMPLEMENTATION-ARCHITECTURE-2026-10-12.md`.
- Architecture commit: `7450247a1d039bd6464e74e58babb6e80d90063a`.
- Closure: `acabfba8031421438747fed69bcbc65ba844787e`.
- Phase 1 completed 3/3.

## 2026-10-12 - Slice 1.2 inventory completed

- Canonical evidence: `docs/REPOSITORY-NETWORK-REUSE-OWNERSHIP-INVENTORY-2026-10-12.md`.
- Evidence commit: `8a45649276023ecc6626e5f8b25a76f0403c2912`.

## 2026-10-12 - Slice 1.1 audit completed

- Canonical evidence: `docs/REPOSITORY-NETWORK-AUDIT-2026-10-12.md`.
- Evidence commit: `08e593c9f3b74cae57ab5bf22dbebc33a2a6c176`.

## 2026-10-12 - Program normalized into 20 dependency-safe slices

- Overall progress is slice-based.
- Adaptive tasks are derived at slice start.
- Protected roadmap changes require explicit amendment.

---

# Current execution pointer

**Completed:** 5/20  
**Overall:** 25.0%  
**Phase:** Phase 2 - Define the canonical System control plane  
**Phase progress:** 1/3  
**Until Phase 3:** 2 slices  
**Current slice:** Slice 2.1 - Create the repository-network governance, invariant and tombstone contract (`COMPLETE`)  
**Tasks:** 5/5  
**Next:** Slice 2.2 - Create the machine-readable Repository Registry  
**Next task:** not yet derived; generate from fresh Slice 2.2 evidence at slice start  
**Blockers/drift/amendments:** descriptor exact-owner-acceptance/evidence split remains BLOCKING for future Core release governance; Purpose Context Blueprint lag is WARNING; Core maintainer handoff coverage is WARNING; Distribution hard-coded adapter compatibility knowledge is a WARNING extension risk; future compact `release-receipt.json` remains INFO/future work; U35/U36 are RESOLVED/PASS. No plan amendment is required.
