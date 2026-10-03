# WSA-2026-055 — Connections unknown external-effect recovery

**Repair phase:** R3.10  
**Severity / confidence:** MEDIUM / PROVEN, unchanged  
**State:** CLOSED after owner and System contract acceptance  
**Contradiction:** C-A4.3-007  
**Original evidence:** E-A4.3-023, E-A4.3-024, E-A4.3-027  
**Owner:** AI-Verse-Connections  
**Audited/live baseline:** 938ead7282541a5e92c0bbe3b966dda9a80d2b65  
**Repair PR:** AI-Verse-Connections #9 — https://github.com/aiverse-filmmakers/AI-Verse-Connections/pull/9  
**Exact tested PR head:** cad314102bfa62776dea453e631ecd215fcd3d59  
**Merged Connections main:** 6f1da00b955ce7b31e20a625a48d866d6c3a7e54

## Original failure

A process could persist a pending idempotency reservation, cross the provider edge, and crash before writing the terminal receipt. The durable state then failed to distinguish a safe pre-edge abandonment from an external effect that may already have occurred. The same key could remain pending indefinitely, attemptedExternal remained false until terminal receipt, and budget truth did not account for the uncertain attempt. Blind replay could duplicate a provider effect.

This closure is limited to unknown external-effect recovery. It does not claim a provider-safe idempotency guarantee: no supported provider contract makes an unknown outcome replay-safe.

## Accepted state and recovery law

- A process/host/token-bound execution reservation records the operation before the external edge.
- The provider-edge marker and unknown external-effect state are durably committed with the budget reservation before any outbound provider call.
- A crash before the provider edge is distinguishable from a crash after it. A dead pre-edge reservation is safely classified as abandoned, its unused reservation is released, and the same key can retry.
- A post-edge crash remains explicitly unknown, blocks same-key replay, appears in doctor output, and counts against rate/day budget until reconciled.
- An operator can use the local reconciliation command only with explicit --resolution, --execution-id, --confirm, and a factual non-secret --note. “Not applied” releases the reservation and permits retry; “applied” permanently fences replay of that key.
- Legacy pending/attempted failures lacking the new boundary marker are unverifiable and fail closed.
- When a provider has no replay-safe idempotency contract, reconciliation requires local operator evidence; the repair does not guess whether the remote effect happened.
- No-key retries of the same capability are fenced while an unresolved outcome exists.

## Permanent adversarial regressions

Child-process crash injection covers four boundaries: execution reservation, budget reservation, provider edge before a response, and provider response before terminal receipt. The suite also proves safe pre-edge retry, post-edge replay fencing, applied/not-applied reconciliation, unknown-budget/doctor visibility, explicit confirmation and note requirements, and legacy fail-closed behavior.

All seven dedicated WSA-2026-055 regression scenarios pass on merged main. The pre-existing adapter-failure regression now reflects the correct post-edge external-unknown state while preserving terminal budget accounting.

## Owner validation and identity

| Gate | Exact tested head | Merged main |
|---|---:|---:|
| Full Connections CI | Run 37162219780, 6/6 PASS; representative suite 49/49 | Run 37162302260, 6/6 PASS |
| WSA-055 focused workflow | Run 37162219755, 3/3 PASS (Ubuntu/macOS/Windows) | Run 37162302267, 3/3 PASS |
| WSA-054 focused workflow | Run 37162219760, 3/3 PASS | Run 37162302270, 3/3 PASS |

The exact PR head and merged main contain identical Git blobs for all ten changed files. Connections has zero open PRs after merge. The owner PR merged at 6f1da00b955ce7b31e20a625a48d866d6c3a7e54.

## Finding-specific outcome

The crash uncertainty identified by C-A4.3-007 is resolved for Connections: the durable state marks uncertainty at the provider boundary, prevents unsafe replay, exposes unresolved work to operators, and accounts for the unknown attempt in budget truth. The operator must not select “applied” or “not applied” without evidence outside the local receipt. This finding-specific closure does not close adjacent Connections findings, the broader A4.3 phase, or the whole-system NO-GO verdict.

System Contract Validation exact-head run 37162833929 passed on this closure PR: Python 3.11 and Python 3.13 both completed all contract tests successfully. The merged-main Contract Validation run is required and will be recorded after merge.
