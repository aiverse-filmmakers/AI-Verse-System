# AI-Verse Dogfood, UX and Platform Completeness Plan

**Status:** Canonical product-readiness and dogfood plan  
**Date:** 2026-09-13  
**Purpose:** Stop the endless audit loop, start real usage, and make future platform expansion deliberate instead of blocking.

This document answers four practical questions:

1. What can be used now?
2. What is the minimum interface needed to use it daily?
3. What platform layers must AI-Verse eventually cover to compete with mature agent systems?
4. Which missing layers block personal dogfood, closed beta, public beta, or later production?

The core rule is:

> A future improvement does not make a previously passed milestone "unfinished" unless it breaks that milestone's explicit acceptance contract.

AI-Verse must use release gates, not an infinite definition of "perfect."

---

## 1. Readiness vocabulary

Do not ask only whether a repository is "100% finished."

Use these states:

| State | Meaning |
|---|---|
| ENGINE READY | Core component logic works and its own tests pass |
| INTEGRATION READY | Supported current-generation owner boundaries work |
| DOGFOOD READY | Bogdan can install it through a documented path and use it safely for real work |
| CLOSED-BETA READY | A non-developer can install/use it with bounded support and no manual repo surgery |
| PUBLIC-BETA READY | Security, onboarding, update/recovery, distribution and real product-path acceptance meet the public gate |
| PRODUCTION READY | Multi-user/remote/enterprise-scale security, operations and support expectations are satisfied where claimed |
| FUTURE / EXPERIMENTAL | Useful direction that does not block an earlier passed gate |

### Stopping rule

Once a release gate passes on immutable artifacts, later audits may create future work but must not revoke the passed gate merely because a better architecture is imaginable.

A passed gate may be revoked only by evidence such as:

- a reproducible acceptance failure;
- a security vulnerability that violates the gate's threat model;
- data loss/corruption;
- authority or workspace isolation failure;
- documented install path no longer working;
- incompatible current-generation integration;
- release artifact not matching the evidence used to pass the gate.

"Could be nicer," "could be more generic," "could support another runtime," or "could add another feature" does not revoke a passed dogfood release.

---

## 2. What is usable now

### Five-component first-member beta

**CURRENT: DOGFOOD READY as a frozen technical beta.**

The frozen set is:

| Component | Frozen revision |
|---|---|
| AI-Verse OS | `89fb9043ec58c05931d477ef3e154df428a06c22` |
| AI-Verse Brain | `bef8261ad35d126d29aeff5d496f46904125b7b6` |
| AI-Verse Memory | `f5b417f9e7ce1b3f05bc80d10a483d10f6ad10ee` |
| AI-Verse Skills | `3ab838e6e64561bbb7cea8f85d0ebc75b9e84337` |
| AI-Verse Data | `189b13264ab86115d2f21fee3ba8cd5a8dac6581` |

Canonical install guide:

- AI-Verse-OS `docs/FIVE-COMPONENT-BETA-INSTALL.md`

The release acceptance has already proven:

- exact immutable refs;
- OS-only operation;
- late optional-component discovery;
- representative install-order independence;
- Memory recall through the composed host;
- immutable external Skills resolution;
- bounded Data query through the host;
- Connections metadata discovery without credential exposure;
- Data disable/update/re-enable with data preservation;
- Brain direction ownership and explicit handback;
- Brain, Memory and Data detach/reinstall without canonical state loss;
- component doctors;
- no tracked OS mutation by optional component lifecycle.

This is enough to begin real personal usage.

It is not a claim that the entire ten-component end state is complete.

### Multiple Bots

**CURRENT: ENGINE + INTEGRATION READY through Phase 4, not DOGFOOD PRODUCT READY.**

Phase 0 through Phase 4 are complete.

Phase 4.9 passed:

- 417/417 full repository tests;
- 5/5 dedicated compatibility/evaluation tests.

Current next gate:

- Phase 5.1 simple install command/package.

Multiple Bots should not block five-component dogfood. Add it after its Phase 5 install/onboarding/health surface is ready, or use it only as an advanced development component.

### Token

**CURRENT: strong engine, not yet required for the first dogfood loop.**

Token's local alpha accounting/telemetry engine is substantial, but turnkey activation, collection, cost-aware primary reads, host authorization and normal released distribution remain incomplete.

Do not block daily AI-Verse usage on Token.

### Dashboard

**CURRENT: foundation only, not the current way to start using AI-Verse.**

Do not wait for the final Dashboard before dogfooding.

### Apps

**CURRENT: architecture seed.**

Does not block dogfood.

### Connections

**CURRENT: architecture seed.**

Does not block local five-component dogfood. It does block the eventual claim of a generic secure external-action platform.

---

## 3. Current component installation and adoption model

The word the product should use is **adopt**.

Internally, adoption may mean attach, initialize, dynamic discovery or migration depending on the component.

### OS

Install the frozen OS, then initialize the person/system through onboarding.

Current surfaces include:

`ai-verse-os onboard`

and runtime-specific onboarding capabilities such as Claude Code `/onboard` and Codex `$onboard`.

### Brain

Current adoption:

```text
install package
-> attach to OS
-> initialize Brain state
-> optionally hand strategic direction to Brain
```

The release path uses:

`ai-verse-brain attach <OS_ROOT> --apply`

`ai-verse-brain init <OS_ROOT> --apply`

Strategic ownership remains a separate explicit transaction.

### Memory

The frozen installer:

- installs the engine;
- installs runtime adapters;
- attaches Memory;
- initializes the derived index;
- runs doctor.

Existing standalone Memory migration remains explicit.

### Skills

Skills intentionally does not need an OS attachment record.

Current adoption:

```text
install immutable generation
-> OS discovers provider dynamically
-> runtime pins generation before use
```

This is the correct model for a permission-neutral external provider.

### Data

Current adoption:

```text
install Data runtime
-> attach/register to OS
-> explicitly initialize Data for a selected workspace
```

Installation must not create databases in every workspace.

### Target unified user UX

The user should eventually be able to say or run:

```text
AI-Verse, install and adopt Memory.
AI-Verse, add Data to my Client X workspace.
AI-Verse, add Brain but do not give it strategic control yet.
```

or use a single product command family such as:

```text
aiverse component install <name>
aiverse component adopt <name>
aiverse component status <name>
aiverse component disable <name>
aiverse component enable <name>
aiverse component detach <name>
aiverse component doctor <name>
aiverse reconcile
```

The unified command is an orchestration UX over owner-controlled component lifecycle operations, not a reason to move component ownership into OS.

---

## 4. Start using AI-Verse now

### Immediate interface

Use the frozen five-component beta inside a currently supported capable runtime.

The lowest-friction current choices are:

1. Claude Code opened at the AI-Verse OS root.
2. Codex opened at the AI-Verse OS root.

The current OS already has first-class onboarding/capability surfaces for these runtimes.

The first dogfood objective is not to prove a beautiful UI.

It is to prove:

- AI-Verse remembers useful history correctly;
- workspaces help rather than create friction;
- Skills are selected usefully;
- Brain direction/verification improves work;
- Data is useful for current structured facts;
- component boundaries stay invisible during ordinary use.

### Do not build the full Dashboard first

The Dashboard should be informed by real usage.

A large UI built before dogfood risks encoding the wrong navigation, concepts and workflows.

### Next interface MVP

Build the smallest **AI-Verse Agent Gateway / Shell** that turns the five-component system into one conversational endpoint.

Its first version should:

- accept a normal user message;
- bind the current system/workspace/user;
- invoke the selected runtime/agent;
- make Brain, Memory, Skills and Data available through existing owner boundaries;
- stream the response and tool activity;
- expose approvals;
- expose run state and cancellation;
- return structured status/receipts;
- expose an OpenAI-compatible agent endpoint where practical.

Then use an existing frontend such as Open WebUI as the temporary web interface.

This tests the AI-Verse backend and UX before investing in the final native Dashboard.

### Long-term interface architecture

```text
                     AI-Verse canonical components
                              |
                       AI-Verse host/gateway
                              |
          +-------------------+-------------------+
          |                   |                   |
     Native Dashboard     Open WebUI         CLI / IDE
          |                   |                   |
     desktop/browser       temporary UI      Claude/Codex
          |
     mobile/channels
```

Hermes, Codex, Claude Code and other compatible agents/runtimes are execution clients/hosts, not the canonical owner of AI-Verse state.

The final native Dashboard can replace the borrowed UI without replacing the underlying AI-Verse system.

---

## 5. Progressive onboarding: the "grandma test"

### Product requirement

A new user should not need to understand:

- Brain;
- Memory;
- Data;
- Skills;
- Bots;
- Connections;
- MCP;
- workspaces;
- canonical truth;
- capability leases.

The system should reveal concepts only when useful.

### First-use target

Within a few minutes the user should reach a useful outcome.

First-run should ask only what is necessary to begin safely.

A good default flow is:

1. What would you like help with first?
2. Where should I work / what sources may I access?
3. What kinds of actions should I always ask before doing?

Then begin helping.

The existing deeper onboarding questions remain useful, but they should not all be a mandatory barrier before first value.

### Progressive learning contract

While working, AI-Verse may gather evidence and propose structure.

Examples:

```text
Repeated client work detected
-> propose a Client workspace

Stable preference detected
-> propose Memory/profile update

Repeated workflow detected
-> propose a Skill

Repeated structured records detected
-> propose a Data Space/schema

Recurring responsibility detected
-> propose an Automation

Durable specialist role detected
-> propose a Bot

Complex one-off task detected
-> use temporary Worker(s) rather than create permanent Bots
```

### Invisible complexity

Normal users should experience:

> "It learns how I work and becomes more useful."

They should not experience:

> "Please choose which canonical subsystem should own this datum."

Advanced users may inspect the architecture, provenance and decisions.

### Progressive autonomy

Start conservative.

The system learns both the user and the user's desired autonomy level over time.

Suggested modes:

- Guided: ask before meaningful changes/actions.
- Balanced: auto-handle low-risk reversible operations, ask for consequential changes.
- Trusted: broader bounded autonomy within explicit scopes.

The underlying permission system remains authoritative. A UI mode is not itself a permission grant.

---

## 6. Agent runtime / loop contract

AI-Verse currently uses external runtimes and component-specific execution paths. The mature platform still needs one explicit **host/runtime loop contract** so every supported runtime proves equivalent safety semantics.

The host loop contract should cover:

1. message/task intake;
2. system + workspace + identity resolution;
3. context assembly;
4. Brain/goal orientation where applicable;
5. Memory recall;
6. capability/Skill discovery and readiness;
7. model selection;
8. tool/connection selection;
9. pre-action authorization;
10. tool execution;
11. result validation;
12. owner-routed durable writes;
13. checkpoint/persistence;
14. continuation or stop decision;
15. completion verification;
16. receipts/traces/cost attribution.

Required controls:

- stable run ID;
- stable task/session identity;
- maximum loop steps;
- token/cost budget;
- wall-clock deadline;
- concurrency ceiling;
- cancellation;
- pause/resume;
- retry policy;
- idempotency for side effects;
- checkpointing around externally visible effects;
- crash recovery where the runtime claims durability;
- deterministic stop reason;
- human approval interrupts;
- no-progress/loop detection;
- context compaction without silently changing canonical truth.

### /goal

A user-facing `/goal` or natural-language equivalent should be a UX surface over Brain-owned intent/objective machinery, not a second goal database.

Examples:

```text
/goal get my portfolio ready by Friday
/goal status
/goal pause
/goal change deadline Friday -> Monday
/goal done
```

The same actions should work through natural language.

---

## 7. MCP and protocol interoperability

MCP must become a first-class supported interoperability surface.

### AI-Verse as MCP client

AI-Verse should be able to consume approved external MCP servers for tools/resources without every capability becoming a native Connection implementation.

Ownership:

- Connections owns external connection/auth/liveness.
- Skills may describe reliable workflows using MCP capabilities.
- OS/host owns scope and outer permission policy.
- the runtime invokes tools through bounded capabilities.

### AI-Verse as MCP server

AI-Verse should be able to expose selected bounded capabilities to compatible external agents through MCP without exposing raw internal databases or credentials.

Owner APIs remain behind the MCP projection.

### MCP admission/security

An MCP server or tool must not be trusted merely because it speaks MCP.

Required controls should include:

- explicit server admission;
- server identity/origin;
- auth issuer binding;
- per-server and per-tool allowlists;
- capability mapping;
- tool metadata/version fingerprint;
- tool-list change detection;
- permission review on broadened capabilities;
- structured output validation where feasible;
- untrusted tool-result labeling;
- prompt-injection/tool-poisoning defenses;
- privilege separation between untrusted external tools and high-privilege internal tools;
- outbound network restrictions where appropriate;
- approval for sensitive external effects;
- rate limits/budgets;
- audit/receipt provenance.

### A2A

A2A remains the preferred external agent-to-agent protocol for Multiple Bots interoperability.

Production A2A exposure must keep transport identity/authentication separate from model-provided actor text and apply authorization to every operation/resource.

---

## 8. Security baseline

Security is a release dimension, not a final polish task.

### Personal local dogfood minimum

For the current single-user local threat model:

- local/loopback control surfaces by default;
- no unauthenticated remote administrative exposure;
- workspace/path/symlink containment;
- no raw credentials in Memory, prompts, logs or canonical Data by design;
- destructive/external actions require current authorization;
- bounded loops and budgets;
- preserve canonical data during install/update/uninstall;
- immutable release refs;
- component doctor checks.

### Before remote or closed-beta exposure

Add or prove:

- authenticated human/client identity;
- protocol actor mapping;
- secure session management;
- CSRF/CORS/origin policy for browser clients;
- TLS or an authenticated secure tunnel for remote exposure;
- rate limits and abuse ceilings;
- secrets backend / OS keychain / encrypted broker;
- scoped opaque credential handles;
- audit trail for privileged actions;
- sandbox/tool isolation profiles;
- browser/network SSRF controls;
- prompt-injection trust labels and external-content boundaries;
- MCP server/tool admission;
- package/Skill/App provenance and supply-chain admission;
- security audit command;
- backup/restore drills;
- dependency vulnerability scanning;
- safe update/rollback path.

### Before broad public/production claims

Where applicable:

- multi-user identity;
- RBAC/ACL;
- tenant/workspace isolation tests;
- OIDC/SSO and enterprise identity only if product scope needs it;
- account recovery/session revocation;
- privacy/export/delete controls;
- security event logging;
- red-team/regression suite;
- remote gateway hardening;
- key rotation;
- disaster recovery;
- security update policy;
- disclosure/security policy.

### Security law

Do not rely on the model's system prompt to enforce a permission.

The execution boundary must enforce it.

---

## 9. Self-improvement without unsafe self-modification

AI-Verse should improve itself, but improvement must be a controlled promotion pipeline.

### Improvement loop

```text
observe real work
-> detect friction/repetition/failure
-> propose improvement
-> identify canonical owner
-> create candidate version
-> test/evaluate in isolation
-> compare against current version
-> require approval according to risk
-> promote atomically
-> monitor
-> rollback/compensate if regression appears
```

### What may improve

Examples:

- Skills;
- prompts/instructions;
- workspace structure;
- Data schemas through explicit migration;
- Brain strategy rules within allowed evolution bounds;
- Bot role definitions;
- automations;
- app versions;
- model routing preferences.

### What must not silently self-modify

- permission floors;
- credential policy;
- authority ownership;
- security gates;
- approval requirements;
- canonical migration rules;
- immutable audit history.

### Time-based reflection

A 3-5 minute reflection interval may be useful as a trigger during long work, but elapsed time alone must not cause automatic promotion.

Better triggers include:

- repeated failure;
- repeated manual correction;
- repeated workflow;
- task completion;
- verified performance regression;
- explicit user request;
- scheduled maintenance window.

### Skill improvement

Skills should support:

- candidate edits;
- diff/review;
- isolated evaluation;
- versioned immutable generation;
- promotion;
- rollback;
- provenance explaining why the Skill changed.

An agent may propose and test its own Skill improvement. It should not silently overwrite the stable production Skill.

---

## 10. Platform completeness checklist

This checklist prevents "unknown unknowns" from being rediscovered randomly in future audits.

Status vocabulary:

- STRONG: substantial current implementation.
- PARTIAL: real implementation exists but system-level product contract is incomplete.
- INTENDED: architecture exists, implementation not complete.
- GAP: not yet a clear first-class system contract.

| Platform layer | AI-Verse state |
|---|---|
| canonical ownership/source of truth | STRONG |
| workspace isolation | STRONG |
| Brain/goals/verification | STRONG core |
| historical Memory | STRONG core |
| structured Data | STRONG core |
| Skills/package generations | STRONG core |
| multi-agent coordination | STRONG engine, product install pending |
| capability leases/budgets/cancellation | STRONG in Multiple Bots |
| external Connections | INTENDED |
| Apps/plugin platform | INTENDED |
| Dashboard/control room | PARTIAL |
| telemetry/cost | STRONG engine, operationalization pending |
| unified install/adopt/reconcile UX | PARTIAL |
| agent runtime loop contract | GAP/PARTIAL across runtimes |
| durable run checkpoint/resume contract | PARTIAL |
| MCP client | INTENDED/PARTIAL in component research, not system-complete |
| MCP server | GAP |
| A2A | STRONG in Multiple Bots interoperability |
| generic OpenAI-compatible agent endpoint | GAP as AI-Verse product surface |
| model/provider abstraction and fallback | PARTIAL/runtime-specific |
| terminal/computer/browser execution | external runtime responsibility today |
| scheduler/cadence execution | NEEDS OWNER |
| triggers/webhooks/events | PARTIAL/FUTURE |
| notifications/channels | FUTURE |
| authenticated remote gateway | PARTIAL in Multiple Bots, system product GAP |
| human identity/authentication | GAP at system product level |
| multi-user RBAC/ACL | FUTURE/GAP |
| SSO/OIDC/SCIM | FUTURE if needed |
| secrets/credential broker | INTENDED via Connections |
| sandbox execution | runtime-specific, no universal AI-Verse contract |
| prompt-injection trust model | GAP as explicit system contract |
| MCP/tool poisoning defenses | GAP as explicit system contract |
| security audit command | GAP |
| dependency/supply-chain security | PARTIAL |
| package/skill/app admission | PARTIAL/INTENDED |
| approval policy | STRONG foundations, fragmented UX |
| owner-routed durable writes | PARTIAL |
| audit/provenance/receipts | STRONG foundations, fragmented |
| tracing/run observability | PARTIAL |
| eval/regression framework | PARTIAL by component, no unified platform gate |
| red-team/security evals | GAP |
| backup/export/import | STRONG in Data, mixed system-wide |
| disaster recovery | PARTIAL |
| update/rollback | PARTIAL |
| progressive onboarding | GAP beyond current fixed intake |
| accessibility/non-technical UX | GAP |
| natural-language system administration | INTENDED |
| self-improvement promotion pipeline | PARTIAL across Brain/Skills, system contract GAP |
| Skill improvement UX | GAP/PARTIAL |
| goal UX such as /goal | GAP as shell command, Brain primitives exist |
| mobile/messaging clients | FUTURE |
| offline/local deployment | STRONG direction |
| remote/VPS deployment | PARTIAL, security gate required |
| privacy/export/delete | PARTIAL |
| release channels/version compatibility | PARTIAL, five-component beta is frozen |

This table is not a demand to implement every row before dogfood.

It is the platform coverage map.

---

## 11. Competitive benchmark lessons

The product-completeness model was cross-checked against current public architecture/documentation for:

- OpenClaw;
- Open WebUI;
- Hermes Agent;
- Letta;
- OpenHands;
- LangGraph;
- MCP;
- A2A;
- OWASP Agentic AI guidance.

Important patterns worth adopting:

### OpenClaw

- persistent Gateway;
- explicit serialized agent loop;
- channel clients;
- per-agent tool policy;
- configurable sandboxing;
- security audit;
- loopback-first Gateway exposure;
- separation of Gateway control plane and agent tools.

### Open WebUI

- polished chat shell independent from agent backend;
- RBAC and resource ACLs;
- MCP/OpenAPI extension surfaces;
- automations;
- subagents;
- server-side tool loop;
- existing-agent connection through OpenAI-compatible APIs.

### Hermes

- broad toolsets;
- MCP discovery;
- skills;
- memory;
- delegation;
- cron;
- messaging channels;
- command/memory/skill write approval concepts.

### Letta

- persistent agent state;
- explicit tool rules;
- required-before-exit and loop-control rules;
- per-tool approvals;
- client-side tool pause/resume;
- continual-learning direction.

### OpenHands

- risk-scored action confirmation;
- pluggable security analyzers;
- approval/reject/resume flow;
- sandboxed execution patterns.

### LangGraph

- durable checkpoints;
- pause/resume;
- fault tolerance;
- human interrupts;
- state inspection;
- subagent persistence choices.

### MCP and A2A

- standard interoperability;
- explicit transport/auth boundaries;
- long-running task semantics;
- protocol evolution/versioning;
- least-privilege authorization.

### OWASP agent guidance

AI-Verse threat modeling must explicitly include:

- prompt injection;
- tool abuse/privilege escalation;
- data exfiltration;
- Memory poisoning;
- goal hijacking;
- excessive autonomy;
- approval manipulation;
- cascading multi-agent compromise;
- denial of wallet/unbounded loops;
- sensitive-data leakage;
- supply-chain compromise;
- MCP tool poisoning.

---

## 12. Release gates from now on

### Gate D0 - Bogdan dogfood

**Goal:** use AI-Verse for real work now.

Must have:

- frozen five-component install;
- doctors green;
- at least one supported runtime;
- no remote unauthenticated exposure;
- one real workspace;
- Memory recall;
- one useful Skill;
- one Data use case;
- Brain tick/goal flow usable;
- state survives restart/reinstall where claimed.

Future Dashboard, Apps, Connections, Token and Multiple Bots product polish do not block D0.

### Gate D1 - AI-Verse Shell MVP

Must have:

- one conversational endpoint;
- workspace switching;
- run state;
- cancellation;
- approvals;
- Brain/Memory/Skills/Data composition;
- current health summary;
- OpenAI-compatible endpoint or equivalent client contract;
- basic authentication if exposed beyond loopback.

This is the recommended next product build.

### Gate B1 - closed non-developer beta

Add:

- one-command installer/bootstrap;
- progressive onboarding;
- secure remote access path;
- recovery/update path;
- security audit;
- safe secret handling;
- minimum sandbox/tool policy;
- exact release artifacts;
- support bundle/diagnostics;
- no repo editing required.

### Gate B2 - expanded AI-Verse

Add productized:

- Multiple Bots;
- Token;
- Connections;
- channels;
- deeper automations.

### Gate P1 - native product shell

Complete:

- native Dashboard/web/desktop shell;
- owner-backed projections;
- authenticated commands;
- detachable surfaces as designed;
- Apps host surface.

### Gate P2 - public platform

Add whatever public product scope actually promises:

- Apps platform;
- broad Connections;
- MCP client/server;
- multi-user identity/RBAC if applicable;
- package admission;
- red-team/security gates;
- public distribution;
- versioned compatibility and migration.

---

## 13. Recommended immediate implementation order

Do not start another broad architecture cycle.

1. Install the frozen five-component beta in a clean dogfood root.
2. Use it in Claude Code or Codex for real work.
3. Keep a friction log from actual usage.
4. Implement only blockers revealed by D0 use.
5. Build the small AI-Verse Shell/Gateway.
6. Connect Open WebUI as a temporary UI.
7. Productize Multiple Bots Phase 5 after the shell can consume it.
8. Add Token observability.
9. Implement Connections with security first.
10. Finish the native Dashboard from observed user behavior.
11. Build Apps on the stable owner/gateway contracts.

---

## 14. Definition of a successful first dogfood week

The first week is successful if the user can forget most component names and simply work.

Measure:

- number of real tasks completed;
- times the system needed manual repository intervention;
- wrong/stale Memory recalls;
- unnecessary questions;
- useful retained knowledge;
- repeated workflows that should become Skills;
- structured information that should become Data;
- runtime/permission friction;
- actions that should have required approval but did not;
- actions that asked approval unnecessarily;
- crashes/restarts and recovery quality;
- latency/cost;
- concepts the user had to understand that should have stayed invisible.

Those observations should drive the next build more than another unconstrained architecture audit.

---

## 15. Canonical product principle

The platform can be technically deep while the user experience stays simple.

The desired experience is:

> Tell AI-Verse what you want. It knows the relevant context, remembers useful history, structures durable facts, chooses capabilities, asks when risk matters, improves repeated work, creates specialist help when justified, and keeps the underlying complexity out of the way.

The internal architecture remains inspectable for advanced users and developers.

The default user should not have to operate it like an infrastructure engineer.


---

## 16. Benchmark-first feature design

AI-Verse should not invent important agent behaviors from a single user idea or a single reference implementation.

When a desired feature already exists elsewhere, the required design process is:

1. identify the concrete feature requested;
2. inspect the original implementation that motivated the request;
3. inspect the strongest comparable implementations in other serious systems;
4. identify shared primitives, control surfaces, persistence model, failure modes, security tradeoffs and UX;
5. separate copied convention from AI-Verse-specific ownership constraints;
6. design the AI-Verse version as a synthesis of the strongest compatible patterns;
7. record which systems influenced each adopted choice;
8. build only after the comparison is complete.

Examples that require this process include:

- persistent goals / `/goal`;
- self-learning and self-improving Skills;
- post-turn/background reflection;
- memory learning;
- agent loops;
- cron/heartbeat/cadence;
- subagents and durable Bots;
- MCP usage;
- approval models;
- sandboxing;
- remote gateways;
- onboarding;
- skill marketplaces/workshops.

Current benchmark examples:

- persistent goals: Codex Goal mode, Hermes Persistent Goals, OpenClaw Goal;
- self-learning: Hermes background review + curator, OpenClaw Skill Workshop/self-learning, Letta self-editing memory/skills/harness;
- durable runtime loops/checkpoints: OpenClaw agent loop, LangGraph persistence/interrupts, Codex/Hermes goal loops;
- Skills governance: Hermes Skill approval/curator, OpenClaw Workshop proposal/auto modes, Letta learned/pre-made Skills.

This is a methodology rule, not a requirement to copy implementation code or licensing-restricted source.

## 17. Unified installation and adoption UX

The internal component architecture may remain modular and independently versioned while the user experiences one product.

The target public UX is:

```text
install AI-Verse once
-> run setup
-> choose a profile such as Core / Full / Custom
-> installer fetches exact compatible component versions
-> components install through their own owner-controlled lifecycle
-> AI-Verse adopts/initializes them
-> one final doctor/readiness check
-> start working
```

A future distribution command may resemble:

```text
aiverse install
aiverse setup
```

or one bootstrap command that installs the AI-Verse CLI and launches setup.

Component-level expert commands should still follow one consistent wrapper vocabulary where applicable:

```text
aiverse component install <name>
aiverse component adopt <name>
aiverse component status <name>
aiverse component doctor <name>
aiverse component enable <name>
aiverse component disable <name>
aiverse component detach <name>
aiverse component uninstall <name>
aiverse component migrate <name>
```

The wrapper delegates to each component's canonical lifecycle. Not every verb must apply to every component.

For example:

- Skills may use dynamic discovery rather than attachment;
- Data initialization is workspace-specific;
- Brain strategic handover remains separate from ordinary adoption.

### Distribution architecture

Do not require a monorepo merely to achieve one-line installation.

Preferred direction:

```text
AI-Verse distribution/meta-package
          |
          +-- pins compatible OS
          +-- pins Brain
          +-- pins Memory
          +-- pins Skills
          +-- pins Data
          +-- optionally Multiple Bots / Token / Connections / Apps / Dashboard
```

This preserves independent component development, rollback and portability while hiding installation complexity from normal users.

A physical monorepo may still be chosen later for developer-maintenance reasons, but it should not be necessary for the user experience.
