# WSA-2026-058 — Gateway idempotency scale

**Finding:** WSA-2026-058 (A4.5; HIGH / PROVEN)  
**Transition:** OPEN -> CLOSED  
**Owner repository:** AI-Verse-Gateway  
**Audited owner baseline:** `dec450e622b3bdfbb5b0c51cc325ea34a08dcb5d`  
**Repair PR:** [AI-Verse-Gateway #37](https://github.com/aiverse-filmmakers/AI-Verse-Gateway/pull/37)  
**Final tested owner PR head:** `c73f803315cdafbbe0daed46fb8b00579683ba3f`  
**Merged owner ref:** `089aaa6440bbbbb9f41195eafe123ad2e06d5625`  
**Exact tested and merged owner tree:** `2e802e3039a9cffaf61ac6fe627c00fadca89bd2`

## Finding and closure law

The audit found that every idempotency claim and commit read, parsed and rewrote the full `state/idempotency.json` map. Unique Automation invocation IDs caused unbounded history growth and per-operation work that scaled with all prior records.

Idempotency state is now indexed into SHA-256-keyed record files. A claim becomes visible through one atomic exclusive link; complete writes are staged before publication. Commits serialize across processes and atomically replace one record. Legacy migration publishes its completion marker only after copying and verifying the records, making interrupted migration restart-safe. Stale lock recovery is covered. No time-based expiry is added because the existing replay and changed-payload rejection contract has no established safe retention horizon.

## Permanent regression and scale evidence

- Multiple store instances and processes cannot both reserve one idempotency key.
- Replay and changed-payload conflict behavior remain intact.
- Interrupted legacy migration resumes safely; stale lock recovery works.
- State survives close/reopen and remains available to uninstall/replay workflows.
- Canonical CI benchmark seeds 1,000 and 100,000 records and times 25 claim+commit samples using the Gateway store. Ubuntu Node 22 median: 3.045 ms at 1,000 records; 3.312 ms at 100,000 records (1.09x).
- Exact-head CI `37171337867`: six Node 20/22 Ubuntu/macOS/Windows jobs passed.
- Permanent Bot Composition `37171337863`, Automation Recommendation Boundary `37171337866`, Context Ladder Integrated Acceptance `37171337875`, and Temporary Worker Composition `37171337916`: PASS.
- Merged-main CI `37171433540`, attempt 2: all six jobs passed and the benchmark ran. The initial run's unrelated over-budget review assertion failure passed on retry at the same immutable merged commit.
- Tested PR head and merged owner main have identical tree `2e802e3039a9cffaf61ac6fe627c00fadca89bd2`; open Gateway PRs after merge: 0.

## System closure validation

| Gate | System ref | Contract Validation run | Python 3.11 | Python 3.13 |
|---|---|---:|---|---|
| Exact closure PR head | `37ef89a67b658a9029f55c3a9e9cfc92bfc86daa` | `37171700305` | PASS | PASS |
| Merged System main | `2d71fe8532a9968753ff39926a5d05d435b42722` | `37171736538` | PASS | PASS |

Both runs validate the exact System closure head and its merged-main record.

The canonical register and tracker record WSA-2026-058 as CLOSED and WSA-2026-059 as ACTIVE. Whole-system NO-GO, Dashboard MC1.4 pause, and owner-dogfood pause remain in force.

## Outcome

WSA-2026-058 is closed for AI-Verse-Gateway. No whole-system release gate is released.
