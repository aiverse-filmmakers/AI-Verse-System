# AI-Verse Repository State Ledger

> GENERATED FILE. Do not hand-edit. Machine truth is `governance/repository-registry.json` for static facts and `governance/repository-state.json` for dynamic facts.

Regenerate with `python scripts/refresh_repository_state.py --write-ledger`. Verify with `python scripts/refresh_repository_state.py --check-ledger`.

## Snapshot

- State schema: `ai-verse.repository-state/v1`
- Registry binding blob: `88839264a3270d65d21297ade089f111aa843975`
- Refresh mode: `scoped-refresh`
- Refresh scope: `Core`
- Refresh status: `complete`
- Refresh evidence revision: `90d3f430da490fb27d6a63dd94cd8eac8bb5019d`
- Last full refresh: `ea797aa2c37973a6b1d80695ccae45812011c0e7`
- Watchdog: `WATCHDOG-CURRENT`
- Watchdog reason: Successful Registry-derived global heartbeat at 2026-11-14T10:24:45Z; all registered repositories were scanned with no access/fetch failure.

## Repository state

| Repository | Component | Observed HEAD | Owner acceptance | Distribution pin | Descriptor | System sync | Freshness |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aiverse-filmmakers/AI-Verse-System | ai-verse-system | `90d3f430da49` | not-applicable | not-applicable | not-applicable | not-applicable | fresh / Core |
| aiverse-filmmakers/ai-verse-distribution | ai-verse-distribution | `46722f989ac1` | accepted `fc3182c8f7de` | not-applicable | observed `fc3182c8f7de` / accepted | synchronized `90d3f430da49` | fresh / Core |
| aiverse-filmmakers/AI-Verse-OS | ai-verse-os | `8084d51ba32b` | accepted `2060fe7764cf` | pinned `c949bca4e5b6` / core-os-0.3.15-candidate-2026-11-11-v2 | observed `2060fe7764cf` / accepted | synchronized `90d3f430da49` | fresh / Core |
| aiverse-filmmakers/AI-Verse-Brain | ai-verse-brain | `32cae304861b` | accepted `14ded0120c11` | pinned `14ded0120c11` / core-os-0.3.15-candidate-2026-11-11-v2 | observed `14ded0120c11` / accepted | synchronized `967013147705` | fresh / Core |
| aiverse-filmmakers/AI-Verse-Memory | ai-verse-memory | `1e7bd0298d38` | accepted `5a853e316288` | pinned `5a853e316288` / core-os-0.3.15-candidate-2026-11-11-v2 | observed `5a853e316288` / accepted | synchronized `1ff43cd377e7` | fresh / Core |
| aiverse-filmmakers/AI-Verse-Skills | ai-verse-skills | `bcbc162bee84` | accepted `4664880a852e` | pinned `390c6e1633af` / core-os-0.3.15-candidate-2026-11-11-v2 | observed `4664880a852e` / accepted | synchronized `90d3f430da49` | fresh / Core |
| aiverse-filmmakers/AI-Verse-Data | ai-verse-data | `67b8b0614291` | accepted `f8978f8f7a1b` | pinned `f8978f8f7a1b` / core-os-0.3.15-candidate-2026-11-11-v2 | observed `f8978f8f7a1b` / accepted | synchronized `b4d6ec721c5d` | fresh / Core |
| aiverse-filmmakers/AI-Verse-Gateway | ai-verse-gateway | `ceb8849ec062` | unverified | unpinned | observed `386ff40135a8` / candidate | unverified | fresh / global |
| aiverse-filmmakers/AI-Verse-Automations | ai-verse-automations | `fda8b25b11b8` | unverified | unpinned | observed `287ce9d6718e` / candidate | unverified | fresh / global |
| aiverse-filmmakers/AI-Verse-Multiple-Bots | ai-verse-multiple-bots | `b4ad4315e560` | unverified | unpinned | observed `ddf70ac19736` / candidate | unverified | fresh / global |
| aiverse-filmmakers/ai-verse-token | ai-verse-token | `363dde3d87ed` | unverified | unpinned | observed `d36916323abb` / candidate | unverified | fresh / global |
| aiverse-filmmakers/AI-Verse-Connections | ai-verse-connections | `b6eedea9a1ab` | unverified | unpinned | observed `602a1c52ab78` / candidate | unverified | fresh / global |
| aiverse-filmmakers/AI-Verse-Dashboard | ai-verse-dashboard | `91aad66592ab` | unverified | unpinned | observed `bd26986e202d` / candidate | unverified | fresh / global |
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
