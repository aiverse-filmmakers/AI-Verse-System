# WSA-2026-032 Closure - Connections Final-Edge Lifecycle and Budget Authority

**Finding:** `WSA-2026-032`  
**Severity / confidence:** HIGH / PROVEN  
**Owner:** `AI-Verse-Connections`  
**Repair wave:** R1.10  
**Closure date:** 2026-10-02  
**State:** **CLOSED**

## 1. Finding

Connections reloaded connection-level authority before provider execution, but did not recompute the complete documented authority intersection.

Specifically:

- component lifecycle readiness was checked only at function entry;
- rate/day budgets were checked before the final edge;
- concurrent calls with distinct idempotency keys could observe the same remaining budget;
- a disable/uninstall between planning and provider execution could therefore leave a planned call unfenced.

Canonical contradiction: `C-A1.10-004`.

Required closure evidence:

1. re-read lifecycle state immediately before adapter execution;
2. make budget check/reservation atomic across concurrent calls;
3. count provider-edge reservations in usage;
4. terminalize reservation state consistently;
5. add deterministic disable/uninstall and minute/day concurrency races.

## 2. Baseline and repair identity

**Pre-repair Connections ref:** `63f8698545d731654f76684bf6ba40248996fc6a`  
**Open Connections PRs before repair:** 0

**Repair branch:** `repair/wsa-2026-032-final-edge-authority`  
**Repair PR:** `AI-Verse-Connections#7`  
**Final tested PR head:** `303741c330cca01bfef6dc90af03f7ca49c3f47b`  
**Merged Connections ref:** `65566b6cc99cc8e26bcacf1a985a1f43c6a42fe6`  
**Tested/merged product tree:** `150a6fcd5a8916a0b06257e4dac1397446492ef6`

The final tested PR head and merged `main` commit have the same product tree.

Open Connections PRs after merge: **0**.

## 3. Final implementation contract

### 3.1 Lifecycle is re-read at the final provider edge

A shared `assertComponentReady()` check now protects both the initial planning stage and the final provider edge.

Immediately before adapter execution, under the Connections state lock, execution re-reads:

- lifecycle installed state;
- setup state;
- enabled state;
- installation system binding;
- current connection record;
- current connection/capability authority.

A disable or non-purge uninstall that occurs after initial planning therefore wins before the adapter can execute.

### 3.2 Complete current connection authority is recomputed

Inside the same final-edge lock, Connections re-runs:

- installation system binding;
- connection enabled/configured/live-verified/healthy/authorized/approved state;
- system scope;
- workspace scope;
- capability admission;
- review-required state;
- delegated capability;
- per-action approval;
- capability fingerprint/risk continuity.

This preserves the previous connection-level final-edge protections while adding lifecycle and budget authority.

### 3.3 Budget check and reservation are atomic

The final-edge state lock now covers:

1. current lifecycle re-read;
2. current registry re-read;
3. current effective limits;
4. receipt history read;
5. rate/day budget check;
6. provider-edge budget reservation append.

Two distinct executions cannot both observe and consume the same final remaining call slot.

### 3.4 Provider-edge reservations count immediately

Before leaving the final-edge lock, Connections appends a dedicated budget reservation receipt containing:

- `budgetReserved: true`;
- a unique `budgetReservationId`;
- connection/capability identity;
- provider identity;
- timestamp and caller scope.

Budget calculation counts:

- current provider-edge budget reservations; and
- historical attempted-external receipts that predate the reservation model.

Terminal receipts linked to a reservation are not double-counted.

### 3.5 Reservation terminalization

Successful, provider-error and thrown provider-edge outcomes carry the same `budgetReservationId` and `budgetState: terminal`.

This gives every normal provider-edge reservation an explicit terminal result while preserving one budget count per attempted edge.

If the final lifecycle/connection/budget authority check rejects before a provider-edge budget reservation is created, any earlier idempotency `pending` hold is terminalized as a pre-provider failure with:

- `attemptedExternal: false`;
- `preProvider: true`;
- the exact authority/budget error code.

This prevents deterministic final-edge rejections from leaving a supported idempotency key permanently stuck in `pending`.

Crash-recovery behavior remains a separate later finding and is not claimed fixed here.

## 4. Permanent regressions

Dedicated coverage was added in:

`test/connections-final-edge-authority.integration.test.js`

The suite proves:

1. disable after planning is observed at the final edge;
2. uninstall after planning is observed at the final edge;
3. neither lifecycle race reaches the external provider;
4. pre-provider idempotency holds terminalize as local failures;
5. two executions with distinct idempotency keys are forced to the same final edge;
6. with `maxCallsPerMinute: 1`, exactly one execution succeeds and one receives `RATE_LIMIT_EXCEEDED`;
7. exactly one external provider call occurs;
8. with `maxCallsPerDay: 1`, exactly one execution succeeds and one receives `DAILY_BUDGET_EXCEEDED`;
9. exactly one provider-edge budget reservation is counted;
10. successful terminal receipt links to that reservation;
11. the losing idempotency hold terminalizes before provider execution;
12. a deterministic adapter failure terminalizes its provider-edge budget reservation;
13. that failed provider-edge reservation still consumes the configured call budget.

## 5. Validation evidence

### PR-head acceptance

Final PR-head Actions run:

`37015229692`

On exact final head `303741c330cca01bfef6dc90af03f7ca49c3f47b`:

- Ubuntu / Node 20: **PASS**
- Ubuntu / Node 22: **PASS**
- macOS / Node 20: **PASS**
- macOS / Node 22: **PASS**
- Windows / Node 20: validation harness failure before tests
- Windows / Node 22: validation harness failure before tests

Representative successful exact-head suite:

- tests: **38**
- passed: **38**
- failed: **0**

All five dedicated WSA-2026-032 regression tests passed.

### Post-merge acceptance

Post-merge Actions run:

`37015386279`

On merged `main` ref `65566b6cc99cc8e26bcacf1a985a1f43c6a42fe6`:

- Ubuntu / Node 20: **PASS**
- Ubuntu / Node 22: **PASS**
- macOS / Node 20: **PASS**
- macOS / Node 22: **PASS**
- Windows / Node 20: validation harness failure before tests
- Windows / Node 22: validation harness failure before tests

Representative merged-main suite:

- tests: **38**
- passed: **38**
- failed: **0**

### Windows CI limitation

The Windows jobs still fail before `npm test` because the existing package script contains shell globs:

`node --check src/*.js && node --check src/providers/*.js && node --check bin/*.js && npm test`

PowerShell passes those globs literally, causing Node to fail on `src/*.js` with `MODULE_NOT_FOUND`.

This is the same pre-existing validation-harness issue recorded during the preceding Connections repairs. No Windows product-test failure is attributed to WSA-2026-032.

## 6. Finding-specific recheck

### C-A1.10-004

**RESOLVED for WSA-2026-032.**

The final provider-edge authority calculation now includes component readiness and current usage budgets.

### Disable/uninstall race

**PASS.**

Concurrent lifecycle narrowing after planning prevents provider execution.

### Per-minute budget race

**PASS.**

Distinct idempotency keys cannot both cross one remaining per-minute slot.

### Per-day budget race

**PASS.**

Distinct idempotency keys cannot both cross one remaining per-day slot.

### Provider-edge reservation accounting

**PASS.**

The budget slot is reserved atomically before adapter execution and is visible to concurrent executions immediately.

### Terminalization

**PASS.**

Normal provider-edge outcomes link back to their budget reservation, and deterministic pre-provider final-edge failures terminalize earlier idempotency holds without claiming an external attempt.

## 7. Adjacent findings remain open

This closure is limited to `WSA-2026-032`.

The following later Connections findings remain open in their ordered waves, including crash recovery, receipt scaling and provider-error privacy findings.

Dashboard R1.11-R1.13 findings are also untouched.

No Dashboard implementation, crash-recovery protocol, receipt indexing, provider-error redaction or unrelated CI behavior was changed.

## 8. Closure verdict

Required WSA-2026-032 closure behavior is present on merged Connections `main`:

- lifecycle is re-read immediately before the provider edge;
- current installation/connection/capability authority is recomputed;
- rate/day budget check plus reservation is atomic;
- provider-edge reservations count immediately against the budget;
- concurrent distinct-key races cannot oversubscribe a one-call budget;
- disable/uninstall races are fenced before provider execution;
- terminal provider receipts link to the reservation;
- deterministic pre-provider failures terminalize idempotency holds;
- exact-head and post-merge Ubuntu/macOS Node 20/22 checks pass;
- representative exact-head and merged-main suites are 38/38;
- tested and merged product trees are identical;
- open owner PRs are zero.

The pre-existing Windows glob-expansion validation-harness defect remains outside this repair.

**WSA-2026-032: CLOSED.**
