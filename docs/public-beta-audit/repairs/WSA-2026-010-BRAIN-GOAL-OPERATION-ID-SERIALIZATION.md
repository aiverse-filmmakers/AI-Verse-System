# WSA-2026-010 Closure - Brain Goal Operation-ID Serialization

**Finding:** `WSA-2026-010`  
**Severity / confidence:** MEDIUM / PROVEN  
**Owner:** `AI-Verse-Brain`  
**Repair wave:** R3.2  
**Closure date:** 2026-10-02  
**State:** **CLOSED**

## 1. Finding

Goal operation receipts are scoped by `scope + operation_id`, but the audited non-create mutation paths serialized only on `scope + goal_id`.

That meant two concurrent first-use mutations against different Goals could reuse one operation ID while holding different Goal locks:

1. both callers observed no operation receipt;
2. each acquired a different Goal lock;
3. both mutated separate canonical Goal objects;
4. both wrote the same operation-receipt path;
5. only one receipt survived while two semantic mutations had committed.

Affected mutation families were:

- Goal edit;
- Goal transition;
- criteria add/remove/clear;
- progress recording.

**Contradiction:** `C-A1.3-002`.

Required closure evidence:

- serialize mutation admission on `scope + operation_id`;
- retain Goal revision serialization;
- add deterministic cross-Goal same-operation-ID concurrent tests;
- prove exactly one mutation commits;
- prove the losing changed-payload caller receives the established idempotency conflict.

## 2. Baseline and repair identity

**Pre-repair Brain ref:** `908f9a9a06c2b12204ada7f71cd761bae97b52ce`  
**Open Brain PRs before repair:** 0

**Repair branch:** `repair/wsa-2026-010-goal-operation-id-race`  
**Repair PR:** `AI-Verse-Brain#25`  
**Final tested PR head:** `7a2189a3761bc6f11411691d3a664ab48c133b1b`  
**Merged Brain ref:** `39b3feb6ad03aa185a4ba6f5f24614e55c4b969f`  
**Tested/merged product tree:** `2c5ce89d3b9ca4412547ba0a04b730811c6da1fe`

The exact final PR head and merged `main` commit have the same product tree.

Open Brain PRs after merge: **0**.

## 3. Final implementation contract

### 3.1 One operation-ID admission boundary

Every durable Goal mutation now enters through one Goal-service mutation lock keyed by:

`scope + operation_id`

before any Goal-specific revision lock is acquired.

This applies to:

- create;
- edit;
- transition;
- criteria add/remove/clear through their shared mutation path;
- progress recording.

The pre-lock receipt read remains a fast replay path. The receipt is re-read again while the operation-ID lock is held before any canonical Goal mutation is allowed.

### 3.2 Goal revision serialization remains nested beneath operation admission

For non-create mutations the lock order is now:

1. operation-ID admission lock;
2. Goal-specific runtime lock;
3. canonical object-store revision lock/save.

This preserves the existing per-Goal revision protection while adding the missing cross-Goal idempotency namespace protection.

All repaired mutation families therefore use the same ordering.

### 3.3 Concurrent first use is serialized instead of rejected too early

`RuntimeKeyLock` remains intentionally non-blocking and is not modified by this repair.

GoalService adds a narrow bounded wait only around the operation-ID admission key. If another caller currently holds the same operation-ID lock, the contender briefly retries until the first local Goal mutation finishes.

After acquiring the operation-ID lock, the contender re-runs the durable receipt check.

For a different payload, including a different `goal_id`, the existing error remains authoritative:

`operation_id was already used with a different Goal mutation payload`

Therefore the race is resolved by durable idempotency state rather than by a generic transient lock failure.

### 3.4 No self-deadlock when operation ID equals Goal ID

Operation IDs are caller supplied.

If a caller chooses an `operation_id` whose lock key is exactly the same as the Goal lock key, the service recognizes that the operation lock already covers the Goal key and does not attempt to acquire the identical runtime lock twice.

A permanent regression proves that this edge remains valid.

### 3.5 Runtime lock reclaim semantics remain out of scope

The implementation does **not** modify:

- `RuntimeKeyLock.acquire()`;
- lock TTL behavior;
- stale lock reclamation;
- live-holder detection.

Those semantics belong to the next repair:

`R3.3 / WSA-2026-017`.

The Goal-specific admission retry is bounded to five seconds, well below the existing 60-second runtime lock TTL, so this repair does not exercise or broaden stale-holder reclamation.

## 4. Deterministic concurrency regressions

New permanent suite:

`tests/test_goal_operation_id_serialization.py`

The test harness synchronizes the two callers at their first durable receipt check so both reproduce the audited first-use window deterministically.

### 4.1 Cross-Goal edit

Two different active Goals concurrently call `edit()` with the same operation ID and different request payloads.

Proven result:

- exactly one call succeeds;
- exactly one Goal revision advances;
- exactly one objective changes;
- the durable receipt points to the winning Goal/version;
- the loser receives the established changed-payload `ValidationError`.

### 4.2 Cross-Goal transition

Two different active Goals concurrently call `transition(... action="pause")` with the same operation ID.

Proven result:

- exactly one call succeeds;
- exactly one Goal revision advances;
- exactly one Goal becomes paused;
- the loser receives the idempotency conflict.

### 4.3 Cross-Goal criteria mutation

Two different active Goals concurrently call the shared criteria mutation path with the same operation ID.

Proven result:

- exactly one call succeeds;
- exactly one Goal revision advances;
- exactly one Goal receives the new criterion;
- the loser receives the idempotency conflict.

Because criteria add/remove/clear share the repaired `_criteria_mutation()` admission boundary, the serialization law covers all three criteria operations.

### 4.4 Cross-Goal progress recording

Two different active Goals concurrently call `record_progress()` with the same operation ID.

Proven result:

- exactly one call succeeds;
- exactly one Goal revision advances;
- exactly one Goal records an attempt/token increment;
- the loser receives the idempotency conflict.

### 4.5 Operation ID equals Goal ID

A normal edit whose operation ID equals the Goal ID succeeds and advances the Goal exactly once.

This proves the nested operation/Goal locking cannot self-conflict on identical key material.

## 5. PR-head validation

Final PR-head CI:

`37059407803`

On exact final head `7a2189a3761bc6f11411691d3a664ab48c133b1b`:

- package smoke: **PASS**
- Ubuntu Python 3.9: **PASS**
- Ubuntu Python 3.12: **PASS**
- macOS Python 3.9: **PASS**
- macOS Python 3.12: **PASS**
- Windows Python 3.9: **PASS**
- Windows Python 3.12: **PASS**
- CI: **7 / 7 jobs PASS**
- representative unit suite: **242 / 242 tests PASS**

All five dedicated WSA-2026-010 regressions are present in the exact-head unit run.

Cross-repo exact-head contracts:

- OS Direction Ownership Contract `37059407731`: **PASS**
- Skills Receipt Contract `37059408161`: **PASS**

## 6. Post-merge validation

Merged-main CI:

`37059636663`

On merged Brain `main` ref `39b3feb6ad03aa185a4ba6f5f24614e55c4b969f`:

- package smoke: **PASS**
- Ubuntu Python 3.9/3.12: **PASS**
- macOS Python 3.9/3.12: **PASS**
- Windows Python 3.9/3.12: **PASS**
- CI: **7 / 7 jobs PASS**
- representative unit suite: **242 / 242 tests PASS**

All five dedicated WSA-2026-010 regressions are present in the merged-main unit run.

Merged-main cross-repo contracts:

- OS Direction Ownership Contract `37059636656`: **PASS**
- Skills Receipt Contract `37059636711`: **PASS**

The tested PR-head tree and merged-main tree are identical:

`2c5ce89d3b9ca4412547ba0a04b730811c6da1fe`

## 7. Finding-specific recheck

### C-A1.3-002

**RESOLVED for WSA-2026-010.**

The operation-receipt namespace and mutation-admission lock namespace now match for all durable Goal mutations.

### Concurrent cross-Goal first use

**PASS.**

Two different Goals cannot both mutate under one first-use operation ID.

### Changed-payload reuse

**PASS.**

After the winner commits its mutation and receipt, the serialized contender re-reads that receipt and receives the existing changed-payload idempotency error.

### Goal revision protection

**PASS.**

Per-Goal locking and object-store expected revision checks remain beneath the operation-ID admission boundary.

### Existing Brain contracts

**PASS.**

The full Brain suite, package smoke, OS Direction Ownership contract and Skills Receipt contract are green on exact head and merged main.

## 8. Adjacent findings remain open

This closure is limited to `WSA-2026-010`.

The next dependency-safe finding is:

`R3.3 / WSA-2026-017 - Skills live-holder lock reclaim`.

Explicitly unchanged:

- `WSA-2026-011` Brain release/version identity;
- `WSA-2026-017` RuntimeKeyLock/live-holder reclaim semantics;
- later atomicity, migration, retrieval and lifecycle findings.

The whole-system verdict remains **NO-GO**.

## 9. Closure verdict

Required WSA-2026-010 behavior is present on merged Brain `main`:

- all durable Goal mutations serialize first on scope + operation ID;
- Goal revision serialization remains nested and authoritative;
- cross-Goal same-operation-ID first use commits exactly one mutation;
- the losing changed-payload caller receives the established idempotency conflict;
- criteria and progress paths are covered;
- operation-ID-equals-Goal-ID cannot self-conflict;
- RuntimeKeyLock reclaim behavior was not modified;
- exact-head CI is 7 / 7 PASS with 242 / 242 tests;
- exact-head OS and Skills contracts PASS;
- merged-main CI is 7 / 7 PASS with 242 / 242 tests;
- merged-main OS and Skills contracts PASS;
- tested and merged product trees are identical;
- open Brain PRs are zero.

**WSA-2026-010: CLOSED.**
