# AI-Verse Repository Network Governance, Release Safety and Self-Checking Implementation Plan

**Status:** ACTIVE  
**Canonical planning repo:** `aiverse-filmmakers/AI-Verse-System`  
**Primary implementation repo:** `aiverse-filmmakers/ai-verse-distribution`  
**Affected repos:** AI-Verse-System, ai-verse-distribution, all releasable AI-Verse component repositories  
**Started:** 2026-10-12  
**Program size:** 20 slices  
**Completed:** 9  
**Remaining:** 11  
**Overall progress:** 45.0%  
**Current execution phase:** Phase 3 - Build System self-checking machinery and synchronize current truth  
**Current phase progress:** 2/3 slices complete  
**Slices until next phase:** 1  
**Current slice:** 3.3 - Reconcile current System truth and known drift  
**Current slice status:** NOT STARTED  
**Next slice:** 4.1 - Extend/reuse Component Release Descriptor

> This file is the execution tracker. A slice is not COMPLETE until implementation, tests/evidence, tracker update, required canonical State/ledger publication and progress accounting are committed.

## Tracker history preservation

Phase 0/1 detail is preserved at Slice 1.3 closure `acabfba8031421438747fed69bcbc65ba844787e`. Slice 2.1 closure is `11940b87838afa0f46570ecdd8f8e00f74b7de5a`. Slice 2.2 start/closure are `4e5b8b55a3f5227083daf72ec55d9fcaaef3a12f` and `98773f6db85ac727a32ed798cf5113fe839e24a1`. Slice 2.3 start/closure/final State snapshot are `8cb5fbff630f45f730db904771333d73d5616a57`, `fc0d178809867362dc29183411f26b9f65980903` and `423e04917a9f1a9b4f012fa9daf4366fc8135e8c`. Slice 3.1 start/final State snapshot/final CI are `dbe13e49d84176131e0447785a4748951a17ad8e`, `28ae533e7c2acb2ab155fa7d7cd11f10afd4c9f2` and run `38279213073`. Slice 3.2 implementation commits and evidence are recorded below. Compaction changes presentation only, never program laws, ownership, slice outcomes, acceptance criteria, ordering, denominator or evidence floors.

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

## Slice 2.2 - Create the machine-readable Repository Registry

**Status:** COMPLETE  
**Closure:** `98773f6db85ac727a32ed798cf5113fe839e24a1`.

## Slice 2.3 - Define Repository State, generated ledger and maintainer entrypoint

**Status:** COMPLETE  
**Closure bookkeeping:** `fc0d178809867362dc29183411f26b9f65980903`  
**Final State/ledger snapshot:** `423e04917a9f1a9b4f012fa9daf4366fc8135e8c`  
**Final CI:** run `38260626280`, Python 3.11 and 3.13 passed.

---

# Phase 3 - Build System self-checking machinery and synchronize current truth

**Phase size:** 3 slices  
**Current phase progress:** 2/3

## Slice 3.1 - Scoped/full repository refresh and generated ledger

**Status:** COMPLETE  
**Dependencies:** 2.3  
**Tasks:** 5/5 complete  
**Final State/ledger:** `28ae533e7c2acb2ab155fa7d7cd11f10afd4c9f2`  
**Final CI:** run `38279213073`, Python 3.11 and 3.13 passed.

The one System-owned refresh engine now performs Registry-derived component/Core/Agent/Full/global exact-ref observation. Distribution qualification never substitutes for owner acceptance; ambiguity/access/fetch failure fails visibly; the ledger remains projection only; System publication concurrency is rejected.

## Slice 3.2 - Drift Watchdog and heartbeat

**Status:** COMPLETE  
**Dependencies:** 3.1  
**Tasks:** 6/6 complete

### Outcome

A single daily/manual Repository Drift Watchdog now wraps the existing refresh engine rather than creating a second discovery/comparison system. It performs Registry-derived global scans, records successful heartbeat evidence in Repository State, distinguishes failed and stale watchdog conditions, preserves unrelated drift, never writes sibling repositories, never changes release pins or promotion, and publishes only System State + generated ledger with exact-head/concurrency-safe behavior.

The existing v1 Repository State contract proved sufficient for the frozen watchdog semantics, so task 3.2.2 was completed by **REUSE** rather than unnecessary schema expansion. `refresh.last_full_refresh` records the full attempt, per-repository State records access/descriptor/pin evidence, and `watchdog.last_successful_full_scan` plus watchdog status records the successful heartbeat/failure transition. This adaptive reduction changed technique only, not the acceptance destination.

### Task record

1. **3.2.1 - Refresh state, reread plan/adaptive method/frozen architecture/governance, inspect State/refresh/CI/tests and derive tasks.** `COMPLETE`
2. **3.2.2 - Prove and use the minimal State facts required for heartbeat/attempt/failure semantics.** `COMPLETE`, existing State v1 reused; no schema expansion required.
3. **3.2.3 - Add watchdog transitions around the same global refresh engine.** `COMPLETE`, `scripts/run_repository_watchdog.py`.
4. **3.2.4 - Prove complete/failed/stale/missed-window/scoped-isolation/unrelated-drift semantics.** `COMPLETE`, watchdog + State tests.
5. **3.2.5 - Add daily/manual least-privilege System-only watchdog workflow and maintainer usage.** `COMPLETE`, `.github/workflows/repository-drift-watchdog.yml` and maintainer docs.
6. **3.2.6 - Run and publish a real full-network heartbeat, validate the exact implementation and close.** `COMPLETE`; final State/ledger publication follows this closure bookkeeping commit as the direct child snapshot.

### Evidence

- Watchdog orchestration + transition tests: `e79aba5a70f0ea357384be890676558cbb5d7a42`
- Daily/manual workflow + maintainer docs: `7a54cea11fc6fac160cc2c8e62bc262e5f335e72`
- First real heartbeat snapshot: `3e4ccd7ec245f425832b61dd56f72b51b2736eb2`, direct child of exact observed System head `7a54cea11fc6fac160cc2c8e62bc262e5f335e72`
- First heartbeat correctly observed Distribution movement to `90f175418f8d13faeece8bcb1ad0796d2adecfb1`; its two intervening commits changed only the transition contract document and its test. The default released Core set remained released/default and retained the same five exact Core pins.
- First heartbeat State and ledger both validated, but Contract Validation run `38280880766` exposed five tests that incorrectly assumed the canonical State would remain permanently bootstrap-stale/global-inactive. This failure was not hidden.
- Fixture correction: `c2d41e58eb68f343bb30769435b07b7061bb040c`. No production watchdog code changed.
- Corrected Contract Validation run `38281202375`: 95 tests passed on Python 3.11 and 3.13; Python 3.11 live read-only Core refresh passed.
- Final heartbeat State/ledger snapshot: direct child of this closure bookkeeping revision, changing only `governance/repository-state.json` and `docs/REPOSITORY-STATE-LEDGER.md`.

### Frozen operational behavior

- Schedule: once daily at `.github/workflows/repository-drift-watchdog.yml`, plus manual dispatch.
- One refresh engine: `scripts/refresh_repository_state.py`; watchdog orchestration calls it with Registry-derived global scope.
- Successful complete full scan -> `WATCHDOG-CURRENT` with exact heartbeat revision and timestamped successful full-scan record.
- First unsuccessful expected full scan after CURRENT -> `WATCHDOG-FAILED`.
- Second consecutive unsuccessful expected scan, or an inferred missed expected daily window plus failed attempt -> `WATCHDOG-STALE`.
- A persisted CURRENT heartbeat at least two expected daily windows old is operationally not current even if no runner was available to write a transition.
- Scoped refreshes preserve global watchdog truth and may satisfy scoped freshness where governance permits.
- Watchdog-specific drift is changed independently; unrelated drift is preserved.
- Workflow token is scoped to the System repository. A hard path guard permits only State + ledger changes. Normal non-force push makes concurrent movement fail rather than overwrite.

### Drift disposition

The former global `repository-watchdog-stale` warning is resolved by the successful full heartbeat. Existing non-watchdog drift remains unchanged: exact Core owner-acceptance gap `BLOCKING`; Purpose Context Blueprint lag `WARNING`; Core maintainer handoff `WARNING`; Distribution adapter shadow risk `WARNING`; compact release receipt `INFO`. No plan amendment was required.

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

## 2026-10-12 - Slice 3.2 Drift Watchdog completed

- Reused the existing State v1 contract after evidence showed no new schema fields were needed.
- Added watchdog orchestration and tests at `e79aba5a70f0ea357384be890676558cbb5d7a42`.
- Added daily/manual System-only workflow and maintainer documentation at `7a54cea11fc6fac160cc2c8e62bc262e5f335e72`.
- First heartbeat `3e4ccd7ec245f425832b61dd56f72b51b2736eb2` proved real Distribution-head movement could be recorded without changing released Core pins.
- First-heartbeat CI exposed stale bootstrap fixture assumptions; those tests were corrected at `c2d41e58eb68f343bb30769435b07b7061bb040c` without production changes.
- Corrected run `38281202375` passed 95 tests on Python 3.11 and 3.13 plus the live Core refresh.
- Final canonical heartbeat snapshot is published as the direct child of this bookkeeping revision.
- No protected roadmap change and no plan amendment.

## 2026-10-12 - Slice 3.1 scoped/full refresh completed

Final State/ledger `28ae533e7c2acb2ab155fa7d7cd11f10afd4c9f2`; final CI run `38279213073` passed.

## 2026-10-12 - Slice 2.3 Repository State control plane completed

Final State/ledger `423e04917a9f1a9b4f012fa9daf4366fc8135e8c`; final CI run `38260626280` passed.

## 2026-10-12 - Slice 2.2 Repository Registry completed

Closure `98773f6db85ac727a32ed798cf5113fe839e24a1`.

## 2026-10-12 - Slice 2.1 permanent governance completed

Closure `11940b87838afa0f46570ecdd8f8e00f74b7de5a`.

## 2026-10-12 - Phase 1 completed and architecture frozen

Closure `acabfba8031421438747fed69bcbc65ba844787e`.

---

# Current execution pointer

**Completed:** 9/20  
**Overall:** 45.0%  
**Phase:** Phase 3 - Build System self-checking machinery and synchronize current truth  
**Phase progress:** 2/3  
**Until Phase 4:** 1 slice  
**Current slice:** Slice 3.3 - Reconcile current System truth and known drift (`NOT STARTED`)  
**Next:** start Slice 3.3 with a fresh relevant State read and evidence-first reconciliation task derivation  
**Blockers/drift/amendments:** Core exact-owner-acceptance gap BLOCKING; Purpose Context lag WARNING; Core maintainer handoff WARNING; Distribution adapter shadow-risk WARNING; compact release receipt INFO; watchdog CURRENT. No plan amendment required.
