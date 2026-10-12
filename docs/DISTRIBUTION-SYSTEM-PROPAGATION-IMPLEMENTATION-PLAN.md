# AI-Verse Repository Network Governance, Release Safety and Self-Checking Implementation Plan

**Status:** ACTIVE  
**Canonical planning repo:** `aiverse-filmmakers/AI-Verse-System`  
**Primary implementation repo:** `aiverse-filmmakers/ai-verse-distribution`  
**Affected repos:** AI-Verse-System, ai-verse-distribution, all releasable AI-Verse component repositories  
**Started:** 2026-10-12  
**Program size:** 20 slices  
**Completed:** 6  
**Remaining:** 14  
**Overall progress:** 30.0%  
**Current execution phase:** Phase 2 - Define the canonical System control plane  
**Current phase progress:** 2/3 slices complete  
**Slices until next phase:** 1  
**Current slice:** 2.2 - Create the machine-readable Repository Registry  
**Current slice status:** COMPLETE  
**Task progress:** 5/5  
**Next slice:** 2.3 - Define Repository State, generated ledger and maintainer entrypoint  
**Next slice task list:** NOT YET DERIVED - generate from live evidence when Slice 2.3 starts

> This file is the execution tracker. A slice is not COMPLETE until implementation, tests/evidence, tracker update and progress accounting are committed.

## Tracker history preservation

Verbose Phase 0/1 history is preserved at Slice 1.3 closure `acabfba8031421438747fed69bcbc65ba844787e`. Verbose Slice 2.1 history is preserved at closure `11940b87838afa0f46570ecdd8f8e00f74b7de5a`. Slice 2.2 detailed start state is preserved at `4e5b8b55a3f5227083daf72ec55d9fcaaef3a12f`. Compaction changes presentation only, never program laws, ownership, slice outcomes, acceptance criteria, ordering, denominator or evidence floors.

---

# 0. Mission and permanent execution model

Make the AI-Verse repository network behave as one controlled, self-checking product without collapsing repositories into one codebase.

> **Define centrally. Enforce at the canonical owner. Verify again at composition.**

> **Fix the destination. Discover the safest route from current reality.**

> **Discovery may adapt the route. It may not silently change the destination.**

Reusable planning method: `docs/ADAPTIVE-IMPLEMENTATION-PLANNING-SKILL.md`.

## Canonical roles

- **AI-Verse-System:** architecture/product intent, ownership, invariants, cross-repository governance, Repository Registry, Repository State semantics, generated ledger, tombstones and current-vs-intended truth. Never a second component implementation home or installer.
- **Component repositories:** implementation, local APIs/schemas, local state/migration/recovery semantics, native CI/acceptance, component release descriptor/evidence and implementation provenance.
- **ai-verse-distribution:** exact release composition, candidate admission, compatibility, lifecycle orchestration, member payload boundary, whole-product qualification, promotion/channels and durable release reconstruction. Never sibling domain/state authority.
- **Member installation:** admitted runtime/product artifacts plus legitimate member-facing generated files only. Internal governance remains source-only.

## Canonical contracts to reuse

- `docs/REPOSITORY-NETWORK-GOVERNANCE-CONTRACT.md`
- `docs/SAFE-UPDATE-AND-STATE-PRESERVATION-CONTRACT.md`
- `docs/COMPONENT-RELEASE-DESCRIPTOR-CONTRACT.md`
- `docs/WHOLE-RELEASE-PRESERVATION-RESULT-CONTRACT.md`
- `docs/LIVING-SPEC-PROTOCOL.md`
- `docs/OWNER-PRODUCT-INTENT.md`
- `docs/ARCHITECTURE-TOMBSTONES.md`

No second updater, compatibility fingerprint, whole-release acceptance database, Registry/State authority, sibling acceptance authority or promotion database may be introduced silently.

## Permanent laws

1. Discovery location never determines ownership. Ambiguity is `BLOCKED - OWNER UNRESOLVED`.
2. Owner validation and Distribution qualification are separate mandatory layers.
3. Repository Registry static truth, Repository State dynamic truth and generated human ledger are distinct.
4. Scoped decisions use scoped refreshes; full scans are reserved for full-network decisions/watchdog.
5. Stable repository identity, exact immutable refs and Git ancestry outrank timestamps for lineage.
6. `CANONICAL-DRIFT-DETECTED` freezes automatic correction. Stale docs cannot regress accepted implementation; newer unvalidated code cannot auto-rewrite intent.
7. Drift carries `INFO | WARNING | BLOCKING` plus `component | Core | Agent | Full | global`; only intersecting/global BLOCKING drift blocks release.
8. Maintainer governance remains outside member installs. Unknown/user files remain protected.
9. Candidate qualification binds exact Distribution/System/Registry/State/component/descriptor/owner/compatibility/preservation/toolchain evidence; bound-input change requires requalification.
10. Admitted releases require durable reconstruction evidence.
11. Emergency safety release cannot bypass owner validation, exact refs, compatibility/migration, preservation, whole-product qualification or member isolation. Only explicit non-safety `SYSTEM-SYNC-DEBT` may be temporarily carried and it blocks later normal promotion until reconciled.
12. Retired/replaced/prohibited architecture leaves durable tombstones.
13. Depended-on contracts cannot disappear silently. Breaking change requires compatible replacement, versioned coexistence or coordinated migration/release.
14. Rollout remains Wave 1 System+Distribution+Core, then Registry-confirmed Wave 2 Agent, then Registry-confirmed Wave 3 Full/future.
15. Adaptive execution may alter tasks/techniques but never silently weaken ownership, product intent, permanent laws, slice outcomes, safety, validation, member isolation, evidence floors, major ordering or denominator. Protected change requires `BLOCKED - PLAN AMENDMENT REQUIRED`.

> **Discovery may reduce unnecessary work. It may never reduce safety, ownership, preservation, validation, member-isolation or required evidence on its own authority.**

---

# 1. Required execution bookkeeping

Before every substantial slice: read latest plan/skill, refresh relevant live state, inspect existing implementation/contracts, classify `REUSE | EXTEND | CREATE | RETIRE | BLOCK/UNKNOWN`, derive the smallest evidence-backed tasks, update this tracker to `IN PROGRESS` before implementation, and verify no protected roadmap element changed.

Before `COMPLETE`: close or supersede every task with evidence, record exact commits/tests/reports/final refs/drift/amendments, update counters and commit this tracker.

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

Decision: one Component Release Descriptor; reuse Distribution update/preservation/candidate/qualification/promotion; System owns Registry/State; generated ledger only; reject duplicate mechanisms.

## Slice 1.3 - Architecture freeze and Wave 1 acceptance matrix

**Status:** COMPLETE  
**Evidence:** `docs/REPOSITORY-NETWORK-IMPLEMENTATION-ARCHITECTURE-2026-10-12.md`, architecture commit `7450247a1d039bd6464e74e58babb6e80d90063a`, closure `acabfba8031421438747fed69bcbc65ba844787e`.

Frozen paths include Registry/State schemas and data, generated ledger, refresh/watchdog surfaces, existing component descriptor only and existing Distribution release machinery only.

---

# Phase 2 - Define the canonical System control plane

**Phase size:** 3 slices  
**Current phase progress:** 2/3

## Slice 2.1 - Repository-network governance, invariants and tombstones

**Status:** COMPLETE  
**Task progress:** 5/5  
**Closure:** `11940b87838afa0f46570ecdd8f8e00f74b7de5a`

Created `docs/REPOSITORY-NETWORK-GOVERNANCE-CONTRACT.md`, `docs/ARCHITECTURE-TOMBSTONES.md` and README discoverability. Existing update/release contracts remain canonical for their domains.

## Slice 2.2 - Create the machine-readable Repository Registry

**Status:** COMPLETE  
**Dependencies:** 2.1  
**Task progress:** 5/5

### Final task record

1. **2.2.1 - Refresh Wave 1 refs/stable repository identities, inspect schema/validator/CI conventions and derive/refine the task list.** `COMPLETE`
2. **2.2.2 - Create `contracts/repository-registry.schema.json` with versioned static identity/ownership/lifecycle/profile/descriptor/acceptance/spec/dependency semantics and explicit exclusion of dynamic state.** `COMPLETE`
3. **2.2.3 - Create `governance/repository-registry.json` with System, Distribution and five Core owners, stable GitHub IDs as logical identity anchors and current names as routing metadata.** `COMPLETE`
4. **2.2.4 - Add semantic validator/tests and extend existing Contract Validation workflow; prove uniqueness, rename-safe identity, lifecycle/profile/shipping invariants and fail-closed unregistered release semantics.** `COMPLETE`
5. **2.2.5 - Run validation, refresh final refs, verify no competing Distribution Registry, account for concurrency and close without dynamic State/runtime/member-payload/protected-roadmap changes.** `COMPLETE`

### Implementation evidence

- Slice start/tracker: `4e5b8b55a3f5227083daf72ec55d9fcaaef3a12f`
- Registry schema: `7ecb833240ff6824aa43097f48be9d611b94c8f5`
- Initial seven-entry Registry: `94179f1e26d2e19fae3b104cac7c2eb74d107917`
- Semantic validator: `a0e14b9f74061594b30e6376ffef12db4a65bc48`
- Contract tests: `6ddfc792e0200dfc4da653e9c8c59117c2eb47ed`
- Existing Contract Validation workflow extension: `f8878460ee2757fad7249e3ca666b5af0d8a801a`
- Initial closure tracker write: `f63e93b45cf42f37de51dc24a379cd63c1005fa7`
- Canonical machine Registry: `governance/repository-registry.json`
- Registry schema: `contracts/repository-registry.schema.json`
- Validator: `scripts/validate_repository_registry.py`
- Tests: `tests/test_repository_registry.py`

### Registry semantics accepted

- schema version is `ai-verse.repository-registry/v1`;
- `repository_id` is the stable logical identity key;
- current `owner/name` is routing metadata, so a rename with unchanged stable ID does not create a new logical repository;
- first-class unregistered release participation is fail-closed with `unregistered_first_class_release: block`;
- Distribution explicitly is not an independent Registry authority;
- Registry holds only stable/declarative identity, responsibility, lifecycle, rollout wave, release-profile participation, shipping participation, descriptor path, acceptance discovery surface, System refs and optional known direct compatibility dependencies;
- live HEAD, owner-accepted revision, Distribution pin, CI outcome, last refresh, drift and watchdog state are excluded and remain Repository State concerns;
- initial Wave 1 Registry contains exactly seven entries: System, Distribution, OS, Brain, Memory, Skills and Data;
- System/Distribution are Wave 1 control-plane participants but are not marked as Distribution-shipped runtime components;
- five Core owners are active `runtime-component` entries, participate in `Core`, are Distribution-shipped and expect `release/component-release.json` plus component-native owner acceptance.

### Validation evidence

Contract Validation workflow run `38256854398` on commit `f8878460ee2757fad7249e3ca666b5af0d8a801a` completed `success`.

Both matrix jobs passed:

- Python 3.13 job `114837022223`
- Python 3.11 job `114837022371`

Both jobs passed the existing descriptor/preservation checks, the new `Validate repository registry` step and the full shared contract test suite. Registry tests prove rename-safe identity, duplicate stable-ID/component-ID rejection, dynamic-field rejection, shipped-component descriptor/profile/native-acceptance requirements, Distribution authority rejection and unregistered dependency rejection.

Distribution searches for `repository-registry` and `repository_registry` returned no matching code entries. GitHub marked those searches incomplete, so they are supportive evidence rather than standalone proof; they are consistent with the Phase 1 audit and with Distribution remaining unchanged during this slice.

### Final freshness and concurrent System work

Component/Distribution refs remained unchanged through final refresh:

- ai-verse-distribution: `fd11b4a95487638d47ff55472a3703b03892d0e8`
- AI-Verse-OS: `64f7325444d18f94c9d4755d32eb89f3468bda6b`
- AI-Verse-Brain: `69f7912eeb35f0178f6952ff0554aec8d7f2c496`
- AI-Verse-Memory: `f1327be48ba2ee0043959021365e6dbb9dcb1d3a`
- AI-Verse-Skills: `afde5c06307fba7d074de2929c2eb6c3dc6bdab8`
- AI-Verse-Data: `f8978f8f7a1bc94edecddc2662112233289159a3`

Two unrelated concurrent System commits were preserved:

1. `d9920be2727a550266086b84b73aafbc397c07de`, `Record Safe Infrastructure Slice 1.2 evidence inventory`, added only `docs/SAFE-INFRASTRUCTURE-SLICE-1.2-INVENTORY.md`.
2. `e515c6356b9619d5c20ec5f9448cba9f273ca015`, `Freeze Safe Infrastructure Phase 1 architecture`, added only `docs/SAFE-INFRASTRUCTURE-SLICE-1.3-ARCHITECTURE-FREEZE.md`.

Neither touched this program, Registry schema/data, validator, Registry tests or the Contract Validation workflow. The successful Registry CI run occurred after the first concurrent commit; the second concurrent commit landed after that successful CI and before the Slice 2.2 tracker closure. Exact compare proves the second commit is documentation-only and unrelated to Registry behavior. The initial closure tracker write `f63e93b45cf42f37de51dc24a379cd63c1005fa7` followed it without overwriting it.

### Acceptance disposition

PASS.

- one canonical global Registry exists;
- stable repository ID protects logical identity across owner/name rename;
- static Registry truth is separated from future dynamic Repository State;
- Distribution has no competing Registry authority and remained unchanged;
- unregistered first-class release participation is explicitly fail-closed;
- schema, semantic validator, positive/negative tests and the existing Contract Validation path cover the Registry;
- no runtime behavior, release composition, component implementation or member payload changed;
- concurrent unrelated System work was preserved and explicitly accounted for;
- no protected roadmap element changed and no plan amendment was required.

Known drift carried forward unchanged: descriptor exact-owner-acceptance/evidence split remains BLOCKING for future Core release governance; Purpose Context Blueprint lag WARNING; Core maintainer handoff WARNING; Distribution adapter hard-coded compatibility knowledge WARNING; compact release receipt INFO/future work; U35/U36 remain RESOLVED/PASS.

### NEXT

**Slice 2.3 - Define Repository State, generated ledger and maintainer entrypoint.**

## Slice 2.3 - Define Repository State, generated ledger and maintainer entrypoint

**Status:** NOT STARTED  
**Dependencies:** 2.2

Create versioned dynamic Repository State at `governance/repository-state.json`, schema `contracts/repository-state.schema.json`, generated `docs/REPOSITORY-STATE-LEDGER.md` and `docs/MAINTAINER-START-HERE.md` semantics.

Acceptance: Markdown ledger generated only; Registry fields are not independently duplicated as dynamic truth; scoped freshness is explicit; `WATCHDOG-STALE`/equivalent exists so silence cannot masquerade as CLEAN.

---

# Phase 3 - Build System self-checking machinery and synchronize current truth

**Phase size:** 3 slices

## Slice 3.1 - Scoped/full repository refresh and generated ledger

**Status:** NOT STARTED  
**Dependencies:** 2.3

Implement `scripts/refresh_repository_state.py` consuming Registry and exact Git/owner/Distribution evidence. Acceptance: deterministic/evidence-backed refresh, inaccessible repos explicit, dates informational only, generated ledger truthful, no member impact.

## Slice 3.2 - Drift Watchdog and heartbeat

**Status:** NOT STARTED  
**Dependencies:** 3.1

Scheduled/manual full scans reuse the same refresh engine and record heartbeat/failures/severity/scope. Acceptance: stale watchdog never green, unrelated warnings do not block unrelated releases, least-privilege read/validation, no second state engine.

## Slice 3.3 - Reconcile current System truth and known drift

**Status:** NOT STARTED  
**Dependencies:** 3.2

Reconcile actual drift evidence-first, with Purpose Context as mandatory regression fixture. Acceptance: accepted implementation not reverted because docs lag; unvalidated newer code not canonized because newer; architecture docs remain appropriately stable; reconciliation recorded and Repository State truthful.

---

# Phase 4 - Integrate canonical component owners

**Phase size:** 3 slices

## Slice 4.1 - Extend/reuse Component Release Descriptor

**Status:** NOT STARTED  
**Dependencies:** 3.3

Extend only the existing descriptor where evidence proves missing compatibility fields. Acceptance: one metadata format, exact immutable revision binding, no live-health/readiness authority, breaking changes cannot masquerade as compatible.

## Slice 4.2 - Wave 1/Core maintainer handoff

**Status:** NOT STARTED  
**Dependencies:** 4.1

Add minimal source-only owner handoff semantics in OS, Brain, Memory, Skills and Data. Acceptance: discoverable handoff, exact candidate acceptance where technically possible, no copied global governance docs, local CI cannot claim member release alone.

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

Automate permanent-invariant regressions for owner routing, owner/Distribution failures, wrong pins, stale System, unregistered repos, stale watchdog, breaking contracts, candidate drift, member leakage, user-state survival and receipt validity.

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

## 2026-10-12 - Slice 2.2 machine-readable Repository Registry completed

- Created versioned `ai-verse.repository-registry/v1` schema and the single System-owned `governance/repository-registry.json` authority.
- Registered System, Distribution, OS, Brain, Memory, Skills and Data as initial Wave 1 entries using stable GitHub repository IDs as logical identity anchors.
- Kept current `owner/name` as routing metadata and excluded live/dynamic state from Registry.
- Added semantic validation for identity uniqueness, shipping/profile/lifecycle/descriptor/acceptance rules, fail-closed unregistered participation and non-Registry Distribution authority.
- Added Registry tests and extended the existing Contract Validation workflow instead of creating parallel CI.
- GitHub Actions run `38256854398` passed on Python 3.11 and 3.13, including Registry validation and shared tests.
- Preserved and accounted for unrelated concurrent System commits `d9920be2727a550266086b84b73aafbc397c07de` and `e515c6356b9619d5c20ec5f9448cba9f273ca015`, each of which added only a separate Safe Infrastructure evidence document.
- No runtime, release composition, member payload or protected roadmap change occurred.

## 2026-10-12 - Slice 2.1 permanent governance completed

- Created repository-network governance contract and architecture tombstone ledger and linked them from README.
- Closure: `11940b87838afa0f46570ecdd8f8e00f74b7de5a`.

## 2026-10-12 - Phase 1 completed and architecture frozen

- Audit: `docs/REPOSITORY-NETWORK-AUDIT-2026-10-12.md`.
- Inventory: `docs/REPOSITORY-NETWORK-REUSE-OWNERSHIP-INVENTORY-2026-10-12.md`.
- Architecture: `docs/REPOSITORY-NETWORK-IMPLEMENTATION-ARCHITECTURE-2026-10-12.md`.
- Closure: `acabfba8031421438747fed69bcbc65ba844787e`.

---

# Current execution pointer

**Completed:** 6/20  
**Overall:** 30.0%  
**Phase:** Phase 2 - Define the canonical System control plane  
**Phase progress:** 2/3  
**Until Phase 3:** 1 slice  
**Current slice:** Slice 2.2 - Create the machine-readable Repository Registry (`COMPLETE`)  
**Tasks:** 5/5  
**Next:** Slice 2.3 - Define Repository State, generated ledger and maintainer entrypoint  
**Next task:** not yet derived; generate from fresh Slice 2.3 evidence at slice start  
**Blockers/drift/amendments:** descriptor exact-owner-acceptance/evidence split remains BLOCKING for future Core release governance; Purpose Context Blueprint lag WARNING; Core maintainer handoff WARNING; Distribution hard-coded adapter compatibility knowledge WARNING; compact release receipt INFO/future work; U35/U36 RESOLVED/PASS. No plan amendment required.
