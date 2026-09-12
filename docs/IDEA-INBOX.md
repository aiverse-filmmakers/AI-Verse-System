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
