# WSA-2026-052 Closure Packet

**Finding:** `WSA-2026-052`  
**Contradiction:** `C-A4.2-007`  
**Title:** OS semantic migration source concurrency  
**Severity / confidence:** HIGH / PROVEN, unchanged  
**Owner:** `AI-Verse-OS`  
**Repair wave:** R3.5  
**Status:** CLOSED after owner repair, merged-main recheck and canonical System acceptance

## 1. Original failure

The semantic migration importer derived an import identity from both the source digest and classifier plan digest, then checked for prior same-source receipts before executing owner effects. The first durable receipt was written only after those effects.

Two concurrent first imports for one source could therefore both observe no prior receipt, choose different classifier plans, derive different plan-dependent owner idempotency keys, and execute divergent owner writes before either receipt existed.

This violated source-level migration idempotency. The source, not a classifier plan, must serialize first-import authority.

## 2. Repair identity

- Restored pre-repair OS baseline: `9f0f07f8b7f68b3297b732ae4ca296a6a102c7d8`
- Baseline product tree: `3710b9e747c265429b31f3d006d99b82bce683b9`
- Repair PR: `AI-Verse-OS#46`
- Final tested PR head: `ab9e10abd44417707761f8479e46c9ea8f7c3f59`
- Merged OS ref: `9effe3869a87fb2c11287ae4821f93620abcc055`
- Tested and merged product tree: `3868653c83d22f3f43f09f113ef18b8341dd6357`

A temporary empty file was accidentally created and immediately removed on OS `main` before the repair branch was created. The restored baseline tree was verified identical to the preceding product tree, so no product drift entered this repair.

## 3. Accepted repair

The owner now establishes source authority before any migration owner effect:

- normal semantic imports acquire a per-source cross-process file lock;
- POSIX uses `fcntl.flock`; Windows uses `msvcrt.locking`;
- first admission writes a durable `in-progress` source reservation before owner actions;
- the reservation binds `source_sha256`, the winning `plan_sha256`, and `import_key`;
- a concurrent same-source import waits for the source lock instead of executing in parallel;
- after the first import commits, later same-source calls replay the committed source result, including reclassified plans;
- an interrupted reservation may be resumed only with the originally bound plan/import identity;
- a different plan presented while a source is interrupted fails closed until the bound recovery completes;
- if a canonical receipt exists after a crash but the reservation was not finalized, the next admission adopts that receipt and marks the source committed;
- more than one pre-existing same-source receipt fails closed for reconciliation instead of choosing arbitrarily;
- migration Data candidate `created_at` is stable across an interrupted-plan retry so owner idempotency payloads remain replay-compatible;
- clarification-resolution imports retain their existing independent path and were not broadened into this repair.

The coordination directories are also created with first-run race tolerance and then revalidated for directory/symlink safety.

## 4. Permanent regressions

`AI-Verse-OS/scripts/test-migration-source-concurrency.py` uses real subprocesses sharing one OS root and covers:

1. concurrent same source / same plan: exactly one owner effect, one canonical receipt, one replay;
2. concurrent same source / different plans: exactly one plan wins, exactly one owner effect occurs, the loser source-replays the committed winner;
3. crash after an owner effect but before the migration receipt: the source remains durably `in-progress`, a different plan fails closed, the bound plan recovers using the same owner idempotency identity without duplicating the already-fired effect, and later reclassification replays the committed source.

Permanent workflow: `.github/workflows/migration-source-concurrency.yml`, running the focused suite on Ubuntu, macOS and Windows.

## 5. Exact-head acceptance

PR exact head `ab9e10abd44417707761f8479e46c9ea8f7c3f59`:

- `Migration Source Concurrency` run `37127337259`: Ubuntu/macOS/Windows, **3 / 3 PASS**;
- `Repository QC` `37127337229`: PASS;
- `OS Brain Permission Contract` `37127337249`: PASS;
- `OS Write Command Boundary` `37127337244`: PASS;
- `Data Natural-Key Routing` `37127337223`: PASS;
- `Five-Component Public Beta` `37127337257`: PASS;
- `Invisible Intelligence Automation Consent` `37127337251`: PASS;
- `Invisible Intelligence Temporary Worker` `37127337280`: PASS;
- `Invisible Intelligence Permanent Bot Consent` `37127337231`: PASS;
- `Direction Ownership` `37127337232`: PASS;
- `Four Repo Acceptance` `37127337234`: PASS.

All **11 / 11** triggered workflow groups passed on the exact reviewed head.

Pre-PR focused validation also passed compilation, the existing migration-import regression suite, the existing semantic-migration clarification suite, and all three new concurrency/crash regressions.

## 6. Merged-main acceptance

Merged OS `main` ref `9effe3869a87fb2c11287ae4821f93620abcc055` has the exact same product tree as the tested PR head.

All **8 / 8** merged-main workflow groups passed:

- `Migration Source Concurrency` `37127474697`: Ubuntu/macOS/Windows, **3 / 3 PASS**;
- `Repository QC` `37127474755`: PASS;
- `OS Brain Permission Contract` `37127474737`: PASS;
- `OS Write Command Boundary` `37127474716`: PASS;
- `Data Natural-Key Routing` `37127474730`: PASS;
- `Direction Ownership` `37127474692`: PASS;
- `Four Repo Acceptance` `37127474710`: PASS;
- `Five-Component Public Beta` `37127474779`: PASS.

The focused merged-main jobs explicitly passed the `Prove source-level serialization and crash recovery` step on Windows, macOS and Ubuntu.

## 7. Finding-specific recheck

- concurrent same-source same-plan first import: RESOLVED;
- concurrent same-source different-plan first import: RESOLVED;
- durable source reservation before owner effects: PROVEN;
- process-level source serialization across supported OS families: PROVEN;
- plan/result binding to one source reservation: PROVEN;
- crash after owner effect with bound-plan recovery: PROVEN;
- reclassified contender during interrupted import: FAILS CLOSED;
- post-commit reclassification: SOURCE REPLAY;
- duplicate/divergent owner write under the tested races: NOT OBSERVED, exactly one owner effect;
- `C-A4.2-007`: RESOLVED for `WSA-2026-052`.

## 8. Scope and residual program state

This closure does not close `WSA-2026-014` or any later migration/lifecycle finding. Memory migration handoff atomicity remains independently open and is the next dependency-safe R3 repair.

The whole-system public-beta verdict remains **NO-GO** until the ordered repair program and bounded final recheck complete.
