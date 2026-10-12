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
**Current slice:** 2.3 - Define Repository State, generated ledger and maintainer entrypoint  
**Current slice status:** IN PROGRESS  
**Task progress:** 1/6  
**Next slice:** 3.1 - Scoped/full repository refresh and generated ledger  
**Next slice task list:** NOT YET DERIVED - generate from live evidence when Slice 3.1 starts

> This file is the execution tracker. A slice is not COMPLETE until implementation, tests/evidence, tracker update and progress accounting are committed.

## Tracker history preservation

Verbose Phase 0/1 history is preserved at Slice 1.3 closure `acabfba8031421438747fed69bcbc65ba844787e`. Verbose Slice 2.1 history is preserved at closure `11940b87838afa0f46570ecdd8f8e00f74b7de5a`. Slice 2.2 detailed start state is preserved at `4e5b8b55a3f5227083daf72ec55d9fcaaef3a12f` and closure evidence at `98773f6db85ac727a32ed798cf5113fe839e24a1`. Compaction changes presentation only, never program laws, ownership, slice outcomes, acceptance criteria, ordering, denominator or evidence floors.

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
**Closure:** `98773f6db85ac727a32ed798cf5113fe839e24a1`

Created `ai-verse.repository-registry/v1`, the canonical seven-entry Wave 1 Registry, semantic validator/tests and existing Contract Validation workflow coverage. Stable GitHub repository ID is logical identity; owner/name is routing metadata; dynamic state is excluded; unregistered first-class release participation is fail-closed; Distribution is not a competing Registry authority. GitHub Actions run `38256854398` passed Python 3.11 and 3.13. Known drift carried forward unchanged.

## Slice 2.3 - Define Repository State, generated ledger and maintainer entrypoint

**Status:** IN PROGRESS  
**Dependencies:** 2.2  
**Task progress:** 1/6

### Slice start record

Slice 2.3 starts from the completed static Registry and the frozen Phase 1 control-plane architecture. Fresh inspection found no existing Repository State schema/data, state validator, generated repository-state ledger, maintainer entrypoint or repository-state refresh/generation script. Therefore these surfaces are `CREATE`, while the existing Contract Validation workflow is `EXTEND`.

Starting refs:

- AI-Verse-System `main`: `606bab362e68b3689f1d497849fc7dfc6545a934`
- ai-verse-distribution `main`: `fd11b4a95487638d47ff55472a3703b03892d0e8`
- AI-Verse-OS `main`: `64f7325444d18f94c9d4755d32eb89f3468bda6b`
- AI-Verse-Brain `main`: `69f7912eeb35f0178f6952ff0554aec8d7f2c496`
- AI-Verse-Memory `main`: `f1327be48ba2ee0043959021365e6dbb9dcb1d3a`
- AI-Verse-Skills `main`: `afde5c06307fba7d074de2929c2eb6c3dc6bdab8`
- AI-Verse-Data `main`: `f8978f8f7a1bc94edecddc2662112233289159a3`

Distribution and all five Core owner refs are unchanged from Slice 2.2. System advanced from Slice 2.2 closure `98773f6db85ac727a32ed798cf5113fe839e24a1` by one unrelated commit, `606bab362e68b3689f1d497849fc7dfc6545a934`, which modifies only `docs/SAFE-INFRASTRUCTURE-UPGRADE-AND-RECOVERY-IMPLEMENTATION-PLAN.md`. It is preserved unrelated concurrency and does not alter this program, Registry or release composition.

Fresh evidence used to bootstrap truthful dynamic State:

- current released/default Core composition: `ai-verse-distribution/release-sets/core-first-run-rc1-2026-10-12.json`;
- current durable Core release evidence: `ai-verse-distribution/qualification/core-update-program-u36/release-evidence.json`;
- the release set pins current OS, Brain, Memory, Skills and Data refs exactly to the live heads listed above;
- U35/U36 evidence remains released/pass, with member state preserved and reverse rollback to old stable not admitted;
- current component descriptors remain the known Slice 1.1 drift surface: OS descriptor is accepted for older revision `9600929b946746c25c64e48471fcc83031fddda9`; Brain/Memory/Skills/Data descriptors use `development` at older revisions and do not provide exact current owner-acceptance evidence.

This slice records those distinctions rather than relabeling descriptor truth or inferring acceptance from Distribution qualification.

Relevant mechanism classification:

- `contracts/repository-state.schema.json`: `CREATE`, versioned dynamic-state contract.
- `governance/repository-state.json`: `CREATE`, one canonical System dynamic-state source.
- `scripts/validate_repository_state.py`: `CREATE`, semantic validator following existing validator convention.
- `scripts/refresh_repository_state.py`: `CREATE` at the already-frozen single refresh/generation path. Slice 2.3 adds deterministic State-to-ledger rendering/checking only; Slice 3.1 will extend the same script with live scoped/full refresh logic rather than creating another engine.
- `docs/REPOSITORY-STATE-LEDGER.md`: `CREATE`, generated projection only.
- `docs/MAINTAINER-START-HERE.md`: `CREATE`, source-only governance entrypoint/read order/freshness guide.
- `.github/workflows/contract-validation.yml`: `EXTEND`, no parallel CI.
- second State database or hand-maintained dynamic Markdown: `RETIRE/NOT NEEDED`.

Final derived adaptive tasks:

1. **2.3.1 - Refresh Wave 1 refs/evidence, inspect existing surfaces and derive/refine Slice 2.3 tasks.** `COMPLETE`
2. **2.3.2 - Create the versioned Repository State schema and initial `governance/repository-state.json`, separating dynamic observations from Registry static truth and recording explicit scoped freshness, evidence availability, watchdog staleness and current open drift.** `NOT STARTED`
3. **2.3.3 - Create `scripts/validate_repository_state.py` plus positive/negative tests proving Registry/State identity binding, no static-field duplication, exact-ref semantics, unavailable-versus-failed evidence distinction, scoped freshness and fail-closed watchdog state.** `NOT STARTED`
4. **2.3.4 - Create the frozen `scripts/refresh_repository_state.py` path with deterministic ledger render/check mode, generate `docs/REPOSITORY-STATE-LEDGER.md`, and prove the Markdown ledger is reproducible projection only.** `NOT STARTED`
5. **2.3.5 - Create `docs/MAINTAINER-START-HERE.md` and minimal discoverability wiring so maintainers know the canonical read order, Registry/State/ledger authority boundaries, freshness rules and blocking-drift handling.** `NOT STARTED`
6. **2.3.6 - Extend existing Contract Validation CI, run/inspect real validation, refresh final refs/concurrency and close Slice 2.3/Phase 2 without runtime, release-composition, member-payload or protected-roadmap changes.** `NOT STARTED`

Protected-boundary check: PASS. This slice defines the already-frozen System control-plane surfaces only. It does not implement live repository fetching/watchdog scheduling, repair owner descriptors, change Distribution composition/promotion, modify component implementation or alter member payload. No plan amendment is required.

### Acceptance criteria

- one canonical dynamic Repository State exists at `governance/repository-state.json`;
- Registry static fields are not independently duplicated as State truth;
- State entries bind to registered repositories by stable `repository_id`;
- dynamic evidence can distinguish accepted, unverified, unavailable, failed and not-applicable states where relevant;
- scoped freshness is explicit and cannot be inferred from dates alone;
- watchdog has an explicit `WATCHDOG-STALE`/equivalent state so absent automation cannot masquerade as CLEAN;
- `docs/REPOSITORY-STATE-LEDGER.md` is deterministic generated projection only;
- maintainer entrypoint identifies canonical read order and refresh obligations;
- schema, semantic validation, tests and existing Contract Validation CI cover the new surfaces.

### NEXT

**Slice 3.1 - Scoped/full repository refresh and generated ledger.**

---

# Phase 3 - Build System self-checking machinery and synchronize current truth

**Phase size:** 3 slices

## Slice 3.1 - Scoped/full repository refresh and generated ledger

**Status:** NOT STARTED  
**Dependencies:** 2.3

Extend `scripts/refresh_repository_state.py` to consume Registry and exact Git/owner/Distribution evidence for scoped/full refreshes. Acceptance: deterministic/evidence-backed refresh, inaccessible repos explicit, dates informational only, generated ledger truthful, no member impact.

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

## 2026-10-12 - Slice 2.3 Repository State control-plane work started

- Refreshed System, Distribution and five Core owner refs before implementation.
- Confirmed no pre-existing Repository State schema/data, ledger, maintainer entrypoint or refresh/generation script exists.
- Reused the frozen single `scripts/refresh_repository_state.py` destination rather than creating a separate ledger generator; Slice 2.3 will establish deterministic rendering/checking and Slice 3.1 will extend the same implementation with live refresh.
- Confirmed current Core release-set and U36 evidence remain valid bootstrap evidence for dynamic shipped-pin state.
- Preserved unrelated concurrent System commit `606bab362e68b3689f1d497849fc7dfc6545a934`, which changes only the separate Safe Infrastructure plan.
- No protected roadmap change; no plan amendment required.

## 2026-10-12 - Slice 2.2 machine-readable Repository Registry completed

- Created versioned `ai-verse.repository-registry/v1` schema and the single System-owned `governance/repository-registry.json` authority.
- Registered System, Distribution, OS, Brain, Memory, Skills and Data as initial Wave 1 entries using stable GitHub repository IDs as logical identity anchors.
- Kept current `owner/name` as routing metadata and excluded live/dynamic state from Registry.
- Added semantic validation for identity uniqueness, shipping/profile/lifecycle/descriptor/acceptance rules, fail-closed unregistered participation and non-Registry Distribution authority.
- Added Registry tests and extended the existing Contract Validation workflow instead of creating parallel CI.
- GitHub Actions run `38256854398` passed on Python 3.11 and 3.13, including Registry validation and shared tests.
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
**Current slice:** Slice 2.3 - Define Repository State, generated ledger and maintainer entrypoint (`IN PROGRESS`)  
**Tasks:** 1/6  
**Next:** Task 2.3.2 - create the Repository State schema and initial dynamic State  
**Blockers/drift/amendments:** descriptor exact-owner-acceptance/evidence split remains BLOCKING for future Core release governance; Purpose Context Blueprint lag WARNING; Core maintainer handoff WARNING; Distribution hard-coded adapter compatibility knowledge WARNING; compact release receipt INFO/future work; U35/U36 RESOLVED/PASS. No plan amendment required.
