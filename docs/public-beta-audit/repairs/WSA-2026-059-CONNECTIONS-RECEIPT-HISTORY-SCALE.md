# WSA-2026-059 — Connections receipt-history scale

**Finding:** WSA-2026-059 (A4.5; MEDIUM / PROVEN)  
**Transition:** OPEN -> CLOSED  
**Owner repository:** AI-Verse-Connections  
**Audited owner baseline:** `fb8b10deb6e05656e1e3b97e8d93650d58c57a7b`  
**Repair PR:** [AI-Verse-Connections #12](https://github.com/aiverse-filmmakers/AI-Verse-Connections/pull/12)  
**Final tested owner PR head:** `d46478297f79c31335a5f942ddb4a41b8cce2359`  
**Merged owner ref:** `602a1c52ab782cc9a8b7a4caa60ccb29efe403d1`  
**Tested / merged owner tree:** `cfb2688c673dc8a1ff8c4f3e0114807654d17023`

## Finding and closure law

The audit found that external execution repeatedly scanned lifetime receipt history for idempotency and budget decisions. The repair preserves the append-only receipt log as canonical audit history while adding rebuildable indexed current state for hot idempotency lookups, bounded recent budget partitions, execution recovery, and unresolved effects. Full historical inspection remains an explicit streaming operation.

The latest receipt state is stored in compact hash-partitioned shards. Rebuilds stream canonical history and retain only offsets and execution identity needed to publish current shards. Missing or corrupt derived state rebuilds from canonical receipts; malformed canonical history still fails closed. Same-key replay and legacy execution identity behavior remain intact.

## Permanent regression and scale evidence

- Tail recovery, missing/corrupt shard rebuild, legacy execution identity retention, and canonical-log corruption behavior are covered by permanent regressions.
- Full Connections CI on the exact PR head, run `37174364926` attempt 4: Node 20/22 across Ubuntu, macOS and Windows, 6/6 PASS.
- WSA-054 Write Lock Recovery, run `37174364887` attempt 4: Ubuntu/macOS/Windows, 3/3 PASS.
- WSA-055 External Effect Recovery, run `37174364902` attempt 4: Ubuntu/macOS/Windows, 3/3 PASS.
- WSA-059 Receipt Index Scale, run `37174364891` attempt 4: PASS.
- The scale benchmark seeds 1,000 and 100,000 repeated-key receipts and measures 25 lookup/commit samples, plus distinct-key rebuild memory. The hosted Node 22 run passed.
- Tested PR tree and merged owner tree are identical; Connections has zero open PRs after merge.

## System closure validation

System Contract Validation must be recorded on the closure PR head and on merged System main before this packet is finalised.

## Outcome

WSA-2026-059 is closed for AI-Verse-Connections. The whole-system NO-GO verdict and release pauses remain in force. R4.10 is complete; R5 remains pending until the ordered tracker advances through the next dependency-safe finding.
