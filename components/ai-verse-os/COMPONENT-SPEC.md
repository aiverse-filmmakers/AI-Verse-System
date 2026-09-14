# AI-Verse OS Component Specification

**Component:** AI-Verse OS  
**Repository reviewed:** `aiverse-filmmakers/AI-Verse-OS`  
**Reviewed branch:** `main`  
**Reviewed head:** `3bb28154748f693ba2fd7f5473cc086ddc9d975f`  
**Fresh standalone review:** 2026-09-13  
**Evidence rule:** this version was rebuilt from AI-Verse-OS alone. Earlier AI-Verse-System summaries were not treated as source evidence.

---

## 1. Executive identity

**CURRENT:** AI-Verse OS is a domain-neutral, local-first operating layer for AI-assisted work.

**Current accepted evidence head:** `156f15f162c6d63159b54d3ad87e0342ec7cf9aa` (includes Invisible Intelligence owner routes and progressive Memory bridge).  

It is best understood as the **host constitution** of the AI-Verse family. It defines where truth lives, how work is scoped, how optional components attach, which source has authority, which capability may be selected, which permissions constrain action, and how user-owned state survives system evolution.

Its public design principle is:

> One OS. One source of truth. Many isolated workspaces. Reusable capabilities. Connected systems. Automated cadence. Apps on top.

The phrase "operating system" here does not mean a kernel or replacement for macOS/Linux/Windows. It means a persistent architecture and host contract for AI-assisted work.

**LAW:** OS should coordinate specialized systems without absorbing their canonical responsibilities.

**INTENDED:** the mature OS should feel like a self-describing AI environment that can discover, attach, activate, migrate, diagnose and compose optional components in any reasonable order, while remaining portable enough for capable runtimes such as Claude Code, Codex, Hermes and future hosts.

---

## 2. The problem AI-Verse OS solves

Without an operating layer, an AI stack tends to fragment into:

- large prompts containing everything;
- duplicated context in multiple agents;
- one-off project folders with different rules;
- hidden app-local truth;
- vector indexes mistaken for canonical data;
- memory that silently overrides current context;
- agent-specific capability copies;
- plugins that edit each other's files;
- no clear source when two systems disagree;
- no safe upgrade boundary between system code and user state;
- no principled workspace isolation;
- no consistent permission floor;
- no durable lifecycle for optional components.

AI-Verse OS exists to make those failure modes structurally difficult rather than relying on the model to remember not to cause them.

---

## 3. Product philosophy

### 3.1 Domain neutral core

**CURRENT:** architecture v2 deliberately removed profession-specific assumptions from the universal root.

A doctor, filmmaker, developer, researcher, founder, student, household, legal matter or unknown future domain should start from the same architecture.

**LAW:** specialize content, vocabulary, policies and local workflows, not the fundamental OS architecture.

### 3.2 Workspace first specialization

New domain-specific structure begins inside the workspace that needs it.

Only proven reusable knowledge or capabilities should move upward.

### 3.3 Progressive disclosure

Do not load everything simply because it exists.

The runtime should resolve scope first, then current context, then only the deeper knowledge, memory, connections and capabilities required for the task.

### 3.4 Evidence over presence

A connection entry is not proof of access.

A capability folder is not proof that it executes.

An automation file is not proof that cadence actually runs.

A dashboard is not proof that its displayed data is authoritative.

The `/audit` capability explicitly scores verified operation rather than folder count.

### 3.5 Least necessary complexity

The Three Ms framework pushes the system toward:

- eliminate before automate;
- deterministic operations where possible;
- focused AI responsibilities;
- staged autonomy;
- explicit validation;
- replaceable machinery;
- scoped permissions;
- kill switches.

---

## 4. Unified Workspace Architecture

**CURRENT:** AI-Verse OS v2 is organized around four dimensions:

1. **Ownership** - who may edit which state.
2. **Scope** - system, operator, shared or one workspace.
3. **Lifecycle** - inbox, context, memory, knowledge, decision, capability, archive.
4. **Authority** - which source wins when sources disagree.

The architecture is declared machine-readably in `AI-VERSE.yaml` and explained under `system/architecture/`.

---

## 5. Canonical layer model

### System-owned

Examples:

- `AGENTS.md`
- `CLAUDE.md`
- `AI-VERSE.yaml`
- `system/`
- `skills/registry.yaml`
- deterministic OS scripts
- generated runtime peers owned by OS

These may evolve through OS updates.

### User-owned

Examples:

- `operator/`
- `knowledge/`
- user workspaces
- connection registry
- agent definitions
- automations
- generated/custom apps

These must not be casually overwritten by OS updates.

### Derived

`runtime/` contains rebuildable state such as caches, indexes, logs, reports and generated ownership ledgers.

**LAW:** if deleting `runtime/` destroys irreplaceable truth, that truth was stored in the wrong layer.

---

## 6. Privacy and local-first meaning

**CURRENT:** the public template gitignores user-owned state by default.

This includes operator information, user workspaces, shared user knowledge, connection registries, user agent definitions, automations, local extension state, direction coordination state and most runtime state.

Therefore:

> local-first does not mean all user truth is committed to Git.

The public repository tracks contracts, examples and templates. Personal/organizational state is local unless the operator deliberately chooses another version-control policy.

---

## 7. Workspace model

A workspace is the universal isolation primitive.

It may represent:

- a project;
- role;
- case;
- client;
- practice;
- product;
- research area;
- team;
- course;
- study;
- personal area;
- custom domain unknown to the template.

Every substantial workspace has `WORKSPACE.yaml`.

The workspace schema keeps `type` and `domains` free-form rather than enforcing an industry taxonomy.

### Workspace responsibilities

A workspace should identify:

- identity and purpose;
- status;
- owners;
- source routes;
- current context;
- privacy constraints;
- approval policy;
- relevant connections;
- local capabilities;
- automations.

**LAW:** workspace-specific facts, memory, knowledge and capabilities stay local unless deliberately promoted.

---

## 8. Knowledge lifecycle

AI-Verse OS distinguishes information by meaning.

```text
incoming material
    ↓
inbox
    ↓
classify
    ├─ current context
    ├─ memory/history
    ├─ durable knowledge
    ├─ decision
    ├─ source route
    ├─ capability / automation candidate
    └─ archive / discard
```

### Context

What matters now.

### Memory

What happened and may matter later.

### Knowledge

Reusable validated understanding.

### Decision

What was settled, why and under which constraints.

### Capability

Repeatable execution.

### Archive

Historical material that must not silently override current truth.

**LAW:** receipt is not validation. Raw material does not become canonical truth merely because it arrived.

---

## 9. Capability taxonomy

The OS makes an important distinction between kinds of reusable machinery.

| Need | Preferred artifact |
|---|---|
| current state | context |
| historical event | memory |
| reusable understanding | knowledge |
| settled choice | decision |
| repeatable human method | SOP/knowledge |
| reusable artifact shape | template |
| deterministic file/API/data operation | script |
| repeatable AI-guided judgment | skill |
| coordination across capabilities | agent |
| schedule/event-driven reliable work | automation |
| persistent human interface | app |

**LAW:** not every useful thing should become an agent.

**LAW:** agents coordinate capabilities and context. They should not become giant duplicate knowledge stores.

---

## 10. Built-in capabilities

The canonical built-in capability sources live under:

```text
system/capabilities/
```

Current foundation capabilities include:

- `onboard`
- `workspace`
- `grill-me`
- `link`
- `audit`
- `level-up`
- `3d-brain`

The runtime-neutral registry is `skills/registry.yaml`.

Claude and Codex trees are generated runtime peers:

- `.claude/skills/`
- `.agents/skills/`

They are not intended to be parallel editable sources.

---

## 11. Runtime adapter ownership

**CURRENT:** `scripts/sync-runtime-adapters.mjs` synchronizes canonical OS capabilities into runtime-specific peers.

It records exact OS-owned generated files and last-generated SHA-256 digests under:

```text
runtime/adapters/os-owned.json
```

A generated file may be replaced only when ownership and last-generated bytes prove it is safe.

Unknown files and locally modified generated files are preserved and reported as conflicts.

Symlink/path escape cases fail closed.

**LAW:** a generator may replace only output it can prove it owns and that has not been independently modified.

This rule protects extension adapters and user-created runtime capabilities from OS synchronization.

---

## 12. Runtime startup model

`AGENTS.md` is the canonical runtime behavior contract.

For substantial work, a compatible runtime is expected to:

1. read `AI-VERSE.yaml`;
2. read `AGENTS.md`;
3. inspect relevant enabled local extensions;
4. identify scope;
5. resolve strategic direction ownership;
6. load ownership-aware current context;
7. choose the smallest relevant capability;
8. retrieve only required knowledge/memory/assets;
9. resolve required connections;
10. execute at the lowest reliable autonomy level;
11. validate;
12. write back only durable state.

**LAW:** runtime adapters should point back to one standing contract rather than each maintaining a full independent constitution.

---

## 13. Source-of-truth model

High-level authority:

- runtime behavior -> `AGENTS.md`
- architecture and paths -> `AI-VERSE.yaml`
- architecture intent -> `system/architecture/`
- workspace identity -> workspace `WORKSPACE.yaml`
- current state -> ownership-aware current-context resolver
- strategic direction -> OS or Brain according to explicit owner
- decisions -> scoped decision history
- workspace knowledge -> workspace `knowledge/`
- cross-workspace knowledge -> root `knowledge/`
- live external facts -> verified live source where appropriate
- indexes/apps/dashboards/summaries -> derived views only

When sources conflict:

1. identify scope;
2. resolve direction owner;
3. compare authority and timestamp;
4. prefer the narrower applicable canonical source;
5. preserve provenance;
6. do not silently merge incompatible claims;
7. surface consequential ambiguity.

---

## 14. Strategic direction ownership

**CURRENT:** OS and Brain share a strict one-owner-per-scope model.

Each scope has:

```text
direction_owner = os
or
direction_owner = brain
```

Durable local coordination lives in:

```text
.aiverse/direction/ownership.json
```

### OS-owned direction

OS onboarding/workspace/level-up may edit strategic direction.

### Brain-owned direction

Brain intent becomes canonical.

Existing OS strategic files remain as provenance but are frozen.

The OS current-context resolver removes frozen strategic sections from active context and retains only allowed operational sections plus Brain refs/view.

A Brain outage does **not** return ownership to OS.

### Handback

Current architecture supports explicit Brain -> OS export and handback.

Brain detach must be blocked while any scope is Brain-owned.

**LAW:** exactly one editable strategic owner per scope.

**LAW:** provenance may survive without retaining authority.

---

## 15. Ownership-aware current context

`scripts/current-context.mjs` is more than a convenience reader.

When OS owns a scope, it returns normal OS current context.

When Brain owns a scope, it:

- validates direction ownership;
- removes OS strategic sections;
- excludes arbitrary unknown headings from active direction;
- preserves allowed operational state;
- includes valid Brain references;
- reports missing/invalid Brain view instead of falling back to old OS strategy;
- rejects symlink/path escape.

This is a central runtime safety boundary.

---

## 16. Capability provider architecture

**CURRENT:** OS can discover four provider classes:

1. `os`
2. `aiverse-skills`
3. `local`
4. `workspace:<id>`

Qualified IDs preserve provider identity.

Examples:

```text
os:onboard
aiverse-skills:whisper
local:my-helper
workspace:film:shot-check
```

Protected OS aliases cannot be captured by another provider.

For non-protected exact bare names, the preference order is:

1. active workspace;
2. local personal;
3. distributed AI-Verse Skills;
4. OS.

Explicit qualified requests never silently fall back to another provider.

---

## 17. Capability integrity vs readiness

This distinction is critical.

**CURRENT:** capability discovery verifies things such as:

- provider/generation structure;
- manifest hash;
- package membership;
- package digest;
- provider identity;
- path containment;
- workspace authorization;
- package integrity.

But discovered candidates currently report:

```text
readiness: UNVERIFIED
permission: unknown
approval: not_required
```

That is intentional.

**GAP:** AI-Verse OS does not yet expose one generic live readiness engine that verifies runtime dependencies, connection usability and contextual execution prerequisites for every capability.

**LAW:**

```text
discovered
!= ready
!= permitted
!= approved
!= executed successfully
```

This must remain explicit in future UI/Dashboard/agent behavior.

---

## 18. Action permission boundary

OS owns an outer host permission floor.

Current decisions:

- `allow`
- `approval_required`
- `deny`

Default operator/workspace floors include:

- external actions -> confirm
- destructive actions -> confirm
- high-stakes decisions -> human-review

Operator and workspace values intersect by strictness.

Paused or archived workspaces deny action execution.

Malformed policy fails closed.

### Important boundary

For local classes such as `read_local`, `write_local_reversible` and `modify_canonical_state`, OS may have no additional floor. A higher intelligence/component policy may still be stricter.

**LAW:** OS allow never manufactures approval or overrides another layer's denial.

**LAW:** effective authority is restrictive intersection, not privilege union.

---

## 19. Connections

Connections are routes to external systems/sources.

The registry stores safe metadata such as:

- id;
- mechanism;
- status;
- scope;
- safe authentication description;
- authority/use.

It must not store secrets.

### Current host behavior

The dynamic host adapter can return bounded, scoped connection metadata.

### What OS does not currently provide

**GAP:** OS is not a universal connection execution engine.

A registry entry says how/where a source exists, not that a generic OS process can authenticate and operate it.

Actual access may be provided by a runtime, plugin, CLI, API adapter, MCP-like system or another component.

**LAW:** registration is not proof of live access.

---

## 20. Automations and Cadence

`automations/` defines the architecture for:

- jobs;
- triggers;
- policies.

Definitions are user-owned.

The architecture expects:

- scope;
- trigger/schedule;
- authoritative inputs;
- capability;
- permission;
- validation;
- retry/failure behavior;
- output;
- approval/kill switch.

### Current implementation reality

**CURRENT OWNERSHIP:** OS deliberately does not become the universal scheduler. AI-Verse Automations is the canonical cadence/schedule/trigger owner. OS supplies scope, permission and owner-routing boundaries that Automations must re-check; a file under `automations/` is still not treated as proof of execution.

The accepted Agent release proves real Automations delivery, and Invisible Intelligence G/H additionally prove that recommendation-only behavior creates no recurring state while direct recurring consent reaches the canonical Automations owner.

---

## 21. Agents

`agents/` is an orchestration architecture layer.

Agents should coordinate:

- context;
- capabilities;
- scripts;
- connections;
- approvals.

**GAP:** base OS does not contain one generic full agent-execution engine for arbitrary user agent definitions.

Brain is a separate intelligence component and the OS host can integrate with it.

This is consistent with OS non-ownership, but the distinction should be explicit in product language.

---

## 22. Apps

Apps are persistent interfaces/tools built on top of the OS.

**LAW:** important canonical state remains in the appropriate owner rather than becoming app-only truth.

The included 3D Brain is the strongest concrete app example.

It visualizes selected real sources but is deliberately derived.

Deleting the visualization must not delete the knowledge it represents.

---

## 23. 3D Brain

The `3d-brain` capability:

- discovers approved local source paths;
- lets the user choose categories;
- scaffolds a local app under `apps/3d-brain/`;
- builds a real graph from source notes;
- preserves explicit Markdown/wikilink connectivity;
- does not invent connections/chronology;
- keeps app-local visualization derived from canonical sources;
- binds to localhost;
- has concrete verification requirements.

This is both a capability and a reference implementation of the rule:

> apps may visualize truth without becoming truth.

---

## 24. Optional extension registry

Local attachment state lives under:

```text
.aiverse/extensions/registry.json
```

The registry is gitignored.

Current semantics distinguish:

- supported;
- installed;
- enabled.

Health is live.

Unknown top-level fields and sibling extension entries must be preserved by writers.

Paths are repository-relative and must remain inside the OS root.

**LAW:** optional extension lifecycle must not normally edit tracked OS files.

**LAW:** registration grants no workspace visibility, connection permission, approval or Brain authority.

---

## 25. Component doctor

Current command:

```text
ai-verse-os components doctor
```

Current known local-extension component IDs are hardcoded:

- `ai-verse-brain`
- `ai-verse-memory`
- `ai-verse-data`

External Skills is checked separately.

The doctor can identify states such as:

- absent;
- available-unattached;
- attached-enabled;
- attached-disabled;
- incompatible;
- Skills available-active/inactive.

It also diagnoses the shared extension-registry lock and never steals/deletes it automatically.

### Limitation

**GAP:** this is not yet a fully generic registry-driven component framework.

Adding future components such as Token or another extension requires OS component-manager awareness unless the implementation is generalized.

### Health depth limitation

The current doctor primarily proves:

- registration shape;
- safe engine/instruction paths;
- some local installation evidence;
- Skills active-generation structure.

It does not run every component's deep health suite.

Therefore:

```text
attached-enabled
!= fully healthy
```

---

## 26. Reconciliation

Current command:

```text
ai-verse-os components reconcile
```

**CURRENT:** reconcile supports both a deterministic plan and a deliberately narrow apply mode. The plan remains owner-aware. Apply executes only owner actions explicitly admitted by OS; the accepted automatic path is Brain attach/init when the exact owner CLI is available. Registry locks, migration-required states and non-automatic owner actions remain fail-closed.

Distribution's `aiverse start` consumes this contract and revalidates the exact plan before using it for bounded self-heal.

### Remaining scope

There is still no universal arbitrary `activate <component>` transaction that may invent lifecycle semantics for every future component. Broader activation/migration remains owner-specific and must preserve canonical ownership. That is now a breadth/release-train gap, not evidence that reconcile is plan-only.

---

## 27. Dynamic AI-Verse host adapter

The current implementation is `scripts/ai_verse_host_adapter.py`.

The code has evolved beyond its historical four-component name.

Current class:

```text
AIverseOSHost
```

Current adapter ID:

```text
ai-verse-os:host
```

A backward-compatible `OSFourComponentHost` alias remains.

### Current supported surfaces

The host can expose:

- `read_context`
- `retrieve_history`
- `list_capabilities`
- `list_connections`
- `authorize_action`
- `request_action`
- `query_data` when Data is available

### Dynamic optional behavior

- no Memory -> history may be empty rather than host failure;
- external Skills can appear later via the installed provider root;
- Data operation is advertised only when Data is available;
- Connections are read from OS registry metadata;
- config does not require a Skills source checkout;
- legacy `--skills-entrypoint` is accepted only for compatibility.

**LAW:** optional components add operations/capabilities to one host rather than requiring a new fixed host topology.

---

## 28. Data host boundary

OS has an explicit Data host:

```text
node scripts/data-host.mjs --root <os-root>
```

OS owns:

- trusted scope;
- extension discovery;
- host permission floor;
- dispatch decision.

Data owns:

- structured records;
- schemas;
- query/aggregate;
- relations;
- transactions;
- idempotency;
- events/receipts;
- database integrity;
- migration/backup/recovery.

OS does not open Data SQLite files directly.

Read operations map to local read permission.

Destructive operations map to the stricter delete-data floor.

Approval-required destructive requests are blocked before Data engine invocation.

**LAW:** integration should call the owning component's supported boundary rather than reach into its canonical database.

---

## 29. Canonical write-command boundary

Current command:

```text
node scripts/write-command.mjs enqueue --root <os-root>
```

This is a crucial boundary and must not be overstated.

### What exists

It validates:

- exact scope;
- immutable request shape;
- bounded structured parameters;
- fingerprint;
- idempotency;
- provenance;
- OS permission floor;
- safe runtime paths.

It queues request/receipt records in:

```text
runtime/write-commands/
```

### Current execution boundary

The original Phase 3.7 `write-command.mjs` queue remains a safe intake/transport and still must not be mistaken for a generic arbitrary write executor by itself.

**CURRENT SYSTEM UPDATE (2026-09-14):** OS now also exposes bounded owner routes through the host adapter for the accepted Invisible Intelligence operations, including workspace organization, Memory capture, Skills learning candidates, safe structured Data, temporary Workers, durable Bots with consent, and Automations with recurring consent. Those routes re-check trusted evidence/authority and invoke the canonical owner rather than mutating sibling stores directly.

The generic queued write-command surface is therefore still not a universal handler framework for every future owner, but the earlier statement that the system has no owner-specific canonical execution path is superseded for the accepted routes.

---

## 30. Installation

Current development/member-test command:

```bash
npx --yes github:aiverse-filmmakers/AI-Verse-OS install
```

Global CLI from GitHub:

```bash
npm install -g github:aiverse-filmmakers/AI-Verse-OS
```

Then:

```bash
ai-verse-os install
```

### Current behavior

Installer:

- requires Git;
- clones branch `main`;
- refuses a non-empty target that is not already an OS root;
- validates key architecture files;
- verifies Claude/Codex onboarding packages;
- reports Node/runtime guidance.

### Intended published UX

The README intends a future:

```bash
npx ai-verse-os install
```

after registry publication.

---

## 31. Install-order independence

Install-order independence should be interpreted correctly.

It does **not** mean installing the OS blindly on top of an arbitrary non-empty directory.

The intended model is:

```text
component package/runtime may exist first
or OS may exist first
        ↓
discover
        ↓
attach
        ↓
activate/adopt
        ↓
migrate if required
        ↓
initialize
        ↓
health + authority check
```

Chronology must never determine authority.

Current local extension architecture supports this model better than the original tracked-file integration model.

---

## 32. Update behavior

Current command:

```text
ai-verse-os update
```

It:

- requires a Git checkout;
- refuses update when tracked system files are dirty;
- ignores local ignored user state;
- fetches `origin/main`;
- performs fast-forward-only merge;
- revalidates required files.

### Current limitations

**GAP:** update is tied to moving `main`, not an immutable release channel.

**GAP:** there is no general OS rollback command.

**GAP:** architecture migrations are governed conceptually, but update CLI is not a full versioned migration engine.

---

## 33. Core doctor vs component doctor vs audit

There are three different health levels.

### `ai-verse-os doctor`

Checks things such as:

- Node;
- Git;
- OS root;
- required files;
- Claude/Codex runtime presence.

### `ai-verse-os components doctor`

Checks known component attachment/readiness evidence.

### `/audit`

Performs a broader evidence-based review of:

- architecture;
- authority;
- workspace isolation;
- Context;
- Connections;
- Capabilities;
- Cadence;
- compatibility;
- freshness;
- real execution evidence.

**GAP:** there is no single command that proves all three levels plus every component-specific doctor in one end-to-end system health result.

A core doctor can currently say "OS is ready" while an optional component is separately degraded.

---

## 34. Audit model

The built-in audit rubric scores 100 points across:

- architecture integrity;
- context;
- connections;
- capabilities;
- cadence.

It applies hard score caps for severe authority, context or isolation failures.

This is important because it treats an AI operating system as an **operational evidence system**, not just a folder structure.

Audit reports are point-in-time derived evidence under `runtime/reports/`.

A resolved finding requires fresh evidence, not merely a changed file.

---

## 35. Onboarding

**CURRENT:** onboarding is progressive by default. The deeper seven-question intake remains available when useful, but it is no longer a mandatory first-value barrier.

The ordinary Agent product path is `aiverse start`, which performs exact released install/setup/doctor and then hands off conversationally with “What would you like help with?” without granting permissions or transferring Brain strategy. OS progressive onboarding/history bridges gather additional context only when it becomes relevant.

The owner-level onboarding machinery still preserves existing state, detects legacy paths, checks direction ownership before strategic writes, resumes safely after interruption, avoids profession-specific scaffolding and distinguishes configured from verified connections.

---

## 36. Workspace creation

The `workspace` capability:

- checks if a separate workspace is justified;
- avoids near-duplicates;
- creates only minimum structure;
- keeps type/domains extensible;
- checks direction ownership before strategic edits;
- routes external authoritative sources instead of copying by default;
- keeps specialized structure local;
- promotes reusable material only after evidence.

**LAW:** do not create empty-folder theater.

---

## 37. Knowledge capture

`grill-me` captures operator knowledge through scoped interviews.

It separates:

- confirmed facts;
- tentative ideas;
- historical context;
- reusable knowledge;
- decisions;
- source routes.

Raw interviews live in scoped inboxes.

Promotion happens only after classification.

This prevents a conversational transcript from automatically becoming canonical truth.

---

## 38. Linking sources

`link` is designed to make a source discoverable without copying it.

A durable route should record:

- location;
- contents;
- when to use it;
- authority;
- scope/privacy;
- access verification.

This is a core anti-duplication pattern in OS design.

---

## 39. Improvement model

`level-up` uses Three Ms to produce one scoped improvement at a time.

It checks strategic ownership before changing goals/objectives.

It may result in:

- deleting unnecessary work;
- routing/context repair;
- connection verification;
- SOP/knowledge;
- template;
- script;
- local/shared skill;
- agent;
- automation;
- app;
- policy.

It explicitly does not default to adding more AI complexity.

---

## 40. Expansion policy

The universal root is meant to stay stable.

New top-level folders must prove they represent a genuinely universal architectural concern with distinct ownership/lifecycle.

Possible future domain packs must remain optional overlays.

**LAW:** repeated use earns promotion. Speculation does not.

---

## 41. Failure behavior

The OS repeatedly favors fail-closed semantics.

Examples:

- malformed direction ownership -> no strategic fallback;
- unsafe workspace/symlink -> deny;
- malformed action policy -> deny;
- incompatible capability provider -> exclude/degrade;
- unsafe extension engine path -> reject;
- Data permission failure -> no dispatch;
- modified generated adapter -> preserve/report conflict;
- shared registry lock -> diagnose, never steal automatically.

**LAW:** uncertainty about ownership or authority should not silently widen access.

---

## 42. Historical evolution

### Architecture v2

PR #1 transformed the system into the domain-neutral Unified Workspace Architecture.

**Lesson:** a universal OS should adapt through scoped evidence rather than profession-specific roots.

### Capability Provider Contract

PR #2 established provider identity, generation and ownership before implementing discovery.

**Lesson:** cross-repository integration should begin with ownership/contract definition, not ad hoc file scanning.

### Local extension registry

PR #3 removed the need for optional extensions to permanently edit tracked OS contracts.

**Lesson:** installation state belongs outside upstream-owned system files.

### Runtime adapter ownership

PR #4 moved canonical built-ins to `system/capabilities/` and made Claude/Codex generated peers ownership-aware.

**Lesson:** generated outputs need explicit ownership and conflict preservation.

### Single strategic direction owner

PR #5 prevented OS and Brain from becoming two editable strategy systems.

**Lesson:** one responsibility needs one canonical owner.

### Four-provider capability resolution

PR #6 implemented scoped discovery across OS, distributed, local and workspace providers.

**Lesson:** unify discovery without merging ownership.

### Permission intersection

PR #7 made OS and Brain authority restrictive by intersection.

**Lesson:** one permissive layer cannot weaken another layer.

### Cross-repository acceptance

PRs #8-9 moved architecture claims into executable composition proof.

**Lesson:** integration is not real until the supported path works across repositories.

### Astra repair: cross-workspace capability symlink leakage

PR #10 hardened physical workspace containment.

**Lesson:** logical scope labels are not enough. Physical filesystem boundaries matter.

### Astra repair: frozen OS strategy reactivation

PR #11 introduced ownership-aware current-context filtering.

**Lesson:** preserving historical provenance must not preserve current authority.

### Maintained host adapter

PR #13 moved composition away from CI-only inline wiring.

**Lesson:** acceptance must exercise a maintainable public integration boundary.

### Documentation correction

PRs #14-15 corrected user-facing integration claims after implementation.

**Lesson:** documentation drift is itself an architecture risk in a multi-repo system.

### Write-command boundary

PR #16 created safe owner-controlled command transport.

**Lesson:** cross-component write requests need immutable identity, scope and idempotency before effects.

**Still unfinished:** canonical handlers remain later integration work.

### Data host

PR #17 added an explicit component-owned Data execution boundary.

**Lesson:** the host should delegate to component APIs rather than access component storage directly.

### Five-component release hardening

PR #18 made the host dynamically optional-component aware and added components doctor/reconcile.

**Lesson:** one host should gain/lose optional capabilities dynamically.

### Workspace ID alignment

PR #20 aligned scope validators with canonical workspace IDs.

**Lesson:** shared identities must have one exact grammar across boundaries.

### Registry lock diagnostics

PR #21 exposed lock state but never auto-stole it.

**Lesson:** concurrency safety is preferable to "helpful" destructive recovery.

### Refreshed real acceptance

PR #23 removed the legacy tracked Brain registration workaround from acceptance.

**Lesson:** tests must match real member integration paths, not hidden preparation.

---

## 43. Evidenced inspirations and inherited frameworks

This fresh OS-only review found explicit provenance that must be preserved.

### Nate Herk

`THIRD-PARTY-NOTICES.md` states that portions of the repository are derived from software copyright 2026 Nate Herk and are distributed under the included MIT license.

It also states that the names **The Three Ms of AI** and **The Four Cs of an AI OS** are identified by their original publisher as trademarks of Nate Herk.

AI-Verse uses shortened descriptive framework labels and maintains AI-Verse-specific modifications/additions.

**INSPIRATION:** Three Ms / Four Cs are therefore evidenced external conceptual ancestry, not purely original AI-Verse inventions.

### 3D visualization stack

The 3D Brain renderer includes explicit third-party notices for packages including:

- 3d-force-graph;
- three.js;
- three-forcegraph;
- Preact;
- D3-related libraries;
- ngraph libraries;
- Marked;
- supporting runtime packages.

These are implementation dependencies/inspirations for the visualization layer, not evidence that they define OS architecture.

### External AI OS competitors

**EVIDENCE LIMITATION:** no reviewed canonical OS file names a definitive competitive set of other AI operating systems used to design Unified Workspace Architecture.

Do not invent such a list.

---

## 44. Documentation drift found in this standalone review

### Drift 1: architecture README understates provider implementation

`system/architecture/README.md` still says external provider discovery and later integration stages remain separate work.

But `system/architecture/capability-resolution.md`, resolver code and CI prove external provider discovery is implemented.

### Drift 2: Skill Authoring names the wrong authoring source

`SKILL-AUTHORING.md` says the "current materialized authoring source" is `.claude/skills/<skill-name>/`.

Current architecture and `skills/registry.yaml` say the canonical editable source is `system/capabilities/`, with Claude/Codex as generated peers.

### Drift 3: historical four-component host document

`docs/FOUR-COMPONENT-HOST-ADAPTER.md` still describes the older fixed four-component framing and an example with `--skills-entrypoint`.

Current host code is dynamic, uses `AIverseOSHost`, exposes optional Data, real Connections metadata and no longer requires a Skills source checkout.

### Drift 4: named Memory support in AI-VERSE.yaml

`AI-VERSE.yaml` retains an `extensions.memory` support declaration while current attachment truth is generic `.aiverse/extensions/registry.json`.

This can be interpreted safely as host-support declaration, but the distinction is not explicit enough.

### Drift 5: doctor terminology

Core `ai-verse-os doctor` can report "AI-Verse OS is ready" without running component doctor or operational `/audit`.

The wording can overstate full-system health.

**GAP:** these should be cleaned so member-facing docs match the current implementation generation.

---

## 45. Current intended milestone

Based on the repository's release-hardening PRD and current status docs, the present OS milestone is the **first usable AI-Verse member-beta host**.

At this milestone, OS is intended to:

- install cleanly;
- update safely;
- onboard a new operator;
- create isolated workspaces;
- preserve user-owned state;
- attach optional components without tracked-file mutation;
- dynamically discover Memory/Skills/Data and compose Brain;
- keep strategic ownership singular;
- provide restrictive permission floors;
- expose connection metadata;
- route Data through its supported engine;
- diagnose component attachment;
- reconcile practical installation-order differences;
- maintain clean cross-repo acceptance.

The stronger AI-Verse-System target additionally expects a frictionless activate/adopt/migrate experience for newly installed additions.

---

## 46. Current-target readiness verdict

**Verdict: FUNCTIONALLY READY, BUT NOT YET SEAMLESS AS A COMPLETE OPERATING PRODUCT**

The foundational architecture is strong.

Several important integration surfaces are real and tested.

However, the current implementation still has meaningful gaps between "correct host architecture" and "every addition works like a glove immediately."

### Completeness by dimension

| Dimension | Verdict |
|---|---|
| Unified core architecture | **COMPLETE** |
| Source-of-truth/ownership model | **COMPLETE** |
| Workspace isolation | **COMPLETE / STRONGLY ENFORCED** |
| Built-in capability model | **COMPLETE WITH DOC DRIFT** |
| External capability discovery | **COMPLETE FOR DISCOVERY** |
| Generic live capability readiness | **MISSING / DEFERRED** |
| OS permission floor | **COMPLETE** |
| Direction ownership | **COMPLETE** |
| Dynamic Brain/Memory/Skills/Data host composition | **COMPLETE WITH LIMITATIONS** |
| Connections metadata | **COMPLETE** |
| Generic connection execution layer | **NOT OWNED / NOT IMPLEMENTED BY OS** |
| Data host boundary | **COMPLETE** |
| Cross-component write intake | **COMPLETE** |
| Canonical write dispatch/handlers | **CURRENT FOR ACCEPTED INVISIBLE ROUTES; GENERIC QUEUE FRAMEWORK PARTIAL** |
| OS install | **COMPLETE FOR GITHUB DEVELOPMENT PATH** |
| OS update | **COMPLETE WITH RELEASE LIMITATIONS** |
| Component attachment model | **COMPLETE FOR KNOWN CORE EXTENSIONS** |
| Generic extensible component discovery | **PARTIAL** |
| Component reconcile | **PLAN + BOUNDED OWNER APPLY** |
| Universal activate/adopt command | **CURRENT AGENT FIRST-RUN VIA DISTRIBUTION; ARBITRARY FUTURE COMPONENTS PARTIAL** |
| Universal legacy-state migration orchestration | **PARTIAL / COMPONENT-SPECIFIC** |
| Core doctor | **COMPLETE FOR CORE CHECKS** |
| Unified whole-system health command | **CURRENT FOR AGENT PROFILE VIA DISTRIBUTION DOCTOR; BROADER FULL PROFILE PARTIAL** |
| Automation/Cadence architecture | **COMPLETE AS ARCHITECTURE** |
| Universal scheduler/runtime | **CURRENT OWNER IS AI-VERSE AUTOMATIONS; INTENTIONALLY OUTSIDE OS** |
| Agent architecture | **COMPLETE AS MODEL** |
| Generic agent executor | **NOT PRESENT IN BASE OS** |
| App architecture | **COMPLETE AS MODEL** |
| Concrete app proof | **3D Brain EXISTS** |
| Release/version immutability | **PARTIAL** |
| Cross-platform OS CLI proof | **STRONG** |
| Full five-component release proof | **HISTORICAL FIVE-COMPONENT + FROZEN AGENT RELEASE ACCEPTED** |

---

## 47. Command/lifecycle matrix

| Capability | Required now? | Current command/path | End-to-end proven? | Missing |
|---|---:|---|---:|---|
| Install OS | Yes | `npx --yes github:aiverse-filmmakers/AI-Verse-OS install` | Yes | Immutable release channel/published package |
| Install global CLI | Useful | `npm install -g github:aiverse-filmmakers/AI-Verse-OS` | Yes | Registry publication |
| Core doctor | Yes | `ai-verse-os doctor` | Yes | Does not include component/operational health |
| Onboard | Yes | progressive OS onboarding; ordinary Agent path is `aiverse start` | Yes | broader UI/channel polish |
| Update | Yes | `ai-verse-os update` | Yes | Version channels/rollback/migration engine |
| Component doctor | Yes | `ai-verse-os components doctor` | Yes | Hardcoded known components, shallow health |
| Component reconcile | Yes | `ai-verse-os components reconcile [--apply]` | Yes for bounded owner apply | no arbitrary future-owner lifecycle invention |
| Attach Brain | If present | Brain-owned attach command surfaced by reconcile | Yes in acceptance | Not unified under OS activate |
| Attach Memory | If present | rerun Memory installer | Yes in acceptance | Not unified under OS activate |
| Attach Data | If present | Data-owned install/host route | Yes in Agent composition | broader migration UX |
| Discover Skills | If present | passive provider discovery | Yes | Live generic readiness still separate |
| Activate/adopt arbitrary component | Agent first-run current via Distribution | `aiverse start` for Agent profile | Yes for Agent | generic future component activation remains partial |
| Migrate old component state | Yes for stateful additions | component-specific | Mixed | Shared discovery/plan/apply/verify UX |
| Disable component | Yes | component-owned | Mixed | Unified OS UX |
| Detach/uninstall component | Yes | component-owned | Mixed | Unified OS UX |
| Reinstall preserved state | Yes | component-specific + reconcile/Distribution | Yes in Agent acceptance | broader cross-version release train |
| Queue cross-component write | Yes | `write-command.mjs enqueue` | Yes | generic queue remains intake-only |
| Execute owner-routed canonical write | Yes for accepted invisible routes | OS host adapter -> canonical owner | Yes for workspace/Memory/Skills/Data/Bots/Workers/Automations boundaries | broader owners require contracts |
| Audit operational system | Yes | `/audit` | Yes as AI-guided audit | Not one deterministic aggregate doctor |
| Run universal automation scheduler | Yes at system level | AI-Verse Automations owner | Yes in Agent acceptance | OS intentionally does not own scheduler |

---

## 48. Exact blockers to "works perfectly together like a glove"

### 48.1 Universal activation/adoption

There is no one operation that takes a newly installed component from:

```text
available
→ attached
→ enabled
→ initialized
→ adopted by the active agent
→ migrated if needed
→ health verified
```

This is the single most visible product gap.

### 48.2 Executable reconciliation

**CURRENT for bounded cases:** reconcile has an apply path and the Agent first-run self-heal consumes it. Automatic mutation is deliberately allowlisted to the exact owner-controlled Brain attach/init case; migration, registry-lock and unknown-owner states remain non-automatic.

Broader arbitrary component activation is still intentionally not synthesized by OS.

### 48.3 Generic component manager

Known core local extensions are hardcoded.

Future additions should be describable through a versioned component contract so Token/Apps/future modules do not require bespoke OS code simply to become discoverable.

### 48.4 Canonical write handlers

The generic queue is still intake-only, but CURRENT host routes now execute the accepted owner-controlled workspace/Memory/Skills/Data/Bot/Worker/Automation operations through their canonical owners. The remaining gap is a generic extensible protocol for additional future owner classes, not absence of all canonical execution.

### 48.5 Capability readiness

Integrity and selection exist.

Generic live readiness is still explicitly unverified.

A mature host should be able to say not just "I found this capability" but "its runtime/dependencies/connections are currently usable in this scope."

### 48.6 Unified health

Core doctor, component doctor and `/audit` are separate layers.

A user should eventually be able to ask one system-level health question and receive a truthful aggregate result without collapsing those distinctions.

### 48.7 Migration orchestration

Stateful components need one consistent migration UX for pre-existing agent history and standalone state.

The component-specific migration mechanics can stay with the component.

### 48.8 Release versioning

The current CLI follows moving `main`.

A real member release should install an immutable tested generation and support explicit update channels/rollback policy.

### 48.9 Documentation convergence

Current docs should be reconciled with actual host/provider implementation so agents do not follow stale integration instructions.

---

## 49. What is intentionally not an OS defect

These absences should not automatically be "fixed" by stuffing more machinery into OS.

### Brain cognition

Brain should remain separate.

### Memory engine

Memory should remain separate.

### Structured Data database

Data should remain separate.

### Skills generation lifecycle

External Skills should remain separately owned.

### Application-specific databases

Apps should not become OS canonical stores.

### Full connector credentials/execution

OS can own scope/routing/permission contracts without owning every provider credential implementation.

### Telemetry accounting

Token should own telemetry rather than OS.

The goal is not to make OS monolithic.

The goal is to make integration seamless while ownership remains modular.

---

## 50. Portability beyond AI-Verse runtimes

The most portable OS concepts are:

- scope identifiers;
- workspace manifests;
- source-of-truth rules;
- direction ownership;
- current-context resolver;
- extension registry;
- capability provider contract;
- action-permission boundary;
- write-command envelope;
- host operations;
- component health/reconcile semantics.

**INTENDED:** Hermes and other capable hosts should integrate through a stable versioned host/component protocol rather than ad hoc direct filesystem reading.

### Current limitation

The polished user experience is strongest for Claude Code and Codex.

The Brain JSON-subprocess host is the best current seed for a runtime-neutral external host contract.

---

## 51. Definition of done

AI-Verse OS reaches the intended mature state when:

1. its universal architecture remains stable and domain-neutral;
2. user-owned state survives upgrades and ordinary component lifecycle;
3. every optional component can be independently available before or after OS;
4. attachment is explicit and idempotent;
5. activation/adoption can be invoked by a user or existing agent;
6. stateful additions can discover and migrate existing history safely;
7. component health is truthful and live;
8. component reconciliation can be safely applied;
9. future components can register without hardcoded OS enumeration;
10. capability readiness is distinguished and actually verifiable;
11. cross-component write commands can reach the correct canonical owner safely;
12. strategic ownership remains singular;
13. workspace isolation remains physical and logical;
14. permissions fail closed;
15. integrations call component-owned boundaries instead of internal storage;
16. runtime adapters preserve local modifications;
17. OS distribution is immutable/versioned/reproducible;
18. acceptance uses the exact member path;
19. system documentation matches implementation;
20. compatible non-AI-Verse runtimes can adopt stable contracts without weakening authority.

---

## 52. Supreme-system contribution

AI-Verse OS is the layer that allows all other components to become more capable without collapsing into one monolith.

Brain can reason without becoming the filesystem.

Memory can remember without becoming current direction.

Data can structure facts without becoming Memory.

Skills can expand without becoming OS.

Multiple Bots can coordinate without becoming a second canonical workspace system.

Connections can reach live systems without granting themselves authority.

Apps and Dashboard can visualize and operate without owning hidden truth.

Token can observe resource use without becoming operational state.

The OS succeeds when these independently owned pieces feel like **one coherent system to the user while remaining cleanly separable underneath**.

---

## 53. Open decisions

1. What should the universal component activation command syntax be?
2. Should component discovery be registry-driven and self-describing instead of hardcoded IDs?
3. **Answered for current public beta:** `components reconcile --apply` exists, but automatic execution is deliberately narrow and owner-controlled; broader owner actions remain explicit.
4. What shared migration-plan schema should stateful components expose?
5. **Partially answered:** accepted owner-specific execution routes now exist through the OS host adapter; what generic extensible protocol should cover additional future owners and the legacy queue?
6. **Answered:** AI-Verse Automations owns universal Cadence/schedules/triggers; OS owns scope/permission boundaries, not scheduling truth.
7. Should core doctor aggregate component doctor while still distinguishing structural vs live health?
8. What formal versioned "AI-Verse Host Protocol" should external runtimes target?
9. How should release channels, immutable versions and rollback work?
10. Should the named Memory support declaration in `AI-VERSE.yaml` become a generic host-support declaration?
11. How should current stale four-component/authoring docs be migrated without losing useful historical context?
12. What future components must be understood by OS core versus discoverable generically through contracts?
