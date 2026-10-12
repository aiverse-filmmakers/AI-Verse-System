# AI-Verse Repository State Ledger

> GENERATED FILE. Do not hand-edit. Machine truth is `governance/repository-registry.json` for static facts and `governance/repository-state.json` for dynamic facts.

Regenerate with `python scripts/refresh_repository_state.py --write-ledger`. Verify with `python scripts/refresh_repository_state.py --check-ledger`.

## Snapshot

- State schema: `ai-verse.repository-state/v1`
- Registry binding blob: `175c269a7f8b036bab6f2378ecb794836d002f93`
- Refresh mode: `scoped-refresh`
- Refresh scope: `Core`
- Refresh status: `complete`
- Refresh evidence revision: `84afaa49a77bc8c9869a0172e13f2c9f61718ddc`
- Last full refresh: `0ace417725831e0ba3843fdc77a27d578b3b3010`
- Watchdog: `WATCHDOG-CURRENT`
- Watchdog reason: Successful Registry-derived global heartbeat at 2026-10-12T17:02:00Z; all registered repositories were scanned with no access/fetch failure.

## Repository state

| Repository | Component | Observed HEAD | Owner acceptance | Distribution pin | Descriptor | System sync | Freshness |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aiverse-filmmakers/AI-Verse-System | ai-verse-system | `84afaa49a77b` | not-applicable | not-applicable | not-applicable | not-applicable | fresh / Core |
| aiverse-filmmakers/ai-verse-distribution | ai-verse-distribution | `90f175418f8d` | unverified | not-applicable | not-applicable | unverified | fresh / Core |
| aiverse-filmmakers/AI-Verse-OS | ai-verse-os | `866359d877bf` | accepted `64f7325444d1` | pinned `64f7325444d1` / core-first-run-rc1-2026-10-12 | observed `64f7325444d1` / accepted | unverified | fresh / Core |
| aiverse-filmmakers/AI-Verse-Brain | ai-verse-brain | `4406d1506828` | accepted `69f7912eeb35` | pinned `69f7912eeb35` / core-first-run-rc1-2026-10-12 | observed `69f7912eeb35` / accepted | unverified | fresh / Core |
| aiverse-filmmakers/AI-Verse-Memory | ai-verse-memory | `09911eae0b4b` | accepted `f1327be48ba2` | pinned `f1327be48ba2` / core-first-run-rc1-2026-10-12 | observed `f1327be48ba2` / accepted | unverified | fresh / Core |
| aiverse-filmmakers/AI-Verse-Skills | ai-verse-skills | `d4a02888ba8d` | accepted `afde5c06307f` | pinned `afde5c06307f` / core-first-run-rc1-2026-10-12 | observed `afde5c06307f` / accepted | unverified | fresh / Core |
| aiverse-filmmakers/AI-Verse-Data | ai-verse-data | `7e9fadbd7375` | accepted `f8978f8f7a1b` | pinned `f8978f8f7a1b` / core-first-run-rc1-2026-10-12 | observed `f8978f8f7a1b` / accepted | unverified | fresh / Core |

## Open drift

| Severity | Scope | Drift | Repositories | Reason | Required action |
| --- | --- | --- | --- | --- | --- |
| WARNING | Core | distribution-adapter-compatibility-shadow-risk | ai-verse-distribution | Distribution contains hard-coded supported revision and command knowledge in trusted adapters. This is legitimate orchestration today but must not become a second compatibility or owner-acceptance authority. | Bind future admission to Registry, descriptor and owner evidence while retaining Distribution trusted argv routing. |
| INFO | Core | compact-release-receipt-not-yet-implemented | ai-verse-distribution | Durable release reconstruction evidence exists across current release-set and qualification files, but the planned compact single release receipt binding is not implemented yet. | Implement the compact immutable release receipt in Slice 5.4 without replacing existing qualification evidence. |

## Authority and freshness rules

- This ledger is a projection only and is never machine authority.
- Static repository identity, ownership and lifecycle facts come only from the Registry.
- Dynamic HEADs, pins, descriptor observations, acceptance evidence, sync state, freshness, watchdog state and drift come only from Repository State.
- Dates are informational only. Exact Git identity, evidence refs and refresh scope determine freshness and lineage.
- `WATCHDOG-STALE` and `WATCHDOG-FAILED` are not CLEAN. A valid scoped refresh may prove a scoped decision while the full watchdog is stale, subject to the governance contract.
- Any intersecting or global `BLOCKING` drift blocks the relevant future release decision until reconciled.
