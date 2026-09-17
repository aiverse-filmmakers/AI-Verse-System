# Independent Whole-System Audit Finding Register

**Program:** Independent Whole-System Public-Beta Audit  
**Register established by:** A0.3 Evidence/finding ledger  
**Established:** 2026-09-15  
**Live repair-state format established:** 2026-09-17 during canonical closure of `WSA-2026-009`  
**Status:** CANONICAL LIVE FINDING INDEX / POST-AUDIT REPAIR STATE

## 1. Authority and preserved history

This file remains the canonical live index for stable audit finding IDs and their current post-audit repair state.

The complete detailed audit register as it stood after Wave R0 — including every original detailed finding record, the full contradiction register, every evidence-ID index, allocation ledger, negative-space checks, evidence limitations, downstream rules, and the post-audit closure records already written for WSA-2026-006, WSA-2026-012, WSA-2026-016 and WSA-2026-029 — is preserved **byte-for-byte** at:

`FINDING-REGISTER-THROUGH-R0-2026-09-17.md`

Preserved source blob:

`0bf2aff584a0e9b1f18c1325cc0279e44dd6628f`

The preserved companion is historical evidence and must not be rewritten. This live index records later repair-state transitions while pointing back to the immutable detailed history and per-repair closure packets.

Rules:

1. Finding IDs remain stable and are never renumbered or reused.
2. Original audit evidence, contradiction text, severity, confidence, scope and required closure evidence remain authoritative in the preserved detailed register unless later closure evidence explicitly changes state.
3. State transitions require a completed owner repair, exact regression evidence, required rechecks, and a closure packet under `../repairs/`.
4. Closing one finding does not implicitly close adjacent findings or whole journey/adversarial tasks.
5. New findings, if genuinely discovered during repair, continue from the next unused global ID.
6. Dashboard MC1.4 and owner dogfood remain paused until R0-R6 and the bounded final independent recheck explicitly release them.

**Next unused finding ID:** `WSA-2026-064`.

## 2. Current finding summary

| Finding | Severity | Confidence | State | Root area | Affected repos | Opened by |
|---|---|---|---|---|---|---|
| `WSA-2026-001` | LOW | PROVEN | OPEN | release metadata / documentation drift | `ai-verse-distribution`, `AI-Verse-System` | A0.2 |
| `WSA-2026-002` | LOW | PROVEN | OPEN | System documentation drift | `AI-Verse-System`, `AI-Verse-Connections` | A0.2 |
| `WSA-2026-003` | INFO | PROVEN | OPEN | hosted CI / evidence availability | `AI-Verse-Connections`, `AI-Verse-System` | A0.2 |
| `WSA-2026-004` | LOW | PROVEN | OPEN | audit control-document drift | `AI-Verse-System` | A0.3 |
| `WSA-2026-005` | LOW | PROVEN | OPEN | capability source-of-truth / contract metadata drift | `AI-Verse-OS` | A1.1 |
| `WSA-2026-006` | BLOCKER | PROVEN | CLOSED | destructive lifecycle / filesystem safety | `AI-Verse-Gateway` | A1.2 |
| `WSA-2026-007` | HIGH | PROVEN | OPEN | setup/disable/uninstall/status lifecycle truth | `AI-Verse-Gateway` | A1.2 |
| `WSA-2026-008` | HIGH | PROVEN | OPEN | concurrency / idempotency / session binding / run control | `AI-Verse-Gateway` | A1.2 |
| `WSA-2026-009` | HIGH | PROVEN | CLOSED | filesystem containment / scope isolation | `AI-Verse-Brain` | A1.3 |
| `WSA-2026-010` | MEDIUM | PROVEN | OPEN | Goal concurrency / replay safety | `AI-Verse-Brain` | A1.3 |
| `WSA-2026-011` | LOW | PROVEN | OPEN | release/version identity | `AI-Verse-Brain` | A1.3 |
| `WSA-2026-012` | BLOCKER | PROVEN | CLOSED | destructive lifecycle / filesystem containment | `AI-Verse-Memory` | A1.4 |
| `WSA-2026-013` | HIGH | PROVEN | OPEN | lifecycle authority / canonical writes | `AI-Verse-Memory` | A1.4 |
| `WSA-2026-014` | HIGH | PROVEN | OPEN | migration / canonical authority transfer | `AI-Verse-Memory` | A1.4 |
| `WSA-2026-015` | LOW | PROVEN | OPEN | release/version/bootstrap reproducibility | `AI-Verse-Memory` | A1.4 |
| `WSA-2026-016` | BLOCKER | PROVEN | CLOSED | lifecycle controller containment | `AI-Verse-Skills` | A1.5 |
| `WSA-2026-017` | HIGH | PROVEN | OPEN | lifecycle concurrency / serialization | `AI-Verse-Skills` | A1.5 |
| `WSA-2026-018` | MEDIUM | PROVEN | OPEN | immutable generation retention | `AI-Verse-Skills` | A1.5 |
| `WSA-2026-019` | LOW | PROVEN | OPEN | release/version/bootstrap reproducibility | `AI-Verse-Skills` | A1.5 |
| `WSA-2026-020` | HIGH | PROVEN | OPEN | trusted scope provenance / workspace isolation | `AI-Verse-Data` | A1.6 |
| `WSA-2026-021` | LOW | PROVEN | OPEN | release/version/install reproducibility | `AI-Verse-Data` | A1.6 |
| `WSA-2026-022` | HIGH | PROVEN | OPEN | operator/domain authority binding | `AI-Verse-Multiple-Bots` | A1.7 |
| `WSA-2026-023` | HIGH | PROVEN | OPEN | Worker workspace isolation / canonical coordination authority | `AI-Verse-Multiple-Bots` | A1.7 |
| `WSA-2026-024` | HIGH | PROVEN | OPEN | canonical cost truth / trusted ACTUAL source enforcement | `ai-verse-token` | A1.8 |
| `WSA-2026-025` | MEDIUM | PROVEN | OPEN | pricing evidence transactionality / concurrency | `ai-verse-token` | A1.8 |
| `WSA-2026-026` | HIGH | PROVEN | OPEN | canonical store ownership / lifecycle safety / health truth | `AI-Verse-Automations` | A1.9 |
| `WSA-2026-027` | HIGH | PROVEN | OPEN | canonical schedule authority / migration handoff / readiness truth | `AI-Verse-Automations` | A1.9 |
| `WSA-2026-028` | MEDIUM | PROVEN | OPEN | native attachment lifecycle / host discovery truth | `AI-Verse-Automations` | A1.9 |
| `WSA-2026-029` | BLOCKER | PROVEN | CLOSED | destructive lifecycle / filesystem containment | `AI-Verse-Connections` | A1.10 |
| `WSA-2026-030` | HIGH | PROVEN | OPEN | system scope isolation / canonical installation binding | `AI-Verse-Connections` | A1.10 |
| `WSA-2026-031` | HIGH | PROVEN | OPEN | credential origin binding / token passthrough prevention | `AI-Verse-Connections` | A1.10 |
| `WSA-2026-032` | HIGH | PROVEN | OPEN | final-edge authority / concurrency / safety budgets | `AI-Verse-Connections` | A1.10 |
| `WSA-2026-033` | HIGH | PROVEN | OPEN | external path authorization / provider-edge containment | `AI-Verse-Connections` | A1.10 |
| `WSA-2026-034` | HIGH | PROVEN | OPEN | lifecycle concurrency / release receipt authority | `ai-verse-distribution` | A1.12 |
| `WSA-2026-035` | MEDIUM | PROVEN | OPEN | first-run requirements / executable compatibility truth | `ai-verse-distribution` | A1.12 |
| `WSA-2026-036` | MEDIUM | PROVEN | OPEN | diagnostics / secret redaction / failure handling | `ai-verse-distribution` | A1.12 |
| `WSA-2026-037` | LOW | PROVEN | OPEN | repository-local release/status documentation drift | `ai-verse-distribution` | A1.12 |
| `WSA-2026-038` | HIGH | PROVEN | OPEN | workspace isolation / realtime subscription lifecycle | `AI-Verse-Dashboard` | A1.13 |
| `WSA-2026-039` | HIGH | PROVEN | OPEN | system identity / registered-root authority binding | `AI-Verse-Dashboard` | A1.13 |
| `WSA-2026-040` | HIGH | PROVEN | OPEN | local gateway authentication / privacy boundary | `AI-Verse-Dashboard` | A1.13 |
| `WSA-2026-041` | MEDIUM | PROVEN | OPEN | local browser integration / Origin policy | `AI-Verse-Dashboard` | A1.13 |
| `WSA-2026-042` | MEDIUM | PROVEN | OPEN | canonical ownership / projection truth | `AI-Verse-Dashboard` | A1.13 |
| `WSA-2026-043` | MEDIUM | PROVEN | OPEN | release contract consistency / machine-readable acceptance | `AI-Verse-System` | A1.14 |
| `WSA-2026-044` | MEDIUM | PROVEN | OPEN | meta authority / living-spec synchronization / current release truth | `AI-Verse-System` | A1.14 |
| `WSA-2026-045` | MEDIUM | PROVEN | OPEN | retrieval freshness / provenance cache invalidation | `AI-Verse-Gateway` | A2.5 |
| `WSA-2026-046` | MEDIUM | PROVEN | OPEN | release composition / public-member product path | `AI-Verse-Skills`, `ai-verse-distribution`, `AI-Verse-System` | A2.8 |
| `WSA-2026-047` | MEDIUM | PROVEN | OPEN | migration release evidence / cross-owner persistence | `AI-Verse-OS`, `AI-Verse-Gateway`, `AI-Verse-Memory`, `AI-Verse-Data`, `ai-verse-distribution` | A3.2 |
| `WSA-2026-048` | MEDIUM | PROVEN | OPEN | learning release evidence / cross-owner user journey | `AI-Verse-Gateway`, `AI-Verse-OS`, `AI-Verse-Brain`, `AI-Verse-Skills`, `ai-verse-distribution` | A3.5 |
| `WSA-2026-049` | MEDIUM | PROVEN | OPEN | system isolation release evidence / multi-root journey | `ai-verse-distribution`, `AI-Verse-OS`, `AI-Verse-Gateway`, `AI-Verse-Memory`, `AI-Verse-Data`, `AI-Verse-Multiple-Bots`, `AI-Verse-Automations`, `ai-verse-token` | A3.10 |
| `WSA-2026-050` | MEDIUM | PROVEN | OPEN | authentication availability / pre-auth resource exhaustion | `AI-Verse-Gateway` | A4.1 |
| `WSA-2026-051` | HIGH | PROVEN | OPEN | SSRF / DNS rebinding / credential-bearing provider edge | `AI-Verse-Connections` | A4.1 |
| `WSA-2026-052` | HIGH | PROVEN | OPEN | migration concurrency / source-level idempotency | `AI-Verse-OS` | A4.2 |
| `WSA-2026-053` | HIGH | PROVEN | OPEN | structured Data concurrency / natural-key uniqueness | `AI-Verse-OS`, `AI-Verse-Brain`, `AI-Verse-Data` | A4.2 |
| `WSA-2026-054` | HIGH | PROVEN | OPEN | crash recovery / state-lock ownership / external-effect receipt safety | `AI-Verse-Connections` | A4.3 |
| `WSA-2026-055` | MEDIUM | PROVEN | OPEN | external-effect idempotency / crash uncertainty / recovery | `AI-Verse-Connections` | A4.3 |
| `WSA-2026-056` | MEDIUM | PROVEN | OPEN | canonical receipt corruption / health truth / recovery | `AI-Verse-Connections` | A4.3 |
| `WSA-2026-057` | MEDIUM | PROVEN | OPEN | provider-error diagnostics / receipt minimization / secret-at-rest boundary | `AI-Verse-Connections` | A4.4 |
| `WSA-2026-058` | MEDIUM | PROVEN | OPEN | long-lived runtime state scale / idempotency indexing | `AI-Verse-Gateway` | A4.5 |
| `WSA-2026-059` | MEDIUM | PROVEN | OPEN | external-effect history scale / receipt indexing / budget lookup | `AI-Verse-Connections` | A4.5 |
| `WSA-2026-060` | LOW | PROVEN | OPEN | machine-readable release compatibility / blocker truth | `ai-verse-distribution` | A5.2 |
| `WSA-2026-061` | LOW | PROVEN | OPEN | release-acceptance documentation / version and CI status truth | `ai-verse-token` | A5.3 |
| `WSA-2026-062` | LOW | PROVEN | OPEN | profile composition documentation / release scope truth | `AI-Verse-Multiple-Bots` | A5.3 |
| `WSA-2026-063` | MEDIUM | PROVEN | OPEN | product runtime release evidence / supported runtime boundary | `AI-Verse-Gateway`, `ai-verse-distribution` | A5.4 |

Current counts:

| Dimension | Count |
|---|---:|
| BLOCKER | 4 historical / **0 OPEN** |
| HIGH | 24 historical |
| MEDIUM | 22 historical |
| LOW | 12 historical |
| INFO | 1 historical |
| PROVEN | 63 |
| OPEN | **58** |
| CLOSED | **5** |

These counts do **not** imply public-beta approval. The whole-system verdict remains **NO-GO** until the ordered repair program and final bounded independent recheck complete.

## 3. Post-audit closures

| Finding | Owner | Repair PR | Merged owner ref | Closure packet |
|---|---|---|---|---|
| `WSA-2026-006` | `AI-Verse-Gateway` | `#32` | `5347a0b7e3f3f302f4570e9bc37d515192753610` | `../repairs/WSA-2026-006-GATEWAY-DESTRUCTIVE-PURGE.md` |
| `WSA-2026-012` | `AI-Verse-Memory` | `#30` | `7a1ed5777fd11616375501d730fcbd488beff8b8` | `../repairs/WSA-2026-012-MEMORY-LIFECYCLE-CONTAINMENT.md` |
| `WSA-2026-016` | `AI-Verse-Skills` | `#15` | `3541d2a7af1b20ca12736ed7454d119295d8e193` | `../repairs/WSA-2026-016-SKILLS-CONTROLLER-CONTAINMENT.md` |
| `WSA-2026-029` | `AI-Verse-Connections` | `#2` | `a04f655c6f0c9b57d17e64b5c1ff8eb88aab4016` | `../repairs/WSA-2026-029-CONNECTIONS-DESTRUCTIVE-PURGE.md` |
| `WSA-2026-009` | `AI-Verse-Brain` | `#24` | `908f9a9a06c2b12204ada7f71cd761bae97b52ce` | `../repairs/WSA-2026-009-BRAIN-NATIVE-HOST-ROOT-CONTAINMENT.md` |

## 4. WSA-2026-009 closure overlay

**State transition:** `OPEN -> CLOSED`  
**Severity/confidence:** HIGH / PROVEN, unchanged  
**Original audited and live pre-repair Brain ref:** `6f986e8d06c7f9c069fbf05aa92ae7b7a1af9bf4`  
**Repair PR:** `AI-Verse-Brain#24`  
**Final tested PR head:** `f35a3f683f9014bbe3b508af341c09992ae2c1c3`  
**Merged Brain ref:** `908f9a9a06c2b12204ada7f71cd761bae97b52ce`  
**Reviewed/merged product tree:** `66b650a63879898b936b7c8c550d10654caed366`

Closure evidence:

- one shared physical native-path containment guard now covers host detection, operator/workspace state, runtime, nested runtime locks, initialization, installation markers and standalone-to-native adoption;
- POSIX symlinks and Windows junction/reparse redirection fail closed;
- paths are revalidated immediately before mutation, not merely during planning;
- external-sentinel regressions cover ten hostile layouts;
- PR-head CI run `35228628402` succeeded, including package smoke and all six Ubuntu/macOS/Windows Python 3.9/3.12 test legs;
- Windows Python 3.12 job `105226554049` completed 237 tests successfully and exercised the real junction attack class;
- macOS Python 3.12 job `105226553976` passed 237/237 including all ten containment attacks;
- PR-head Skills Receipt Contract `35228628604` and OS Direction Ownership Contract `35228628938` succeeded;
- tested PR tree equals merged product tree exactly;
- post-merge CI run `35228849333` succeeded 7/7;
- post-merge Skills Receipt Contract `35228849545` and OS Direction Ownership Contract `35228849499` succeeded;
- zero Brain PRs remained open after merge;
- A1.3 finding-specific recheck: PASS for WSA-2026-009 only;
- A3.2 Brain destination-containment branch: RESOLVED while the journey remains PARTIAL overall;
- A4.1 Brain owner-root branch: RESOLVED while the adversarial task remains FAIL overall.

This closure does **not** alter WSA-2026-010 or WSA-2026-011, and it does not close any remaining A3.2/A4.1 findings.

## 5. Current repair position

- R0: **4 / 4 CLOSED = 100%**.
- R1: **1 / 13 CLOSED = 7.69%**.
- Total findings: **5 / 63 CLOSED**, **58 / 63 OPEN**.
- Open BLOCKERs: **0**.
- Current ACTIVE repair in the execution tracker: `R1.2 / WSA-2026-020`.
- WSA-2026-020 implementation has not begun as part of this closure.
- Whole-system verdict: **NO-GO**.

## 6. Navigation and downstream rule

For original detailed evidence, contradiction IDs, evidence IDs, impact, expected/observed law and required closure evidence for any finding, read:

`FINDING-REGISTER-THROUGH-R0-2026-09-17.md`

For current repair state, use this file plus the exact closure packet listed above and `../repairs/REPAIR-EXECUTION-TRACKER-2026-09-17.md`.

Future repair closures must:

1. preserve stable IDs and historical evidence;
2. update the live summary state/counts here only after closure evidence is complete;
3. add the closure packet and exact merged owner ref to Section 3;
4. add a concise closure overlay when needed;
5. mark exactly one next repair ACTIVE in the execution tracker;
6. never infer that an adjacent finding or whole-system verdict is closed merely from one owner repair.
