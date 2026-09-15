# AI-Verse Dashboard Canonical Mission Control Adoption Plan

**Date:** 2026-09-15  
**Status:** CANONICAL GO-AHEAD PLAN  
**Product owner decision:** use Builderz Labs Mission Control as the initial visual/application shell, while AI-Verse remains the canonical architecture and source of truth.  
**Implementation repository:** `aiverse-filmmakers/AI-Verse-Dashboard`  
**Upstream UI baseline:** `builderz-labs/mission-control@5483a0e1eef15b467c167e95796791112cedbb7c`  
**AI-Verse Dashboard baseline:** `c636acf019f76194c40a341bd7985906383f7106`  
**AI-Verse Gateway baseline at decision:** `0ccd7ea16d4931c71a9b978f6bd96d690d4d9173`

## 1. Authority

This document is the canonical Dashboard implementation direction until the product owner explicitly supersedes it.

Future chats and agents must not restart the older Dashboard roadmap, choose a different shell foundation, or resume the old "desktop last" sequence merely because an older document still exists.

Older Dashboard plans are retained as historical design evidence. Their ownership, isolation, security, and source-of-truth laws remain valid unless this plan explicitly changes them. Their sequencing and shell-foundation decisions are superseded where they conflict with this document.

## 2. Final decision

Start from the Builderz Labs Mission Control product shell and adapt it into AI-Verse.

Do not replace AI-Verse architecture with Mission Control architecture.

Mission Control is initially:

- the launchable visual shell;
- a source of mature UI components and operator workflows;
- an MIT-licensed implementation donor where direct reuse is appropriate;
- a temporary compatibility host while AI-Verse owner-backed projections replace Mission Control-owned domain state.

AI-Verse remains authoritative for:

- OS and workspace authority;
- Brain goals, intent, strategy, evaluation and learning;
- Memory;
- Data;
- Skills;
- Multiple Bots, Workers, Rooms, Threads, Team Runs and coordination;
- Automations;
- Connections and external credential/execution boundaries;
- Token telemetry, pricing and cost truth;
- Gateway sessions, runs, checkpoints, runtime events and bounded controls;
- Distribution and installation lifecycle.

The Dashboard owns presentation, local UI preferences, selected-system metadata, disposable caches, desktop process-supervision metadata, and secure references needed to reach the canonical owners.

## 3. Why this supersedes the prior shell decision

The previous Dashboard research correctly protected AI-Verse ownership, but it chose to build the visual shell from zero.

The new product decision is to preserve those ownership laws while using a mature launchable shell to accelerate dogfooding.

This changes:

- shell bootstrap strategy;
- implementation order;
- desktop timing;
- visual-component source.

This does not change:

- zero-shadow-authority law;
- systemId/workspace isolation;
- owner-routed writes;
- canonical AI-Verse Gateway;
- explicit permissions and approvals;
- owner-routed Memory, Data, Skills, Bots, Automations, Connections and Token truth;
- browser and desktop sharing one product UI.

## 4. Fastest safe first proof

Before deleting or stripping anything from Mission Control, prove that its existing task-dispatch path can talk through the real AI-Verse runtime edge.

Mission Control already supports a generic OpenAI-compatible local provider.

AI-Verse Gateway already exposes the OpenAI-compatible path:

`POST /v1/chat/completions`

Therefore the first proof is:

~~~text
Mission Control UI
        |
        | local OpenAI-compatible provider
        v
AI-Verse Gateway :8787/v1
        |
        v
selected AI-Verse system + workspace
        |
        v
OS owner boundary + sibling component owners
        |
        v
admitted runtime
~~~

For a local development proof, Mission Control can be configured conceptually as:

~~~text
LOCAL_LLM_ENDPOINT=http://127.0.0.1:8787/v1
LOCAL_LLM_API_KEY=<AI-Verse Gateway bearer token>
dispatchModel=local/aiverse
~~~

Mission Control strips the `local/` prefix before sending the model name, so the Gateway receives `aiverse`.

This path is for proving the shell and task-dispatch runtime route only. Stock Mission Control does not route its main /chat page through this generic local-provider path. It does not authorize Mission Control's SQLite task, agent, memory, schedule, cost or integration stores to become AI-Verse truth.

## 5. Prototype before strip

The first implementation phase must keep the upstream Mission Control feature set visible long enough to perform a feature-by-feature disposition audit.

Every Mission Control surface receives one of four dispositions:

1. **PROJECT**: UI reads and controls an existing AI-Verse owner.
2. **ADOPT**: capability is genuinely useful and missing, so add it to the correct AI-Verse owner and surface it in Dashboard.
3. **PRESENTATION-ONLY**: keep the UI/interaction idea but replace Mission Control's backend/state with an AI-Verse projection.
4. **STRIP**: capability is irrelevant, redundant, unsafe, or conflicts with AI-Verse ownership.

No feature is removed merely because AI-Verse does not currently expose it.

## 6. Existing AI-Verse Dashboard work is preserved

Do not discard the current AI-Verse Dashboard repository.

The following work remains valuable and should be reused behind or inside the Mission Control-derived shell:

- versioned protocol contracts;
- stable `systemId` and `workspaceId` scope model;
- system registration and validation;
- read-only filesystem/SQLite projection code where still owner-correct;
- isolation and traversal/symlink tests;
- typed client contracts;
- panel registry;
- layout and presentation contracts;
- full/compact/HUD presentation model;
- live activity normalization;
- run timeline/log models;
- runtime-adapter interfaces;
- multi-system separation tests.

Current Dashboard-local synthetic health/work/inbox semantics and process-local session authority remain scaffolding and must not be promoted.

## 7. Canonical migration sequence

### Phase MC0: preserve and baseline

- pin the exact Mission Control upstream commit;
- preserve all prior AI-Verse Dashboard plans as historical;
- record third-party license/provenance;
- do not delete current Dashboard code;
- run Mission Control unmodified as a reference instance.

### Phase MC1: AI-Verse runtime dispatch proof

- run one real AI-Verse Gateway;
- point Mission Control's OpenAI-compatible local provider at it;
- create and dispatch a task whose agent uses `dispatchModel=local/aiverse` and verify it traverses Mission Control -> Gateway -> selected AI-Verse OS/workspace -> runtime -> Mission Control;
- verify Gateway authentication and system/workspace scope;
- do not use Mission Control domain stores as AI-Verse truth.

Exit gate: a real Mission Control task can execute through canonical AI-Verse Gateway with no duplicate runtime owner.

### Phase MC2: first-class AI-Verse mode

Create an explicit AI-Verse adapter/mode rather than leaving the integration disguised as a generic local LLM.

It must surface:

- selected AI-Verse system;
- selected workspace;
- Gateway health/readiness;
- Gateway run/session state;
- streaming events;
- cancel/pause/resume/approval capabilities;
- owner provenance.

Mission Control-specific provider/runtime assumptions become replaceable adapters.

### Phase MC3: feature parity and disposition

Use the canonical Mission Control feature-gap map in AI-Verse-Dashboard.

For every panel/API/workflow:

- identify current Mission Control owner;
- identify correct AI-Verse owner;
- determine whether AI-Verse already has it;
- if missing, decide whether to implement it;
- only then project, adopt, or strip.

No mass deletion before this gate is complete.

### Phase MC4: AI-Verse native shell conversion

Progressively replace Mission Control domain state with AI-Verse owner-backed projections.

Priority order:

1. system/workspace/Gateway;
2. Chat and Runs;
3. Bots/Workers/Rooms/Tasks;
4. Attention/Approvals;
5. Automations;
6. Token usage/cost;
7. Memory and Skills;
8. Connections/integrations/webhooks/channels;
9. Health/doctor/security;
10. Brain;
11. Apps/Data and advanced surfaces.

### Phase MC5: desktop

Wrap the same product UI for macOS using Tauri 2 unless a concrete blocker proves Electron is necessary.

Desktop adds:

- folder picker;
- registered-system persistence;
- one isolated Gateway supervisor per registered AI-Verse system when needed;
- secure Gateway credential storage;
- Distribution install action;
- native windows/HUD later.

Browser remains the same UI connected to an already-running Gateway.

## 8. Mission Control state rule

Mission Control's local SQLite may remain temporarily for shell-local compatibility while the port is in progress.

It must not become canonical AI-Verse state for:

- tasks;
- Bots/agents;
- Memory;
- schedules;
- costs/tokens;
- integrations;
- approvals;
- run/session continuation;
- workspace truth.

As each surface is adopted, replace or bypass that Mission Control store with an owner-backed AI-Verse projection/command path.

If a temporary compatibility record must exist, mark it explicitly disposable and derivable.

## 9. Third-party code rule

Builderz Labs Mission Control is MIT licensed at the pinned baseline.

Before copying or adapting source:

- preserve required copyright/license notices;
- record imported/adapted files in `THIRD_PARTY_NOTICES.md`;
- prefer copying modular UI/presentation components over importing canonical domain ownership;
- keep an upstream pin so later audits know exactly what was used.

GawkBot remains a UX/product reference only unless separate commercial permission is obtained. Its Sustainable Use License is not an acceptable default source-code basis for a distributed/commercial AI-Verse product.

## 10. Product target

The finished product should feel simpler than Mission Control and more job-oriented like GawkBot, while retaining a full control room beneath it.

Default user experience:

~~~text
AI-Verse
  Chat / Ask AI-Verse
  Workspaces
  Recent work
  Needs you
~~~

Advanced Control Center:

~~~text
System health
Gateway
Bots / Workers / Rooms
Tasks / Runs
Approvals
Automations
Memory
Skills
Connections
Usage / Cost
Security / Audit
Logs
Brain
Apps / Data
~~~

The beginner does not need to understand component architecture. The advanced user can inspect it.

## 11. Finish line

The Dashboard foundation decision is complete when:

- the official plan is recorded in System and Dashboard;
- older contradictory plans are visibly marked historical/superseded;
- Mission Control can route a real task dispatch through canonical AI-Verse Gateway;
- the complete feature-disposition map exists;
- no Mission Control domain store has silently become AI-Verse authority;
- the adopted shell can select a real AI-Verse system/workspace;
- future implementation continues from this track rather than returning to the old scratch-built sequencing.

After that, implementation proceeds feature by feature from the disposition map.
