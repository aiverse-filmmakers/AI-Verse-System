# WSA-2026-025 Closure - Token Pricing Transactionality

**Finding:** `WSA-2026-025`  
**Contradiction:** `C-A1.8-002`  
**Title:** Failed pricing synchronization is not failure-atomic across an immutable snapshot batch  
**Severity / confidence:** MEDIUM / PROVEN, unchanged  
**Owner:** `ai-verse-token`  
**Repair wave:** R3.7  
**Closure date:** 2026-10-03  
**State:** **CLOSED**

## 1. Original failure

The audited pricing store validated an incoming snapshot batch before mutation, but then published each immutable snapshot directly into its final visible location one file at a time.

If a later file write failed, or a competing process committed a conflicting snapshot after prevalidation, the refresh could return failure while earlier snapshots from that same response remained visible to normal pricing reads and therefore to the cost engine.

That violated the required batch-visibility invariant: a failed pricing refresh must not expose a partially committed authoritative snapshot batch.

## 2. Repair identity

**Accepted pre-repair Token ref:** `1a85d0da0e529b659b62d3c9a3e2d40c853d67d3`  
**Accepted pre-repair product tree:** `486cc2da61648e02179e2dbeb0b0c9d448ec6d1f`  
**Repair PR:** `ai-verse-token#2`  
**Final tested PR head:** `d59aa7a8e74bb73eeb23aee123793e2901a200cb`  
**Merged Token ref:** `69b15e59ad117e147730dbc30dfef7cbc083c8de`  
**Tested/merged product tree:** `7f388e99a1d2694e688dc09f23932498ac502388`

The exact tested PR tree and merged Token `main` tree are identical.

## 3. Final pricing publication contract

### 3.1 New batches are staged outside authority

Every newly admitted immutable snapshot batch is first written beneath:

`.snapshot-batch-staging/<batch-id>/`

Normal `get` and `list` reads do not inspect this staging area. A partially staged or crashed batch therefore has no pricing authority.

### 3.2 The complete batch is verified before publication

The staging directory contains the candidate snapshots plus a bounded versioned manifest.

The manifest binds each `price_snapshot_id` to the SHA-256 digest of its canonical serialized content. The staged batch is read back and validated before it can become visible.

### 3.3 Publication has one atomic visibility edge

After complete staging and verification, the whole staging directory is renamed atomically into:

`snapshot-batches/<batch-id>/`

Readers see either no committed batch or the whole committed batch. There is no per-member final-file publication loop for new batches.

Legacy `snapshots/*.json` remain readable for backward compatibility, but new writes use the batch publication contract.

### 3.4 Successful synchronization truth shares the same commit boundary

During repair review, a second transactionality edge was identified: publishing a snapshot batch and subsequently writing its `updated` sync-state observation as separate commits could still let a refresh fail after new prices became visible.

The final repair therefore embeds the successful `updated` sync observation in the committed batch manifest itself.

For an updated response that introduces new snapshots, the snapshot set and successful refresh truth become visible together through the same atomic directory rename.

`syncState(sourceId)` reads both legacy standalone sync-state observations and success observations embedded in committed batches.

A duplicate-only refresh may still write a standalone success observation because it publishes no new snapshot authority.

### 3.5 Cross-process publication is serialized

Batch admission and publication use a cross-process commit lock created with exclusive-create semantics.

The lock records:

- a random ownership token;
- PID;
- hostname;
- acquisition timestamp.

A live local holder is never reclaimed merely because the lock is old.

A dead local holder can be reclaimed only after a short grace period and only after the lock is re-read and its token/owner identity is unchanged.

Release is token-bound. A changed or disappeared lock fails closed instead of being silently deleted.

### 3.6 Competing batches are decided against current committed truth

After acquiring the commit lock, the writer reconstructs currently visible pricing truth and checks every candidate against it.

An exact replay remains a duplicate. A different payload for an already committed `price_snapshot_id` fails with `PRICE_SNAPSHOT_CONFLICT` before the contender publishes anything.

This prevents a prevalidation race from exposing a losing batch subset.

## 4. Permanent adversarial regressions

### Later staged-member I/O failure

A deterministic failure is injected on the second staged snapshot member.

Acceptance proves:

- the first staged member remains non-authoritative;
- neither candidate ID is visible;
- normal listing is empty;
- no committed batch directory exists;
- abandoned in-process staging is cleaned.

### Real cross-process conflicting batch race

Two real processes start together with batches that each contain one unique snapshot plus one shared conflicting snapshot ID.

Acceptance proves:

- exactly one process commits;
- the loser returns `PRICE_SNAPSHOT_CONFLICT`;
- the winner is visible as one complete batch;
- the losing process's unique snapshot never becomes visible.

### Crash after first staged member

A child process exits after writing its first staged snapshot while holding the commit lock.

Acceptance proves:

- the crashed subset is invisible;
- no partial batch is returned by `get` or `list`;
- the next writer safely reclaims the dead local lock;
- the recovery writer publishes its own complete batch.

### Old-but-live commit lock

A deliberately old lock owned by the current live process is installed.

Acceptance proves age alone never authorizes lock theft: the contender times out with `PRICE_STORE_BUSY` and publishes no snapshot.

### Synchronizer success publication

A full `PricingSynchronizer.refreshSource` updated response is exercised.

Acceptance proves the new snapshots and the successful `updated` observation become readable together, with no separate legacy success-state file required.

### Synchronizer publication failure

A deterministic manifest-write failure is injected before the atomic rename.

Acceptance proves:

- refresh returns failed / `SYNC_INVALID`;
- no new snapshot becomes visible;
- the failed observation is recorded safely;
- the failed response cannot influence pricing authority.

## 5. Exact-head acceptance

Final tested PR head: `d59aa7a8e74bb73eeb23aee123793e2901a200cb`

### Focused pricing workflow

`Pricing Transactionality` run `37151667552`: **PASS**.

- Ubuntu Node 22: PASS;
- macOS Node 22: PASS;
- Windows Node 22: PASS;
- **3 / 3 jobs PASS**.

The focused workflow runs both the storage-level and full synchronizer-level WSA-2026-025 regressions.

### Full Token CI

`CI` run `37151667585`: **PASS, 6 / 6 jobs**.

Matrix:

- Ubuntu Node 22: PASS;
- Ubuntu Node 24: PASS;
- macOS Node 22: PASS;
- macOS Node 24: PASS;
- Windows Node 22: PASS;
- Windows Node 24: PASS.

Representative exact-head canonical suite: **268 / 268 tests PASS, 0 fail, 0 skipped**.

Release acceptance: **3 / 3 PASS**.

All six WSA-2026-025 focused regressions are present in the canonical discovered suite.

## 6. Merged-main acceptance

Merged Token ref: `69b15e59ad117e147730dbc30dfef7cbc083c8de`

### Focused pricing workflow

`Pricing Transactionality` run `37151877209`: **PASS**.

- Ubuntu Node 22: PASS;
- macOS Node 22: PASS;
- Windows Node 22: PASS;
- **3 / 3 jobs PASS**.

### Full Token CI

`CI` run `37151877242`: **PASS, 6 / 6 jobs**.

Matrix:

- Ubuntu Node 22: PASS;
- Ubuntu Node 24: PASS;
- macOS Node 22: PASS;
- macOS Node 24: PASS;
- Windows Node 22: PASS;
- Windows Node 24: PASS.

Representative merged-main Ubuntu Node 22 log explicitly reports:

- **268 tests**;
- **268 pass**;
- **0 fail**;
- **0 skipped**.

The same merged-main log explicitly shows all six permanent WSA-2026-025 cases PASS.

Release acceptance: **3 / 3 PASS**.

The exact tested PR tree and merged Token tree are **identical**: `7f388e99a1d2694e688dc09f23932498ac502388`.

Open Token PRs after merge: **0**.

## 7. Finding-specific recheck

### C-A1.8-002

**RESOLVED for WSA-2026-025.**

A failed refresh cannot expose only part of a newly fetched authoritative snapshot batch.

### Later-write failure

**PASS.**

A staged-member failure leaves zero members from the candidate batch visible.

### Cross-process race

**PASS.**

Competing writers serialize against current committed truth and exactly one whole conflicting batch wins.

### Writer crash

**PASS.**

A crash during staging leaves no pricing authority behind, and a later writer can safely recover a dead local commit lock.

### Refresh success truth

**PASS.**

New snapshot authority and the successful `updated` observation share one atomic publication edge.

### Backward compatibility

**PASS.**

Previously committed legacy snapshot files remain readable while all new batch writes use the atomic publication path.

## 8. Adjacent findings remain open

This closure is limited to `WSA-2026-025`.

It does not close Distribution receipt concurrency, Connections crash-safety findings, later Token findings, or any R4-R6 work.

The next dependency-safe finding is:

`R3.8 / WSA-2026-034 - Distribution lifecycle receipt concurrency`.

The whole-system verdict remains **NO-GO**.

## 9. Closure verdict

Required WSA-2026-025 behavior is present on merged Token `main`:

- new immutable snapshot batches stage outside authority;
- complete batch content is validated before publication;
- one atomic directory rename is the visibility edge;
- readers ignore incomplete staging;
- successful updated sync truth is committed with the new snapshot batch;
- competing processes serialize through a token-bound cross-process lock;
- live holders cannot be stolen by age alone;
- dead local holders can be recovered safely;
- later-write failure exposes zero members of the failed batch;
- competing conflicting batches produce exactly one whole winner;
- process crash leaves the staged subset non-authoritative;
- exact-head focused acceptance is 3 / 3 PASS;
- exact-head full CI is 6 / 6 PASS;
- merged-main focused acceptance is 3 / 3 PASS;
- merged-main full CI is 6 / 6 PASS;
- representative canonical suites are 268 / 268 PASS;
- release acceptance is 3 / 3 PASS;
- exact tested and merged product trees are identical.

**WSA-2026-025: CLOSED.**
