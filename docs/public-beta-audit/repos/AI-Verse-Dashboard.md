# A1.13 - Independent Repository Audit: AI-Verse-Dashboard

**Audit date:** 2026-09-16  
**Frozen ref:** bf6a3a019b07b189c9c701f4edf01e0ded1e7a00  
**System baseline:** 5e923f76dd45433620a5df1138910c7419de70b7  
**Status:** COMPLETE  
**Standalone verdict:** DOGFOOD BLOCKED  
**R-a:** COMPLETE / PASS  
**R-b:** COMPLETE / MATERIAL FAILURES FOUND  
**R-c:** COMPLETE / BLOCKED  
**New findings:** WSA-2026-038 through WSA-2026-042  
**Next unused finding ID after this task:** WSA-2026-043  
**Next:** A1.14 AI-Verse-System

## 1. Independence and drift control

A1.13 reconstructed AI-Verse-Dashboard from the frozen Dashboard repository itself before relying on sibling repositories as evidence.

At task start and immediately before the System audit branch was created:

- Dashboard main remained exactly bf6a3a019b07b189c9c701f4edf01e0ded1e7a00;
- System main remained exactly 5e923f76dd45433620a5df1138910c7419de70b7;
- Dashboard had zero open PRs;
- System had zero open PRs;
- no Dashboard product file was modified;
- MC1.4 remained BLOCKED behind the whole-system audit gate.

The frozen ref is therefore still valid for A1.13.

## 2. Standalone reconstruction

AI-Verse Dashboard is Layer 5, the local visual Control Room and presentation surface for one or more isolated AI-Verse OS installations.

Its intended ownership boundary is unusually explicit:

- Dashboard may own presentation state;
- Dashboard may own local OS connection metadata;
- Dashboard may own disposable caches and layout state;
- Dashboard may normalize runtime/session/event projections;
- Dashboard must not become a second source of canonical domain truth;
- systemId is intended to be the primary browser-to-OS authority selector;
- workspaceId is intended to scope all workspace-bound operations;
- browser requests should never supply arbitrary filesystem roots;
- canonical mutations must ultimately pass owner command/permission boundaries.

Current repository reality contains two overlapping generations:

1. an existing scratch-built read-only/live Dashboard foundation under packages/, apps/gateway and apps/web;
2. a newer Mission Control adoption program whose accepted progress is 11/100 and whose real local proof MC1.4 is intentionally paused.

The existing local apps/gateway is explicitly documented as temporary scaffolding and not the canonical AI-Verse Gateway.

## 3. Current implementation inventory

### Executable roots

- packages/protocol: request/response/event envelope, method registry, ID rules and raw-root rejection.
- packages/registry: OS compatibility probe, systemId registry and per-window selection.
- packages/os-read-adapter: path containment, Markdown and SQLite read-only projectors, workspace discovery and disposable cache.
- packages/client: typed Dashboard RPC client and client-side cache.
- packages/read-models: derived Health, Work, Inbox and Now projections.
- packages/live: sessions, heterogeneous timeline, runtime adapters, run/activity models.
- apps/gateway: localhost HTTP/WebSocket query gateway and subscription hub.
- apps/web: framework-free shell/panel/layout models for later React/Vite host.
- scripts/mc1: pinned Mission Control bootstrap, canonical Gateway preflight and disposable runtime-dispatch proof automation.

### Governance roots

- README.md
- docs/ARCHITECTURE-BLUEPRINT.md
- docs/MODULAR-DESKTOP-SHELL.md
- docs/BASELINE-PRESERVATION-REPORT-2026-09-15.md
- docs/PRD-MISSION-CONTROL-AIVERSE-DASHBOARD-2026-09-15.md
- docs/CANONICAL-MISSION-CONTROL-ADOPTION-PLAN-2026-09-15.md
- docs/MISSION-CONTROL-EXECUTION-TRACKER-2026-09-15.md
- THIRD_PARTY_NOTICES.md

### Test and CI roots

- test/protocol.test.ts
- test/registry.test.ts
- test/read-adapters.test.ts
- test/gateway.test.ts
- test/web-shell.test.ts
- test/read-models.test.ts
- test/isolation.test.ts
- test/phase1-gate.test.ts
- live/runtime tests
- test/mc1-lab.test.ts
- .github/workflows/ci.yml

## 4. Evidence inventory

### E-A1.13-001 - frozen repository identity
Source: live GitHub repository state  
Ref: bf6a3a019b07b189c9c701f4edf01e0ded1e7a00

Verified:

- public repository;
- default branch main;
- zero open PRs;
- exact match to the A0 frozen Dashboard ref.

### E-A1.13-002 - repository evolution
Source: commit history and merged PRs #1 through #10

Important current milestones:

- Phase 1 scratch Dashboard foundation complete;
- Phase 2 implemented through runtime adapter Task 5;
- Mission Control adoption made canonical;
- MC0 complete;
- MC1.1 through MC1.3 accepted;
- MC1.4 paused behind whole-system audit.

### E-A1.13-003 - README ownership law
Source: README.md

README states Dashboard owns zero domain truth, registered OS installations are isolated by systemId, workspace isolation is server-side, arbitrary roots are not browser authority, and local-first Gateway behavior is the intended interface pattern.

### E-A1.13-004 - architecture blueprint
Source: docs/ARCHITECTURE-BLUEPRINT.md

The blueprint requires:

- local authenticated control/read gateway;
- one approved OS root per stable systemId;
- hard system isolation;
- workspace isolation;
- separate query and command paths;
- browser never receives path authority;
- server-side realpath resolution;
- symlink escape rejection;
- disposable system-partitioned cache;
- authenticated command intent;
- no silent cross-system fallback.

### E-A1.13-005 - current Mission Control PRD and tracker
Source: PRD and MISSION-CONTROL-EXECUTION-TRACKER-2026-09-15.md

Current accepted Mission Control progress is 11/100.

MC1.4 remains BLOCKED by explicit owner decision until the independent whole-system audit and required blocking repairs release the gate.

### E-A1.13-006 - preservation report
Source: docs/BASELINE-PRESERVATION-REPORT-2026-09-15.md

Preservation law explicitly keeps:

- systemId/workspaceId isolation;
- no silent fallback;
- server-side root resolution;
- traversal and symlink escape rejection;
- cross-system cache/session/subscription isolation.

The same document explicitly labels:

- apps/gateway as temporary Dashboard-local scaffolding;
- SessionStore-backed agent truth as non-canonical;
- source-derived Health/Work/Inbox semantics as shadow-authority risk;
- direct CLI runtime execution as prototype scaffolding.

### E-A1.13-007 - protocol enforcement
Source: packages/protocol/src/ids.ts, methods.ts, envelope.ts

Verified:

- bounded systemId/workspaceId patterns;
- strict request envelope;
- workspace requirement on workspace-scoped methods;
- recursive forbidden raw-root keys;
- 64 KiB params bound;
- command methods fail closed in the current local query router;
- protocol version negotiation.

### E-A1.13-008 - OS registry
Source: packages/registry/src/validation.ts, registry.ts, selection.ts

Registration:

- canonicalizes the candidate root at registration time;
- verifies a lightweight AI-Verse shape;
- rejects duplicate and overlapping canonical roots;
- maps root to stable in-memory systemId;
- hides the root from public views;
- refuses unknown or unauthorized IDs;
- stores independent per-window selection state.

The registry does not pin a filesystem identity beyond the stored canonical pathname.

### E-A1.13-009 - path containment
Source: packages/os-read-adapter/src/path-resolve.ts

Workspace/source resolution:

- validates workspace IDs;
- resolves systemId through the registry;
- resolves the workspace directory to realpath;
- rejects workspace realpaths outside the OS root;
- rejects absolute, traversal and NUL source paths;
- resolves source realpath and rejects symlink escape outside the workspace.

This is a strong current control.

### E-A1.13-010 - Markdown/SQLite read boundaries
Source: markdown.ts, sqlite.ts

Markdown:

- file-only;
- extension allowlist;
- 256 KiB size cap;
- realpath containment;
- hash/provenance projection.

SQLite:

- file and extension checks;
- 32 MiB cap;
- Node readOnly database open;
- PRAGMA query_only;
- table/column identifier allowlists;
- SELECT/WITH/EXPLAIN gate;
- parameter and row bounds.

### E-A1.13-011 - local Gateway HTTP/WS server
Source: apps/gateway/src/server.ts

Verified:

- listener binds 127.0.0.1;
- explicit remote host values are refused;
- POST /rpc parses protocol requests;
- GET /health is public;
- WebSocket connections bind to one syntactic systemId;
- cross-system RPC frames on a bound socket are rejected.

No authentication or bearer/session authorization is implemented by this server.

### E-A1.13-012 - browser Origin implementation
Source: server.ts

LOOPBACK_ORIGINS contains only:

- http://127.0.0.1
- http://localhost

isLoopbackOrigin constructs protocol + hostname + explicit port when present and requires the full string to match the set.

Therefore http://localhost:5173 and http://127.0.0.1:5173 fail the browser Origin check.

### E-A1.13-013 - WebSocket subscription implementation
Source: handleSocket in server.ts and SubscriptionHub

Each subscribe frame calls hub.subscribe and assigns the new subscription ID to one local variable.

If the same socket subscribes again:

- prior subscription is not unsubscribed;
- the local subId is overwritten;
- only the newest subscription is removed on close;
- prior listeners remain registered and continue sending events to the same socket.

### E-A1.13-014 - query router
Source: apps/gateway/src/query-router.ts

Current served reads include:

- system.list/get/info;
- workspace list/get/health/inbox;
- task list derived view;
- agent/session reads;
- run reads;
- source.preview.

Unknown systems/workspaces fail instead of falling back.

The local command set remains blocked.

### E-A1.13-015 - unauthenticated read trace
Source: server.ts + query-router.ts

A client with no Origin header is intentionally treated as a non-browser client and accepted.

No token, session, OS-user identity or other credential is checked.

Such a client can:

1. call system.list;
2. discover registered systemId values;
3. call workspace.list;
4. discover workspace IDs;
5. call source.preview and other projections.

The HTTP server is loopback-only, but the read boundary is otherwise unauthenticated.

### E-A1.13-016 - system root substitution trace
Source: registry.ts + path-resolve.ts

Registry stores the canonical path string from registration.

Later resolveRoot returns the stored pathname without proving it still names the same filesystem object or approved installation.

resolveWorkspaceRoot subsequently resolves the current realpath of that stored path and treats the new target as the system root.

A removed/replaced registered path can therefore silently rebind one existing systemId to different compatible filesystem content.

### E-A1.13-017 - read-model shadow semantics
Source: packages/read-models/src/workspace-sources.ts, health.ts, inbox.ts

Current derived projections invent semantic states from file presence and names.

Examples:

- manifest presence becomes healthy/critical;
- presence of Memory + decisions becomes healthy/warning;
- heading detection determines context health;
- every inbox file becomes kind review, severity info and createdAt equal to observation time;
- current work is returned as empty rather than owner-backed task truth.

These are Dashboard interpretations, not owner-declared truth.

### E-A1.13-018 - repository acknowledges read-model limitation
Source: BASELINE-PRESERVATION-REPORT

The repository itself labels synthetic Health/Work/Inbox semantics as shadow-authority risk and requires replacement by owner-declared projections.

### E-A1.13-019 - session/runtime scaffolding
Source: packages/live

SessionStore partitions sessions by systemId and the query router checks workspace existence before exposing session projections.

Runtime adapters use shell=false-style argv spawn, bounded message/output sizes and per-system adapter registration.

These are useful scaffolds but are explicitly not canonical agent/Bot authority.

### E-A1.13-020 - panel/client model
Source: packages/client and apps/web

Current web package is framework-free and has no actual browser/Vite host.

DashboardClient sends typed RPC frames and namespaces client cache keys by systemId/workspaceId.

Panel/layout state remains presentation-only.

### E-A1.13-021 - Gateway tests
Source: test/gateway.test.ts

Current tests prove:

- loopback binding;
- read route behavior;
- command blocking;
- no cross-system fallback;
- basic WebSocket partitioning;
- rejection of a cross-system RPC frame.

The tests perform only one subscribe per socket and do not exercise A -> B resubscribe cleanup.

HTTP tests use Node fetch without browser Origin.

### E-A1.13-022 - registry/isolation tests
Source: registry.test.ts, isolation.test.ts

Tests cover:

- compatible shape;
- duplicate/overlap roots;
- unknown system failure;
- per-window selection;
- traversal/symlink source escape;
- A/B fixture isolation.

No test replaces an approved canonical root after registration.

### E-A1.13-023 - Phase 1 gate
Source: test/phase1-gate.test.ts

Phase 1 exercises register -> read -> panels -> isolate -> shell -> live local query.

It does not launch a browser host and therefore does not prove Origin compatibility.

### E-A1.13-024 - Mission Control MC1 automation
Source: scripts/mc1 and test/mc1-lab.test.ts

Verified:

- exact upstream Mission Control pin;
- disposable lab path;
- deletion containment;
- canonical Gateway config read;
- authenticated canonical Gateway /status and /v1/models checks;
- optional workspace-explicit chat smoke;
- in-memory proof secrets;
- secret redaction;
- hidden token prompt;
- temporary Mission Control domain state only.

### E-A1.13-025 - third-party provenance
Source: THIRD_PARTY_NOTICES.md

Builderz Mission Control is pinned to 5483a0e1eef15b467c167e95796791112cedbb7c under MIT.

GawkBot is reference-only under the reviewed Sustainable Use License.

No imported Mission Control source was recorded at this snapshot.

### E-A1.13-026 - CI workflow
Source: .github/workflows/ci.yml

Dashboard CI performs npm ci, TypeScript build and the full Node test suite across:

- Ubuntu;
- macOS;
- Windows;

using Node 22.

### E-A1.13-027 - MC1 PR-head CI
Source: Dashboard CI run 34994307940

PR #8 implementation head passed all three OS jobs with successful install/build/test steps.

### E-A1.13-028 - latest pause PR CI
Source: Dashboard CI run 34997395259

PR #10 head passed all three OS jobs:

- macOS;
- Windows;
- Ubuntu.

The latest PR changed only the Dashboard execution tracker to pause MC1.4.

### E-A1.13-029 - current-head hosted status limitation
Source: workflow/status query for bf6a3a019b07...

No workflow run/status is attached directly to the merge commit.

The exact runtime tree was already tested in PR #8, and PR #9/#10 changed tracker documentation only. PR #10's documentation head also passed 3/3 CI.

### E-A1.13-030 - final live pre-write freeze
Source: live GitHub state

Immediately before audit mutation:

- Dashboard head remained bf6a3a019b07...;
- System head remained 5e923f76dd45...;
- both repositories had zero open PRs;
- next unused finding ID was WSA-2026-038.

## 5. Verified strengths

The standalone audit verifies several unusually strong boundaries:

- systemId and workspaceId are first-class protocol fields;
- arbitrary roots are rejected from normal protocol params;
- workspace/path realpath containment is explicit;
- symlink escape at source/workspace boundaries is rejected;
- missing systems fail closed instead of falling back;
- query and command method sets are separated;
- current local query server remains read-only;
- cache/session objects are system-namespaced;
- layout state is not domain truth;
- current Mission Control proof uses the canonical authenticated AI-Verse Gateway rather than promoting Dashboard local gateway authority;
- third-party pinning and provenance are explicit;
- whole-system audit pause is correctly enforced in Dashboard tracker.

## 6. Contradiction register

### C-A1.13-001 - WebSocket workspace switching leaks previous subscription scope

**Source A:** README/architecture require workspace-scoped subscriptions and no context leakage.  
**Source B:** handleSocket leaves the old subscription registered when the same socket subscribes again.  
**Higher-authority source:** executable WebSocket server and SubscriptionHub.  
**Classification:** implementation defect / workspace isolation.  
**Finding:** WSA-2026-038.

### C-A1.13-002 - approved systemId is not durably bound to the approved filesystem identity

**Source A:** architecture describes systemId as mapping to one explicitly approved compatible OS root and treats each registered OS as an authority boundary.  
**Source B:** the implementation stores a pathname and later follows whatever filesystem object currently resolves at that path.  
**Higher-authority source:** executable registry/path resolver.  
**Classification:** implementation defect / system identity isolation.  
**Finding:** WSA-2026-039.

### C-A1.13-003 - architecture says authenticated local gateway, implementation has no authentication

**Source A:** architecture names a local authenticated control/read gateway and authenticated intent.  
**Source B:** apps/gateway authenticates neither /rpc nor WebSocket clients; Origin is the only browser-origin check and missing Origin is allowed.  
**Higher-authority source:** executable server.  
**Classification:** implementation defect / local data-access security.  
**Finding:** WSA-2026-040.

### C-A1.13-004 - browser origin policy rejects normal localhost application ports

**Source A:** architecture expects a separate local Web UI/React/Vite app consuming the Dashboard Gateway.  
**Source B:** server accepts only loopback Origin strings without explicit ports.  
**Higher-authority source:** executable server.  
**Classification:** implementation defect / browser integration.  
**Finding:** WSA-2026-041.

### C-A1.13-005 - Dashboard claims projection-only truth but current read models invent domain semantics

**Source A:** README/architecture say Dashboard owns zero domain truth.  
**Source B:** current read models synthesize health and inbox classifications from generic file presence/name patterns.  
**Source C:** preservation report explicitly calls these semantics shadow-authority risk.  
**Higher-authority source:** executable read models, with current repository limitation acknowledgment.  
**Classification:** implementation defect / shadow authority.  
**Finding:** WSA-2026-042.

## 7. New findings

### WSA-2026-038 - WebSocket resubscribe leaves prior workspace subscription active

**Severity:** HIGH  
**Confidence:** PROVEN  
**State:** OPEN  
**Root area:** workspace isolation / realtime subscription lifecycle  
**Affected repo:** AI-Verse-Dashboard

#### Summary

One WebSocket can subscribe to workspace A and then subscribe to workspace B.

The server creates a second subscription but does not remove the first.

The socket therefore continues receiving A events after the client has switched to B.

#### Deterministic trace

1. Connect socket bound to system S.
2. Send subscribe for workspace A.
3. Server creates sub-1.
4. Send subscribe for workspace B.
5. Server creates sub-2 and overwrites local subId.
6. sub-1 remains in SubscriptionHub.
7. Publish event for S/A.
8. sub-1 still invokes the same socket listener.
9. Client receives A event after B became the apparent active subscription.

On close, only sub-2 is removed.

#### Impact

Workspace-scoped live context can bleed across an explicit workspace switch.

This can contaminate the visible timeline/control-room state with events from the previous workspace and directly violates the primary workspace isolation contract.

#### Required closure evidence

- unsubscribe the previous subscription before accepting a new one, or track and clear all subscriptions per socket;
- validate the requested workspace through protocol and registered workspace resolution;
- add A -> B -> A resubscribe tests;
- prove no stale events after each switch;
- prove socket close releases all subscriptions.

### WSA-2026-039 - registered systemId can silently follow a replaced OS filesystem root

**Severity:** HIGH  
**Confidence:** PROVEN  
**State:** OPEN  
**Root area:** system identity / registered-root authority binding  
**Affected repo:** AI-Verse-Dashboard

#### Summary

Registration canonicalizes the approved root once and stores its pathname.

Later reads resolve that pathname again.

If the registered path is removed/replaced or redirected to another compatible tree, the same systemId can begin reading the replacement without new user approval.

#### Impact

The security/context meaning of a stable systemId can change underneath active windows, caches and runtime state.

A system selected as A can silently become filesystem B while retaining A's Dashboard identity.

#### Required closure evidence

- bind registration to durable owned identity beyond pathname alone;
- detect root replacement/rebinding before reads;
- mark the system unauthorized on identity drift;
- require explicit reapproval/rebind;
- add rename/symlink/replacement regressions.

### WSA-2026-040 - Dashboard-local Gateway exposes OS read APIs without authentication

**Severity:** HIGH  
**Confidence:** PROVEN  
**State:** OPEN  
**Root area:** local gateway authentication / privacy boundary  
**Affected repo:** AI-Verse-Dashboard

#### Summary

apps/gateway binds to loopback but performs no client authentication.

A non-browser client with no Origin header is explicitly accepted.

It can enumerate systems/workspaces and request read projections.

#### Impact

Any process able to connect to the local TCP port can access Dashboard-exposed OS data independently of the filesystem permissions and Dashboard UI selection flow.

The current server is read-only, which bounds impact, but this still violates the documented authenticated-gateway boundary.

#### Required closure evidence

- require a local authenticated session/token or stronger OS-bound transport identity;
- do not treat Origin as authentication;
- preserve loopback binding;
- reject unauthenticated HTTP and WebSocket requests;
- add local unauthenticated-client negative tests;
- ensure future command paths cannot inherit this gap.

### WSA-2026-041 - browser Origin check rejects normal localhost origins with explicit ports

**Severity:** MEDIUM  
**Confidence:** PROVEN  
**State:** OPEN  
**Root area:** local browser integration / Origin policy  
**Affected repo:** AI-Verse-Dashboard

#### Summary

The Origin allowlist contains only http://localhost and http://127.0.0.1.

A real local web host normally sends an Origin with its port, such as http://localhost:5173.

The implementation includes the port in the compared origin string, so such requests are rejected.

#### Impact

The intended separate browser/Vite UI cannot call the local Dashboard Gateway under normal development/desktop-web port layouts without changing the policy or proxying same-origin.

Node-based tests do not expose the bug because they send no Origin header.

#### Required closure evidence

- define an explicit trusted local-origin policy that safely handles approved ports;
- test HTTP and WebSocket calls from representative localhost/127.0.0.1 origins with ports;
- reject non-loopback and unapproved origins.

### WSA-2026-042 - synthetic Health/Inbox projections create Dashboard shadow semantics

**Severity:** MEDIUM  
**Confidence:** PROVEN  
**State:** OPEN  
**Root area:** canonical ownership / projection truth  
**Affected repo:** AI-Verse-Dashboard

#### Summary

Current read models assign domain-like semantics from generic filesystem observations.

Examples include classifying workspace health from file presence/headings and converting every inbox filename into a review/info item with observation time as createdAt.

The repository itself now acknowledges this as shadow-authority scaffolding.

#### Impact

Dashboard can display authoritative-looking health/attention semantics that were not declared by the owning component.

This risks misleading operators and creates a second interpretation layer over canonical owners.

#### Required closure evidence

- replace synthetic production semantics with owner-declared projections;
- preserve unavailable/unknown when owner truth is absent;
- label any remaining heuristics explicitly as derived/non-authoritative;
- add tests proving Dashboard does not invent owner health, approval or task truth.

## 8. Current Mission Control release interpretation

The Mission Control adoption program is not a completed Dashboard release.

Current accepted program progress is 11/100.

MC0 is complete.

MC1.1, MC1.2 and MC1.3 are accepted automation/build work.

MC1.4, the first real owner-local Mission Control -> canonical Gateway proof, is intentionally BLOCKED by the whole-system audit gate.

MC1.5 and MC2+ remain pending.

Therefore A1.13 does not represent the current Mission Control shell as dogfood-ready or release-ready.

## 9. CI and acceptance interpretation

The current Dashboard has meaningful cross-platform CI.

PR #8's runtime-proof implementation passed Ubuntu, macOS and Windows.

PR #10's exact pause change also passed Ubuntu, macOS and Windows.

The final merge commit has no directly attached workflow run, so A1.13 does not overstate current-head CI identity.

The runtime code has not changed after PR #8; subsequent accepted changes were tracker-only.

Existing tests cover many happy-path isolation properties, but they do not cover:

- repeated WebSocket subscription on one socket;
- registered root replacement after approval;
- unauthenticated local client denial;
- browser loopback Origin values with explicit ports.

## 10. Mandatory lens review

### Identity and ownership

Dashboard ownership law is clear and generally sound.

The major current identity gap is that systemId is not durably bound to the originally approved filesystem object.

### Scope and isolation

Static path isolation is strong.

Realtime workspace resubscribe isolation is broken by WSA-2026-038.

### Read/write boundary

Current local Dashboard Gateway is read-only and command methods fail closed.

Mission Control proof routes through the canonical authenticated AI-Verse Gateway rather than expanding local Dashboard authority.

### Authentication and privacy

Current temporary apps/gateway is not authenticated despite architecture requiring an authenticated local gateway.

This is WSA-2026-040.

### Filesystem safety

Workspace and source realpath containment are strong.

Registered root identity replacement remains a higher-level gap.

### Canonical truth

Dashboard-local synthetic Health/Inbox interpretations violate the intended owner-backed projection model.

The repository already plans to retire them.

### Runtime/session state

Session and adapter state is system-namespaced and explicitly temporary.

No current evidence supports treating it as canonical Bot or Memory truth.

### Browser/product path

There is no actual React/Vite browser application yet.

The current origin check would reject ordinary local host ports once that application is launched.

### Third-party provenance

Mission Control pinning and current license attribution are explicit.

GawkBot remains reference-only.

### Cross-platform

CI covers Node 22 on Ubuntu, macOS and Windows.

### Failure/recovery

Current static tests cover fail-closed unknown IDs and traversal.

Subscription replacement, root rebinding and authenticated reconnect behavior need stronger failure-path coverage.

### Release readiness

The repository itself has correctly paused dogfood.

A1.13 agrees with that pause for independent technical reasons as well.

## 11. Negative-space checks

A1.13 explicitly reviewed for:

- arbitrary browser root authority;
- systemId/workspaceId validation;
- path traversal;
- symlink escape;
- workspace fallback;
- cross-system cache/session mixing;
- local Gateway bind scope;
- local Gateway authentication;
- browser Origin handling;
- WebSocket rebind/resubscribe;
- stale subscription lifecycle;
- root replacement after registration;
- source preview bounds;
- SQLite write escape;
- runtime adapter shell invocation;
- synthetic domain truth;
- third-party source import/provenance;
- MC1 secret handling;
- audit pause integrity.

No Dashboard product repair was made.

## 12. Deferred/non-findings

The following remain intentional incomplete product work rather than new defects at this snapshot:

- the SystemRegistry is in-memory and persisted registry work is explicitly planned for MC6;
- the actual browser/React/Vite shell has not yet been built;
- the local apps/gateway is explicitly temporary scaffolding rather than the canonical AI-Verse Gateway;
- command mutations are intentionally blocked in the scratch local router;
- Full owner-backed Mission Control conversion is MC4 future work;
- native DMG/Tauri packaging is future MC6 work;
- MC1.4 real owner-local proof remains intentionally paused.

These are not represented as completed public-beta features.

## 13. Cross-repository claims for A2

A1.13 records but does not sibling-validate:

- canonical production runtime/session truth should come from AI-Verse Gateway;
- OS owns system/workspace structure and write policy;
- Multiple Bots owns Bot/Worker/Room/Task coordination where defined;
- Automations owns schedules/triggers;
- Token owns canonical usage/cost truth;
- Memory owns canonical durable memory;
- Skills owns capability truth;
- Connections owns credential/external-effect boundaries;
- Brain owns goals/strategy;
- Data owns structured canonical records;
- Apps owns app lifecycle where defined;
- Distribution owns install/release lifecycle.

A2 must verify each corresponding other-side contract.

## 14. Finding summary after A1.13

New:

- WSA-2026-038 HIGH;
- WSA-2026-039 HIGH;
- WSA-2026-040 HIGH;
- WSA-2026-041 MEDIUM;
- WSA-2026-042 MEDIUM.

Global totals after this task:

- BLOCKER: 4;
- HIGH: 20;
- MEDIUM: 8;
- LOW: 9;
- INFO: 1;
- total: 42;
- PROVEN: 42;
- OPEN: 42.

## 15. Evidence limitations

- A1.13 intentionally does not use sibling implementation as proof of sibling-side behavior.
- The current scratch web package is a framework-free model, so no real browser launch exists to run an end-user Origin test.
- Root-replacement finding is proven by direct control flow and path semantics, not by modifying the audited repository or running a destructive filesystem reproduction.
- The real MC1.4 owner-local proof was deliberately not run because the audit gate explicitly forbids it.
- The current merge commit has no directly attached hosted CI run; PR-head CI is recorded exactly rather than relabeled as merge-head CI.
- apps/gateway is known temporary scaffolding, but current executable defects remain findings because the repository preserves and tests that implementation and its laws.

## 16. Definition of done for repair/recheck

For Dashboard to clear current standalone blocking risk after the repair phase:

1. repeated WebSocket workspace subscriptions must fully fence the previous scope;
2. registered system identity must detect/reject approved-root replacement;
3. the local Dashboard Gateway must authenticate read clients if retained;
4. browser Origin policy must support explicitly approved loopback application ports;
5. synthetic owner-domain semantics must be replaced or clearly non-authoritative;
6. isolation/security regressions must run on all supported OSes;
7. no repair may promote Dashboard into canonical owner authority;
8. MC1.4 remains blocked until the whole-system repair gate explicitly releases it.

## 17. Task completion record

**Task:** A1.13 AI-Verse-Dashboard independent repository audit  
**Reviewed ref:** bf6a3a019b07b189c9c701f4edf01e0ded1e7a00  
**System baseline:** 5e923f76dd45433620a5df1138910c7419de70b7  
**Evidence read:** architecture, README, Mission Control PRD/tracker/adoption plan, preservation report, protocol, registry, path adapters, local Gateway, read models, client/web models, live/session/runtime scaffolds, MC1 scripts/tests, provenance, CI and commit/PR history  
**Tests/CI inspected:** registry, read adapters, gateway, isolation, Phase 1, live/runtime, MC1; PR #8 and PR #10 cross-platform CI  
**Claims verified:** read-only path containment, no arbitrary browser roots, fail-closed unknown system behavior, command blocking, system-scoped caches/sessions, third-party pinning, MC1 audit pause  
**Contradictions:** C-A1.13-001 through C-A1.13-005  
**Findings opened:** WSA-2026-038 through WSA-2026-042  
**Negative-space:** Section 11  
**Evidence limitations:** Section 15  
**Verdict:** COMPLETE / DOGFOOD BLOCKED  
**Tracker change:** A1.13 COMPLETE; accepted progress 31/100; A1.14 NEXT  
**Next task:** A1.14 AI-Verse-System meta/release authority
