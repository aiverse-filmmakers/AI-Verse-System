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

**Status:** IN PROGRESS  
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

## Slice 4.2 - Brain/Gateway substantial-task learning trigger

**Status:** NOT STARTED  
**Repos:** Brain, Gateway, Memory, Skills  
**Dependencies:** 4.1

Wire current learning-candidate and evidence contracts into post-run/substantial-task review without reviewing every trivial turn.

## Slice 4.3 - Later task actually uses learned Skill

**Status:** NOT STARTED  
**Repos:** Gateway + Skills + composed owners  
**Dependencies:** 4.2

Prove restart persistence, active immutable generation, actual subsequent selection/use, rollback and quarantine paths.

---

# Phase 5 - Automatic Data emergence

## Slice 5.1 - Data safe additive structure creation/evolution

**Status:** NOT STARTED  
**Repos:** AI-Verse-Data  
**Dependencies:** current Data catalog/schema migration engine

Use existing Data Space, catalog, additive schema, idempotency, transaction, provenance and migration machinery.

Safe automatic operations are limited to additive/reversible owner-supported changes. Destructive/ambiguous migration remains approval-required.

## Slice 5.2 - Runtime structured-truth classification and owner routing

**Status:** NOT STARTED  
**Repos:** Brain + Gateway + Data  
**Dependencies:** 5.1

Meaningful repeated structured information should be routed into an existing or safely created Data structure without asking the user to choose Data/schema.

---

# Phase 6 - Temporary Workers and permanent Bot boundary

## Slice 6.1 - Automatic temporary Workers

**Status:** NOT STARTED  
**Repos:** AI-Verse-Multiple-Bots, Gateway  
**Dependencies:** existing Worker/lease/budget lifecycle

Use existing temporary Worker machinery automatically for requested work when justified by task complexity, within existing authority/budget/scope. No durable promotion.

## Slice 6.2 - Permanent Bot recommendation and consent

**Status:** NOT STARTED  
**Repos:** AI-Verse-Multiple-Bots, Gateway  
**Dependencies:** 6.1

Repeated specialist need may create a recommendation, not a durable Bot. Explicit user agreement or an explicit direct permanent-Bot request is required before canonical Bot creation.

---

# Phase 7 - Automation recommendation and consent boundary

## Slice 7.1 - Repeated responsibility recommendation

**Status:** NOT STARTED  
**Repos:** Brain/Gateway + AI-Verse-Automations  
**Dependencies:** existing Automations scheduler

Observed recurring time/event pattern may generate a natural-language recommendation only. No canonical schedule/job exists before consent.

## Slice 7.2 - Consent/direct request -> canonical Automation

**Status:** NOT STARTED  
**Repos:** AI-Verse-Automations + Gateway  
**Dependencies:** 7.1

Explicit yes or direct scheduling instruction creates through the existing Automations owner path, unless another authority boundary blocks it. No redundant confirmation.

---

# Phase 8 - Central invisible organization loop

## Slice 8.1 - Meaningful-work post-run organization routing

**Status:** NOT STARTED  
**Repos:** Gateway + Brain, consuming OS/Memory/Data/Skills/Bots/Automations owner APIs  
**Dependencies:** Phases 2-7 owner primitives

Implement the smallest owner-correct post-run routing path:

```text
meaningful work completes
-> bounded evidence
-> Brain/runtime classification
-> route to canonical owner
-> owner validates and mutates/proposes
-> verify
```

No Optimizer database, second Brain, scheduler or canonical store.

## Slice 8.2 - Review budget / trivial-turn suppression

**Status:** NOT STARTED  
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

- Total implementation slices: 24 including planning/final gates
- COMPLETE: 6
- IN PROGRESS: 1
- BLOCKED: 2
- NOT STARTED: 15

**Current slice:** 4.1 - Skills safe new-Skill auto-eligibility  
**Exact NEXT after current slice:** 4.2 - Brain/Gateway substantial-task learning trigger  
**Expected first repos touched:** AI-Verse-System, AI-Verse-OS  
**Later repos:** Brain, Memory, Skills, Data, Gateway, Multiple Bots, Automations, ai-verse-distribution  
