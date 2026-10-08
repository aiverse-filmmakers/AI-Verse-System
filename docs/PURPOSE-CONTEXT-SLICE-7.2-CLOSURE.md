# Purpose Context - Slice 7.2 Closure

**Slice:** 7.2 - Context budget/freshness policy  
**Status:** COMPLETE / ACCEPTED FOR CONTINUATION  
**Date:** 2026-10-08  
**Gateway accepted head:** `535beb9c9a02f5da7ae7062fc1a34111232beca8`  
**OS accepted head:** `b2e1b531402bc492e40eafbbcacddb78ec7a46b6`

## Accepted behavior

1. Runtime Purpose has a hard logical envelope maximum of **16,384 bytes**.
2. Gateway requests that same bound from OS and independently rejects owner output above it.
3. OS exposes `os.purpose-budget-policy.v1` with deterministic low-to-high retention priority.
4. Final OS composition re-applies the budget after Data/current-state/profile enrichment so optional rich/material context cannot displace trajectory-critical strategic context merely because it was added later.
5. Mission, goals, strategies, initiatives, and trajectory outrank optional rich context under byte pressure; retained Brain provenance remains synchronized with retained strategic objects.
6. Every Purpose-relevant runtime assembly requires a fresh OS owner read. Gateway Purpose projection-cache reuse is forbidden.
7. Irrelevant tasks continue to perform zero Purpose reads.
8. Genuine owner/process availability failures allow ordinary runtime execution to continue with Purpose absent. No stale Purpose projection is substituted.
9. Scope, authority, provenance, and budget contract violations remain fail-closed and are never relabeled as availability failures.
10. `gateway.purpose-precedence-policy.v1` makes fresh OS owner Purpose outrank stale cached UI/output candidates. Cached candidates remain ignored even during owner unavailability.
11. Gateway remains runtime/context assembler only; OS remains Purpose projection owner throughout.

## Task evidence

- Task 1: Gateway PR #42 exact head `f7065cfa294f1458e3eaca5341922d9d0532186f`, merged `24012566a8bbc866c681d51e2e5920569e67f25c`; CI `37825398472` PASS across Ubuntu/macOS/Windows Node 20/22 including benchmark; Context Ladder `37825398733` and runtime boundaries PASS.
- Task 2: OS PR #53 exact head `1bb4ea254b060021d65ae6d6ef4dcc672e652b01`, merged `45f3734fa4bbaf64e0d72b25b694770e736b9cc1`; Direction Ownership `37828582547` PASS.
- Task 3: OS PR #54 exact head `fe544c6c99d0a2ce2f1a4067fdf7aee00f64a139`, merged/final OS head `b2e1b531402bc492e40eafbbcacddb78ec7a46b6`; Direction Ownership `37829015241` PASS including tight-budget trajectory-preservation proof.
- Task 4: Gateway PR #43 exact head `bec27fd4ed0aba569fb1618985b12f5a4b2318a2`, merged `0d784147c71695803b311c403003d964e59ec27f`; CI `37829416492` PASS across Ubuntu/macOS/Windows Node 20/22 including benchmark; Context Ladder `37829416435` and runtime boundaries PASS.
- Task 5: Gateway PR #44 exact head `6586e471b191ab1caa947564d4da5292cbf3f6eb`, merged `a41fce18aefd0719d416f6100a247aa427d4de00`; CI `37840314915` PASS across Ubuntu/macOS/Windows Node 20/22 including benchmark; Context Ladder `37840315167`, Permanent Bot `37840315025`, Automation Boundary `37840315148`, Temporary Worker `37840315146` PASS.
- Task 6: Gateway PR #45 exact head `246d5447f2a2b4f54be0ab990a08aaf187c34b7d`, merged/final Gateway head `535beb9c9a02f5da7ae7062fc1a34111232beca8`; CI `37840713473` PASS across Ubuntu/macOS/Windows Node 20/22 including benchmark; Context Ladder `37840713435`, Permanent Bot `37840713454`, Automation Boundary `37840713515`, Temporary Worker `37840713474` PASS.

## Acceptance summary

- trivial deterministic work retains zero Purpose owner reads;
- strategic work reaches Purpose only after relevance passes;
- no unrelated workspace is read as a side effect;
- Purpose-unavailable fallback preserves ordinary execution without silently substituting stale Purpose state;
- size, refresh, availability, and precedence behavior are explicit and testable;
- fresh canonical owner reads always outrank cached UI/output artifacts;
- no second Purpose authority was introduced.

## Next

**Slice 7.3 - Real-world Purpose Context value gate.**

Phase 8 remains blocked until Slice 7.3 explicitly records `VALUE PROVEN`.