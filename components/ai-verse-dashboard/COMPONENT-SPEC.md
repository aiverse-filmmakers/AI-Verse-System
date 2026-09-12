# AI-Verse Dashboard Component Specification

**Component:** AI-Verse Dashboard  
**Repository:** aiverse-filmmakers/AI-Verse-Dashboard  
**Reviewed default branch:** main  
**Reviewed revision:** c636acf019f76194c40a341bd7985906383f7106  
**Review date:** 2026-09-13  
**Repository-declared stage:** 0.1.0-alpha.0, Phase 2 in progress, next Phase 2 Task 6  
**Audit method:** docs/AUDIT-METHODOLOGY.md

## 1. Identity

AI-Verse Dashboard is Layer 5: the visual Control Room and controller surface for one or more AI-Verse OS installations.

Its intended product promise is:

- make system, workspace, agent, work, attention, health, automation, Brain and usage state visible;
- let an operator issue commands through the correct owning system;
- preserve strict systemId and workspaceId isolation;
- support browser, future native desktop and future remote/channel clients through one typed Gateway contract;
- remain deletable and rebuildable without losing canonical AI-Verse domain truth.

The decisive boundary is that Dashboard is an interface and projection layer, not another OS and not a domain database.

## 2. Executive verdict

### CURRENT

The repository contains a real TypeScript protocol, OS-root registry, read-only Markdown/SQLite adapters, localhost HTTP/WebSocket Gateway, typed query client, framework-free shell/layout models, read-model helpers, a process-local live SessionStore, a local echo adapter, one generic CLI JSONL runtime adapter and 13 test-backed build tasks.

The current code strongly enforces several isolation properties:

- explicit systemId and workspaceId on scoped protocol operations;
- raw-root rejection in protocol parameters;
- server-side root resolution;
- traversal and symlink escape rejection;
- read-only SQLite;
- per-system cache/session/subscription namespaces;
- loopback-only Gateway binding;
- fail-closed unknown-system behavior.

### INTENDED

The intended Dashboard is much larger:

- a real React/Vite application;
- a modular dockable desktop shell;
- floating/detached/HUD panels;
- a persistent Bot and Room experience;
- heterogeneous Chat;
- real live runtime control;
- automations and approvals;
- omnichannel ingress;
- Brain graph;
- token/cost/resource observability;
- Mac/Windows desktop packaging;
- all mutations routed through canonical owner APIs.

### GAP

The repository is not yet a user-operable Dashboard and is not complete for the current Phase 2 live-control milestone.

The major current-target blockers are:

1. no launchable browser application, DOM, React/Vite host, start command or executable bootstrap;
2. no supported UI/API/CLI flow to register and persist an OS connection;
3. all Gateway commands are still rejected by assertQueryOnly, including chat.send and chat.abort;
4. Phase 2 agent/run reads are backed by Dashboard's own process-local SessionStore rather than owner-declared runtime/system truth;
5. health, work and inbox projections currently invent semantics from filesystem conventions, including treating unavailable work as an empty list;
6. no actor authentication, per-command authorization or approval enforcement exists at the Gateway;
7. the generic CLI adapter advertises abort support but does not retain/kill an in-flight child process;
8. browser Origin validation rejects ordinary loopback origins that include a port, so a normal browser-hosted UI cannot currently use the HTTP/WS Gateway;
9. there is no repository CI and one test hardcodes a developer-local sibling OS path, so clean-checkout acceptance is not proven;
10. several correctness bugs remain in cache invalidation, global subscription keys, registry persistence/stability and presentation-state validation.

### LAW

Dashboard may own presentation/configuration state and disposable projections. It must not own canonical tasks, Bots, Rooms, Memory, Brain state, automations, approvals, usage truth, provider conversation continuation or runtime truth.

A UI convenience must never become a second owner.

## 3. Product philosophy

The repository consistently documents five core principles:

1. **Projection over duplication.** Read the owner, normalize for display, keep provenance.
2. **Command through ownership.** A user gesture is not permission to mutate a sibling store directly.
3. **Explicit scope.** Every OS-derived view or action is bound to a systemId and, where applicable, workspaceId.
4. **Disposable UI state.** Layout, selection, caches and view state can be rebuilt without domain loss.
5. **Host-independent panels.** Visual panels should be reusable across browser, desktop wrapper and future clients.

These principles are sound. Current implementation only partially reaches them.

## 4. Current architecture

Current executable shape:

    framework-free shell/layout models
                |
        DashboardClient
        HTTP query only
                |
      localhost Gateway
       /rpc + WebSocket
          /         \
 SystemRegistry      SessionStore
      |                  |
 read adapters       runtime adapters
      |
 workspace files / workspace-local SQLite
      |
 read-model projections

Important current boundaries:

- apps/web is not a web application. It exports TypeScript view/layout models only.
- packages/client is read-only HTTP RPC only. It has no command helper and no WebSocket/reconnect/resync implementation.
- apps/gateway exposes a server library but there is no product bootstrap that creates the registry, registers systems, wires adapters and starts the app.
- packages/live is a Phase 2 in-memory/runtime scaffold.
- command names exist in the protocol, but the current QueryRouter rejects every command before routing.

## 5. Ownership and source-of-truth map

| Responsibility | Correct owner | Current Dashboard behavior | Verdict |
|---|---|---|---|
| AI-Verse domain state | OS / owning component | read via files/SQLite conventions | PARTIAL, direct-storage coupling |
| Dashboard registered-system metadata | Dashboard | in-memory SystemRegistry | CURRENT but not persisted/stable |
| selected system/window | Dashboard presentation | in-memory SelectionStore | CURRENT, not integrated/persisted |
| layout/panel placement | Dashboard presentation | in-memory LayoutManager | CURRENT contract only |
| saved layouts | Dashboard presentation | savePreset returns an object only | PARTIAL, not actually persisted |
| projection cache | Dashboard | in-memory DisposableCache | CURRENT but defective/unused in Gateway |
| health meaning | owner-declared schema | Dashboard synthesizes manifest/context/layers | BOUNDARY VIOLATION |
| work/task truth | owner | missing source becomes empty WorkSummary | BOUNDARY VIOLATION |
| inbox/attention meaning | owner | inbox filenames become synthetic review/info items | BOUNDARY VIOLATION |
| Bot/agent truth | OS/runtime/Multiple-Bots owner | agent.list exposes SessionStore sessions as agents | BOUNDARY VIOLATION if retained |
| run truth | runtime/owner | recent SessionStore timeline entries | PHASE 2 SCAFFOLD, not final truth |
| provider chat continuation | provider/runtime owner | Dashboard SessionStore is current transcript source | PHASE 2 SCAFFOLD, must remain disposable |
| canonical writes | owning component through OS/host boundary | no Gateway write path | MISSING |
| approvals/permissions | owner/host policy | no actor/permission model | MISSING |

### Hidden canonical database conclusion

Dashboard is **not currently a hidden durable database**. No production source file creates a writable domain SQLite store or writes canonical Markdown.

However, two forms of hidden authority are already emerging:

1. **Semantic shadow truth:** workspace-sources.ts invents health, work and inbox meaning instead of consuming owner-declared schemas.
2. **Process-local operational truth:** SessionStore is the only current source for agent/session/run APIs and stores transcript/status state inside Dashboard.

Both are acceptable only as temporary scaffolding. Neither may become the production canonical owner.

## 6. Read path

### CURRENT read path

    panel/client
      -> protocol request
      -> Gateway QueryRouter
      -> systemId registry resolution
      -> workspace resolution
      -> direct Markdown/SQLite/filesystem read
      -> Dashboard read-model normalization
      -> response with some provenance

Strong points:

- physical realpath containment;
- no browser-supplied roots;
- read-only SQLite plus query_only;
- bounded Markdown/SQLite reads in the dedicated adapters;
- no cross-system fallback;
- per-system identifiers on protocol responses/events.

Weak points:

- several read models infer domain semantics from raw internal file conventions;
- workspace-sources reads fixed files directly rather than an owner projection contract;
- task absence is represented as an empty list instead of unavailable;
- inbox createdAt is regenerated on every read;
- manifest/layer health freshness is incorrectly tied to CURRENT.md modification time;
- source.preview calls the projection cache with NaN metadata, ignores the result, reads again and then caches;
- the client does not validate the response envelope/version/systemId with the protocol schema;
- the browser client has no event-driven invalidation/reconnect/resync path.

### INTENDED read path

    caller
      -> explicit system/workspace scope
      -> versioned owner projection API
      -> canonical/derived distinction
      -> bounded result
      -> provenance + source version + freshness
      -> Dashboard-only aggregation/presentation

The owner must define health/task/Bot/approval semantics. Dashboard may aggregate but must not manufacture them.

## 7. Write and control path

### CURRENT

There is no public Dashboard write path.

The protocol names 12 commands, but QueryRouter calls assertQueryOnly before routing. chat.send, chat.abort, task controls, cron controls, approval resolution, initiative activation and inbox resolution all fail with COMMAND_BLOCKED_READ_ONLY.

The generic CLI JSONL adapter can execute a configured process when called directly from code, but it is not wired to the Gateway command surface.

That direct adapter is not a substitute for the canonical write boundary.

### INTENDED

For every privileged effect:

    UI intent
      -> authenticated actor/session
      -> systemId/workspaceId
      -> command schema
      -> owner resolution
      -> current permission check
      -> approval when required
      -> durable idempotency
      -> canonical owner effect
      -> receipt/event
      -> UI projection refresh

Dashboard should never mutate a sibling database/file or treat a runtime adapter as authority to bypass this pipeline.

## 8. Information architecture and surface readiness

| Surface | CURRENT | INTENDED / GAP |
|---|---|---|
| Now / Control Room | NowModel exists | focus/work/attention must come from real owner state |
| Chat | typed timeline + SessionStore + adapters | real UI, provider continuity and command boundary missing |
| Work | model exists; actual source always empty | canonical task/work projection required |
| Runs / Timeline | SessionStore-derived trace/log helpers | real runtime/owner trace source required |
| Automations | protocol names only | Phase 3 |
| Inbox / Attention | filenames synthesized as review items | real approvals/questions/failures + actions required |
| Health | generic type plus Dashboard-authored checks | owner-declared health/readiness schema required |
| Brain | graph protocol names only | Phase 5 |
| Usage / tokens / cost | panel definition + protocol method name | no Gateway implementation or data source |
| Bots | panel definition; agent.list returns sessions | canonical Bot roster/state required |
| Rooms | documentation only | canonical Room/Thread projection required |
| Preview / Takeover | documentation only | runtime visibility integration required |
| Component/system health | /health only says Gateway process is up | aggregate dependency/integration/system health missing |

## 9. Token, Bot and attention surfaces

### Tokens / usage

CURRENT:
- Usage panel definition exists.
- usage.summary exists in protocol query names.
- QueryRouter does not serve usage.summary.
- no token, cost, provider, model or machine accounting implementation was found in current source.

There is also a scope mismatch: the Usage panel is declared system-scoped only, while usage.summary is classified as workspace-scoped by the protocol.

### Bots

CURRENT:
- Bots panel definition exists.
- no Bot domain model or canonical Bot registry exists in Dashboard.
- agent.list returns SessionStore session summaries under the key agents.

INTENDED:
- render canonical Bot identities, status and responsibility from the owning runtime/Multiple-Bots/OS projection.
- never infer Bot identity from chat sessions.

### Attention

CURRENT:
- NowModel can combine WorkSummary.attention and InboxItem lists.
- current WorkSummary is empty because there is no source.
- current inbox entries are synthesized from filenames with regenerated timestamps.
- no approval action can execute through Gateway.

INTENDED:
- owner-declared attention/approval records with severity, expiry, provenance and explicit allowed actions.

## 10. Modular desktop-shell vision

### CURRENT

Implemented as contracts/models:

- panel IDs and full/compact/HUD presentation enums;
- PanelRegistry;
- panel capability flags for float/detach/pin;
- LayoutManager with docked/floating/detached/hud/hidden states;
- per-panel system/workspace binding;
- explicit retarget method;
- save/load preset object model;
- design token constants;
- desktop/narrow ShellModel;
- tests that manipulate three independent panel instances;
- tests that preserve scope when a model is marked detached.

### INTENDED, not currently implemented

- React/Vite application;
- actual DOM rendering;
- docking engine such as Dockview;
- drag/drop/resizable dock groups;
- real floating windows;
- real browser popouts;
- native detached windows;
- always-on-top HUD;
- persisted layouts;
- View menu and preset UI;
- multi-monitor/window lifecycle;
- responsive rendered UI;
- keyboard/focus implementation;
- light/dark implementation;
- screenshot/visual regression fixtures;
- Tauri/Electron host;
- real native Mac/Windows installers.

Therefore the detachable desktop-shell vision is currently **contract/model ready, host/UI not implemented**.

A PanelState value of detached is not evidence that a window detaches.

## 11. Local and remote state

### Dashboard-owned local state that is legitimate

- registered connection metadata;
- active selection;
- panel placement/presentation;
- local preferences;
- disposable projection caches;
- subscription bookkeeping.

Current implementations are in-memory and disappear on restart.

### Local state that must not become canonical

- SessionStore transcripts/status;
- synthetic work/health/inbox models;
- copied provider/runtime history.

### Remote/external runtime state

CURRENT:
- one generic cli-jsonl subprocess adapter;
- LocalEchoAdapter;
- no Claude-specific, Codex-specific or ACP-specific implementation;
- no remote-host transport;
- no OpenClaw/channel bridge;
- no durable provider-session restore contract.

## 12. Security and permissions

### Strong CURRENT controls

- loopback-only server bind;
- strict protocol envelope;
- scoped IDs;
- raw-root key rejection;
- payload bound on params;
- canonical realpath resolution;
- traversal, absolute path, NUL and symlink escape rejection;
- read-only SQLite;
- no system fallback;
- system/workspace partitioning in core caches/sessions/subscriptions.

### GAPS

1. No authenticated actor/session at HTTP or WebSocket boundary.
2. No user/role/workspace ACL model.
3. No per-command permission intersection.
4. No approval re-check at effect time because no write path exists.
5. WebSocket subscribe control frames bypass the versioned request schema.
6. WebSocket connections can subscribe to syntactically valid but unregistered system IDs.
7. normal browser loopback origins with ports are rejected by isLoopbackOrigin.
8. no response-size bound or explicit WebSocket max payload contract in application code.
9. cli-jsonl can execute an arbitrary configured binary/args and inherits host process environment.
10. cli-jsonl advertises abort:true but abort only closes SessionStore state and does not kill an in-flight child.
11. no secret-redaction policy exists for transcripts/log projections.
12. no rate limiting was found.

The arbitrary CLI adapter is safe only as a trusted local integration primitive. It must not become a user-controlled command string.

## 13. Correctness defects found in current source

### D1. Workspace cache invalidation key mismatch

putProjection stores keys shaped:

    systemId:proj:workspaceId:path:mtime:size

invalidateWorkspace looks for:

    systemId:workspaceId:

Those prefixes do not match. Workspace invalidation therefore does not remove projection entries.

Current source.preview does not effectively consume the cache, which limits present impact but does not make the defect acceptable.

### D2. System-wide SubscriptionHub event key is invalid

SubscriptionHub.publish allows workspaceId to be absent but calls workspaceScopeKey with "-" when absent. "-" is not a valid workspaceId under the protocol regex. A system-wide event can therefore throw during key generation.

### D3. Browser Origin policy rejects ordinary loopback ports

isLoopbackOrigin compares against only http://127.0.0.1 and http://localhost, but constructs a comparison string including the request port. Browser origins such as http://127.0.0.1:3100 or http://localhost:5173 fail.

Node tests do not send an Origin and therefore do not cover the browser path.

### D4. CLI abort capability is overstated

CliJsonlAdapter.capabilities returns abort:true. The adapter does not retain an active child-process handle by session and abort does not kill that child. Session state changes, execution does not reliably stop.

### D5. Stable system IDs are not actually stable across restart

SystemRegistry is in-memory and auto-generates aiverse-01, aiverse-02 based on registration order. Restart/reordering can change identity. This conflicts with saved layout/session provenance requirements.

### D6. Windows root-overlap test uses "/" literal

SystemRegistry's root containment helper concatenates parent + "/". On Windows canonical paths use backslashes, so nested-root overlap protection is not portable.

### D7. Inbox provenance/time is fabricated

Filesystem inbox items receive createdAt = observedAt on every projection. Refreshing makes an old file look newly created. Sanitized filename IDs can also collide.

### D8. Missing work is encoded as empty work

workspace-sources explicitly returns summarizeWork(..., []) when no canonical task source exists. The architecture's own law says missing/unavailable must not be shown as zero.

### D9. Health semantics are Dashboard-authored

Health dimensions manifest/context/layers and checks such as objective/next/constraints are defined inside Dashboard. The architecture explicitly says Dashboard must not define 4Cs meaning.

### D10. Presentation preset validation is incomplete

loadPreset verifies instanceId and known panelId but does not fully revalidate systemId, workspaceId, state, placement, presentation or panel capability. retarget validates systemId but not workspaceId or the panel's scope requirements.

## 14. Lifecycle matrix

| Stage | Exists? | Command/API | Idempotent? | State owner | Acceptance evidence | Gap |
|---|---|---|---|---|---|---|
| install | source only | npm ci/build conventions, no member command | unverified | repository | no clean install acceptance | no packaged install |
| attach/register OS | partial | SystemRegistry.register in code | duplicate fails rather than reconcile | Dashboard | unit tests | no public UX/API, no persistence |
| enable | no | none | n/a | Dashboard/host | none | missing |
| activate/adopt | no | none | n/a | host | none | missing |
| initialize | partial | object construction/mount calls | mixed | Dashboard | unit tests | no product bootstrap |
| migrate/import | no | none | n/a | Dashboard config future | none | no persisted state yet |
| doctor/status | partial | GET /health, validateCompatibleOs, workspace.health | read-only | Dashboard + owner | unit tests | only shallow/synthetic health |
| update | no supported path | none | unverified | distribution | none | missing |
| disable | no public path | none | n/a | Dashboard | none | missing |
| detach OS | internal only | SystemRegistry.unregister | yes-ish in memory | Dashboard | no product acceptance | no public flow/persistence |
| uninstall | no | none | n/a | distribution | none | missing |
| reinstall | no | none | n/a | distribution | none | missing |
| reconcile | no | none | n/a | host/Dashboard | none | missing |
| rollback | no | none | n/a | distribution | none | missing |

## 15. Install-order behavior

Conceptually, the in-memory registry can register an OS after Dashboard objects exist, so the code does not require one repository install order.

Product-level order independence is not proven because:

- Dashboard has no supported installation/launch flow;
- there is no persistent discovery/registry;
- there is no reconcile operation;
- there is no late-adoption command;
- one repository test assumes a sibling OS at a hardcoded developer path.

Install-order independence is therefore PARTIAL at library level and MISSING at member/product level.

## 16. Health-depth assessment

- **STRUCTURAL:** PARTIAL. validateCompatibleOs checks OS shape and workspace manifests.
- **ATTACHMENT:** PARTIAL. in-memory registry state can be validated.
- **RUNTIME:** PARTIAL. GET /health proves the Gateway process answers.
- **DEPENDENCY:** MISSING. runtime/provider/owner projection dependencies are not deeply checked.
- **OPERATIONAL:** PARTIAL/TEST-ONLY. fixtures exercise reads and a generic child process.
- **SYSTEM:** MISSING. no supported end-to-end member path through real owner projections and canonical commands.

GET /health must not be interpreted as system health.

## 17. Current milestone

The repository's current intended milestone is:

**Phase 2 Task 6: full live agent-control story green.**

The build ledger marks 13 tasks complete and 60/60 tests locally green, but Phase 2 Task 6 is still unchecked.

### Current-target readiness

**Verdict: PARTIAL, NOT CURRENT-TARGET COMPLETE.**

The current core has useful pieces, but the missing product/control wiring is material, not polish.

### Exact remaining work before Phase 2 can truthfully pass

1. Add a real application/bootstrap entrypoint that constructs the registry/cache/router/hub/runtime adapters and starts the supported product.
2. Add the actual React/Vite UI or explicitly redefine the milestone as a headless library milestone. Current docs call it a visual Dashboard, so model-only completion is insufficient.
3. Add a supported OS registration/select flow with persistent stable system IDs.
4. Replace Dashboard-invented health/work/inbox semantics with versioned owner projections.
5. Replace agent.list-as-sessions with a real owner-declared agent/Bot projection.
6. Define whether SessionStore is only a disposable display buffer; make provider/runtime history and continuation recoverable from the owner.
7. Wire authenticated chat.send/chat.abort through the selected owner command boundary.
8. Do not call CliJsonlAdapter directly as canonical authority. Route privileged effects through owner permission/approval/idempotency checks.
9. Implement real cancellation of in-flight runtime work or advertise abort:false.
10. Add browser-compatible HTTP/WS origin handling and a typed WebSocket client with reconnect/resync and event invalidation.
11. Add actor authentication before enabling writes, plus command authorization and approval context.
12. Fix D1-D10 correctness issues above.
13. Replace the developer-local integration prerequisite in tests with a portable fixture or explicit optional integration suite.
14. Add CI on clean machines and exercise supported Node/platform matrix.
15. Add one end-to-end Phase 2 gate that uses the documented user path, not direct object construction.

If the required canonical OS command/projection APIs do not yet exist, those portions are externally blocked. That cannot be resolved by Dashboard inventing alternate stores or direct write shortcuts.

## 18. Final seamless-system gap

After Phase 2, the repository still intentionally has later phases:

- Phase 3: automations, approvals and audit;
- Phase 4: OpenClaw plus Telegram/Discord/WhatsApp bridge with ACL/risk controls;
- Phase 5: Brain graph projection and optional 3D;
- Phase 6: traces, token/cost/resource observability and exporters;
- final native desktop packaging on explicit approval.

For the final "works like a glove" state, all of those must consume the same owner-declared projection/command contracts without adding Dashboard-owned truth.

## 19. Completeness matrix

| Dimension | Status | Reason |
|---|---|---|
| ENGINE / CORE | PARTIAL | strong read/isolation scaffolding, Phase 2 control incomplete |
| ARCHITECTURE / CONTRACT | COMPLETE WITH LIMITATIONS | extensive architecture and protocol, some contracts contradict implementation |
| INSTALL / PACKAGE | MISSING | private workspace packages, no supported user install/start |
| HOST INTEGRATION | PARTIAL | can register an OS in code, no bootstrap/product path |
| ATTACH / REGISTER | PARTIAL | SystemRegistry only, process-local |
| ACTIVATE / ADOPT | MISSING | no supported activation/reconcile |
| SCOPE INITIALIZATION | PARTIAL | IDs and panel scopes exist, no user flow |
| MIGRATION / LEGACY | NOT APPLICABLE CURRENTLY / FUTURE GAP | no persisted Dashboard config yet |
| HEALTH / DOCTOR | PARTIAL | structural/process checks, synthetic domain health |
| PERMISSION / SAFETY | PARTIAL | strong filesystem isolation, weak actor/command auth |
| CROSS-COMPONENT READ | PARTIAL | direct raw conventions rather than owner projection APIs |
| CROSS-COMPONENT WRITE | MISSING | all commands blocked |
| UPDATE / UPGRADE | MISSING | no supported path |
| DISABLE / DETACH / UNINSTALL | MISSING | internal unregister only |
| REINSTALL / RECONCILE | MISSING | no product flow |
| CROSS-PLATFORM | UNVERIFIED | Windows-sensitive path code, no CI matrix |
| ACCEPTANCE | PARTIAL | 60 tests claimed locally, mostly library/fixture tests |
| RELEASE / DISTRIBUTION | MISSING | no releases, packages private, no desktop artifact |
| DOCUMENTATION CONSISTENCY | PARTIAL | architecture strong, status claims overstate several implemented surfaces |

## 20. Historical evolution

### HISTORICAL

The repository is young and its visible history is mostly additive, not repair-driven.

Key evolution:

- 2026-09-09: research, architecture blueprint and source-adoption plan established Layer 5.
- 2026-09-10: multi-OS isolation added systemId as a boundary above workspace.
- 2026-09-12: PR #1 added the modular desktop-shell architecture as a planning-only amendment.
- 2026-09-12: Task 1 was reworked to add panelId and full/compact/HUD protocol concepts after that amendment.
- 2026-09-12: Phase 1 tasks were implemented sequentially and marked complete.
- 2026-09-12: Phase 2 Tasks 1-5 added in-memory live models, reads, activity, trace/log helpers and a generic runtime adapter.

No substantial repair PR lineage was found beyond the additive/rework sequence. PR #1 is the only visible pull request; later implementation commits were pushed directly to main.

### Permanent lessons already evidenced

- systemId must exist above workspaceId for multi-install isolation;
- panel detachment must never relax scope;
- presentation state is allowed to be Dashboard-owned;
- missing owner state must fail closed rather than borrow another system.

### New audit law

A projection layer must not only avoid durable duplicate storage. It must also avoid becoming the **semantic owner** by inventing health, work, Bot, approval or runtime meaning from raw internals.

## 21. INSPIRATION

Explicit repository-recorded inspirations include:

- LifeOS Pulse: projection-first status/health patterns;
- OpenClaw: typed Gateway, channel/pairing concepts, automations/approvals;
- OpenHands: runtime/client separation and ACP/session ideas;
- OpenFang: autonomous-worker information architecture;
- TenacitOS: Mission Control visual concepts, while explicitly rejecting local dashboard JSON as canonical truth and direct editor ownership;
- Langfuse and Phoenix: trace/span/token/cost observability;
- Hermes Desktop: native React UI over a separate headless backend;
- Grok Bot: persistent Bot roster, heterogeneous timeline, Status -> Preview -> Takeover;
- Kylon: Room/thread collaboration, permissions and provenance concepts;
- Dockview: docking/popout patterns;
- Tauri 2: preferred native-wrapper direction, with Electron as fallback/reference.

The repository describes these as curated concepts. No current source evidence reviewed here establishes a wholesale fork.

There is no repository LICENSE file at the reviewed tree. Before copying implementation code from an inspiration, licensing and attribution must be made explicit.

## 22. Definition of done

### Current-target definition of done: Phase 2

Phase 2 is done only when all of these are true:

- a clean user can install and launch Dashboard through a documented path;
- a compatible OS can be registered through a supported product path and retains a stable ID across restart;
- a real browser UI renders Now/Chat/Work/Runs/Bots/Attention/Health with truthful unavailable states;
- owner-declared projections, not Dashboard filesystem guesses, provide domain meaning;
- chat send and abort travel through an authenticated/authorized canonical command boundary;
- runtime cancellation stops actual work;
- live events reconnect/resync safely;
- no Dashboard process-local session store is the only copy of provider/runtime truth;
- browser HTTP/WS transport works from the supported UI origin;
- cross-system and cross-workspace isolation remains enforced;
- clean CI passes with no developer-local sibling path prerequisite;
- end-to-end Phase 2 acceptance uses the supported user path.

### Final-target definition of done

In addition to current-target completion:

- Automations and approvals are real owner-backed projections/commands.
- Omnichannel ingress enforces pairing, ACL and risk policies.
- Brain graph is a derived projection, not a Dashboard graph database.
- token/cost/resource usage comes from canonical/official telemetry.
- modular panels actually dock, float, detach and support native HUD behavior.
- Dashboard settings/presentation persistence is versioned and migratable.
- Mac/Windows packaging is tested and immutable.
- deleting Dashboard caches/reinstalling Dashboard cannot delete canonical domain/provider truth.
- the complete system remains usable with optional components absent or later-installed.

## 23. Open decisions

1. What exact versioned owner projection API will provide health, work, Bots, Rooms, attention, approvals, usage and Brain data?
2. What is the supported Dashboard-to-OS command transport: socket, localhost RPC, stable CLI JSON, MCP/ACP or another contract?
3. Which owner persists chat/provider continuation and run history?
4. How will stable systemId connection metadata be persisted, migrated and backed up without becoming domain truth?
5. What authentication model protects local and future remote Dashboard clients?
6. Which runtime adapters are production-supported first?
7. When will Dockview/Tauri evaluation move from inspiration to implementation?
8. Is Usage system-scoped, workspace-scoped or both? Current panel/protocol definitions disagree.

## 24. Supreme-system contribution

Dashboard contributes the following system-wide laws:

1. **Visual projections do not own domain truth.**
2. **Projection semantics must be owner-declared, not inferred from sibling internals.**
3. **Unavailable is not empty, zero or healthy.**
4. **UI/runtime buffers must be disposable and reconstructable from the real owner when continuity matters.**
5. **A runtime adapter is a connector, not permission or canonical authority.**
6. **Every privileged UI effect must traverse the owner-routed permission/approval/idempotency pipeline.**
7. **Detached/floating/HUD presentation never widens system/workspace authority.**
8. **A component is not a user-facing Dashboard merely because its view models and tests exist. Product-path acceptance must exercise the real UI/launch/install path.**
