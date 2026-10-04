# WSA-2026-050 — Gateway pre-auth CPU admission

**Transition:** ACTIVE -> CLOSED  
**Severity / confidence:** MEDIUM / PROVEN, unchanged  
**Owner:** AI-Verse-Gateway  
**Audited/live pre-repair main:** 3fd9618f693ec71e186cc47da66c2b2694837a17  
**Repair PR:** [AI-Verse-Gateway #36](https://github.com/aiverse-filmmakers/AI-Verse-Gateway/pull/36)  
**Final tested owner head:** 5cfca65d05f599415ae6e7d8d551fe330c478354  
**Merged owner main:** dec450e622b3bdfbb5b0c51cc325ea34a08dcb5d  
**Tested / merged product tree:** a3d9e5a14ba8b2183515f65089179f3216e7c0ae

## Finding and accepted closure law

The audit found synchronous scrypt bearer verification before the only principal-scoped rate limiter. Request-time bearer checks now use asynchronous scrypt, and a fixed-window pre-auth limiter admits work by the TCP peer address before any KDF. Concurrent authentication work is capped at 64 process-wide and 32 per peer. Rate-limit bucket memory is capped at 4,096 and fails closed at capacity.

Only the TCP peer address is trusted. Forwarded client-address headers are ignored. In direct mode the bucket applies to the client transport address; behind a TLS proxy all forwarded users share the proxy peer bucket, and the trusted proxy must enforce any per-client limits.

## Permanent regression coverage

- Asynchronous scrypt remains pending while the event loop gets a turn.
- Pre-auth limiter buckets follow the transport peer, ignore forged X-Forwarded-For, reject over-limit attempts, and fail closed when bucket capacity is exhausted.
- Concurrent pre-auth KDF work is bounded and capacity is released after completion.
- An integrated invalid-bearer flood returns authentication failures while a valid authenticated status request succeeds and the event loop continues making progress.

## Owner validation

| Gate | Exact tested PR head | Merged main |
|---|---:|---:|
| Gateway CI / Node 20 and 22 | 37168685440 — Ubuntu/macOS/Windows 6/6 PASS | 37168784273 — Ubuntu/macOS/Windows 6/6 PASS |
| Context Ladder Integrated Acceptance | 37168685460 — PASS | merged-main CI 37168784273 — 6/6 PASS |
| Temporary Worker Composition | 37168685442 — PASS | merged-main CI 37168784273 — 6/6 PASS |
| Permanent Bot Composition | 37168685438 — PASS | merged-main CI 37168784273 — 6/6 PASS |
| Automation Recommendation Boundary | 37168685444 — PASS | merged-main CI 37168784273 — 6/6 PASS |

The exact tested head and merged main have identical product tree a3d9e5a14ba8b2183515f65089179f3216e7c0ae. Gateway has zero open PRs after merge.

System Contract Validation exact-head and merged-main results will be recorded after both pass.

## Outcome

WSA-2026-050 is closed for AI-Verse-Gateway. This finding-specific closure preserves the whole-system NO-GO verdict and existing release pauses.
