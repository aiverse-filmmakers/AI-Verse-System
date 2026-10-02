# Independent Whole-System Audit Finding Register

**Program:** Independent Whole-System Public-Beta Audit  
**Established:** 2026-09-15  
**Live repair-state checkpoint:** R1.13 / `WSA-2026-040` closure, 2026-10-02  
**Status:** CANONICAL LIVE FINDING INDEX / POST-AUDIT REPAIR STATE

## 1. Authority and preserved history

This file is the canonical live index for current finding state during the ordered repair program.

The complete original audit register through Wave R0 is preserved byte-for-byte at:

`FINDING-REGISTER-THROUGH-R0-2026-09-17.md`

with blob SHA:

`0bf2aff584a0e9b1f18c1325cc0279e44dd6628f`

The complete live register immediately after R1.1 / WSA-2026-009 is preserved byte-for-byte at:

`FINDING-REGISTER-THROUGH-R1.1-2026-09-17.md`

with blob SHA:

`4defe78d3b16a930b9f11fc5279edbe1faebef55`

Those preserved files retain the original detailed finding records, contradiction/evidence indexes, prior closure overlays, allocation history, negative-space checks, evidence limitations and downstream rules. They must not be rewritten.

Rules:

1. Finding IDs are stable and are never renumbered or reused.
2. Historical severity/confidence/evidence remain authoritative unless an explicit later record changes them.
3. A finding becomes CLOSED only after owner repair, exact regression evidence, required rechecks and a closure packet.
4. One closure never implicitly closes adjacent findings or whole-system gates.
5. New findings continue from the next unused global ID.
6. Dashboard MC1.4 and owner dogfood remain paused until R0-R6 plus the bounded final independent recheck release them.

**Next unused finding ID:** `WSA-2026-064`.

## 2. Current counts

| Dimension | Count |
|---|---:|
| Historical findings | 63 |
| PROVEN | 63 |
| OPEN | **46** |
| CLOSED | **17** |
| Historical BLOCKERs | 4 |
| OPEN BLOCKERs | **0** |

Historical severity totals remain: BLOCKER 4, HIGH 24, MEDIUM 22, LOW 12, INFO 1.

The whole-system verdict remains **NO-GO**.

## 3. Current state by finding

### CLOSED

`WSA-2026-006`, `WSA-2026-009`, `WSA-2026-012`, `WSA-2026-016`, `WSA-2026-020`, `WSA-2026-022`, `WSA-2026-023`, `WSA-2026-024`, `WSA-2026-029`, `WSA-2026-030`, `WSA-2026-031`, `WSA-2026-032`, `WSA-2026-033`, `WSA-2026-038`, `WSA-2026-039`, `WSA-2026-040`, `WSA-2026-051`.

### OPEN

`WSA-2026-001`, `002`, `003`, `004`, `005`, `007`, `008`, `010`, `011`, `013`, `014`, `015`, `017`, `018`, `019`, `021`, `025`, `026`, `027`, `028`, `034`, `035`, `036`, `037`, `041`, `042`, `043`, `044`, `045`, `046`, `047`, `048`, `049`, `050`, `052`, `053`, `054`, `055`, `056`, `057`, `058`, `059`, `060`, `061`, `062`, `063`.

For each finding's original title, severity, confidence, root area, affected repositories, expected/observed law, evidence IDs, impact and required closure evidence, use the preserved detailed registers above.

## 4. Accepted post-audit closures

| Finding | Owner | Repair PR | Merged owner ref | Closure packet |
|---|---|---|---|---|
| `WSA-2026-006` | `AI-Verse-Gateway` | `#32` | `5347a0b7e3f3f302f4570e9bc37d515192753610` | `../repairs/WSA-2026-006-GATEWAY-DESTRUCTIVE-PURGE.md` |
| `WSA-2026-012` | `AI-Verse-Memory` | `#30` | `7a1ed5777fd11616375501d730fcbd488beff8b8` | `../repairs/WSA-2026-012-MEMORY-LIFECYCLE-CONTAINMENT.md` |
| `WSA-2026-016` | `AI-Verse-Skills` | `#15` | `3541d2a7af1b20ca12736ed7454d119295d8e193` | `../repairs/WSA-2026-016-SKILLS-CONTROLLER-CONTAINMENT.md` |
| `WSA-2026-029` | `AI-Verse-Connections` | `#2` | `a04f655c6f0c9b57d17e64b5c1ff8eb88aab4016` | `../repairs/WSA-2026-029-CONNECTIONS-DESTRUCTIVE-PURGE.md` |
| `WSA-2026-009` | `AI-Verse-Brain` | `#24` | `908f9a9a06c2b12204ada7f71cd761bae97b52ce` | `../repairs/WSA-2026-009-BRAIN-NATIVE-HOST-ROOT-CONTAINMENT.md` |
| `WSA-2026-020` | `AI-Verse-Data` | `#17` | `491e22084418f34b849c7d9e700a40973888dcf6` | `../repairs/WSA-2026-020-DATA-TRUSTED-SCOPE-PROVENANCE.md` |
| `WSA-2026-022` | `AI-Verse-Multiple-Bots` | `#69` | `cb20bfd014530a7faa26e6abc868d8f85226ec79` | `../repairs/WSA-2026-022-MULTIPLE-BOTS-OPERATOR-AUTHORITY-BINDING.md` |
| `WSA-2026-023` | `AI-Verse-Multiple-Bots` | `#70` | `e84090f932762316a985e30054859bb846bca963` | `../repairs/WSA-2026-023-MULTIPLE-BOTS-WORKER-WORKSPACE-ISOLATION.md` |
| `WSA-2026-024` | `ai-verse-token` | `#1` | `1a85d0da0e529b659b62d3c9a3e2d40c853d67d3` | `../repairs/WSA-2026-024-TOKEN-TRUSTED-ACTUAL-ADMISSION.md` |
| `WSA-2026-030` | `AI-Verse-Connections` | `#3` | `ac8e34cffeaaa0417aaf5011a2379af1b044bf96` | `../repairs/WSA-2026-030-CONNECTIONS-INSTALLATION-SYSTEM-BINDING.md` |
| `WSA-2026-031` | `AI-Verse-Connections` | `#4` | `78a9843e338f2e301e7a8c7c3153d5b43cb69ea4` | `../repairs/WSA-2026-031-CONNECTIONS-CREDENTIAL-ORIGIN-BINDING.md` |
| `WSA-2026-033` | `AI-Verse-Connections` | `#5` | `5759425fcf3692ce64f4834aaa1b101c483c8a34` | `../repairs/WSA-2026-033-CONNECTIONS-NORMALIZED-PATH-AUTHORIZATION.md` |
| `WSA-2026-051` | `AI-Verse-Connections` | `#6` | `63f8698545d731654f76684bf6ba40248996fc6a` | `../repairs/WSA-2026-051-CONNECTIONS-DNS-REBINDING-CONTAINMENT.md` |
| `WSA-2026-032` | `AI-Verse-Connections` | `#7` | `65566b6cc99cc8e26bcacf1a985a1f43c6a42fe6` | `../repairs/WSA-2026-032-CONNECTIONS-FINAL-EDGE-AUTHORITY.md` |
| `WSA-2026-038` | `AI-Verse-Dashboard` | `#11` | `fe0119235df5227560b3a0ef9be8cf85d8aa1d4c` | `../repairs/WSA-2026-038-DASHBOARD-WEBSOCKET-WORKSPACE-ISOLATION.md` |
| `WSA-2026-039` | `AI-Verse-Dashboard` | `#12` | `c9e29ab660c7f56bea83dd00050a1342286734dc` | `../repairs/WSA-2026-039-DASHBOARD-REGISTERED-ROOT-IDENTITY.md` |
| `WSA-2026-040` | `AI-Verse-Dashboard` | `#13` | `359a19f683a15485299cb2bab4e844d8d05b4fd6` | `../repairs/WSA-2026-040-DASHBOARD-LOCAL-READ-AUTHENTICATION.md` |

## 5. WSA-2026-020 closure overlay

**Transition:** `OPEN -> CLOSED`  
**Severity/confidence:** HIGH / PROVEN, unchanged  
**Audited/live pre-repair Data ref:** `8edde7dca5afa34e300130cc6b8ee2b4170ad40f`  
**Repair PR:** `AI-Verse-Data#17`  
**Final tested PR head:** `8c30a5557f03cccfb5e96410b18732f9654ff531`  
**Merged Data ref:** `491e22084418f34b849c7d9e700a40973888dcf6`  
**Reviewed/merged product tree:** `a1c8b251f8820b7066f60135895fcb928227d44b`

Closure evidence:

- genuine TrustedDataRoot instances are runtime-authenticated through module-private provenance;
- genuine Data scopes are runtime-authenticated through a module-private scope registry;
- structural lookalikes, copied visible fields/methods and forged roots do not acquire authority;
- storage open derives root, workspace binding and database path from private authoritative facts rather than caller-visible scope values;
- trusted roots/scopes/bindings are immutable after construction;
- forged scopes fail before outside storage is created or opened, including through `createDataClient`;
- five permanent focused provenance/tampering regressions were added;
- PR-head CI `35259285539`: SUCCESS, all six Ubuntu/macOS/Windows Node 22/24 jobs;
- PR-head Release Smoke `35259285534`: SUCCESS;
- PR-head Five-Component Release Acceptance `35259285592`: SUCCESS, 3/3 install-order jobs;
- final tested PR tree equals merged tree exactly;
- post-merge CI `35259564907`: SUCCESS, all six matrix jobs;
- open Data PRs after merge: 0;
- A1.6 finding-specific recheck: PASS for WSA-2026-020 only;
- Data branch of A2.4 trusted scope isolation: RESOLVED for this finding;
- Data branch of A3.10 cross-root isolation: RESOLVED for this finding; journey remains incomplete overall;
- Data branch of A4.1 forged scope/path authority: RESOLVED for this finding; adversarial phase remains incomplete overall.

`WSA-2026-021` remains OPEN and was not modified.

## 6. WSA-2026-022 closure overlay

**Transition:** `OPEN -> CLOSED`  
**Severity/confidence:** HIGH / PROVEN, unchanged  
**Audited/live pre-repair Multiple Bots ref:** `c600e2bc014351a61e1c0e2673fc63f5d5fa54ec`  
**Repair PR:** `AI-Verse-Multiple-Bots#69`  
**Final tested PR head:** `7c31c18fa789f5b4a7f377fa781db85764f1b7a9`  
**Merged Multiple Bots ref:** `cb20bfd014530a7faa26e6abc868d8f85226ec79`  
**Reviewed/merged product tree:** `4c2bd28712cd10c43af57ad1f9c1c5cf875e350b`

Closure evidence:

- normal bearer transport remains Gateway access only and carries no operator/domain mutation authority;
- trusted operator authority is explicitly host/session bound;
- claimed operator provenance must match the authenticated bound operator principal;
- Bot lifecycle/rebind, Approval decisions, dead-letter retry, Task/Team Run operator overrides and Handoff operator override fail closed without trusted operator authority;
- existing Task creator/owner/assignee, Team Run leader and Handoff-target rights remain intact;
- dedicated regressions prove transport-only bearer cannot self-grant operator controls and cannot switch operator identity;
- PR-head CI `35284371590`: SUCCESS; npm test 519/519, Phase 4 eval 5/5, pack check PASS, release eval 7/7;
- exact PR-head and merged product tree: identical;
- merged-main CI `35284559449`: SUCCESS; npm test 519/519, Phase 4 eval 5/5, pack check PASS, release eval 7/7;
- open Multiple Bots PRs after merge: 0;
- A1.7 finding-specific recheck: PASS for WSA-2026-022 / C-A1.7-001;
- secure-remote operator-control seam: RESOLVED for this finding;
- adversarial operator identity spoofing recheck: PASS;
- cancellation/control domain-law recheck: PASS with legitimate non-operator rights preserved.

`WSA-2026-023` remains OPEN and was not modified.

## 7. WSA-2026-023 closure overlay

**Transition:** `OPEN -> CLOSED`  
**Severity/confidence:** HIGH / PROVEN, unchanged  
**Live pre-repair Multiple Bots ref:** `cb20bfd014530a7faa26e6abc868d8f85226ec79`  
**Repair PR:** `AI-Verse-Multiple-Bots#70`  
**Final tested PR head:** `c451e4a4065f4e5ecb9026a5a453cf7573ce2cef`  
**Merged Multiple Bots ref:** `e84090f932762316a985e30054859bb846bca963`  
**Reviewed/merged product tree:** `c01ede3789b38409438b6baf6aa0526c5ef1c4e7`

Closure evidence:

- existing Workers are first-class principals for generic workspace validation;
- Worker scope is proven against both canonical Worker workspace and Team Run workspace;
- foreign-workspace Worker delegation fails before Task/lease/queue persistence;
- direct Worker messaging is workspace-validated for Worker targets and Worker senders;
- runner failure cleanup changes Worker state only after Task/Worker/Team Run binding is proven;
- cancellation cannot invoke or mutate a Worker from a foreign/unbound Task;
- initial CI `35285759155` caught an over-broad lifecycle/planning interpretation before merge;
- final policy was narrowed to scope-only while preserving the canonical failure/cancel fence;
- final PR-head CI `35285867694`: SUCCESS; npm test 523/523, Phase 4 eval 5/5, pack check PASS, release eval 7/7;
- exact tested PR tree and merged product tree: identical;
- merged-main CI `35286065219`: SUCCESS; npm test 523/523, Phase 4 eval 5/5, pack check PASS, release eval 7/7;
- open Multiple Bots PRs after merge: 0;
- A1.7 / C-A1.7-002 finding-specific recheck: RESOLVED for WSA-2026-023;
- generic Worker delegation seam: PASS;
- direct Worker message seam: PASS;
- adversarial failure/cancel Worker mutation recheck: PASS;
- valid fan-out, manager execution, final publication, handoff and Worker integrations remain green.

`WSA-2026-024` remains OPEN and was not modified.

## 8. WSA-2026-024 closure overlay

**Transition:** `OPEN -> CLOSED`  
**Severity/confidence:** HIGH / PROVEN, unchanged  
**Audited/live pre-repair Token ref:** `23b7b8ecbc9d9ef267f5e10449f785eb11107dd4`  
**Repair PR:** `ai-verse-token#1`  
**Final tested PR head:** `2656bc110b21cbf89ff10a866c8ddf7c45244eab`  
**Merged Token ref:** `1a85d0da0e529b659b62d3c9a3e2d40c853d67d3`  
**Reviewed/merged product tree:** `486cc2da61648e02179e2dbeb0b0c9d448ec6d1f`

Closure evidence:

- TokenLedger rejects non-null ACTUAL money without internal trusted-source admission before canonical persistence;
- plain objects, generic storage callers and arbitrary collectors cannot self-assert ACTUAL;
- public ActualCostSourceRegistry attachment alone does not grant canonical ledger authority;
- trusted OpenRouter, Hermes and Command Code implementations issue exact-event internal admission;
- admission is non-enumerable/non-serializable, bound to registered source route and exact canonical event JSON;
- JSON clones and post-seal mutations fail closed;
- CollectorRunner preserves a valid proof only across exact canonical normalization;
- rejected arbitrary collector ACTUAL does not advance its checkpoint;
- trusted-admission implementation is absent from package public exports;
- initial CI `35329251285` correctly exposed legacy synthetic-ACTUAL test fixtures using the now-forbidden generic path;
- production admission was not weakened; only intentional ACTUAL test fixtures were migrated to the internal test-only trusted path;
- final PR-head CI `35329691387`: SUCCESS, 6/6 Ubuntu/macOS/Windows × Node 22/24 jobs;
- representative PR-head suite: 262/262 tests plus 3/3 release acceptance;
- exact tested PR tree and merged product tree: identical;
- merged-main CI `35329970704`: SUCCESS, 6/6 matrix jobs;
- representative merged-main suite: 262/262 tests plus 3/3 release acceptance;
- open Token PRs after merge: 0;
- A1.8 / C-A1.8-001 finding-specific recheck: RESOLVED for WSA-2026-024;
- direct-storage, collector, public-registry, trusted-source and structural-forgery seams: PASS.

`WSA-2026-025` remains OPEN and was not modified.

## 9. WSA-2026-030 closure overlay

**Transition:** `OPEN -> CLOSED`  
**Severity/confidence:** HIGH / PROVEN, unchanged  
**Audited/live pre-repair Connections ref:** `a04f655c6f0c9b57d17e64b5c1ff8eb88aab4016`  
**Repair PR:** `AI-Verse-Connections#3`  
**Final reviewed PR head:** `8f724c74aef5b8dc22d138f9115f0b1d8de55cb7`  
**Merged Connections ref:** `ac8e34cffeaaa0417aaf5011a2379af1b044bf96`  
**Reviewed/merged product tree:** `0c32b64c87338f708990cc37f218b1c8a86669a5`

Closure evidence:

- lifecycle `systemId` is now the canonical installation system binding;
- Generic and MCP connection creation reject a system different from the installation binding;
- verify, capability admission, approval and reauth reject foreign/legacy connection system state;
- execution resolves an installation-bound connection at planning and again immediately before provider execution;
- ordinary `setup` cannot silently change an existing system binding;
- setup rejects legacy registry state containing connections for another system;
- explicit `rebind-system --from-system <old> --system <new>` is the supported migration path;
- rebind runs under the canonical state lock, migrates connection system IDs and invalidates verification, authorization, approval and capability admission;
- registry-first interrupted rebind remains fail-closed and can be safely retried;
- doctor reports per-connection system-binding mismatches;
- 17 permanent two-system/rebind/recovery scenarios are present in the dedicated regression suite;
- every changed JavaScript/test file passed exact-head V8 syntax parsing;
- exact-head structural recheck of all required WSA-2026-030 authority edges: PASS;
- reviewed PR tree and merged `main` tree are identical;
- open Connections PRs after merge: 0;
- PR-head Actions `35334960224` and merged-main Actions `35335199615` both hit inherited WSA-2026-003 no-runner infrastructure: all six jobs had `steps: null`, so no hosted product tests executed and no green test count is claimed;
- A1.10 / C-A1.10-002 finding-specific recheck: RESOLVED for WSA-2026-030;
- creation, verify/admit/approve, execution, final-edge system-binding, setup/rebind and diagnostic seams: PASS by exact merged-code recheck.

`WSA-2026-032`, `WSA-2026-033`, `WSA-2026-051` and later Connections findings remain OPEN and were not modified.

## 10. WSA-2026-031 closure overlay

**Transition:** `OPEN -> CLOSED`  
**Severity/confidence:** HIGH / PROVEN, unchanged  
**Live pre-repair Connections ref:** `ac8e34cffeaaa0417aaf5011a2379af1b044bf96`  
**Repair PR:** `AI-Verse-Connections#4`  
**Final tested PR head:** `bcd7c8617ec96e36dd6652c969c1dae8d015d928`  
**Merged Connections ref:** `78a9843e338f2e301e7a8c7c3153d5b43cb69ea4`  
**Tested/merged product tree:** `56f6e4e674876e1fe5b38d905800612548bbe838`

Closure evidence:

- one shared MCP credential-origin guard now owns the cross-origin reuse invariant;
- registered MCP security origin is derived from canonical connection URL state;
- add applies the shared guard before persistence;
- reauth applies the same guard before changing the credential handle;
- failed cross-origin reauth preserves the old handle;
- same-origin credential rotation remains allowed;
- verify rechecks the invariant before credential resolution and before any provider request;
- dedicated regression proves cross-origin add and reauth rejection plus same-origin rotation;
- corrupted legacy state using an unavailable conflicting secret fails with `MCP_CREDENTIAL_REUSE_FORBIDDEN` before secret resolution;
- the conflicting origin receives zero HTTP requests in the regression;
- exact-head and post-merge Ubuntu/macOS Node 20/22 checks pass, with 26/26 tests on the successful jobs;
- Windows jobs fail before tests on the pre-existing package-script glob portability issue, not on WSA-2026-031 product logic;
- final tested PR tree and merged product tree are identical;
- open Connections PRs after merge: 0;
- A1.10 / C-A1.10-003: RESOLVED for WSA-2026-031;
- A4.1 credential-origin secret-boundary branch: RESOLVED for this finding.

`WSA-2026-032`, `WSA-2026-051` and later Connections findings remain OPEN and were not modified.

## 11. WSA-2026-033 closure overlay

**Transition:** `OPEN -> CLOSED`  
**Severity/confidence:** HIGH / PROVEN, unchanged  
**Live pre-repair Connections ref:** `78a9843e338f2e301e7a8c7c3153d5b43cb69ea4`  
**Repair PR:** `AI-Verse-Connections#5`  
**Final tested PR head:** `5104ba8412374af69842b86e49b2bbc5235d59c4`  
**Merged Connections ref:** `5759425fcf3692ce64f4834aaa1b101c483c8a34`  
**Tested/merged product tree:** `100bf2d82f6935c745dd33aa5174fb300b3974a2`

Closure evidence:

- admitted Generic API path prefixes are canonicalized before use;
- raw and encoded dot-segment/path-separator confusion forms fail closed;
- URL construction now happens before path authorization;
- normalized `target.pathname`, not the raw caller string, is authorized;
- path-boundary matching prevents `/v1` from authorizing `/v10`;
- query-only encoded traversal text does not alter pathname authorization;
- the final normalized outbound pathname is rechecked against current admitted prefixes immediately before fetch;
- dedicated WSA-2026-033 regressions cover plain, encoded, mixed-case, nested, separator, boundary, query-only and final-edge cases;
- exact-head and merged-main Ubuntu/macOS Node 20/22 checks pass with 29/29 tests on representative successful jobs;
- Windows jobs still fail before tests on the pre-existing shell-glob portability defect;
- final tested PR tree and merged product tree are identical;
- open Connections PRs after merge: 0;
- A1.10 / C-A1.10-005: RESOLVED for WSA-2026-033;
- A4.1 normalized path-authorization branch: RESOLVED for this finding.

`WSA-2026-032`, `WSA-2026-051` and later Connections findings remain OPEN and were not modified.

## 12. WSA-2026-051 closure overlay

**Transition:** `OPEN -> CLOSED`  
**Severity/confidence:** HIGH / PROVEN, unchanged  
**Live pre-repair Connections ref:** `5759425fcf3692ce64f4834aaa1b101c483c8a34`  
**Repair PR:** `AI-Verse-Connections#6`  
**Final tested PR head:** `0fceea60789e5145a90570000288c18e67443cfd`  
**Merged Connections ref:** `63f8698545d731654f76684bf6ba40248996fc6a`  
**Tested/merged product tree:** `67413e50942816a15c08b0da5cd2d07c538c1dfa`

Closure evidence:

- target DNS is resolved once under policy and the transport is pinned to an approved address;
- IPv4 and IPv6 DNS answers are validated before transport creation;
- mixed public/private answer sets fail closed by default;
- localhost hostname variants are normalized and denied by default;
- HTTPS keeps the registered DNS hostname for SNI/certificate verification;
- the actual connected remote address is rechecked against the approved DNS set;
- request bytes are withheld until remote-address verification succeeds;
- Generic API and MCP use the same shared protection;
- deterministic rebinding tests model public policy resolution followed by a private connected socket;
- both provider regressions prove zero bearer transmission to the rebound socket;
- exact-head and merged-main Ubuntu/macOS Node 20/22 checks pass with 33/33 tests on representative successful jobs;
- Windows jobs still fail before tests on the pre-existing shell-glob portability defect;
- final tested PR tree and merged product tree are identical;
- open Connections PRs after merge: 0;
- A4.1 / C-A4.1-002: RESOLVED for WSA-2026-051;
- A4.1 / C-A4.1-005: RESOLVED for WSA-2026-051.

`WSA-2026-032` and later Connections findings remain OPEN and were not modified.

## 13. WSA-2026-032 closure overlay

**Transition:** `OPEN -> CLOSED`  
**Severity/confidence:** HIGH / PROVEN, unchanged  
**Live pre-repair Connections ref:** `63f8698545d731654f76684bf6ba40248996fc6a`  
**Repair PR:** `AI-Verse-Connections#7`  
**Final tested PR head:** `303741c330cca01bfef6dc90af03f7ca49c3f47b`  
**Merged Connections ref:** `65566b6cc99cc8e26bcacf1a985a1f43c6a42fe6`  
**Tested/merged product tree:** `150a6fcd5a8916a0b06257e4dac1397446492ef6`

Closure evidence:

- lifecycle readiness is re-read immediately before adapter execution;
- installation, connection and capability authority are recomputed at the final edge;
- budget check plus provider-edge reservation is atomic under the state lock;
- current provider-edge reservations count immediately against minute/day budgets;
- terminal provider receipts link to their budget reservation without double-counting;
- deterministic pre-provider final-edge failures terminalize earlier idempotency holds;
- disable and uninstall races produce zero provider calls;
- distinct-key maxCallsPerMinute race permits exactly one provider call;
- distinct-key maxCallsPerDay race permits exactly one provider call;
- adapter failure terminalizes the provider-edge budget reservation and consumes the budget slot;
- exact-head and merged-main Ubuntu/macOS Node 20/22 checks pass with 38/38 tests on representative successful jobs;
- Windows jobs still fail before tests on the pre-existing shell-glob portability defect;
- final tested PR tree and merged product tree are identical;
- open Connections PRs after merge: 0;
- A1.10 / C-A1.10-004: RESOLVED for WSA-2026-032.

Later Connections findings remain OPEN and were not modified.

## 14. WSA-2026-038 closure overlay

**Transition:** `OPEN -> CLOSED`  
**Severity/confidence:** HIGH / PROVEN, unchanged  
**Live pre-repair Dashboard ref:** `bf6a3a019b07b189c9c701f4edf01e0ded1e7a00`  
**Repair PR:** `AI-Verse-Dashboard#11`  
**Final tested PR head:** `2e1926891c9b74274f89b7be807bce8902ce0853`  
**Merged Dashboard ref:** `fe0119235df5227560b3a0ef9be8cf85d8aa1d4c`  
**Tested/merged product tree:** `8d0ee475e86b4fd963db8b4d013c7fe32e0fcb1a`

Closure evidence:

- WebSocket subscribe frames use the canonical workspace protocol schema;
- requested workspace scope resolves through the registered system/workspace boundary before state changes;
- successful A -> B and B -> A switches remove the previous hub subscription before installing the new one;
- exactly one successful workspace subscription remains active per socket;
- invalid protocol or unregistered replacement scopes are rejected without replacing the current valid scope;
- stale A events do not reach the socket after B becomes active;
- stale B events do not reach the socket after switching back to A;
- socket close removes every tracked subscription and returns the hub to zero subscribers;
- PR-head Actions `37016702464`: Ubuntu/macOS/Windows Node 22 PASS;
- representative exact-head suite: 68 tests, 67 pass, 0 fail, 1 pre-existing skip;
- merged-main Actions `37016845362`: Ubuntu/macOS/Windows Node 22 PASS;
- representative merged-main suite: 68 tests, 67 pass, 0 fail, 1 pre-existing skip;
- final tested PR tree and merged product tree are identical;
- open Dashboard PRs after merge: 0;
- A1.13 / C-A1.13-001: RESOLVED for WSA-2026-038.

`WSA-2026-039`, `WSA-2026-040`, `WSA-2026-041` and `WSA-2026-042` remain OPEN and were not modified.

## 15. WSA-2026-039 closure overlay

**Transition:** `OPEN -> CLOSED`  
**Severity/confidence:** HIGH / PROVEN, unchanged  
**Live pre-repair Dashboard ref:** `fe0119235df5227560b3a0ef9be8cf85d8aa1d4c`  
**Repair PR:** `AI-Verse-Dashboard#12`  
**Final tested PR head:** `facdbfcf58cc36ad92ea28a82410e467d348ccf0`  
**Merged Dashboard ref:** `c9e29ab660c7f56bea83dd00050a1342286734dc`  
**Tested/merged product tree:** `bd150bacf338597cfa72678496fa82d23db46257`

Closure evidence:

- registration binds each approved `systemId` to canonical realpath plus durable filesystem identity;
- root identity remains privileged server-side state and is excluded from public Dashboard views;
- every `resolveRoot()` rechecks the approved filesystem identity before workspace/content reads;
- missing, renamed, same-path replacement and symlink/junction redirection cases fail closed;
- first identity drift marks the system unauthorized and records sticky drift state;
- ordinary `revalidate()` cannot silently bless a replacement root after identity drift;
- explicit `rebind(systemId, candidateRoot)` is the only supported operation that clears drift and approves a changed root;
- rebind preserves duplicate/overlap protections and stable `systemId`;
- replacement workspace content remains unreachable until explicit rebind;
- PR-head Actions `37018365465`: Ubuntu/macOS/Windows Node 22 PASS;
- representative exact-head suite: 73 tests, 72 pass, 0 fail, 1 pre-existing skip;
- merged-main Actions `37018487192`: Ubuntu/macOS/Windows Node 22 PASS;
- representative merged-main suite: 73 tests, 72 pass, 0 fail, 1 pre-existing skip;
- final tested PR tree and merged product tree are identical;
- open Dashboard PRs after merge: 0;
- A1.13 / C-A1.13-002: RESOLVED for WSA-2026-039.

`WSA-2026-040`, `WSA-2026-041` and `WSA-2026-042` remain OPEN and were not modified.

## 16. WSA-2026-040 closure overlay

**Transition:** `OPEN -> CLOSED`  
**Severity/confidence:** HIGH / PROVEN, unchanged  
**Live pre-repair Dashboard ref:** `c9e29ab660c7f56bea83dd00050a1342286734dc`  
**Repair PR:** `AI-Verse-Dashboard#13`  
**Final tested PR head:** `91fcd67ab9e1ae0dfca1f7ffd73f196f5de632cc`  
**Merged Dashboard ref:** `359a19f683a15485299cb2bab4e844d8d05b4fd6`  
**Tested/merged product tree:** `f05af17ed355845468bfb9eabe2863f79fe8e878`

Closure evidence:

- strong per-Gateway local session token is required and weak configured tokens fail before bind;
- every HTTP route is default-deny before route/RPC dispatch;
- every WebSocket upgrade is authenticated before Origin/path/system handling;
- native clients can use `Authorization: Bearer`;
- browser-style clients can use the dedicated auth subprotocol while only the public Dashboard protocol is negotiated back;
- loopback Origin alone does not authenticate;
- valid authentication does not bypass the separate non-loopback Origin policy;
- loopback-only server binding is unchanged;
- current/future RPC methods remain behind the same transport authentication boundary;
- `DashboardClient` requires the local token and sends bearer credentials automatically;
- unauthenticated health/read/command/future-route and WebSocket negative tests pass;
- token material is not returned in HTTP bodies or the selected WebSocket protocol;
- PR-head Actions `37029230010`: Ubuntu/macOS/Windows Node 22 PASS;
- representative exact-head suite: 76 tests, 75 pass, 0 fail, 1 pre-existing skip;
- merged-main Actions `37029380753`: Ubuntu/macOS/Windows Node 22 PASS;
- representative merged-main suite: 76 tests, 75 pass, 0 fail, 1 pre-existing skip;
- final tested PR tree and merged product tree are identical;
- open Dashboard PRs after merge: 0;
- A1.13 / C-A1.13-003: RESOLVED for WSA-2026-040.

`WSA-2026-041` and `WSA-2026-042` remain OPEN and were not modified.

## 17. Current repair position

- R0: **4 / 4 CLOSED = 100%**.
- R1: **13 / 13 CLOSED = 100%**.
- R2: **0 / 5 CLOSED = 0%**.
- Total: **17 / 63 CLOSED = 26.98%**.
- Remaining: **46 / 63 OPEN = 73.02%**.
- Open BLOCKERs: **0**.
- Current ACTIVE repair: `R2.1 / WSA-2026-007`.
- WSA-2026-007 implementation has **not begun** in this closure.
- Whole-system verdict: **NO-GO**.

## 18. Navigation rule

Use this file for current state. Use the preserved detailed registers for historical audit evidence and prior overlays. Use the exact closure packet for each CLOSED finding, and use `../repairs/REPAIR-EXECUTION-TRACKER-2026-09-17.md` plus `../synthesis/A6.4-ORDERED-REPAIR-PROGRAM.md` for execution order.
