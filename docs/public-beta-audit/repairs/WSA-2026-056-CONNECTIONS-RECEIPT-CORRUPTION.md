# WSA-2026-056 — Connections receipt corruption and doctor health

**Finding:** WSA-2026-056 (A4.3; MEDIUM / PROVEN)  
**Transition:** OPEN -> CLOSED  
**Owner repository:** AI-Verse-Connections  
**Audited owner baseline:** `6f1da00b955ce7b31e20a625a48d866d6c3a7e54`  
**Repair PR:** [AI-Verse-Connections #10](https://github.com/aiverse-filmmakers/AI-Verse-Connections/pull/10)  
**Final tested owner PR head:** `b007be2d42908c3cefdf75db52e1359f7915870f`  
**Merged owner ref:** `2e608a3061ea1cd5db9ccd27d1b0779396707d4f`  
**Exact tested and merged owner tree:** `06478712ae67744b32491ca06882846715dc6add`

## Finding and closure law

A malformed or truncated receipt NDJSON row previously made the entire receipt history unreadable, while doctor did not report the problem. Since receipt history informs external-effect recovery, silently skipping rows, trusting a valid prefix, or rebuilding empty would lose evidence and could permit unsafe replay.

The repair inspects receipt history without modifying it and returns structured integrity diagnostics: trusted-prefix count, first malformed line and byte offset, file size and SHA-256 fingerprint, plus whether corruption is a truncated tail. Receipt consumers fail closed on any corruption. Doctor reports the integrity failure and marks external-effect recovery unavailable.

Recovery instructions require stopping the service, creating a byte-exact quarantine copy, restoring a validated complete backup or reconstructing the complete ledger from the trustworthy prefix plus provider/system evidence, recording unknown possible effects and reconciling them, validating the candidate, then atomically replacing the log. Empty rebuild, truncating to a valid prefix and skipping malformed rows are prohibited.

## Permanent regression coverage

- Interior malformed JSON preserves original bytes and exposes only a diagnostic trusted prefix; consumers reject the history.
- Doctor surfaces the corruption and blocks external-effect recovery.
- A truncated final line is identified as a tail and receipt consumers reject it.
- Recovery semantics and evidence-preserving restrictions are documented in `docs/SECURITY.md`.

## Owner validation

| Gate | Exact PR head | Merged main |
|---|---|---|
| CI (Node 20/22 × Ubuntu/macOS/Windows) | Run `37169364292`, 6/6 pass | Run `37169420860`, retry attempt 2 passed all six jobs |
| WSA-055 External Effect Recovery | Run `37169364254`, 3 OS jobs pass | Run `37169420861`, 3 OS jobs pass |
| WSA-054 Write Lock Recovery | Run `37169364258`, 3 OS jobs pass | Run `37169420885`, 3 OS jobs pass |

The first merged-main CI attempt had one Windows Node 20 failure in the existing WSA-032 daily-budget race test (50/51 tests passed). The failed job was rerun on the same immutable merged SHA and passed. The focused WSA-056 regressions passed in the failing attempt as well. This intermittent existing race is disclosed here; no WSA-056 failure remains.

Connections main is `2e608a3061ea1cd5db9ccd27d1b0779396707d4f`, with tree `06478712ae67744b32491ca06882846715dc6add`; open Connections PRs: 0.

## System closure validation

| Gate | System ref | Contract Validation run | Python 3.11 | Python 3.13 |
|---|---|---:|---|---|
| Exact closure PR head | `b950c753a2a31699ce7ca8b75969e059c4d0d5fe` | `37169719130` | PASS | PASS |
| Merged System main | `09546014d18eafe586ebed65dc6cd3637a86a012` | `37169783495` | PASS | PASS |

System PR #154 merged after exact-head validation. The tested closure tree and merged System tree were based on the recorded PR head; both Python contract jobs passed on the PR and merged main. The canonical Finding Register and Repair Execution Tracker record WSA-2026-056 as CLOSED and WSA-2026-057 as ACTIVE. Whole-system NO-GO, dashboard pause and owner-dogfood pause remain in force.

## Outcome

WSA-2026-056 is closed for AI-Verse-Connections. WSA-2026-057 / R4.8 becomes ACTIVE. This finding-specific closure does not release any whole-system gate.
