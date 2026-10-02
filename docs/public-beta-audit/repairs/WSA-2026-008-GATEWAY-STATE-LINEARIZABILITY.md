# WSA-2026-008 Closure - Gateway State Linearizability

**Finding:** `WSA-2026-008`  
**Severity / confidence:** HIGH / PROVEN  
**Owner:** `AI-Verse-Gateway`  
**Repair wave:** R3.1  
**Closure date:** 2026-10-02  
**State:** **CLOSED**

## 1. Finding

Gateway durable JSON writes were physically atomic, but several semantic transitions were not linearizable.

At the audited baseline:

- idempotency claim performed read/check before the serialized replacement, so two first callers could both observe an unused key and both return `new`;
- first session binding performed read/validate before its write, so conflicting first bindings could both pass validation;
- run persistence could replace current state from a stale captured object with no durable revision compare, allowing execution state to overwrite newer pause/cancel control;
- cancellation/control was not rechecked at every output/effect boundary.

Canonical contradictions: `C-A1.2-002` and `C-A1.2-003`.

Required closure evidence:

- atomic idempotency claim/compare/reservation;
- atomic first session create-or-validate;
- run revision/CAS or equivalent transition discipline;
- control authority recheck immediately before durable/effect edges;
- deterministic concurrency regressions;
- no stale post-pause/post-cancel streaming or owner handoff.

## 2. Baseline and repair identity

**Pre-repair Gateway ref:** `b27cebe11e536aa5a0f9bad707f38b0c2471879d`  
**Open Gateway PRs before repair:** 0

**Repair branch:** `repair/wsa-2026-008-state-linearizability`  
**Repair PR:** `AI-Verse-Gateway#34`  
**Final tested PR head:** `da359b8db45eb11b04fd1907500117bb8c122bbc`  
**Merged Gateway ref:** `cd0789401ddf7c536558a27d84328e963b10c882`  
**Tested/merged product tree:** `fe02f4271b3f47b25210d81d77caad5c728d708c`

The exact final PR head and merged `main` commit have the same product tree.

Open Gateway PRs after merge: **0**.

## 3. Final implementation contract

### 3.1 Idempotency admission is one serialized state transition

`claimIdempotency()` now performs lookup, digest comparison and first reservation inside the existing serialized `mutateJson()` boundary.

For one namespace/key:

- the first exact payload acquires one durable reservation;
- a concurrent exact-payload first use cannot also return `new`; it fails with `IDEMPOTENCY_IN_PROGRESS`;
- a concurrent different payload fails with `IDEMPOTENCY_CONFLICT`;
- after the first operation commits a result, exact replays return the canonical recorded result.

`commitIdempotency()` also mutates the ledger through the same serialized primitive.

### 3.2 First session binding is atomic create-or-validate

`createSession()` now uses one serialized mutation of the session file.

Inside that transition Gateway either:

- creates the first binding; or
- validates the already committed system/workspace/principal binding.

Two conflicting first writers therefore cannot both acquire authority.

### 3.3 Runs carry a durable revision

New runs start with `revision: 0`.

Each canonical `mutateRun()` transition increments the current durable revision.

`saveRun()` is compare-and-swap:

- the caller presents the revision it read;
- persistence re-reads the current canonical run under the serialized file mutation;
- a revision mismatch raises `RUN_REVISION_CONFLICT`;
- stale captured state is not persisted.

Legacy runs without the field are interpreted as revision zero for compatibility.

### 3.4 Operator control transitions mutate current state atomically

Pause, resume and cancel now operate through `mutateRun()` instead of read-then-save.

This gives each control a single current-state transition:

- terminal state is not silently replaced by a stale pause;
- cancel preserves already completed/canceled truth;
- resume validates the current canonical resumable state;
- a successful control increments the same revision observed by execution guards.

### 3.5 Execution authority is rechecked after provider/runtime waits

After runtime invocation returns, Gateway re-reads the current durable run and verifies:

- expected revision still matches;
- status still grants execution authority;
- the execution signal was not aborted.

A pause/cancel occurring while a runtime call is outstanding therefore revokes the stale executor before it can apply the returned result.

### 3.6 Streaming is fenced by current run authority

Assistant text emission now rechecks current revision/control authority before every emitted chunk.

A runtime that ignores cancellation and returns text after the operator has paused/canceled cannot continue producing Gateway `assistant.delta` events.

### 3.7 Owner effects are fenced immediately before delivery

The normal tool/action path rechecks durable run authority after authorization and immediately before `host.requestAction()`.

The direct composed owner-action path supports the legitimate pre-execution `queued` state while still requiring an unchanged revision and a non-paused/non-canceled state.

Approval execution similarly rechecks the current `awaiting_approval` run before owner delivery.

A stale executor therefore cannot use an earlier run snapshot to perform a canonical owner action after control has changed.

### 3.8 Restart is a quiescence boundary

The new CAS discipline exposed two pre-existing restart races in optional post-completion work.

Gateway now:

- serializes pending session-digest recovery before pending organization-review recovery;
- tracks active run execution promises;
- exposes an engine drain primitive;
- makes graceful server close stop accepting traffic and wait for active execution plus startup recovery to finish before returning.

A caller that awaits `close()` can therefore start a replacement Gateway without the old process continuing to mutate the same durable run.

This preserves CAS instead of weakening it to accommodate overlapping old/new writers.

## 4. Permanent regressions

`test/state-linearizability.test.mjs` is part of the canonical `npm test` suite and proves:

1. concurrent identical first idempotency claims admit exactly one reservation;
2. the competing identical first claim returns `IDEMPOTENCY_IN_PROGRESS`;
3. after result commit, exact replay returns the canonical result;
4. concurrent changed-payload reuse of the same operation key produces one admission and one `IDEMPOTENCY_CONFLICT`;
5. conflicting concurrent first session bindings choose exactly one durable binding;
6. the losing binding fails with `SESSION_BINDING_MISMATCH`;
7. stale run completion cannot overwrite a newer cancel;
8. stale `saveRun()` fails with `RUN_REVISION_CONFLICT`;
9. cancel during a runtime that ignores control preserves canceled state;
10. that late runtime result emits no assistant delta;
11. that late runtime result performs no owner call;
12. that late runtime result emits no completion or Memory digest handoff;
13. pause during the same race preserves paused state and prevents stale streaming/completion.

The existing restart/learning/Data integration suite additionally proves graceful restart remains functional under the new revision model.

## 5. Validation-driven refinements

The repair was deliberately not merged on the first green-looking implementation.

### 5.1 Direct composed owner path compatibility

Initial exact-head composed runs on `6f3366452b4691364403823cca8dadac9a09c67f` failed because the new effect guard initially permitted only `running/resuming`.

The composed contracts intentionally exercise `handleToolCalls()` directly on a `queued` run.

The final policy therefore admits `queued` only at that direct owner-effect boundary while still requiring exact revision equality and rejecting pause/cancel/control drift.

All four composed contracts are green on the final head.

### 5.2 Concurrent post-completion startup recovery

A subsequent core CI run exposed that session-digest recovery and organization-review recovery were launched concurrently and could mutate the same completed run revision.

The two recovery passes are now serialized while remaining background/non-blocking during server startup.

### 5.3 Old/new Gateway overlap during graceful restart

A later restart integration failure exposed that `live.close()` previously closed HTTP transport without waiting for active execution/post-completion state work.

The final implementation tracks active executions and drains both execution and recovery before graceful close resolves.

This made server close the durable process-handover boundary rather than weakening CAS.

### 5.4 Canonical regression enrollment

A first all-green final-shape run reported 107 / 107 tests, which revealed that the repository's `npm test` command explicitly enumerated test files and did not yet include the new WSA-2026-008 file.

The package test script was corrected before merge.

The accepted exact head runs the dedicated WSA-008 regressions as part of the canonical suite and reports **113 / 113**.

## 6. Validation evidence

### Final PR-head acceptance

Final PR-head CI:

`37055012899`

On exact final head `da359b8db45eb11b04fd1907500117bb8c122bbc`:

- Ubuntu Node 20: **PASS**
- Ubuntu Node 22: **PASS**
- macOS Node 20: **PASS**
- macOS Node 22: **PASS**
- Windows Node 20: **PASS**
- Windows Node 22: **PASS**
- matrix: **6 / 6 PASS**
- representative canonical suite: **113 / 113 passed**

Final exact-head composed acceptance:

- Context Ladder Integrated Acceptance `37055012896`: **PASS**
- Temporary Worker Composition `37055012893`: **PASS**
- Permanent Bot Composition `37055012914`: **PASS**
- Automation Recommendation Boundary `37055012900`: **PASS**

### Post-merge acceptance

Merged-main CI:

`37055200397`

On merged Gateway `main` ref `cd0789401ddf7c536558a27d84328e963b10c882`:

- Ubuntu Node 20/22: **PASS**
- macOS Node 20/22: **PASS**
- Windows Node 20/22: **PASS**
- matrix: **6 / 6 PASS**
- representative canonical suite: **113 / 113 passed**

The tested PR-head tree and merged-main tree are identical:

`fe02f4271b3f47b25210d81d77caad5c728d708c`

## 7. Finding-specific recheck

### C-A1.2-002

**RESOLVED for WSA-2026-008.**

Idempotency claim/reservation and first session binding are serialized semantic transitions rather than read-check-write sequences.

### C-A1.2-003

**RESOLVED for WSA-2026-008.**

Run writers carry durable revisions, stale captured writes fail closed, and operator control mutates the current canonical run.

### Concurrent idempotency

**PASS.**

Same-key same-payload first use produces exactly one reservation. Changed-payload concurrent reuse cannot acquire a second semantic admission.

### Concurrent first session binding

**PASS.**

Exactly one binding becomes canonical; a conflicting contender fails against that committed state.

### Pause/cancel during runtime result

**PASS.**

Late provider/runtime results cannot stream, complete, or perform owner effects after current control authority changes.

### Post-control owner handoff

**PASS.**

The dedicated regression observes zero owner calls and no Memory digest handoff after concurrent cancel.

### Restart/recovery

**PASS.**

Post-completion recovery is serialized and graceful close drains old process state work before restart.

## 8. Adjacent findings remain open

This closure is limited to `WSA-2026-008`.

The next dependency-safe finding is:

`R3.2 / WSA-2026-010 - Brain Goal operation-ID race`.

Gateway R4 retrieval/cache and pre-auth CPU findings remain unchanged.

The whole-system verdict remains **NO-GO**.

## 9. Closure verdict

Required WSA-2026-008 behavior is present on merged Gateway `main`:

- idempotency admission is atomic;
- first session binding is atomic;
- runs carry durable revisions;
- stale saves fail closed;
- pause/resume/cancel are current-state atomic transitions;
- runtime return and assistant streaming recheck current run authority;
- owner effects are fenced immediately before delivery;
- graceful restart quiesces old process state mutation;
- dedicated concurrency regressions are included in canonical `npm test`;
- exact-head CI is 6 / 6 PASS;
- exact-head composed acceptance is 4 / 4 PASS;
- merged-main CI is 6 / 6 PASS;
- canonical suite is 113 / 113 PASS on exact head and merged main;
- tested and merged product trees are identical;
- open Gateway PRs are zero.

**WSA-2026-008: CLOSED.**
