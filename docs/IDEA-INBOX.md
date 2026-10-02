# AI-Verse System Idea Inbox

This is the capture layer for system ideas that are not yet fully classified or implemented.

Do not treat this file as implementation truth.

Once an idea has a clear architectural home, promote it into the relevant component/system specification and leave a short provenance record here.

## Status vocabulary

- **RAW** - newly captured, not yet analyzed.
- **NEEDS-SCOPING** - valid direction, owner/contract not yet clear.
- **ACCEPTED-INTENT** - agreed desired behavior, not necessarily implemented.
- **DEFERRED** - valid but deliberately not part of the current milestone.
- **REJECTED** - considered and deliberately not pursued.
- **PROMOTED** - incorporated into a canonical spec/plan.

---

## 2026-10-02 - TheAlgorithm-inspired verifiable task-solving loop

**Status:** NEEDS-SCOPING

The owner wants Daniel Miessler's TheAlgorithm preserved as a future AI-Verse inspiration/upgrade candidate.

Potentially useful ideas include:

- current-state -> ideal-state task framing;
- explicit, testable definition-of-done criteria;
- positive, negative and edge acceptance criteria;
- evidence-gated completion rather than "should work";
- original-request re-read before declaring completion;
- independent review at important commitment boundaries;
- post-task learning routed into existing AI-Verse learning owners.

This is **not an implementation commitment** and does not change the current roadmap or public-beta repair order.

Before adoption, AI-Verse should compare these ideas against existing Brain Goals/completion contracts, Gateway execution, Multiple Bots Tasks, self-learning and audit verification, then adopt only the parts that measurably improve task quality without creating duplicate truth or unnecessary ceremony.

External inspiration:

- https://github.com/danielmiessler/TheAlgorithm

Tracked in:

- `docs/INSPIRATION-PRIOR-ART-AND-GAP-RADAR.md`

---

## 2026-10-02 - Purpose Context / Telos-inspired deep context

**Status:** PROMOTED

The owner wants AI-Verse to gain a Telos-inspired layer that gives agents explicit deep context about:

- mission/purpose;
- goals and priorities;
- strategies and constraints;
- KPIs/success measures;
- current state;
- recent material changes that should alter decisions.

The feature must use AI-Verse's existing canonical owners rather than create a new monolithic Telos database.

Accepted architecture:

- OS -> identity/scope/current operating context;
- Brain/current direction owner -> strategic intent/goals/priorities/strategy;
- Data -> current structured KPI/operational truth;
- Memory -> historical evidence/provenance;
- Gateway/runtime -> derived context assembly.

High-impact mission/goal/priority/value changes must not be silently rewritten.

**Execution priority:** first eligible new cross-owner capability after the active whole-system repair/requalification program establishes a safe baseline. Do not append it to the end of unrelated long-range expansion.

External inspiration:

- https://github.com/danielmiessler/telos

Promoted to:

- `docs/PURPOSE-CONTEXT-TELOS-ADOPTION-PLAN.md`
- `docs/OWNER-PRODUCT-INTENT.md`
- `docs/FINAL-AI-VERSE-BLUEPRINT.md`
- `docs/MASTER-PLAN.md`
- `docs/INSPIRATION-PRIOR-ART-AND-GAP-RADAR.md`

---

## 2026-09-12 - Living system specification

**Status:** PROMOTED

AI-Verse-System must update whenever meaningful ideas, plans, fixes, lifecycle changes, integrations, migrations, readiness findings or architectural decisions change.

Promoted to:

- `docs/LIVING-SPEC-PROTOCOL.md`
- `docs/MASTER-PLAN.md`

---

## 2026-09-12 - Seamless component adoption

**Status:** PROMOTED

A newly installed component should not merely exist on disk.

An already-running agent/host should be able to adopt it as the canonical infrastructure for its responsibility through a supported setup/activation sequence.

Examples of the intended user experience include concepts such as:

- activate Memory;
- activate Data;
- activate Brain;
- activate Token;
- reconcile and activate installed components.

The exact public syntax remains an open design decision.

Promoted to:

- `docs/MASTER-PLAN.md`
- `docs/RESEARCH-PROMPT.md`
- `components/ai-verse-os/COMPONENT-SPEC.md`

---

## 2026-09-12 - Existing-history migration

**Status:** PROMOTED

Stateful components such as Memory and Data must account for existing users/agents with historical state.

The intended system needs explicit import/migration behavior rather than silently starting from zero or creating parallel truth.

Promoted to:

- `docs/MASTER-PLAN.md`
- `docs/RESEARCH-PROMPT.md`
- relevant future component specifications

---

## 2026-09-12 - Current-target completeness

**Status:** PROMOTED

A repository must not be described as complete merely because its internal engine is finished.

Documentation must compare it against what the component is supposed to achieve **at the current milestone**, including integration, lifecycle, commands, migration, adoption, acceptance and distribution.

Promoted to:

- `docs/MASTER-PLAN.md`
- `docs/RESEARCH-PROMPT.md`
- `docs/COMPONENT-TEMPLATE.md`
- existing OS component documentation


---

## 2026-09-13 - Canonical write-handler completion

**Status:** ACCEPTED-INTENT

The fresh OS-only audit confirmed that the current OS write-command boundary is transport-only. It validates and queues immutable requests but deliberately performs no canonical mutation.

The mature system needs owner-specific handlers that can consume those requests and route them to the correct canonical owner while rechecking current scope, owner, permission, approval and durable idempotency at the actual write edge.

This must not become one giant OS mutation API. Handlers should delegate to the owning component/source.

Promoted/current detail:

- `components/ai-verse-os/COMPONENT-SPEC.md`
- `components/ai-verse-os/QC.md`

---

## 2026-09-13 - Self-describing component lifecycle contract

**Status:** ACCEPTED-INTENT

The current OS component doctor knows Brain, Memory and Data explicitly and treats Skills as a special external provider.

As the ecosystem expands, new components such as Token and future modules should not require bespoke hardcoded OS enumeration merely to become discoverable.

The intended direction is a versioned, self-describing component contract exposing enough safe metadata for discovery, compatibility, lifecycle commands and health delegation while preserving component ownership.

Promoted/current detail:

- `components/ai-verse-os/COMPONENT-SPEC.md`
- `components/ai-verse-os/QC.md`

---

## 2026-09-13 - Unified readiness and health envelope

**Status:** ACCEPTED-INTENT

The OS currently separates core doctor, component doctor and evidence-based `/audit`, while capability discovery intentionally reports readiness as unverified.

The mature system should preserve those distinctions but provide one truthful aggregate health/readiness view capable of saying which layer is healthy, degraded, unverified or unavailable.

It must never turn "discovered" into "ready" or "registered" into "healthy".

Promoted/current detail:

- `components/ai-verse-os/COMPONENT-SPEC.md`
- `components/ai-verse-os/QC.md`

---

## 2026-09-13 - Cadence runtime ownership

**Status:** NEEDS-SCOPING

AI-Verse OS has a strong Cadence architecture for jobs, triggers and policies, but the base OS repo does not currently implement one universal scheduler/event execution engine.

A system-level decision is needed on whether Cadence runtime belongs in OS, Automations, Brain, another component, or an external host/runtime contract.

Until decided, the existence of automation definitions must not be documented as proof of scheduled execution.

Promoted/current detail:

- `components/ai-verse-os/COMPONENT-SPEC.md`
- `components/ai-verse-os/QC.md`


---

## 2026-09-13 - Component lifecycle symmetry

**Status:** ACCEPTED-INTENT

The Brain audit found a concrete lifecycle asymmetry: current main exposes `disable` through the CLI but has no public `enable` command. Its internal API can enable Brain, while re-running `attach` deliberately preserves the disabled state.

System-wide lifecycle contracts should therefore require symmetry wherever the state exists:

```text
enable <-> disable
attach <-> detach
install <-> uninstall/reinstall path
authority handover <-> handback where applicable
```

A component should never expose a user-facing state transition with no supported way back unless the transition is intentionally terminal and documented as such.

Promoted/current detail:

- `components/ai-verse-brain/COMPONENT-SPEC.md`
- `components/ai-verse-brain/QC.md`

---

## 2026-09-13 - Activation must remain separate from authority transfer

**Status:** ACCEPTED-INTENT

Brain proves that component adoption and strategic ownership are different operations.

Installing/attaching/activating Brain must not automatically transfer strategic direction from the host/OS to Brain.

A generic future `activate brain` flow may configure Brain as an available intelligence layer, but any transfer of canonical strategic authority must remain a separately visible, explicit, reversible transaction with provenance.

This principle should apply to any future component activation that can change a canonical owner.

Promoted/current detail:

- `components/ai-verse-brain/COMPONENT-SPEC.md`
- `components/ai-verse-brain/QC.md`

---

## 2026-09-13 - Shared owner-routed write pipeline

**Status:** ACCEPTED-INTENT

The OS re-audit found that OS currently provides safe write-command intake without canonical handlers.

The Brain audit independently found that Brain classifies durable writes by canonical owner and exposes a host `write_route` contract, but the cognition/learning pipeline does not complete a generic OS/Memory/Knowledge/Capability write transaction.

These are two halves of the same missing system layer.

Intended system flow:

```text
Brain / agent identifies durable candidate
        ↓
classify canonical owner
        ↓
bounded immutable write request
        ↓
host / OS validates scope + permission + authority
        ↓
canonical owner revalidates current state + durable idempotency
        ↓
canonical effect
        ↓
receipt / provenance
        ↓
Brain may reference result without duplicating owner state
```

The solution must not be direct Brain access to OS/Memory internal storage.

Promoted/current detail:

- `components/ai-verse-os/COMPONENT-SPEC.md`
- `components/ai-verse-brain/COMPONENT-SPEC.md`

---

## 2026-09-13 - Immutable release must match the documented architecture

**Status:** ACCEPTED-INTENT

The Brain audit found a concrete release-generation drift: current README describes local-registry attachment, direction ownership, disable/detach and other post-beta hardening while the recommended immutable `v0.1.0-beta.1` tag predates those features.

System-wide rule:

> A member-facing immutable install version must contain the same architecture and lifecycle behavior the current member documentation describes.

Development `main` may move ahead, but docs must distinguish development behavior from the latest released behavior.

Before calling a component member-ready, verify the exact immutable artifact rather than only the repository head.

Promoted/current detail:

- `components/ai-verse-brain/COMPONENT-SPEC.md`
- `components/ai-verse-brain/QC.md`

---

## 2026-09-13 - Cadence runtime ownership confirmed as outside Brain

**Status:** NEEDS-SCOPING

The OS audit found that base OS has Cadence architecture but no universal scheduler.

The Brain audit independently confirms that Brain intentionally owns **when cognition would be useful**, while the host owns cron/event/background execution.

Brain emits cadence plans and portable hooks but must not become the deterministic scheduler.

The remaining system decision is therefore not whether Brain should absorb scheduling. It is which host/component becomes the canonical Cadence execution owner for AI-Verse and how non-AI-Verse hosts implement the same contract.

Related existing idea: Cadence runtime ownership.

Promoted/current detail:

- `components/ai-verse-brain/COMPONENT-SPEC.md`
- `components/ai-verse-brain/QC.md`


---

## 2026-09-13 - Apps/UI projections and app registration ownership

**Status:** PROMOTED

The standalone AI-Verse Apps audit confirmed a system-wide source-of-truth rule: apps, dashboards and other interfaces may present, cache and interact with canonical state, but they must not become hidden competing truth stores.

A UI or app projection should be deletable and rebuildable from the declared canonical owners. If an app legitimately owns canonical domain state in the future, that ownership must be explicit rather than emerging accidentally from local state.

The intended registration split is:

- Apps defines the versioned app manifest/registration schema and lifecycle contract.
- OS owns the authoritative app-registration records for each AI-Verse system.
- Apps tooling requests registration changes through the OS-owned boundary rather than creating a second editable registry.

The Apps audit also reinforces the existing Cadence scoping issue: declaring background behavior in an app manifest does not make Apps the universal scheduler owner.

Promoted/current detail:

- `docs/MASTER-PLAN.md`
- `components/ai-verse-apps/COMPONENT-SPEC.md`
- `components/ai-verse-apps/QC.md`


---

## 2026-09-13 - Migration authority handoff and source freeze

**Status:** ACCEPTED-INTENT

The Memory audit found that safe copying is not enough to complete adoption. A legacy Memory store may remain preserved for evidence, but after adoption there must be exactly one active writable canonical route.

The reviewed migration plan should be bound to a source snapshot/fingerprint, or apply must explicitly detect source drift after review. After target verification, the system should record a handoff/retirement receipt for the legacy writable route.

Promoted/current detail:

- `docs/MASTER-PLAN.md`
- `components/ai-verse-memory/COMPONENT-SPEC.md`
- `components/ai-verse-memory/QC.md`

---

## 2026-09-13 - Symmetric physical containment for canonical writes

**Status:** ACCEPTED-INTENT

The Memory audit found a concrete asymmetry: native read/index paths validate lexical and resolved physical ownership, but canonical write destinations are not protected by the same rule before file creation.

System-wide law: scoped canonical storage must validate physical containment before writes as well as reads. Rejecting an escaped file during later indexing is too late because the filesystem effect has already happened.

Promoted/current detail:

- `docs/MASTER-PLAN.md`
- `components/ai-verse-memory/COMPONENT-SPEC.md`
- `components/ai-verse-memory/QC.md`

---

## 2026-09-13 - Detach must match discovery reality

**Status:** ACCEPTED-INTENT

The Memory audit found that registry detach removes Memory's local extension entry while deliberately preserving installed engine and agent adapters.

Preserving canonical user data is correct. A lifecycle operation called `detach` should either make the component unavailable through every host discovery surface that attachment opened, or clearly identify itself as a narrower registry/local-host detach.

Promoted/current detail:

- `docs/MASTER-PLAN.md`
- `components/ai-verse-memory/COMPONENT-SPEC.md`
- `components/ai-verse-memory/QC.md`


---

## 2026-09-13 - Projection semantics must remain owner-declared

**Status:** ACCEPTED-INTENT

The Dashboard audit exposed a stronger form of the existing non-canonical UI law.

A UI can avoid a second writable database and still become a hidden authority if it invents another component's meaning from private files or transient session state.

Examples include defining health dimensions inside Dashboard, treating an unavailable task source as an empty task list, treating chat sessions as canonical Bots, or regenerating attention timestamps during projection.

System-wide rule:

- owners expose versioned read/projection semantics for the state they own;
- apps/dashboards may normalize and aggregate those owner-declared schemas;
- transient UI/runtime buffers remain disposable when continuity belongs to another owner;
- unavailable owner state remains unavailable rather than becoming empty, zero or healthy;
- a runtime adapter is a connector, not permission or canonical ownership.

Promoted/current detail:

- `docs/MASTER-PLAN.md`
- `components/ai-verse-dashboard/COMPONENT-SPEC.md`
- `components/ai-verse-dashboard/QC.md`


---

## 2026-09-13 - Authenticated coordination control plane

**Status:** ACCEPTED-INTENT

The Multiple Bots audit found that current internal coordination authorization is much stronger than its HTTP ingress identity model.

The Gateway currently accepts actor IDs from request bodies, and the internal operator gate recognizes an operator-style ID convention. That is suitable only inside a trusted control boundary, not as remote caller authentication.

System-wide intended contract:

- authenticate the transport/control-plane caller;
- map that authenticated principal to the protocol principals it may act as;
- authorize the requested operation;
- only then apply component scope, lease, approval and policy checks.

This must be completed before a remote Dashboard/channel/control client is treated as trusted administration.

Promoted/current detail:

- docs/MASTER-PLAN.md
- components/ai-verse-multiple-bots/COMPONENT-SPEC.md
- components/ai-verse-multiple-bots/QC.md

---

## 2026-09-13 - Current-generation component compatibility contract

**Status:** ACCEPTED-INTENT

The Multiple Bots audit found a concrete example of integration drift: its Brain adapter still consumes the old tracked AI-VERSE.yaml Brain registration signal, while the current Brain lifecycle uses the local extension registry and treats tracked manifest registration as legacy.

System-wide intent:

- consumers should integrate through the owner component's current supported lifecycle/interface contract;
- a historical green integration test must not be treated as permanent proof of present compatibility;
- compatibility/evaluation suites should use current versioned contracts or owner-supported fixtures;
- one component should not maintain a private copy of another component's obsolete installation truth.

Promoted/current detail:

- docs/MASTER-PLAN.md
- components/ai-verse-multiple-bots/COMPONENT-SPEC.md
- components/ai-verse-multiple-bots/QC.md

---

## 2026-09-13 - Multiple Bots structured Data boundary

**Status:** ACCEPTED-INTENT

The Multiple Bots audit found no current AI-Verse Data adapter, contract or test.

The intended integration must preserve Data ownership:

    Bot / Worker Task
      -> bounded structured-data request
      -> host / OS permission and scope boundary
      -> AI-Verse Data owner API
      -> bounded result / receipt
      -> runtime context or coordination Artifact

Multiple Bots must not open Data SQLite directly or become another editable structured-data store.

Candidate durable Data writes should use the shared owner-routed write pipeline once canonical handlers exist.

Promoted/current detail:

- docs/MASTER-PLAN.md
- components/ai-verse-multiple-bots/COMPONENT-SPEC.md
- components/ai-verse-multiple-bots/QC.md

---

## 2026-09-13 - Canonical coordination-state migration

**Status:** ACCEPTED-INTENT

The Multiple Bots audit established that its SQLite database is not merely a disposable cache. It contains package-owned coordination objects, ordered events, deliveries and recovery state.

Before stable member release, canonical coordination-state evolution needs:

- explicit schema-version compatibility;
- migrations for supported older databases;
- safe failure on newer unsupported databases;
- backup/recovery expectations;
- uninstall preservation;
- release acceptance against existing persistent state.

This generalizes the system law that “derived indexes are disposable” only when they can actually be rebuilt from a stronger canonical source.

Promoted/current detail:

- docs/MASTER-PLAN.md
- components/ai-verse-multiple-bots/COMPONENT-SPEC.md
- components/ai-verse-multiple-bots/QC.md

---

## 2026-09-13 - Telemetry evidence must not become sibling canonical state

**Status:** ACCEPTED-INTENT

The Token audit confirms a system-wide ownership rule:

- usage telemetry may attribute activity to workspaces, projects, agents, Bots, Workers, Skills, tasks, automations and connections;
- those observations remain Token-owned evidence;
- a Dashboard/Data/Memory/Brain/Bots projection does not transfer canonical ownership;
- operational state must continue to come from the component that owns that responsibility.

A telemetry observation may inform a decision, but it must never silently become canonical operational state.

Promoted/current detail:

- `docs/MASTER-PLAN.md`
- `components/ai-verse-token/COMPONENT-SPEC.md`
- `components/ai-verse-token/QC.md`

---

## 2026-09-13 - Attribution is not authorization

**Status:** ACCEPTED-INTENT

The Token audit shows that workspace/project/agent/Bot/task IDs in telemetry are attribution facts, not proof of caller permission.

System-wide intent:

- hosts must apply an authorized scope floor before exposing scoped telemetry reads or writes;
- a caller cannot gain access merely by supplying another scope ID;
- Token must not become the canonical identity/ACL database merely to enforce this boundary;
- scoped readers/adapters should intersect requested filters with host-owned authorization.

Promoted/current detail:

- `docs/MASTER-PLAN.md`
- `components/ai-verse-token/COMPONENT-SPEC.md`
- `components/ai-verse-token/QC.md`

---

## 2026-09-13 - Telemetry readiness and monetary truth

**Status:** ACCEPTED-INTENT

Token establishes two reusable readiness/truth requirements.

First, telemetry readiness must distinguish:

`INSTALLED -> ATTACHED -> ENABLED -> SOURCE-ACTIVE -> COLLECTING -> PRICING-READY -> COST-READY -> AUTHORIZED -> READY`

No earlier state automatically implies a later one.

Second, monetary usage intelligence must preserve truth provenance:

- UNKNOWN is not zero;
- a trusted real zero remains real;
- ACTUAL and CALCULATED remain visibly distinct;
- calculated usage cost must not be presented as invoice-confirmed billing.

Promoted/current detail:

- `docs/MASTER-PLAN.md`
- `components/ai-verse-token/COMPONENT-SPEC.md`
- `components/ai-verse-token/QC.md`



---

## 2026-09-13 - External connection authority, readiness and credential opacity

**Status:** ACCEPTED-INTENT

The standalone Connections audit establishes several system-wide external-access laws.

A connection record is not proof that an external capability is usable. The mature system must preserve distinct states such as registered, configured, live-verified, healthy, authorized, approved and successfully executed.

Agents should normally receive opaque connection handles and bounded capabilities rather than raw credentials. Connections may own the handle and execution boundary while the raw secret remains in an approved credential backend such as an OS keychain, encrypted store or managed provider.

External side effects must re-check current scope, grants, delegated authority, approval and revocation at the actual provider execution edge. A previously discovered or planned capability must not survive later permission narrowing or revocation by relying on stale authority.

Connecting an external system also does not transfer canonical ownership of that system's records into AI-Verse. External data remains externally canonical unless an explicit ownership or synchronization contract says otherwise.

Promoted/current detail:

- `docs/MASTER-PLAN.md`
- `components/ai-verse-connections/COMPONENT-SPEC.md`
- `components/ai-verse-connections/QC.md`


---

## 2026-09-13 - Dynamic external-provider adoption can replace attachment

**Status:** PROMOTED

The Skills audit establishes a lifecycle exception to the generic component-attachment model.

A read-only external provider does not need a host-local attachment record when the host can discover it dynamically from a canonical/configured root and provider appearance changes no canonical authority or host-owned state.

The mechanism must remain late-install aware, absence aware, fail closed on incompatible state, and permission-neutral.

AI-Verse Skills is the current concrete implementation.

Promoted to:

- `docs/MASTER-PLAN.md`
- `components/ai-verse-skills/COMPONENT-SPEC.md`
- `components/ai-verse-skills/QC.md`

---

## 2026-09-13 - Integrity-valid is not trusted or authorized

**Status:** PROMOTED

The Skills audit confirms that package integrity, security/trust admission, environment readiness, scope authorization, action approval and effect verification are separate states.

A valid digest and pinned provenance prove what bytes were selected. They do not prove that a package is safely/licensably admitted or authorized to act.

This distinction must remain explicit for any future package, plugin, extension or capability marketplace.

Promoted to:

- `docs/MASTER-PLAN.md`
- `components/ai-verse-skills/COMPONENT-SPEC.md`
- `components/ai-verse-skills/QC.md`

---

## 2026-09-13 - Runtime support requires invocation acceptance

**Status:** PROMOTED

Directory exposure or adapter materialization alone should not be described as complete runtime support.

A runtime-support claim should be backed by a tested path equivalent to:

```text
discover
-> select
-> load required resources
-> invoke
-> obtain a verified outcome/receipt
```

This preserves a distinction between package visibility/adapter compatibility and real operational support.

Promoted to:

- `docs/MASTER-PLAN.md`
- `components/ai-verse-skills/COMPONENT-SPEC.md`
- `components/ai-verse-skills/QC.md`


---

## 2026-09-13 - Nested authority must be enforced at the final operation

**Status:** PROMOTED

The Data audit found that a wrapper can correctly declare a narrow top-level capability model and still accidentally widen authority inside a transaction or bulk envelope.

Current AI-Verse Data main demonstrates the failure mode: Apps deliberately expose read/create/update but a nested delete can be classified as update. The active Data hardening line repairs it.

System-wide rule:

> Every nested operation inside a batch, transaction, workflow or delegated action must be re-evaluated against the caller's effective authority. An outer envelope never grants broader authority to its contents.

Related rule:

> Provenance, audit and receipt APIs must not become a side channel that reveals the existence of resources the caller is not authorized to read.

Promoted to:

- docs/MASTER-PLAN.md
- components/ai-verse-data/COMPONENT-SPEC.md
- components/ai-verse-data/QC.md

---

## 2026-09-13 - Stateful adoption must precede empty initialization

**Status:** PROMOTED

The Data audit makes the existing-history migration rule concrete.

A stateful component must not initialize a new empty canonical store merely because its new canonical target path is empty when known eligible legacy/standalone state may already exist.

The safe lifecycle is:

~~~text
discover current canonical target
-> discover eligible legacy state
-> reconcile/adopt/migrate if required
-> verify one canonical route
-> initialize new state only when no canonical state needs adoption
~~~

This is especially important for Data because a bound standalone Data database cannot currently be reopened as native workspace Data, while ordinary portable import intentionally preserves binding identity.

Promoted to:

- docs/MASTER-PLAN.md
- components/ai-verse-data/COMPONENT-SPEC.md
- components/ai-verse-data/QC.md

---

## 2026-09-13 - Release acceptance must execute the real component path

**Status:** PROMOTED

The Data audit confirms the product-path acceptance rule with a concrete failure mode.

A release test that imports internal install/init/client primitives can prove that the pieces compose, but it does not prove that the actual materialized extension or host runtime can be discovered and used by a member installation.

System-wide rule:

> Final release acceptance must exercise the supported install -> attach/register -> enable/activate/init -> host/runtime use -> health/readiness path without hidden state patching or bypassing the public integration boundary.

Promoted to:

- docs/MASTER-PLAN.md
- docs/AUDIT-METHODOLOGY.md
- components/ai-verse-data/COMPONENT-SPEC.md
- components/ai-verse-data/QC.md

---

## 2026-09-13 - Cross-mode component state adoption

**Status:** ACCEPTED-INTENT

A component is not install-order independent merely because it safely blocks duplicate truth.

The Brain audit proved a concrete case: standalone Brain state under `.ai-verse-brain/` is correctly rejected once the same root becomes a native AI-Verse host, but no supported transaction adopts that canonical state into the native layout.

System-wide rule:

```text
standalone component first
+ compatible host later
must have a dry-run-first adoption/migration path
```

That path should detect competing stores, preserve provenance and stable identity where possible, map scopes explicitly, surface conflicts, verify the destination, and retire the old authority only after successful adoption.

Promoted/current detail:

- `components/ai-verse-brain/COMPONENT-SPEC.md`
- `components/ai-verse-brain/QC.md`

---

## 2026-09-13 - Rollback must restore or compensate

**Status:** ACCEPTED-INTENT

A lifecycle state named `ROLLED_BACK` is not, by itself, a rollback mechanism.

When AI-Verse documentation promises rollback/recovery, the implementation must provide one of:

- deterministic restoration to a known-good prior version/state;
- a verified compensating recovery when literal restoration is impossible.

The rollback path must preserve provenance and be acceptance-tested.

This applies beyond Brain to future prompts, strategies, skills, configuration, deployments and other evolvable system state.

Promoted/current detail:

- `components/ai-verse-brain/COMPONENT-SPEC.md`
- `components/ai-verse-brain/QC.md`

---

## 2026-09-13 - Contract surface is not operational integration

**Status:** ACCEPTED-INTENT

Exposing an adapter/provider method does not make that feature operational.

A component integration should be classified as implemented only when the current product path actually invokes the contract under the intended conditions and acceptance evidence proves the effect.

The Brain audit surfaced `query_data` as the concrete example: the host/bridge operation exists, but normal cognition does not currently consume it.

System documentation should therefore distinguish:

```text
interface exists
runtime consumes it
end-to-end effect verified
```

as separate readiness levels.

Promoted/current detail:

- `components/ai-verse-brain/SOURCE-MAP.md`
- `components/ai-verse-brain/QC.md`

---

## 2026-09-13 - Executable security-invariant labeling

**Status:** NEEDS-SCOPING

Security documentation must distinguish executable guarantees from protocol/operator prohibitions.

If a component claims that a class of sensitive material can never enter canonical state, either:

- enforce that claim at the appropriate persistence boundary, or
- narrow the wording to match the actual controls.

The exact generic detection/redaction strategy needs scoping so AI-Verse does not create a brittle or overly broad data-loss-prevention layer with high false positives.

Promoted/current detail:

- `components/ai-verse-brain/COMPONENT-SPEC.md`
- `components/ai-verse-brain/QC.md`


---

## 2026-09-13 - Milestone stopping rule and real-world dogfood

**Status:** PROMOTED

A passed immutable acceptance gate must remain passed unless new evidence proves a real regression, security violation within the gate threat model, data-loss/corruption issue, authority/isolation failure, or broken supported install path.

Future improvements do not retroactively make a passed dogfood milestone unfinished.

The frozen OS + Brain + Memory + Skills + Data first-member beta is now treated as ready for controlled personal dogfood.

Promoted to:

- `docs/FINAL-AI-VERSE-BLUEPRINT.md`
- `docs/DOGFOOD-UX-AND-PLATFORM-COMPLETENESS.md`

---

## 2026-09-13 - Progressive onboarding and invisible complexity

**Status:** ACCEPTED-INTENT

AI-Verse should pass a "grandma test": a new user should receive useful help without understanding Brain, Memory, Data, Skills, Bots, workspaces, MCP or canonical ownership.

First use should ask only the minimum needed to begin safely, then learn progressively during real work.

The system may propose Memories, Workspaces, Skills, Data schemas, Automations, durable Bots or temporary Workers when repeated evidence justifies them. Complexity remains inspectable for advanced users but hidden by default.

Promoted/current detail:

- `docs/DOGFOOD-UX-AND-PLATFORM-COMPLETENESS.md`
- `docs/FINAL-AI-VERSE-BLUEPRINT.md`

---

## 2026-09-13 - Thin AI-Verse Shell/Gateway before full Dashboard

**Status:** ACCEPTED-INTENT

Do not wait for the final native Dashboard before dogfooding the system.

The next interface milestone should be a small conversational AI-Verse Shell/Gateway over existing owner boundaries, with workspace binding, run state, approvals, cancellation and Brain/Memory/Skills/Data composition.

Where practical it should expose an OpenAI-compatible agent endpoint so an existing frontend such as Open WebUI can serve as a temporary user interface while the final Dashboard is informed by real usage.

Promoted/current detail:

- `docs/DOGFOOD-UX-AND-PLATFORM-COMPLETENESS.md`
- `docs/FINAL-AI-VERSE-BLUEPRINT.md`

---

## 2026-09-13 - Explicit host agent-loop contract

**Status:** ACCEPTED-INTENT

Every runtime publicly claimed as AI-Verse-compatible should prove an equivalent execution-loop contract covering intake, context assembly, model/tool execution, authorization, budgets, cancellation, pause/resume, retries, idempotency, checkpointing around side effects, no-progress protection, completion verification and receipts.

A user-facing `/goal` surface should map to Brain-owned intent/objective state rather than create a parallel goal store.

Promoted/current detail:

- `docs/DOGFOOD-UX-AND-PLATFORM-COMPLETENESS.md`
- `docs/FINAL-AI-VERSE-BLUEPRINT.md`

---

## 2026-09-13 - MCP as a first-class bidirectional interoperability surface

**Status:** ACCEPTED-INTENT

AI-Verse should support both:

- consuming approved external MCP servers through Connections/host policy;
- exposing selected bounded AI-Verse capabilities to external compatible agents through MCP without exposing raw internal stores or credentials.

Speaking MCP does not imply trust. Admission, identity/origin, capability mapping, tool-list change detection, tool-result trust, prompt-injection/tool-poisoning defenses, least privilege, rate limits, approvals and final-edge authorization remain mandatory.

Promoted/current detail:

- `docs/DOGFOOD-UX-AND-PLATFORM-COMPLETENESS.md`
- `docs/FINAL-AI-VERSE-BLUEPRINT.md`

---

## 2026-09-13 - Security is a release dimension

**Status:** ACCEPTED-INTENT

Security must be gated by the deployment threat model rather than deferred until the end.

Local single-user dogfood may use a narrower loopback-first threat model. Remote/closed/public releases require progressively stronger authenticated identity, secure transport, secret brokering, sandbox/tool policy, browser/network controls, rate limits, supply-chain admission, security auditability, backup/recovery and red-team/regression coverage.

Model instructions must never substitute for executable permission enforcement.

Promoted/current detail:

- `docs/DOGFOOD-UX-AND-PLATFORM-COMPLETENESS.md`
- `docs/FINAL-AI-VERSE-BLUEPRINT.md`

---

## 2026-09-13 - Controlled self-improvement promotion pipeline

**Status:** ACCEPTED-INTENT

AI-Verse should improve repeated work, but no privileged production behavior should silently rewrite itself.

The intended loop is:

`observe -> propose -> identify owner -> candidate version -> isolated test/eval -> compare -> approve by risk -> promote -> monitor -> rollback/compensate`.

This applies to Skills, prompts/instructions, workspace structure, Data schemas through migration, Brain strategy within its allowed bounds, Bot definitions, automations and Apps.

A 3-5 minute interval may trigger reflection during long work, but time alone must not automatically promote changes.

Promoted/current detail:

- `docs/DOGFOOD-UX-AND-PLATFORM-COMPLETENESS.md`
- `docs/FINAL-AI-VERSE-BLUEPRINT.md`


---

## 2026-09-13 - Benchmark-first feature synthesis

**Status:** ACCEPTED-INTENT

Important AI-Verse behaviors should not be invented from one user request when mature systems already implement the same concept.

For features such as persistent goals, self-learning, skill improvement, agent loops, cadence, approvals, MCP, sandboxing, onboarding and remote execution, first compare the strongest existing implementations, extract common primitives/failure modes and then synthesize the AI-Verse version.

Current concrete examples:

- `/goal`: compare Codex, Hermes and OpenClaw;
- self-learning/Skill improvement: compare Hermes, OpenClaw and Letta.

Promoted/current detail:

- `docs/DOGFOOD-UX-AND-PLATFORM-COMPLETENESS.md`

---

## 2026-09-13 - Unified AI-Verse distribution and component UX

**Status:** ACCEPTED-INTENT

Normal users should eventually install AI-Verse as one product rather than manually install ten repositories.

The internal repositories may remain independent. A distribution/meta-installer should pin compatible versions, orchestrate component-owned install/adopt/init steps, run final readiness checks and expose one consistent component command vocabulary.

A future monorepo is optional and should be chosen for developer-maintenance reasons, not because one-line installation requires it.

Promoted/current detail:

- `docs/DOGFOOD-UX-AND-PLATFORM-COMPLETENESS.md`


---

## 2026-09-13 - Gateway and Automations become first-class repositories

**Status:** ACCEPTED-INTENT

The public-beta synthesis identifies two concepts large enough to need dedicated implementation ownership:

- **AI-Verse-Gateway** for user/client/runtime ingress, run-loop transport/control, streaming, approvals/cancellation and remote client security without domain-truth ownership.
- **AI-Verse-Automations** for schedules, triggers, recurring jobs, wake delivery, retries/recovery and automation-run lifecycle.

MCP, Goals, Self-learning, Agent Loops, Security, Identity/RBAC and Evals do not get separate repositories at this stage.

Promoted/current detail:

- `docs/PUBLIC-BETA-EXECUTION-PLAN.md`
- `docs/FINAL-AI-VERSE-BLUEPRINT.md`

---

## 2026-09-13 - Standard install/setup language for every component

**Status:** PROMOTED

All current and future components should converge on one product vocabulary:

`install -> setup -> status -> doctor -> enable/disable -> update -> uninstall`

Component-specific semantics remain owner-controlled and setup must not silently transfer authority.

The product-level `aiverse` CLI will wrap existing native commands rather than forcing mature components to rewrite their internals solely for naming consistency.

Promoted to:

- `docs/COMPONENT-INSTALL-SETUP-CONTRACT.md`
- `docs/PUBLIC-BETA-EXECUTION-PLAN.md`

---

## 2026-09-13 - Benchmarked Persistent Goals contract

**Status:** PROMOTED

Fresh benchmark-first research across Hermes Persistent Goals, OpenClaw Goal, current OpenAI Codex Goal source/current failure evidence and Prime Agent established the exact AI-Verse Goal contract.

Key promoted decisions:

- Brain remains the only canonical Goal/intent owner.
- Gateway owns autonomous continuation but stores only bindings/leases, not a second Goal.
- every autonomous turn revalidates goal_id, Brain version, activation epoch, scope, authority and budget;
- completion is an evidence-backed Brain verification transaction, not a judgment of the last assistant response;
- waiting consumes no model turns;
- repeated no-progress is host-circuit-broken;
- Goal state is not a cron/task/standing-order substitute;
- Automations may wake an explicitly eligible Goal by goal_id without copying Goal state;
- Multiple Bots may coordinate delegated work but cannot complete the Brain Goal;
- default public-beta continuation window is 20 turns per activation epoch.

Promoted to:

- `docs/GOALS-BENCHMARK-AND-CONTRACT.md`
- `docs/FINAL-AI-VERSE-BLUEPRINT.md`

---

## 2026-09-13 - Benchmarked self-learning Skill lifecycle

**Status:** PROMOTED

Fresh benchmark-first research across Hermes /learn, /refine and Curator, OpenClaw Self-learning/Skill Workshop, Letta continual learning/Skills and Prime Agent continual harness established the exact AI-Verse self-learning contract.

Key promoted decisions:

- Brain evaluates improvement opportunities.
- Memory owns historical evidence.
- Skills owns reusable package proposals, immutable generations, admission/evals, promotion, protection, curation and rollback.
- Gateway/Automations may trigger review but never own learned Skill state.
- public-beta default mode is `propose`, not direct autonomous production editing;
- `auto` is restricted to low-risk agent-learned content after all gates pass;
- new active Skills, executable/permission-expanding changes and changes to user/first-party/third-party content require explicit approval;
- background review permissions are owner- and operation-scoped;
- duplicate prevention is executable, not prompt-only;
- active generation bytes are never rewritten in place by learning;
- automatic hard purge is forbidden.

Promoted to:

- `docs/SELF-LEARNING-BENCHMARK-AND-CONTRACT.md`
- `docs/FINAL-AI-VERSE-BLUEPRINT.md`



---

## 2026-09-14 - AI-employee product shell and deferred Kylon/Grok-Bot competitive gaps

**Status:** ACCEPTED-INTENT

The owner clarified that the near-term AI-Verse product remains deliberately **single-user first**, primarily local with optional private VPS/VPN use.

The immediate product priority is not enterprise/multi-user expansion. It is making the already-built system visible through a focused shell where:

- the main AI-Verse chat remains primary;
- permanent Bots/AI employees are clearly visible beside it;
- Bot roles, availability/activity and delegated work are discoverable;
- temporary Worker activity can surface when relevant;
- current workspace/scope and meaningful work status are visible;
- approvals/attention can surface without exposing backend architecture.

Multiple Bots is already a strong backend coordination engine, but the product currently risks hiding that value because there is no user-operable interface centered on chat + AI team.

A borrowed shell such as Open WebUI is acceptable for temporary dogfood, but is not considered the final answer if it cannot expose AI-Verse-specific team/Bot/work concepts cleanly.

### Near-term priority

Build a **thin single-user AI-Verse shell**, not a giant Dashboard rewrite.

Prefer using existing Gateway, Multiple Bots, OS and owner-backed projections. The shell must remain non-canonical.

### Deliberately deferred competitive gaps

The following Kylon/Grok-Bot-style product capabilities are valid future directions but are deliberately low priority until the single-user shell and current implementation tracks are strong:

- public/multi-user account system;
- human-team invitations/membership;
- organization administration;
- enterprise RBAC/SSO/SCIM;
- broad public SaaS tenancy;
- human/AI shared-company roster semantics beyond the single owner;
- enterprise collaboration controls;
- large-scale external-user administration.

Other future product gaps to revisit after the shell proves daily use:

- richer persistent per-Bot working-environment/computer UX where it adds real value;
- broader simplified app/account connection UX;
- room/workspace surfaces combining conversation, AI employees, Data and Apps;
- generated Apps/views over AI-Verse Data;
- stronger visible asynchronous/background-work experience.

These are retained so they are not forgotten, but they must not distract from the current single-user interface milestone.



---

## 2026-09-14 - Invisible friction capture and privacy-safe member feedback loop

**Status:** DEFERRED

The owner wants AI-Verse to eventually notice moments where the user is clearly dissatisfied with system behavior and preserve enough structured evidence to improve the product without requiring the user to stop and write a bug report.

Examples include:

- the answer was wrong or ignored an instruction;
- a Skill performed badly;
- Memory was stale, overconfident, or used the wrong fact;
- information was routed to the wrong canonical owner/workspace;
- the agent made an unwanted assumption;
- a Bot/Worker delegated or coordinated poorly;
- an Automation behaved unexpectedly;
- the user explicitly corrects the system or expresses frustration with the result.

Desired future flow:

```text
normal work
    -> bounded frustration/correction signal detected
    -> capture a local structured friction record
    -> include only the minimum technical evidence needed to explain what happened
    -> redact secrets, personal data and unrelated conversation
    -> classify likely owner/subsystem and failure type
    -> optionally use the record locally for repair/learning
    -> optionally submit a sanitized product-feedback report upstream with user consent
```

### Local-first requirement

Every installation should be able to keep its own private friction log without sending anything externally.

This local record may reference private trace/session/run IDs so the user's own AI-Verse installation can inspect exact evidence later.

### Universal member feedback

A future member-facing product may offer an **opt-in upstream feedback channel** so many installations can contribute product-quality evidence.

Do **not** implement this as a world-writable shared file or repository path.

A safer design is a controlled ingestion endpoint or repository issue bot that accepts a strict structured schema, rate-limits submissions, strips unsupported fields and never grants clients repository write credentials.

The upstream report should contain only sanitized information such as:

- failure category;
- affected component/interface;
- expected behavior;
- observed behavior;
- high-level preceding conditions;
- software/release versions;
- anonymous installation/build fingerprint if useful;
- whether the signal was explicit user correction, explicit negative feedback, or model-inferred frustration;
- optional reproducibility/debug references that are safe to share.

Raw conversation text, credentials, private files, personal Memory, business Data and full prompts must **not** be uploaded by default.

If richer context would materially help, ask the user before attaching it or provide a review screen.

### Signal-quality requirement

Frustration detection is an imperfect model inference and must not be treated as proof that the software is wrong.

Distinguish at least:

- explicit user correction / "this is wrong";
- explicit negative feedback / complaint;
- repeated repair attempts;
- inferred frustration;
- system-detected contradiction/failure.

False-positive inferred frustration should not silently rewrite Skills, Memory, policy or product behavior.

### Product-learning boundary

This feedback system may generate evidence and repair candidates, but canonical owners remain responsible for actual changes.

Examples:

- Memory problem -> Memory evidence/repair path;
- Skill problem -> Skills proposal/evaluation path;
- routing problem -> relevant owner/runtime;
- product-wide recurring bug -> maintainer/product feedback queue.

No remote feedback collector gains authority over a member's installation.

### Priority

Useful future capability, but deliberately **not part of the current milestone**.

Current priorities remain:

1. finish active implementation tracks;
2. dogfood the released Agent product;
3. build the focused single-user shell;
4. learn from real usage;
5. only then productize automatic friction capture if the real dogfood evidence justifies it.

