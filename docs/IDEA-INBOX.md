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
