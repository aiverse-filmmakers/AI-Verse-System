# WSA-2026-057 — Connections MCP provider error redaction

**Finding:** WSA-2026-057 (A4.4; MEDIUM / PROVEN)  
**Transition:** OPEN -> CLOSED  
**Owner repository:** AI-Verse-Connections  
**Audited owner baseline:** `2e608a3061ea1cd5db9ccd27d1b0779396707d4f`  
**Repair PR:** [AI-Verse-Connections #11](https://github.com/aiverse-filmmakers/AI-Verse-Connections/pull/11)  
**Final tested owner PR head:** `ac54373104a180fe27ce74a6e4371a0e0b7cb147`  
**Merged owner ref:** `fb8b10deb6e05656e1e3b97e8d93650d58c57a7b`  
**Exact tested and merged owner tree:** `4bd49c355cda5828b9eb77091dce0250340e077e`

## Finding and closure law

At the audited A4.4 source, Connections promoted arbitrary MCP JSON-RPC error messages into local exception text and attached the entire provider error object as `details.rpc`. The execution failure receipt and CLI could then persist or print bearer credentials and private provider context echoed by the remote service.

The adapter now discards provider-controlled message/data fields and raises a local `MCP_RPC_ERROR` with a fixed bounded summary and only a validated safe integer JSON-RPC code. The CLI formatter emits that same safe shape. The durable external-effect receipt retains the local error code and unknown-effect outcome needed for replay/reconciliation, without raw provider text or data.

## Permanent regression coverage

The MCP integration mock echoes the actual bearer credential and private lookup context in the JSON-RPC error message and `data`. The regression proves:

- the surfaced ConnectionsError has a fixed message and only the numeric provider code;
- CLI diagnostic JSON excludes bearer and private values;
- raw receipt bytes exclude both echoed values and provider message fields;
- the durable failure receipt preserves `MCP_RPC_ERROR` and the `external-unknown` effect state.

Security documentation defines the provider error boundary and receipt/diagnostic minimization.

## Owner validation

| Gate | Exact PR head | Merged main |
|---|---|---|
| CI, Node 20/22 × Ubuntu/macOS/Windows | `37170064211`, 6/6 pass; suite 51/51 | `37170167486`, 6/6 pass |
| WSA-054 Write Lock Recovery | `37170064219`, 3 OS jobs pass | `37170167519`, 3 OS jobs pass |
| WSA-055 External Effect Recovery | `37170064209`, 3 OS jobs pass | `37170167543`, 3 OS jobs pass |

The exact PR tree and merged main tree are identical. Connections main is `fb8b10deb6e05656e1e3b97e8d93650d58c57a7b`; open Connections PRs after merge: 0. WSA-054 and WSA-055 recovery guarantees and WSA-056 receipt-integrity protections remain intact.

## System closure validation

| Gate | System ref | Contract Validation run | Python 3.11 | Python 3.13 |
|---|---|---:|---|---|
| Exact closure PR head | `65c3c181cc2c30f336904b8471fe9b426162e620` | `37170356078` | PASS | PASS |
| Merged System main | `da040a6d2bac2fca0be099ba1a5c61f8d7054af6` | `37170460920` | PASS | PASS |

The exact-head and merged-main Contract Validation jobs passed on Python 3.11 and 3.13. The canonical register and tracker record WSA-2026-057 as CLOSED and WSA-2026-058 as ACTIVE. The whole-system NO-GO verdict, Dashboard MC1.4 pause and owner-dogfood pause remain in force.

## Outcome

WSA-2026-057 is closed for AI-Verse-Connections. WSA-2026-058 / R4.9 becomes ACTIVE. No whole-system release gate is released.
