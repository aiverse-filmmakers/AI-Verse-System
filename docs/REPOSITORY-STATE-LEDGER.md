# AI-Verse Repository State Ledger

> GENERATED FILE. Do not hand-edit. Machine truth is `governance/repository-registry.json` for static facts and `governance/repository-state.json` for dynamic facts.

Regenerate with `python scripts/refresh_repository_state.py --write-ledger`. Verify with `python scripts/refresh_repository_state.py --check-ledger`.

## Snapshot

- State schema: `ai-verse.repository-state/v1`
- Registry binding blob: `cc4df25367762c8a8148f87bf9015b4f5107ce17`
- Refresh mode: `full-refresh`
- Refresh scope: `global`
- Refresh status: `complete`
- Refresh evidence revision: `d2a4317f2acb4a4c21d3dfd133dd4f63213a1f4f`
- Last full refresh: `d2a4317f2acb4a4c21d3dfd133dd4f63213a1f4f`
- Watchdog: `WATCHDOG-CURRENT`
- Watchdog reason: Successful Registry-derived global heartbeat at 2026-10-19T03:15:53Z; all registered repositories were scanned with no access/fetch failure.

## Repository state

| Repository | Component | Observed HEAD | Owner acceptance | Distribution pin | Descriptor | System sync | Freshness |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aiverse-filmmakers/AI-Verse-System | ai-verse-system | `d2a4317f2acb` | not-applicable | not-applicable | not-applicable | not-applicable | fresh / global |
| aiverse-filmmakers/ai-verse-distribution | ai-verse-distribution | `eab886735b42` | unverified | not-applicable | not-applicable | unverified | fresh / global |
| aiverse-filmmakers/AI-Verse-OS | ai-verse-os | `26045ee1e665` | accepted `b6d8c7c7eea0` | pinned `64f7325444d1` / core-first-run-rc1-2026-10-12 | observed `b6d8c7c7eea0` / accepted | unverified | fresh / global |
| aiverse-filmmakers/AI-Verse-Brain | ai-verse-brain | `39336cd19eb4` | accepted `f746806e4361` | pinned `69f7912eeb35` / core-first-run-rc1-2026-10-12 | observed `f746806e4361` / accepted | unverified | fresh / global |
| aiverse-filmmakers/AI-Verse-Memory | ai-verse-memory | `09911eae0b4b` | accepted `f1327be48ba2` | pinned `f1327be48ba2` / core-first-run-rc1-2026-10-12 | observed `f1327be48ba2` / accepted | unverified | fresh / global |
| aiverse-filmmakers/AI-Verse-Skills | ai-verse-skills | `23779f105159` | accepted `afde5c06307f` | pinned `afde5c06307f` / core-first-run-rc1-2026-10-12 | observed `afde5c06307f` / accepted | unverified | fresh / global |
| aiverse-filmmakers/AI-Verse-Data | ai-verse-data | `7e9fadbd7375` | accepted `f8978f8f7a1b` | pinned `f8978f8f7a1b` / core-first-run-rc1-2026-10-12 | observed `f8978f8f7a1b` / accepted | unverified | fresh / global |
| aiverse-filmmakers/AI-Verse-Gateway | ai-verse-gateway | `95cc8319c1dc` | unverified | unpinned | observed `1772b75e2add` / candidate | unverified | fresh / global |
| aiverse-filmmakers/AI-Verse-Automations | ai-verse-automations | `fda8b25b11b8` | unverified | unpinned | observed `287ce9d6718e` / candidate | unverified | fresh / global |
| aiverse-filmmakers/AI-Verse-Multiple-Bots | ai-verse-multiple-bots | `b4ad4315e560` | unverified | unpinned | observed `ddf70ac19736` / candidate | unverified | fresh / global |
| aiverse-filmmakers/ai-verse-token | ai-verse-token | `363dde3d87ed` | unverified | unpinned | observed `d36916323abb` / candidate | unverified | fresh / global |
| aiverse-filmmakers/AI-Verse-Connections | ai-verse-connections | `b557ef1d83a9` | unverified | unpinned | observed `602a1c52ab78` / candidate | unverified | fresh / global |
| aiverse-filmmakers/AI-Verse-Dashboard | ai-verse-dashboard | `ec5d40aea7fa` | unverified | unpinned | observed `bd26986e202d` / candidate | unverified | fresh / global |
| aiverse-filmmakers/AI-Verse-Apps | ai-verse-apps | `db5b0115bf59` | unverified | not-applicable | not-applicable | unverified | fresh / global |

## Open drift

| Severity | Scope | Drift | Repositories | Reason | Required action |
| --- | --- | --- | --- | --- | --- |
| INFO | global | none | - | No open drift recorded. | Continue normal evidence refresh. |

## Authority and freshness rules

- This ledger is a projection only and is never machine authority.
- Static repository identity, ownership and lifecycle facts come only from the Registry.
- Dynamic HEADs, pins, descriptor observations, acceptance evidence, sync state, freshness, watchdog state and drift come only from Repository State.
- Dates are informational only. Exact Git identity, evidence refs and refresh scope determine freshness and lineage.
- `WATCHDOG-STALE` and `WATCHDOG-FAILED` are not CLEAN. A valid scoped refresh may prove a scoped decision while the full watchdog is stale, subject to the governance contract.
- Any intersecting or global `BLOCKING` drift blocks the relevant future release decision until reconciled.
