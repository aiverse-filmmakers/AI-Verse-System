# Post-Audit Repair Execution Tracker

**Created:** 2026-09-17  
**Authority:** `docs/public-beta-audit/synthesis/A6.4-ORDERED-REPAIR-PROGRAM.md`  
**Audit verdict entering repair:** **NO-GO**  
**Audit findings entering repair:** **63 PROVEN / 63 OPEN / 0 CLOSED**  
**Execution rule:** one finding or tightly coupled single-owner closure unit at a time.  
**Current active finding:** `WSA-2026-020`

## 1. Purpose

This tracker is the persistent execution record for repairing the Independent Whole-System Public-Beta Audit findings.

A6.4 remains the dependency-order authority. This file adds operational state so repair work can be resumed from GitHub without relying on chat history.

For every finding, record:

- status;
- baseline SHA;
- repair branch and PR;
- repaired/merged SHA;
- exact regression tests;
- CI/workflow evidence;
- affected repo re-audit;
- affected seam/journey/adversarial rechecks;
- finding-register state transition;
- residual limitations.

A finding is not CLOSED merely because a code PR merged.

## 2. Status vocabulary

- `NEXT` — first eligible repair after all dependencies are satisfied
- `ACTIVE` — the one repair currently being implemented/rechecked
- `PENDING` — waiting for earlier repair dependencies
- `FIXED-PENDING-RECHECK` — implementation merged but required closure evidence incomplete
- `CLOSED` — repair plus required regression/re-audit evidence accepted
- `DEFERRED` — explicitly risk-accepted only where audit policy permits
- `BLOCKED` — cannot proceed because required evidence/access/precondition is missing

Exactly one finding should normally be ACTIVE.

## 3. Repair phases and tasks

### Phase R0 — Destructive containment BLOCKERs

| Order | Finding | Owner | Status |
|---:|---|---|---|
| R0.1 | WSA-2026-006 Gateway destructive purge containment | AI-Verse-Gateway | **CLOSED** |
| R0.2 | WSA-2026-012 Memory lifecycle parent-symlink containment | AI-Verse-Memory | **CLOSED** |
| R0.3 | WSA-2026-016 Skills lifecycle-controller containment | AI-Verse-Skills | **CLOSED** |
| R0.4 | WSA-2026-029 Connections destructive purge containment | AI-Verse-Connections | **CLOSED** |

**R0 exit:** **COMPLETE - 4 / 4 BLOCKERs CLOSED.** Exact-ref destructive-containment repairs and finding-specific lifecycle/security rechecks are recorded for all four findings. Hosted Connections runner availability remains separately OPEN as WSA-2026-003 and is not misclassified as a WSA-029 product-test failure.

### Phase R1 — Trusted authority, scope, identity and final-edge security

| Order | Finding | Owner | Status |
|---:|---|---|---|
| R1.1 | WSA-2026-009 Brain physical host-root containment | AI-Verse-Brain | **CLOSED** |
| R1.2 | WSA-2026-020 Data trusted scope provenance | AI-Verse-Data | **ACTIVE** |
| R1.3 | WSA-2026-022 Multiple Bots operator authority binding | AI-Verse-Multiple-Bots | PENDING |
| R1.4 | WSA-2026-023 Worker workspace isolation | AI-Verse-Multiple-Bots | PENDING |
| R1.5 | WSA-2026-024 Token trusted ACTUAL source authority | ai-verse-token | PENDING |
| R1.6 | WSA-2026-030 Connections installation/system binding | AI-Verse-Connections | PENDING |
| R1.7 | WSA-2026-031 Connections credential-origin binding | AI-Verse-Connections | PENDING |
| R1.8 | WSA-2026-033 Connections normalized path authorization | AI-Verse-Connections | PENDING |
| R1.9 | WSA-2026-051 Connections DNS/private-network containment | AI-Verse-Connections | PENDING |
| R1.10 | WSA-2026-032 Connections final-edge lifecycle/budget authority | AI-Verse-Connections | PENDING |
| R1.11 | WSA-2026-038 Dashboard WebSocket workspace isolation | AI-Verse-Dashboard | PENDING |
| R1.12 | WSA-2026-039 Dashboard registered-root identity binding | AI-Verse-Dashboard | PENDING |
| R1.13 | WSA-2026-040 Dashboard local read authentication | AI-Verse-Dashboard | PENDING |

**R1 progress:** **1 / 13 CLOSED = 7.69%.** WSA-2026-020 is the only ACTIVE R1 finding.

### Phase R2 — Authoritative lifecycle/readiness truth

| Order | Finding | Owner | Status |
|---:|---|---|---|
| R2.1 | WSA-2026-007 Gateway live lifecycle truth | AI-Verse-Gateway | PENDING |
| R2.2 | WSA-2026-013 Memory write authority vs lifecycle | AI-Verse-Memory | PENDING |
| R2.3 | WSA-2026-026 Automations canonical store ownership | AI-Verse-Automations | PENDING |
| R2.4 | WSA-2026-027 Automations legacy authority live fence | AI-Verse-Automations | PENDING |
| R2.5 | WSA-2026-028 Automations attachment reconciliation | AI-Verse-Automations | PENDING |

### Phase R3 — Atomicity, serialization, migration and crash safety

| Order | Finding | Owner | Status |
|---:|---|---|---|
| R3.1 | WSA-2026-008 Gateway state linearizability | AI-Verse-Gateway | PENDING |
| R3.2 | WSA-2026-010 Brain Goal operation-ID race | AI-Verse-Brain | PENDING |
| R3.3 | WSA-2026-017 Skills live-holder lock reclaim | AI-Verse-Skills | PENDING |
| R3.4 | WSA-2026-053 Data natural-key uniqueness | AI-Verse-Data | PENDING |
| R3.5 | WSA-2026-052 OS semantic migration source concurrency | AI-Verse-OS | PENDING |
| R3.6 | WSA-2026-014 Memory migration handoff atomicity | AI-Verse-Memory | PENDING |
| R3.7 | WSA-2026-025 Token pricing transactionality | ai-verse-token | PENDING |
| R3.8 | WSA-2026-034 Distribution lifecycle receipt concurrency | ai-verse-distribution | PENDING |
| R3.9 | WSA-2026-054 Connections crashed-holder write lock | AI-Verse-Connections | PENDING |
| R3.10 | WSA-2026-055 Connections unknown external-effect recovery | AI-Verse-Connections | PENDING |

### Phase R4 — Remaining runtime MEDIUM hardening

| Order | Finding | Owner | Status |
|---:|---|---|---|
| R4.1 | WSA-2026-018 Skills active-generation retention | AI-Verse-Skills | PENDING |
| R4.2 | WSA-2026-036 Distribution final error redaction | ai-verse-distribution | PENDING |
| R4.3 | WSA-2026-041 Dashboard localhost Origin policy | AI-Verse-Dashboard | PENDING |
| R4.4 | WSA-2026-042 Dashboard projection semantics | AI-Verse-Dashboard | PENDING |
| R4.5 | WSA-2026-045 Gateway exact-source freshness cache | AI-Verse-Gateway | PENDING |
| R4.6 | WSA-2026-050 Gateway pre-auth CPU admission | AI-Verse-Gateway | PENDING |
| R4.7 | WSA-2026-056 Connections receipt-corruption health truth | AI-Verse-Connections | PENDING |
| R4.8 | WSA-2026-057 Connections provider-error minimization | AI-Verse-Connections | PENDING |
| R4.9 | WSA-2026-058 Gateway idempotency-state scale | AI-Verse-Gateway | PENDING |
| R4.10 | WSA-2026-059 Connections receipt-history scale | AI-Verse-Connections | PENDING |

### Phase R5 — Release/current-state/documentation synchronization

| Order | Finding | Owner | Status |
|---:|---|---|---|
| R5.1 | WSA-2026-011 Brain release/version identity | AI-Verse-Brain | PENDING |
| R5.2 | WSA-2026-015 Memory release/bootstrap identity | AI-Verse-Memory | PENDING |
| R5.3 | WSA-2026-019 Skills release/bootstrap identity | AI-Verse-Skills | PENDING |
| R5.4 | WSA-2026-021 Data release/install identity | AI-Verse-Data | PENDING |
| R5.5 | WSA-2026-043 release schema/validator consistency | AI-Verse-System | PENDING |
| R5.6 | WSA-2026-001 Invisible candidate acceptance metadata | ai-verse-distribution / AI-Verse-System | PENDING |
| R5.7 | WSA-2026-035 Agent Python prerequisite | ai-verse-distribution | PENDING |
| R5.8 | WSA-2026-060 Full compatibility stale Agent blocker | ai-verse-distribution | PENDING |
| R5.9 | WSA-2026-037 Distribution architecture/roadmap status | ai-verse-distribution | PENDING |
| R5.10 | WSA-2026-061 Token beta.3 acceptance prose | ai-verse-token | PENDING |
| R5.11 | WSA-2026-062 Multiple Bots Agent composition prose | AI-Verse-Multiple-Bots | PENDING |
| R5.12 | WSA-2026-005 OS capability-source metadata | AI-Verse-OS | PENDING |
| R5.13 | WSA-2026-002 stale System Connections spec | AI-Verse-System | PENDING |
| R5.14 | WSA-2026-044 System living-spec propagation | AI-Verse-System | PENDING |
| R5.15 | WSA-2026-004 stale audit README entrypoint | AI-Verse-System | PENDING |

### Phase R6 — Composed release requalification

| Order | Finding | Owner | Status |
|---:|---|---|---|
| R6.1 | WSA-2026-003 hosted CI evidence availability | Connections / System | PENDING |
| R6.2 | WSA-2026-046 current Video Editor absent from admitted Agent | Skills / Distribution / System | PENDING |
| R6.3 | WSA-2026-047 semantic migration composed acceptance | multi-owner | PENDING |
| R6.4 | WSA-2026-048 Goal-to-learned-Skill composed acceptance | multi-owner | PENDING |
| R6.5 | WSA-2026-049 two-system A/B isolation acceptance | multi-owner | PENDING |
| R6.6 | WSA-2026-063 real non-test Gateway runtime release evidence | Gateway / Distribution | PENDING |

### Phase RF — Bounded final independent recheck

Status: PENDING

Run only after R0-R6 closure gates. Scope is the mandatory final recheck in A6.4/A6.5. This phase issues a new evidence-based readiness verdict. It is the only phase that may release Dashboard MC1.4 or owner dogfood.

## 4. Per-finding execution contract

Before implementation:
1. recheck owner repo head/open PRs and record drift;
2. read the finding and original evidence packet;
3. identify the exact executable boundary and tests;
4. write a bounded repair record under `docs/public-beta-audit/repairs/`.

Implementation:
1. create one owner repair branch;
2. implement the smallest complete fix;
3. add permanent negative regressions for the original failure;
4. do not opportunistically fix unrelated findings.

Acceptance:
1. inspect the PR diff;
2. require owner test/CI evidence where available;
3. merge only the reviewed head;
4. re-run the finding-specific standalone/seam/journey/adversarial checks;
5. write exact closure evidence into the repair record;
6. transition the finding register only after closure evidence exists;
7. mark exactly one next finding ACTIVE.

## 5. Completed task - R0.3 / WSA-2026-016

**Owner:** `AI-Verse-Skills`  
**Original baseline:** `8c321c03421a2e0e470280cc40e588a27c1a510d`  
**Repair PR:** `AI-Verse-Skills#15`  
**Final PR head:** `62b49d6420a6034fd08c47c2070ec473f128a392`  
**Merged Skills:** `3541d2a7af1b20ca12736ed7454d119295d8e193`  
**Status:** CLOSED  
**Closure packet:** `repairs/WSA-2026-016-SKILLS-CONTROLLER-CONTAINMENT.md`

Closure evidence:
- one shared `controller_path` physical containment primitive added;
- POSIX symlinks and Windows junction/reparse controller indirection rejected;
- controller, generation, active-pointer, setup/integration and learning state routed through the same confinement law;
- destructive generation purge validates confined generation paths before recursive deletion;
- external-sentinel regressions cover redirected `.aiverse`, generation storage, learning state, status, commit and purge;
- Windows tests use real `mklink /J` directory junctions;
- corrected final PR-head Validate run `35192350269`: SUCCESS;
- corrected final PR-head Containment run `35192350296`: 6 / 6 jobs SUCCESS;
- corrected final PR-head Runtime Readiness run `35192350294`: 6 / 6 jobs SUCCESS;
- corrected final PR-head Full E2E run `35192350298`: SUCCESS;
- Windows 3.9 containment job `105107547111`: 10 tests / OK;
- final PR tree and merged main tree both `3e5f72ed405aec0cc015afb52a98505178cf0c3f`;
- zero open Skills PRs after merge;
- post-merge Containment run `35201821336`: SUCCESS;
- post-merge Runtime Readiness run `35201821346`: SUCCESS;
- post-merge Full E2E run `35201821359`: SUCCESS;
- post-merge Validate run `35201821414`: SUCCESS;
- A1.5 finding-specific recheck: PASS for WSA-016 only;
- A3.10 Skills destructive-containment branch: RESOLVED; journey remains PARTIAL;
- A4.1 Skills controller-confinement branch: RESOLVED; adversarial task remains FAIL;
- finding state: `OPEN -> CLOSED`.

The early macOS lexical `/var` vs `/private/var` interruption-test mismatch was caught before merge, corrected to compare physical paths, and the corrected head passed the full supported matrix. It is retained in the closure packet as repair evidence.

This repair does not close WSA-2026-017, WSA-2026-018 or WSA-2026-019.

## 5A. Completed task - R0.4 / WSA-2026-029

**Owner:** `AI-Verse-Connections`  
**Original audited ref:** `baaac641558dbff1c2eabb0b5ec785a633f49a5b`  
**Live pre-repair ref:** `53b62bc636b9f1f367073c977050d12faf6509ec` (zero product-file diff from audited ref)  
**Repair PR:** `AI-Verse-Connections#2`  
**Final PR head:** `c4bb77f680298d91ce619db91a39d69daaaa76a8`  
**Merged Connections:** `a04f655c6f0c9b57d17e64b5c1ff8eb88aab4016`  
**Status:** CLOSED  
**Closure packet:** `repairs/WSA-2026-029-CONNECTIONS-DESTRUCTIVE-PURGE.md`

Closure evidence:
- durable exact-realpath `ownership.json` added;
- install refuses unrelated non-empty foreign homes;
- recognizable legacy Connections state can receive the ownership marker;
- broad filesystem/user/system homes are refused;
- exact home symlink/junction targets are refused;
- missing, wrong/foreign and copied markers fail closed;
- purge no longer recursively deletes an arbitrary configured root;
- only known Connections-owned entries are removed;
- unknown/unowned children are preserved;
- exact repaired destructive lifecycle harness: **10 / 10 PASS**;
- actual `install -> setup -> uninstall({purge:true})` lifecycle path: PASS;
- final PR head and merged product files have zero differences;
- open Connections PRs after merge: 0;
- PR run `35219295977`, unchanged-main run `35218943165` and post-merge run `35219652570` all exhibit inherited WSA-2026-003 no-runner infrastructure behavior (`steps: []`, `runner_id: 0`), so no hosted product test executed and no hosted cross-platform pass is claimed;
- A1.10 finding-specific recheck: PASS for WSA-029 only;
- A3.10 destructive lifecycle containment branch: RESOLVED for all four R0 findings; A3.10 remains PARTIAL overall;
- A4.1 Connections destructive-purge branch: RESOLVED; adversarial task remains FAIL overall;
- finding state: `OPEN -> CLOSED`.

This repair does not close WSA-2026-003 or WSA-2026-030 through WSA-2026-033, WSA-2026-051, WSA-2026-054 through WSA-2026-057, or WSA-2026-059.

## 5B. Most recently completed task - R1.1 / WSA-2026-009

**Owner:** `AI-Verse-Brain`  
**Original audited / pre-repair ref:** `6f986e8d06c7f9c069fbf05aa92ae7b7a1af9bf4`  
**Repair PR:** `AI-Verse-Brain#24`  
**Final tested PR head:** `f35a3f683f9014bbe3b508af341c09992ae2c1c3`  
**Merged Brain:** `908f9a9a06c2b12204ada7f71cd761bae97b52ce`  
**Product tree:** `66b650a63879898b936b7c8c550d10654caed366`  
**Status:** CLOSED  
**Closure packet:** `repairs/WSA-2026-009-BRAIN-NATIVE-HOST-ROOT-CONTAINMENT.md`

Closure evidence:
- one shared native physical-path guard added;
- native `operator` and `workspaces` symlink/junction/reparse parents fail host compatibility;
- operator state, workspace state and individual workspace parents are physically confined;
- native runtime and nested runtime-lock paths are physically confined and revalidated before mutation;
- initialization and `installation.json` paths use the same containment law;
- standalone-to-native adoption transaction, staging, retirement, destination and runtime paths are confined and revalidated between phases;
- permanent external-sentinel regressions cover ten hostile path layouts;
- Windows directory attacks use real `mklink /J` junctions;
- PR-head CI run `35228628402`: SUCCESS, package smoke plus all six Ubuntu/macOS/Windows Python matrix legs;
- Windows Python 3.12 job `105226554049`: 237 tests successful, nine executable WSA-009 junction/path attacks pass, one ordinary file-symlink test intentionally skipped;
- macOS Python 3.12 job `105226553976`: 237 / 237 tests passed including all ten containment attacks;
- PR-head Skills Receipt Contract run `35228628604`: SUCCESS;
- PR-head OS Direction Ownership Contract run `35228628938`: SUCCESS;
- final tested PR tree equals merged tree `66b650a63879898b936b7c8c550d10654caed366`;
- post-merge CI run `35228849333`: 7 / 7 jobs SUCCESS;
- post-merge Skills Receipt Contract run `35228849545`: SUCCESS;
- post-merge OS Direction Ownership Contract run `35228849499`: SUCCESS;
- open Brain PRs after merge: 0;
- A1.3 finding-specific recheck: PASS for WSA-009 only;
- A3.2 Brain destination-scope branch: RESOLVED; journey remains PARTIAL overall;
- A4.1 Brain owner-root branch: RESOLVED; adversarial task remains FAIL overall;
- finding state: `OPEN -> CLOSED`.

This repair does not close WSA-2026-010 or WSA-2026-011.

## 6. Repair log

### R0.1 / WSA-2026-006 - CLOSED

- baseline Gateway: `46c15ee58b028dd7fb8b310327ea705ef618805e`
- repair PR: `AI-Verse-Gateway#32`
- PR head: `94a1416724f076f06783385c4df07cf18bdbd788`
- merged Gateway: `5347a0b7e3f3f302f4570e9bc37d515192753610`
- CI: run `35152574719`, six Linux/macOS/Windows Node 20/22 jobs SUCCESS
- full test result observed on Ubuntu Node 22: 104 passed / 0 failed
- composed Gateway workflows: four of four SUCCESS
- exact PR-head to merge comparison: zero changed files
- A1.2 finding-specific recheck: PASS for WSA-006 only
- A3.10 Gateway destructive-containment branch: RESOLVED; journey remains PARTIAL due other findings
- A4.1 Gateway destructive-containment branch: RESOLVED; adversarial task remains FAIL due other findings
- finding state: `OPEN -> CLOSED`

### R0.2 / WSA-2026-012 - CLOSED

- baseline Memory: `406b14fb4398eb1b16dd5f30e50520e8c3540972`
- repair PR: `AI-Verse-Memory#30`
- initial CI run `35155623941`: caught macOS/Windows platform-alias handling and was not merged
- corrected PR head: `acbe3e22d9b12c0fc1b0dcd95eeea393a57a69f2`
- final CI run `35155708095`: 12 / 12 jobs SUCCESS
- Windows public-beta acceptance: real junction/reparse tests SUCCESS
- merged Memory: `7a1ed5777fd11616375501d730fcbd488beff8b8`
- exact PR-head to merge comparison: zero changed files
- A1.4 finding-specific recheck: PASS for WSA-012 only
- A3.10 Memory destructive-containment branch: RESOLVED; journey remains PARTIAL
- A4.1 Memory path-containment branch: RESOLVED; adversarial task remains FAIL
- finding state: `OPEN -> CLOSED`

### R0.3 / WSA-2026-016 - CLOSED

- baseline Skills: `8c321c03421a2e0e470280cc40e588a27c1a510d`
- repair PR: `AI-Verse-Skills#15`
- corrected final PR head: `62b49d6420a6034fd08c47c2070ec473f128a392`
- merged Skills: `3541d2a7af1b20ca12736ed7454d119295d8e193`
- PR-head workflow families: 4 / 4 SUCCESS
- containment matrix: 6 / 6 SUCCESS
- post-merge main workflow families: 4 / 4 SUCCESS
- exact PR-head and merge product tree: `3e5f72ed405aec0cc015afb52a98505178cf0c3f`
- A1.5 finding-specific recheck: PASS for WSA-016 only
- A3.10 Skills destructive-containment branch: RESOLVED; journey remains PARTIAL
- A4.1 Skills controller-confinement branch: RESOLVED; adversarial task remains FAIL
- finding state: `OPEN -> CLOSED`

### R0.4 / WSA-2026-029 - CLOSED

- audited Connections: `baaac641558dbff1c2eabb0b5ec785a633f49a5b`
- live pre-repair product tree: `53b62bc636b9f1f367073c977050d12faf6509ec`, zero changed files from audited ref
- repair PR: `AI-Verse-Connections#2`
- final PR head: `c4bb77f680298d91ce619db91a39d69daaaa76a8`
- merged Connections: `a04f655c6f0c9b57d17e64b5c1ff8eb88aab4016`
- exact destructive lifecycle harness: 10 / 10 PASS
- actual service lifecycle install/setup/purge: PASS
- exact PR-head to merge comparison: zero changed files
- hosted matrix unavailable: six jobs allocate no runner and execute zero steps, retained under WSA-2026-003
- A1.10 finding-specific recheck: PASS for WSA-029 only
- A3.10 destructive-containment branch: all four R0 findings RESOLVED; journey remains PARTIAL
- A4.1 Connections purge branch: RESOLVED; adversarial task remains FAIL overall
- finding state: `OPEN -> CLOSED`

### R1.1 / WSA-2026-009 - CLOSED

- baseline Brain: `6f986e8d06c7f9c069fbf05aa92ae7b7a1af9bf4`
- repair PR: `AI-Verse-Brain#24`
- final tested PR head: `f35a3f683f9014bbe3b508af341c09992ae2c1c3`
- merged Brain: `908f9a9a06c2b12204ada7f71cd761bae97b52ce`
- exact PR-head and merged product tree: `66b650a63879898b936b7c8c550d10654caed366`
- PR-head CI: all seven jobs SUCCESS
- PR-head contract workflows: 2 / 2 SUCCESS
- post-merge CI: all seven jobs SUCCESS
- post-merge contract workflows: 2 / 2 SUCCESS
- A1.3 finding-specific recheck: PASS for WSA-009 only
- A3.2 Brain destination-containment branch: RESOLVED; journey remains PARTIAL
- A4.1 Brain path-containment branch: RESOLVED; adversarial task remains FAIL overall
- finding state: `OPEN -> CLOSED`

## 7. Current task - R1.2 / WSA-2026-020

**Owner:** `AI-Verse-Data`  
**Status:** ACTIVE  
**Execution state:** not yet implemented. The next repair session must first recheck Data main/open PRs and the exact WSA-2026-020 evidence before creating the owner repair branch.

No later finding may become ACTIVE until WSA-2026-020 reaches CLOSED or an explicitly recorded BLOCKED state.
