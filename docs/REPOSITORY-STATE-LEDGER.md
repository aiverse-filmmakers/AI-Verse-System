# AI-Verse Repository State Ledger

> GENERATED FILE. Do not hand-edit. Machine truth is `governance/repository-registry.json` for static facts and `governance/repository-state.json` for dynamic facts.

Regenerate with `python scripts/refresh_repository_state.py --write-ledger`. Verify with `python scripts/refresh_repository_state.py --check-ledger`.

## Snapshot

- State schema: `ai-verse.repository-state/v1`
- Registry binding blob: `88839264a3270d65d21297ade089f111aa843975`
- Refresh mode: `scoped-refresh`
- Refresh scope: `Core`
- Refresh status: `complete`
- Refresh evidence revision: `8debcde9fa197f8591cab44440e928903d140cf4`
- Last full refresh: `2d25213b0dc46e7274c7790dd5881694f94c08ae`
- Watchdog: `WATCHDOG-CURRENT`
- Watchdog reason: Successful Registry-derived global heartbeat at 2026-10-23T08:33:22Z; all registered repositories were scanned with no access/fetch failure.

## Repository state

| Repository | Component | Observed HEAD | Owner acceptance | Distribution pin | Descriptor | System sync | Freshness |
| --- | --- | --- | --- | --- | --- | --- | --- |
| aiverse-filmmakers/AI-Verse-System | ai-verse-system | `8debcde9fa19` | not-applicable | not-applicable | not-applicable | not-applicable | fresh / Core |
| aiverse-filmmakers/ai-verse-distribution | ai-verse-distribution | `a3db40f5418e` | accepted `1e05ea2c491a` | not-applicable | observed `1e05ea2c491a` / accepted | synchronized `16c0243bf3d2` | fresh / Core |
| aiverse-filmmakers/AI-Verse-OS | ai-verse-os | `d490db4c02e7` | accepted `7bb622678339` | pinned `7bb622678339` / core-tool-placement-candidate-2026-10-23 | observed `7bb622678339` / accepted | synchronized `b43b640a7795` | fresh / Core |
| aiverse-filmmakers/AI-Verse-Brain | ai-verse-brain | `6ad408e38b6b` | accepted `7e6f7a7e8a3d` | pinned `7e6f7a7e8a3d` / core-tool-placement-candidate-2026-10-23 | observed `7e6f7a7e8a3d` / accepted | synchronized `967013147705` | fresh / Core |
| aiverse-filmmakers/AI-Verse-Memory | ai-verse-memory | `09911eae0b4b` | accepted `f1327be48ba2` | pinned `f1327be48ba2` / core-tool-placement-candidate-2026-10-23 | observed `f1327be48ba2` / accepted | synchronized `3c5715230f10` | fresh / Core |
| aiverse-filmmakers/AI-Verse-Skills | ai-verse-skills | `297c63a5be95` | accepted `390c6e1633af` | pinned `390c6e1633af` / core-tool-placement-candidate-2026-10-23 | observed `390c6e1633af` / accepted | synchronized `6be63e25b7eb` | fresh / Core |
| aiverse-filmmakers/AI-Verse-Data | ai-verse-data | `7e9fadbd7375` | accepted `f8978f8f7a1b` | pinned `f8978f8f7a1b` / core-tool-placement-candidate-2026-10-23 | observed `f8978f8f7a1b` / accepted | synchronized `b4d6ec721c5d` | fresh / Core |
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
