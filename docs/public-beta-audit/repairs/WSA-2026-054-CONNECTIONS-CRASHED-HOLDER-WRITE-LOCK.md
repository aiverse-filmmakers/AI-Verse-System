# WSA-2026-054 — Connections crashed-holder write-lock recovery

**Repair order:** R3.9
**Finding:** WSA-2026-054 (HIGH / PROVEN)
**Owner:** AI-Verse-Connections
**Audited owner baseline:** `65566b6cc99cc8e26bcacf1a985a1f43c6a42fe6`
**Repair PR:** [AI-Verse-Connections #8](https://github.com/aiverse-filmmakers/AI-Verse-Connections/pull/8)
**Exact tested PR head:** `fe2b7a34b5d2d45d31a79f0e6de4d18c3130dc96`
**Merged owner ref:** `938ead7282541a5e92c0bbe3b966dda9a80d2b65`
**Status:** **CLOSED**

## Audit basis and bounded closure

The preserved original audit evidence identifies a persistent `.write.lock` directory with no holder identity or liveness test. A process death before finally-cleanup could wedge lifecycle, registry, idempotency, and terminal receipt mutations; doctor did not report lock health. This closure is limited to WSA-2026-054 and does not close adjacent WSA-2026-055 or later Connections findings.

## Accepted implementation

Connections now writes a complete holder record (random token, PID, host, and acquisition time) to a synced temporary file and atomically links it into place. A writer releases only a lock with its own token. Live local holders are never stolen; unverifiable, foreign-host, malformed, and legacy directory locks fail closed.

A dead local holder can be reclaimed only after a separate cross-process recovery claim is acquired, the exact holder token is reread, the stale lock is moved to token-specific quarantine, and the moved record is verified dead and identical. Doctor reports write-lock health, including stale and unverifiable states. Owned stale/recovery/temp artifacts are included in managed cleanup.

Permanent child-process regressions cover live-holder protection and doctor visibility, killed-holder diagnosis/recovery, five concurrent writers after a process death, crash after reservation, and recovery before publishing the terminal receipt after an external effect. The existing idempotency race test now uses a deterministic final-edge barrier. The package syntax check was made portable across Windows so the full CI matrix can run there.

A legacy directory lock has no trusted holder identity. Doctor reports it as `legacy-unverifiable`; an operator must confirm its old process is gone before removing that exact directory. Age alone is not used to reclaim it.

## Validation evidence

- Dedicated WSA-054 workflow on exact head `37160381903`: Ubuntu, macOS, Windows — **3/3 PASS**.
- Full CI on exact head `37160381905`: Ubuntu/macOS/Windows × Node 20/22 — **6/6 PASS**.
- Dedicated WSA-054 workflow on merged main `37160478608`: Ubuntu, macOS, Windows — **3/3 PASS**.
- Full CI on merged main `37160478577`: Ubuntu/macOS/Windows × Node 20/22 — **6/6 PASS**.
- All eight changed-file blob IDs match exactly between tested head and merged main.
- All seven WSA-054 adversarial regressions pass on merged main.
- Zero open Connections PRs after merge.

The owner acceptance is complete. Canonical System Contract Validation and this register transition are validated by the System PR carrying this packet.
