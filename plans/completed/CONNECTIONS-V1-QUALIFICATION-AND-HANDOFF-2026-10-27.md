# AI-Verse Connections — V1 Qualification and Independent Handoff Plan

**Date:** 2026-10-27  
**Status:** **COMPLETED 2/2 (100%) FOR OWNER-LOCAL V1 QUALIFICATION**, with one evidenced delegated-grant security repair; **Full/member release remains blocked/unadmitted**  
**Planning method:** [Adaptive Implementation Planning Skill](../../docs/ADAPTIVE-IMPLEMENTATION-PLANNING-SKILL.md) + [Implementation Plan Template](../../docs/IMPLEMENTATION-PLAN-TEMPLATE.md). Tasks are derived only when the active slice starts.

## Plan details

- **Outcome / owner / repository:** Qualify current Connections v1 as an independently usable, safe single-user external capability boundary; record whether any actual Gateway/OS caller contract needs a **minimal** repair before a future Full-profile integration. Canonical implementation owner: [`aiverse-filmmakers/AI-Verse-Connections`](https://github.com/aiverse-filmmakers/AI-Verse-Connections). System owns cross-repo planning/reconciliation; Distribution alone owns member release.
- **Planning depth:** **Standard**, two fixed outcome slices. External effects and durable receipts require extended safety controls, but the executable runtime already contains them; reuse the existing [security contract](https://github.com/aiverse-filmmakers/AI-Verse-Connections/blob/main/docs/SECURITY.md), not a duplicate architecture program.
- **Current revision / status:** `main@b557ef1d83a9d6c802070887ca84c3b3df2aef29`, executable `@ai-verse/connections@0.1.0-beta.1`, `private:true` in `package.json` (no npm publish claim). Exact current [main CI 38384137363](https://github.com/aiverse-filmmakers/AI-Verse-Connections/actions/runs/38384137363) passed **6/6 Ubuntu/macOS/Windows × Node 20/22**. Main security/recovery workflows and release-descriptor validation passed at that SHA. Pinned candidate descriptor revision `602a1c52ab782cc9a8b7a4caa60ccb29efe403d1`, with historically accepted owner-native [CI 37182362458](https://github.com/aiverse-filmmakers/AI-Verse-Connections/actions/runs/37182362458).
- **Release reality:** System's 26 October [Repository State](../../governance/repository-state.json) observed current source, but reports Connections owner acceptance **`unverified`**, candidate descriptor **`candidate`**, and Distribution **`unpinned`**. Full profile is not admitted. The [13 September Connections QC](../../components/ai-verse-connections/QC.md) and [older blueprint snapshot](../../docs/FINAL-AI-VERSE-BLUEPRINT.md) describe the former *research-only* seed and are historical; they must not govern today's implementation claims. Do not rewrite that history as if it never happened.
- **Fixed outcomes:** **2 slices**: C1 prove current code/contract and classify actual gaps; C2 verify/reuse one supported local provider execution seam and produce a bounded owner handoff. Overall **2/2 slices COMPLETE (100%)**. Existing v1 functionality reused; exactly one demonstrated security defect fixed with regression evidence. No feature expansion.

## Product brief

- **Who needs this / observed problem:** A filmmaker/agent should be able to use a permitted external capability through one local OS's Connections boundary, without pasting secret tokens into models or bypassing workspace/approval policy. Existing Connections already supplies registry, credentials, provider adapters, execution and recovery, but System release status and later Gateway/Full adoption have not been newly proven.
- **Desired journey:** Register a **local disposable fake** generic API or MCP provider; verify/discover it; explicitly admit one capability, approve that admitted set, execute once in the allowed system/workspace through the current owner public entrypoint, inspect a receipt and untrusted labeling; verify that revoked permission, changed MCP schema, wrong workspace, spoofed identity or replay blocks any further provider effect. If current tests fully prove this, **reuse those exact tests and do not code again**.
- **Scope:** Existing v1 generic authenticated API and MCP HTTP `2026-07-28` adapter + CLI/library authority and lifecycle. One single-user system, local synthetic provider/temporary state, current immutable source/evidence and any **currently declared** consumer protocol. Repository owner owns fixes; System records decisions. Network access to real providers **excluded** by default.
- **Non-goals:** Provider marketplace, OAuth browser login, MCP stdio, legacy MCP 2025 transport, MCP Tasks/push notifications, multi-user RBAC, external event/trigger ingest, arbitrary cloud accounts, Data sync, Token cost engine, new Gateway execution engine, Dashboard UI code, new component ownership, public Full/member release. New ideas require separate product approval/plan.
- **Keep:** Connection identity and separate configured/liveVerified/healthy/authorized/approved states; system/workspace/lease/approval intersection at **final provider edge**; opaque env/vault credential handles; no secrets in receipts; MCP tool fingerprints/re-approval; SSRF/DNS-rebinding/redirect bounds; untrusted provider-result labeling; append-only receipts/idempotency/recovery, unknown-effect fencing and user-state preservation; owner-controlled lifecycle.
- **Open decisions:** Whether a current Gateway/OS host actually invokes the public Connections contract or only proposes future Full composition. Lack of an already-shipped caller is **not** an invitation to add one to Gateway while Dashboard is changing. A real third-party provider acceptance requires owner account/consent later, outside this plan.

## Permanent laws / no-work rule

1. Connections alone owns external connection/capability/credential boundary and external-effect receipts. OS/Gateway supply caller scope and permission floors. Bots orchestrates Tasks; Automations schedules triggers; Token owns usage/cost evidence; Data owns structured business truth; Dashboard only presents/control-routes.
2. **No connection automatically conveys tool permission.** Mere configured/reachable/discovered status is never authorization; every external effect must satisfy the current exact system/workspace and approval intersections at the final edge.
3. Untrusted external tools, data and self-reported MCP identity may never escalate authority; HTTP origin, DNS, path, redirect and output safety boundaries stay effective.
4. No loss/truncation/implicit replay of canonical receipts or unresolved effects; keep owner state on normal update/uninstall and preserve unknown files.
5. **Do not rebuild V1 or add providers just because the planning document exists.** Existing tests and code should be counted as `REUSE`; only verified defects may produce small owner-source changes. Distribution release/admission remains a separate decision.

## Requirements and checks

| ID | Observable success / meaningful failure / unaffected behavior | Owner / slice | Evidence/check |
| --- | --- | --- | --- |
| C-R01 | Confirm main v1 executable and CI matrix for exact SHA; old seed-only summary must not be treated as the current implementation. | Connections / C1 | Read current package/CLI/src/test contracts, main native [38384137363](https://github.com/aiverse-filmmakers/AI-Verse-Connections/actions/runs/38384137363), security/recovery flows and candidate descriptor. |
| C-R02 | Supported generic/MCP provider verification, explicit capability admission, authorized execution and one canonical receipt already work; missing/disallowed state never silently executes. | Connections / C1,C2 | Reuse existing `connections-core`, `connections-mcp`, `connections-credential-origin` and `connections-final-edge-authority` integration tests, or add one focused gap test only if missing. |
| C-R03 | Revocation immediately wins; provider tool/schema drift clears admission; system/workspace and untrusted origin cannot widen authority. | Connections / C1,C2 | Reuse integration tests for MCP, final edge, DNS-rebinding, normalized path and system-binding; if a proven gap exists, reproduce with a disposable provider before fixing. |
| C-R04 | Replays, crashed/unknown provider effects, receipts and budgets cannot double-apply or silently truncate; user/credential state remains recoverable. | Connections / C1,C2 | Reuse recovery, write-lock, receipt-scale, purge-foreign, lifecycle and idempotency tests. No actual external side effects. |
| C-R05 | Identify whether a currently shipping Gateway/OS/Bot caller has a specific incompatible v1 contract. Otherwise record that host/Full admission is deferred. | Connections with caller owner / C2 | Trace actual caller code/API, not prose; compare request validation → final-edge decision → provider → receipt/error; no cross-owner edits without separately scoped plan and CI. |
| C-R06 | Owner candidate is not mistaken for an admitted Full member release. `private:true` and `candidate/unpinned` remain honest. | System/Distribution / C2 | Scoped read-only State check; use exact descriptor/current main revisions; future real-account rollout needs explicit permission and Full release qualification. |

No new SLO is assumed. Existing receipt-index 4,096-bucket and budget scaling tests are reused; only measure when current CI or a reported real workload demonstrates degradation.

## Current flow and design choice

- **Actual path:** Operator registers generic/MCP connection → Connections stores identity and opaque credential handle → owner performs live verify/discover (untrusted catalog) → maps/admittedly approves exact tool/capability → Gateway/host forwards a bounded system/workspace/capability lease if integrated → **Connections final-edge rechecks current registry+revocation+scope+approval+rate limits** → provider adapter injects secret at edge → append-only receipt and `untrusted_external` provenance or fixed safe failure.
- **Classification:** `REUSE`: existing credentials, registry, generic HTTP, MCP stateless HTTP, verification, approval, revocation, final-edge enforcement, receipts and all tests. `EXTEND`: only a demonstrated, small missing v1 seam/regression. `BLOCK/UNKNOWN`: unproven live Gateway consumer, external OAuth/provider accounts, Full release. `CREATE`: **none presupposed**. `RETIRE`: no old logic without evidence.
- **Chosen design vs simpler alternative:** Prefer an existing local disposable HTTP/MCP test provider and current public CLI/library. Avoid new provider SDK, service, port, auth store, mirror API, MCP daemon or Dashboard-specific connector; no added dependencies anticipated.
- **Compatibility/security/recovery:** Preserve explicit credential scopes and current receipts; never mutate an actual account or private Core, publish keys, or rewrite another owner's state. If v1 calls fail against a real shipped host due to conflicting ownership/protocol, log exact evidence and mark that specific cross-owner route **BLOCKED** for an approved plan amendment, not an unauthorized Gateway change.

## Applicable risks

| Risk | Concrete decision / evidence | Owner/blocker |
| --- | --- | --- |
| Credentials / private data | Use local fake provider and placeholder secret; never real API key/chat content/production account in CI; secrets only through owner opaque handles. | Connections C1/C2 |
| Permission change during request | Final-edge re-check is required even after planning; disable/revoke/schema drift fail closed; existing authority tests take priority. | Connections C2 |
| SSRF/untrusted tool metadata | Preserve HTTPS-by-default, local-exception test controls, no redirects and DNS origin checks; false provider identity never trusts a tool. | Connections C2 |
| Effect unknown/recovery | Receipt canonical log not truncated, unknown effect never auto-replayed, corruption blocks execution, indexed receipts remain derived. | Connections C1/C2 |
| Cross-platform/packaging | Current CI covers three OS × Node20/22, but does not establish public npm publication or a member installer; `package.json private:true` deliberately remains. | Connections/Distribution |
| Host integration | No claim that Gateway/OS currently registers/discovers every Connections capability. Full profile blocked until composition/permissions separately qualified. | Host/Distribution |
| Scope drift/release | Current component owner descriptor candidate, State owner acceptance unverified, Distribution unpinned. No local CI may override those statuses. | System/Distribution |

## Phases and slices

### Phase 1 — Evidence-first v1 owner qualification

#### Slice C1 — Current V1 implementation, exact-source evidence, and stop/de-duplication decision

- **Requirement IDs / owner:** C-R01…C-R04; Connections owner, System evidence.
- **Dependencies / exact start:** `main@b557ef1d83a9d6c802070887ca84c3b3df2aef29`; [native CI 38384137363](https://github.com/aiverse-filmmakers/AI-Verse-Connections/actions/runs/38384137363) **6/6** plus current security/recovery workflows passing; descriptor candidate `602a1c52...`; current installed runtime v1.
- **Bounded repo/surface:** Existing `src/`, `test/`, `package.json`, `docs/SECURITY.md`, `release/component-release.json` and System evidence map; no Docker/prod keys or new cross-repo APIs.
- **Acceptance/evidence:** Exact caller/owner/authority/recovery path, current test matrix + adversarial coverage reconciled, list of **confirmed** untested/failed v1 requirements (possibly **none**), and explicit statement of which "missing features" are intentionally out of scope. If existing evidence proves V1, complete with **zero code changes**.
- **First useful check / adaptive start task:** `C1.1 - Refresh main, designated CI, and run existing local fake-provider tests; map each C-R02...C-R04 behavior to an actual tested entrypoint before deriving tasks.`
- **Rollout/disable/recovery:** No real provider side effects, no user state or release promotion. A proven regression must get a narrow failing reproduction before fix.
- **Completion / next:** Exact refs/test evidence and small verified gap ledger; then C2. If there are no gaps, proceed with a read-only handoff rather than manufacturing implementation.

### Phase 2 — Minimal current-consumer qualification and release-boundary handoff

#### Slice C2 — Supported fake-provider contract proven or explicitly out-of-scope host blocker recorded

- **Requirement IDs / owner:** C-R02…C-R06; Connections v1/host contract as evidence; System/Distribution record only.
- **Dependencies / exact start:** C1 completed with exact source+test links; frozen current v1 public entrypoints. **Do not begin by writing a new adapter.**
- **Bounded repo/surface:** Reuse existing `test/connections-core.integration.test.js`, `test/connections-mcp.integration.test.js`, `test/connections-system-binding.integration.test.js`, `test/connections-final-edge-authority.integration.test.js` and current release metadata; inspect only the necessary active Gateway/OS caller source. No host/Dashboard commits in this plan.
- **Acceptance/evidence:** A disposable local provider request proves register → verify → admit → approve → execute → receipt and selected negative paths (revoke, workspace mismatch, tool catalog drift, replay/unknown effect), **through the currently supported Connections public entrypoint**; if already conclusively covered, existing exact tests suffice. Record whether a current real host consumer exists and where any unproven Full-profile integration is explicitly deferred. Final state says "Connections V1 qualified owner-locally" or names a **reproduced blocker**; never silently claims live provider or member release.
- **First task / adaptive tasks:** `C2.1 - Compare C1 evidence with one public local fake-provider call and currently shipping caller route; derive only tests/repairs for demonstrably missing behavior.` Potential implementation tasks are intentionally **not pre-authorized**.
- **Rollout/disable/recovery:** Keep test accounts synthetic and local; no provider credential, outside network, state purge or webhook trigger; no runtime promotion. If real host contract requires protected cross-owner changes, block that part and propose a scoped amendment.
- **Completion / next:** Accepted v1 source & CI evidence, qualified bounded local contract (or precise unresolved seam), immutable owner vs Distribution status, no-regression audit, System plan closeout. **Next: Dashboard/Full release owner when ready**, not a speculative "Connections V2".

## Reviews and progress

- **Product/architecture:** Single-user first, minimal UI-dependent development; original v1 architecture reused and no feature proliferation.
- **Code/adversarial:** Test revocation, system scope, untrusted MCP catalog, SSRF and crash recovery before code changes; prefer current fixtures.
- **Behavior/delivery:** Existing v1 candidate may be ready owner-locally while Full Distribution remains blocked; distinguish CI pass from credentialed real-provider qualification.
- **Current checkpoint:** **2/2 verification/qualification slices COMPLETE (100%)** on current owner source `d326e39f4f07fb163250d671b8960a1fc00e8e03`. V1 was already functional; one permission-boundary defect fixed; no broader host/Full acceptance claimed.
- **Next action:** **STOP** Connections v1 scope. Dashboard may consume documented owner-backed read projections via a trusted host; a new Gateway/desktop-host executable bridge and any Full/member release remain separate work, with separate authorization, tests and approval. No real credentials needed for this owner-local closeout.

## 2026-10-27 completed C1 + C2 qualification and bounded Dashboard handoff

**Completed: C1 — Current v1 audit and gap detection (1/1); C2 — Local public provider-edge security proof and host handoff (1/1). Overall: 2/2 fixed slices (100%). Tasks: 2 evidence/repair tasks plus a focused red/green regression and owner handoff. Blockers: none for the stated local v1 scope. Separate, unresolved future Full-profile and real desktop-host execution admission are NOT accepted by this closeout.**

### C1 evidence review and reproduced issue

- Owner `main@b557ef1d83a9d6c802070887ca84c3b3df2aef29` already implemented `ConnectionsService`, generic authenticated HTTP and stateless MCP 2026-07-28 provider, scoped installation/registry, opaque vault/environment handles, verify/discover, explicit capability admit+approve, revoke/re-auth, final-edge checks, idempotent unknown-effect receipt recovery and state-safe uninstall. Existing tests cover local HTTP/MCP providers and adversarial DNS/SSRF, schema drift, revocation, system-binding, concurrency, index recovery and receipt-log corruption. This **supersedes the historical 2026-09-13 research-seed audit as current-state evidence** without erasing that history.
- [Exact main CI 38384137363](https://github.com/aiverse-filmmakers/AI-Verse-Connections/actions/runs/38384137363) was green on six Linux/macOS/Windows × Node20/22 legs. The same SHA's external-effect, receipt-scale and write-lock recovery suites and descriptor gate were green.
- One **actual** permission defect was found in `src/policy.js`: `assertConnectionUsable` only checked the caller lease **if `request.grantedCapabilities` existed**. The already approved read capability could therefore be executed directly by a library caller with **no caller-grant array**, violating final-edge delegated authority intersection. CLI supplying the field did not make the owner API safe. No additional untested expansion was authorized.

### C2 red/green proof and stable integration guidance

- Added one focused disposable local HTTP provider regression `test/connections-delegated-grant-required.integration.test.js` to the Connections owner. Original test-only [CI 40465436849](https://github.com/aiverse-filmmakers/AI-Verse-Connections/actions/runs/40465436849) was intentionally **RED on all 6 platforms/versions** with `Missing expected rejection`; direct service execution reached the provider without the required delegated grant.
- Minimal owner fix changes **one conditional**: `grantedCapabilities` must be an explicit array containing the requested capability, even for approved/read-only capability. No shape change to `execute`, caller/request/result envelopes, provider adapters, credential handling, persisted receipts or existing CLI. The same check is reused at planning and final provider edge. The test proves absent, null, empty, incorrect and malformed grants block provider invocation; explicit matching grant still succeeds with `untrusted_external` label.
- Connections [PR #14](https://github.com/aiverse-filmmakers/AI-Verse-Connections/pull/14) passed final [CI 40465861074](https://github.com/aiverse-filmmakers/AI-Verse-Connections/actions/runs/40465861074) **6/6**, plus same-revision [external-effect recovery 40465861094](https://github.com/aiverse-filmmakers/AI-Verse-Connections/actions/runs/40465861094), [write-lock 40465861064](https://github.com/aiverse-filmmakers/AI-Verse-Connections/actions/runs/40465861064), and [receipt index 40465861115](https://github.com/aiverse-filmmakers/AI-Verse-Connections/actions/runs/40465861115) all green; merged to `d326e39f4f07fb163250d671b8960a1fc00e8e03`.
- [Stable owner-backed Dashboard handoff](https://github.com/aiverse-filmmakers/AI-Verse-Connections/blob/main/docs/DASHBOARD-CONSUMPTION-HANDOFF-2026-10-27.md) lists supported `status()`, `doctor()`, `listConnections()` and operation/receipt/error code semantics. Current `src/index.js` exposes **local `ConnectionsService` and CLI**; a **separately authenticated scope-binding host** is required before browser integration or provider execution. An existing Gateway/OS Connections HTTP execution endpoint was **not** evidenced. UI should start with owner-backed read-only projections; never allow browser/model-supplied trusted grants, raw credentials, scope or direct provider execution.
- The local fake-provider v1 journey, explicit permission and absence-of-provider-call negatives are verified by existing v1 suites plus the new red/green test. **No real third-party account, private Core, host-integrated Dashboard execution, OAuth, MCP stdio or Full release has been tested.** The current owner descriptor remains `candidate` at prior exact accepted source `602a1c52ab782cc9a8b7a4caa60ccb29efe403d1`; last System-generated snapshot says owner evidence `unverified`, Distribution `unpinned`. The code fix's merged head is **not** silently declared newly owner-release-accepted. No Registry/State/Distribution member changes made.

### Stop rule

**C1+C2 satisfied for Connections V1 owner-local safety/contract qualification. STOP new providers and features.** Further work only on a demonstrated defect or a separately approved caller/Full composed acceptance. The future Dashboard can independently bind its native host to existing service read APIs; any new trusted host-to-Connections *execution* adapter, system/workspace scope proof, consent UX and real external credentials require distinct approval/qualification. **No current Dashboard source change requested or performed.**

### Merged-main supplementary Windows race observation (not concealed)

Connections post-merge owner CI [40466076583](https://github.com/aiverse-filmmakers/AI-Verse-Connections/actions/runs/40466076583), [external effect 40466076634](https://github.com/aiverse-filmmakers/AI-Verse-Connections/actions/runs/40466076634), and [receipt index 40466076477](https://github.com/aiverse-filmmakers/AI-Verse-Connections/actions/runs/40466076477) succeeded. The independent [write-lock recovery run 40466076723](https://github.com/aiverse-filmmakers/AI-Verse-Connections/actions/runs/40466076723) initially **failed only on Windows Node20**: concurrent child process returned code 1 before sending `done`, with child stderr suppressed by the existing test harness; Ubuntu/macOS passed. The exact same Windows job was **rerun without modifying source and passed**, completing the same three-OS workflow. Thus no deterministic lock-engine defect or link to the delegated-grant code change was reproduced; no speculative filesystem lock changes are justified by this evidence alone. Retain the original attempt, monitor recurrence, and if it repeats, first capture the child error and reproduce the failing race before a focused repair. This observation does not affect the red/green demonstrated delegated-grant bypass or authorize a release promotion.
