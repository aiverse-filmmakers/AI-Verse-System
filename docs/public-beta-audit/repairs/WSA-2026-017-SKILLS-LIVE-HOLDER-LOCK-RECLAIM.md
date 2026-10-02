# WSA-2026-017 Closure - Skills Live-Holder Lock Reclaim

**Finding:** `WSA-2026-017`  
**Severity / confidence:** HIGH / PROVEN  
**Owner:** `AI-Verse-Skills`  
**Repair wave:** R3.3  
**Closure date:** 2026-10-02  
**State:** **CLOSED**

## 1. Finding

Skills lifecycle serialization used an exclusive lock file containing holder metadata, but stale recovery was based on file age alone.

At the audited baseline, when the lock file was older than `LOCK_STALE_SECONDS = 300`, a contender unlinked it without checking whether the recorded holder process was still alive.

A valid long-running install, update, rollback, uninstall or learning mutation could therefore lose its serialization lock while still executing, allowing a second canonical mutation to overlap.

**Contradiction:** `C-A1.5-002`.

Required closure evidence:

- stale recovery must be holder-aware;
- an old lock held by a live process must not be reclaimed;
- a stale lock left by a dead/crashed process must still be recoverable;
- cross-platform lifecycle serialization must remain green.

## 2. Baseline and repair identity

**Pre-repair Skills ref:** `3541d2a7af1b20ca12736ed7454d119295d8e193`  
**Open Skills PRs before repair:** 0

**Repair branch:** `repair/wsa-2026-017-live-holder-lock-reclaim`  
**Repair PR:** `AI-Verse-Skills#16`  
**Final tested PR head:** `8705a1f31d7b25ca03176c9936e76e631a9bb78d`  
**Merged Skills ref:** `4fc240593929ebce9d82632479384d1cd45980b7`  
**Tested/merged product tree:** `92fb45c0ec4e6a6b4e88805ab491a06c0d5a2f1e`

The exact final PR head and merged `main` commit have the same product tree.

Open Skills PRs after merge: **0**.

## 3. Final implementation contract

### 3.1 Age alone no longer authorizes stale-lock deletion

The existing lifecycle lock path and exclusive-create acquisition contract remain unchanged.

When a lock file is older than the stale threshold, Skills now inspects its recorded holder before any reclaim is considered.

A stale lock is removed only when the holder can be positively identified as dead.

### 3.2 New lock metadata carries local holder identity

New lifecycle locks record:

- unique lock token;
- holder PID;
- holder hostname;
- acquisition timestamp.

The hostname prevents a process on one machine from treating a PID from a different host as local authority.

Legacy lock files without a hostname remain compatible by treating their recorded PID as local legacy metadata.

### 3.3 POSIX holder liveness is checked directly

On POSIX systems Skills uses process-signal liveness probing with signal 0.

Semantics:

- process lookup failure means dead;
- permission denied means a process exists and is therefore treated as live;
- unexpected probe errors are treated as unknown;
- the current process is always recognized as live.

Unknown state does not authorize reclaim.

### 3.4 Windows holder liveness uses process state, not destructive signaling

Windows does not use `os.kill(pid, 0)`.

Skills opens the process with `PROCESS_QUERY_LIMITED_INFORMATION` and reads its exit code.

Semantics:

- `STILL_ACTIVE` means live;
- invalid PID means dead;
- access/inspection failure means unknown and fails closed.

This preserves the same holder-aware law on Windows without risking destructive signal semantics.

### 3.5 Foreign or unverifiable holders fail closed

A stale lock is not reclaimed when:

- its hostname identifies another host;
- its JSON metadata is malformed;
- its PID is invalid or missing;
- holder liveness cannot be determined safely;
- process inspection is denied or otherwise inconclusive.

The contender remains bounded by the existing lifecycle lock timeout and receives the existing busy error instead of deleting an unverified lock.

### 3.6 Reclaim rechecks lock identity before unlink

When a stale local holder is proven dead, Skills records the observed lock token and re-reads the lock immediately before deletion.

Reclaim proceeds only if the current lock still carries the same non-empty token.

A holder change detected during stale evaluation therefore prevents deletion of the changed lock.

### 3.7 Normal release ownership remains token-bound

Normal cleanup is unchanged: a process releases the lock only when the current file token matches the token it acquired.

The repair changes stale recovery authority only.

## 4. Permanent regressions

The existing lifecycle suite now includes two dedicated WSA-2026-017 regressions.

### 4.1 Live old holder cannot be reclaimed

The test:

1. acquires the real lifecycle lock;
2. artificially ages its mtime beyond the 300-second stale threshold;
3. starts a contender while the original holder remains live;
4. proves the contender times out with the existing lifecycle-busy error;
5. proves the lock still exists while the holder remains active;
6. proves normal owner cleanup removes it afterward.

This deterministically reproduces the original failure condition without waiting five minutes.

### 4.2 Dead/crashed holder is recoverable

The test starts a child Python process that acquires the real lifecycle lock and exits through `os._exit(0)`, deliberately bypassing context-manager cleanup.

The parent then:

1. confirms the orphan lock remains;
2. confirms the recorded PID is not the parent PID;
3. artificially ages the lock beyond the stale threshold;
4. acquires the lifecycle lock successfully;
5. confirms the recovered lock now belongs to the parent and uses a new token;
6. confirms normal cleanup removes the recovered lock.

This proves holder-aware safety does not strand legitimate crashed-holder recovery.

## 5. PR-head validation

### Validate AI-Verse Skills

Workflow:

`37063765194`

Result: **PASS**

Representative discovered suite:

**131 / 131 tests PASS**

Both dedicated WSA-2026-017 tests are present in the canonical discovered suite.

### Lifecycle Controller Containment

Workflow:

`37063765080`

Exact-head matrix:

- Ubuntu Python 3.9: **PASS**
- Ubuntu Python 3.12: **PASS**
- macOS Python 3.9: **PASS**
- macOS Python 3.12: **PASS**
- Windows Python 3.9: **PASS**
- Windows Python 3.12: **PASS**
- matrix: **6 / 6 PASS**

Representative lifecycle suite:

**12 / 12 tests PASS**

This workflow compiles the lifecycle modules and runs the immutable lifecycle/controller containment regressions on every matrix entry.

### Full E2E Install

Workflow:

`37063765131`

Result: **PASS**

The end-to-end path completed:

- registry and generation validation;
- full pinned upstream install;
- provider-v1 validation;
- setup and doctor;
- generation pin/adaptation;
- immutable update;
- pointer-only rollback;
- uninstall while retaining pinned generation bytes;
- recovery after uninstall.

## 6. Post-merge validation

Merged-main ref:

`4fc240593929ebce9d82632479384d1cd45980b7`

### Validate AI-Verse Skills

Workflow:

`37064093509`

Result: **PASS**

Representative suite:

**131 / 131 tests PASS**

Both dedicated WSA-2026-017 regressions are present after merge.

### Lifecycle Controller Containment

Workflow:

`37064093519`

Merged-main matrix:

- Ubuntu Python 3.9/3.12: **PASS**
- macOS Python 3.9/3.12: **PASS**
- Windows Python 3.9/3.12: **PASS**
- matrix: **6 / 6 PASS**

Representative lifecycle suite:

**12 / 12 tests PASS**

### Full E2E Install

Workflow:

`37064093517`

Result: **PASS**

All external-install, provider, update, rollback, uninstall and recovery steps completed successfully.

The tested PR-head tree and merged-main tree are identical:

`92fb45c0ec4e6a6b4e88805ab491a06c0d5a2f1e`

## 7. Finding-specific recheck

### C-A1.5-002

**RESOLVED for WSA-2026-017.**

Stale age is no longer sufficient authority to remove a lifecycle lock.

### Live old holder

**PASS.**

A lock older than the stale threshold remains protected when its recorded holder process is alive.

### Dead/crashed holder

**PASS.**

A stale orphan lock left by a process that exited without cleanup is reclaimed after the holder is proven dead.

### Cross-platform holder awareness

**PASS.**

The lifecycle containment matrix passes on Ubuntu, macOS and Windows under Python 3.9 and 3.12.

### Existing lifecycle behavior

**PASS.**

Normal serialization, generation lifecycle, install/update/rollback/uninstall and end-to-end recovery remain green.

## 8. Adjacent findings remain open

This closure is limited to `WSA-2026-017`.

The next dependency-safe finding is:

`R3.4 / WSA-2026-053 - Data natural-key uniqueness`.

Explicitly unchanged:

- `WSA-2026-018` Skills active execution generation retention;
- `WSA-2026-019` Skills release/bootstrap identity;
- later lifecycle, migration, retention and release findings.

The whole-system verdict remains **NO-GO**.

## 9. Closure verdict

Required WSA-2026-017 behavior is present on merged Skills `main`:

- stale age alone cannot reclaim a live holder;
- holder identity is recorded with PID and hostname;
- POSIX and Windows liveness are checked safely;
- unknown or foreign holder state fails closed;
- dead/crashed holders remain recoverable;
- lock token identity is rechecked before stale unlink;
- normal token-bound release semantics remain intact;
- exact-head Validate workflow passes with 131 / 131 tests;
- exact-head lifecycle matrix is 6 / 6 PASS;
- exact-head E2E is PASS;
- merged-main Validate workflow passes with 131 / 131 tests;
- merged-main lifecycle matrix is 6 / 6 PASS;
- merged-main E2E is PASS;
- tested and merged product trees are identical;
- open Skills PRs are zero.

**WSA-2026-017: CLOSED.**
