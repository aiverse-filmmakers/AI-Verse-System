# Invisible Intelligence / Grandma / Jarvis UX Implementation Plan

**Status:** Persistent execution source of truth  
**Project:** AI-Verse Invisible Intelligence / Grandma / Jarvis UX  
**Canonical planning repo:** `aiverse-filmmakers/AI-Verse-System`  
**Started:** 2026-09-14  
**Rule:** Update this file before and after every implementation slice. A slice is COMPLETE only when owner implementation, focused tests, and exact evidence are recorded.

## 0. Operating rules

1. Work one bounded slice at a time.
2. Re-check current GitHub state before every slice because multiple agents may change repositories concurrently.
3. Distribution Agent public-beta PR #2 has priority while open. Do not modify, reset, rebase, merge into, or force new component refs into its frozen candidate.
4. The Safe Update / Release Train project remains the canonical owner of release descriptors, update transactions, compatibility contracts, release-train automation and state-preservation release machinery. Consume it, do not duplicate it.
5. Preserve canonical ownership. OS owns workspace state; Brain owns goals/strategy/classification; Memory owns historical memory; Skills owns Skill package/generation lifecycle; Data owns schemas/records; Multiple Bots owns Workers/Bots; Automations owns schedules/triggers; Distribution owns product installation/release sets.
6. Deterministic owner/security boundaries override model suggestions.
7. Do not weaken authority, privacy, migration, protected-Skill, recurring-job or permanent-Bot approval rules.
8. A normal user should not have to choose between Memory, Data, Skill, Workspace, Bot or Automation.
9. Documentation is never completion evidence by itself.
10. Final completion requires composed product acceptance through the real assembled Agent product.

## 0A. Anti-bloat rule

Prefer wiring together existing capabilities over adding new abstractions.

Every new mechanism must satisfy at least one of these:

- remove user-facing complexity;
- enable required behavior that cannot already be expressed through existing capabilities;
- close a proven safety, correctness or reliability gap.

Do NOT add new modes, services, stores, orchestration layers, state machines, registries, configuration or indirection merely for architectural elegance, conceptual neatness or hypothetical future flexibility.

Before introducing a new mechanism, explicitly verify that the required behavior cannot be achieved by composing or extending existing canonical owners and interfaces.

When both approaches satisfy the requirement, choose the smaller one.

**Existing capability + wiring is preferred over new architecture.**

## 1. Verified baseline at project start

### Active collision state

- `aiverse-filmmakers/ai-verse-distribution` PR #2, **Release immutable Agent public beta**, is OPEN.
- inspected PR #2 head: `d37f159e0ab27aef25047e497735b13e84fe7456`
- Distribution CI on that head: success
- Core clean-machine acceptance on that head: success
- Agent clean-machine release gate on that head: failure
- therefore PR #2 remains protected and unaccepted.
- AI-Verse-System currently has no open PR for this project.
- owner repositories inspected at project start had no open PRs.
- Safe Update / Release Train has active `release-train/*` branches and its canonical plan currently records Slice 4.0 in progress. This project must not take over or rewrite that work.

### Current owner heads inspected

- System: `4343d5a48cd8f065eeabaf5584b26505f9ceb706`
- OS: `eb059fdf753eba16eedd7c1c4f378ab4f152aa2e`
- Brain: `dfc6fa56e680b384723d7042c1d54f807e853c66`
- Memory: `ae1d8a0b14a9a8309450789f3d2f04b2a6426a42`
- Skills: `8fb8c8d3256a4e5a52609f83080e0cb384800e6d`
- Data: `a553aa261cd0ed20114c801fb01fc86bdd21050f`
- Gateway: `240c2b1b71abc7a8dbdc4d573da7fd85a110ca8f`
- Automations: `494469a496d479cfec618bcd9511033c0cd3e815`
- Multiple Bots: `9bffdffd07fb8abcea848213642936a23ecf4ecf`
- Token: `23b7b8ecbc9d9ef267f5e10449f785eb11107dd4`

These are observations, not frozen refs for this project. Re-check before every slice.

### Current collision update before Phase 8

- Distribution PR #2 is now MERGED. Final candidate head `775a5a49c6a861dd8ff8aad525b69c33ee02dd06` passed Distribution CI `34853174986`, Clean Machine Agent Release Gate `34853174857`, and Clean Machine Core Acceptance `34853174887`.
- The original frozen Agent release remains immutable. Invisible Intelligence will use a later candidate only after project acceptance.
- Safe Update / Release Train still has active `release-train/*` work. This project continues to consume, not duplicate, its release/update/state-preservation machinery.

## 2. Status vocabulary

- `NOT STARTED`
- `IN PROGRESS`
- `BLOCKED`
- `COMPLETE`

Every slice records:

- affected repo(s)
- dependencies
- anti-bloat decision
- acceptance criteria
- exact tests required
- exact PR/commit/workflow evidence
- explicit NEXT slice

---

# Phase 0 - Persistent plan and collision boundaries

## Slice 0.1 - Create persistent implementation plan

**Status:** COMPLETE  
**Repos:** AI-Verse-System  
**Dependencies:** none

### Acceptance criteria

- this plan exists in the canonical System repo;
- all requested behaviors are represented as bounded slices;
- collision rules for Distribution PR #2 and Safe Update are explicit;
- anti-bloat rule is project-wide;
- exact first implementation slice is identified;
- future agents can resume from GitHub alone.

### Tests/evidence

- plan commit: `cd9b447ad57b9025a6e9ea12db793d8bd39282d3`
- System PR: #12
- merged SHA: `32df3aeb9d127c95a183ad697edf59d790b2689c`
- live collision state captured above

### NEXT

**Slice 1.1 - OS progressive onboarding using the existing resumable intake, with no new onboarding store.**

---

# Phase 1 - Progressive onboarding and question minimization

## Slice 1.1 - OS progressive onboarding

**Status:** COMPLETE  
**Repos:** AI-Verse-OS, then AI-Verse-System evidence sync  
**Dependencies:** 0.1

### Anti-bloat decision

Reuse the existing `onboard` capability, `ai-verse-os-intake.md`, existing direction-owner checks, existing workspace capability and existing runtime adapters. Do not create an onboarding service, database or second profile store.

### Required behavior

- fresh user can begin useful work before completing the deep seven-question intake;
- default conversational entry is equivalent to "What would you like help with?";
- missing profile/intake facts are requested only when they block safe/correct work;
- known answers are reused rather than re-asked;
- existing seven-question flow remains available as deep/full intake;
- resumability survives restart using existing state;
- strategic direction still respects OS/Brain ownership.

### Exact acceptance

- fresh-state test reaches useful-action-ready state without seven answers;
- deep intake remains selectable;
- restart preserves partial progress;
- repeated invocation does not repeat already-known questions;
- Brain-owned direction does not create parallel OS goals;
- no architecture jargon required in normal flow.

### Evidence

- OS PR: #28
- PR head: `a7548405a73247c10e4cb35dde7869f5eac3e39c`
- merged OS SHA: `a21a44e7b78805b89a48f5c01f40ec0dc09fbd01`
- focused test: `scripts/test-progressive-onboarding.mjs`
- Repository QC run `34831174973`: success; focused progressive-onboarding step passed; adapter integration and real Skills-provider integration passed
- CLI smoke run `34831175417`: success on Ubuntu, macOS and Windows
- Five-Component Public Beta run `34831175138`: success for all three install-order scenarios
- Four Repo Acceptance run `34831175093`: success
- Data Host Boundary run `34831175025`: success
- Direction Ownership run `34831174969`: success
- OS Brain Permission Contract run `34831175124`: success
- OS Write Command Boundary run `34831174931`: success

### Accepted implementation

- normal first use starts from a real request instead of forcing the seven-question intake;
- when no task exists yet, the conversational prompt is "What would you like help with?";
- missing intake facts are asked only when they block safety, scope, permission, external access, consequential action, strategic ownership or correct routing;
- existing answers and canonical state are reused across restart;
- the existing intake remains the resumable deep-intake record, with no new onboarding store;
- the seven-question flow remains available as an explicit full/deep intake;
- Brain-owned strategic direction remains protected;
- runtime/CLI/README surfaces no longer present full intake as a prerequisite for first value.

## Slice 1.2 - Natural-language question gate

**Status:** COMPLETE  
**Repos:** AI-Verse-OS and Gateway only if current runtime surface requires it  
**Dependencies:** 1.1

Implement the smallest reusable check that keeps internal technical choices invisible and asks only when authority/safety/scope/external effect genuinely requires user input. Prefer updating existing runtime instructions/contracts over adding a new policy service.

### Evidence

- Gateway PR: #2
- PR head: `40d00e432e2515c8f1ebf38bbcddc9fa11df8790`
- merged Gateway SHA: `fc654df78e69e497864995f99a3f7a895f149752`
- CI run `34831479592`: success across Ubuntu, macOS and Windows on Node 20 and 22
- end-to-end runtime probe: `fixtures/question-policy-runtime.mjs` + `test/loop-contracts.test.mjs`
- implementation reuses Gateway's existing system-context assembly; no new policy service/store/mode was added
- deterministic OS host authorization remains stronger than runtime instructions

### Accepted implementation

Gateway now tells the runtime to act instead of asking for safe/reversible/internal choices within existing authority, reuse known context, avoid subsystem-choice questions, recognize direct user instructions as intent for the requested work, and ask only for real safety/authority/scope/external-effect blockers.

---

# Phase 2 - Automatic workspace emergence

## Slice 2.1 - OS owner-side automatic workspace create/evolve primitive

**Status:** COMPLETE  
**Repos:** AI-Verse-OS  
**Dependencies:** 1.1

### Required behavior

Using existing workspace schema/template/direction-owner rules:

- idempotently locate matching existing workspace;
- create only for substantial scopes;
- evolve matching workspace rather than duplicate it;
- infer clear boundaries from supplied evidence;
- preserve workspace isolation;
- never widen permissions;
- persist provenance explaining create/evolve reason;
- survive restart.

No second workspace registry unless current implementation proves one is strictly required.

### Evidence

- OS PR: #29
- final PR head: `f7e2b96c718f9392fd4e4d975d2cf9de9cd3bfe6`
- merged OS SHA: `933a6beadf87b646fb8c8e0358aaeea6b0504424`
- canonical owner primitive: `scripts/workspace-owner.mjs ensure --root <os-root>`
- focused acceptance: `scripts/test-workspace-owner.mjs`
- Repository QC run `34832020361`: success, including automatic workspace owner test, adapter integration and Skills-provider integration
- Five-Component Public Beta run `34832020302`: success in all three install orders
- Four Repo Acceptance run `34832020438`: success
- OS Write Command Boundary run `34832020472`: success
- Direction Ownership run `34832020379`: success
- OS Brain Permission Contract run `34832020299`: success

### Accepted implementation

The OS now has a deterministic owner-side `ensure` operation that creates a minimum workspace only for a substantial, clear, privacy-safe scope; reuses/evolves an existing matching workspace; rejects ambiguous/privacy/permission/credential/Connection expansion; avoids duplicates; preserves unrelated workspace state; persists restart-safe provenance; uses conservative approval defaults; and performs only safe additive domain/source evolution without rewriting unsupported user-authored YAML.

## Slice 2.2 - Runtime classification and routing to OS

**Status:** COMPLETE  
**Repos:** Brain + Gateway + OS  
**Dependencies:** 2.1

Wire meaningful-work evidence to the canonical OS workspace path. The classifier may suggest scope identity; OS validates and owns mutation.

### Evidence

- OS PR: #30
- OS PR head: `02718658b12bd9aa5bdb107d487c862e0a82679b`
- merged OS SHA: `c9daa62f2f9b49a32dd9897962f61c257678fe28`
- OS Repository QC run `34832528643`: success
- OS Four Repo Acceptance run `34832528691`: success
- OS Five-Component Public Beta run `34832528635`: success
- OS Write Command Boundary run `34832528659`: success
- OS Brain Permission Contract run `34832528628`: success
- OS Direction Ownership run `34832529275`: success
- Gateway PR: #3
- Gateway PR head: `3dd79a3ffb7dac9a2929b1e4a24b058ab4c472e3`
- merged Gateway SHA: `034d4edc83c971b491d28f93ca571f97e66ff5d6`
- Gateway CI run `34833839372`: success across Ubuntu, macOS and Windows on Node 20 and 22
- end-to-end acceptance proves owner-routed `workspace.ensure`, request fingerprinting, no mid-run scope mutation, durable session rebinding, next-turn workspace use, and rejection of silent session-scope override

### Accepted implementation

The runtime may classify a clear substantial scope and request organization through the existing generic action tool. OS rechecks and owns the workspace mutation through `workspace.ensure`. When OS confirms a created/evolved/existing workspace, Gateway updates only the durable session binding for later turns; the active run and any active Brain Goal keep their original scope. No second workspace owner, classifier service, policy service, database, or registry was introduced.

---

# Phase 3 - Invisible Memory / profile routing

## Slice 3.1 - Prove or close automatic safe Memory routing

**Status:** COMPLETE  
**Repos:** Brain, Memory, Gateway as required by current implementation  
**Dependencies:** 1.2

Inspect current behavior first. Reuse current Memory evidence/provenance/supersession path. Implement only missing routing for stable facts/preferences/lessons that already meet Memory rules. Do not persist every utterance.

### Evidence

- Memory PR #11 merged at `1c6acf036d42937e57d94dfe48ac501727861653`
- final Memory PR head: `d6cb7e50a1677ade023b2f046988f5aae9cb7aac`
- Memory Test run `34834329680`: success across Ubuntu/macOS/Windows, Python 3.9 and 3.12, installer smoke, OS-update integration, and public-beta acceptance on all three OSes
- Memory owner gate: `capture_candidate`, reusing canonical `write_atomic`, provenance/evidence refs, serialized mutation and durable `effect_id` idempotency
- OS PR #31 merged at `ce7db254af18ee2f7e1c5bc5448d2d7540dab209`
- final OS PR head: `0898d779a36ee741fc2829c879874af0f4a224c8`
- OS Repository QC `34850675624`: success
- OS Five-Component Public Beta `34850675678`: success
- OS Four Repo Acceptance `34850675611`: success using accepted Memory SHA
- OS Direction Ownership `34850675689`: success
- OS Brain Permission Contract `34850675694`: success
- OS Write Command Boundary `34850675728`: success
- Gateway PR #4 merged at `7cc1617aeac6caefce627842f5bbe1620c960d5f`
- final Gateway PR head: `b8f29641b8a7b4026d1dbcc369f9a3fb14c23171`
- Gateway CI `34850849483`: success on Ubuntu, macOS and Windows, Node 20 and 22
- Gateway injects trusted run provenance, evidence refs, retry identity and request fingerprint; runtime cannot supply those trusted fields
- OS binds Memory candidate to the active operator/workspace scope; cross-workspace capture is rejected
- automatic capture is limited to high-confidence durable historical evidence and fails closed on current truth, strategy, secrets, privacy ambiguity, permission expansion and unsupported types

### Accepted implementation

A normal run may propose a bounded historical Memory candidate through the existing action loop. Gateway supplies trusted provenance/idempotency, OS enforces current-scope routing, and Memory performs final deterministic admission through its existing canonical writer. Trivial turns and weak/current/unsafe candidates are not automatically persisted. No new Memory store, writer, post-task service, classifier service or routing database was introduced.

---

# Phase 4 - Automatic safe learned Skills

## Slice 4.1 - Skills safe new-Skill auto-eligibility

**Status:** COMPLETE  
**Repos:** AI-Verse-Skills  
**Dependencies:** current self-learning contracts

Extend existing proposal/evaluation/generation/promotion machinery so a genuinely new low-risk `agent_learned` or permitted `workspace_local` Skill may become active automatically only when every mandatory gate passes.

No new Skill store or workshop subsystem.

### Required negative gates

No auto-promotion if candidate:

- expands permission/capability;
- needs a credential/Connection;
- persists secrets;
- adds unsafe dependency/executable authority;
- overwrites protected/user/upstream content;
- fails admission/eval;
- is duplicate/dangerous;
- cannot be rolled back.

### Evidence

- Skills PR #11 merged at `8b82e41bd8f0adecdfd93d64ae1fb30552802b99`
- final PR head: `fef39614e5901ae23d77c84ec754932999f90cb9`
- Validate AI-Verse Skills `34851686901`: success
- Runtime Readiness `34851687162`: success on Ubuntu/macOS/Windows, Python 3.9 and 3.12
- Full E2E Install `34851687125`: success through install/update/rollback/uninstall/recovery
- new `agent_learned` creation in opt-in `auto` mode is gated by low risk, confidence >= 0.90, security/admission, dedup, provenance, scope, permission/dependency, Connection/credential and exact-generation checks
- `workspace_local` auto-create remains separately opt-in
- protected/user/upstream/external ownership cannot auto-promote
- every promotion creates a verified immutable generation and preserves rollback

## Slice 4.2 - Brain/Gateway substantial-task learning trigger

**Status:** COMPLETE  
**Repos:** Brain, Gateway, Memory, Skills  
**Dependencies:** 4.1

Wire current learning-candidate and evidence contracts into post-run/substantial-task review without reviewing every trivial turn.

### Evidence

- Brain PR #21 merged at `a53f79cf083d99b39a87d9ffe9509bf4e2d02922`
- Brain PR head `20c1a345f3ff2e577806b8a8f2375f9393f5e305`
- Brain CI `34852941983`: success
- Brain Skills Receipt Contract `34852941859`: success
- Brain OS Direction Ownership Contract `34852941819`: success
- Skills PR #12 merged at `fb0c138ef424734cd2e5359040f376e35c4c5875`
- Skills PR head `c8abfa68d84f65c04fb38181c2a786275fd33827`
- Skills Validate `34853205965`, Runtime Readiness `34853206011`, Full E2E Install `34853205943`: all success
- Gateway PR #5 merged at `ae5b322db4e7ac593bd03d5f5c9630c6e65edf76`
- Gateway PR head `7637d5e969b8e63ee66e7fcd6cfb9249e640526d`
- Gateway CI `34855127641`: success on Ubuntu/macOS/Windows, Node 20 and 22
- OS PR #35 merged at `3ebb0530a876c404031274d4fa4d3ec1909ec21a`
- OS PR head `a3ae276d9e755af7ca6538e6c39930fb2cc62bdc`
- OS Repository QC `34855123759`: success
- OS Write Command Boundary `34855123724`: success
- OS Brain Permission Contract `34855123720`: success
- OS Direction Ownership `34855123727`: success
- OS Four Repo Acceptance `34855123787`: success with accepted Brain/Memory/Skills owner refs
- OS Five-Component Public Beta `34855123756`: success across all three install orders
- Gateway suppresses non-substantial learning before any owner action or action-budget use
- Gateway injects trusted run identity, scope, evidence refs and timestamp; runtime cannot forge them
- Brain deterministically admits/ignores reusable-procedure candidates; it does not become a Skill store
- OS only transports admitted candidates to the configured Skills owner entrypoint
- Skills proposal submission is retry/idempotency bound; reused candidate ID with changed metadata/package bytes fails closed
- no new review daemon, scheduler, store, post-task service or second model pass was introduced

## Slice 4.3 - Later task actually uses learned Skill

**Status:** COMPLETE  
**Repos:** Gateway + Skills + composed owners  
**Dependencies:** 4.2

Prove restart persistence, active immutable generation, actual subsequent selection/use, rollback and quarantine paths.

### Evidence so far

- OS PR #37 merged at `caa38f46d29e66363493d0e11da83aa924af1dea`
- final OS PR head: `799af68369440f114108cdbf60668c917e040d13`
- OS Four Repo Acceptance `34855795748`: success
- OS Five-Component Public Beta `34855795755`: success across all three install orders
- OS Repository QC `34855795777`: success
- OS Direction Ownership `34855795762`: success
- OS Brain Permission Contract `34855796007`: success
- OS Write Command Boundary `34855795908`: success
- real Skills owner was switched to opt-in `auto`, a safe candidate auto-promoted into a new immutable generation, and a fresh OS host object rediscovered it from persisted owner state
- a later generation/digest-bound `capability.read_instructions` execution successfully loaded the learned procedure
- an unsafe secret-bearing candidate was quarantined and never appeared in capability discovery
- compare-and-set learning rollback restored the exact previous immutable generation and removed the learned capability from later discovery

### Gateway later-use evidence

- Gateway Context Ladder PR #6 merged first, preserving concurrent ownership and avoiding branch interference
- Gateway PR #7 merged at `4e5e6d55f659604922b794cfc517e0898b47fbe1`
- final Gateway PR head: `f3291587483f3202a61dd8147c0b5ea552a1f954`
- Gateway CI `34856430622`: success on Ubuntu, macOS and Windows with Node 20 and 22
- first substantial run created the learned capability through the existing Skills route
- Gateway process was restarted from the same durable home
- a later short normal request received the learned capability through canonical owner context, selected its exact generation/digest, and invoked `capability.read_instructions`
- successful later use did not depend on in-process cache, a repeated learning prompt, or hidden duplicate Skill state

---

# Phase 5 - Automatic Data emergence

## Slice 5.1 - Data safe additive structure creation/evolution

**Status:** COMPLETE  
**Repos:** AI-Verse-Data  
**Dependencies:** current Data catalog/schema migration engine

Use existing Data Space, catalog, additive schema, idempotency, transaction, provenance and migration machinery.

Safe automatic operations are limited to additive/reversible owner-supported changes. Destructive/ambiguous migration remains approval-required.

### Acceptance evidence

- Data PR #15 merged at `579dae596a1c929bbc0e900541d29742c18b875e`
- accepted PR head: `64ce5611a0f34f904742af96f39bdaa69824108b`
- Data CI `34859531419`: success across Node 22/24 on Ubuntu, macOS and Windows
- Data Release Smoke `34859532062`: success
- Data Five-Component Release Acceptance `34859532054`: success across all three install orders
- owner path can create a missing Data Space/schema, return existing state idempotently, or apply only safe additive fields
- exact idempotency replay is durable across restart and semantic drift under the same key fails closed
- existing field-definition changes, `allowUnknownFields` changes and required-field additions without defaults route to migration-required rather than silent mutation
- provenance/receipt attribution is preserved and workspace scope remains isolated
- trusted host-bound automatic requests preserve the real Bot/Worker/system actor instead of falsely attributing automatic writes to the local human operator

A packaging mismatch found by composed OS acceptance was corrected without changing Data semantics:

- Data PR #16 merged at `8edde7dca5afa34e300130cc6b8ee2b4170ad40f`
- accepted PR head: `f304be47dfd31387cf3f1d769e5b00510a2dd837`
- Data CI `34861500075`: success across Node 22/24 on Ubuntu, macOS and Windows
- Data Release Smoke `34861500051`: success
- Data Five-Component Release Acceptance `34861500107`: success across all three install orders
- materialized/installed Data engine now truthfully advertises the already-accepted trusted host-bound actor contract

## Slice 5.2 - Runtime structured-truth classification and owner routing

**Status:** COMPLETE  
**Repos:** Brain + Gateway + OS + Data  
**Dependencies:** 5.1

Meaningful repeated structured information should be routed into an existing or safely created Data structure without asking the user to choose Data/schema.

### Acceptance evidence

- Brain PR #22 merged at `16c0b7ea32fcb4759cfb8368876b6985016eab68`
- Brain PR head `de2023920c6c01034f4844326deb34d21f4dbd82`
- Brain CI `34859912066`, Direction Ownership `34859912053`, Skills Receipt Contract `34859911976`: all success
- Brain deterministically admits only substantial, workspace-bound, repeated, high-confidence structured current truth
- secret-bearing, privacy-ambiguous, permission-expanding, destructive, weak-evidence and low-confidence candidates do not auto-route
- runtime cannot smuggle trusted scope, provenance, approval or authority fields through the Brain gate
- Gateway PR #8 merged at `587a7c53aa2afda68027b1158f52e1e17d1b5dbb`
- Gateway PR head `1f4594bb13a38f0f56bd5d71d9d63b288c07aed4`
- Gateway CI `34861198912`: success
- OS PR #38 merged at `92bb939885d2f2bf84c1bbb48a2c92c523d5a4bd`
- final OS PR head `8a65658a5cd09bea57142e40a098a478e4269279`
- OS Direction Ownership `34864858935`, Write Command Boundary `34864859015`, Data Host Boundary `34864858878`, Brain Permission Contract `34864858860`, Repository QC `34864858968`, Four Repo Acceptance `34864858864`, Five-Component Public Beta `34864859011`: all success
- OS composes Brain admission with Data-owned structure/query/create/update operations and does not become a Data store
- natural-key duplicate checking reuses or updates one canonical record instead of creating duplicates
- multiple matches, migration-required changes, owner refusal and concurrency conflicts fail closed without silently widening authority
- later context receives only bounded Data orientation; records are queried from Data when needed rather than dumped into every prompt
- no optimizer service, second canonical store, review daemon or new scheduler was introduced

---

# Phase 6 - Temporary Workers and permanent Bot boundary

## Slice 6.1 - Automatic temporary Workers

**Status:** COMPLETE  
**Repos:** AI-Verse-Multiple-Bots, OS, Gateway  
**Dependencies:** existing Worker/lease/budget lifecycle

Use existing temporary Worker machinery automatically for requested work when justified by task complexity, within existing authority/budget/scope. No durable promotion.

### Anti-bloat decision

No Worker service, optimizer, scheduler, second runtime, second Bot registry or temporary-agent store was added. The implementation wires the existing Gateway action loop -> OS host boundary -> Multiple Bots Team Run/Worker/Task/lease/runtime/cleanup machinery.

### Acceptance evidence

- Multiple Bots PR #67 merged at `ba97408fa14ba7a5823c4376b10e190c887958b4`
- final Multiple Bots PR head: `172101fd732ebe018a95f0ff920189642d5b6a60`
- Multiple Bots CI `34867051626`: success
- OS PR #39 merged at `b598e733df89c496cf5740388a1283dda026eb89`
- final OS PR head: `f1bcaa5b82cd6a8fdabe34e947c4420c139237f5`
- OS Direction Ownership `34867446921`, Write Command Boundary `34867446415`, Brain Permission Contract `34867446703`, Repository QC `34867446820`, Four Repo Acceptance `34867446622`, Five-Component Public Beta `34867446873`, Invisible Intelligence Temporary Worker `34867446819`: all success
- Gateway PR #9 merged at `4c52286be8f480473ced9af56098e00b0a5452a3`
- final Gateway PR head: `3679b8e41f03be6552fc4bb2bbe72b0ad1ca79d3`
- Gateway CI `34870647229`: success across Ubuntu/macOS/Windows on Node 20/22 after one unchanged failed-job retry
- Gateway -> OS -> Multiple Bots composition `34870647371`: success
- Gateway admits at most one automatic temporary specialist per foreground run
- unsupported `json-subprocess` runtime is suppressed rather than bridged through a new runtime abstraction
- runtime cannot forge Worker runtime, budget, tools, Connections, trusted provenance or task evidence
- composed canonical state proves zero durable Bots, expired temporary Worker, revoked lease, run-scoped leader and preserved Worker-generated Artifact

## Slice 6.2 - Permanent Bot recommendation and consent

**Status:** COMPLETE  
**Repos:** AI-Verse-Multiple-Bots, OS, Gateway  
**Dependencies:** 6.1

Repeated specialist need may create a recommendation, not a durable Bot. Explicit user agreement or an explicit direct permanent-Bot request is required before canonical Bot creation.

### Anti-bloat decision

No second Bot registry, approval store, recommendation database or Bot-creation service was added. Durable creation reuses the existing Multiple Bots registry. Gateway derives consent from the actual conversation, OS validates the trusted consent/runtime/scope boundary, and Multiple Bots remains the canonical durable identity owner.

### Acceptance evidence

- Multiple Bots PR #68 merged at `c600e2bc014351a61e1c0e2673fc63f5d5fa54ec`
- final Multiple Bots PR head: `c3f2f2bc86a6cb4d089a8e125360786ed29d74dc`
- Multiple Bots CI `34871826025`: success
- installed owner extension exposes the existing canonical durable Bot registry without weakening the low-level registry
- exact same-manifest retry returns existing canonical state; changed payload under the same durable identity fails closed

- OS PR #40 merged at `c13d3ca858f887b3ceac690544819ccc55e9d5b0`
- final OS PR head: `074f5cb2723a5772837ba441d894e1b0ab98ac89`
- Direction Ownership `34872286898`: success
- Permanent Bot Consent `34872286971`: success against accepted Multiple Bots owner
- Brain Permission Contract `34872286921`: success
- Four Repo Acceptance `34872286988`: success
- Repository QC `34872286869`: success
- Write Command Boundary `34872286856`: success
- Temporary Worker regression `34872286928`: success
- Five-Component Public Beta `34872286901`: success
- OS accepts only trusted explicit consent modes `direct_request` or `affirmative_to_recommendation`
- consent evidence is preserved in canonical Bot lifecycle provenance
- initial Bot authority is conservative: zero tools, zero Connections, zero peers, no Worker creation, no handoff, bound scope only
- requested Skills must resolve through the canonical Skills owner before durable attachment

- Gateway PR #10 merged at `2b6222763ac3f290463e118ea8430082b3a10934`
- final Gateway PR head: `5ce9e60e348a0a794a2c208a85c714d76573f13c`
- Gateway CI `34873514835`: success across Ubuntu/macOS/Windows on Node 20/22 after one unchanged Windows failed-job retry
- Temporary Worker regression composition `34873514925`: success
- Gateway -> OS -> Multiple Bots Permanent Bot Composition `34873514977`: success using accepted OS `c13d3ca858f887b3ceac690544819ccc55e9d5b0` and Multiple Bots `c600e2bc014351a61e1c0e2673fc63f5d5fa54ec`
- direct "create me a permanent bot" requests count as consent without redundant confirmation
- short affirmative follow-up counts only when it immediately follows a clear assistant recommendation for a dedicated/permanent specialist
- repeated need alone, advice questions, negation and temporary-only requests do not cross the durable boundary
- model-supplied consent/runtime/permissions/scope/provenance are rejected
- composed canonical state proves exactly one durable Bot after consent and zero durable creation before consent

---

# Phase 7 - Automation recommendation and consent boundary

## Slice 7.1 - Repeated responsibility recommendation

**Status:** COMPLETE  
**Repos:** Gateway + canonical AI-Verse-Automations negative composition  
**Dependencies:** existing Automations scheduler

Observed recurring time/event pattern may generate a natural-language recommendation only. No canonical schedule/job exists before consent.

### Anti-bloat decision

Reuse the existing Automations Store, trigger parser, scheduler Engine, OS permission recheck and owner wake adapters. Do not create another scheduler, recommendation store, cron service or recurring-responsibility registry.

### Acceptance evidence

- Gateway PR #11 merged at `1df2426e53ea57b4e704248bf1c9aa5500a25293`
- final Gateway PR head: `078419c8b6ae087939caceac29872f75d64a740f`
- Gateway CI `34874227131`: success across Ubuntu/macOS/Windows on Node 20/22
- Automation Recommendation Boundary `34874227177`: success against canonical Automations `494469a496d479cfec618bcd9511033c0cd3e815`
- Temporary Worker regression composition `34874227186`: success
- Permanent Bot regression composition `34874227080`: success
- clear repeated responsibility can produce a natural-language recommendation with zero owner actions
- one-off work does not produce a recurring recommendation
- normal user copy contains no Automation/scheduler/cron/trigger/job jargon
- real Automations database remains at zero automations, zero triggers and zero runs after the recommendation flow
- no new scheduler, recommendation database, classifier service or recurring-responsibility registry was introduced

## Slice 7.2 - Consent/direct request -> canonical Automation

**Status:** COMPLETE  
**Repos:** AI-Verse-Automations + OS + Gateway  
**Dependencies:** 7.1

Explicit yes or direct scheduling instruction creates through the existing Automations owner path, unless another authority boundary blocks it. No redundant confirmation.

### Anti-bloat decision

The implementation reuses the existing Automations Store, scheduler Engine, OS extension registry/action-permission boundary and Gateway run engine. The only new owner primitive atomically composes the already-existing Automation + trigger writes so a crash cannot leave half a recurring definition. No second scheduler, mutable HTTP scheduler API, approval database, trigger registry, recurring-work service or execution runtime was introduced.

### Acceptance evidence

- Automations PR #2 merged at `53ab6a79a07f99f7e0e357a9c78337926823d96d`
- final Automations PR #2 head: `cfd4a2f15d575db401ce3c43bf5fe64f0fffeae3`
- Automations CI `34874771002`: success
- owner `create_definition` creates the Automation and trigger in one SQLite transaction
- exact replay under the same trusted idempotency key returns existing state; changed semantics under the same key fail closed
- trigger-insert failure rolls the Automation row back

- Automations PR #3 merged at `caaed83b98026dd955640fc015d181529b91a1c6`
- final Automations PR #3 head: `269661c074a101faef503669790dc127bfc3c29f`
- Automations CI `34875231065`: success
- Automations attaches through the existing OS `.aiverse/extensions/registry.json` contract
- unrelated extension entries/top-level fields and explicit disabled state are preserved
- the shared registry lock is never stolen and tracked OS files remain untouched
- the materialized owner bridge exposes only atomic `create_definition` against the configured canonical Automations state

- OS PR #41 merged at `b08cc8c05c56fad7bc390f391292bdfbdd7d23e0`
- final OS PR #41 head: `750d1fc95427a4d3491e241ae62cd4e7706265ec`
- OS Write Command Boundary `34875633144`: success
- Permanent Bot Consent `34875633131`: success
- Automation Consent `34875633237`: success against accepted Automations owner
- Direction Ownership `34875633127`: success
- Repository QC `34875633136`: success
- Five-Component Public Beta `34875633247`: success
- Four Repo Acceptance `34875633130`: success
- Temporary Worker regression `34875633104`: success
- OS Brain Permission Contract `34875633065`: success
- OS validates trusted explicit consent, accepts only recurring cron/interval creation, fixes the execution target to Gateway and fixes scheduled wake authority to `read_local`
- model/runtime cannot choose target owner, durable IDs, scope, permissions, trusted provenance or owner idempotency

- Gateway PR #12 merged at `5743aff0982dcae2ca6f2ec70ccfb2b89b0fc3b0`
- final Gateway PR #12 head: `9b1ff315cc64fc8723879c1a4561c029ed20782b`
- Gateway CI `34878503752`: success across Ubuntu/macOS/Windows on Node 20/22
- Automation Recommendation + Consent Boundary `34878503745`: success
  - `recommendation-does-not-schedule`: success
  - `gateway-os-automations-consent`: success
- Temporary Worker regression composition `34878503747`: success
- Permanent Bot regression composition `34878503751`: success
- direct recurring instructions count as consent only when cadence is complete and deterministically matches the proposed cron/interval
- short affirmative follow-up counts only after an immediately preceding recommendation containing the complete cadence
- repeated need without consent, cadence mismatch, missing timezone, forged trusted fields and recursive schedule creation are suppressed before any owner action
- Gateway now consumes the existing Automations wake envelope at `POST /v1/automations/invoke` using the existing run engine
- canonical schedule firing creates one normal Gateway run with Automation/trigger/invocation provenance
- exact wake replay after Gateway restart returns the same durable run; changed payload under the same invocation ID is rejected
- composed acceptance proves exactly one conservative canonical recurring definition, target `gateway`, wake authority `read_local`, and no second definition from observation alone

---

# Phase 8 - Central invisible organization loop

## Slice 8.1 - Meaningful-work post-run organization routing

**Status:** COMPLETE  
**Repos:** Gateway, consuming existing OS/Memory/Data/Skills owner APIs  
**Dependencies:** Phases 2-7 owner primitives

Implement the smallest owner-correct post-run routing path:

```text
meaningful work completes
-> bounded evidence
-> existing runtime classification
-> route to canonical owner
-> owner validates and mutates/proposes
-> verify
```

No Optimizer database, second Brain, scheduler or canonical store.

### Anti-bloat decision

The accepted implementation adds one bounded post-run review inside the existing Gateway run engine. It does not add an Optimizer, second Brain service, scheduler, review daemon, approval database, routing store or canonical state owner. The review may only propose the four previously accepted safe organization routes: `workspace.ensure`, `memory.capture`, `skills.learning-candidate` and `data.structured-truth`.

Workers, permanent Bots, Automations, credentials, Connections, permission/scope expansion, external effects, strategic authority transfer and destructive/irreversible mutation are not admitted by the review path.

### Acceptance evidence

- Gateway PR #13 merged at `8de15df92da04dd13b4ac98d422f7c6cc19cf38f`
- final Gateway PR head: `e75ed9ff0e7db40bff4a2c34c8f84b584441d6e5`
- Gateway CI `34884868299`: success across Ubuntu, macOS and Windows on Node 20 and 22
- Temporary Worker regression composition `34884868349`: success
- Permanent Bot regression composition `34884868344`: success
- Automation recommendation + consent regression `34884868300`: success for both no-schedule recommendation and real Gateway -> OS -> Automations consent composition
- the foreground run reaches its normal completed output before optional organization review state is processed; review failure cannot rewrite the foreground answer into failure or approval wait
- completed-work evidence is bounded and secret-like evidence is not admitted for review
- review proposals are durably persisted before owner execution and resume after restart without reclassification
- owner writes use deterministic per-run/per-owner idempotency keys; exact replay does not duplicate canonical effects
- review-required owner approval is skipped rather than manufacturing consent or parking the already-completed foreground run
- review messages and review tool results are not appended to the user/session conversation history
- a successful `workspace.ensure` may rebind the durable session for later turns and subsequent review routes use the owner-confirmed workspace
- any of the four safe organization operations already routed during the foreground run are deterministically suppressed from the post-run review to avoid duplicate owner mutation
- an attempted `bots.permanent` review proposal is rejected by the Gateway allowlist before the host sees it
- existing accepted owner gates remain final authority; this slice reuses rather than duplicates their admission, provenance, rollback/idempotency and canonical mutation contracts

## Slice 8.2 - Review budget / trivial-turn suppression

**Status:** IN PROGRESS  
**Repos:** Gateway/Brain  
**Dependencies:** 8.1

Prove low-value turns do not incur expensive organization review while strong evidence/substantial work does.

---

# Phase 9 - Natural-language receipts and invisible subsystem jargon

## Slice 9.1 - User-facing outcome language

**Status:** NOT STARTED  
**Repos:** Gateway plus owners only where response metadata originates  
**Dependencies:** owner behaviors implemented

Normal surfaces describe user outcomes, while technical receipts retain component detail for advanced inspection.

---

# Phase 10 - Grandma first-run / product bootstrap

## Slice 10.1 - Distribution product-level bootstrap

**Status:** BLOCKED  
**Repos:** ai-verse-distribution + owner lifecycle consumers  
**Dependencies:** Distribution PR #2 merged/resolved; consume Safe Update / release-train machinery where available

Fresh non-technical user path:

```text
install AI-Verse
-> exact released Agent components
-> safe owner setup
-> doctor/readiness
-> safe deterministic reconcile where appropriate
-> conversational first-run
-> progressive onboarding
```

Low-level install/setup/status/doctor/onboard commands remain for CI/support/advanced use.

Do not mutate the first frozen Agent release. Create a later exact candidate after this project is accepted.

## Slice 10.2 - Safe deterministic self-heal

**Status:** NOT STARTED  
**Repos:** Distribution/OS and owner components only where current deterministic reconcile exists  
**Dependencies:** 10.1

Auto-repair only deterministic reversible owner-controlled setup defects. Never auto-heal corruption destructively, unknown migration, credential/security failures, authority conflicts or ambiguous canonical stores.

---

# Phase 11 - Cross-repo acceptance

## Slice 11.1 - Scenario acceptance A-F

**Status:** NOT STARTED

Prove:

A. Grandma first run  
B. automatic client workspace  
C. automatic safe Skill learning/use  
D. dangerous Skill blocked/quarantined/approval-required  
E. automatic safe Data  
F. destructive Data change does not happen silently

## Slice 11.2 - Scenario acceptance G-M

**Status:** NOT STARTED

Prove:

G. Automation recommendation boundary  
H. direct Automation request  
I. permanent Bot boundary  
J. temporary Workers  
K. no subsystem-choice jargon  
L. restart truth/no duplicate canonical state  
M. no silent authority expansion

---

# Phase 12 - System synchronization and release

## Slice 12.1 - Living-spec CURRENT updates

**Status:** NOT STARTED  
**Repos:** AI-Verse-System  
**Dependencies:** corresponding owner slices complete

Only after implementation/evidence exists:

- update relevant component specs/QC/source maps;
- change GAP/INTENDED to CURRENT where warranted;
- update Public Beta Tracker;
- append System Changelog;
- keep Owner Product Intent canonical and unchanged unless product intent itself changes.

## Slice 12.2 - New immutable Agent candidate with Invisible Intelligence

**Status:** BLOCKED  
**Repos:** ai-verse-distribution  
**Dependencies:** PR #2 merged, Safe Update/release-train compatible state, all required owner slices accepted

Create a NEW exact Agent release candidate. Do not mutate the original frozen Agent release.

Run:

- Distribution CI;
- Core regression;
- Agent clean-machine Ubuntu;
- Agent clean-machine macOS;
- Agent clean-machine Windows;
- Grandma/Invisible Intelligence composed scenarios.

## Slice 12.3 - Final project gate

**Status:** NOT STARTED

Complete only when every required slice is COMPLETE, composed acceptance is green, state/authority invariants hold, and the exact release set is frozen with evidence.

---

# Overall progress

- Formal tracked completion: **16 / 24 = 66.7%**
- Current active slice: **8.2 - Review budget / trivial-turn suppression**
- Completed through: **8.1 - Meaningful-work post-run organization routing**
- Distribution PR #2 is merged; the original frozen Agent release remains immutable.
- Product bootstrap and the new immutable Invisible Intelligence Agent candidate remain gated by the separately owned Safe Update / release-train-compatible state and later project acceptance.
- The document contains the separate planning slice `0.1`; the formal 24-slice denominator is preserved to match the established project progress convention.

**Exact NEXT:** finish 8.2 by proving cheap deterministic trivial-turn suppression and bounded review spend for substantial work.  
**Expected first repo touched:** AI-Verse-Gateway  
**Later repos:** AI-Verse-System, then release/bootstrap owners only when their dependency gates are satisfied.  
