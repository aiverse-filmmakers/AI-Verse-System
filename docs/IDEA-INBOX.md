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
