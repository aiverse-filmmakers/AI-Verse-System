# AI-Verse Repository Network Implementation Architecture Freeze

**Status:** COMPLETE SLICE 1.3 EVIDENCE  
**Program:** `docs/DISTRIBUTION-SYSTEM-PROPAGATION-IMPLEMENTATION-PLAN.md`  
**Slice:** 1.3 - Freeze the implementation architecture and acceptance matrix  
**Scope:** AI-Verse-System, ai-verse-distribution, and Wave 1/Core owners: OS, Brain, Memory, Skills and Data  
**Source inventory:** `docs/REPOSITORY-NETWORK-REUSE-OWNERSHIP-INVENTORY-2026-10-12.md`  
**Date:** 2026-10-12

This document freezes the implementation architecture that later slices must build. It is Phase 1 design evidence, not the permanent governance contract. Slice 2.1 will create the permanent law surface from these frozen decisions.

The governing rule remains:

> **Define centrally. Enforce at the canonical owner. Verify again at composition.**

No product/runtime behavior is changed by this document.

---

## 1. Fresh state used for the freeze

Observed refs when Slice 1.3 began:

| Repository | Ref |
|---|---|
| AI-Verse-System | `27e21a1e519a17ae79f98d977ffcdac1b63c4436` |
| ai-verse-distribution | `fd11b4a95487638d47ff55472a3703b03892d0e8` |
| AI-Verse-OS | `64f7325444d18f94c9d4755d32eb89f3468bda6b` |
| AI-Verse-Brain | `69f7912eeb35f0178f6952ff0554aec8d7f2c496` |
| AI-Verse-Memory | `f1327be48ba2ee0043959021365e6dbb9dcb1d3a` |
| AI-Verse-Skills | `afde5c06307fba7d074de2929c2eb6c3dc6bdab8` |
| AI-Verse-Data | `f8978f8f7a1bc94edecddc2662112233289159a3` |

The five Core owner refs and Distribution ref are unchanged from Slice 1.2.

System moved concurrently after the initial refresh. The first observed move from Slice 1.2 closure `bd3f5a4bc14d88ab5076b74b1226512728b327e0` to `27e21a1e519a17ae79f98d977ffcdac1b63c4436` changed only `docs/SAFE-INFRASTRUCTURE-UPGRADE-AND-RECOVERY-IMPLEMENTATION-PLAN.md`. A second direct descendant `e843d5533ea8ec3367ac57b5a6afde8bac357002` changed only the same unrelated plan. The Slice 1.3 start commit `819f87aa111aaf6c7c0401e658b4420934a9f4e4` was based on that newer parent. Neither concurrent change alters this program, the Slice 1.2 inventory, the repository-network contracts, or the Core composition.

Current Distribution evidence remains:

- production Core release: `release-sets/core-first-run-rc1-2026-10-12.json`;
- U35 exact transition/member qualification: `qualification/core-update-program-u35/qualification.json`;
- U36 durable release evidence: `qualification/core-update-program-u36/release-evidence.json`;
- current Core forward release/update program: complete and released;
- current reverse rollback to `core-stable-2026-10-10`: not admitted because exact reverse preservation qualification does not exist.

---

## 2. Frozen control-plane ownership and paths

### 2.1 System-owned permanent and machine surfaces

The following target paths are frozen for later implementation:

| Concern | Canonical owner | Frozen target path | Rule |
|---|---|---|---|
| Repository-network permanent governance | AI-Verse-System | `docs/REPOSITORY-NETWORK-GOVERNANCE-CONTRACT.md` | Permanent law, created in Slice 2.1. References existing safety contracts instead of copying them. |
| Architecture tombstones | AI-Verse-System | `docs/ARCHITECTURE-TOMBSTONES.md` | Durable architecture history. Not dynamic repository state. |
| Repository Registry schema | AI-Verse-System | `contracts/repository-registry.schema.json` | Versioned static registry contract. |
| Repository Registry data | AI-Verse-System | `governance/repository-registry.json` | One canonical global static repository registry. |
| Repository State schema | AI-Verse-System | `contracts/repository-state.schema.json` | Versioned dynamic-state contract. |
| Repository State data | AI-Verse-System | `governance/repository-state.json` | One canonical dynamic repository-state source. |
| Human state ledger | AI-Verse-System | `docs/REPOSITORY-STATE-LEDGER.md` | Generated projection only. Never hand-maintained as machine truth. |
| Maintainer entrypoint | AI-Verse-System | `docs/MAINTAINER-START-HERE.md` | Required read order and freshness entrypoint. |
| Registry validator | AI-Verse-System | `scripts/validate_repository_registry.py` | Follows current System validator convention. |
| State validator | AI-Verse-System | `scripts/validate_repository_state.py` | Follows current System validator convention. |
| State refresh and ledger generation | AI-Verse-System | `scripts/refresh_repository_state.py` | One shared implementation for scoped/full refresh and ledger generation. |
| Drift watchdog workflow | AI-Verse-System | `.github/workflows/repository-drift-watchdog.yml` | Calls the same refresh/state machinery. Must not create a second comparison engine or state database. |
| Contract/schema CI | AI-Verse-System | existing `.github/workflows/contract-validation.yml` | Extend existing validation workflow for new schemas/contracts where appropriate rather than duplicate validation logic. |

`governance/` is frozen as the System machine control-plane data directory. It holds machine governance truth such as Registry and Repository State. Human-readable policy remains in `docs/`; schemas remain in `contracts/`; executable maintainer tooling remains in `scripts/`; scheduled automation remains under `.github/workflows/`.

### 2.2 No duplicate System truth

The following are explicitly prohibited target patterns:

- a second Registry in Distribution;
- a second Repository State database in Distribution;
- hand-maintained dynamic state in Markdown;
- a separate watchdog state database;
- copying Registry static fields into Repository State as separately maintained truth;
- using dates as lineage authority;
- allowing a generated ledger to become an editable canonical state source.

Distribution may consume the exact relevant Registry/State evidence for qualification, but that snapshot is immutable qualification evidence, not an editable competing authority.

---

## 3. Registry and Repository State boundary

### 3.1 Repository Registry contains stable/declarative truth

Registry entries must contain only stable or intentionally declared facts such as:

- stable GitHub repository ID;
- current `owner/name`;
- canonical component ID;
- canonical responsibility/owner domain;
- lifecycle classification: active, experimental, retired or external;
- release-profile participation;
- whether Distribution ships the component;
- expected component release descriptor path;
- expected owner CI/acceptance discovery surface;
- System spec/ownership references;
- source/member classification where useful;
- direct compatibility dependencies only where canonically known.

Registry must not contain current live HEAD, current accepted revision, current Distribution pin, current CI outcome, last refresh, current drift or watchdog heartbeat.

### 3.2 Repository State contains observed/dynamic truth

Repository State must contain dynamic facts such as:

- observed live HEAD/ref;
- owner-accepted revision and exact evidence reference;
- Distribution-pinned revision and release ID;
- System synchronization checkpoint/status;
- observed descriptor revision/status;
- last scoped refresh;
- last full refresh;
- access-unverified state;
- watchdog heartbeat/freshness;
- drift severity, scope, reason, relevant refs and required action;
- unavailable evidence versus failed evidence;
- immutable references to supporting evidence rather than copies of owner truth.

The generated ledger joins Registry labels/identity with Repository State observations for humans. It does not become a third source of truth.

---

## 4. Frozen refresh rules

### 4.1 Scoped refresh is the normal decision path

A decision must refresh only the repositories and evidence required by its scope.

Frozen minimum scopes:

| Decision | Minimum refresh scope |
|---|---|
| Single component candidate | Component owner + Distribution + relevant System governance/Registry/State + declared direct dependencies |
| Core release | System + Distribution + OS + Brain + Memory + Skills + Data |
| Agent release | System + Distribution + active Agent-profile repos + required Core dependencies |
| Full release | System + Distribution + every active shipped repo in the target Full profile |
| Architecture/network watchdog | Full registered-repository scan |

A full network scan before every component change is prohibited unless a specific contract requires it.

### 4.2 Exact identity and ancestry

Refresh uses:

- stable repository identity;
- exact immutable Git refs;
- Git ancestry/compare evidence where lineage matters;
- owner acceptance evidence for the exact revision;
- Distribution exact release refs;
- System synchronization evidence.

Dates are context/display only.

### 4.3 Candidate freshness binding

Every candidate qualification freezes the exact state/evidence used. If any bound input changes, the previous qualification cannot silently carry forward.

Before final admission, Distribution must either:

1. perform a fresh scoped refresh and freeze its result, or
2. prove that every already-frozen bound input remains exactly unchanged.

---

## 5. Drift and release-blocking rules

Every drift record carries:

```text
severity: INFO | WARNING | BLOCKING
scope: component | Core | Agent | Full | global
reason
relevant refs
required action
```

Blocking is the intersection of severity and release scope. `BLOCKING` drift blocks an admission when its scope intersects the candidate/release scope, or when the drift is global. INFO and WARNING do not automatically block unrelated releases.

Frozen classifications for important conditions:

| Condition | Default severity | Scope behavior | Release effect |
|---|---|---|---|
| Required owner acceptance missing for exact candidate ref | BLOCKING | component and containing profile | Blocks adoption/admission |
| Required owner evidence inaccessible/unverified | BLOCKING | candidate scope | Required evidence unavailable is not CLEAN |
| Candidate component ref differs from bound accepted ref | BLOCKING | component/profile | Blocks qualification/admission |
| Unregistered first-class component enters release composition | BLOCKING | target profile | Blocks composition |
| Whole-release preservation failure | BLOCKING | target release/profile | Blocks promotion |
| Member governance leakage into member payload | BLOCKING | target release/global safety | Blocks release |
| Breaking owner contract without accepted migration/version path | BLOCKING | affected component/profile | Blocks composition/promotion |
| Required candidate snapshot changed after qualification | BLOCKING | target release | Requalification required |
| Durable release receipt missing at final admission | BLOCKING | target release | Candidate testing may continue, final promotion may not |
| System architecture/product wording stale versus accepted implementation | WARNING unless governing contract semantics are unsafe | relevant System/profile scope | Freezes automatic correction; does not automatically revert accepted implementation |
| Hard-coded Distribution adapter knowledge not yet contract-bound | WARNING | affected component/profile | Track and constrain; becomes BLOCKING only if it is used as the sole acceptance authority |
| Non-release documentation lag | INFO or WARNING | narrow scope | Does not block unrelated release |
| Watchdog stale | WARNING globally by default | global maintenance state | May become BLOCKING for admission if required freshness cannot be satisfied by a valid fresh scoped refresh |

The current Purpose Context Blueprint lag remains WARNING and cannot cause automatic rollback. The current descriptor exact-owner-acceptance gap remains BLOCKING for future owner-adoption governance until repaired under the existing descriptor contract path.

### 5.1 Watchdog heartbeat

The System watchdog architecture is frozen as:

- scheduled full registered-repository scan once per day;
- manual dispatch available for maintainers;
- safe event-triggered scans may be added later only if they reuse the same refresh implementation;
- `WATCHDOG-STALE` after two consecutive expected daily full scans are missed or fail to produce a successful full heartbeat;
- heartbeat is stored inside Repository State, not a second database;
- heartbeat records watchdog version/ref, last successful full scan, scanned registered repos and any access/fetch failures;
- watchdog uses least-privilege read/validation authority by default and must not require a broad cross-repo write token;
- watchdog never silently rewrites sibling repositories or promotes releases.

A fresh scoped release refresh may satisfy release-local freshness even while the global watchdog is WARNING-stale, unless the candidate depends on a global fact that could not be proven from the scoped refresh. Missing required evidence always fails closed.

---

## 6. Component release descriptor architecture

The existing Component Release Descriptor remains the only canonical component release/compatibility metadata format.

Frozen rule:

- System owns the contract/schema semantics;
- each component owner publishes its own descriptor tied to an exact immutable owner revision;
- component owner acceptance evidence must identify the exact accepted candidate revision;
- later extensions may add only evidence-backed compatibility fields such as interface/contract generation, state-schema generation, required contract ranges, breaking-change classification, migration requirements and owner-declared direct compatibility dependencies;
- descriptor metadata never becomes live runtime health, readiness or authority truth;
- Distribution consumes the descriptor and acceptance evidence but does not create an independent component acceptance record.

A second compatibility fingerprint format remains prohibited.

Current Wave 1 descriptors do not yet satisfy this exact-ref acceptance architecture for the currently shipped refs. Slice 1.3 freezes the target architecture but does not rewrite or retroactively relabel those descriptors. Historical shipped-release evidence remains historical evidence. Future owner adoption must pass the exact-ref rule once the planned descriptor/handoff work lands.

---

## 7. Distribution candidate, qualification and promotion architecture

Distribution already has the correct release-composition skeleton and must be extended, not replaced.

Existing authorities retained:

- `release-sets/` for exact release composition;
- `compatibility/` and catalog compatibility for release-set composition/update/rollback admission;
- `.qualification/` for immutable staged/snapshotted qualification inputs where needed;
- `qualification/` for durable candidate/release qualification evidence;
- existing Core candidate overlay, forward lineage/promotion ledger and channel selection in the Distribution catalog;
- existing install/update/rollback, lifecycle recovery and state-preservation machinery.

### 7.1 Immutable candidate evidence snapshot

Frozen canonical path:

`qualification/<candidate-or-release-id>/candidate-evidence.json`

It must bind, as applicable:

- exact Distribution candidate revision;
- exact System governance/contract revision used;
- exact Registry revision/blob or commit-bound content identity;
- exact scoped Repository State evidence/ref used for the decision;
- exact component repository refs;
- exact component descriptor refs/digests;
- exact owner acceptance evidence refs;
- compatibility/migration metadata refs;
- whole-release preservation evidence refs as they become available;
- dependency locks/toolchain/runtime facts required for reproduction;
- drift results relevant to the candidate scope.

This file is qualification evidence, not a second release set and not a second Registry/State authority.

### 7.2 Promotion model

Do not invent a parallel promotion subsystem or ceremonial rings unsupported by Distribution.

Frozen conceptual progression:

```text
owner accepted exact ref
-> Distribution explicit candidate
-> qualification, including any dogfood/canary/limited evidence actually supported
-> released/admitted release set
-> current/default channel where policy allows
```

Dogfood/canary/limited validation may be evidence inside qualification. It does not require a new canonical release status unless Distribution later gains a real operational state that needs one.

The existing candidate overlay remains an explicit qualification target. Once promoted, a candidate leaves the overlay and enters the forward promotion/lineage machinery. Exact release-set composition remains canonical shipped composition truth.

---

## 8. Durable release receipt and reproducibility

Do not create a second release database.

Frozen canonical receipt path for future admitted releases:

`qualification/<release-id>/release-receipt.json`

The corresponding release set should reference the receipt from its evidence section once implemented.

The receipt is a compact immutable binding of evidence. It does not replace `release-sets/<release-id>.json` as composition truth.

Minimum receipt contents where applicable:

- release ID;
- exact Distribution revision;
- exact release-set path/content identity;
- exact component revisions/artifacts;
- component descriptor revisions/digests;
- owner acceptance evidence refs;
- System governance contract ref;
- Registry ref;
- Repository State/candidate refresh evidence ref;
- dependency locks/toolchain/runtime facts;
- migration/compatibility classification;
- qualification and preservation result refs;
- promotion channel/current status;
- previous known-good release reference;
- emergency/sync-debt state if applicable.

The receipt must not contain member private content, user-owned state or secrets. Software reconstruction and user-state rollback remain separate concerns.

Existing task-specific historical `release-evidence.json` files remain valid historical evidence. The target `release-receipt.json` consolidates the future admitted-release reconstruction binding without rewriting history.

---

## 9. Emergency safety release architecture

System defines permanent emergency policy in Slice 2.1. Distribution enforces it through the same candidate, qualification, preservation and promotion machinery used by normal releases.

Emergency eligibility is limited to urgent security, corruption or user-data-protection fixes.

Break-glass may not bypass:

- canonical owner validation;
- exact immutable refs;
- owner acceptance evidence;
- compatibility/migration requirements;
- state preservation;
- Distribution whole-product qualification;
- member isolation.

The only allowed temporary debt is non-safety System documentation synchronization debt explicitly recorded as `SYSTEM-SYNC-DEBT` in candidate/release evidence. Any later normal promotion is blocked until required sync debt is reconciled.

Emergency is therefore a bounded policy path through existing release machinery, not a separate updater or promotion system.

---

## 10. Member payload boundary

The target member boundary reuses and strengthens current Distribution behavior.

Source/maintainer-only by default:

- Repository Registry/State/Ledger;
- watchdog/drift reports and heartbeat;
- architecture tombstones;
- repository-network governance contracts and plans;
- audit/inventory/architecture-freeze evidence;
- owner maintainer handoff instructions;
- qualification snapshots/results/receipts;
- internal promotion/lineage governance;
- System contract snapshots used for qualification;
- Distribution maintenance scripts/tests.

Member/runtime only when explicitly admitted:

- admitted product/runtime artifacts;
- owner runtime adapters installed through canonical lifecycle;
- product-facing generated `AGENTS.md`, `CLAUDE.md`, `AI-VERSE.yaml` where they are part of the member product contract;
- narrow Distribution bootstrap extension/helper already owned by Distribution;
- canonical user/owner runtime state.

The implementation rule is deterministic inclusion, not broad copy then delete.

User/local files must never be deleted because their filename resembles an internal governance filename. Generated member files may be refreshed only when ownership/receipt evidence proves Distribution owns that generated file and local edits are unambiguous. Ambiguity fails closed.

---

## 11. Architecture tombstone format

Canonical target: `docs/ARCHITECTURE-TOMBSTONES.md` in System.

The permanent contract in Slice 2.1 will define semantics. The tombstone ledger itself records durable entries.

Each tombstone entry must carry at least:

- tombstone ID;
- date;
- status: retired, replaced or prohibited-resurrection;
- affected architecture/surface;
- superseded refs/paths;
- replacement architecture/ref;
- reason and evidence;
- compatibility/migration impact;
- cleanup obligations if any;
- canonical owner;
- relevant release/qualification refs;
- resurrection condition, default `none` unless explicitly approved.

System owns cross-system architecture tombstones. Component-local tombstones exist only when needed for a component-owned local API/schema/migration and must not become a competing global architecture history.

---

## 12. Rollout wave gates

Rollout order remains:

1. **Wave 1:** System + Distribution + Core: OS, Brain, Memory, Skills, Data.
2. **Wave 2:** Registry-confirmed active Agent-profile repos such as Gateway, Automations, Multiple Bots and actual dependencies discovered by Registry.
3. **Wave 3:** Registry-confirmed active Full/future repos such as Connections, Apps, Dashboard, Token and future first-class repos.

Frozen gate:

- Wave 1 must prove the full pattern end to end before the governance/handoff pattern is propagated to Wave 2;
- Wave 2/3 participation is Registry-driven, not based on guessed repository names;
- experimental, retired or external repos are not silently treated as shippable;
- no unregistered first-class repo can enter an admitted release;
- later waves may adapt file layout per repository, but cannot weaken the semantic owner/acceptance/handoff rules proven in Wave 1.

---

## 13. Core Wave 1 acceptance matrix

A future Wave 1 release is admissible only when the applicable row passes for every component/release in scope.

| Gate | Canonical evidence owner | Pass condition | Failure effect |
|---|---|---|---|
| Registered identity/role | System Registry | Stable repo identity, component ID, lifecycle/profile role and ownership valid | BLOCKING |
| Live repository observation | System Repository State | Exact live ref observed or explicit access failure recorded | Required access failure is BLOCKING for candidate scope |
| Owner descriptor validity | Component owner under System descriptor contract | Descriptor validates and identifies exact candidate revision | BLOCKING |
| Owner native acceptance | Component owner | Native CI/acceptance evidence passes for exact candidate revision | BLOCKING |
| Owner compatibility/migration metadata | Component owner | Required compatibility generations/ranges/migrations are valid | BLOCKING when relevant |
| System governance ref | System | Exact governing contract/Registry ref frozen for candidate | BLOCKING if missing or changed without requalification |
| Scoped repository freshness | System State refresh | Required scope refreshed, no required evidence unresolved | BLOCKING if required evidence unavailable |
| System drift evaluation | System | No BLOCKING drift intersects target release scope | BLOCKING on intersecting BLOCKING drift |
| Distribution candidate freeze | Distribution | Candidate exact refs and evidence snapshot immutable | BLOCKING if mutable/mismatched |
| Release-set compatibility | Distribution consuming owner/System contracts | Exact composition plus update/rollback rules valid | BLOCKING |
| Whole-product qualification | Distribution | Clean/composed qualification passes for exact candidate | BLOCKING |
| Preservation | Distribution + canonical state owners | Whole-release preservation result passes | BLOCKING |
| Member payload isolation | Distribution | No internal governance leakage; user-owned state/files protected | BLOCKING |
| Promotion | Distribution | Existing release catalog/promotion policy admits exact qualified set | BLOCKING until satisfied |
| Durable release receipt | Distribution | `qualification/<release-id>/release-receipt.json` binds reconstructable admitted evidence | BLOCKING for final admission |
| System synchronization debt | System + Distribution evidence | No unresolved required sync debt for normal promotion | BLOCKING for normal promotion |

### 13.1 Role-specific Wave 1 responsibilities

**Component owners**

- implement component behavior;
- own local interfaces/schemas/migrations;
- publish one canonical release descriptor;
- run native acceptance;
- hand exact accepted revision/evidence to Distribution;
- never claim member shipment from local CI alone.

**AI-Verse-System**

- owns permanent cross-repo law;
- owns Registry and Repository State;
- performs/records refresh and drift classification;
- owns tombstones/current-vs-intended truth;
- never becomes a second component implementation home.

**ai-verse-distribution**

- adopts only exact accepted owner refs;
- freezes qualification evidence;
- validates exact composition/transition compatibility;
- performs preservation/whole-product qualification;
- enforces member payload boundary;
- promotes through existing release machinery;
- persists compact release receipt;
- never becomes component domain authority.

**Member boundary**

- receives only admitted product/runtime payload;
- preserves user-owned state;
- does not receive maintainer governance;
- ambiguous ownership/local modifications fail closed rather than overwrite/delete.

---

## 14. Duplicate-source-of-truth audit

The frozen architecture has one owner for each truth category:

| Truth | Single canonical authority |
|---|---|
| Cross-repo architecture/law | AI-Verse-System governance contract |
| Static repository identity/role | System Repository Registry |
| Dynamic repository observation/drift | System Repository State |
| Human dynamic overview | Generated System ledger only |
| Component implementation/API/schema | Component owner |
| Component release/compat metadata | Owner Component Release Descriptor under System contract |
| Component exact native acceptance | Component owner evidence |
| Exact shipped composition | Distribution release set |
| Release-set update/rollback compatibility | Distribution composition compatibility consuming owner/System facts |
| Candidate qualification evidence | Distribution candidate evidence snapshot/qualification |
| User-state preservation outcome | Existing System contract + owner state semantics + Distribution qualification evidence |
| Promotion/current channel | Existing Distribution catalog/promotion machinery |
| Admitted-release reconstruction binding | Distribution `release-receipt.json` |
| Architecture retirement history | System tombstone ledger |

Rejected duplicate target mechanisms remain rejected:

- second compatibility fingerprint format;
- second safe-update subsystem;
- separate whole-release acceptance database;
- hand-maintained canonical Markdown state ledger;
- Distribution-owned sibling component acceptance truth;
- watchdog-owned second state database;
- parallel promotion database;
- broad member payload copy then delete cleanup.

No unresolved duplicate source of truth remains in the target design.

---

## 15. Known drift carried forward, not fixed by Slice 1.3

1. `BLOCKING`, Core release-governance evidence: current owner descriptors do not certify the exact currently shipped refs, and four owners use noncanonical `development` status. Target architecture is now explicit; repair belongs to planned descriptor/handoff work.
2. `WARNING`, Core/System: Purpose Context Blueprint wording is stale versus accepted/admitted implementation. Reconcile evidence-first in Slice 3.3.
3. `WARNING`, Core maintainer governance: owner-local cross-repo handoff coverage is uneven. Repair in Slice 4.2.
4. `WARNING`, Distribution/component handoff: hard-coded adapter supported-revision knowledge must not become a second acceptance/compatibility authority. Future adoption gates must consume Registry/descriptor/owner evidence while retaining trusted argv routing.
5. `INFO`, Distribution reproducibility: compact canonical future `release-receipt.json` is not yet implemented. Slice 5.4 owns that implementation.
6. U35/U36 pending release state remains `RESOLVED/PASS`.

None of these require a protected roadmap amendment. Slice 1.3 freezes where each is resolved without weakening the existing acceptance floor.

---

## 16. Phase 2 handoff

Phase 2 can proceed without architectural guessing.

Slice 2.1 should create the permanent governance contract at:

`docs/REPOSITORY-NETWORK-GOVERNANCE-CONTRACT.md`

and initialize the architecture tombstone ledger at:

`docs/ARCHITECTURE-TOMBSTONES.md`

It must encode the already-approved laws and this freeze without introducing a second updater, component metadata format, state database, release database or promotion system.

Slice 2.2 should then create:

- `contracts/repository-registry.schema.json`
- `governance/repository-registry.json`
- `scripts/validate_repository_registry.py`

with Wave 1/Core entries first.

Slice 2.3 should then create:

- `contracts/repository-state.schema.json`
- `governance/repository-state.json`
- `docs/REPOSITORY-STATE-LEDGER.md` as generated output
- `docs/MAINTAINER-START-HERE.md`
- `scripts/validate_repository_state.py`

The later refresh/watchdog implementation must use `scripts/refresh_repository_state.py` and `.github/workflows/repository-drift-watchdog.yml` as one shared state model, not parallel logic.

---

## 17. Slice 1.3 acceptance disposition

- no unresolved duplicate source of truth remains in the target design: **PASS**;
- every planned new file/tool has one canonical owner and frozen path: **PASS**;
- release-blocking versus informational drift is explicit: **PASS**;
- Core Wave 1 acceptance matrix is defined: **PASS**;
- Phase 2 can proceed without architectural guessing: **PASS**;
- member preservation/safety/isolation floors were not weakened: **PASS**;
- protected roadmap amendment required: **NO**.
