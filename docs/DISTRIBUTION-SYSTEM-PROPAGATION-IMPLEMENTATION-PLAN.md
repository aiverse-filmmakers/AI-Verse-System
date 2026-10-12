# AI-Verse Repository Network Governance, Release Safety and Self-Checking Implementation Plan

**Status:** ACTIVE  
**Canonical planning repo:** `aiverse-filmmakers/AI-Verse-System`  
**Primary implementation repo:** `aiverse-filmmakers/ai-verse-distribution`  
**Affected repos:** AI-Verse-System, ai-verse-distribution, all releasable AI-Verse component repositories  
**Started:** 2026-10-12  
**Program size:** 20 slices  
**Completed:** 7  
**Remaining:** 13  
**Overall progress:** 35.0%  
**Current execution phase:** Phase 3 - Build System self-checking machinery and synchronize current truth  
**Current phase progress:** 0/3 slices complete  
**Slices until next phase:** 3  
**Current slice:** 3.1 - Scoped/full repository refresh and generated ledger  
**Current slice status:** IN PROGRESS  
**Task progress:** 1/5  
**Next slice:** 3.2 - Drift Watchdog and heartbeat

> This file is the execution tracker. A slice is not COMPLETE until implementation, tests/evidence, tracker update and progress accounting are committed.

## Tracker history preservation

Verbose Phase 0/1 history is preserved at Slice 1.3 closure `acabfba8031421438747fed69bcbc65ba844787e`. Verbose Slice 2.1 history is preserved at closure `11940b87838afa0f46570ecdd8f8e00f74b7de5a`. Slice 2.2 detailed start state is preserved at `4e5b8b55a3f5227083daf72ec55d9fcaaef3a12f` and closure at `98773f6db85ac727a32ed798cf5113fe839e24a1`. Slice 2.3 detailed start state is preserved at `8cb5fbff630f45f730db904771333d73d5616a57`, closure bookkeeping at `fc0d178809867362dc29183411f26b9f65980903`, and final atomic State/ledger snapshot at `423e04917a9f1a9b4f012fa9daf4366fc8135e8c`. Compaction changes presentation only, never program laws, ownership, slice outcomes, acceptance criteria, ordering, denominator or evidence floors.

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
**Evidence:** this plan + `docs/ADAPTIVE-IMPLEMENTATION-PLANNING-SKILL.md`.

---

# Phase 1 - Audit and normalize current reality

**Status:** COMPLETE, 3/3

## Slice 1.1 - Audit live network and safety machinery

**Status:** COMPLETE  
**Evidence:** `docs/REPOSITORY-NETWORK-AUDIT-2026-10-12.md`, commit `08e593c9f3b74cae57ab5bf22dbebc33a2a6c176`.

## Slice 1.2 - Reuse/ownership/payload/drift inventory

**Status:** COMPLETE  
**Evidence:** `docs/REPOSITORY-NETWORK-REUSE-OWNERSHIP-INVENTORY-2026-10-12.md`, commit `8a45649276023ecc6626e5f8b25a76f0403c2912`.

## Slice 1.3 - Architecture freeze and Wave 1 acceptance matrix

**Status:** COMPLETE  
**Evidence:** `docs/REPOSITORY-NETWORK-IMPLEMENTATION-ARCHITECTURE-2026-10-12.md`, architecture commit `7450247a1d039bd6464e74e58babb6e80d90063a`, closure `acabfba8031421438747fed69bcbc65ba844787e`.

---

# Phase 2 - Define the canonical System control plane

**Status:** COMPLETE, 3/3

## Slice 2.1 - Repository-network governance, invariants and tombstones

**Status:** COMPLETE  
**Closure:** `11940b87838afa0f46570ecdd8f8e00f74b7de5a`.

Created `docs/REPOSITORY-NETWORK-GOVERNANCE-CONTRACT.md`, `docs/ARCHITECTURE-TOMBSTONES.md` and README discoverability.

## Slice 2.2 - Create the machine-readable Repository Registry

**Status:** COMPLETE  
**Closure:** `98773f6db85ac727a32ed798cf5113fe839e24a1`.

Created versioned `ai-verse.repository-registry/v1`, canonical seven-entry Wave 1 Registry, validation/tests and existing Contract Validation workflow coverage. Stable GitHub repository ID is logical identity; dynamic state is excluded; unregistered first-class release participation is fail-closed.

## Slice 2.3 - Define Repository State, generated ledger and maintainer entrypoint

**Status:** COMPLETE  
**Closure bookkeeping:** `fc0d178809867362dc29183411f26b9f65980903`  
**Final atomic State/ledger snapshot:** `423e04917a9f1a9b4f012fa9daf4366fc8135e8c`

Created `ai-verse.repository-state/v1`, canonical `governance/repository-state.json`, validator/tests, deterministic generated ledger, maintainer entrypoint and the single frozen `scripts/refresh_repository_state.py` path. Watchdog intentionally starts `WATCHDOG-STALE`. Final Contract Validation run `38260626280` passed Python 3.11 and 3.13.

---

# Phase 3 - Build System self-checking machinery and synchronize current truth

**Phase size:** 3 slices  
**Current phase progress:** 0/3

## Slice 3.1 - Scoped/full repository refresh and generated ledger

**Status:** IN PROGRESS  
**Dependencies:** 2.3  
**Task progress:** 1/5

### Starting evidence and refs

Fresh pre-implementation inspection on 2026-10-12 confirmed the Slice 2.3 final snapshot remains current and all six non-System Wave 1 repositories are unchanged:

- AI-Verse-System: `423e04917a9f1a9b4f012fa9daf4366fc8135e8c`
- ai-verse-distribution: `fd11b4a95487638d47ff55472a3703b03892d0e8`
- AI-Verse-OS: `64f7325444d18f94c9d4755d32eb89f3468bda6b`
- AI-Verse-Brain: `69f7912eeb35f0178f6952ff0554aec8d7f2c496`
- AI-Verse-Memory: `f1327be48ba2ee0043959021365e6dbb9dcb1d3a`
- AI-Verse-Skills: `afde5c06307fba7d074de2929c2eb6c3dc6bdab8`
- AI-Verse-Data: `f8978f8f7a1bc94edecddc2662112233289159a3`

Existing surfaces inspected and classified:

- `scripts/refresh_repository_state.py`: **EXTEND** as the one refresh/projection engine. No second refresh tool.
- `governance/repository-registry.json`: **REUSE** as static identity/scope/routing input.
- `contracts/repository-state.schema.json` + `scripts/validate_repository_state.py`: **REUSE**, extend only if implementation proves a missing state fact.
- `docs/REPOSITORY-STATE-LEDGER.md`: **REUSE** as generated projection only.
- Component `release/component-release.json` + canonical descriptor validator: **REUSE** for descriptor/owner-acceptance observation. Do not create another acceptance format.
- Distribution `release-sets/`: **REUSE** for exact shipped pins/current default released composition. No second promotion or pin database.
- Existing Contract Validation workflow: **EXTEND** for refresh tests/live dry-run if reliable; do not create watchdog scheduling before Slice 3.2.

The current default released Core set remains `release-sets/core-first-run-rc1-2026-10-12.json`, with exact pins matching all five current Core heads. Current descriptor drift remains unchanged: OS describes older accepted revision `9600929b946746c25c64e48471fcc83031fddda9`; Brain/Memory/Skills/Data describe older `development` revisions.

### Derived task list

1. **3.1.1 - Refresh live Wave 1 refs, reread plan/skill/architecture, inspect current refresh/State/Registry/descriptor/Distribution surfaces and derive the execution tasks.** `COMPLETE`
2. **3.1.2 - Extend the single `scripts/refresh_repository_state.py` engine with deterministic Registry-derived scope resolution and live GitHub evidence collection for stable repository identity, exact default-branch HEAD, exact descriptor-at-HEAD observation, canonical descriptor owner-acceptance evaluation and exact Distribution default released pins. Fail closed on ambiguity, access loss, fetch failure or System publication concurrency.** `IN PROGRESS`
3. **3.1.3 - Extend refresh tests with injected/fake evidence to prove component/Core/Agent/Full/global scope selection, exact-ref behavior, accepted-vs-unverified owner evidence, exact Distribution pin selection, unavailable-vs-failed handling, deterministic output and no timestamp lineage authority.** `PENDING`
4. **3.1.4 - Extend maintainer/CI usage so the existing validation path exercises a real read-only Core refresh dry-run without writing sibling repositories, while State/ledger write mode remains explicit and source-only.** `PENDING`
5. **3.1.5 - Perform a real Core refresh, publish the refreshed State plus generated ledger atomically from an exact pre-publication System head, run final validation/CI, refresh concurrency/refs and close Slice 3.1 without watchdog scheduling, drift auto-reconciliation, runtime/member-payload or protected-roadmap changes.** `PENDING`

### Acceptance floor

- scoped decisions refresh only their required Registry-derived scope;
- full/global refresh can cover all registered repositories without a second engine;
- repository identity is verified against stable GitHub repository ID, not inferred from path/name;
- exact immutable refs and exact-at-ref descriptor/release evidence are used;
- canonical descriptor validation may prove an accepted descriptor revision, but Distribution qualification is never converted into owner acceptance;
- inaccessible evidence is explicit and distinct from executed checks that fail;
- ambiguous/multiple current Distribution pins fail closed rather than selecting by date or filename;
- dates remain informational only and cannot establish freshness/lineage;
- State publication detects System-head concurrency rather than silently overwriting fresher work;
- generated ledger remains projection only;
- no sibling repository writes, runtime behavior, release composition or member payload changes occur;
- no plan amendment is currently required.

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

## 2026-10-12 - Slice 3.1 started

- Refreshed System, Distribution and all five Core heads before implementation; no Wave 1 ref moved since the Slice 2.3 final snapshot.
- Re-read the adaptive planning method, architecture freeze, State/Registry control plane, descriptor contract and current Distribution default Core release set.
- Classified the existing refresh script as EXTEND and all Registry/State/descriptor/Distribution authority surfaces as REUSE-first.
- Derived five evidence-backed tasks with no plan amendment and no new competing source of truth.

## 2026-10-12 - Slice 2.3 Repository State control plane completed

- Created versioned `ai-verse.repository-state/v1`, canonical `governance/repository-state.json`, fail-closed validator/tests, deterministic generated ledger, maintainer entrypoint and single frozen refresh/projection path.
- Final atomic State/ledger snapshot: `423e04917a9f1a9b4f012fa9daf4366fc8135e8c`.
- Final GitHub Actions run `38260626280` passed Python 3.11 and 3.13.
- No runtime, component, Distribution composition or member payload changed.

## 2026-10-12 - Slice 2.2 machine-readable Repository Registry completed

- Created versioned Registry and canonical seven-entry Wave 1 Registry with validation/tests and existing CI coverage.
- Closure: `98773f6db85ac727a32ed798cf5113fe839e24a1`.

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

**Completed:** 7/20  
**Overall:** 35.0%  
**Phase:** Phase 3 - Build System self-checking machinery and synchronize current truth  
**Phase progress:** 0/3  
**Until Phase 4:** 3 slices  
**Current slice:** Slice 3.1 - Scoped/full repository refresh and generated ledger (`IN PROGRESS`)  
**Tasks:** 1/5  
**Current task:** 3.1.2 - Extend the single refresh engine with live scoped/full exact-evidence collection  
**Next:** complete 3.1 before starting 3.2  
**Blockers/drift/amendments:** descriptor exact-owner-acceptance/evidence split remains BLOCKING for future Core release governance; Purpose Context Blueprint lag WARNING; Core maintainer handoff WARNING; Distribution hard-coded adapter compatibility knowledge WARNING; compact release receipt INFO/future work; watchdog WARNING/STALE until Slice 3.2; U35/U36 RESOLVED/PASS. No plan amendment required.