> **SUPERSEDED IMPLEMENTATION-SEQUENCE NOTICE, 2026-09-15**
>
> This plan is preserved as historical product/architecture evidence. Its ownership, isolation, canonical-Gateway, shared browser/desktop UI, Tauri-host, and multi-system laws remain relevant. Its decision to build the Dashboard shell from scratch is superseded by [DASHBOARD-CANONICAL-MISSION-CONTROL-ADOPTION-PLAN-2026-09-15.md](DASHBOARD-CANONICAL-MISSION-CONTROL-ADOPTION-PLAN-2026-09-15.md), which makes Builderz Labs Mission Control the approved initial shell. Future work must follow the canonical plan when sequencing conflicts.

# AI-Verse Dashboard MVP: Shared Web + macOS Desktop Plan

**Date:** 2026-09-15  
**Status:** Proposed implementation plan for immediate owner dogfood  
**Primary repository to implement:** aiverse-filmmakers/AI-Verse-Dashboard  
**System authority:** this document records product and integration direction only. Canonical ownership remains with the existing component owners.

## 1. Decision summary

Build the smallest useful AI-Verse product shell now.

The first real Dashboard is not a giant control room. It is:

1. one shared React web application;
2. wrapped by a thin Tauri 2 desktop host for macOS;
3. able to select one or more compatible AI-Verse OS folders;
4. able to detect an existing AI-Verse installation without modifying it;
5. able to start or attach to the canonical AI-Verse Gateway for the selected OS;
6. able to authenticate a supported runtime without making Dashboard the credential owner;
7. able to chat through the canonical AI-Verse Gateway inside the selected OS/workspace;
8. able to invoke the canonical Distribution product path when the user explicitly chooses to install AI-Verse into a folder;
9. deliberately minimal in UI so the owner can begin dogfooding AI-Verse immediately;
10. structured so future Bots, Work, Approvals, Automations, Brain, Token, Apps and other panels can be added without replacing the shell.

The first target artifact is a macOS DMG. The same React/Vite frontend must also run in a normal browser.

This supersedes the older Dashboard build-map sequencing assumption that desktop packaging should happen only as a final phase. The owner has now explicitly promoted a thin macOS desktop shell to the immediate product priority.

## 2. Why this is the smallest owner-correct MVP

The current AI-Verse backend is already substantially more complete than its product surface.

The Agent profile already includes:

- AI-Verse OS;
- Brain;
- Memory;
- Skills;
- Data;
- Gateway;
- Automations;
- Multiple Bots;
- Token.

The immediate missing piece is not another backend authority. It is a usable client.

The existing Dashboard repository already contains useful foundations:

- versioned protocol models;
- systemId and workspaceId isolation;
- compatible-OS validation;
- registered-system abstractions;
- read-only filesystem and SQLite adapters;
- typed client scaffolding;
- live session/run models;
- host-independent panel/layout contracts;
- research for a modular desktop shell.

However, it does not yet contain a launchable React application or a native desktop host, and its current local Dashboard gateway remains a projection/query scaffold rather than the canonical AI-Verse runtime edge.

Therefore the fastest correct route is to preserve the useful Dashboard contracts while moving the actual first chat path onto the canonical AI-Verse Gateway.

## 3. Non-negotiable ownership rule

There must be only one canonical runtime/client edge.

The canonical AI-Verse Gateway owns:

- authenticated client sessions;
- runs;
- run checkpoints;
- streamed runtime events;
- bounded control operations;
- live context/session continuity.

Dashboard owns only:

- visual presentation;
- selected-system metadata;
- local presentation preferences;
- disposable caches;
- desktop process supervision metadata;
- secure references needed to connect to the selected local Gateway.

Dashboard must not become a second owner of:

- goals;
- Memory;
- structured Data;
- Skills;
- Bots/Rooms/Tasks;
- Automations;
- Token/cost truth;
- permissions;
- provider conversation truth;
- canonical run state.

The current Dashboard apps/gateway process should therefore be treated as a Dashboard projection service or compatibility scaffold, not as a second runtime Gateway. It should eventually be renamed, narrowed, absorbed behind owner projections, or retired where the canonical Gateway already owns the answer.

Do not deepen the current synthetic health/work/inbox/session semantics that the System audit already identified as shadow authority.

## 4. Recommended stack

### Shared frontend

Keep the current Dashboard TypeScript/npm workspace and add:

- React 19;
- TypeScript;
- Vite;
- Tailwind CSS v4;
- Radix UI or shadcn-style primitives;
- TanStack Query for Gateway-backed server state;
- TanStack Virtual only when long timelines/logs require it.

Do not migrate package managers or introduce a heavier web framework merely for the MVP.

Vite remains preferable to Next.js because the product is a local-first SPA with a separate canonical backend and needs clean desktop wrapping rather than SSR or SEO.

### Desktop host

Use Tauri 2.

Why:

- it wraps the same Vite application used by the browser;
- it provides native macOS windows and DMG packaging;
- it provides a native directory picker with multiple-directory selection;
- it can start or supervise child processes;
- it supports sidecar binaries for a later self-contained build;
- it supports native secure storage options;
- it keeps the desktop-specific layer small instead of embedding another Chromium runtime.

Electron remains a fallback only if a concrete blocker is proven.

### Stable frontend-to-host seam

Introduce a host capability interface rather than scattering Tauri calls through React components.

Conceptually:

~~~text
HostBridge
  capabilities()
  selectSystemFolders()
  registerSystem()
  ensureGateway()
  gatewayStatus()
  installSystem()
  openExternal()
  secureSecretGet()
  secureSecretSet()
~~~

Provide two implementations:

- DesktopHostBridge for Tauri.
- BrowserHostBridge for a normal browser.

The React UI must never care which host it is running under.

## 5. Browser and desktop parity

The product should have one UI, not a browser product and a desktop product.

Shared in both:

- account/runtime status;
- selected AI-Verse system;
- selected workspace;
- chat timeline;
- composer;
- streaming response UX;
- abort;
- session continuation;
- later Bots/Work/Approvals panels.

Desktop-only capabilities:

- native folder picker;
- trusted local root registration;
- automatic Gateway process start/supervision;
- secure local Gateway secret storage;
- invoking Distribution installation;
- future detached native windows/HUDs.

Browser behavior:

- connect to an already-running local or trusted remote AI-Verse Gateway;
- never gain arbitrary filesystem authority;
- never pretend that browser folder APIs are equivalent to trusted OS-root registration.

A capability difference at the host edge is acceptable. The application UI and owner contracts remain the same.

## 6. Multiple AI-Verse folders

The Dashboard should support registering multiple independent AI-Verse OS installations from the beginning.

Each registration keeps:

- stable systemId;
- label;
- canonical local root, host-side only;
- default workspace;
- Gateway home;
- Gateway port/endpoint;
- secure Gateway credential reference;
- optional Distribution home for Dashboard-managed installs;
- last-opened presentation metadata.

The root itself remains privileged desktop-host metadata. Normal UI/Gateway requests use systemId and workspaceId.

### Important current Gateway constraint

The canonical AI-Verse Gateway currently binds one system root in each Gateway configuration.

Do not rewrite Gateway into a multi-root daemon for this MVP.

Instead, supervise one isolated Gateway instance per registered AI-Verse system when required.

Example:

~~~text
System A
  root A
  gateway home A
  gateway token A
  gateway port A

System B
  root B
  gateway home B
  gateway token B
  gateway port B
~~~

Only the selected system needs to be kept running in the smallest implementation. Later, frequently used systems can remain warm.

This preserves the hard isolation already designed around systemId while avoiding a risky canonical-Gateway redesign.

## 7. Existing-folder detection

Reuse and harden the current Dashboard compatible-OS probe.

A selected folder is a compatible AI-Verse OS when it has the expected current architecture signals, including:

- AI-VERSE.yaml;
- supported schema major;
- unified-workspace architecture;
- AGENTS.md;
- operator directory;
- workspaces directory;
- system directory.

Folder handling must be classified into explicit states.

### A. Compatible existing AI-Verse OS

Register it.

Do not rewrite or reinstall it merely because Dashboard opened it.

Then:

1. discover its product/release state where available;
2. resolve its Gateway instance;
3. start or attach to Gateway;
4. run bounded health checks;
5. enter Chat.

### B. Empty/new folder selected for installation

Only after the user explicitly chooses Install AI-Verse:

1. invoke the canonical Distribution path;
2. install an exact admitted release set;
3. use Distribution/owner setup;
4. verify status/doctor;
5. register the resulting OS;
6. start its Gateway;
7. enter Chat.

The canonical install command remains conceptually:

    aiverse start --root <selected-root> --json

Dashboard is a client of Distribution. It is not a second installer.

### C. Partial, incompatible or unhealthy AI-Verse folder

Fail closed.

Show a clear repair/diagnostic state. Do not guess, overwrite files, silently migrate state, or fabricate missing structure.

Where Distribution exposes a safe owner-controlled reconcile path, Dashboard may present that exact action.

## 8. Distribution strategy for multiple managed installs

Distribution currently stores a product receipt under its Distribution home.

For Dashboard-managed independent installations, use an isolated Distribution home per registered system so one system never silently changes another installation receipt.

Do not change Distribution ownership to achieve this. Use its supported environment/configuration boundary where practical.

The MVP should first support existing installations because that is the shortest path to owner dogfood.

The install button can land immediately after that using the same HostBridge.

## 9. Gateway lifecycle on macOS

On Desktop open or system selection:

1. load registered systems;
2. revalidate the chosen OS root;
3. resolve that system's Gateway home and expected endpoint;
4. probe Gateway /health and /status;
5. verify it belongs to the selected system;
6. if healthy, attach;
7. if not running, start aiverse-gateway serve with that system's isolated Gateway home and chosen loopback port;
8. wait for bounded readiness;
9. if startup fails, surface a useful diagnostic instead of silently retrying forever;
10. terminate only a Gateway process the Dashboard itself owns when appropriate.

All child processes must be launched as argv arrays, never interpolated shell strings.

### macOS PATH issue

A packaged macOS GUI application does not reliably inherit the user's interactive shell PATH.

The desktop host must therefore:

- resolve known executable locations deterministically for the first owner build; and
- move toward bundled immutable sidecars for public standalone builds.

Do not make the React renderer responsible for executable discovery.

## 10. ChatGPT / OpenAI authentication

Do not build a new OAuth implementation inside Dashboard and do not store raw ChatGPT credentials in Dashboard state.

For the first owner MVP, use Codex's official rich-client/App Server authentication surface as a provider-runtime adapter candidate because it already supports managed Sign in with ChatGPT flows.

The desired boundary is:

~~~text
Dashboard UI
  -> AI-Verse Gateway
      -> admitted runtime adapter
          -> Codex App Server / Codex auth
              -> Sign in with ChatGPT
~~~

Codex should own its authentication tokens and refresh lifecycle.

Dashboard should only know:

- signed in or signed out;
- account/runtime readiness;
- actions such as begin login or logout;
- model/runtime availability needed for UX.

### Experimental-interface caveat

Codex App Server and some of its transports are currently documented as experimental.

Therefore:

- never make it a canonical AI-Verse architecture dependency;
- isolate it behind the Gateway runtime-adapter contract;
- keep the Dashboard UI unaware of Codex-specific protocol details;
- make the adapter replaceable if the official surface changes.

This lets the first DMG use the most convenient official ChatGPT sign-in path without binding AI-Verse to one provider implementation.

## 11. Secret handling

Desktop renderer JavaScript should not persist Gateway bearer tokens in localStorage or ordinary JSON settings.

For desktop:

- keep the Gateway bearer credential in native secure storage or an equivalent protected desktop secret store;
- keep ChatGPT/Codex auth material owned by Codex;
- pass authenticated Gateway requests through a narrow desktop transport where practical so the bearer credential does not need to be exposed to every React component.

For browser:

- use an explicit connection/auth flow suitable for the already-running Gateway;
- retain loopback/trusted-origin rules;
- never expose filesystem roots as client authority.

## 12. MVP UI

The first usable screen should be deliberately small.

### First run

Show:

- Open AI-Verse Folder
- Install AI-Verse
- recent registered systems, if any

Folder selection may allow multiple folders.

### Main window

Top strip:

- selected AI-Verse system/folder label;
- selected workspace;
- Gateway status;
- runtime/account status.

Main surface:

- chat timeline;
- streaming activity/status;
- composer;
- stop/abort.

Optional small secondary control:

- switch system;
- switch workspace.

That is enough for MVP.

Do not block owner dogfood on:

- Dockview;
- draggable panels;
- Brain graph;
- usage charts;
- automation editor;
- large Control Room page;
- terminal;
- 3D views;
- detached HUDs;
- omnichannel messaging;
- full Bot/Room UI;
- Apps;
- Connections.

The existing panel contracts should remain because these features can be added on the same shell later.

## 13. Future expansion path

Once the chat-first shell is real, add owner-backed surfaces in this order unless a new product priority supersedes it:

1. permanent Bots + temporary Worker activity from Multiple Bots;
2. active work and attention/approvals;
3. Runs and richer live activity;
4. Automations;
5. Token usage/cost;
6. owner-declared Health;
7. Brain goals/graph;
8. Data views;
9. Connections;
10. Apps;
11. advanced docking, detached windows and HUDs.

Every surface must consume an owner contract. Dashboard does not manufacture domain truth merely to populate a panel.

## 14. References to borrow from

Use references selectively, not as wholesale forks.

### Hermes Desktop

Borrow:

- chat-first native composition;
- live tool activity;
- preview rail ideas;
- session continuity.

Do not make Hermes the required runtime.

### OpenClaw

Borrow:

- typed realtime protocol patterns;
- clear client/server boundary;
- activity compression;
- approvals/task UX later.

Do not fork the full monorepo or import its canonical agent model.

### OpenHands

Borrow:

- typed client to runtime separation;
- interchangeable agent/runtime adapter concept.

Do not turn Dashboard into an IDE.

### LifeOS Pulse

Borrow:

- zero-truth projection discipline;
- freshness and health evidence.

Do not let Dashboard-owned projections become canonical.

### Grok Bot and Kylon

Borrow later:

- persistent Bot identity;
- progressive runtime visibility;
- shared work/Room presentation;
- permission/provenance UX.

Do not import their ownership architectures.

### Dockview

Use later for dock/floating/popout layout instead of inventing a docking engine.

### Tauri 2

Use now as the desktop host.

## 15. Implementation slices

The goal is to get to owner dogfood before finishing the broader Dashboard roadmap.

### Slice M0.1: Launchable shared web shell

Implement in AI-Verse-Dashboard:

- real React 19 + Vite app under apps/web;
- reuse protocol/client/shell contracts where correct;
- minimal first-run + chat UI;
- HostBridge contract;
- BrowserHostBridge;
- no direct OS mutations;
- tests and CI.

Acceptance:

- npm command launches the browser app;
- UI can connect to a configured canonical Gateway;
- selected system/workspace remains explicit;
- no Dashboard synthetic domain state is required for chat.

### Slice M0.2: Thin macOS Tauri host

Add:

- apps/desktop or equivalent Tauri wrapper;
- same apps/web frontend;
- native directory picker with multi-select;
- persistent local system registry;
- existing-install validation;
- per-system Gateway process supervisor;
- secure Gateway secret handling;
- development DMG build.

Acceptance:

- launch DMG;
- choose an existing compatible AI-Verse folder;
- app registers it;
- Gateway is running or starts automatically;
- closing/reopening Dashboard preserves registration without changing canonical OS state.

### Slice M0.3: Canonical live chat + ChatGPT login

Add:

- canonical Gateway transport/client;
- streaming chat;
- abort;
- session continuation;
- provider/runtime login status;
- Codex App Server based ChatGPT sign-in adapter behind the Gateway runtime interface, or the nearest official supported equivalent if the interface changes before implementation.

Acceptance:

- click Sign in with ChatGPT;
- complete official login flow;
- return to Dashboard;
- send a message;
- Gateway executes inside the selected AI-Verse system/workspace;
- streamed result appears;
- app restart preserves supported session/account continuity;
- switching to another registered OS never inherits the first system's session context.

This is the first true owner-dogfood finish line.

### Slice M0.4: Install AI-Verse from the app

Add:

- explicit Install AI-Verse action;
- Distribution invocation through argv-safe host command;
- isolated Distribution home per Dashboard-managed system;
- progress/diagnostic events;
- post-install validation and Gateway setup/attach.

Acceptance:

- choose an empty target;
- install exact admitted Agent release/candidate selected by product policy;
- status/doctor pass;
- resulting system becomes registered;
- Chat works without manual terminal setup.

### Slice M0.5: Standalone owner DMG and browser release

Harden:

- bundle or sidecar the minimum immutable bootstrap/runtime assets needed to avoid relying on shell PATH;
- build signed/notarized macOS artifact when public distribution is required;
- ship browser build from the same frontend;
- clean-machine acceptance.

Do not bundle duplicate canonical state into the app.

## 16. Multi-system acceptance gate

Before calling the MVP architecture sound, test two real independent AI-Verse folders.

Required proof:

- two different systemIds;
- two different Gateway homes/tokens;
- no shared runtime session IDs;
- no chat history transfer;
- no Memory/workspace fallback;
- no root leakage to the wrong system;
- switching A -> B -> A restores each system's own client/session state only;
- removing one Dashboard registration does not damage either OS;
- deleting Dashboard presentation state does not damage either OS.

## 17. Security gate

MVP must prove:

- loopback-first Gateway;
- no browser supplied arbitrary local root authority;
- no shell-string process execution;
- no ChatGPT token stored by Dashboard;
- no Gateway bearer token in normal renderer persistence;
- explicit system/workspace scope on every run;
- owner APIs for mutations;
- Distribution for installation;
- fail-closed incompatible folder handling;
- bounded startup/retry behavior;
- secrets redacted from logs and support output.

## 18. Dogfood definition of done

The owner should be able to:

1. download/open the macOS app;
2. select an existing AI-Verse folder;
3. see the app recognize it;
4. have the correct local Gateway available automatically;
5. sign in through the supported ChatGPT/Codex path;
6. choose a workspace;
7. chat with AI-Verse;
8. close the app;
9. reopen it and continue;
10. register a second AI-Verse folder and switch without context leakage.

The MVP is successful at that point even if the rest of the Dashboard is visually sparse.

The product should then grow from actual dogfood friction rather than from speculative panel count.

## 19. Repository impact

### AI-Verse-System

This plan is the canonical current product direction for the immediate Dashboard MVP.

Also update:

- docs/OWNER-PRODUCT-INTENT.md with the desktop/browser MVP priority;
- docs/SYSTEM-CHANGELOG.md with this decision.

### AI-Verse-Dashboard

Implementation should begin only after this plan is accepted.

Expected first changes:

- update BUILD-MAP.md with an MVP-0 track before the broader phases;
- add real React/Vite host;
- add HostBridge abstraction;
- add Tauri desktop app;
- redirect chat/runtime operations to canonical AI-Verse-Gateway;
- preserve existing useful isolation/protocol/layout foundations;
- stop treating the local projection gateway or SessionStore as canonical runtime truth.

### AI-Verse-Gateway

Do not redesign Gateway for multiple roots.

Only add a narrow provider/runtime adapter or capability surface if required for the supported ChatGPT login/runtime path.

### ai-verse-distribution

Do not rebuild installation in Dashboard.

Use Distribution's existing product path. Add only bounded machine-readable behavior if the desktop client demonstrates a concrete missing lifecycle surface.

## 20. External technical references

Current research checked on 2026-09-15:

- Tauri 2 existing frontend integration: https://v2.tauri.app/start/frontend/
- Tauri 2 Vite guidance: https://v2.tauri.app/start/frontend/vite/
- Tauri dialog plugin: https://v2.tauri.app/plugin/dialog/
- Tauri shell/sidecar support: https://v2.tauri.app/develop/sidecar/
- Tauri DMG packaging: https://v2.tauri.app/distribute/dmg/
- Tauri Stronghold plugin: https://v2.tauri.app/plugin/stronghold/
- Codex authentication: https://learn.chatgpt.com/codex/auth
- Codex App Server: https://learn.chatgpt.com/codex/app-server
- Codex App Server authentication: https://learn.chatgpt.com/codex/app-server/authentication

## 21. Final architecture in one diagram

~~~text
                       SAME REACT/VITE UI
                    /                    \
             Normal browser          macOS Tauri DMG
                  |                       |
          BrowserHostBridge       DesktopHostBridge
                  |                 |   |    |
                  |                 |   |    +-> folder picker / install
                  |                 |   +------> Gateway supervisor
                  |                 +----------> secure local secrets
                  |                       |
                  +----------- Gateway transport -----------+
                                      |
                           Canonical AI-Verse Gateway
                                      |
                         selected system + workspace
                                      |
                      OS host / owner component contracts
                                      |
                Brain / Memory / Skills / Data / Bots / etc.
                                      |
                          admitted runtime adapter
                                      |
                       ChatGPT/Codex or other runtime
~~~

The shell is thin. The backend ownership remains deep.

That is the correct tradeoff for the first usable AI-Verse application.
