# AI-Verse local-first desktop: compose existing owners and prove the complete product

**Date:** 27 October 2026  
**Status:** C0 IN PROGRESS (source-only integration audit, 0/7 slices accepted). C1-C6 not started. No product code or release approved by this document.  
**Plan owner:** AI-Verse-System (cross-repository integration and acceptance only).  
**Code owners:** Dashboard for presentation/desktop host; Gateway for sessions/runs/transport; OS for workspace/permissions; Automations for durable scheduling and wake delivery; Brain for goals/ticks; Multiple Bots for workers/teams; Connections for external credentials and approvals; Token for usage/cost; Distribution for install/upgrade/recovery.  
**Planning depth:** EXTENDED, because composition spans privileged desktop access, persistent state, scheduling, provider secrets, permissions, platform lifecycle and recovery.  
**Rules:** [Adaptive Implementation Planning Skill](../../docs/ADAPTIVE-IMPLEMENTATION-PLANNING-SKILL.md), [Implementation Plan Template](../../docs/IMPLEMENTATION-PLAN-TEMPLATE.md), [Owner Product Intent](../../docs/OWNER-PRODUCT-INTENT.md), and existing [Dashboard execution tracker](https://github.com/aiverse-filmmakers/AI-Verse-Dashboard/blob/codex/dashboard-source-checkpoint/docs/MISSION-CONTROL-EXECUTION-TRACKER-2026-09-15.md).

## Product brief and fixed destination

The operator's 27 October direction is to **stop redesigning or rebuilding already-finished modules**, compose the actual AI-Verse system behind the existing Dashboard, deliver a Mac-usable application with real AI and owner-backed work, and test the resulting installed product rather than merely each isolated repository. Coding, review and disposable integration tests may take place through GitHub without the operator's Mac. Final private folders, real accounts, physical UI/hardware, and owner dogfood are locally verified on the Mac, with no requirement to keep a Codex conversation open.

**Desired first journey:** Open the existing Dashboard as a locally running app; choose the already-installed OS; see one authentic system/workspace identity, real connection and runtime status; send a chat message that Gateway executes through OS and a supported AI runtime; see streaming and stop/approval; return to the same conversation after restart; create or interact with a real workspace via its owner; view Bots/tasks/Automations when active; configure and observe an existing durable wake; stop the UI while a separately supervised scheduler can continue; reopen to see authoritative results; recover correctly from a crash; and repeat with a second isolated OS without leaking any state. Later specialist Filmmaking actions consume this foundation rather than blocking first owner use.

**NON-NEGOTIABLE NO-REBUILD RULE:** Reuse supported existing owner products and contracts. Do not create another Gateway, run/session store, OS root, memory system, Brain loop, skill library, workflow executor, credential vault, token ledger, automation scheduler, task/worker coordinator, installer or updater. Dashboard may own its UI/presentation metadata but must not become canonical domain truth. A *minimal adapter* is permitted only after caller-to-owner source inspection proves a missing seam and its owning repository is agreed. If the required feature is genuinely absent or unsafe, record a bounded BLOCK/UNKNOWN instead of pretending a completed component exists or inventing a substitute.

**Scope:** owner-first local desktop and shared browser UI, selected OS/workspace, canonical chat and persistence, member-safe execution boundaries, current owner projections/actions, Bots and durable scheduled wakes/heartbeat, existing provider routes, desktop launcher/supervision, cross-platform disposable composition tests, and manual Mac acceptance. **Not in scope:** redesigning the present canvas, a parallel Mission Control database, SaaS hosting, general multi-tenant auth, new creative providers, a new universal AI runtime, unattended paid calls, member-channel release, or a standalone cloud heartbeat.

A Github Pages design preview is static. An interactive local browser build may communicate with an authorized loopback backend, and a Mac desktop host can supervise that backend; the public preview can never carry private credentials or OS-root authority. CI can test real owner code in disposable installations but not the user's private files/accounts. A persistent heartbeat works only while its OS service/computer/server is running and allowed to execute, even if the Dashboard window is closed. Sleeping/offline Mac means no guaranteed local continuous activity.

## State of evidence at plan creation (reuse/extend/blocked)

| Existing artifact or owner | Verified checkpoint, not a new acceptance claim | Disposition |
| --- | --- | --- |
| Gateway | main@ceb8849ec062f0d3997ceb0207e42c25aedd20c6. Existing authenticated /health, /status, /v1/chat/completions, /v1/runs, per-run events, control endpoints, checkpoint/recovery. [Gateway readiness plan](GATEWAY-COMPLETION-AND-DASHBOARD-READINESS-2026-10-23.md): 10/10 candidate slices done, not member release. | REUSE. No new chat server, loop, SSE, durability model or Gateway store. |
| Dashboard | working review branch codex/dashboard-source-checkpoint@bac349113cc9cb1a67bdb5e4d57cb3da0d580d89, [PR #42](https://github.com/aiverse-filmmakers/AI-Verse-Dashboard/pull/42); the functional preview is still demo-only. Separate real Mission Control-to-Gateway local-model proof accepted in earlier MC1, but not wired into the live Personal preview. Tracker has **15/100 historical accepted points; MC2.1 pending**. | REUSE existing preview/shell, typed client/protocol and MC1 proof. EXTEND only the agreed canonical transport/host seams; do not restart the UI. |
| Dashboard plan authority | [Existing Dashboard living plan](https://github.com/aiverse-filmmakers/AI-Verse-Dashboard/blob/codex/dashboard-source-checkpoint/docs/CANONICAL-MISSION-CONTROL-ADOPTION-PLAN-2026-09-15.md) and PR #41 record Personal-first amendment, as yet unmerged. [MC2.1 typed contract](https://github.com/aiverse-filmmakers/AI-Verse-Dashboard/blob/codex/dashboard-source-checkpoint/docs/MC2.1-AIVERSE-GATEWAY-CLIENT-CONTRACT-2026-10-26.md) is a design draft. | PRESERVE historic acceptance. This plan coordinates composition and does not silently replace the 100-point tracker, PRD, protected gates or Mission Control disposition. Reconcile changes before changing their denominator or ordering. |
| OS / Core | AI-Verse-OS main@0dc744057199970a34a60c11dff192e407ad64ed. OS owns root structure, workspace scope, permissions and component composition. Current /learn feature is separate accepted scope. | REUSE OS host/owner APIs, never duplicate state in browser. |
| Distribution | ai-verse-distribution main@355ac5012697117f24dd351dce1be71d0ae4e839. Canonical installation, admitted release resolution, upgrades, doctor and safe preservation. Gateway candidate was qualified for a scoped disposable Agent composition, not automatically promoted. | REUSE exact admitted releases; only Distribution installs/updates. Never bootstrap over private data or resolve from floating source branches. |
| Automations | main@fda8b25b11b8419113a2625d09fd3da66b61064f. Existing durable cron/interval/event/webhook wake service, permissions, idempotency, unknown-effect recovery and read-only local projection. Its command is ai-verse-automations serve. | REUSE as the only time scheduler/heartbeat wake owner, plus existing Brain tick/Bot/Team/Gateway target contracts. Never implement a Dashboard timer as canonical execution. |
| Multiple Bots | main@b4ad4315e560db0f60615e7c5ea59cb13c86969b. Owner for Bots, Team Runs, Workers, delegation and execution approvals. | REUSE current supported owner read/actions only. |
| Connections | main@b6eedea9a1ab569581f56a9d123de3497464619d, merged guided-key repair. Local service/vault is complete for its accepted scope; [S2 authenticated host/OAuth plan](GUIDED-PROVIDER-CONNECTIONS-BACKEND-2026-10-27.md) is blocked until binding/eligibility decisions. | REUSE vault, supported checks, capability grants. No duplicate credential store or unapproved new provider transport. |
| Brain, Memory, Skills, Data, Token | Each retains canonical domain ownership and prior accepted gates, subject to current-generation composed qualification. Token stop-check closed without code changes. | Consume authoritative current APIs and failure states. No duplicate products or gratuitous redesign. |
| GitHub repository watchdog | System main@172f095afac0c6a2be770ab314c8251e1d5f25da includes a repository watchdog heartbeat commit. | Do not confuse a GitHub repository monitoring marker with a running OS/agent heartbeat. |

Every listed SHA is a planning snapshot. Before each slice, refresh the relevant live PR/branch/accepted release. **A green component build is not proof of full-product readiness.**

## Permanent laws

1. One domain, one canonical owner. Owner operations and state are always preferred over simulated Dashboard/legacy projections.
2. Keep real OS roots, private files, tokens, OAuth exchange/refresh, API keys and bearer credentials off GitHub Pages and out of ordinary browser storage, telemetry, PRs and logs. Trusted authenticated host and OS/owner scope checks bind all effects.
3. Every session, workspace, wake, approval and returned event is bound to the active system/workspace/principal and current scope epoch. B -> A switches must never replay B content or inherit its credentials/Memory. Late streams and callbacks are fenced.
4. No silent destructive install, migration, arbitrary subprocess, wake activation, paid generation or permission widening. Existing user state is always preserved, even if app registry/cache is reset.
5. A successful schedule registration is not proof that a wake executed or its effect succeeded. Keep distinct configured, running, paused, unknown, blocked, completed, missed/offline and owner-verified states where applicable. Never blindly retry an ambiguous external effect.
6. Browser, native, CI, local Mac, live model and member release evidence are different gates and must be reported separately.
7. Previously accepted slice histories, frozen refs, 100-point Dashboard baseline, owner PR evidence and disabled/unavailable states remain honest. A change of product ordering or gated direction requires a documented amendment rather than quiet counter adjustment.
8. Do not work in parallel against a moving Dashboard branch without reading current head and preserving other authors' commits; avoid unrelated UI styling changes.

## Requirements and observable checks

| ID | Correct journey, important failure and preserved behavior | Owner / fixed slice | Acceptance |
| --- | --- | --- | --- |
| CP01 | Existing UI calls canonical Gateway; stream, stop, pause/approval and continuation work. Wrong token/scope or missing Gateway fails closed. | Dashboard + Gateway / C1 | Real HTTP/SSE against disposable actual Gateway, status/identity mismatch and cancel/replay tests. |
| CP02 | User selects system/workspace; only owner-backed workspace creation and actions mutate state. UI reload does not invent duplicate owners. | Dashboard + OS / C2 | Create/read/restart/switch two disposable OS roots; diff owner state and reject forged cross-scope writes. |
| CP03 | Dashboard starts/attaches to the right local services, resolves ports and secrets through a trusted host, and exits/recovers cleanly. | Dashboard host + Distribution / C3 | CI launcher/process tests, native Mac build, no token/absolute root in renderer logs or public artifacts. |
| CP04 | Existing Automations wakes Brain, Bot/Team or supported Gateway target according to owner contract. UI closing is independent from supervised service; offline is honest. | Automations + Brain/Bots/Gateway + Dashboard host / C4 | Fake clock/short interval, cron/timezone, restart, duplicate, revoke, missed wake, unknown outcome, stop/restart and receipt checks. |
| CP05 | Real local AI is usable with admitted Gateway runtime; provider setup displays honest readiness and, where eligible, authorized connection state. | Gateway/runtime + Connections host / C5 | Approved local-model run; mocked credential failure/race/security tests; optional separately approved real provider test, no forced paid use. |
| CP06 | Bots, current work, approvals, Memory/Skills/Data/Token and status are displayed only from current owner truth. Unavailable optional owner is explicitly unavailable. | Dashboard + existing owners / C2/C4/C6 | Current-generation owner projection fixtures, missing-owner degradations and permission-negative cases. |
| CP07 | One native Mac app uses same UI as local browser and can reopen prior owner sessions/workspaces. Existing OS need not be reinstalled. | Dashboard host / C3/C6 | Disposable Mac runner packaging smoke plus physical owner Mac trial before real-install signoff. |
| CP08 | Install/update/recovery use Distribution's frozen admission and doctor, never one more installer. | Distribution + Dashboard host / C3/C6 | Clean disposable install; existing populated install unchanged after no-op/update/rollback; reject wrong/incomplete root. |
| CP09 | A -> B -> A never leaks runs, Memory, credentials, scheduled wakes or workspace events. | All trusted boundaries / C6 | Two isolated disposable systems, adversarial late events and unauthorized reads/writes; no cross-owner fallback. |
| CP10 | The user can see actual work and recover instead of debugging developer internals. | Dashboard / C1-C6 | End-to-end task walkthrough with meaningful error, connection status, progress, approval and restart recovery. |

Performance and resources: record startup, streamed-first-response latency, wake jitter, idle CPU/memory, failure recovery and local service overhead on a reproducible baseline. Do not invent thresholds before the measurements. Keep the UI quiet and focused on chat/current work. Accessibility and macOS keyboard/trackpad journeys are genuine interaction tests, not mere CSS/source assertions.

## Current flow and simplest design

Existing supported path:

User Dashboard -> authenticated trusted host / approved client adapter -> canonical Gateway session/run/SSE -> OS owner host/permission boundary -> admitted runtime, Brain/Memory/Skills/Data/Bots as authorized -> Gateway event/receipt -> Dashboard projection.

Existing durable wake path:

Approved event/interval/cron -> Automations service claim/idempotent invocation -> current OS permission boundary -> Brain tick or Multiple Bots/Gateway supported target -> acknowledgment/receipt -> read-only Dashboard projection.

**Approach:** complete the missing bindings in the *current* Dashboard implementation, using the [MC2.1 Gateway client contract](https://github.com/aiverse-filmmakers/AI-Verse-Dashboard/blob/codex/dashboard-source-checkpoint/docs/MC2.1-AIVERSE-GATEWAY-CLIENT-CONTRACT-2026-10-26.md) as the source-reviewed starting seam. Keep existing Dashboard preview layout instead of creating a rival app. Prefer existing host, protocol, client, owner adapters and Distribution launcher; the exact choice of native shell or process wrapper must be based on existing checked-in Dashboard implementation at C0, not a greenfield React/Tauri migration by default. A new library, process or store needs written evidence that supported existing facilities cannot meet the acceptance case, plus a safe rollback.

Provider status must distinguish configured, live-verified, authorized, approved and funded/usable if a meaningful check exists. No browser UI may decide owner approval. Read-only connected services do not imply broad mutation authority.

## Relevant risks and decisions

| Risk | Existing boundary and check |
| --- | --- |
| Browser or remote session calls private OS | Local host derives system/workspace/principal from trusted registration; strict origin, authentication and CSRF controls. No user-entered root, command or URL is accepted as authority. |
| Credential disclosure/provider billing | Reuse Connections/native secret owner; never place bearer tokens in renderer persistence; synthetic provider tests by default and explicit approval for live billed calls. |
| Missed wake / duplicate or unknown external action | Reuse Automations SQLite, idempotency, owner receipt and recovery. Distinguish service-offline state; unknown action needs operator reconciliation, not blind retry. |
| Dashboard UI closes but work continues | OS service/host owns lifecycle and supervision; UI does not own scheduler ticks. Closing the Mac lid, sleep, shutdown and power loss are separately classified. |
| Existing private install corruption | First use disposable Distribution installation; revalidate existing roots; never reinstall over operator state; protect upgrades with existing LKG/preservation rules. |
| Mixed revision and plugin incompatibility | Test exact admitted component set plus explicit candidate set separately; fail as unsupported rather than silently using moving main code. |
| Misleading readiness | Keep candidate/local dogfood/member release states distinct; zero real AI claims from deterministic mocks; no automatic promotion from CI alone. |
| Parallel edits to active Dashboard | Inspect PR #41/#42 and current head; coordinate additions via bounded PRs and existing tracker; do not force push or overwrite local Mac-only changes. |

## Seven dependency-safe acceptance slices

**Progress unit = 7 fixed outcome slices; at creation 0/7 (0%).** These are *composition/acceptance milestones*, not duplicate Gateway, OS or Dashboard feature points. Detailed tasks are discovered/refined at each slice start per the Adaptive Planning Skill. No implementation of C1-C6 begins before C0's collision and authority review.

### C0. Inventory the actual installed composition and reconcile Dashboard gates

**C0 execution ledger (derived 27 October 2026; source-only, no new owner source):**

- [x] C0.1 Refresh live heads, Dashboard PRs, System PR and accepted/disposable release baselines before tracing contracts.
- [ ] C0.2 Trace current Personal chat/demo, existing typed Dashboard /rpc and live adapters, canonical Gateway transport/auth/events, and identify the smallest existing caller seam.
- [ ] C0.3 Trace OS/workspace and Distribution installation identity, existing Automations/Brain/Bot wake and relevant Connections/Token contracts; record verified supported/unsupported cases and completion statuses, not speculative expansion.
- [ ] C0.4 Reconcile current Personal-first design amendment versus existing Mission Control MC2.1 gate and the original tracker, without quietly changing accepted 15/100 points or other accepted owner plans.
- [ ] C0.5 Publish exact-source handoff matrix and meaningful negative/whole-product test route; review C0 acceptance and next C1 entry, keeping any unresolved protected change blocked until its owner review.

**Starting revision inventory:** System main `172f095afac0c6a2be770ab314c8251e1d5f25da`, Dashboard review `bac349113cc9cb1a67bdb5e4d57cb3da0d580d89` (main `016da5fda319c94bda6704859acc5b12d23ad4ed`), Gateway `ceb8849ec062f0d3997ceb0207e42c25aedd20c6`, OS `0dc744057199970a34a60c11dff192e407ad64ed`, Automations `fda8b25b11b8419113a2625d09fd3da66b61064f`, Distribution `355ac5012697117f24dd351dce1be71d0ae4e839`, Connections `b6eedea9a1ab569581f56a9d123de3497464619d`, Multiple Bots `b4ad4315e560db0f60615e7c5ea59cb13c86969b`, Brain `32cae304861bb0c897a64dd0931bead516d22833`, Token `363dde3d87edaf8e7acd072c542775017f0b5dbf`. GitHub is a *source snapshot*, not evidence of the operator's installed Mac revisions.

- **Owner/scope:** System planning, Dashboard/Gateway/Distribution/Automations/Connections contract evidence only.
- **Dependencies:** Current PR/branches, admitted release catalog, existing MC1 proof and MC2.1 draft.
- **Fixed result:** One exact versioned owner/component acceptance matrix showing which already-built interfaces are directly consumable, which need a minimal adapter, and which are blocked. Decide the existing UI/build to extend; do not restart either preview or Mission Control UI.
- **Acceptance/evidence:** Inspect real caller -> scope/auth -> owner effect -> response/receipt for chat, workspace, Bots, automations, credential and native launch. Identify existing launchers and their supported OS platforms. Reconcile pending Dashboard Personal-first ordering with its 100-point tracker through existing amendment/review; no fake progress.
- **First derived task:** C0.1 refresh latest owner heads/accepted artifacts and trace the real Dashboard-to-Gateway path, including any branch modifications after this plan.
- **Next:** C1 only after owner/adapter map is reviewed. No writes to private OS.

### C1. One real Dashboard conversation through canonical Gateway

- **Owner/scope:** Existing Dashboard shell, host/client adapter, canonical Gateway. No new execution server.
- **Dependencies:** C0 and accepted typed MC2.1 contract/design gate.
- **Fixed result:** Primary and additional chats send/stream/abort/continue authentic scoped Gateway sessions instead of demo replies; connection/offline/approval/error states are truthful. Preserve previous working split, resize, selection, chat tools and preview behavior where still applicable.
- **Acceptance/evidence:** Actual disposable Gateway with admitted deterministic runtime for failure/stream/restart/control tests, plus explicitly approved local-model path for real-response proof. Verify header authentication, A/B isolation, late-event fencing, idempotent retries, unchanged session source of truth. An unimplemented attachment or app-action is clearly unavailable, not silently simulated as a production action.
- **Next:** C2. Roll back adapter without destroying Gateway state.

### C2. Canonical workspace and owner-backed work visibility

- **Owner/scope:** Existing Dashboard integration to OS/Brain/Memory/Skills/Data/Token/Multiple Bots supported read/actions.
- **Dependencies:** C1 authenticated scoped transport.
- **Fixed result:** Workspace switch/creation, conversation context, active work/Bot identities and relevant action/approval status reflect the existing owner; Canvas local demo data remains clearly distinct until owner action contracts are supported.
- **Acceptance/evidence:** Disposable existing/new workspace, switch, restart, denied writes, owner unavailable, stale projection, token/status truth; no duplicated canonical task or memory store. A real action is enabled only with a supported owner command, idempotency and current permission check.
- **Next:** C3.

### C3. Trusted Mac/local-browser launcher and service lifecycle

- **Owner/scope:** Existing Dashboard host/build, Gateway and Distribution integration; reuse checked-in technologies.
- **Dependencies:** C1/C2 proven owner scope and identity.
- **Fixed result:** A runnable local Dashboard with simple start/stop, existing-OS detection, secure per-system Gateway attach/start and diagnostics, usable in local browser and as an owner Mac application/build. A separate supported service may remain running after GUI closure.
- **Acceptance/evidence:** GitHub CI disposable Mac/Linux/Windows supported backend tests, macOS package artifact, two system registrations, root mismatch and port contention, OS state unchanged after UI close, crash and restart; manual Mac install/execution intentionally pending until the owner tests it. Reuse the canonical Distribution install/update path if installation is needed.
- **Next:** C4.

### C4. Actual heartbeat, scheduled wakes and Bots without another scheduler

- **Owner/scope:** Automations, Brain, Multiple Bots, Gateway (only for their supported downstream contracts); Dashboard for projection and authorized controls; trusted host for service lifecycle.
- **Dependencies:** C2 scope and C3 host supervision; owner target compatibility verified at C0.
- **Fixed result:** The owner can configure/observe an approved periodic review/heartbeat or scheduled task using existing Automations interval/cron, see current Brain/Bot/work state and the last wake receipt, and stop/pause/disable it through its owning control boundary. No UI-local countdown is called a canonical heartbeat. Background work can continue without open Dashboard only while the scheduler and underlying computer/server remain active.
- **Acceptance/evidence:** Exercise actual Automations service and owner target on disposable installs with time-travel or bounded short intervals; prove claim, run, pause, workspace revoke, crash, duplicate invocation, offline/missed wake and unknown external effect; no duplicate run, hidden approval or automatic retry. If Automations' current Gateway receive-side mapping lacks a versioned endpoint, mark that target blocked and use only an existing supported Brain/Bot target until a minimal owner-admitted adapter is proven.
- **Next:** C5.

### C5. Real AI/runtime and safe connection status in the composed product

- **Owner/scope:** Existing Gateway runtime adapter, Connections service and secure Dashboard host, Token read owner. Do not redo completed local key-verification work.
- **Dependencies:** C1 real conversation and C3 trusted host. Connections S2 remains a separately governed host/eligibility gate.
- **Fixed result:** One *supported, approved* local AI runtime is usable end-to-end; supported provider connection UX may be enabled only when its full authenticated host lifecycle exists. OAuth or paid models are not necessary to prove the already-accepted local model route.
- **Acceptance/evidence:** current supported local-model route replayed through the real Dashboard, failure and recovery tests; secrets redacted. For any provider claimed as connected, complete host auth/identity, vault/refresh/callback and race/security tests; separate real-account sign-in and billed provider test needs operator approval. If route eligibility remains blocked, show it accurately while local AI dogfood proceeds.
- **Next:** C6.

### C6. Whole-product acceptance and owner Mac handoff

- **Owner/scope:** Distribution and all installed canonical owners for composed tests; Dashboard for user journeys, launcher/artifact and diagnostics. Do not declare more capabilities than the selected release profile actually provides.
- **Dependencies:** C1-C5 relevant accepted outcomes and exact pinned candidate/admitted release sets. Unavailable optional owners need explicit degraded/disabled cases, not fake success.
- **Fixed result:** Single downloadable/reproducible local app build and one executable test path that spins up a disposable *real* OS composition including Gateway, Brain, Memory, Skills, Data, Bots, Automations, Connections, Token when admitted for the chosen profile. Tests execute a real call chain, not just mock one owner or assert source patterns. Actual Mac private-instance acceptance remains a separate owner gate.
- **Acceptance/evidence:** clean bootstrap/doctor, existing populated install non-destructive attach, chat->owner tool/action->receipts, workspace creation/switch, permitted denial, multi-agent delegation, durable automation wake, memory/skill/data projections, usage owner status, cancel/restart, credential-secret scan, two-OS A->B->A, update/LKG recovery and failures (offline Gateway/owner, corrupt or stale state, duplicate/missed wake, permission revoke). Provide precise artifact SHA, exact CI logs per platform and release channel, fail/skip map, small readable Mac launcher guide and manual test checklist.
- **Mac signoff:** owner tests actual folders, permitted local runtime/real provider account if chosen, physical GUI, background service behavior, sleep and reopening. Only after separately satisfied owner/Distribution gates may a private owner dogfood release be described as ready. Member release requires its own approval.
- **Next:** maintain the single existing Dashboard tracker and file owner-specific defects against demonstrated failures only.

## Execution/review and checkpoint

**Plan creation:** planning only; no app/runtime/Automation changes, no provider keys, no paid calls, no member release or system migrations. 0/7 slices accepted. This coordination plan does not award Dashboard MC points or reopen Gateway 10/10, Connections V1 2/2, Token beta.3 or other accepted owner closeouts.

**Reviews:** (1) product and architecture: distinguish owner product law from historical Mission Control order; (2) code/adversarial: minimal exact-source adapter diffs, failure tests and deletion/reuse test; (3) behavior/delivery: real disposable installed chain, native build, separate physical Mac evidence and release-preservation checks. Document blocked requirements without fabricating success.

**First action after review:** C0.1 check live branch heads, currently admitted releases and open PRs, then inventory reusable Dashboard-to-Gateway and Automations-to-owner seams. Only produce the bounded C0 task list after this fresh check. Stop if the existing current-generation acceptance already proves a proposed task. The first *implementation* target is the existing main chat sending and receiving a real Gateway run through one OS/workspace, not a new UI, a new backend or a synthetic heartbeat.

**Progress reporting:** completed/7 acceptance slices + tasks within the active slice; exact PR/commit and CI/native evidence; unresolved owner blockers; next slice. Distinguish candidate, local demo, real owner dogfood, Distribution-admitted artifact and released product in every summary.
