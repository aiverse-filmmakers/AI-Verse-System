# Independent Whole-System Audit Finding Register

**Program:** Independent Whole-System Public-Beta Audit  
**Established:** 2026-09-15  
**Live repair-state checkpoint:** R3.1 / `WSA-2026-008` closure, 2026-10-02  
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
| OPEN | **40** |
| CLOSED | **23** |
| Historical BLOCKERs | 4 |
| OPEN BLOCKERs | **0** |

Historical severity totals remain: BLOCKER 4, HIGH 24, MEDIUM 22, LOW 12, INFO 1.

The whole-system verdict remains **NO-GO**.

## 3. Current state by finding

### CLOSED

`WSA-2026-006`, `WSA-2026-007`, `WSA-2026-008`, `WSA-2026-009`, `WSA-2026-012`, `WSA-2026-013`, `WSA-2026-016`, `WSA-2026-020`, `WSA-2026-022`, `WSA-2026-023`, `WSA-2026-024`, `WSA-2026-026`, `WSA-2026-027`, `WSA-2026-028`, `WSA-2026-029`, `WSA-2026-030`, `WSA-2026-031`, `WSA-2026-032`, `WSA-2026-033`, `WSA-2026-038`, `WSA-2026-039`, `WSA-2026-040`, `WSA-2026-051`.

### OPEN

`WSA-2026-001`, `002`, `003`, `004`, `005`, `010`, `011`, `014`, `015`, `017`, `018`, `019`, `021`, `025`, `034`, `035`, `036`, `037`, `041`, `042`, `043`, `044`, `045`, `046`, `047`, `048`, `049`, `050`, `052`, `053`, `054`, `055`, `056`, `057`, `058`, `059`, `060`, `061`, `062`, `063`.

For each finding's original title, severity, confidence, root area, affected repositories, expected/observed law, evidence IDs, impact and required closure evidence, use the preserved detailed registers above.

## 4. Accepted post-audit closures

| Finding | Owner | Repair PR | Merged owner ref | Closure packet |
|---|---|---|---|---|
| `WSA-2026-006` | `AI-Verse-Gateway` | `#32` | `5347a0b7e3f3f302f4570e9bc37d515192753610` | `../repairs/WSA-2026-006-GATEWAY-DESTRUCTIVE-PURGE.md` |
| `WSA-2026-007` | `AI-Verse-Gateway` | `#33` | `b27cebe11e536aa5a0f9bad707f38b0c2471879d` | `../repairs/WSA-2026-007-GATEWAY-LIVE-LIFECYCLE-TRUTH.md` |
| `WSA-2026-008` | `AI-Verse-Gateway` | `#34` | `cd0789401ddf7c536558a27d84328e963b10c882` | `../repairs/WSA-2026-008-GATEWAY-STATE-LINEARIZABILITY.md` |
| `WSA-2026-012` | `AI-Verse-Memory` | `#30` | `7a1ed5777fd11616375501d730fcbd488beff8b8` | `../repairs/WSA-2026-012-MEMORY-LIFECYCLE-CONTAINMENT.md` |
| `WSA-2026-013` | `AI-Verse-Memory` | `#31` | `cbc6651d60d42c63015bc1b25b5cd8f0c49d5904` | `../repairs/WSA-2026-013-MEMORY-WRITE-LIFECYCLE-AUTHORITY.md` |
| `WSA-2026-026` | `AI-Verse-Automations` | `#4` | `e5ec241f1d86e76b15bab5be81e720a827e4fa09` | `../repairs/WSA-2026-026-AUTOMATIONS-STORE-OWNERSHIP.md` |
| `WSA-2026-027` | `AI-Verse-Automations` | `#5` | `017eaf3e74d604208c606cc08f4137006f723625` | `../repairs/WSA-2026-027-AUTOMATIONS-LIVE-LEGACY-FENCE.md` |
| `WSA-2026-028` | `AI-Verse-Automations` | `#6` | `287ce9d6718ef06e4589a2a3e767c6a9ba376755` | `../repairs/WSA-2026-028-AUTOMATIONS-ATTACHMENT-LIFECYCLE.md` |
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

## 17. WSA-2026-007 closure overlay

**Transition:** `OPEN -> CLOSED`  
**Severity/confidence:** HIGH / PROVEN, unchanged  
**Live pre-repair Gateway ref:** `5347a0b7e3f3f302f4570e9bc37d515192753610`  
**Repair PR:** `AI-Verse-Gateway#33`  
**Final tested PR head:** `8f19c4e70a4014c6e1ab164753999be85e9e3fd4`  
**Merged Gateway ref:** `b27cebe11e536aa5a0f9bad707f38b0c2471879d`  
**Tested/merged product tree:** `f25d6483395416affdf55fe8c05933163594740e`

Closure evidence:

- one owner lifecycle reader now derives absent/setup-required/unhealthy/disabled/ready truth from current disk state;
- setup validates configuration and remote-bind safety before canonical ready publication;
- candidate host compatibility is verified before config publication;
- failed host setup does not replace an existing ready setup;
- failed first setup leaves setup-required and publishes no config/host authority;
- every successful setup receives a service generation;
- startServer re-reads owner lifecycle/config and rejects stale generations;
- every live request rechecks lifecycle state;
- disabled/absent/unhealthy/setup-required/restart-required states are fenced before operational routes;
- live status/health expose current lifecycle diagnostics;
- disable while live changes CLI status, doctor and live status to disabled and operational traffic receives GATEWAY_DISABLED;
- enable restores live readiness within the same setup generation;
- uninstall while live changes CLI status, doctor and live status to absent and operational traffic receives GATEWAY_ABSENT;
- uninstall/reinstall setup creates a new generation so the old process becomes restart-required instead of reviving;
- fresh server start on the new generation succeeds;
- pre-existing remote-bind override security remains green;
- exact-head CI `37032145023`: Ubuntu/macOS/Windows Node 20/22 all PASS;
- representative exact-head suite: 107 tests, 107 pass, 0 fail, 0 skipped;
- exact-head Context Ladder Integrated Acceptance `37032144965`: PASS;
- exact-head Permanent Bot Composition `37032144825`: PASS;
- exact-head Temporary Worker Composition `37032145348`: PASS;
- exact-head Automation Recommendation Boundary `37032145079`: PASS;
- merged-main CI `37032364023`: Ubuntu/macOS/Windows Node 20/22 all PASS;
- representative merged-main suite: 107 tests, 107 pass, 0 fail, 0 skipped;
- final tested PR tree and merged product tree are identical;
- open Gateway PRs after merge: 0;
- A1.2 / C-A1.2-001: RESOLVED for WSA-2026-007;
- A2.3 Gateway lifecycle/status branch: RESOLVED for this finding;
- A3.10 / C-A3.10-002 Gateway branch: RESOLVED for this finding.

`WSA-2026-008` and later Gateway/concurrency findings remain OPEN and were not modified. Memory and Automations lifecycle findings remain independent and OPEN.

## 18. WSA-2026-013 closure overlay

**Transition:** `OPEN -> CLOSED`  
**Severity/confidence:** HIGH / PROVEN, unchanged  
**Live pre-repair Memory ref:** `7a1ed5777fd11616375501d730fcbd488beff8b8`  
**Repair PR:** `AI-Verse-Memory#31`  
**Final tested PR head:** `d998cb2612b42d11727d39429fb45b3b11999062`  
**Merged Memory ref:** `cbc6651d60d42c63015bc1b25b5cd8f0c49d5904`  
**Tested/merged product tree:** `4444ff070fd55c604a80c072081068bb265ccde6`

Closure evidence:

- native canonical mutation consumes current local registry, component setup receipt and migration authority state;
- normal writes require registry supported/installed/enabled, current registry attachment, receipt installed/enabled and setup-complete;
- loaded Memory code cannot write before setup or after disable, detach or uninstall;
- preserved canonical data does not grant write authority after uninstall/reinstall without setup;
- registry supported=false and installed=false each fail closed;
- migration-required blocks ordinary canonical writes;
- explicit migration/recovery uses a narrow migration intent while still requiring base lifecycle readiness;
- standalone retired-authority semantics remain unchanged;
- atomics, session digests, promotion and metadata mutation have lifecycle-transition regressions;
- same-process mutations serialize through a process-local mutex while the existing durable file lock remains cross-process authority;
- exact-head workflow `37037225207`: all 12 jobs PASS;
- representative exact-head unit suite: 127 tests, 126 pass, 0 fail, 1 existing skip;
- exact-head public-beta acceptance passes Ubuntu/macOS/Windows;
- exact-head installer smoke passes Ubuntu/Windows and proves pre-setup denial then post-setup success;
- merged-main workflow `37037623090`: all 12 jobs PASS;
- representative merged-main unit suite: 127 tests, 126 pass, 0 fail, 1 existing skip;
- final tested PR tree and merged product tree are identical;
- open Memory PRs after merge: 0;
- A1.4 / C-A1.4-002: RESOLVED for WSA-2026-013;
- A2.3 Memory lifecycle/write-admission branch: RESOLVED for this finding;
- A3.10 / C-A3.10-002 Memory branch: RESOLVED for this finding.

`WSA-2026-014`, `WSA-2026-015` and Automations lifecycle findings remain OPEN and were not modified.

## 19. WSA-2026-026 closure overlay

**Transition:** `OPEN -> CLOSED`  
**Severity/confidence:** HIGH / PROVEN, unchanged  
**Live pre-repair Automations ref:** `caaed83b98026dd955640fc015d181529b91a1c6`  
**Repair PR:** `AI-Verse-Automations#4`  
**Final tested PR head:** `2fca42703abcb22a54ac55113c3f9e4d6d5e62d5`  
**Merged Automations ref:** `e5ec241f1d86e76b15bab5be81e720a827e4fa09`  
**Tested/merged product tree:** `1c5d09d9c0d287b1eb42f031482c6c0f9819899a`

Closure evidence:

- durable SQLite `application_id`, `user_version` and `meta.owner_id` now identify the canonical Automations store;
- canonical access requires current owner identity, schema version and the exact required Automations schema;
- schema validation covers required tables, columns, foreign keys and indexes including uniqueness;
- non-empty valid foreign SQLite is rejected before Automations schema or metadata writes;
- only exact known unmarked v2 and exact known v1 Automations formats are admitted for adoption/migration;
- v1 `runs.claim_owner` migration runs only after exact prior-format proof;
- missing required tables/indexes and wrong owner/version markers fail closed;
- descriptor reports invalid store identity/schema as unhealthy;
- doctor does not issue operational queries against an invalid foreign/incompatible store;
- PR-head CI `37045314691`: 9 / 9 Ubuntu/macOS/Windows Python 3.11/3.12/3.13 jobs PASS;
- representative exact-head suite: 41 / 41 tests PASS;
- merged-main CI `37045503553`: 9 / 9 jobs PASS;
- representative merged-main suite: 41 / 41 tests PASS;
- exact tested PR tree and merged product tree are identical;
- open Automations PRs after merge: 0;
- A1.9 / C-A1.9-001: RESOLVED for WSA-2026-026;
- A2.3 canonical-store health/readiness branch: RESOLVED for this finding;
- A3.2 known-compatible store adoption branch: RESOLVED for this finding;
- existing A3.7 replay and A3.10 recovery behavior remains green under the full owner suite.

`WSA-2026-027` and `WSA-2026-028` remain OPEN and were not modified.

## 20. WSA-2026-027 closure overlay

**Transition:** `OPEN -> CLOSED`  
**Severity/confidence:** HIGH / PROVEN, unchanged  
**Live pre-repair Automations ref:** `e5ec241f1d86e76b15bab5be81e720a827e4fa09`  
**Repair PR:** `AI-Verse-Automations#5`  
**Final tested PR head:** `d9b2d9bbbfdf0175dae75b70422d20f335d61c3b`  
**Merged Automations ref:** `017eaf3e74d604208c606cc08f4137006f723625`  
**Tested/merged product tree:** `47193905f91583ed82aa197062d724e2ed515fd5`

Closure evidence:

- one shared live migration-authority reader combines configured handoff state with current legacy-definition discovery;
- status changes from ready to migration-required immediately when a legacy definition appears after setup;
- doctor uses the same live authority snapshot and agrees with status;
- enable refuses both configured and newly discovered legacy authority conflicts;
- scheduler tick returns without claim, retry or trigger advancement while a live conflict exists;
- manual and event ingress reject the conflict before creating a run;
- an already claimed run becomes blocked with LEGACY_AUTHORITY_CONFLICT rather than being delivered;
- blocked runs remain explicitly recoverable after the legacy conflict is removed;
- live authority is re-read immediately before the downstream delivery edge;
- a conflict injected during the OS permission check still produces zero downstream requests;
- post-setup discovered conflict removal restores live readiness because no configured handoff state was created;
- setup-time configured migration state remains latched until the explicit existing setup/handoff path clears it;
- PR-head CI `37048094225`: 9 / 9 Ubuntu/macOS/Windows Python 3.11/3.12/3.13 jobs PASS;
- representative exact-head suite: 46 / 46 tests PASS;
- merged-main CI `37048371219`: 9 / 9 jobs PASS;
- representative merged-main suite: 46 / 46 tests PASS;
- exact tested PR tree and merged product tree are identical;
- open Automations PRs after merge: 0;
- A1.9 / C-A1.9-002: RESOLVED for WSA-2026-027;
- A2.3 Automations live lifecycle/readiness branch: RESOLVED for this finding;
- A3.2 legacy-authority handoff fence: RESOLVED for this finding;
- A3.7 scheduler replay behavior remains green under the full owner suite;
- A3.10 lifecycle/recovery behavior remains green, including blocked-run recovery.

`WSA-2026-028` remains OPEN and was not modified.

## 21. WSA-2026-028 closure overlay

**Transition:** `OPEN -> CLOSED`  
**Severity/confidence:** MEDIUM / PROVEN, unchanged  
**Live pre-repair Automations ref:** `017eaf3e74d604208c606cc08f4137006f723625`  
**Repair PR:** `AI-Verse-Automations#6`  
**Final tested PR head:** `edd096f51523659c3aae899008567ef291f1b15e`  
**Merged Automations ref:** `287ce9d6718ef06e4589a2a3e767c6a9ba376755`  
**Tested/merged product tree:** `9791f8bd1c0c3a2aaf262d76809dd1c440d05a66`

Closure evidence:

- attached registry enabled state now follows canonical component enable/disable truth;
- attach-os reconciles an existing divergent enabled flag back to component truth;
- status exposes attachment installed/enabled/files/consistency state;
- doctor treats attachment divergence as a critical unhealthy condition;
- enable/disable synchronization runs under the existing exclusive registry lock and raw-text lost-update check;
- component lifecycle mutation rolls back if registry synchronization cannot acquire the lock;
- unattached standalone enable/disable remains side-effect free and does not materialize extension directories;
- uninstall first fences the component, then removes the owned registry entry and exact owned bridge files;
- uninstall preserves canonical SQLite definitions/runs;
- uninstall refuses to remove modified/unsafe extension-owned files;
- unrelated registry fields and extension entries survive disable and uninstall;
- reinstall setup remains detached until explicit attach-os, then materializes a current enabled registration;
- PR-head CI `37050123823`: 9 / 9 Ubuntu/macOS/Windows Python 3.11/3.12/3.13 jobs PASS;
- representative exact-head suite: 51 / 51 tests PASS;
- merged-main CI `37050285820`: 9 / 9 jobs PASS;
- representative merged-main suite: 51 / 51 tests PASS;
- exact tested PR tree and merged product tree are identical;
- open Automations PRs after merge: 0;
- A1.9 / C-A1.9-003: RESOLVED for WSA-2026-028;
- A2.3 Automations attachment/component lifecycle branch: RESOLVED for this finding;
- A3.10 uninstall/reinstall lifecycle branch: RESOLVED for this finding.

**Wave R2 is now complete: 5 / 5 CLOSED.**

## 22. WSA-2026-008 closure overlay

**Transition:** `OPEN -> CLOSED`  
**Severity/confidence:** HIGH / PROVEN, unchanged  
**Live pre-repair Gateway ref:** `b27cebe11e536aa5a0f9bad707f38b0c2471879d`  
**Repair PR:** `AI-Verse-Gateway#34`  
**Final tested PR head:** `da359b8db45eb11b04fd1907500117bb8c122bbc`  
**Merged Gateway ref:** `cd0789401ddf7c536558a27d84328e963b10c882`  
**Tested/merged product tree:** `fe02f4271b3f47b25210d81d77caad5c728d708c`

Closure evidence:

- idempotency claim/check/reservation is one serialized mutation;
- concurrent identical first claims admit exactly one reservation and the competing first claim is in-progress rather than a second new operation;
- concurrent changed-payload reuse fails with idempotency conflict;
- idempotency result commit uses the same serialized ledger mutation;
- first session binding is an atomic create-or-validate transition;
- conflicting concurrent first bindings choose one durable binding and reject the loser;
- every run carries a durable revision and normal run mutation increments it;
- stale `saveRun()` uses compare-and-swap and fails with `RUN_REVISION_CONFLICT`;
- pause, resume and cancel mutate current canonical run state atomically;
- runtime return rechecks durable run revision/control authority before result application;
- assistant delta emission rechecks current authority before each emitted chunk;
- owner effects recheck current run authority immediately before delivery;
- approval execution rechecks current awaiting-approval authority before owner delivery;
- pause/cancel during a runtime that ignores control produces no stale assistant stream, completion or owner handoff;
- startup session-digest and organization recovery are serialized;
- graceful server close drains active execution and startup recovery before process handover;
- WSA-008 regressions are included in canonical `npm test`;
- PR-head CI `37055012899`: Ubuntu/macOS/Windows Node 20/22, 6 / 6 jobs PASS;
- representative exact-head suite: 113 / 113 tests PASS;
- exact-head Context Ladder `37055012896`: PASS;
- exact-head Temporary Worker Composition `37055012893`: PASS;
- exact-head Permanent Bot Composition `37055012914`: PASS;
- exact-head Automation Recommendation Boundary `37055012900`: PASS;
- merged-main CI `37055200397`: Ubuntu/macOS/Windows Node 20/22, 6 / 6 jobs PASS;
- representative merged-main suite: 113 / 113 tests PASS;
- exact tested PR tree and merged product tree are identical;
- open Gateway PRs after merge: 0;
- A1.2 / C-A1.2-002: RESOLVED for WSA-2026-008;
- A1.2 / C-A1.2-003: RESOLVED for WSA-2026-008;
- Gateway state-linearizability branch of R3: RESOLVED for this finding.

`WSA-2026-010` is now the next dependency-safe finding and was not modified.

## 23. Current repair position

- R0: **4 / 4 CLOSED = 100%**.
- R1: **13 / 13 CLOSED = 100%**.
- R2: **5 / 5 CLOSED = 100%**.
- R3: **1 / 10 CLOSED = 10%**.
- Total: **23 / 63 CLOSED = 36.51%**.
- Remaining: **40 / 63 OPEN = 63.49%**.
- Open BLOCKERs: **0**.
- Current ACTIVE repair: `R3.2 / WSA-2026-010`.
- WSA-2026-010 implementation has **not begun** in this closure.
- Whole-system verdict: **NO-GO**.

## 24. Navigation rule

Use this file for current state. Use the preserved detailed registers for historical audit evidence and prior overlays. Use the exact closure packet for each CLOSED finding, and use `../repairs/REPAIR-EXECUTION-TRACKER-2026-09-17.md` plus `../synthesis/A6.4-ORDERED-REPAIR-PROGRAM.md` for execution order.
