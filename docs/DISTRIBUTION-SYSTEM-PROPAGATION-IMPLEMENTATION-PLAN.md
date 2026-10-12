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
**Current slice:** 2.2 - Create the machine-readable Repository Registry  
**Current slice status:** IN PROGRESS  
**Task progress:** 1/5  
**Next slice:** 2.3 - Define Repository State, generated ledger and maintainer entrypoint  
**Next slice task list:** NOT YET DERIVED - generate from live evidence when Slice 2.3 starts

> This file is the execution tracker. A slice is not COMPLETE until implementation, tests/evidence, tracker update and progress accounting are committed.

## Tracker history preservation

Verbose Phase 0/1 history is preserved at Slice 1.3 closure commit `acabfba8031421438747fed69bcbc65ba844787e`. Verbose Slice 2.1 history is preserved at closure commit `11940b87838afa0f46570ecdd8f8e00f74b7de5a`. Compaction changes presentation only, never program laws, ownership, slice outcomes, acceptance criteria, ordering, denominator or evidence floors.

---

# 0. Mission and permanent execution model

Make the AI-Verse repository network behave as one controlled, self-checking product without collapsing repositories into one codebase.

Central rule:

> **Define centrally. Enforce at the canonical owner. Verify again at composition.**

Execution rule:

> **Fix the destination. Discover the safest route from current reality.**

Adaptive-authority rule:

> **Discovery may adapt the route. It may not silently change the destination.**

Reusable planning method: `docs/ADAPTIVE-IMPLEMENTATION-PLANNING-SKILL.md`.

## Canonical roles

- **AI-Verse-System:** architecture/product intent, ownership, system invariants, cross-repo governance, Repository Registry, Repository State semantics, generated ledger, tombstones, shared governance semantics and current-vs-intended truth. Never a second component implementation home or installer.
- **Component repositories:** implementation, local APIs/schemas, local state/migration/recovery semantics, native CI/acceptance, component release descriptor/evidence and implementation provenance.
- **ai-verse-distribution:** exact release composition, immutable refs, candidate admission, cross-component compatibility, lifecycle orchestration, member payload boundary, whole-product qualification, promotion/channels and durable release reconstruction evidence. Never sibling domain/state authority.
- **Member installation:** admitted runtime/product artifacts plus legitimate member-facing generated files only. Internal governance remains source-only.

## Existing contracts to reuse

- `docs/REPOSITORY-NETWORK-GOVERNANCE-CONTRACT.md`
- `docs/SAFE-UPDATE-AND-STATE-PRESERVATION-CONTRACT.md`
- `docs/COMPONENT-RELEASE-DESCRIPTOR-CONTRACT.md`
- `docs/WHOLE-RELEASE-PRESERVATION-RESULT-CONTRACT.md`
- `docs/LIVING-SPEC-PROTOCOL.md`
- `docs/OWNER-PRODUCT-INTENT.md`
- `docs/ARCHITECTURE-TOMBSTONES.md`

No second updater, compatibility fingerprint, whole-release acceptance database, Repository State authority, sibling acceptance authority or promotion database may be introduced silently.

## Permanent laws

1. Discovery location never determines ownership. Ambiguous ownership is `BLOCKED - OWNER UNRESOLVED`.
2. Owner validation and Distribution whole-product qualification are separate mandatory layers.
3. Repository Registry static truth and Repository State dynamic truth are separate; Markdown ledger is generated projection only.
4. Scoped decisions use scoped refreshes; full scans are reserved for full-network decisions/watchdog.
5. Stable repository identity, exact immutable refs and Git ancestry outrank timestamps for lineage.
6. `CANONICAL-DRIFT-DETECTED` freezes automatic correction. Stale System docs cannot revert accepted implementation; newer unvalidated code cannot rewrite intent automatically.
7. Drift records carry `INFO | WARNING | BLOCKING` plus `component | Core | Agent | Full | global`; only intersecting/global BLOCKING drift blocks a release.
8. Maintainer governance never enters member installs by default. Unknown/user files remain protected.
9. Candidate qualification binds exact Distribution/System/Registry/State/component/descriptor/owner/compatibility/preservation/toolchain evidence; bound-input change requires requalification.
10. Admitted releases require durable reconstruction evidence, not only expiring CI artifacts.
11. Emergency safety release may not bypass owner validation, exact refs, compatibility/migration, preservation, whole-product qualification or member isolation. Only explicit non-safety `SYSTEM-SYNC-DEBT` is temporarily allowed and blocks later normal promotion until reconciled.
12. Retired/replaced/prohibited architecture leaves durable System tombstones.
13. Depended-on APIs/schemas/interfaces cannot disappear silently. Breaking change requires compatible replacement, versioned coexistence or coordinated migration/release.
14. Rollout remains Wave 1 System+Distribution+Core, then Registry-confirmed Wave 2 Agent, then Registry-confirmed Wave 3 Full/future.
15. Adaptive execution may alter tasks/techniques but never silently weaken ownership, product intent, permanent laws, slice outcomes, preservation, validation, member isolation, evidence floors, major ordering or denominator. Protected change requires `BLOCKED - PLAN AMENDMENT REQUIRED`.

Non-degradation law:

> **Discovery may reduce unnecessary work. It may never reduce safety, ownership, preservation, validation, member-isolation or required evidence on its own authority.**

---

# 1. Required execution bookkeeping

Before every substantial slice: read the latest plan/skill, refresh only relevant live state, inspect existing implementation/contracts, classify `REUSE | EXTEND | CREATE | RETIRE | BLOCK/UNKNOWN`, derive the smallest evidence-backed tasks, update this tracker to `IN PROGRESS` before implementation, and verify no protected roadmap element changed.

Before `COMPLETE`: close/supersede every derived task with evidence, record exact commits/tests/reports/fresh refs/drift/amendments, update counters and commit this tracker.

Overall progress = completed slices / 20. Task count is local only.

---

# Phase 0 - Persistent program foundation

## Slice 0.1 - Canonical implementation program

**Status:** COMPLETE  
**Evidence:** this plan + `docs/ADAPTIVE-IMPLEMENTATION-PLANNING-SKILL.md`; archived detail at `acabfba8031421438747fed69bcbc65ba844787e`.

---

# Phase 1 - Audit and normalize current reality

**Status:** COMPLETE, 3/3

## Slice 1.1 - Audit live network and safety machinery

**Status:** COMPLETE  
**Evidence:** `docs/REPOSITORY-NETWORK-AUDIT-2026-10-12.md`, commit `08e593c9f3b74cae57ab5bf22dbebc33a2a6c176`.

Carried findings: descriptor exact-owner-acceptance gap BLOCKING for future Core release governance; Purpose Context Blueprint lag WARNING; Core maintainer handoff WARNING; Distribution safety machinery reuse-first.

## Slice 1.2 - Reuse/ownership/payload/drift inventory

**Status:** COMPLETE  
**Evidence:** `docs/REPOSITORY-NETWORK-REUSE-OWNERSHIP-INVENTORY-2026-10-12.md`, commit `8a45649276023ecc6626e5f8b25a76f0403c2912`.

Decision: one Component Release Descriptor; reuse Distribution update/preservation/candidate/qualification/promotion; System owns future Registry/State; generated ledger only; reject duplicate mechanisms.

## Slice 1.3 - Architecture freeze and Wave 1 acceptance matrix

**Status:** COMPLETE  
**Evidence:** `docs/REPOSITORY-NETWORK-IMPLEMENTATION-ARCHITECTURE-2026-10-12.md`, architecture commit `7450247a1d039bd6464e74e58babb6e80d90063a`, closure `acabfba8031421438747fed69bcbc65ba844787e`.

Frozen paths include `contracts/repository-registry.schema.json`, `governance/repository-registry.json`, later Repository State/ledger/refresh/watchdog surfaces, existing descriptor only and existing Distribution release machinery only.

---

# Phase 2 - Define the canonical System control plane

**Phase size:** 3 slices  
**Current phase progress:** 1/3

## Slice 2.1 - Repository-network governance, invariants and tombstones

**Status:** COMPLETE  
**Task progress:** 5/5  
**Closure:** `11940b87838afa0f46570ecdd8f8e00f74b7de5a`

Created permanent governance at `docs/REPOSITORY-NETWORK-GOVERNANCE-CONTRACT.md`, tombstones at `docs/ARCHITECTURE-TOMBSTONES.md`, and README discoverability. Existing update/release contracts remain canonical for their own domains. No runtime/component/Distribution composition/member payload changed.

## Slice 2.2 - Create the machine-readable Repository Registry

**Status:** IN PROGRESS  
**Dependencies:** 2.1  
**Task progress:** 1/5

### Slice start record

Slice 2.2 begins from accepted Slice 2.1 governance and the frozen Phase 1 control-plane architecture. Fresh inspection confirms existing JSON schemas live under `contracts/`, semantic validators under `scripts/`, and `.github/workflows/contract-validation.yml` already runs Python 3.11/3.13 validation plus the shared unittest suite. Therefore this slice extends that existing validation path rather than creating parallel CI.

Starting refs:

- AI-Verse-System `main`: `11940b87838afa0f46570ecdd8f8e00f74b7de5a`
- ai-verse-distribution `main`: `fd11b4a95487638d47ff55472a3703b03892d0e8`
- AI-Verse-OS `main`: `64f7325444d18f94c9d4755d32eb89f3468bda6b`
- AI-Verse-Brain `main`: `69f7912eeb35f0178f6952ff0554aec8d7f2c496`
- AI-Verse-Memory `main`: `f1327be48ba2ee0043959021365e6dbb9dcb1d3a`
- AI-Verse-Skills `main`: `afde5c06307fba7d074de2929c2eb6c3dc6bdab8`
- AI-Verse-Data `main`: `f8978f8f7a1bc94edecddc2662112233289159a3`

All seven refs are unchanged from the end of Slice 2.1 except System, whose head is exactly the Slice 2.1 closure commit.

Fresh stable repository identity verification:

- System: GitHub repository ID `1367664026`, current name `aiverse-filmmakers/AI-Verse-System`
- Distribution: `1350081263`, `aiverse-filmmakers/ai-verse-distribution`
- OS: `1361862361`, `aiverse-filmmakers/AI-Verse-OS`
- Brain: `1362233598`, `aiverse-filmmakers/AI-Verse-Brain`
- Memory: `1361910454`, `aiverse-filmmakers/AI-Verse-Memory`
- Skills: `1362243580`, `aiverse-filmmakers/AI-Verse-Skills`
- Data: `1364457521`, `aiverse-filmmakers/AI-Verse-Data`

The IDs match the Phase 1 audit and are the rename-safe identity anchor. Current `owner/name` remains declarative routing metadata, not logical identity.

Relevant mechanism classification:

- Registry schema at `contracts/repository-registry.schema.json`: `CREATE`, frozen Phase 1 destination.
- Registry data at `governance/repository-registry.json`: `CREATE`, the one global static registry authority.
- semantic validator at `scripts/validate_repository_registry.py`: `CREATE`, following existing validator convention.
- contract validation workflow: `EXTEND`, reuse existing `.github/workflows/contract-validation.yml`.
- shared unittest suite: `EXTEND` with Registry positive/negative semantic cases.
- Distribution registry/database: `RETIRE/NOT NEEDED`; Distribution consumes/freeze-snapshots relevant System Registry evidence later but does not own a competing editable registry.
- Repository State/current HEAD/accepted ref/Distribution pin/current drift: `NOT IN REGISTRY`; those remain Slice 2.3+ dynamic State concerns.

Final derived adaptive tasks:

1. **2.2.1 - Refresh Wave 1 refs/stable repository identities, inspect schema/validator/CI conventions and derive/refine the task list.** `COMPLETE`
2. **2.2.2 - Create `contracts/repository-registry.schema.json` with versioned static identity/ownership/lifecycle/profile/descriptor/acceptance/spec/dependency semantics and explicit exclusion of dynamic state.** `NOT STARTED`
3. **2.2.3 - Create `governance/repository-registry.json` with System, Distribution and the five Core owners as Wave 1 entries, using stable GitHub IDs as logical identity anchors and current names as routing metadata.** `NOT STARTED`
4. **2.2.4 - Add `scripts/validate_repository_registry.py`, Registry contract tests and extend existing contract-validation workflow; prove uniqueness, rename-safe identity, lifecycle/profile/shipping invariants and fail-closed unknown first-class release participation semantics.** `NOT STARTED`
5. **2.2.5 - Run/inspect validation evidence, refresh final refs, verify Distribution has no competing registry and close Slice 2.2 without dynamic State/runtime/member-payload or protected-roadmap changes.** `NOT STARTED`

Protected-boundary check: PASS. This slice implements only the already-frozen static System Registry. It does not create Repository State, infer current acceptance/HEAD/drift, change release composition, alter component ownership, modify member payload or weaken any safety/validation floor. No plan amendment is required.

### Acceptance criteria

- one canonical global Registry exists at `governance/repository-registry.json`;
- stable repository identity prevents owner/name rename from silently creating a new logical component;
- static Registry facts remain separate from dynamic Repository State;
- Distribution does not maintain a competing independent Registry;
- unregistered first-class release components cannot be treated as silently admitted by Registry semantics/validator;
- schema, semantic validator and existing contract-validation path cover the Registry.

### NEXT

**Slice 2.3 - Define Repository State, generated ledger and maintainer entrypoint.**

## Slice 2.3 - Define Repository State, generated ledger and maintainer entrypoint

**Status:** NOT STARTED  
**Dependencies:** 2.2

Create versioned dynamic Repository State at `governance/repository-state.json`, schema `contracts/repository-state.schema.json`, generated `docs/REPOSITORY-STATE-LEDGER.md` and `docs/MAINTAINER-START-HERE.md` semantics.

Acceptance: Markdown ledger generated only; Registry facts are not independent dynamic truth; scoped freshness explicit; stale/missing watchdog evidence cannot masquerade as CLEAN.

---

# Phase 3 - Build System self-checking machinery and synchronize current truth

**Phase size:** 3 slices

## Slice 3.1 - Scoped/full repository refresh and generated ledger

**Status:** NOT STARTED  
**Dependencies:** 2.3

Implement `scripts/refresh_repository_state.py` consuming Registry and exact Git/owner/Distribution evidence. Acceptance: deterministic evidence-backed refresh, inaccessible repos explicit, dates informational only, generated ledger truthful, no member impact.

## Slice 3.2 - Drift Watchdog and heartbeat

**Status:** NOT STARTED  
**Dependencies:** 3.1

Scheduled/manual full scans reuse the same refresh engine and record heartbeat/failures/severity/scope. Acceptance: stale watchdog never green, unrelated warnings do not block unrelated releases, least-privilege read/validation, no second state engine.

## Slice 3.3 - Reconcile current System truth and known drift

**Status:** NOT STARTED  
**Dependencies:** 3.2

Reconcile actual drift evidence-first, with Purpose Context as mandatory regression fixture. Acceptance: accepted implementation not reverted because docs lag; unvalidated newer code not canonized because newer; architecture docs remain appropriately stable; reconciliation is recorded and Repository State becomes truthful.

---

# Phase 4 - Integrate canonical component owners

**Phase size:** 3 slices

## Slice 4.1 - Extend/reuse Component Release Descriptor

**Status:** NOT STARTED  
**Dependencies:** 3.3

Extend only the existing descriptor where evidence proves missing compatibility fields. Acceptance: one metadata format, exact immutable revision binding, no live health/readiness authority, breaking changes cannot masquerade as compatible.

## Slice 4.2 - Wave 1/Core maintainer handoff

**Status:** NOT STARTED  
**Dependencies:** 4.1

Add minimal source-only owner handoff semantics in OS, Brain, Memory, Skills and Data. Acceptance: discoverable handoff, exact candidate acceptance where possible, no copied global governance docs, local CI cannot claim member release alone.

## Slice 4.3 - Wave 2/3 handoff governance

**Status:** NOT STARTED  
**Dependencies:** 4.2

Apply proven semantics only to Registry-confirmed active release-relevant repos. Acceptance: active first-class repos registered/handoff-capable, retired/experimental/external explicit, CI gaps visible, no broad write authority.

---

# Phase 5 - Enforce safe composition and delivery in Distribution

**Phase size:** 4 slices

## Slice 5.1 - Immutable candidate snapshot and owner-adoption gates

**Status:** NOT STARTED  
**Dependencies:** 4.3

Extend existing candidate machinery so arbitrary SHAs cannot enter admission and exact owner/System/Registry/State evidence is frozen.

## Slice 5.2 - Member payload isolation

**Status:** NOT STARTED  
**Dependencies:** 5.1

Enforce deterministic payload boundaries across install/setup/update/rollback while preserving unknown/user files and zero-loss behavior.

## Slice 5.3 - Promotion and qualification

**Status:** NOT STARTED  
**Dependencies:** 5.2

Use existing candidate/released/preservation/promotion mechanics. Owner failure blocks adoption; whole-product failure blocks promotion; intersecting BLOCKING drift blocks; emergency path preserves all safety gates; `SYSTEM-SYNC-DEBT` blocks later normal promotion.

## Slice 5.4 - Durable release receipts

**Status:** NOT STARTED  
**Dependencies:** 5.3

Persist `qualification/<release-id>/release-receipt.json` as compact immutable reconstruction binding without user secrets/state.

---

# Phase 6 - Prove the network and close

**Phase size:** 3 slices

## Slice 6.1 - Cross-repo regression/evidence validation

**Status:** NOT STARTED  
**Dependencies:** 5.4

Automate permanent-invariant regressions for owner routing, owner/Distribution failure, wrong pin, stale System, unregistered repo, stale watchdog, breaking contract, candidate drift, member leakage, user-state survival and receipt validity.

## Slice 6.2 - End-to-end qualification

**Status:** NOT STARTED  
**Dependencies:** 6.1

Prove Distribution-originated, component-originated, sibling-defect, stale-doc, breaking-contract and emergency paths end to end with exact refs, preservation, member isolation, provenance and reconstructability.

## Slice 6.3 - Canonical closeout and handoff

**Status:** NOT STARTED  
**Dependencies:** 6.2

Close only after all 20 slices pass, required rollout waves are governed, no duplicate truth remains, admitted releases use accepted owner refs plus whole-product qualification, preservation/member isolation pass, and Registry/State/watchdog/receipt evidence is operational.

---

# Program Change Log

## 2026-10-12 - Slice 2.2 started from fresh Wave 1 identity evidence

- Confirmed all seven Wave 1 repository heads are unchanged from Slice 2.1 closure except System being exactly the Slice 2.1 closure commit.
- Reverified stable GitHub repository IDs and current `owner/name` for System, Distribution, OS, Brain, Memory, Skills and Data.
- Confirmed existing schema/validator/contract-validation conventions and chose `CREATE` for Registry schema/data/validator, `EXTEND` for existing CI/tests and `RETIRE/NOT NEEDED` for any Distribution-owned competing registry.
- Derived five evidence-backed tasks without changing the frozen architecture or acceptance floor.

## 2026-10-12 - Slice 2.1 permanent governance completed

- Created `docs/REPOSITORY-NETWORK-GOVERNANCE-CONTRACT.md` and `docs/ARCHITECTURE-TOMBSTONES.md`; linked both from README.
- Reused existing update/release contracts; no runtime, release composition, component repository or member payload changed.
- Closure commit: `11940b87838afa0f46570ecdd8f8e00f74b7de5a`.

## 2026-10-12 - Phase 1 completed and architecture frozen

- Audit: `docs/REPOSITORY-NETWORK-AUDIT-2026-10-12.md`.
- Inventory: `docs/REPOSITORY-NETWORK-REUSE-OWNERSHIP-INVENTORY-2026-10-12.md`.
- Architecture: `docs/REPOSITORY-NETWORK-IMPLEMENTATION-ARCHITECTURE-2026-10-12.md`.
- Phase 1 closure: `acabfba8031421438747fed69bcbc65ba844787e`.

---

# Current execution pointer

**Completed:** 5/20  
**Overall:** 25.0%  
**Phase:** Phase 2 - Define the canonical System control plane  
**Phase progress:** 1/3  
**Until Phase 3:** 2 slices  
**Current slice:** Slice 2.2 - Create the machine-readable Repository Registry (`IN PROGRESS`)  
**Tasks:** 1/5  
**Current task:** 2.2.2 - Create the Registry schema  
**Next:** Slice 2.3 after Slice 2.2 acceptance  
**Blockers/drift/amendments:** descriptor exact-owner-acceptance/evidence split remains BLOCKING for future Core release governance; Purpose Context Blueprint lag WARNING; Core maintainer handoff WARNING; Distribution hard-coded adapter compatibility knowledge WARNING; compact release receipt INFO/future work; U35/U36 RESOLVED/PASS. No plan amendment required.
