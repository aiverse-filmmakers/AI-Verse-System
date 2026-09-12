# AI-Verse Dashboard Source Map

**Component:** AI-Verse Dashboard  
**Repository reviewed:** aiverse-filmmakers/AI-Verse-Dashboard  
**Default branch:** main  
**Exact reviewed revision:** c636acf019f76194c40a341bd7985906383f7106  
**Head commit:** Phase 2 Task 5: runtime adapters (reviewed PASS)  
**Head timestamp:** 2026-09-12T17:19:52Z  
**Audit date:** 2026-09-13  
**Method:** AI-Verse-System/docs/AUDIT-METHODOLOGY.md

## 1. Review boundary

This audit was performed from the Dashboard repository itself before consulting AI-Verse-System destination documents.

No sibling AI-Verse repository was audited.

The only sibling integration evidence used is evidence embedded directly in Dashboard, most notably test/registry.test.ts, which contains a developer-local structural probe for /home/hermes/ai-verse-dev/AI-Verse-OS.

## 2. Repository inventory

At the reviewed revision the recursive Git tree contained:

- 69 tracked blobs;
- approximately 373 KB of tracked file content;
- no tracked .github/workflows directory;
- no generated dist directory;
- no node_modules directory;
- no release artifacts;
- no tracked database;
- no tracked native desktop host.

Tracked top-level structure:

    .gitignore
    README.md
    apps/
      gateway/
      web/
    docs/
    package.json
    package-lock.json
    packages/
      client/
      live/
      os-read-adapter/
      protocol/
      read-models/
      registry/
    test/
    tsconfig.json

dist and node_modules are ignored build/dependency outputs rather than canonical source.

## 3. Canonical source classification

### Current executable implementation

- packages/protocol/src/*
- packages/registry/src/*
- packages/os-read-adapter/src/*
- packages/read-models/src/*
- packages/client/src/*
- packages/live/src/*
- apps/gateway/src/*
- apps/web/src/*

### Current package/build metadata

- package.json
- package-lock.json
- tsconfig.json
- workspace package.json files

### Current architecture/product intent

- README.md
- docs/ARCHITECTURE-BLUEPRINT.md
- docs/MODULAR-DESKTOP-SHELL.md
- docs/BUILD-MAP.md

### Inspiration/provenance evidence

- docs/REFERENCE-ADOPTION-MAP.md
- docs/RESEARCH-2026-09.md
- docs/MODULAR-DESKTOP-SHELL.md
- PR #1

### Acceptance/test evidence

- test/protocol.test.ts
- test/registry.test.ts
- test/read-adapters.test.ts
- test/gateway.test.ts
- test/web-shell.test.ts
- test/read-models.test.ts
- test/isolation.test.ts
- test/phase1-gate.test.ts
- test/live-chat.test.ts
- test/live-runs.test.ts
- test/live-activity.test.ts
- test/live-runs-timeline.test.ts
- test/live-adapters.test.ts

### Generated/vendor

No tracked generated or vendored implementation was identified. package-lock.json is dependency lock metadata.

## 4. Root identity evidence

### README.md

High-level claims:

- Dashboard is Layer 5, a visual Control Room.
- Dashboard owns zero canonical domain truth.
- canonical writes go through the selected OS.
- one or more OS installations are isolated by systemId.
- provider/runtime sessions cannot cross systems.
- mandatory surfaces include Now, Chat, Work, Runs, Automations, Inbox, Health, Brain and Usage.
- modular/detachable/HUD direction is part of the product plan.

Evidence classification:
- architecture/product intent;
- not sufficient by itself to prove implementation.

### package.json

Current facts:

- name: @ai-verse/dashboard
- version: 0.1.0-alpha.0
- private: true
- Node >=22
- root scripts only build, test and check
- no start/dev/package/release script
- no React/Vite/Tauri/Electron/Dockview dependency at root

This is strong negative-space evidence that the current repository is a TypeScript library/test scaffold rather than a launchable visual application.

## 5. Architecture documents

### docs/ARCHITECTURE-BLUEPRINT.md

High-value intended laws:

- Dashboard is not a source of truth;
- presentation/configuration/caches may be Dashboard-owned;
- domain state remains owner-owned;
- every operation is explicitly system-scoped;
- browser never receives raw filesystem root authority;
- SQLite is read-only;
- missing state is unavailable, never zero;
- Dashboard must not define 4Cs health meaning;
- owner/core command boundary performs canonical mutation;
- typed protocol must support capabilities, provenance/freshness and reconnect/resync;
- authentication and permissions are required for privileged control;
- no Dashboard domain database by default.

Status:
- canonical intended architecture;
- implementation is only partial.

### docs/MODULAR-DESKTOP-SHELL.md

Recorded intended UI architecture:

- independently mountable panels;
- docked/floating/detached/HUD states;
- explicit scope retained after detachment;
- saved layout metadata only;
- React/Vite remains reusable in future desktop wrapper;
- Dockview candidate;
- Tauri 2 preferred native-wrapper evaluation;
- persistent Bots and Rooms;
- heterogeneous Chat;
- Status -> Preview -> Takeover;
- responsive/mobile from Phase 1;
- visual regression and design-system quality gates.

Status:
- largely contract/plan;
- some TypeScript layout/panel models implemented;
- real windowing/rendering not implemented.

### docs/BUILD-MAP.md

Current ledger:

- Phase 1 tasks 1-8 marked complete;
- Phase 2 tasks 1-5 marked complete;
- Phase 2 Task 6 pending;
- 13 tasks complete;
- repository claims npm run check green at each task;
- total claimed tests at head: 60/60;
- Phases 3-6 pending.

Important audit interpretation:

BUILD-MAP is status evidence, below current code/tests in the evidence hierarchy. Several "complete" labels describe contracts/models rather than the end-user behavior implied by the task names.

## 6. Protocol evidence

### packages/protocol/src/ids.ts

CURRENT enforcement:

- protocol version 1.0;
- systemId/workspaceId/panelId validation;
- full/compact/hud presentations;
- recursive raw-root-key rejection;
- 64 KiB params bound;
- system/workspace cache-scope helpers.

Notable issue:
- global SubscriptionHub events later misuse workspaceScopeKey with an invalid "-" workspace sentinel.

### packages/protocol/src/envelope.ts

CURRENT:

- strict Zod request/response/event frames;
- method-specific system/workspace requirements;
- handshake/capability negotiation structure.

Gaps:

- client does not validate responses through responseSchema;
- subscribe control frames are separate ad hoc WS messages rather than the same versioned protocol;
- no actor/auth identity is present in current request envelope.

### packages/protocol/src/methods.ts

CURRENT:

- 23 named query methods;
- 12 named command methods;
- two protocol methods;
- assertQueryOnly rejects all command methods.

This file is decisive evidence that the current public Gateway is read-only even though the repository stage string says phase-2-live.

## 7. Registry evidence

### packages/registry/src/validation.ts

CURRENT:

- compatible OS structural validation;
- schema major 2;
- unified-workspace architecture expectation;
- manifest/read-only shape checks.

### packages/registry/src/registry.ts

CURRENT:

- in-memory systemId -> root map;
- root canonicalization;
- duplicate/overlap rejection;
- authorized boolean;
- public view excludes root;
- resolveRoot fails closed.

Gaps:

- no persistence;
- auto-generated IDs depend on process-local registration order;
- no public registration UX/API;
- overlap helper is not Windows-safe because it uses "/" literal;
- registered metadata can become stale after revalidate.

### packages/registry/src/selection.ts

CURRENT:

- per-window selection map;
- system ID verification;
- workspace ID syntax validation.

Gaps:

- not persistent;
- not connected to a real window host;
- workspace existence is not checked at selection time.

## 8. Read-adapter evidence

### packages/os-read-adapter/src/path-resolve.ts

Strong CURRENT enforcement:

- server-side registry root resolution;
- fixed workspace boundary;
- relative logical paths only;
- realpath containment;
- traversal/absolute/NUL/symlink escape rejection.

Coupling:
- assumes workspace layout at root/workspaces/workspaceId rather than consuming a versioned owner projection/discovery API.

### packages/os-read-adapter/src/markdown.ts

CURRENT:

- read-only Markdown projection;
- 256 KiB bound;
- SHA-256;
- simple frontmatter;
- no absolute path returned.

### packages/os-read-adapter/src/sqlite.ts

CURRENT:

- Node DatabaseSync readOnly;
- PRAGMA query_only;
- max database size;
- SELECT/WITH/EXPLAIN only;
- bounded rows/params;
- identifier validation.

Boundary limitation:
- only opens a database located inside the selected workspace root.

### packages/os-read-adapter/src/workspace.ts

CURRENT:

- scans workspaces directory;
- reads WORKSPACE.yaml;
- verifies requested workspace ID against manifest.

### packages/os-read-adapter/src/cache.ts

CURRENT intent:
- disposable in-memory per-system projection cache.

Defect:
- projection keys include "proj" before workspaceId, while invalidateWorkspace searches a prefix without "proj"; workspace invalidation does not match projection entries.

## 9. Read-model evidence

### packages/read-models/src/health.ts

Provides a generic health representation, freshness and severity aggregation.

The generic type itself is compatible with owner-declared health.

### packages/read-models/src/work.ts

Provides normalized work-item/read-summary types with scope checks.

### packages/read-models/src/inbox.ts

Provides normalized inbox/action types.

### packages/read-models/src/now.ts

Aggregates focus, work, inbox and health into a bounded "Now" model and can mark focus/health unavailable.

### packages/read-models/src/workspace-sources.ts

This is the most important source-of-truth boundary finding.

CURRENT code hardcodes:

- context/CURRENT.md
- memory/MEMORY.md
- decisions/log.md
- inbox/
- WORKSPACE.yaml

It then invents:

- manifest/context/layers health dimensions;
- objective/next/constraints checks;
- workspace-layer health meaning;
- inbox kind=review and severity=info from filenames;
- inbox createdAt equal to current observation time;
- an empty WorkSummary when no task store exists.

Contradictions:

- architecture says Dashboard must not define 4Cs meaning;
- architecture says missing is unavailable, not zero;
- BUILD-MAP calls Task 6 "4Cs", while current code exposes no 4C owner schema.

## 10. Gateway evidence

### apps/gateway/src/query-router.ts

CURRENT served queries:

- system.list
- system.get
- system.info
- workspace.list
- workspace.get
- workspace.health
- workspace.inbox.list
- task.list
- agent.list
- agent.sessions
- run.list
- run.get
- run.logs
- source.preview

Critical facts:

- every command is blocked first;
- agent.list returns SessionStore summaries;
- task.list returns an empty current WorkSummary;
- run APIs project SessionStore entries;
- source.preview does not effectively read from the cache it populates;
- many protocol query names are not served;
- usage.summary is not served;
- no system.register method exists.

### apps/gateway/src/server.ts

CURRENT:

- HTTP /health;
- HTTP POST /rpc;
- WebSocket /ws;
- binds 127.0.0.1 only;
- non-loopback browser origins rejected;
- WS socket bound to one systemId.

Defects/gaps:

- no authentication;
- loopback Origin comparison rejects normal origins with ports;
- subscribe frames are not protocol-schema validated;
- subscription can be created for an unregistered systemId;
- repeated subscribe on one socket can leave earlier subscription registered because only the latest subId is retained for close;
- /health only proves process availability;
- no product bootstrap/start script.

### apps/gateway/src/subscriptions.ts

CURRENT:

- per-system seq;
- per-system/workspace listener filters;
- one-second payload dedupe;
- filesystem watcher helper.

Defects/gaps:

- optional workspace event uses invalid "-" sentinel in workspaceScopeKey;
- watchWorkspace is a helper, not automatically wired by startGateway;
- invalidation calls the cache method with the prefix defect noted above.

## 11. Client evidence

### packages/client/src/client.ts

CURRENT:

- query-only HTTP client;
- explicit scope;
- system-partitioned client cache;
- request validation before send;
- explicit retarget.

Gaps:

- no command method;
- no WebSocket/subscription client;
- no reconnect/resync;
- no event-driven cache invalidation;
- no responseSchema/version/systemId validation;
- no abort/cancellation signal;
- no stale-age transformation for cached responses.

## 12. Web-shell evidence

### apps/web/package.json

Description explicitly says:

"Framework-free in Phase 1."

No React/Vite dependencies exist in this package.

### apps/web/src/panels.ts

CURRENT:

- panel definitions for Now, Health, Work, Inbox, Usage, Chat, Bots and Runs;
- presentation/capability flags;
- scope metadata.

Negative space:

- no Room panel;
- no Automations panel;
- no Brain panel;
- no Preview panel;
- no rendered components.

Important scope contradiction:
- Usage panel is system-scoped only, but protocol classifies usage.summary as workspace-scoped.

### apps/web/src/layout.ts

CURRENT:

- in-memory panel instances;
- model states docked/floating/detached/hud/hidden;
- explicit system scope;
- preset object save/load.

Gaps:

- no actual docking/window implementation;
- no preset persistence;
- loadPreset does not fully validate stored scope/state/presentation;
- retarget does not fully reapply workspace/panel-scope validation.

### apps/web/src/shell.ts

CURRENT:
- framework-free ShellModel;
- desktop/narrow boolean;
- provenance string;
- loading/empty/error/stale/unknown text.

This is a view model, not rendered UI acceptance.

### apps/web/src/tokens.ts

CURRENT:
- token constants;
- status labels/colors;
- breakpoints;
- component-state vocabulary.

No CSS/theme/DOM implementation is present.

## 13. Live/runtime evidence

### packages/live/src/sessions.ts

CURRENT:
- process-local SessionStore;
- systemId/sessionId keying;
- transcript/status storage;
- bounded history;
- status transitions.

Boundary concern:
- this store is the current source behind agent/run Gateway APIs and cannot become canonical provider/runtime truth.

### packages/live/src/timeline.ts

CURRENT:
- 11 typed timeline kinds.

Documentation says entries are projections, but SessionStore is currently the actual source for them.

### packages/live/src/adapter.ts

CURRENT:
- RuntimeAdapter interface;
- LocalEchoAdapter.

Interface drift:
- architecture proposed subscribe in the adapter contract, current interface has no subscribe method.

### packages/live/src/runtime-adapters.ts

CURRENT:
- descriptor validation;
- AdapterRegistry partitioned by system;
- generic cli-jsonl child-process adapter.

Important findings:

- Claude Code, Codex and ACP are enum/contract names, not specific implementations;
- arbitrary trusted command array can be spawned;
- child inherits process environment;
- adapter sends message/sessionId/systemId but not workspaceId/actor/permission context;
- capabilities reports abort:true;
- active child is not retained and abort does not kill it.

### packages/live/src/activity.ts

CURRENT:
- validates session system/workspace before live publish;
- groups tool entries per session.

### packages/live/src/runs.ts

CURRENT:
- trace and log-drawer views over SessionStore entries;
- bounded pages;
- search/severity helpers.

These are useful UI models, not proof of real external runtime tracing.

## 14. Test evidence

Repository ledger claims 60/60 local tests green at head.

Breakdown from BUILD-MAP:

| Test file | Claimed count | Main evidence |
|---|---:|---|
| protocol.test.ts | 10 | IDs, envelopes, raw-root rejection, command block |
| registry.test.ts | 5 | OS validation, registration, selection |
| read-adapters.test.ts | 6 | Markdown, SQLite, paths, cache |
| gateway.test.ts | 3 | HTTP/WS read path, isolation |
| web-shell.test.ts | 5 | client/layout/shell models |
| read-models.test.ts | 5 | health/work/inbox/Now helpers |
| isolation.test.ts | 8 | cross-system and path isolation |
| phase1-gate.test.ts | 1 | fixture-based Phase 1 story |
| live-chat.test.ts | 4 | SessionStore/timeline/echo adapter |
| live-runs.test.ts | 4 | session-backed agent/run queries |
| live-activity.test.ts | 2 | hub/WS activity |
| live-runs-timeline.test.ts | 3 | trace/log model/cancel state |
| live-adapters.test.ts | 4 | cli-jsonl subprocess adapter |
| **Total** | **60** | repository ledger |

### What tests prove well

- logical system/workspace separation;
- traversal/symlink rejection;
- read-only SQLite;
- protocol shape;
- in-memory scope partitioning;
- local HTTP/WS server behavior from Node clients;
- generic child process round-trip;
- shell/layout model behavior.

### What tests do not prove

- a rendered browser UI;
- actual browser Origin behavior;
- visual regression;
- real docking/popout/native windowing;
- real OS command integration;
- real permission/approval write effects;
- stable persisted registration;
- real Bot/Room state;
- tokens/cost usage;
- production runtime cancellation;
- clean member installation;
- Mac/Windows desktop packaging;
- cross-platform CI;
- clean-checkout isolation from sibling developer state.

### Hidden prerequisite

test/registry.test.ts includes:

    /home/hermes/ai-verse-dev/AI-Verse-OS

and asserts that path validates as a live OS.

That is a developer-machine integration prerequisite inside the default test suite. It prevents the current test suite from being a clean standalone acceptance contract unless that path exists.

## 15. CI and release evidence

### CI

At the reviewed head:

- no .github/workflows files exist;
- GitHub combined commit status contains no statuses;
- fetch of workflow runs for the head returns no runs.

Therefore:

- BUILD-MAP's npm run check green statements are local/developer evidence;
- current head is not GitHub-CI proven.

### Branch protection

Visible branches main and docs/modular-desktop-shell were not protected at review time.

### Releases

GitHub releases collection is empty.

### Packaging

- packages are marked private;
- no start/dev/package/release script;
- no native artifact;
- no immutable member release proven.

## 16. PR and commit history

### Pull requests

Only one visible PR was found.

#### PR #1 - docs: add modular desktop shell architecture

- merged 2026-09-12;
- six commits;
- 1,116 additions;
- documentation/planning only by its own description;
- explicitly preserved zero-truth/system isolation architecture;
- added docking, floating, detached/HUD direction, persistent Bots/Rooms, heterogeneous timeline, responsive/mobile, visual QA and Tauri/Dockview/Hermes/Grok/Kylon research.

No implementation review PRs were found after PR #1.

### Key commit sequence

| Revision | Date | Meaning |
|---|---|---|
| dde97888 | 2026-09-09 | September research |
| 6c53a531 | 2026-09-09 | architecture blueprint |
| b655cf9b | 2026-09-09 | Layer 5 direction |
| f7e2bf66 | 2026-09-09 | adoption/fork plan |
| 7bcf34f7 / 895998cd | 2026-09-10 | multi-OS isolation amendments |
| 0d072574 | 2026-09-12 | modular-shell PR merge |
| 759de6b1 | 2026-09-12 | initial protocol implementation |
| 122afd0a | 2026-09-12 | protocol rework for panel/presentation |
| 18a9587c | 2026-09-12 | read adapters |
| 1cbe1bdf | 2026-09-12 | Gateway |
| 4a33d9f9 | 2026-09-12 | web-shell models |
| bc2c10cb | 2026-09-12 | health/work/inbox read models |
| 9eee68c4 | 2026-09-12 | isolation/security tests |
| a8e9c863 | 2026-09-12 | Phase 1 gate marked complete |
| a7261188 | 2026-09-12 | Phase 2 chat/session slice |
| 38776a3b | 2026-09-12 | agent/run session reads |
| f34dbefe | 2026-09-12 | live activity |
| 8cc50126 | 2026-09-12 | trace/log drawer |
| c636acf0 | 2026-09-12 | runtime adapters |

History is primarily one-day additive implementation rather than a long repair lineage.

## 17. Explicit inspiration/provenance sources

### docs/REFERENCE-ADOPTION-MAP.md

Records ideas to borrow from:

- LifeOS Pulse;
- OpenClaw;
- OpenHands;
- OpenFang;
- TenacitOS;
- Langfuse;
- Phoenix.

Also records deliberate anti-pattern rejection, especially:
- no TenacitOS-style local JSON as Dashboard truth;
- no direct editor authority bypassing OS owners.

### docs/MODULAR-DESKTOP-SHELL.md

Adds:

- Hermes Desktop;
- Grok Bot;
- Kylon;
- Dockview;
- Tauri 2;
- Electron as fallback/reference.

### docs/RESEARCH-2026-09.md

Research baseline for the architecture and product direction.

No evidence reviewed here proves copied implementation code. Licensing must be rechecked if future code is imported. The reviewed repository contains no LICENSE file.

## 18. Contradiction map

| Claim | Conflicting evidence | Classification |
|---|---|---|
| Phase 1 "web shell" complete | apps/web is framework-free TypeScript models, no React/DOM | status overstatement / architecture-vs-operation |
| Phase 1 includes visual QA | no screenshot/DOM/visual tests | missing implementation |
| Task 6 is "4Cs" | workspace-sources invents manifest/context/layers | documentation drift + boundary defect |
| missing state should not be zero | work source missing becomes [] | implementation defect |
| Phase 2 "live agent control" | all Gateway commands blocked | current milestone incomplete |
| Chat commands flow through OS | no command forwarding implementation | gap |
| agent.list | returns chat session summaries | taxonomy/ownership defect |
| typed timeline is a projection | SessionStore currently owns the timeline state | temporary architecture contradiction |
| saved layouts | savePreset returns in-memory object only | implementation only partial |
| detached panel | only enum/state transition, no window | contract only |
| abort capability true | CLI child is not killed by abort | implementation defect |
| browser localhost Gateway | Origin with port rejected | implementation defect |
| disposable cache invalidation | workspace prefix does not match projection key | implementation defect |
| optional workspace event | "-" sentinel invalid under workspace schema | implementation defect |
| stable systemId | process counter resets/reorders | lifecycle defect |
| Usage panel system-scoped | usage.summary protocol is workspace-scoped | unresolved contract ambiguity |
| npm run check green as portable gate | one default test requires developer-local OS path | acceptance defect |

## 19. Evidence limitations

- The audit inspected current repository source, tests, architecture docs, tree, commits, PR #1, GitHub statuses and workflow runs through the GitHub connector.
- No sibling repository was audited.
- The test suite was not independently executed from this environment because the working runtime could not clone GitHub over network. Current 60/60 status is therefore a repository-ledger claim supported by test source, not a newly reproduced run.
- No GitHub CI exists to substitute for that independent run.
- Whether another AI-Verse component currently exposes all required owner projection/command APIs remains external/unverified by design of this Dashboard-only audit.
- Negative claims are scoped to the reviewed revision and repository tree.
