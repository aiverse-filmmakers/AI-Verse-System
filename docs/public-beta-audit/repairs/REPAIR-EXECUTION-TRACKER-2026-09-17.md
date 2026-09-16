# Post-Audit Repair Execution Tracker

**Created:** 2026-09-17  
**Authority:** `docs/public-beta-audit/synthesis/A6.4-ORDERED-REPAIR-PROGRAM.md`  
**Audit verdict entering repair:** **NO-GO**  
**Audit findings entering repair:** **63 PROVEN / 63 OPEN / 0 CLOSED**  
**Execution rule:** one finding or tightly coupled single-owner closure unit at a time.  
**Current active finding:** `WSA-2026-012`

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
| R0.2 | WSA-2026-012 Memory lifecycle parent-symlink containment | AI-Verse-Memory | **ACTIVE** |
| R0.3 | WSA-2026-016 Skills lifecycle-controller containment | AI-Verse-Skills | PENDING |
| R0.4 | WSA-2026-029 Connections destructive purge containment | AI-Verse-Connections | PENDING |

**R0 exit:** all four BLOCKERs CLOSED after exact-ref negative regression evidence plus lifecycle/security rechecks.

### Phase R1 — Trusted authority, scope, identity and final-edge security

| Order | Finding | Owner | Status |
|---:|---|---|---|
| R1.1 | WSA-2026-009 Brain physical host-root containment | AI-Verse-Brain | PENDING |
| R1.2 | WSA-2026-020 Data trusted scope provenance | AI-Verse-Data | PENDING |
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

## 5. Current task — R0.1 / WSA-2026-006

**Baseline Gateway SHA:** `46c15ee58b028dd7fb8b310327ea705ef618805e`  
**Baseline state:** unchanged from final audit freeze; no open Gateway PRs at repair start.

Repair requirements:
- an unrelated non-empty directory cannot be silently claimed as a Gateway home;
- the installation marker must bind Gateway ownership to the exact canonical home realpath;
- destructive purge requires the exact valid bound marker;
- filesystem roots and broad user-home targets are refused;
- the exact home path itself may not be a symlink/junction/reparse target;
- destructive purge deletes only known Gateway-owned children/files;
- unexpected/unowned children are preserved rather than recursively erased;
- missing, malformed, foreign or copied markers fail closed;
- cross-platform negative regressions cover these cases;
- safe custom-home install/uninstall/reinstall still works.

**Status:** CLOSED

**Closure packet:** `repairs/WSA-2026-006-GATEWAY-DESTRUCTIVE-PURGE.md`

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

### R0.2 / WSA-2026-012 - ACTIVE

Next dependency-safe task: AI-Verse-Memory lifecycle parent-symlink containment. No implementation has begun in this tracker update.
