# Gateway Completion and Dashboard-Ready Delivery Plan

**Status:** READY TO START; no implementation slice claimed complete by this new plan
**Created:** 2026-10-23
**Plan owner:** `aiverse-filmmakers/AI-Verse-System`
**Canonical code owner:** `aiverse-filmmakers/AI-Verse-Gateway`
**Related owners:** AI-Verse-Dashboard (UI, client integration), AI-Verse-OS (scope/host/authorization), Brain (Goals), Memory/Data/Skills/Multiple Bots/Automations/Connections/Token (their canonical domains), ai-verse-distribution (composition, releases)
**Planning depth:** EXTENDED: persistent run state, authenticated permissions, cross-repo contracts, Windows durability and release gates
**Method:** [Adaptive Implementation Planning Skill](../../docs/ADAPTIVE-IMPLEMENTATION-PLANNING-SKILL.md) and [Implementation Plan Template](../../docs/IMPLEMENTATION-PLAN-TEMPLATE.md)
**Fixed destination:** Finish the *existing* canonical Gateway as a reliable, securely bounded, owner-backed, Dashboard-ready local Agent edge, with verified current-generation chat/runs/events/controls, restart behavior, composed integration and honest release qualification. Do not expand "finish" to speculative enterprise or every future owner feature.
**Checkpoint:** 0 / 10 new acceptance slices complete (0%). This is the remaining-work program, **not** an assertion that existing Gateway is 0% implemented.
**Next:** G0.1 — reconcile actual completed/unfinished Gateway workstreams and exact active owner/dependency refs, derive bounded tasks and capture a traceable gap ledger. No code change until G0.1 proves the gap and collision scope.

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
- **Progress:** G0 0/2; G1 0/2; G2 0/2; G3 0/2; G4 0/2; overall 0/10 (0%). Previous accepted programs keep their recorded historical completions; this new counter is not a reset of them.
- **First execution pointer:** **G0.1, task 1**: refresh Gateway `main`, issue #60, current release descriptor, System/Distribution relevant refs, Dashboard MC1.4 gate, then publish a precise continuation ledger. No coding until a real missing behavior is proven.
