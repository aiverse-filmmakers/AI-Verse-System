# AI-Verse OS Component Specification

**Component:** AI-Verse OS  
**Repository:** `aiverse-filmmakers/AI-Verse-OS`  
**Reviewed branch:** `main`  
**Review date:** 2026-09-12  
**Role:** canonical host/environment, scope model, ownership model, routing layer, permission floor, extension attachment contract, and user-state filesystem constitution for the AI-Verse system family.

---

## 1. Executive identity

**CURRENT:** AI-Verse OS is a domain-neutral, local-first operating layer for AI-assisted work. It is not a model, an agent, a memory engine, a database, or a dashboard. It provides the environment in which those systems can operate without competing for canonical truth.

Its central idea is:

> One OS. One source of truth. Many isolated workspaces. Reusable capabilities. Connected systems. Automated cadence. Apps on top.

AI-Verse OS v2 uses a Unified Workspace Architecture. It organizes the system around four stronger primitives than profession-specific folders:

1. ownership;
2. scope;
3. lifecycle;
4. authority.

A workspace is the universal isolation primitive. It can represent a project, client, case, practice, product, role, research area, team, course, personal area, or another meaningful scope without changing the fundamental architecture.

**INTENDED:** AI-Verse OS should mature into the host that can discover, attach, activate, reconcile and safely compose independently installable AI-Verse components regardless of reasonable installation order. It should also remain understandable enough that compatible external agents and runtimes can adopt the same contracts without being forced to become AI-Verse OS internally.

---

## 2. Status vocabulary

The OS architecture deliberately separates concepts that are often incorrectly collapsed:

```text
component/package available
!= supported by this OS
!= attached to this OS root
!= enabled
!= healthy
!= initialized for a scope
!= authorized
```

**LAW:** Installation chronology must never determine authority.

**LAW:** Registration never grants workspace visibility, connection access, action permission, approval, or strategic authority.

**LAW:** Health must be checked live rather than stored as permanent truth.

---

## 3. Role in the complete system

AI-Verse OS is the **host and constitution**, not the owner of every capability.

The OS owns:

- architecture and filesystem contracts;
- operator/workspace scope;
- workspace isolation;
- current-context routing while OS owns direction;
- the extension attachment contract;
- capability discovery/resolution;
- the outer action-permission floor;
- user/system/derived ownership boundaries;
- current-context and source-of-truth rules;
- runtime adapter ownership rules;
- component discovery/doctor/reconciliation surfaces;
- the host adapter through which optional components compose.

The OS should become the place where a user or agent can answer:

- What components are available?
- Which are attached here?
- Which are healthy?
- Which scopes are initialized?
- Which source owns this truth?
- Which component should handle this responsibility?
- What can this actor do here?
- What is missing?
- What needs migration?
- Can this component be safely activated now?

The OS should **not** absorb the internals of Brain, Memory, Data, Skills, Apps, Multiple Bots, Connections or Token merely to make integration easier.

---

## 4. Problem the component solves

Without an operating layer, an advanced personal AI stack tends to become a collection of disconnected agents, prompts, databases, tools and folders that:

- duplicate the same context;
- disagree over which fact is current;
- mix user state with system code;
- leak information between projects;
- require the human to reconstruct context repeatedly;
- treat every new domain as a new bespoke architecture;
- let indexes, dashboards and summaries become accidental truth stores;
- give optional plugins more authority simply because they were installed first;
- become impossible to upgrade without overwriting user state.

AI-Verse OS exists to provide durable architectural law around those problems.

---

## 5. Current architecture

### 5.1 Unified Workspace Architecture

**CURRENT:** the root architecture is declared in `AI-VERSE.yaml`.

The major layers are:

```text
SYSTEM
  architecture / schemas / templates / health / built-in capabilities

USER
  operator
  shared knowledge
  workspaces
  connections
  agents
  automations
  apps

DERIVED
  runtime
```

### 5.2 Knowledge lifecycle

AI-Verse distinguishes:

```text
inbox
  -> classify
      -> context
      -> memory
      -> knowledge
      -> decision
      -> capability / automation
      -> archive
```

Receipt is not validation. Raw material does not become canonical truth merely because it arrived.

### 5.3 Routing

The canonical route is:

```text
identify intent
 -> identify scope
 -> resolve direction owner
 -> load ownership-aware current context
 -> choose capability
 -> retrieve minimum required knowledge
 -> resolve connections
 -> execute
 -> validate
 -> write back only when warranted
```

This implements progressive disclosure rather than loading the entire OS into every conversation.

### 5.4 Four Cs

AI-Verse OS evaluates useful operation through:

- Context;
- Connections;
- Capabilities;
- Cadence.

The Four Cs are conceptual capability layers, not four duplicated filesystem trees.

### 5.5 Three Ms

AI-Verse's improvement framework is:

- Mindset;
- Method;
- Machine.

The framework prefers the least complexity that produces dependable results, deterministic logic where sufficient, staged autonomy, explicit source/scope discipline and replaceable modular machinery.

---

## 6. Canonical ownership

### 6.1 System-owned

Examples include:

- `AGENTS.md`;
- `CLAUDE.md`;
- `AI-VERSE.yaml`;
- `system/`;
- `skills/registry.yaml`;
- generated Claude/Codex runtime adapters;
- deterministic OS scripts.

OS updates may evolve these deliberately.

### 6.2 User-owned

Examples include:

- operator profile/context/memory/decisions;
- shared knowledge;
- workspaces;
- connection registry;
- user-defined agents;
- automations;
- apps.

**LAW:** OS upgrades must not casually overwrite these.

### 6.3 Derived

`runtime/` contains disposable/rebuildable state.

**LAW:** if deleting runtime destroys irreplaceable knowledge, that knowledge is in the wrong layer.

---

## 7. Explicit non-ownership

AI-Verse OS must not become a second owner for responsibilities assigned elsewhere.

### Brain

OS does not own active strategic direction after explicit handover to Brain.

### Memory

OS provides canonical memory locations and context rules but does not replace the Memory engine's indexing/recall responsibility.

### Data

OS does not directly open Data's canonical SQLite database from agent/runtime code. Structured Data operations route through the supported Data boundary.

### Skills

OS owns capability resolution, not the external immutable AI-Verse-Skills distribution. External Skills remains independently installed.

### Apps / Dashboard

Interfaces are views/tools over canonical sources. They do not become hidden truth stores.

### Connections

OS defines connection routing/permission context but secrets and external authority remain with the proper connection/credential owner.

### Multiple Bots

OS supplies scope and authority boundaries. Multi-agent coordination must not duplicate OS canonical state.

### Token

OS may consume usage/cost/time intelligence but should not become the telemetry ledger.

---

## 8. Sources of truth

High-level authority:

- runtime behavior -> `AGENTS.md`;
- architecture/paths -> `AI-VERSE.yaml`;
- architecture intent -> `system/architecture/`;
- current context -> ownership-aware current-context resolver;
- workspace identity -> `WORKSPACE.yaml`;
- strategic direction -> OS or Brain according to explicit per-scope ownership;
- decisions -> append-oriented decision history;
- shared curated knowledge -> `knowledge/`;
- workspace knowledge -> workspace-local knowledge;
- connection route metadata -> connection registry;
- derived search/index/cache/dashboard -> never canonical merely because convenient.

**LAW:** a route, index, projection or summary may point to truth but must not silently become a second editable truth.

---

## 9. Runtime model

**CURRENT:** `AGENTS.md` is the canonical runtime contract. Claude/Codex surfaces adapt back to it rather than maintaining independent standing constitutions.

At substantial-work startup, a compatible runtime:

1. reads OS architecture/runtime contracts;
2. loads only relevant enabled extension instructions;
3. resolves scope;
4. resolves strategic direction ownership;
5. resolves current context;
6. selects the smallest relevant capability;
7. retrieves only necessary evidence;
8. executes under current permissions;
9. validates;
10. writes back only durable state.

**LAW:** do not load the entire OS merely because it exists.

---

## 10. Scope and isolation

Scopes include:

- system;
- operator;
- workspace;
- shared.

Workspaces are physically and logically isolated.

Important repair history established that filesystem links must not allow one workspace's private capabilities to leak into another. Requested workspaces, manifests and physical paths are validated before capability discovery.

**LAW:** scope is a technical boundary, not a prompt convention.

---

## 11. Current lifecycle

### 11.1 OS installation

**CURRENT:** the OS ships a cross-platform CLI package.

Development/member-test path:

```bash
npx --yes github:aiverse-filmmakers/AI-Verse-OS install
```

The long-term published path is intended to become:

```bash
npx ai-verse-os install
```

Current CLI includes install, doctor, onboard, update and version surfaces.

### 11.2 Extension attachment

**CURRENT:** optional local extensions register in:

```text
.aiverse/extensions/registry.json
```

This registry is local and gitignored. Normal extension install/update/disable/detach/uninstall must not modify tracked OS files.

### 11.3 Extension states

The release-hardening architecture distinguishes:

- absent;
- available-unattached;
- attached-disabled;
- attached-unhealthy;
- attached-healthy;
- incompatible;
- migration-required.

### 11.4 Components doctor/reconcile

**CURRENT:** release-hardening added OS component doctor/reconciliation planning.

The purpose is to validate attachment state, health/readiness and safe reconciliation without making the OS the owner of component state.

### 11.5 Update

OS update must preserve user-owned state and local attachment state. Optional components should not dirty tracked OS files merely by existing.

### 11.6 Disable/detach/uninstall

The OS contract expects optional components to preserve canonical user state by default. Component-specific detach/uninstall is owned by the component, subject to OS invariants.

---

## 12. Migration and history integration

### 12.1 OS v1 -> v2

**CURRENT:** legacy root paths such as `context/`, `references/`, `decisions/` and `connections.md` are recognized for deliberate migration.

**LAW:** existing user data is preserved. Migration should not create two active editable canonical copies.

### 12.2 Legacy extension integration

Older Memory installation patterns modified tracked `AGENTS.md` and `skills/registry.yaml`.

**CURRENT:** the extension contract defines exact legacy cleanup rules. Only exact recognized old blocks may be removed. Ambiguous/user-modified material is preserved and reported instead of guessed.

### 12.3 Standalone component history

**INTENDED:** when Memory, Data, Brain or another stateful component was used before attachment to an OS, the OS should support explicit discovery and migration/reconciliation without silently importing or deleting standalone canonical state.

**GAP:** there is not yet one universal cross-component migration command covering every standalone/legacy history source.

---

## 13. Intended lifecycle end state

The mature OS lifecycle should be:

```text
component installed anywhere
        ↓
OS discovers compatible component
        ↓
attach/register to this OS root
        ↓
agent/host adopts component for its responsibility
        ↓
initialize or migrate relevant scope/state
        ↓
health check
        ↓
authorize current use
```

This must work whether the OS or component existed first.

### Activation/adoption sequence

**INTENDED:** an existing agent should be able to receive a deliberate instruction such as:

- activate Memory;
- activate Data;
- activate Brain;
- activate Skills;
- reconcile installed components;

and have the host perform the supported setup sequence for that component.

The exact public syntax is not yet fixed. A future `/activate_memory`-style experience is a UX example, not a claim about current commands.

Activation means more than installing files. It means the host acknowledges:

> This component is now the canonical infrastructure for this responsibility, under the existing ownership and authority contract.

No activation may create two canonical owners.

---

## 14. Install-order independence

**LAW:** installation order must not determine correctness or authority.

The release-hardening architecture explicitly targets representative orders such as:

- OS -> Memory -> Brain -> Skills -> Data;
- Skills/Brain packages -> OS -> attach later;
- OS -> Data -> Brain -> Skills -> Memory;
- OS alone -> create host -> add optional components later;
- detach/reinstall stateful components while preserving canonical state.

**CURRENT:** Skills is naturally external and highly order-independent. Local extension registry attachment allows Memory/Data/Brain to converge on an order-independent model.

**GAP:** true "OS installs later into the same already-nonempty root" is not the universal mechanism. The mature solution is package availability plus later attachment/reconciliation, not blindly installing OS over arbitrary existing directories.

---

## 15. Agent/runtime portability

**CURRENT:** the OS has explicit Claude and Codex runtime adapters and a maintained host adapter used by Brain.

**INTENDED:** the OS architecture should remain usable with Hermes and other capable runtimes by exposing stable contracts rather than embedding assumptions about one vendor's agent.

Portable concepts include:

- workspace/scope identity;
- current-context resolution;
- extension registry;
- capability provider contract;
- permission floor;
- host operation boundaries;
- source-of-truth rules;
- component doctor/reconciliation.

A compatible external runtime should be able to consume those contracts without becoming the owner of OS state.

**LAW:** portability must not weaken scope isolation, permissions or canonical ownership.

---

## 16. Sibling integrations

### Brain

OS and Brain have explicit per-scope strategic direction ownership.

Handover is deliberate and provenance-preserving. Brain installation alone never grants direction ownership.

Current release-hardening adds symmetric Brain -> OS handback and blocks Brain detach while Brain owns a scope.

### Memory

OS supplies canonical operator/workspace Memory locations and ownership-aware current context. Memory can index/recall them without becoming strategic authority.

### Skills

External Skills is discovered as an optional immutable provider. OS owns scoped capability resolution and protected aliases.

### Data

Data is an optional local extension. OS routes bounded operations through the registered Data engine/host boundary rather than opening Data databases directly.

### Connections

The generic host exposes bounded connection metadata, never credentials.

### Apps/Dashboard

Apps and Dashboard should consume OS/component projections while respecting canonical ownership.

### Multiple Bots

Bots should receive scopes/capabilities/permissions from the host and return evidence/results rather than create a parallel OS.

### Token

Token should appear as optional telemetry intelligence that OS/Dashboard/agents can query without converting telemetry into canonical operational state.

---

## 17. Permissions, security and privacy

OS owns an outer host permission floor.

Effective execution authority is the intersection of:

- OS permission floor;
- Brain/intelligence policy where present;
- exact approval requirements;
- component-specific readiness/authority.

**LAW:** denial by either OS or intelligence layer blocks execution.

**LAW:** OS `allow` never manufactures approval.

Security architecture includes:

- workspace containment;
- physical symlink/path resolution;
- local extension path validation;
- fail-closed malformed policy/ownership behavior;
- user-owned state gitignored by default in the public template;
- no secrets in repositories;
- stricter human review for high-consequence work.

---

## 18. Failure and degraded modes

Desired and increasingly implemented behavior:

- missing optional Memory -> history unavailable/empty, unrelated host functions work;
- missing Skills -> built-in/local/workspace capabilities remain;
- missing Data -> Data query unavailable, unrelated host functions work;
- missing connections -> bounded empty/unavailable connection result;
- incompatible present component -> dependent capability fails closed with specific diagnosis;
- Brain outage while Brain owns direction -> no silent OS strategic fallback;
- malformed extension registry -> fail closed rather than guessing attachment state;
- malformed workspace/symlink escape -> deny scoped access.

**LAW:** optional absence is not system corruption.

---

## 19. Important historical repairs

### Repair: domain-neutral architecture v2

The OS was generalized away from profession-specific architecture into universal workspace/scope/ownership contracts.

**Permanent lesson:** specialize content and policy, not the fundamental architecture.

### Repair: local extension registry

Optional extensions previously risked modifying tracked OS-owned files.

The local gitignored extension registry created a stable attachment boundary.

**Permanent lesson:** optional integration metadata belongs outside upstream-tracked canonical OS files.

### Repair: runtime adapter ownership

Generated Claude/Codex adapters gained ownership/digest rules.

**Permanent lesson:** generators may replace only content they provably own and that has not been independently modified.

### Repair: strategic direction ownership

OS and Brain previously risked parallel strategic state.

Explicit per-scope direction ownership and handover were introduced.

**Permanent lesson:** exactly one editable strategic owner per scope.

### Repair: capability provider resolution

OS learned to compose built-in, external distributed, personal and workspace capabilities without merging them into one store.

**Permanent lesson:** discovery can unify interfaces without unifying ownership.

### Repair: permission intersection

OS and Brain authorization were made restrictive-by-intersection.

**Permanent lesson:** one permissive layer cannot override another layer's denial or approval requirement.

### Astra repair: cross-workspace capability symlink leakage

Physical workspace boundaries are now validated before private capability discovery.

**Permanent lesson:** logical scope labels are insufficient without filesystem containment.

### Astra repair: frozen OS strategy reactivation

After Brain handover, raw OS strategic context could potentially re-enter active direction.

Ownership-aware current-context resolution now excludes frozen strategy while preserving allowed operational state.

**Permanent lesson:** provenance may survive without retaining authority.

### Astra repair: supported host adapter

Four-component composition moved from CI-only/inlined wiring to a maintained OS host adapter.

**Permanent lesson:** acceptance tests must exercise the supported public integration boundary, not a special test-only architecture.

### Release-hardening: optional-component-aware host

The fixed four-component concept evolved toward a generic OS host whose capabilities expand/contract dynamically.

**Permanent lesson:** optional components should add capability to one host rather than require a new host topology.

### Release-hardening: component doctor/reconcile

Component attachment/health became inspectable without making OS the owner of each component lifecycle.

**Permanent lesson:** orchestration needs system-wide observability, but ownership remains component-local.

### Release-hardening: Brain handback

Direction transfer became symmetric.

**Permanent lesson:** an ownership transfer mechanism needs a safe exit path, not only an entry path.

---

## 20. Inspirations and curated references

### Evidenced internal frameworks

The OS repository explicitly contains:

- the Three Ms framework;
- the Four Cs framework;
- Unified Workspace Architecture;
- Capability Provider Contract v1;
- the 3D Brain capability/application.

These are current AI-Verse design frameworks, not third-party projects.

### External inspirations

**EVIDENCE LIMITATION:** no canonical OS document was found that names a definitive list of external "top similar systems" used to design the OS itself.

Therefore this specification does not invent inspiration names.

The wider AI-Verse product philosophy is intentionally curatorial: compare strong systems in each category, adopt compatible strengths, reject failure modes, and integrate the result under stricter ownership/portability rules. Future research should record external references explicitly so this history is auditable rather than reconstructed later.

### 3D Brain third-party material

The repository includes third-party notices for the 3D Brain application template. Those notices are evidence of third-party implementation material for that capability, but not sufficient evidence that those projects define the OS architecture.

---

## 21. Current gaps and contradictions

### Gap: universal component activation UX

OS has component doctor/reconcile architecture, but there is not yet one uniform end-user activation grammar for every component.

**INTENDED:** agent-friendly activation/reconciliation sequences that can be invoked at any time.

### Gap: universal standalone-state migration

Memory has concrete legacy/standalone migration behavior, but the whole ecosystem does not yet share one universal migration protocol.

### Gap: machine-level component discovery

The release audit considered a machine-level registry such as `~/.aiverse/` for components installed before an OS. The OS-root registry solves attachment, not all machine-level discovery.

### Gap: immutable member release refs

The release-hardening documents require immutable tags/refs. Moving `main` should remain development, not the final member release channel.

### Gap: stale architecture declaration

`AI-VERSE.yaml` still contains a named Memory extension-support section while the generic local extension registry is the broader installation source. This should be clarified so it is not mistaken for a second attachment store.

### Gap: five-component release evidence

The latest release-status document records OS/Brain/Memory/Skills as green while Data's private-repository runner remained the blocker to declaring the five-component beta fully green at that snapshot.

This is release-state evidence, not an OS architectural flaw.

---

## 22. Desired future state

AI-Verse OS should become a portable host constitution with these properties:

1. one simple install command;
2. clear doctor/status/update commands;
3. stable versioned architecture contracts;
4. independently installable optional components;
5. explicit attachment and adoption;
6. order-independent reconciliation;
7. agent-invokable activation/setup;
8. explicit legacy/standalone migration;
9. safe disable/detach/reinstall with user-state preservation;
10. dynamic discovery of newly attached components;
11. one host interface whose capabilities expand as components appear;
12. strong workspace isolation and permission floors;
13. explicit source-of-truth and direction ownership;
14. no direct internal database coupling between components;
15. portable integration for Hermes/Codex/Claude/other compatible agents;
16. immutable release artifacts;
17. system-wide acceptance gates that use the same paths members use.

The OS should feel less like a repository the user manually maintains and more like a self-describing operating environment that an agent can safely understand, diagnose and extend.

---

## 23. Definition of done

AI-Verse OS is mature for the larger vision when:

- installation and update are versioned and reproducible;
- every optional component has a supported availability -> attachment -> activation lifecycle;
- installation order does not determine correctness;
- components installed later are discoverable without rebuilding the host;
- stateful legacy stores have explicit migration routes;
- a user can ask the agent to adopt a new component and the agent can execute the supported setup safely;
- component health and incompatibility are diagnosable;
- permissions, workspace isolation and strategic ownership remain fail-closed;
- user-owned canonical state survives normal software lifecycle;
- the same host contracts work with the wider AI-Verse family and are portable enough for compatible external runtimes;
- acceptance tests exercise real install/member paths;
- no sibling component requires hidden tracked-file edits or private test-only wiring.

---

## 24. Contribution to the supreme AI-Verse vision

AI-Verse OS is the environment that makes the rest of the system coherent.

Brain can become smarter without becoming the filesystem.
Memory can become deeper without becoming current direction.
Data can become richer without becoming Memory.
Skills can grow without becoming the OS.
Bots can multiply without multiplying sources of truth.
Apps and Dashboard can become powerful without owning canonical state.
Connections can expand without granting uncontrolled authority.
Token can observe everything without becoming operational truth.

The OS exists to let all of those capabilities grow independently while still behaving like one system.

---

## 25. Open decisions

1. What should the universal human/agent-facing activation command syntax be?
2. Should AI-Verse maintain a machine-level installed-component registry in addition to OS-root attachment registries?
3. What common migration manifest should Memory, Data, Brain and future stateful components implement?
4. Which components must support standalone mode versus merely package-available/unattached mode?
5. What exact stable host protocol should Hermes and non-AI-Verse runtimes target?
6. When should `AI-VERSE.yaml` remove/clarify the old named Memory support declaration?
7. What immutable version/tag policy becomes mandatory for member releases?
8. Which lifecycle operations belong in `ai-verse-os` versus remaining component-owned commands?
