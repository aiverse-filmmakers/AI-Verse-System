# Gateway Completion and Dashboard-Ready Delivery Plan

**Status:** IN PROGRESS, Slice G0.1; Tasks 1–3 of 5 complete; Task 4 authorized in same user request but separately evidenced before completion
**Created:** 2026-10-23
**Plan owner:** `aiverse-filmmakers/AI-Verse-System`
**Canonical code owner:** `aiverse-filmmakers/AI-Verse-Gateway`
**Related owners:** AI-Verse-Dashboard (UI, client integration), AI-Verse-OS (scope/host/authorization), Brain (Goals), Memory/Data/Skills/Multiple Bots/Automations/Connections/Token (their canonical domains), ai-verse-distribution (composition, releases)
**Planning depth:** EXTENDED: persistent run state, authenticated permissions, cross-repo contracts, Windows durability and release gates
**Method:** [Adaptive Implementation Planning Skill](../../docs/ADAPTIVE-IMPLEMENTATION-PLANNING-SKILL.md) and [Implementation Plan Template](../../docs/IMPLEMENTATION-PLAN-TEMPLATE.md)
**Fixed destination:** Finish the *existing* canonical Gateway as a reliable, securely bounded, owner-backed, Dashboard-ready local Agent edge, with verified current-generation chat/runs/events/controls, restart behavior, composed integration and honest release qualification. Do not expand "finish" to speculative enterprise or every future owner feature.
**Checkpoint:** 0 / 10 new acceptance slices complete (0%). This is the remaining-work program, **not** an assertion that existing Gateway is 0% implemented.
**Next:** G0.1 Task 4, explicitly authorized together with Task 3 by the owner: publish the evidence-backed no-duplication gap/collision ledger. Stop after Task 4 until owner says `next` for Task 5.

## 1. Product brief and finish line

A user should open AI-Verse through Chat, Open WebUI or a future Dashboard, select the intended AI-Verse system/workspace, submit a real task, see its run events and approval requirements, and recover or intervene safely after interruption. The UI must never need to write Brain/Memory/Data/Skills/Bots/Automation/Token/Connections truth or interpret a missing owner as successful/empty data.

Currently Gateway already has a Node API, authenticated loopback listener, OpenAI-compatible chat and SSE, sessions/runs/events, durable checkpoints/idempotency, OS host and runtime adapters, run controls and Context Ladder/Purpose/Invisible Intelligence implementations. The remaining issue is **current-generation composed product proof, known platform failure, Dashboard contract consumption and release/admission**, not re-creation of the Gateway.

**In scope:** verified local Agent + Dashboard readiness, defect fixes proven necessary by tests, current owner adapter compatibility, honest degraded capabilities, recovery, Windows/macOS/Linux release evidence and explicit user approval paths.

**Not in scope:** inventing a new Gateway, replacing owner APIs with local stores, building Dashboard panels here, copying Mission Control's backend, new autonomous Bot/Automation consent policy, full enterprise multi-tenant/hosted service, remote Internet exposure by default, speculative model-provider adapters, or simultaneous rewrites across siblings.

**Accepted finish line:** a reproducible disposable local system can authenticate, chat, stream, run a bounded authorized task, observe/cancel/pause/resume/approve appropriately, survive an interrupted/restarted run with truthful recovery, maintain two-system/two-workspace isolation, fail closed on unavailable owner surfaces and incompatible versions, and return a real Mission Control/Dashboard-compatible run result. Gateway-native and composed Linux/macOS/Windows evidence are attached to exact refs. Distribution, not this plan, decides release admission; full Dashboard UI completion is a separate plan.

## 2. Resume prior work, never restart or duplicate

This plan is a **continuation and integration ledger**, not a replacement for the existing programs.

| Existing source | Current evidence / state | Continuation decision |
| --- | --- | --- |
| [Gateway README](https://github.com/aiverse-filmmakers/AI-Verse-Gateway/blob/main/README.md), `src/server.mjs`, `src/run-engine.mjs`, `src/host-adapter.mjs`, `src/store.mjs` | On Gateway `main` `95cc8319c1dc95b05da0ebb451d70469170ca3f8`: actual authenticated API, chat, streaming, run control, owner adapters and durable local state exist; main CI succeeded ([run 38383650023](https://github.com/aiverse-filmmakers/AI-Verse-Gateway/actions/runs/38383650023)). | **REUSE/EXTEND.** Characterize current behavior before a change; do not build another transport, run store, context manager or execution engine. |
| [Invisible Intelligence / Grandma UX](../../docs/INVISIBLE-INTELLIGENCE-AND-GRANDMA-UX-IMPLEMENTATION-PLAN.md) | **24/24 COMPLETE** on its own accepted scope: workspace organization, Memory capture, Skills learning/reuse, Data routing, temporary Workers, permanent Bot/Automation consent and composed A–M proof. Later owner work must be rechecked. | **PRESERVE.** No reimplementation or new consent authority; test against current owners where Gateway changes touch paths. |
| [Context Ladder + Lossless Memory](../../docs/CONTEXT-LADDER-AND-LOSSLESS-MEMORY-IMPLEMENTATION-PLAN.md) | **25/25 COMPLETE** and immutable Agent candidate Gateway ref `46c15ee58b028dd7fb8b310327ea705ef618805e` qualified in its historical exact release set. | **PRESERVE/VERIFY.** Reuse fold store, source-exact retrieval, progressive context and context governor. Upgrade only measured failures and do not weaken provenance/freshness. |
| [Purpose Context v1](../../docs/PURPOSE-CONTEXT-IMPLEMENTATION-PLAN.md) | **COMPLETE** for v1, including Gateway strategic proposal/confirmation/owner-receipt and post-write projection behavior; Gateway latest candidate descriptor targets `1772b75e2add73a524715f746e87b3a6b5561bf6`. | **PRESERVE.** Do not create Goal/Purpose database in Gateway. Route strategic effects to Brain/OS and refresh canonical projection only after owner outcome. |
| [Independent audit and repair](../../docs/public-beta-audit/repairs/REPAIR-EXECUTION-TRACKER-2026-09-17.md) and [final recheck](../../docs/public-beta-audit/repairs/FINAL-INDEPENDENT-RECHECK-2026-10-05.md) | **63/63 findings closed**; **conditional supervised synthetic-data Agent dogfood**, not unrestricted/full-profile clearance. Gateway destructive purge, lifecycle, linearizability, source freshness, pre-auth CPU and idempotency scale repairs have closure evidence. | **PRESERVE/REVALIDATE.** Do not re-audit 63 repaired items without new evidence; use their regressions and release gates. |
| [Gateway issue #60](https://github.com/aiverse-filmmakers/AI-Verse-Gateway/issues/60) | **OPEN:** repeated Windows `EPERM` atomic run-state rename during Distribution composed two-system run, including a failed rerun, despite existing transient retry. | **UNFINISHED, PRIORITY DEFECT.** Verify exact pinned Gateway ancestry and reproduce; improve the *existing* atomic-replacement path; require regression and composed Windows rerun. Do not assume a passing unrelated CI lane closes it. |
| [Dashboard canonical tracker](https://github.com/aiverse-filmmakers/AI-Verse-Dashboard/blob/main/docs/MISSION-CONTROL-EXECUTION-TRACKER-2026-09-15.md) | **11/100 points** in Dashboard's separate program. MC1.1–MC1.3 completed; MC1.4 real local proof marked **BLOCKED**, MC1.5 pending, MC2+ pending. | **DEPENDENCY, NOT DUPLICATE PLAN.** Reuse the existing `npm run mc1:local` scripts and pinned Mission Control. Verify explicit MC1.4 gate release; never silently mark it unblocked from the generic conditional dogfood verdict. |
| [Safe Update / Release Train](../../docs/SAFE-UPDATE-AND-RELEASE-TRAIN-IMPLEMENTATION-PLAN.md) and [repository governance](../../docs/MAINTAINER-START-HERE.md) | Older execution plan ends at 14% with an obsolete historical Agent PR #2 dependency; later governance/release implementations exist. Gateway component descriptor is a **candidate**, not automatic Distribution-admitted release. | **RECONCILE CURRENT EVIDENCE FIRST.** Do not resurrect obsolete release-train tasks or create a second updater/descriptor. Preserve newer accepted release and preservation contracts. |
| [Shared Skills Library](../../docs/SHARED-SKILLS-LIBRARY-IMPLEMENTATION-PLAN-2026-10-21.md) | Active separate OS/Skills/Brain/Distribution/member qualification work on 2026-10-23. | **AVOID COLLISION.** Do not rewrite related owner contracts or a frozen candidate. If Gateway needs a new seam, agree smallest additive owner-supported contract first. |
| Gateway historical branches `context-ladder/*`, `invisible-intelligence/*`, `purpose-*`, `migration-drop/*`, `repair/*` | Many historical branch heads exist but none is automatically a live implementation plan or safe missing code. Gateway had no open PR on 2026-10-23. | **RECONCILE, DO NOT BLINDLY CHERRY-PICK.** Compare candidate work to current main, PR merger history, acceptance and source fingerprints before labeling it missing or reusable. |

**Collision rule:** G0.1 must inspect historical work and the *live* Gateway issue/PR/branch evidence, then mark each observed proposed capability `ALREADY DONE`, `ACCEPTED BUT NEEDS CURRENT-GENERATION RECHECK`, `PARTIAL/UNFINISHED`, `REPLACED/OBSOLETE` or `UNPROVEN`. Each actual need gets exactly one `REUSE`, `EXTEND`, `CREATE`, `RETIRE` or `BLOCK/UNKNOWN` disposition. Do not re-open accepted phases, count a historical plan as new progress or implement a second owner.

## 3. Permanent laws and non-negotiables

1. Gateway owns **only** authenticated client ingress, local run/session/checkpoint/event/idempotency/audit state, bounded runtime/host routing and controls. Canonical domain owners retain their truths.
2. One verified principal, exact system and workspace scope per session/run; no client actor text, UI field or model response grants authority. No cross-system fallback or retained stale subscription.
3. OS authorization and current owner lifecycle/permissions, Brain Goal/version/activation epoch, action approvals and explicit strategic-direction handover remain enforced at the final effect boundary.
4. Never bypass owner APIs, create a shadow Goal/Memory/Skill/Bot/Automation/Connection/Token store, or treat copied Mission Control/Dashboard state as canonical.
5. Default local loopback only; bearer verification, secret redaction, remote TLS proxy + explicit authorization, origin/rate/pre-auth admission remain intact.
6. Preserve user-owned Gateway state through updates, uninstall and restart. In-flight interruption reports recovery required when transparent runtime resume is not proven; retries/idempotency cannot duplicate effects.
7. Missing, stale, unsupported or ambiguous owner capability is **unavailable/blocked**, never a fabricated success. Test current-generation owner contracts.
8. Preserve accepted Context Ladder, Purpose and Invisible Intelligence paths, including prompt-injection/untrusted-text separation, retrieval budgets, provenance, source freshness and bounded automatic organization.
9. No unnecessary new runtime adapters, services, stores, package formats, network listeners or framework replacements. Prefer correction, configuration and small adapter changes.
10. Owner-native tests do not establish whole-product release. Use exact owner refs, composed Distribution qualification, source-governance synchronization and immutable release evidence. A new candidate cannot rewrite old accepted release history.
11. Work one bounded owner slice at a time; inspect current source, open PRs and dependent plan work before every implementation; no force push or sibling overwrite.
12. Adaptive tasks may change based on evidence; protected outcome, requirements, ownership, security, denominator and phase sequencing require a documented plan amendment.

## 4. Requirements and observable verification

| ID | Success and important failure | Owning slice | Proof |
| --- | --- | --- | --- |
| GW-R01 | Current user can chat via documented authenticated Gateway; invalid token, wrong scope or disabled Gateway fails closed. | G1.2, G2.1 | Real HTTP + streaming contract, wrong-token/ID/scope regression |
| GW-R02 | Gateway creates and resumes the correct session/run; events, controls and idempotent retries retain authenticated scope. No stale cross-system/workspace events. | G2.1, G2.2 | Original API caller tests and two-system A/B/A composed proof |
| GW-R03 | Tool calls and user approvals cross OS host boundary and owner policy; forged model/user-provided authority does not create an effect. | G1.2, G3.1 | OS owner-backed positive and negative tests; no direct owner store |
| GW-R04 | Brain Goal-bound continuation is available only with a proven current Goal owner contract, otherwise explicitly blocked with diagnostic. | G1.2 | Exact owner adapter and goal-epoch change/owner-unavailable tests |
| GW-R05 | Windows atomic run replacement remains durable under concurrent two-system calls and injected transient contention; no silent corrupted state. | G1.1, G3.1 | Gateway issue #60 regression + Distribution Windows composed acceptance |
| GW-R06 | Restart, interrupted checkpoint, stale lifecycle/config, changed idempotency payload and crash/replay have safe, truthful outcomes. | G3.1 | Cold restart/recovery/operation replay integration tests |
| GW-R07 | Canonical Purpose/Memory/Skills/Data/Bots/Automations/Token/Connections information flows only through admitted owner contracts; unsupported owner path visibly unavailable. | G0.2, G2.2 | Current-generation owner seam matrix; affected composed gates |
| GW-R08 | Dashboard/Mission Control can consume typed Gateway capabilities and see a real task outcome without taking Gateway run authority. | G2.1, G4.1 | Existing MC1 proof reused, incremental contract checks |
| GW-R09 | Auth, origin, remote exposure, rate/CPU admission, budgets and secret redaction remain effective under adversarial input. | G3.2 | Native negative cases, source audit, existing repair regressions |
| GW-R10 | Exact revision is owner-accepted and (only if the separate Distribution gate admits it) packaged with reproducible release/preservation proof. | G4.2 | Descriptor revision/native CI, composed acceptance, Registry/State scoped refresh and release handoff |

**Performance/resources:** Benchmark representative session/run creation, event replay, checkpoint writes and two-system concurrent operations *before* choosing any new optimization. Do not invent throughput promises. A measured regression or observed bottleneck may justify an upgrade only with repeatable baseline, failure injection and no safety erosion.

## 5. Current call path and design decision

Documented starting path:

`Dashboard / Open WebUI / client`
→ bearer + Origin/rate/body/session admission at canonical Gateway
→ Gateway session/run idempotency and bounded checkpoint
→ OS host discovery/current context/permission and owner-backed reads
→ selected permitted runtime adapter
→ OS `authorize_action` / `request_action`, explicit approval when necessary
→ canonical owner effect receipt
→ Gateway events/checkpoint/result and optional Brain Goal evaluation
→ client event stream and recoverable control.

**Reuse:** `src/server.mjs`, `src/run-engine.mjs`, `src/store.mjs`, `src/host-adapter.mjs`, `src/runtime.mjs`, `src/goal-owner.mjs`, context/fold/provenance modules, existing native CI and fixtures, Dashboard `mc1:*` scripts.

**Extend only with evidence:** existing atomic state file replacement, current adapter capability discovery, current-run event/approval contract, typed consumer fixtures, restart/status diagnostics. Prefer small tests/contracts to a new framework.

**Create only if unavoidable:** a genuinely missing small compatibility adapter/operation surface with exact owner, schema and test; first prove existing behavior cannot satisfy the requirement.

**Retire only with proof:** obsolete duplicated path if current callers are migrated and recovery compatibility passes; no speculative pruning of accepted features.

**Blocked:** any proposed owner contract change affecting Brain/OS, unsafe remote model, Dashboard MC1.4 without explicit release, or cross-release migration without Distribution authority.

## 6. Risk and recovery decisions

| Area | Fixed decision |
| --- | --- |
| Security and permissions | Authenticated principal on entry; OS/owner final permission checks; never trust user/model authority hints. Replay/forgery tests stay mandatory. |
| Isolation/privacy | Exact system/workspace/session binding on ingress, events, runtime context, checkpoint and resumption. Two-system A/B/A tests; fail closed on mismatched identity. |
| Persistence/concurrency | Preserve durable Gateway-owned raw runs and state; atomic writes, platform contention/retry tests, corruption recovery and explicit idempotency; do not introduce a second DB. |
| Owner integration and prompt injection | Owner-proven source/current versions; untrusted retrieved text cannot alter tool authority or persistent state; unavailable owners are not hallucinated. |
| Compatibility and platform | Node >=20 for Gateway source unless governed release changes it. Verify Linux/macOS/Windows and actual Distribution pinned revision; Dashboard's Node >=22 is not automatically Gateway's requirement. |
| Remote exposure/secrets | Local-only by default. Do not auto-enable public listener. Recheck TLS proxy, Origin, bearer, rate limiting and sanitized logs. |
| User experience | Clear actionable errors/recovery and one simple default chat path. Dashboard owns presentation, never canonical run state. |
| Release/update | Preserve state, old frozen releases and candidate identities. No release or safe migration inferred from green owner tests. |

## 7. Dependency-safe implementation phases and fixed slices

**Progress unit:** ten **fixed outcome slices**, not a count of all old work or speculative tasks. Detailed tasks are derived only when a slice begins. Every slice records exact starting Git refs, task count, owner PR/merged SHA, tests, blockers, resulting acceptance and next pointer.

### Phase G0 — Reconciliation and contract destination (2 slices)

#### G0.1 — Resume-ledger and active-gap verification

#### G0.1 bounded task execution ledger (opened 2026-10-23)

Task progress for this slice: **3/5** after the verified API/Goal-owner trace. Task 4 is separately authorized and must be recorded before its completion. The fixed slice remains **IN PROGRESS**; overall **0/10 completed slices (0%)**. The task order below is gated by the owner's explicit **`next`** between tasks.

1. **COMPLETE (2026-10-23):** Refresh live exact Gateway, System, Distribution, Dashboard, OS and Brain main refs, open PRs, candidate descriptors, issue #60, governance observation and MC1.4 gate. Evidence recorded below.
2. **COMPLETE (2026-10-23):** Compared earlier Gateway plans, 60 closed PRs, 63 retained branch names, current source and tests, key stale branches and current CI. Distinguished merged, superseded, rejected, separately owned and truly unresolved work; evidence and classification below.
3. **COMPLETE (2026-10-23):** Traced real canonical Gateway endpoints, existing Dashboard /rpc and experimental runtime adapters, MC1 preflight/proof, and current Brain Goal CLI versus required Gateway Goal-owner subprocess contract; verified-vs-missing mapping below.
4. **IN PROGRESS (explicitly authorized together with Task 3):** Publish categorized no-duplication gap/collision ledger with source links.
5. **WAITING:** Review gaps and derive the smallest bounded G0.2 task list. Do not automatically advance into G0.2 without the owner's `next`.

##### Task 1: live source-of-truth checkpoint

| Source | Live observation (all checked 2026-10-23) | Exact evidence |
| --- | --- | --- |
| Gateway main | `95cc8319c1dc95b05da0ebb451d70469170ca3f8`; **0 open PRs**; main CI and Release Descriptor workflow success on the exact main ref. | [Main commit](https://github.com/aiverse-filmmakers/AI-Verse-Gateway/commit/95cc8319c1dc95b05da0ebb451d70469170ca3f8); [CI 38383650023](https://github.com/aiverse-filmmakers/AI-Verse-Gateway/actions/runs/38383650023); [Descriptor gate 38383650087](https://github.com/aiverse-filmmakers/AI-Verse-Gateway/actions/runs/38383650087) |
| Gateway descriptor | `0.1.0-beta.1`, **candidate** at exact source ref `1772b75e2add73a524715f746e87b3a6b5561bf6`; exact candidate CI `37876089214` passed. Descriptor's `supported_platforms` is `linux` even though separate native tests use multiple platforms. It is release metadata, not a live deployed-health or whole-product release claim. | [Descriptor](https://github.com/aiverse-filmmakers/AI-Verse-Gateway/blob/main/release/component-release.json); [Candidate CI](https://github.com/aiverse-filmmakers/AI-Verse-Gateway/actions/runs/37876089214) |
| Gateway open defect | [#60](https://github.com/aiverse-filmmakers/AI-Verse-Gateway/issues/60) **OPEN**. Windows concurrent two-system Gateway run hit repeated `EPERM` during atomic rename, producing a failed run / HTTP 409. Issue states existing transient retries were insufficient for the tested pinned Agent path. Do not mark fixed from unrelated green native CI. | [Issue #60](https://github.com/aiverse-filmmakers/AI-Verse-Gateway/issues/60); referenced Distribution composed run `38062934358` |
| Dashboard main and descriptor | Main `ec5d40aea7fa3111357c086660a2630cef20f51a`, **0 open PRs**, Dashboard main CI success `38384230668`; descriptor `0.1.0-alpha.0` candidate at `bd26986e202d4b911d0c5f64659db71363bfccfa`. | [Dashboard main](https://github.com/aiverse-filmmakers/AI-Verse-Dashboard/commit/ec5d40aea7fa3111357c086660a2630cef20f51a); [CI](https://github.com/aiverse-filmmakers/AI-Verse-Dashboard/actions/runs/38384230668); [Descriptor](https://github.com/aiverse-filmmakers/AI-Verse-Dashboard/blob/main/release/component-release.json) |
| Dashboard integration handoff | [Canonical tracker](https://github.com/aiverse-filmmakers/AI-Verse-Dashboard/blob/main/docs/MISSION-CONTROL-EXECUTION-TRACKER-2026-09-15.md) remains **11/100**; MC1.1–MC1.3 accepted; MC1.4 real local Mission Control-to-Gateway proof **BLOCKED** in that owner tracker, MC1.5 **PENDING**. The separate [Oct 5 controlled dogfood decision](../../docs/public-beta-audit/repairs/FINAL-INDEPENDENT-RECHECK-2026-10-05.md) covers synthetic-data supervised Agent testing but is not documented as an explicit Dashboard MC1.4 tracker unblocking. | [Dashboard execution tracker](https://github.com/aiverse-filmmakers/AI-Verse-Dashboard/blob/main/docs/MISSION-CONTROL-EXECUTION-TRACKER-2026-09-15.md) |
| Distribution main | `66e0ac2c5c631d450cf0708fec208b30fb784402`, native Distribution CI success; **one open PR #75** from `e486c97efdac005c28427d9abf8f71912d4a4700` about member Shared Skills lifecycle. Do not edit its branch, freeze or claim it merged. | [Main commit](https://github.com/aiverse-filmmakers/ai-verse-distribution/commit/66e0ac2c5c631d450cf0708fec208b30fb784402); [PR #75](https://github.com/aiverse-filmmakers/ai-verse-distribution/pull/75); [CI](https://github.com/aiverse-filmmakers/ai-verse-distribution/actions/runs/39554078673) |
| Current owner dependencies | OS main `50f9f678eb847dc447560020ecdb74b9ecc7ea20`; Brain main `6ad408e38b6b876cc8049f207fcba1e86ffd6554`. Both moved on October 23 in Shared Skills work and have no open PR at checkpoint. Do not assume the new refs were already admitted to every Agent composition. | [OS main](https://github.com/aiverse-filmmakers/AI-Verse-OS/commit/50f9f678eb847dc447560020ecdb74b9ecc7ea20); [Brain main](https://github.com/aiverse-filmmakers/AI-Verse-Brain/commit/6ad408e38b6b876cc8049f207fcba1e86ffd6554) |
| System main and governance | System main at task start `9f68f77f3d40eb9decfaef430d8c710ed0265504` (plan merged through PR #259), **0 open PRs** at start. The last published 14/14 Registry-derived full watchdog scan at `2026-10-23T08:33:22Z` was `WATCHDOG-CURRENT`. Its snapshot marks **current Gateway owner acceptance `unverified` and Distribution pin `unpinned`** in that snapshot, distinct from historical immutable Agent acceptance records. System has advanced after the watchdog observation, so it is a historical persisted evidence snapshot, not a new current-ref refresh/publication by this task. | [System plan merge](https://github.com/aiverse-filmmakers/AI-Verse-System/commit/9f68f77f3d40eb9decfaef430d8c710ed0265504); [Repository State](https://github.com/aiverse-filmmakers/AI-Verse-System/blob/main/governance/repository-state.json); [Watchdog](https://github.com/aiverse-filmmakers/AI-Verse-System/actions/runs/39925331838) |

**Task 1 outcome:** Exact current owner refs, relevant PR collision, descriptors, unresolved Windows issue and still-blocked Dashboard MC1.4 are recorded. This is **read-only discovery plus a System planning update**, not implementation code, a new owner acceptance, a fresh formal Registry/State publication, a Distribution promotion or a release. Next permitted task, after an explicit `next`: **G0.1 Task 2**.


##### Task 3: exact API, caller and Brain owner seam (2026-10-23)

**Source refs:** Gateway main `95cc8319c1dc95b05da0ebb451d70469170ca3f8`; Dashboard main `ec5d40aea7fa3111357c086660a2630cef20f51a`; Brain main `6ad408e38b6b876cc8049f207fcba1e86ffd6554`; OS main `50f9f678eb847dc447560020ecdb74b9ecc7ea20`. No relevant new PRs were open. This is source/contract verification, **not live local Gateway execution**.

| Layer/caller | Implemented now, with exact evidence | Missing, unproven or separately owned |
| --- | --- | --- |
| **Canonical Gateway client edge** | [`AI-Verse-Gateway/src/server.mjs`](https://github.com/aiverse-filmmakers/AI-Verse-Gateway/blob/main/src/server.mjs) implements `GET /health`, authenticated `GET /status` and `GET /v1/models`, `POST /v1/chat/completions` (nonstream and SSE), `POST /v1/runs`, `GET /v1/runs/:id`, `GET /v1/runs/:id/events` and diagnostics, and authenticated `POST` cancel/pause/resume/approval. `GET /health` reports lifecycle and is allowed before bearer authentication; other routes apply bearer/rate admission. Model `aiverse` is exposed. | This is a working code path with native tests, **not** evidence that Dashboard's current UI invokes it or that real Mission Control succeeded. API/consumer mapping belongs to Dashboard MC2. |
| **Gateway scope and safety** | `createRun` binds current configured `system_id`, authenticated principal and explicit/default workspace; rejects a mismatched existing session binding. [`src/run-engine.mjs`](https://github.com/aiverse-filmmakers/AI-Verse-Gateway/blob/main/src/run-engine.mjs) delegates actions to OS host boundary and persists run checkpoints. [`test/loop-contracts.test.mjs`](https://github.com/aiverse-filmmakers/AI-Verse-Gateway/blob/main/test/loop-contracts.test.mjs) includes approval/Goal fixture tests. | One canonical Gateway instance is **configured to one system**; a Dashboard showing several systems must select the correct registered, separately authenticated Gateway per system. No automatic cross-system selection inside a single Gateway is established by current code. |
| **Current Dashboard local control gateway** | [`AI-Verse-Dashboard/apps/gateway/src/server.ts`](https://github.com/aiverse-filmmakers/AI-Verse-Dashboard/blob/main/apps/gateway/src/server.ts) is a different local HTTP/WS server (default port 3100) serving authenticated `POST /rpc` and `/ws`. [`packages/client/src/client.ts`](https://github.com/aiverse-filmmakers/AI-Verse-Dashboard/blob/main/packages/client/src/client.ts) sends typed scoped RPC requests, not canonical Gateway `/v1` calls. [`query-router.ts`](https://github.com/aiverse-filmmakers/AI-Verse-Dashboard/blob/main/apps/gateway/src/query-router.ts) serves registered system, workspace, Purpose projection and local session/read-model queries. It truthfully marks health/inbox unavailable when no owner. | **No shipping first-class Dashboard-to-canonical-Gateway client found** in these currently inspected source paths; Dashboard MC2.1–MC2.5 explicitly remain PENDING. The Dashboard `apps/gateway` name **must not** be mistaken for a second AI-Verse Gateway implementation or promoted as session/run authority. |
| **Dashboard legacy runtime** | [`packages/live/src/adapter.ts`](https://github.com/aiverse-filmmakers/AI-Verse-Dashboard/blob/main/packages/live/src/adapter.ts) includes an in-memory echo adapter; [`runtime-adapters.ts`](https://github.com/aiverse-filmmakers/AI-Verse-Dashboard/blob/main/packages/live/src/runtime-adapters.ts) has a bounded CLI JSONL adapter whose `send` spawns a command and consumes `{reply}`. [`test/live-chat.test.ts`](https://github.com/aiverse-filmmakers/AI-Verse-Dashboard/blob/main/test/live-chat.test.ts) uses `LocalEchoAdapter` for isolation fixtures. | Echo/CLI fixture sessions are **not proof** of canonical Gateway session/run integration. Replace/retire their product-authoritative interpretation only after Mission Control feature inventory and owner-backed migration in the **Dashboard** plan; preserve isolation regression coverage. |
| **Mission Control proving path** | [`docs/MC1-MISSION-CONTROL-AIVERSE-RUNTIME-PROOF.md`](https://github.com/aiverse-filmmakers/AI-Verse-Dashboard/blob/main/docs/MC1-MISSION-CONTROL-AIVERSE-RUNTIME-PROOF.md), [`scripts/mc1/lib.ts`](https://github.com/aiverse-filmmakers/AI-Verse-Dashboard/blob/main/scripts/mc1/lib.ts) and [`proof.ts`](https://github.com/aiverse-filmmakers/AI-Verse-Dashboard/blob/main/scripts/mc1/proof.ts) already build a disposable pinned stock Mission Control lab, preflight real Gateway health/status/model and configure `LOCAL_LLM_ENDPOINT=<Gateway>/v1`, `LOCAL_LLM_API_KEY` and `dispatchModel=local/aiverse`. Scripts avoid storing the bearer token. | [Dashboard MC1.4](https://github.com/aiverse-filmmakers/AI-Verse-Dashboard/blob/main/docs/MISSION-CONTROL-EXECUTION-TRACKER-2026-09-15.md) **BLOCKED** pending explicit audit/repair gate release. No accepted real local dispatch/response evidence; MC1.5 and MC2 subsequent. Do not execute a real token-bearing dogfood proof from this task or bypass the blocker. |
| **Gateway → Brain Goal owner** | [`Gateway/src/goal-owner.mjs`](https://github.com/aiverse-filmmakers/AI-Verse-Gateway/blob/main/src/goal-owner.mjs) expects configured JSON-subprocess protocol `ai-verse-goal-owner/1.0` with `goal.get` and `goal.evaluate`, request IDs and fail-closed errors. [`run-engine.mjs`](https://github.com/aiverse-filmmakers/AI-Verse-Gateway/blob/main/src/run-engine.mjs) derives `operator` or `workspace:<id>`, binds goal ID/version/activation epoch, then revalidates before autonomous continuation; the fixture test exercises a [fake goal owner](https://github.com/aiverse-filmmakers/AI-Verse-Gateway/blob/main/fixtures/fake-goal-owner.mjs). | A fake adapter passing tests **does not prove** a live current Brain adapter. If no `goal_owner_config`, Gateway emits `GOAL_OWNER_UNAVAILABLE`; status `goal_owner_configured` is only a config flag, not an end-to-end readiness guarantee. |
| **Current Brain owner capability** | [`Brain/engine/aiverse_brain/goal.py`](https://github.com/aiverse-filmmakers/AI-Verse-Brain/blob/main/engine/aiverse_brain/goal.py) has Brain-owned `GoalService.get`, `evaluate`, canonical stored Goal versions and evidence-gated verdicts. [`cli.py`](https://github.com/aiverse-filmmakers/AI-Verse-Brain/blob/main/engine/aiverse_brain/cli.py) exposes `ai-verse-brain goal ... show/status/evaluate/continuation --json`, with version/scope validation. The exact current Git tree (149 files, nontruncated) contains no file advertising a production `ai-verse-goal-owner/1.0` bridge implementation; [`docs/ADAPTERS.md`](https://github.com/aiverse-filmmakers/AI-Verse-Brain/blob/main/docs/ADAPTERS.md) describes a **different** `ai-verse-brain-bridge/1.0` reasoning/host protocol. | **PARTIAL/BLOCKED OWNER SEAM:** owner Goal semantics and CLI exist; a production adapter converting Gateway's `goal.get` / `goal.evaluate` envelope into owner-approved Brain Goal calls, with exact scope/version/evidence mapping, was **not found in current Brain or Gateway tree**. Another external installation could supply it, but its existence is **not verified**, so the live capability cannot be claimed ready. The Brain owner must approve its public transport. Do not implement new Goal store or covertly route via Dashboard. |

**Task 3 decision:** Canonical Gateway protocol is real and reusable. The missing Dashboard product adapter is **owned by Dashboard MC2**, with MC1.4 real proof still blocked. Brain Goal capability is present, but the Gateway's specific Goal transport remains **unproven at current Brain main**; verify/reuse owner-approved bridge/CLI before creating *minimal glue*. Non-Goal normal chat does not require a Brain Goal adapter. Keep canonical run ownership and user-state preservation with Gateway.

**Task 3 acceptance:** Trigger → auth → Gateway session/run → OS host/model runtime → owner effect/Brain verdict → Gateway event/result → Dashboard/Mission Control caller is documented with real source files, differing protocols named and unavailable semantics distinguished. No code, file/release pin, credential or state mutation outside this System planning record.

##### Task 2: historical work versus shipped Gateway source (2026-10-23)

**Bounded scope and interpretation.** Gateway `main` remains `95cc8319c1dc95b05da0ebb451d70469170ca3f8`, with **zero open PRs** and exact-main [CI success](https://github.com/aiverse-filmmakers/AI-Verse-Gateway/actions/runs/38383650023). GitHub shows **60 closed Gateway PRs**: **59 merged, one closed without merge** (PR #61), and **63 retained branch names**. Branch existence or divergence alone does not imply unfinished accepted work; compare accepted PR/owner source and tests. This task is **historical/source reconciliation**, not the later detailed API/Goal-owner seam audit (Task 3).

| Earlier stream or branch | Status and live code evidence | Safe continuation (not new Gateway implementation) |
| --- | --- | --- |
| Initial Gateway edge and runtime | **ALREADY IMPLEMENTED / REUSE.** Current [README](https://github.com/aiverse-filmmakers/AI-Verse-Gateway/blob/main/README.md), [Architecture](https://github.com/aiverse-filmmakers/AI-Verse-Gateway/blob/main/docs/ARCHITECTURE.md), [Protocol](https://github.com/aiverse-filmmakers/AI-Verse-Gateway/blob/main/docs/PROTOCOL.md) and [package test manifest](https://github.com/aiverse-filmmakers/AI-Verse-Gateway/blob/main/package.json) confirm authenticated local chat/run/SSE, host/runtime adapters, run controls, durable sessions/events and restart behavior. Current source includes `src/server.mjs`, `run-engine.mjs`, `host-adapter.mjs`, `store.mjs`, `auth.mjs`, `goal-owner.mjs`. | Do not rebuild the Gateway, use a new database, or create a second API gateway. The downstream protocol correctness remains to be **verified in Task 3**, not assumed missing. |
| [Context Ladder + Lossless Memory](../../docs/CONTEXT-LADDER-AND-LOSSLESS-MEMORY-IMPLEMENTATION-PLAN.md) | **ACCEPTED HISTORICAL COMPLETION / REUSE.** 25/25 slices complete; Context Ladder Gateway [PR #31](https://github.com/aiverse-filmmakers/AI-Verse-Gateway/pull/31) merged; current source includes `fold-store/engine/archive`, `progressive-context`, `context-governor`, deep context tests and benchmarks. Historical `context-ladder/j2-integrated-acceptance` at `63f82e2...` compares **diverged: +3/-132** against current main, while replacement `j2-integrated-acceptance-v2` at `a08056e...` is **ancestor of current main** (behind 117, ahead 0). F1 branch catalogs and I1 cross-owner orientation map were evaluated/rejected, not incomplete feature requests. | Keep accepted folding, source-exact retrieval, pressure governor, benchmark and isolation behavior; do **not** cherry-pick divergent J2 v1 or resurrect F1/I1. Only fix a measured current-generation regression. |
| [Invisible Intelligence](../../docs/INVISIBLE-INTELLIGENCE-AND-GRANDMA-UX-IMPLEMENTATION-PLAN.md) | **ACCEPTED HISTORICAL COMPLETION / REUSE.** 24/24 slices complete. Gateway [PRs #2–15](https://github.com/aiverse-filmmakers/AI-Verse-Gateway/pulls?q=is%3Apr+is%3Aclosed) built question minimization, workspace routing, Memory capture, Skills learning/later use, Data routing, bounded Workers, permanent Bot/Automation consent, post-run organization and user-friendly outcomes. Current [loop-contracts tests](https://github.com/aiverse-filmmakers/AI-Verse-Gateway/blob/main/test/loop-contracts.test.mjs) still contain matching scenario tests including negative forged-authority cases. | Do not create new organization loop, permission service, domain database, Worker scheduler or recurring-automation mechanism. Re-test changed code against these regressions. |
| [Purpose Context](../../docs/PURPOSE-CONTEXT-IMPLEMENTATION-PLAN.md) and [closure](../../docs/PURPOSE-CONTEXT-FINAL-COMPLETION.md) | **ACCEPTED HISTORICAL COMPLETION / REUSE.** Purpose v1 admitted for Core and Gateway PRs #38–59 merged through [PR #59](https://github.com/aiverse-filmmakers/AI-Verse-Gateway/pull/59). Current Gateway `src/purpose-*.mjs` and ~20 dedicated `test/purpose-*.test.mjs` files confirm relevance, projection/receipt, confirmation, mutation-boundary, post-write and handover code present. | Do not create Gateway Purpose truth or reopen admitted Purpose v1. Future optional extras are not Gateway completion requirements. |
| Repair WSA-006/007/008/045/050/058 | **REPAIRED / REUSE WITH NEGATIVE TESTS.** Historical [repair tracker](../../docs/public-beta-audit/repairs/REPAIR-EXECUTION-TRACKER-2026-09-17.md) closes all **63/63** audit findings. Gateway PRs #32–37 merged, covering purge containment, live lifecycle, state linearizability, exact source freshness, pre-auth CPU and idempotency scaling. Current `test/lifecycle-containment.test.mjs`, `live-lifecycle-authority.test.mjs`, `state-linearizability.test.mjs`, `security-and-recovery.test.mjs` and `src/idempotency-store.mjs` exist. The older `repair/wsa-2026-058-gateway-idempotency-index` branch compares **diverged: +2/-105** with current main, while later revised [PR #37](https://github.com/aiverse-filmmakers/AI-Verse-Gateway/pull/37) was merged and current source has a canonical per-record idempotency store. | Keep proven repaired state and latest implementation. **Do not cherry-pick old idempotency-index branch**, invent a second index or re-run the entire repaired audit program without new evidence. A diverged pre-merge branch SHA may remain so after merge; owner code and accepted PR history decide truth. |
| Earlier Windows atomic fix ([PR #17](https://github.com/aiverse-filmmakers/AI-Verse-Gateway/pull/17)) and later [issue #60](https://github.com/aiverse-filmmakers/AI-Verse-Gateway/issues/60) | **PARTIAL, ONE VERIFIED OPEN BUG / EXTEND EXISTING.** Current [`src/util.mjs`](https://github.com/aiverse-filmmakers/AI-Verse-Gateway/blob/main/src/util.mjs) serializes per-process file writes and retries transient `EPERM`, `EACCES`, `EBUSY` rename errors up to seven retries. Existing [security/recovery tests](https://github.com/aiverse-filmmakers/AI-Verse-Gateway/blob/main/test/security-and-recovery.test.mjs) assert same-file atomic serialization but do not prove forced repeated Windows rename contention. Issue #60 documents **two failed composed Windows two-system runs**, while Linux/macOS passed. Earlier `context-ladder/e1-windows-atomic-state` head is now **strictly behind current main** (ahead 0, behind 213), so the initial fix was retained but not sufficient for that composed case. | A real **existing-mechanism reliability upgrade** is justified, in future **G1.1** only: reproduce/inject contention and fix `atomicJson`/replacement using the minimal safe change; verify pinned Agent ancestry and Windows composed scenario. Do **not** rewrite persistence or claim green native CI fixed issue #60. |
| Unmerged/retained branches | **NOT ACTIVE / DO NOT RESTORE.** Gateway [PR #61](https://github.com/aiverse-filmmakers/AI-Verse-Gateway/pull/61) is closed *without merge* as a descriptor validation route. Its retained `propagation-43-t4-validation` branch currently points to the **same commit as main** (compare identical, ahead/behind 0/0), so it carries no current missing code. 63 historical branch names are not 63 unfinished tasks. | Ignore stale branch names unless Task 3 or 4 finds an exact source/test behavior missing from current main. Never blindly merge prior feature branches. |
| [Safe Update / Release Train historical plan](../../docs/SAFE-UPDATE-AND-RELEASE-TRAIN-IMPLEMENTATION-PLAN.md) | **SEPARATE PROGRAM WITH STALE HISTORICAL CHECKPOINT / OWNER DECISION REQUIRED BEFORE RESUMPTION.** The 2026-09-14 plan still says 5/36 complete, 14%, blocked by Agent PR #2, which was subsequently merged. Later distinct accepted programs are [Safe Infrastructure 18/18](../../docs/SAFE-INFRASTRUCTURE-UPGRADE-AND-RECOVERY-IMPLEMENTATION-PLAN.md) and [Repository Network Governance 20/20](../../docs/REPOSITORY-NETWORK-PROGRAM-CLOSEOUT-HANDOFF-2026-10-18.md). Those later completions **do not by themselves prove all 36 original release-train slices**, so do not declare the old plan complete, discard its remaining legitimate requirements, or implement a second update/release mechanism in Gateway. | Reconcile only the *relevant currently unproven release handoff* via Distribution/owner qualification in future G4.2. Any remaining general release-train backlog belongs to its own System/Distribution owner, not the Gateway code completion stream. |
| Dashboard Mission Control work | **SEPARATE OWNER / BLOCKED HANDOFF.** [Dashboard tracker](https://github.com/aiverse-filmmakers/AI-Verse-Dashboard/blob/main/docs/MISSION-CONTROL-EXECUTION-TRACKER-2026-09-15.md) remains 11/100 with MC1.4 blocked and MC2 later. Current Gateway code is not a reason to rebuild Dashboard or bypass the local-proof gate. | Keep Dashboard canonical roadmap. Task 3 next will *trace* the actual seam only. |
| Brain Goal-bound autonomous continuation | **CURRENT DOCUMENTED DEPENDENCY / TASK 3 MUST PROVE.** [Gateway README](https://github.com/aiverse-filmmakers/AI-Verse-Gateway/blob/main/README.md) says Goal-bound runs fail closed unless Brain exposes/configures owner adapter; current `src/goal-owner.mjs` implements `goal.get`/`goal.evaluate` client operations and [loop-contracts](https://github.com/aiverse-filmmakers/AI-Verse-Gateway/blob/main/test/loop-contracts.test.mjs) tests a fixture adapter, not automatically a deployed current Brain owner transport. | **BLOCK/UNKNOWN** for current real Brain runtime until Task 3 verifies its actual public seam. Never add Goal storage in Gateway to sidestep missing owner transport. |

**No-duplication decision:** The Gateway code is **substantial and present**, not a blank foundation. The audit found exactly one explicitly OPEN Gateway defect in GitHub (#60) and an integration/Goal-owner contract whose **real current support remains to be checked**. Historical main CI, completed project plans and numerous stale branch names are not evidence for new implementation tasks. Fix **only** verified regressions in existing Gateway mechanisms; all other needs require Task 3/4 evidence first. Current Gateway candidate descriptor and Distribution adoption remain separate from historical owner acceptances.

**Task 2 outcome:** Historic workstreams, merged PR lineage, superseded branches and current source/tests have been compared; no executable work was changed. Do **not** start Task 3 until user says `next`. Slice G0.1 stays **IN PROGRESS** at 2/5 tasks, and global remaining-work program remains 0/10 accepted slices.

- **Owner/scope:** System planning record and read-only Gateway/Distribution/Dashboard/OS/Brain state inspection; no production code mutation.
- **Start:** Gateway `main` `95cc8319c1dc95b05da0ebb451d70469170ca3f8`; System plan creation based on `a6697ed24a1d70962544795259427a2acc765021`. Recheck live refs at execution.
- **Dependencies:** This plan present; current sibling PR and CI status checked.
- **Outcome:** Matrix reconciling all previous accepted Gateway-relevant plans and branches with current source; exact holes, issue #60, owner dependencies, candidate-vs-released refs and stopped work. Label evidence before deciding to write code.
- **Acceptance:** Relevant old plans and open issues are inventoried; each actual gap has owner/category and verification path; no accepted implementation is called missing; exact next code slice is chosen from evidence.
- **First derived tasks:** (1) refresh live refs/PRs/issue; (2) compare old plans/branches and current implementation/CI; (3) map real Dashboard API and Goal-owner seam; (4) publish gap and collision ledger with evidence; (5) derive G0.2 tasks.
- **Evidence:** System plan update + linked owner/issue/CI refs. **Rollout/recovery:** read-only; no member effect.
- **Next:** G0.2.

#### G0.2 — Minimal accepted Gateway-to-UI/owner contract and backlog freeze

- **Owner/scope:** System plan + owner-authored Gateway contracts/fixtures only when demonstrably needed.
- **Dependencies:** G0.1 complete.
- **Outcome:** Version/identity/capability/status/readiness mappings established against currently supported Gateway, OS and Dashboard MC2. Avoid adding duplicate "Dashboard Gateway" runtime authority.
- **Acceptance:** Positive and negative caller flows mapped; implemented-vs-unavailable semantics explicit, including Goal adapter, owner lifecycle and remote boundaries; exact bounded task list for issue #60/next behavior; no unapproved sibling change.
- **Evidence:** Protocol/contract fixtures or documented existing tests, current owner version checks.
- **Next:** G1.1.

### Phase G1 — Close evidenced core defects and runtime compatibility (2 slices)

#### G1.1 — Windows durable run-state replacement / issue #60

- **Owner:** Gateway; Distribution provides composed verification only.
- **Dependencies:** G0.2, exact current Distribution pinned Gateway ancestry inspected.
- **Outcome:** Repeated transient Windows atomic-rename contention no longer causes a run failure or incorrect checkpoint; interruption never corrupts canonical state.
- **Acceptance:** Original issue reproduced or conclusively characterized; regression fails on former defect where practical; smallest upgrade to current file write/retry/backoff/lock strategy; tests cover repeated `EPERM`/appropriate `EACCES` and `EBUSY` handling, bounded failure and preservation, and concurrent isolated systems. Gateway exact-head CI and Distribution affected Windows two-system lane pass. If pinned-artifact change needed, Distribution handles it.
- **Recovery:** Retain old checkpoints/backup path; abort if owner/release migration unsafe.
- **Next:** G1.2.

#### G1.2 — Current runtime, host and Goal-owner capability correctness

- **Owner:** Gateway, with Brain/OS owner approvals only if their public surface must change.
- **Dependencies:** G1.1.
- **Outcome:** One usable authenticated runtime route for actual Chat; correct current OS scopes, permissions, Purpose/context, capability/Goal availability and runtime failure semantics.
- **Acceptance:** Normal streaming chat + bounded tool effect passes through current OS; Goal continuation passes only if Brain public Goal adapter is proven available, else clearly reports unsupported/blocked without a shadow store. Stale lifecycle or inaccessible owner fails closed. Existing Invisible Intelligence, Context Ladder and Purpose regression suites remain green.
- **Next:** G2.1.

### Phase G2 — Dashboard-consumable edge (2 slices)

#### G2.1 — Stable chat/run/events/approval consumer contract

- **Owner:** Gateway for protocol and behavior; Dashboard for typed UI client code in its own canonical program.
- **Dependencies:** G1.2; reconcile with Dashboard MC1/MC2 tracker, don't supersede it.
- **Outcome:** Authenticated client can use `/v1/models`, chat streaming, runs, event replay/follow and authorized cancel/pause/resume/approve with explicit capability/reason codes.
- **Acceptance:** Contract tests exercise real endpoints and erroneous token/method/scope/operation-id payloads. No unadvertised control is shown as available, no secret leaks, no hidden user actor permission. Dashboard may implement typed client as its own MC2 work, not as Gateway code.
- **Next:** G2.2.

#### G2.2 — Multi-system isolation and owner-backed handoffs

- **Owner:** Gateway for its session boundary; OS/other owners for their own contract; Dashboard for UI switching.
- **Dependencies:** G2.1.
- **Outcome:** Explicit selected system/workspace remains consistent through chat, events, restart and delegated owner action; no cross-system fallback, fake Health/Inbox/Task/Token data or owner bypass.
- **Acceptance:** A→B→A + wrong-system and wrong-workspace adversarial composed tests; real owner reads and unavailable-degraded behavior; no shadow system registry introduced in Gateway.
- **Next:** G3.1.

### Phase G3 — Reliable operation and adversarial guardrails (2 slices)

#### G3.1 — Restart, checkpoint/replay and operator recovery

- **Owner:** Gateway.
- **Dependencies:** G2.2.
- **Outcome:** Durable, predictable checkpoint/recovery under process crash, cancellation, approval wait, changed idempotency input and concurrent writes.
- **Acceptance:** Cold-start and partial-write scenarios; `paused_recovery_required` remains truthful; no provider-process transparent-resume claim without proof; high-scale replay has bounded work; no lost raw history. Reuse prior WSA closures and never reopen resolved architecture without a regression.
- **Next:** G3.2.

#### G3.2 — Security, resource and optional-remote admission

- **Owner:** Gateway + OS final policy boundary.
- **Dependencies:** G3.1.
- **Outcome:** Safe local default for daily usage, deterministic auth and budget policy, bounded CPU/rate/event consumers, redacted errors and explicit optional remote behavior.
- **Acceptance:** Bearer/Origin/localhost/non-loopback policy, forged metadata, oversized requests, pre-auth stress, SSE lifecycle, malformed events, tool budget/approval, secret hygiene and current owner permission regression green. Any public remote product launch remains separately gated and disabled by default.
- **Next:** G4.1.

### Phase G4 — Whole-product proof and governed delivery (2 slices)

#### G4.1 — Existing Mission Control → real Gateway synthetic dogfood acceptance

- **Owner:** Gateway and Dashboard, using Dashboard's already accepted MC1.1–MC1.3 lab and `npm run mc1:local` path.
- **Dependencies:** G3.2, explicit Dashboard MC1.4 release from its own audit/repair gate. The 2026-10-05 conditional synthetic Agent dogfood permission does **not by itself** override Dashboard's written MC1.4 BLOCKED flag.
- **Outcome:** Stock pinned Mission Control dispatches a disposable read-only task through a real authenticated Gateway/OS/runtime and receives its result; exact system/workspace proven.
- **Acceptance:** Sanitized proof, no persisted Gateway token, no Mission Control state becoming AI-Verse truth, lab removable without touching AI-Verse. User runs one hidden-token local script only when safety gate explicitly permits. If still blocked, do not count this slice complete; non-secret mock preflight/fixtures may continue.
- **Next:** G4.2.

#### G4.2 — Owner acceptance, Distribution qualification and final handoff

- **Owner:** Gateway owner evidence, Distribution release authority, System evidence/governance synchronization; Dashboard retains its own MC2–MC7 roadmap.
- **Dependencies:** G4.1 and exact compatibility/rollback/preservation gates.
- **Outcome:** Gateway-ready product candidate with reproducible clean-machine and composed Linux/macOS/Windows evidence, state preservation and accurate status.
- **Acceptance:** Exact owner-native CI and candidate descriptor revision; composed Agent/Dashboard-relevant journeys with current compatible OS/Brain/other owner refs; update/uninstall/restart/data preservation; explicit Release/Distribution evidence and scope-aware Registry/State refresh; no false claim that candidate=accepted/pinned/admitted; accepted limitations and next Dashboard handoff recorded.
- **Next:** Close this bounded Gateway plan; proceed with Dashboard's **existing** MC2–MC7 plan. Do not replace it.

## 8. Reviews, task discovery and completion report

- **At every slice start:** re-read this file, refresh only relevant current GitHub owner/sibling states, inspect exact current source/test behavior, derive and record minimal current-slice tasks with count, update `IN PROGRESS` and starting refs. No hard-coded complete task list for future slices.
- **During implementation:** one narrow owner branch/PR; prove a public failure or meaningful negative case, implement smallest safe fix, run focused and full relevant regression, inspect diff/adversarial paths and test exact head. No speculative new abstraction. Preserve concurrent owner work.
- **At every slice close:** merge tested owner work, verify merged-main CI and composed evidence as applicable, update this living System plan with PR/SHA/CI, blockers, counters and next slice. Separate `code merged`, `owner accepted`, `Distribution qualified` and `member released`.
- **Protected amendment:** any changed architecture, owner, scope, slice goal, acceptance, denominator or release behavior stops with `BLOCKED - PLAN AMENDMENT REQUIRED` and evidence-based proposal.
- **Progress:** G0 0/2; G1 0/2; G2 0/2; G3 0/2; G4 0/2; overall 0/10 slices (0%). Within G0.1, **Task 3/5 complete**, Task 4 explicitly authorized in same request and pending separate completion checkpoint. Previous accepted programs keep their recorded historical completions; this new counter is not a reset of them.
- **Current execution pointer:** **G0.1 Task 3 complete**; proceed only to the owner's simultaneously authorized **Task 4**, evidence-backed no-duplication gap ledger, then stop until `next` for Task 5. No coding until a real gap is proven.
