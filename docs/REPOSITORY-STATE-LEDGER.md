# AI-Verse Repository State Ledger

> GENERATED FILE. Do not hand-edit. Machine truth is `governance/repository-registry.json` for static facts and `governance/repository-state.json` for dynamic facts.

Regenerate with `python scripts/refresh_repository_state.py --write-ledger`. Verify with `python scripts/refresh_repository_state.py --check-ledger`.

## Snapshot

- State schema: `ai-verse.repository-state/v1`
- Registry binding blob: `cc4df25367762c8a8148f87bf9015b4f5107ce17`
- Refresh mode: `scoped-refresh`
- Refresh scope: `Full`
- Refresh status: `complete`
- Refresh evidence revision: `9f931d229d1bc003a81cfda7a25ed80ff07de100`
- Last full refresh: `0ace417725831e0ba3843fdc77a27d578b3b3010`
- Watchdog: `WATCHDOG-STALE`
- Watchdog reason: Registry expanded in Slice 4.3-T1 after the last successful global heartbeat. The prior scan remains historical evidence but does not cover the newly registered Wave 2/3 repositories, so watchdog status is fail-closed until a new full scan succeeds.

## Repository state

| Repository | Component | Observed HEAD | Owner acceptance | Distribution pin | Descriptor | System sync | Freshness |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aiverse-filmmakers/AI-Verse-System | ai-verse-system | `9f931d229d1b` | not-applicable | not-applicable | not-applicable | not-applicable | fresh / Full |
| aiverse-filmmakers/ai-verse-distribution | ai-verse-distribution | `10d04c723e59` | unverified | not-applicable | not-applicable | unverified | fresh / Full |
| aiverse-filmmakers/AI-Verse-OS | ai-verse-os | `470ad89e6b96` | accepted `64f7325444d1` | pinned `64f7325444d1` / core-first-run-rc1-2026-10-12 | observed `64f7325444d1` / accepted | unverified | fresh / Full |
| aiverse-filmmakers/AI-Verse-Brain | ai-verse-brain | `4406d1506828` | accepted `69f7912eeb35` | pinned `69f7912eeb35` / core-first-run-rc1-2026-10-12 | observed `69f7912eeb35` / accepted | unverified | fresh / Full |
| aiverse-filmmakers/AI-Verse-Memory | ai-verse-memory | `09911eae0b4b` | accepted `f1327be48ba2` | pinned `f1327be48ba2` / core-first-run-rc1-2026-10-12 | observed `f1327be48ba2` / accepted | unverified | fresh / Full |
| aiverse-filmmakers/AI-Verse-Skills | ai-verse-skills | `d4a02888ba8d` | accepted `afde5c06307f` | pinned `afde5c06307f` / core-first-run-rc1-2026-10-12 | observed `afde5c06307f` / accepted | unverified | fresh / Full |
| aiverse-filmmakers/AI-Verse-Data | ai-verse-data | `7e9fadbd7375` | accepted `f8978f8f7a1b` | pinned `f8978f8f7a1b` / core-first-run-rc1-2026-10-12 | observed `f8978f8f7a1b` / accepted | unverified | fresh / Full |
| aiverse-filmmakers/AI-Verse-Gateway | ai-verse-gateway | `95cc8319c1dc` | unverified | unpinned | observed `1772b75e2add` / candidate | unverified | fresh / Full |
| aiverse-filmmakers/AI-Verse-Automations | ai-verse-automations | `fda8b25b11b8` | unverified | unpinned | observed `287ce9d6718e` / candidate | unverified | fresh / Full |
| aiverse-filmmakers/AI-Verse-Multiple-Bots | ai-verse-multiple-bots | `b4ad4315e560` | unverified | unpinned | observed `ddf70ac19736` / candidate | unverified | fresh / Full |
| aiverse-filmmakers/ai-verse-token | ai-verse-token | `363dde3d87ed` | unverified | unpinned | observed `d36916323abb` / candidate | unverified | fresh / Full |
| aiverse-filmmakers/AI-Verse-Connections | ai-verse-connections | `b557ef1d83a9` | unverified | unpinned | observed `602a1c52ab78` / candidate | unverified | fresh / Full |
| aiverse-filmmakers/AI-Verse-Dashboard | ai-verse-dashboard | `ec5d40aea7fa` | unverified | unpinned | observed `bd26986e202d` / candidate | unverified | fresh / Full |
| aiverse-filmmakers/AI-Verse-Apps | ai-verse-apps | - | unverified | not-applicable | not-applicable | unverified | unknown / component |

## Open drift

| Severity | Scope | Drift | Repositories | Reason | Required action |
| --- | --- | --- | --- | --- | --- |
| WARNING | Core | distribution-adapter-compatibility-shadow-risk | ai-verse-distribution | Distribution contains hard-coded supported revision and command knowledge in trusted adapters. This is legitimate orchestration today but must not become a second compatibility or owner-acceptance authority. | Bind future admission to Registry, descriptor and owner evidence while retaining Distribution trusted argv routing. |
| WARNING | global | repository-watchdog-stale | ai-verse-system | Slice 4.3-T1 expanded the canonical Registry after the last successful global heartbeat. The prior heartbeat remains valid historical evidence for the earlier seven-repository Registry but cannot be treated as current coverage for the fourteen-repository Registry. | Run the existing full Registry-derived watchdog against the expanded Registry before interpreting watchdog status as current. Do not infer owner acceptance or release readiness from Registry registration alone. |
| INFO | Core | compact-release-receipt-not-yet-implemented | ai-verse-distribution | Durable release reconstruction evidence exists across current release-set and qualification files, but the planned compact single release receipt binding is not implemented yet. | Implement the compact immutable release receipt in Slice 5.4 without replacing existing qualification evidence. |

## Authority and freshness rules

- This ledger is a projection only and is never machine authority.
- Static repository identity, ownership and lifecycle facts come only from the Registry.
- Dynamic HEADs, pins, descriptor observations, acceptance evidence, sync state, freshness, watchdog state and drift come only from Repository State.
- Dates are informational only. Exact Git identity, evidence refs and refresh scope determine freshness and lineage.
- `WATCHDOG-STALE` and `WATCHDOG-FAILED` are not CLEAN. A valid scoped refresh may prove a scoped decision while the full watchdog is stale, subject to the governance contract.
- Any intersecting or global `BLOCKING` drift blocks the relevant future release decision until reconciled.
