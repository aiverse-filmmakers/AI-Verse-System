# AI-Verse Multiple Bots Source Map

**Component:** AI-Verse Multiple Bots  
**Canonical repository:** aiverse-filmmakers/AI-Verse-Multiple-Bots  
**Reviewed branch:** main  
**Reviewed head:** 9874d413f5e23c9a869bf3ccead0f2751026a732  
**Reviewed tree:** 37737a579bd4c6984ba31b3d786d0e225e2e92ee  
**Review date:** 2026-09-13

This source map records the evidence used to reconstruct the component specification. It is not a code listing. Evidence priority follows docs/AUDIT-METHODOLOGY.md: current executable behavior and current tests outrank stale prose.

---

## 1. Audit anchor

The audit began with:

- AI-Verse-System/docs/AUDIT-METHODOLOGY.md

The independent component baseline was then built from AI-Verse-Multiple-Bots before consulting any sibling component specification.

After the baseline, the following AI-Verse-System documents were used only for cross-component contract comparison:

- docs/MASTER-PLAN.md
- docs/LIVING-SPEC-PROTOCOL.md
- docs/COMPONENT-TEMPLATE.md
- components/ai-verse-brain/COMPONENT-SPEC.md
- components/ai-verse-os/COMPONENT-SPEC.md

No sibling implementation repository was audited in this pass.

---

## 2. Repository identity and distribution evidence

### Top-level identity

- package.json
  - package: @ai-verse/multiple-bots
  - version: 0.1.0-alpha.1
  - Node requirement: >=22.5.0
  - TypeScript build/test scripts
  - no final public member packaging contract yet

- README.md
  - useful identity and quick-start material
  - progress section is stale relative to BUILD-MAP and current code

- src/index.ts
  - public code export surface

- src/cli.ts
  - current CLI and serve/lifecycle surface

### Release evidence

At audit time:

- no latest GitHub Release was returned by the release endpoint;
- no tag namespace was returned;
- current branch main was not protected.

These facts are release-governance evidence, not runtime architecture evidence.

---

## 3. Current canonical progress evidence

### docs/BUILD-MAP.md

Highest-value current planning/status source.

At reviewed head it states:

- Phase 0 complete;
- Phase 1 complete;
- Phase 2 complete;
- Phase 3 complete;
- Phase 4 approximately 80 percent;
- Phase 4.1 through 4.8 complete;
- Phase 4.9 compatibility/evaluation suite is NEXT and has not started;
- Phase 5 Product/Install/Dashboard is not started;
- directional overall first-release progress roughly 95 percent.

### docs/PHASE-4-STATUS.md

Current Phase 4 acceptance ledger.

It records the implementation and acceptance proofs for:

- A2A;
- Hermes;
- OpenClaw;
- Codex/Claude Code;
- external-managed Bot runtime;
- remote identity/auth;
- remote capability/environment leases;
- retry/disconnect/reconnect semantics.

### docs/PHASE-3-STATUS.md

Useful evidence for native-integration implementation history.

Important limitation:

- its final next-gate language is stale and still says Phase 4 has not started.

### docs/PHASE-2-STATUS.md and docs/PHASE-1-STATUS.md

Historical/current gate evidence for the completed coordination and dynamic-squad foundations.

---

## 4. Core architecture evidence

### docs/PERSISTENT-TEAMMATE-ARCHITECTURE.md

Defines the persistent-teammate thesis:

- durable Bots;
- temporary Workers;
- ownership boundaries;
- Rooms/Threads;
- delegation versus handoff;
- capability/environment leases;
- approvals;
- portable runtimes;
- anti-duplication laws.

Important drift:

- older storage text describes SQLite as derived/disposable;
- current code proves the coordination database contains canonical package coordination state.

### docs/COORDINATION-PROTOCOL-V1.1.md

Defines the strongest protocol intent:

- stable identity;
- trusted workspace;
- Task/Message/Artifact separation;
- delegation/handoff distinction;
- Bot/Worker distinction;
- one owner;
- constraint preservation;
- leases;
- provenance;
- idempotence and ordering;
- approval/budget/cancellation semantics;
- remote adapter expectations.

This protocol is important when judging implementation gaps such as direct-message retry behavior.

### docs/ARCHITECTURE-BLUEPRINT.md

Architecture decomposition and planned boundaries.

### docs/IMPLEMENTATION-ROADMAP.md

Historical implementation sequencing.

Current progress claims defer to BUILD-MAP.

---

## 5. Canonical coordination state and persistence

### src/store.ts

Primary evidence for current package state ownership.

Current responsibilities include:

- SQLite coordination database;
- schema version table;
- generic protocol object storage;
- ordered Events;
- Room sequence;
- deliveries;
- idempotency records;
- atomic mutations;
- structural doctor.

Key finding:

- current SQLite is not merely a disposable cache.

### src/types.ts

Core TypeScript protocol/runtime types.

### src/validator.ts

Protocol validation boundary.

### schemas/coordination-v1.schema.json

Schema evidence for the coordination v1 object family.

### src/id.ts

Identity generation helpers.

---

## 6. Durable Bot identity and lifecycle

### src/bot-registry.ts

Primary evidence for:

- durable Bot registration;
- active/disabled/archived lifecycle;
- address collisions;
- workspace/operator scope;
- manager relationship checks;
- peer policy;
- external-managed binding uniqueness;
- archive/live-work guards.

### templates/bot.yaml

User-facing manifest direction.

### test/bot-registry.test.ts and related registry/lifecycle tests

Executable acceptance evidence for durable identity behavior.

---

## 7. Messaging, Rooms and delivery

### src/gateway.ts

Primary evidence for:

- direct message mutation;
- delivery creation;
- event publication;
- Bot lifecycle operations;
- Task creation;
- Handoffs;
- approvals.

Important current finding:

- sendMessage creates a fresh Message and delivery on each call;
- optional idempotencyKey is applied only to the Event emission.

### src/rooms.ts

Primary evidence for:

- Room membership;
- Threads;
- speaker selection;
- temporary discussion;
- work ownership;
- bounded group behavior.

### test/gateway.test.ts

Current direct-message acceptance evidence.

Important negative:

- it does not prove same-key direct-message replay creates only one Message/delivery.

### Room-related tests

Used as evidence for membership, speaker and topology behavior.

---

## 8. Delegation, Handoff and authority

### src/policy.ts

Primary internal authority/policy evidence:

- exact workspace checks for registered Bot principals;
- peer restrictions;
- tool/connection/skill bounds;
- parent/root constraint preservation;
- hop ceilings;
- budget inheritance;
- duplicate-active Task protection;
- handoff target validation.

### src/constraints.ts

Constraint normalization and preservation.

### src/budget.ts

Budget normalization/inheritance.

### src/loop-guard.ts

Cycle/repetition/no-progress safety.

### test/delegation-hardening.test.ts
### test/handoff-hardening.test.ts
### test/safety-ii.test.ts
### test/cancellation.test.ts
### test/approvals.test.ts

High-value enforcement tests.

---

## 9. Execution queue and local recovery

### src/execution-queue.ts

Durable queue evidence:

- queued/claimed/running/completed/failed/canceled/dead_letter states;
- execution leases;
- heartbeats;
- recovery policy;
- attempt count.

### src/recovery.ts

Local stale-execution behavior:

- retry_safe requeue;
- manual dead-letter;
- operator dead-letter retry.

### src/supervisor.ts

Startup/periodic recovery and terminal reconciliation.

### test/recovery.test.ts

Important evidence that generic retry_safe is a caller-selected recovery classification in current public input.

---

## 10. Bot/Worker execution principal

### src/principal-runner.ts

One of the highest-value executable architecture files.

Proves:

- shared Bot/Worker execution engine;
- Worker lineage validation;
- exact Task/principal/workspace lease checks;
- environment checks;
- cancellation and terminal fences;
- Artifact provenance;
- budget accounting;
- Team Run aggregate usage;
- runtime wrapper integration.

### src/runner.ts

Runner orchestration and settlement.

### src/runtime.ts

Host-neutral runtime interfaces and common runtime execution contracts.

---

## 11. Team Run and temporary Worker architecture

### src/team-runs.ts

Primary evidence for:

- Team Run object/lifecycle;
- topology selection;
- Worker creation;
- run/workspace binding;
- leader-only control;
- Worker authority ceilings.

### src/team-run-manager.ts
### src/team-run-fanout.ts
### src/team-run-handoff.ts
### src/team-run-discussion.ts
### src/team-run-disagreement.ts
### src/team-run-verifier.ts
### src/team-run-synthesis.ts
### src/team-run-decision.ts
### src/team-run-control.ts
### src/team-run-cleanup.ts

Together these implement:

- manager topology;
- parallel fan-out;
- direct transfer;
- bounded discussion;
- disagreement detection;
- selective verification;
- leader synthesis;
- adaptive collaboration decision;
- aggregate run control;
- temporary cleanup.

### Team Run test family

The repository contains dedicated tests for these slices. They are treated as stronger evidence than architecture prose.

---

## 12. AI-Verse OS integration

### src/ai-verse-os-registration.ts

Current local extension registration/upgrade/uninstall contract.

### docs/AI-VERSE-OS-REGISTRATION-CONTRACT.md

Documents:

- .aiverse/extensions/registry.json ownership;
- no tracked OS mutation;
- installed versus registered versus enabled versus healthy versus authorized;
- safe registry locking/atomicity.

### src/ai-verse-os-workspace-projection.ts

Read-only workspace/current-context projection.

### docs/AI-VERSE-UPGRADE-UNINSTALL-SAFETY.md

Upgrade/uninstall ownership and preservation contract.

### docs/AI-VERSE-FOUR-CS-HEALTH.md
### src/four-cs-health.ts

Read-only Four Cs evidence projection.

---

## 13. Brain integration

### src/brain-objective-ingress.ts

Current executable Brain ingress source.

Key current behaviors:

- exact workspace Brain object loading;
- objective/initiative/intent projection;
- semantic root objective digest;
- direction-ownership check;
- Brain installation check;
- execution-time freshness.

Critical current defect:

- parseBrainExtensionRegistration reads top-level AI-VERSE.yaml extensions.brain and requires supported/enabled there.

### src/brain-objective-runtime.ts

Execution-time strategic freshness wrapper.

### docs/AI-VERSE-BRAIN-OBJECTIVE-INGRESS.md

Historical Phase 3.3 integration contract.

It explicitly lists AI-VERSE.yaml Brain registration as an authority prerequisite.

### test/brain-objective-ingress.test.ts

Critical fixture evidence:

- test host explicitly writes an AI-VERSE.yaml extensions.brain block;
- therefore current tests validate the old integration generation.

### test/brain-objective-ingress-contract.test.ts

Strong local idempotency/contract evidence for Brain ingress once a Brain projection has been supplied.

### Cross-component comparison after independent baseline

AI-Verse-System/components/ai-verse-brain/COMPONENT-SPEC.md states:

- current Brain main uses .aiverse/extensions/registry.json;
- tracked manifest Brain registration is legacy;
- current Brain attachment/init does not require the old extensions.brain slot.

This comparison establishes a current contract drift in Multiple Bots.

---

## 14. Memory integration

### src/ai-verse-memory-recall.ts
### src/memory-recall-runtime.ts

Evidence for:

- native installed Memory boundary;
- bounded task-scoped recall;
- exact workspace/operator scope;
- no direct ownership of Memory database;
- ephemeral recalled content;
- provenance/digest-only persistence.

### docs/AI-VERSE-MEMORY-RECALL.md

Canonical Phase 3.4 intent.

### Memory integration/hardening tests

Used as enforcement evidence for source ownership, path safety and scope.

---

## 15. Skills integration

### src/ai-verse-skills-capability-resolution.ts
### src/skills-capability-runtime.ts

Evidence for:

- OS-owned Skills capability resolver;
- exact capability reference binding;
- explicit per-Task skills;
- Worker subset behavior;
- package/instruction digest checking;
- ephemeral instructions;
- no permission widening.

### docs/AI-VERSE-SKILLS-CAPABILITY-RESOLUTION.md

Canonical Phase 3.5 contract.

### Skills tests

Used as enforcement evidence for workspace/package binding and authority separation.

---

## 16. Data integration negative evidence

Negative searches were performed in AI-Verse-Multiple-Bots for:

- “AI-Verse Data”
- “ai-verse-data”
- “query_data”
- “Data integration”
- “structured data”

No Multiple Bots Data implementation/contract result was found.

The source tree also contains no Data-specific adapter/module.

The docs tree contains no AI-Verse Data integration contract.

The test tree contains no Data integration test.

The current BUILD-MAP has no Data integration slice.

Therefore the statement “Data integration is absent” is evidence-backed negative space, not inference from one missing README sentence.

### Cross-component owner comparison

AI-Verse-System/components/ai-verse-os/COMPONENT-SPEC.md establishes the current host law that Data owns:

- records;
- schemas;
- queries/aggregates;
- relations;
- transactions;
- idempotency;
- events/receipts;
- integrity;
- migration/backup/recovery.

OS must call Data through Data’s supported boundary rather than open its SQLite directly.

That law is used only to define the correct direction for the missing Multiple Bots Data bridge.

---

## 17. Automations and owner-routed writes

### src/automation-wake-ingress.ts
### docs/AI-VERSE-AUTOMATION-WAKE-SCHEDULE.md

Receive-side automation integration.

Key law:

- Multiple Bots receives an occurrence;
- it does not become the scheduler.

### src/os-write-command.ts
### docs/AI-VERSE-OS-WRITE-COMMAND-BOUNDARY.md

Owner-controlled write intake.

Key limitation:

- transport/receipt boundary exists;
- current OS queue does not itself claim canonical effect.

### src/candidate-writeback.ts
### docs/AI-VERSE-CANDIDATE-WRITEBACK.md

Knowledge/decision candidate routing with:

- exact workspace source/evidence;
- bounded content;
- digest/provenance;
- no local canonical promotion.

---

## 18. Server/control-plane evidence

### src/server.ts

Critical security and product boundary evidence.

Current facts:

- HTTP server has no authentication middleware;
- request actor identity is read from JSON;
- mutating endpoints are exposed by path;
- readJson buffers request body without a top-level transport limit;
- native adapters are enabled by aiVerseOsRoot;
- secure remote Gateway is not implemented here.

### src/gateway.ts

Critical operator identity fact:

- assertOperatorDecision currently checks actorId starts with operator_.

This is an internal convention, not caller authentication.

### test/server.test.ts

Confirms the current local/trusted HTTP usage pattern by mutating Gateway state without authentication.

### docs/BUILD-MAP.md

Phase 5 explicitly lists “secure remote Gateway option” as remaining work.

---

## 19. Runtime interoperability

### src/a2a-runtime.ts
### docs/A2A-RUNTIME-ADAPTER.md

A2A execution and protocol mapping.

### src/hermes-runtime.ts
### docs/HERMES-RUNTIME-ADAPTER.md

Hermes one-shot runtime integration.

### src/openclaw-runtime.ts
### docs/OPENCLAW-RUNTIME-ADAPTER.md

OpenClaw adapter and isolation boundary.

### src/codex-runtime.ts
### src/claude-code-runtime.ts
### src/local-cli-process.ts
### docs/CODEX-CLAUDE-CODE-PROCESS-ADAPTERS.md

Local bounded process execution.

### src/external-managed-runtime.ts
### docs/EXTERNAL-MANAGED-BOT-RUNTIME.md

Persistent external provider/profile binding while local Bot identity remains canonical.

### Runtime adapter tests

Used to confirm:

- identity preservation;
- no authority widening;
- cancellation;
- bounded output;
- provider error normalization.

---

## 20. Remote trust, leases and recovery

### src/remote-machine-auth.ts
### docs/REMOTE-MACHINE-IDENTITY-AUTH.md

Phase 4.6 evidence:

- pinned HTTPS machine identity;
- no TOFU;
- host-injected auth;
- opaque credential refs;
- redirect and origin protection;
- security scheme verification.

### src/remote-leases.ts
### docs/REMOTE-CAPABILITY-ENVIRONMENT-LEASES.md

Phase 4.7 evidence:

- local lease canonical;
- remote grant equal/narrower only;
- environment mapping;
- expiry bounds;
- post-run authority receipt/audit.

### src/remote-recovery.ts
### docs/REMOTE-EXECUTION-RECOVERY.md

Phase 4.8 evidence:

- durable remote recovery journal;
- exact operation identity;
- submitting/remote_active/completed states;
- result cache until local settlement;
- safe A2A resume/replay contract;
- exact_task_key managed replay;
- lease revalidation/renewal;
- durable failed-revocation reconciliation.

### test/remote-leases.test.ts
### test/a2a-recovery.test.ts
### test/remote-recovery.test.ts
### test/external-managed-runtime.test.ts

Highest-value current enforcement tests for remote authority/recovery.

---

## 21. CI evidence

### .github/workflows/ci.yml

Current CI shape:

- Ubuntu;
- Node 22;
- npm install --no-audit --no-fund;
- npm test.

No multi-OS matrix is present.

### Phase 4.8 PR-head gate

PR #51 head:

- 3362541a46863dc801616a41810b888f8ceeb6f6

CI:

- workflow: CI
- run number: 480
- run id: 34721232595
- job id: 103627361983
- tests: 412
- pass: 412
- fail: 0
- cancelled: 0
- skipped: 0

### Current main merge commit

- 9874d413f5e23c9a869bf3ccead0f2751026a732

At audit time:

- fetch_commit_workflow_runs returned no run for this merge SHA;
- combined status returned no statuses.

Therefore the audit records PR-head CI as green without incorrectly calling it merge-commit CI.

---

## 22. PR history used as evidence

### Mainline merged sequence

Important merged PRs include:

- #3 Phase 2 TeamRun + temporary Worker lifecycle
- #5 Worker execution + manager topology
- #7 bounded parallel fan-out
- #11 direct handoff topology
- #14 bounded group discussion
- #18 structured disagreement
- #20 verifier/critic
- #23 canonical TeamRun synthesis
- #26 Worker cleanup hardening
- #27 adaptive collaboration
- #28 budget/cancellation consolidation
- #29 OS registration contract
- #30 workspace state projection
- #31 Brain ingress
- #33 Memory context/recall
- #35 platform-wide smoke
- #37 revert out-of-scope platform smoke
- #38 Skills resolution
- #39 Automations wake/schedule
- #40 OS write-command boundary
- #41 candidate writeback
- #42 Four Cs health
- #43 safe upgrade/uninstall
- #44 A2A
- #45 Hermes
- #46 OpenClaw
- #47 Codex/Claude process adapters
- #48 external-managed runtime
- #49 remote machine auth
- #50 remote capability/environment leases
- #51 remote retry/disconnect/reconnect

### Historical closed/unmerged hardening sequence

Important historical PRs:

- #1 persistent coordination store substrate
- #2 canonical coordination event bus
- #4 durable Bot registry hardening
- #6 durable Bot-to-Bot mailbox
- #8 delegated Task authority hardening
- #9 Handoff hardening
- #10 Rooms/Threads hardening
- #12 safety substrate
- #13 Team Run/Worker lifecycle alternate branch
- #15 manager topology
- #16 fan-out
- #17 direct Team Run handoff
- #19 group discussion
- #21 disagreement
- #22 verifier
- #24 synthesis

These are HISTORICAL evidence only.

They are particularly important because PR #6 contained stronger complete mailbox idempotency than current main.

---

## 23. Inspiration/reference evidence

### docs/REFERENCE-ADOPTION-MAP.md

Highest-value curated inspiration map.

Classifies external systems as:

- ADOPT;
- ADAPT;
- ADAPTER;
- STUDY;
- AVOID.

### docs/RESEARCH-2026-09.md

Research synthesis behind the persistent teammate architecture.

### docs/GROK-BOT-DEEP-DIVE.md

Product/interaction lessons from persistent teammate systems.

### docs/TELEGRAM-MANAGED-TEAM-CONTRACT.md

Future channel guidance, not current Telegram implementation.

Primary inspirations recorded:

- xAI Grok Bot;
- xAI Grok Multi-Agent;
- Hermes Bot Mode;
- Microsoft Agent Framework;
- A2A 1.0;
- OpenAI Agents SDK;
- OpenClaw;
- AgentScope;
- Pydantic AI;
- Google ADK;
- LangGraph;
- CrewAI;
- Agno;
- CAMEL;
- MetaGPT;
- related projects such as ClawSwarm/ClawTeam.

---

## 24. Contradiction evidence map

| Contradiction | Higher-authority evidence | Lower-authority/stale evidence |
|---|---|---|
| Project phase | BUILD-MAP + current merged code | README progress |
| Phase 4 started | BUILD-MAP + PHASE-4-STATUS + PRs #44-51 | tail of PHASE-3-STATUS |
| SQLite canonicality | src/store.ts + recovery/queue behavior | old architecture “derived/disposable” prose |
| Brain registration | current System Brain spec + current Brain lifecycle law | Multiple Bots Phase 3.3 parser/fixture |
| Current sibling compatibility | present contracts + absence of Phase 4.9 | old slice-level “COMPLETE” labels |

---

## 25. Negative-space evidence

The audit explicitly looked for and did not find:

- Multiple Bots Data integration;
- authenticated HTTP Gateway principal/session middleware;
- multi-OS CI matrix;
- current immutable release/tag;
- full public install/onboarding flow;
- current Phase 4.9 implementation;
- direct-message same-key whole-mutation replay test.

Negative claims in the component spec are limited to items supported by source-tree inspection, code search, workflow inspection or current status evidence.

---

## 26. Evidence limitations

1. The repository moved during the audit. Phase 4.8 PR #51 merged while review was underway. Final CURRENT conclusions were rebased to main head 9874d413f5e23c9a869bf3ccead0f2751026a732.
2. Current main itself had no commit-associated CI run returned at final check. The green 412/412 evidence is from the Phase 4.8 PR head.
3. GitHub code search did not index every possible private/system document query consistently, so file/tree inspection and direct fetches were used when stronger.
4. No sibling implementation repository was audited. Cross-component mismatch claims rely on the already-canonical AI-Verse-System component specifications after the Multiple Bots baseline was established.
5. Phase 4.9 is named in current status material but its detailed implementation checklist has not yet been authored in the Multiple Bots repository. The component spec derives a required evaluation scope from current gaps and existing architectural laws rather than pretending an absent implementation plan already exists.
6. External inspiration claims are recorded from the repository’s own research/adoption documents. This audit did not independently re-research each third-party project.
7. No runtime penetration test was performed. Security findings come from executable server/policy code and tests.
