# AI-Verse Repository State Ledger

> GENERATED FILE. Do not hand-edit. Machine truth is `governance/repository-registry.json` for static facts and `governance/repository-state.json` for dynamic facts.

Regenerate with `python scripts/refresh_repository_state.py --write-ledger`. Verify with `python scripts/refresh_repository_state.py --check-ledger`.

## Snapshot

- State schema: `ai-verse.repository-state/v1`
- Registry binding blob: `175c269a7f8b036bab6f2378ecb794836d002f93`
- Refresh mode: `full-refresh`
- Refresh scope: `global`
- Refresh status: `complete`
- Refresh evidence revision: `7a54cea11fc6fac160cc2c8e62bc262e5f335e72`
- Last full refresh: `7a54cea11fc6fac160cc2c8e62bc262e5f335e72`
- Watchdog: `WATCHDOG-CURRENT`
- Watchdog reason: Successful Registry-derived global heartbeat at 2026-10-12T16:56:00Z; all registered repositories were scanned with no access/fetch failure.

## Repository state

| Repository | Component | Observed HEAD | Owner acceptance | Distribution pin | Descriptor | System sync | Freshness |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aiverse-filmmakers/AI-Verse-System | ai-verse-system | `7a54cea11fc6` | not-applicable | not-applicable | not-applicable | not-applicable | fresh / global |
| aiverse-filmmakers/ai-verse-distribution | ai-verse-distribution | `90f175418f8d` | unverified | not-applicable | not-applicable | unverified | fresh / global |
| aiverse-filmmakers/AI-Verse-OS | ai-verse-os | `64f7325444d1` | accepted `9600929b9467` | pinned `64f7325444d1` / core-first-run-rc1-2026-10-12 | observed `9600929b9467` / accepted | unverified | fresh / global |
| aiverse-filmmakers/AI-Verse-Brain | ai-verse-brain | `69f7912eeb35` | unverified | pinned `69f7912eeb35` / core-first-run-rc1-2026-10-12 | observed `75e1d713a422` / development | unverified | fresh / global |
| aiverse-filmmakers/AI-Verse-Memory | ai-verse-memory | `f1327be48ba2` | unverified | pinned `f1327be48ba2` / core-first-run-rc1-2026-10-12 | observed `3f715bf43c8d` / development | unverified | fresh / global |
| aiverse-filmmakers/AI-Verse-Skills | ai-verse-skills | `afde5c06307f` | unverified | pinned `afde5c06307f` / core-first-run-rc1-2026-10-12 | observed `fa455961c176` / development | unverified | fresh / global |
| aiverse-filmmakers/AI-Verse-Data | ai-verse-data | `f8978f8f7a1b` | unverified | pinned `f8978f8f7a1b` / core-first-run-rc1-2026-10-12 | observed `5cbf9908440c` / development | unverified | fresh / global |

## Open drift

| Severity | Scope | Drift | Repositories | Reason | Required action |
| --- | --- | --- | --- | --- | --- |
| BLOCKING | Core | core-owner-acceptance-exact-ref-gap | ai-verse-os, ai-verse-brain, ai-verse-memory, ai-verse-skills, ai-verse-data | The current Core release is Distribution-qualified and pins the live Core heads, but the component descriptor surface does not certify exact owner acceptance for those shipped revisions. OS points to an older accepted revision; Brain, Memory, Skills and Data point to older development revisions. This does not prove the shipped revisions were untested; it means the current owner descriptor surface cannot alone prove exact owner acceptance. | Extend and adopt the one canonical Component Release Descriptor and owner handoff so future Core release admission can bind exact accepted owner revisions and evidence. Do not create a second compatibility or acceptance format. |
| WARNING | Core | core-maintainer-handoff-uneven | ai-verse-os, ai-verse-brain, ai-verse-memory, ai-verse-skills, ai-verse-data | Root-level cross-repository maintainer handoff guidance remains uneven across the five Core owner repositories. | Add minimal owner-specific source-only maintainer handoff in Slice 4.2 without copying global governance into component repositories. |
| WARNING | Core | distribution-adapter-compatibility-shadow-risk | ai-verse-distribution | Distribution contains hard-coded supported revision and command knowledge in trusted adapters. This is legitimate orchestration today but must not become a second compatibility or owner-acceptance authority. | Bind future admission to Registry, descriptor and owner evidence while retaining Distribution trusted argv routing. |
| WARNING | Core | purpose-context-blueprint-lag | ai-verse-system | The stable System Blueprint still lags newer accepted Purpose Context implementation truth. | Reconcile current System truth evidence-first in Slice 3.3 without reverting accepted implementation merely because a stable document lags. |
| INFO | Core | compact-release-receipt-not-yet-implemented | ai-verse-distribution | Durable release reconstruction evidence exists across current release-set and qualification files, but the planned compact single release receipt binding is not implemented yet. | Implement the compact immutable release receipt in Slice 5.4 without replacing existing qualification evidence. |

## Authority and freshness rules

- This ledger is a projection only and is never machine authority.
- Static repository identity, ownership and lifecycle facts come only from the Registry.
- Dynamic HEADs, pins, descriptor observations, acceptance evidence, sync state, freshness, watchdog state and drift come only from Repository State.
- Dates are informational only. Exact Git identity, evidence refs and refresh scope determine freshness and lineage.
- `WATCHDOG-STALE` and `WATCHDOG-FAILED` are not CLEAN. A valid scoped refresh may prove a scoped decision while the full watchdog is stale, subject to the governance contract.
- Any intersecting or global `BLOCKING` drift blocks the relevant future release decision until reconciled.
