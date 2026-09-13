# AI-Verse Public Beta Execution Plan

### Token current status

**Updated 2026-09-13:** the exact audited `@ai-verse/token@0.1.0-alpha.1` artifact was recovered and restored without reconstructing missing Git history. A `0.1.0-beta.1` implementation now closes the planned Token operational gaps: setup/activation, durable runtime materialization, default local collector orchestration and actual collection, concrete pricing transport, ACTUAL/CALCULATED/UNKNOWN primary reads, mandatory host/local-owner read authorization, deeper doctor/readiness, Gateway/Dashboard owner projections, Multiple Bots attribution boundaries, and state-preserving lifecycle behavior.

Local acceptance passes **255/255 normal tests plus 3/3 release tests**, including a clean packed install. Immutable source/package/Git-bundle artifacts and local tags exist.

The remaining Token release step is external: create/push the canonical `aiverse-filmmakers/AI-Verse-Token` remote and run its configured Ubuntu/macOS/Windows Node 22/24 matrix. The current connected GitHub toolset cannot create a new repository, so hosted CI/public remote evidence must not be claimed yet.


**Status:** Canonical execution plan  
**Date:** 2026-09-13  
**Goal:** Reach a coherent public-beta system before broad personal/member testing without reopening completed engines indefinitely.

## 1. Scope rule

Public beta is a defined release target, not "all future AI-Verse ideas complete."

A public-beta blocker is something required by the declared beta experience, threat model or supported compatibility matrix.

Later enterprise, marketplace, hosted multi-user, large-scale, or experimental capabilities remain later milestones unless explicitly pulled into beta.

## 2. Repository classification

### New repository required: AI-Verse-Gateway

Reason:

The human/client/runtime ingress is large enough to deserve its own deployable lifecycle and must remain independent from Dashboard presentation and Multiple Bots coordination.

It should own:

- one stable local/server endpoint for AI-Verse clients;
- chat/run ingress;
- workspace/system/session binding;
- runtime/agent adapter selection;
- the host execution-loop contract;
- streaming events;
- pause/resume/cancel control;
- approval interrupts;
- OpenAI-compatible agent API where practical;
- client authentication/session security for remote exposure;
- protocol projections for health/run state.

It must not own:

- Memory;
- Brain goals;
- Data records;
- Skills;
- Bot coordination truth;
- connection credentials;
- Dashboard UI state beyond transport/session concerns.

Existing Dashboard `apps/gateway` and Multiple Bots Gateway code must be treated as evidence/reusable implementations, not silently duplicated. The new Gateway design should decide what is generalized, what remains component-private, and how Dashboard/Bots connect to the shared edge service.

**Current implementation status (2026-09-13):**

- a public-beta implementation candidate has been built and locally acceptance-tested as `0.1.0-beta.1`;
- it implements the standard lifecycle, OpenAI-compatible client ingress, first-class runs, SSE streaming, durable session/run checkpoints, stop/cancel, pause/resume, approval interrupts, bounded budgets/deadlines, no-progress protection, restart recovery, loopback-by-default security, bearer principal identity, CORS/origin controls, bounded bodies/rates, privileged-control audit receipts, OS host composition, and a Brain-owned Goal continuation adapter boundary;
- it includes cross-platform GitHub Actions configuration for Linux/macOS/Windows and a clean-install acceptance suite;
- it does not create a second Goal, Memory, Data, Skills, Bots, Connections, Token, or Dashboard source of truth;
- the implementation is **not yet a canonical released repository** until `aiverse-filmmakers/AI-Verse-Gateway` is actually published, tagged/pinned and its remote CI passes;
- composed Goal continuation remains activation-pending until Brain exposes the canonical benchmarked Goal-owner API. Gateway intentionally fails closed rather than inventing Goal state.

This means Gateway architecture/implementation is materially closed, but public-beta release evidence is not complete yet.

### New repository required: AI-Verse-Automations

Reason:

AI-Verse already has automation definitions/cadence concepts and Multiple Bots explicitly receives automation wakes while refusing to become a scheduler. Brain emits cadence plans but intentionally does not own scheduling. This leaves a real canonical runtime-owner gap.

It should own:

- scheduler runtime;
- cron/time triggers;
- event/webhook trigger normalization;
- recurring jobs;
- trigger/job lifecycle;
- retry/backoff/dead-letter policy for automation invocation;
- wake delivery into Brain/Bots/Gateway owner boundaries;
- automation run receipts/status;
- pause/resume/run-now;
- safe restart/recovery.

It must not own:

- strategic goals;
- Bot task coordination;
- external credentials;
- canonical business Data;
- Memory.

### Existing repository to repurpose: ai-verse-distribution

Do not create another installer repository.

Repurpose the existing repository into the one-product distribution/meta-installer described by `docs/COMPONENT-INSTALL-SETUP-CONTRACT.md`.

Its current legacy profile-package material should be preserved as historical evidence or migrated deliberately, not silently overwritten.

## 3. No new repository required

### MCP

Do not create `AI-Verse-MCP` now.

MCP is an interoperability protocol, not a canonical truth owner.

Target ownership:

- Connections: external MCP server registration, authentication, health and capability handles;
- Gateway/host: MCP client transport and bounded invocation where needed;
- owner components: optional MCP server projections over their supported APIs;
- OS: outer scope/permission floor.

If MCP later develops substantial independent package/runtime state that cannot fit these owners, revisit the decision.

### Goals

No `AI-Verse-Goals` repo.

Brain already owns explicit intent, desired state, objectives, verification and strategy.

The public `/goal` UX and goal continuation engine must be benchmarked across current systems and implemented as Brain-owned goal state plus host/Gateway loop behavior.

### Self-learning / self-improvement

No `AI-Verse-Learning` repo.

Ownership is intentionally split:

- Brain: improvement decision/evaluation and strategic learning;
- Memory: historical evidence and recalled lessons;
- Skills: reusable learned procedure package lifecycle;
- Gateway/Automations: trigger execution of reflection/maintenance loops;
- Distribution/System: release safety and cross-component acceptance.

### Agent loops

No `AI-Verse-Loops` repo.

The loop is a host execution contract. Gateway should implement the user-facing run loop; Multiple Bots has its own coordination execution loop; Brain supplies cognition/goal state; Automations wakes work.

### Security

No `AI-Verse-Security` repo for public beta.

Security remains a cross-cutting contract enforced at actual boundaries:

- OS policy/scope;
- Gateway identity/session/transport;
- Connections secrets and external execution;
- component storage isolation;
- Skills/App package admission;
- Multiple Bots delegation;
- Distribution/release supply-chain verification.

A separate Security repo is justified later only if AI-Verse develops a substantial independent security product/runtime such as a scanner, policy engine or security-event service.

### Identity / RBAC

No separate repo yet for the local/small public beta.

Gateway authentication plus OS scope/permission policy is sufficient for the initial threat model.

Revisit `AI-Verse-Identity` when hosted multi-user/team tenancy, SSO/OIDC/SCIM or durable human-role management becomes a committed product requirement.

### Evals

No separate repo now.

Component evals remain beside owning code. Cross-system acceptance belongs in System/Distribution release gates.

## 4. Benchmark-first features pulled into beta

The following user-facing behaviors are desired for the first useful Agent profile, but must be implemented from comparative research rather than invented:

### Persistent goals

Compare at minimum:

- Hermes Persistent Goals;
- OpenClaw Goal;
- Codex goal behavior where primary evidence is available.

Extract:

- durable goal state;
- one-goal vs many-goal model;
- completion contract;
- verification/judge;
- continuation;
- turn/token/time budget;
- pause/resume/block/complete/clear;
- subgoals/criteria;
- quality gates;
- race/idempotency behavior;
- operator-only mutations;
- relation to tasks/Bots/Automations.

Brain remains the canonical goal owner.

### Self-learning and Skill evolution

Compare at minimum:

- Hermes self-improvement + Curator;
- OpenClaw Self-learning + Skill Workshop;
- Letta learned Skills/continual learning.

Extract:

- eligibility triggers;
- foreground correction vs background review;
- off/propose/auto modes;
- provenance/ownership;
- proposals/diffs;
- scanners/evals;
- pin/protect rules;
- versioning/backup/rollback;
- usage metrics;
- stale/archive lifecycle;
- consolidation/deduplication;
- privacy/cost controls;
- user approval levels.

Skills owns reusable Skill packages. Brain/Memory provide improvement evidence; Automations/Gateway provide triggers.

## 5. Public beta build program

### Track A: close existing near-finished repos

- OS: public-beta lifecycle UX/readiness/reconcile closure.
- Brain: lifecycle symmetry, standalone/native adoption, real rollback semantics where promised, current immutable release, owner-routed integration, benchmarked Goal UX.
- Memory: migration authority handoff, remaining migration edge cases, write/concurrency hardening, full lifecycle/reconcile and release packaging.
- Skills: trust/admission, licensing decision, benchmarked self-learning/Workshop lifecycle, real runtime invocation acceptance, public release packaging.
- Multiple Bots: finish Phase 5 productization from current Phase 5.1 onward.
- Token: operationalize/install/activate/collect/read/authorize and publish a current repository artifact before calling it public beta.

Data remains frozen unless a real regression/public-beta requirement is demonstrated.

### Track B: create missing first-class runtime owners

- Gateway.
- Automations.

### Track C: one-product distribution

Repurpose `ai-verse-distribution` around the standard install/setup contract.

### Track D: secure interoperability

- Connections v1, including MCP as one supported external tool/integration class.
- Do not block first local public-beta shell on broad provider coverage, but do not claim secure arbitrary external action before Connections exists.

### Track E: temporary and final UI

- Gateway should support an existing UI such as Open WebUI for early web access.
- Dashboard remains the eventual native control room and should consume owner/Gateway contracts rather than block backend beta.

## 6. Release acceptance target

The Agent public-beta profile passes only when a clean install proves:

1. one distribution command/path installs exact compatible versions;
2. setup is explicit and consistent;
3. onboarding gets a non-technical user to first useful task;
4. Gateway provides chat/run access;
5. Brain goal mode works with bounded continuation/verification;
6. Memory recall and learning evidence work;
7. Skills can be used and improved through governed lifecycle;
8. Data structured truth works;
9. Multiple Bots can be optionally used through its product path;
10. Automations can wake/continue bounded work;
11. Token records usage/cost truth when enabled;
12. security baseline matches local/remote claims;
13. system doctor reports truthful readiness;
14. update/disable/reinstall preserve claimed canonical state;
15. no component requires hidden manual repository edits.

## 7. Stop rule

After this gate passes on immutable artifacts, new ideas become the next release unless they expose:

- a security vulnerability inside the declared threat model;
- data loss/corruption;
- authority/isolation failure;
- broken install/setup path;
- current-generation incompatibility;
- failed acceptance evidence.

This is how AI-Verse stops cycling between "finished" and "unfinished."


## 8. Current execution status

**Updated:** 2026-09-13

Completed prerequisites:

- `docs/GOALS-BENCHMARK-AND-CONTRACT.md` exists and is canonical.
- `docs/SELF-LEARNING-BENCHMARK-AND-CONTRACT.md` exists and is canonical.
- `aiverse-filmmakers/ai-verse-distribution` has been reset from the pre-current-project profile experiment and restructured as the current Distribution/meta-installer foundation.
- the old Distribution tree remains available through Git history but is not current product truth.

This unblocks Brain and Skills public-beta implementation against real benchmarked contracts rather than guessed behavior.
