# Safe Update and Release Train Implementation Plan

**Status:** Persistent execution source of truth  
**Project:** AI-Verse safe-update, state-preservation and automated release-train infrastructure  
**Canonical repo:** `aiverse-filmmakers/AI-Verse-System`  
**Started:** 2026-09-14  
**Rule:** This document must be updated before and after every implementation slice. A slice is COMPLETE only when its acceptance criteria and exact evidence are recorded here.

## 0. Operating rules

1. Work one slice at a time.
2. Re-read this plan before every slice.
3. Re-inspect relevant GitHub `main`, active PRs, and current acceptance evidence before changing code.
4. Mark exactly one implementation slice `IN PROGRESS`.
5. Do not merge unrelated architecture work into the current Agent public-beta release.
6. `ai-verse-distribution` remains the only product installer/release-set/update authority.
7. Component repos remain independent owners of their software and canonical state.
8. Distribution orchestrates migrations. Component owners define and execute migration semantics.
9. Exact immutable revisions only. Never update users to floating `main`, implicit `latest`, or guessed combinations.
10. Updates fail closed when migration, compatibility, integrity, or authority preservation cannot be proven.
11. Normal update and uninstall must preserve canonical user state and unknown compatible user files.
12. Rollback is software rollback unless an owner explicitly supports canonical-state rollback.
13. Release metadata is not live health truth. Live `status` and `doctor` remain owner responsibilities.
14. No duplicate canonical Memory, Data, Brain, Bots, Token, scheduler, telemetry, updater, or release authority.
15. If implementation reality changes the plan, edit this document explicitly before continuing.

## 1. Baseline truth

System canonical docs reviewed at project start:

- `docs/FINAL-AI-VERSE-BLUEPRINT.md`
- `docs/PUBLIC-BETA-EXECUTION-PLAN.md`
- `docs/COMPONENT-INSTALL-SETUP-CONTRACT.md`
- `docs/PUBLIC-BETA-TRACKER.md`
- `docs/LIVING-SPEC-PROTOCOL.md`

Current accepted/main refs observed at project start:

| Repo | Current accepted/main evidence | Active conflicting work |
|---|---|---|
| AI-Verse-System | `67e96a3557a90dd03442955b76870f46d56fcd62` | none |
| ai-verse-distribution | `116aa2d74bb55c4ee00bf6139e98bb345b516b8a` | **PR #2 Agent public beta active**, head `e24a6503bba3597af2a51f20e9d4a3a755b8e9fe` |
| AI-Verse-OS | `9600929b946746c25c64e48471fcc83031fddda9` | none |
| AI-Verse-Brain | `80019be5e6df29aee70371544bd96cedbf0329b9` | none |
| AI-Verse-Memory | `031e1e77c97ed3c9012235c7ffe0a4ece05e3695` | none |
| AI-Verse-Skills | `042fda1ea2ddd8b79b74f1db9d3f65212953b64a` | none |
| AI-Verse-Data | `189b13264ab86115d2f21fee3ba8cd5a8dac6581` | none |
| AI-Verse-Gateway | `b20d56eddec6514ec4bc65b510318289b9cffa41` | none |
| AI-Verse-Automations | `494469a496d479cfec618bcd9511033c0cd3e815` | none |
| AI-Verse-Multiple-Bots | `9bffdffd07fb8abcea848213642936a23ecf4ecf` | none |
| ai-verse-token | `23b7b8ecbc9d9ef267f5e10449f785eb11107dd4` | none |

### Collision rule

Distribution PR #2 has priority. Until it is merged or otherwise safely resolved, release-train implementation must stay additive and non-conflicting. System contracts, schemas, validators, fixtures, and documentation may proceed independently. Distribution runtime/update changes that could alter the current Agent candidate are blocked behind the Agent-release dependency gate unless they are required safety fixes.

## 2. Status vocabulary

- `NOT STARTED`
- `IN PROGRESS`
- `BLOCKED`
- `COMPLETE`

Every slice records:

- affected repo(s)
- dependencies
- acceptance criteria
- evidence required
- exact commit/PR/workflow evidence
- next slice

---

# Phase 0 - Baseline, plan, and protected release boundary

## Slice 0.1 - Canonical plan and current-truth capture

**Status:** COMPLETE  
**Repos:** AI-Verse-System  
**Dependencies:** none

### Acceptance criteria

- canonical persistent plan exists in AI-Verse-System;
- all requested deliverables are represented as phased slices;
- current System docs are re-read;
- current main refs and active PR state are recorded;
- Distribution PR #2 is explicitly protected from conflicting changes;
- exact next slice is identified.

### Evidence required

- plan commit SHA;
- branch/PR reference;
- current Distribution PR #2 head;
- current main refs listed above.

### Evidence

- plan creation commit: `154b20cfc9652587febf80d9e242a9e3bfef0972`
- branch: `release-train/safe-update-plan`
- System baseline: `67e96a3557a90dd03442955b76870f46d56fcd62`
- Distribution active Agent PR: #2, head `e24a6503bba3597af2a51f20e9d4a3a755b8e9fe`
- current component refs are captured in the Baseline truth table above.

### NEXT

**Slice 1.1 - Freeze canonical update/state-preservation laws.**

---

# Phase 1 - Canonical contracts and schemas

## Slice 1.1 - Freeze update/state-preservation laws

**Status:** COMPLETE  
**Repos:** AI-Verse-System  
**Dependencies:** 0.1

### Acceptance criteria

Canonical System contract explicitly defines:

- software/state separation;
- unknown migration means stop;
- update fail-closed behavior;
- unknown/user files survive;
- no silent authority changes;
- owner-controlled migration;
- software-only rollback semantics;
- safe refusal over destructive success;
- update consent separation;
- safe uninstall/purge separation;
- owner-backed checkpoint/backup policy;
- modularity/non-duplication constraints.

### Evidence required

- contract file and commit SHA;
- doc/spec validation if present;
- PR and merged SHA;
- changelog/blueprint updates required by Living Spec Protocol.

### Evidence

- canonical contract: `docs/SAFE-UPDATE-AND-STATE-PRESERVATION-CONTRACT.md`
- implementation commits on PR branch: `eb10ef9fdd7fbcc07e347976e8b558c2fe941dc5`, `dcf9ce9d2787d0ae04887f3b8735bdfdc90b5159`, `f9f41b0c449cfc9034ae621b39627ae58e1f03e5`, `ef38198e99dd1617eaf7044dc355f628b206e6cf`
- System PR: #7
- merged SHA: `88da0c7dbeb3e80dfe1ff24dfdfb3b51365afe27`
- AI-Verse-System had no `.github/workflows` directory at this slice, so no hosted workflow existed to run; acceptance was repository-content verification plus merge.
- Blueprint, install/setup lifecycle contract, and System changelog were updated in the same accepted PR.

## Slice 1.2 - Machine-readable Component Release Descriptor contract

**Status:** IN PROGRESS  
**Repos:** AI-Verse-System  
**Dependencies:** 1.1

### Acceptance criteria

Descriptor contract/schema covers:

- component id;
- exact 40-char immutable revision;
- version;
- release status;
- supported platforms;
- runtime requirements;
- lifecycle support;
- canonical-state ownership and preservation claims;
- update/migration compatibility;
- authority-negative facts;
- acceptance/CI evidence;
- distinction from live health truth.

Schema has positive and negative fixtures/tests.

### Evidence required

- schema path;
- validator/test paths;
- passing validation evidence;
- commit/PR/workflow refs.

### Evidence so far

- schema: `contracts/component-release-descriptor.schema.json`
- semantics doc: `docs/COMPONENT-RELEASE-DESCRIPTOR-CONTRACT.md`
- validator: `scripts/validate_component_release_descriptor.py`
- tests: `tests/test_component_release_descriptor.py`
- fixtures: `contracts/examples/component-release-descriptor.valid.json`, `contracts/examples/component-release-descriptor.invalid-floating-ref.json`
- workflow: `.github/workflows/contract-validation.yml`
- System PR: #8
- current PR head before this plan sync: `7e2255ca4cd73e0c7149f611f2195df07965818e`
- hosted workflow evidence: pending; slice remains IN PROGRESS until validation passes.

## Slice 1.3 - Whole-release preservation result contract

**Status:** NOT STARTED  
**Repos:** AI-Verse-System  
**Dependencies:** 1.2

### Acceptance criteria

Machine-readable acceptance result can represent:

- source and target release set;
- clean install;
- upgrade;
- restart/recovery;
- per-owner state preservation;
- authority preservation;
- platform acceptance;
- migration evidence;
- unsafe/failing outcomes.

### Evidence required

- schema/test paths;
- passing contract tests;
- commit/PR/workflow refs.

---

# Phase 2 - Component release-descriptor adoption

## Slice 2.1 - Descriptor support for Core owners

**Status:** NOT STARTED  
**Repos:** AI-Verse-OS, AI-Verse-Brain, AI-Verse-Memory, AI-Verse-Skills, AI-Verse-Data  
**Dependencies:** 1.2  
**Constraint:** do not reopen mature engines beyond release metadata and necessary lifecycle truth.

### Acceptance criteria

Each current Core repo exposes a descriptor conforming to the System contract and pinned to its immutable candidate revision/version/evidence. Descriptor does not claim live health.

### Evidence required

Per repo: commit/PR, schema validation, CI result.

## Slice 2.2 - Descriptor support for Agent owners

**Status:** NOT STARTED  
**Repos:** AI-Verse-Gateway, AI-Verse-Automations, AI-Verse-Multiple-Bots, ai-verse-token  
**Dependencies:** 1.2 and safe Agent release boundary  
**Constraint:** avoid destabilizing current Agent release candidate.

### Acceptance criteria

Each repo exposes a conforming descriptor with truthful lifecycle, state, migration, platform, and authority-negative facts.

### Evidence required

Per repo: commit/PR, schema validation, CI result.

---

# Phase 3 - Distribution candidate discovery and ingestion

## Slice 3.1 - Candidate discovery design and deterministic registry

**Status:** NOT STARTED  
**Repos:** ai-verse-distribution, AI-Verse-System if contract docs need updates  
**Dependencies:** 1.2; Agent PR #2 safely merged/resolved

### Acceptance criteria

Distribution can deterministically identify:

- currently accepted component revision;
- newer candidate;
- exact immutable SHA;
- version;
- migration/compatibility metadata;
- acceptance evidence.

No central database service. No vendored component engines.

### Evidence required

- design/maintainer docs;
- deterministic script/tests;
- commit/PR/workflow refs.

## Slice 3.2 - Candidate descriptor validation and affected-profile calculation

**Status:** NOT STARTED  
**Repos:** ai-verse-distribution  
**Dependencies:** 3.1

### Acceptance criteria

Ingestion rejects:

- malformed descriptors;
- non-immutable refs;
- revision/version mismatches;
- missing required evidence;
- impossible platform/runtime claims.

It deterministically identifies affected profiles/release sets.

### Evidence required

- focused tests including reject cases;
- commit/PR/workflow refs.

## Slice 3.3 - Candidate release-set generation

**Status:** NOT STARTED  
**Repos:** ai-verse-distribution  
**Dependencies:** 3.2

### Acceptance criteria

Accepted input produces a candidate release set that records exact component revisions and never mutates released/current sets.

### Evidence required

- golden fixtures;
- idempotency tests;
- commit/PR/workflow refs.

---

# Phase 4 - Explicit release-set transition compatibility

## Slice 4.1 - Permanent compatibility matrix

**Status:** NOT STARTED  
**Repos:** ai-verse-distribution  
**Dependencies:** 3.3

### Acceptance criteria

Compatibility is explicit and not inferred only from semver. Data can represent:

- supported source sets;
- target set;
- runtime requirements;
- migration requirements;
- rollback compatibility;
- platform support;
- state-preservation expectations;
- known incompatible transitions.

### Evidence required

- compatibility schema/data;
- allow/deny tests;
- commit/PR/workflow refs.

## Slice 4.2 - Owner migration/checkpoint evidence policy

**Status:** NOT STARTED  
**Repos:** AI-Verse-System, ai-verse-distribution  
**Dependencies:** 4.1

### Acceptance criteria

Distribution records/requires owner evidence instead of copying canonical stores. High-risk/destructive migrations cannot be promoted without an owner recovery contract.

### Evidence required

- policy docs;
- machine-readable fields;
- failure tests;
- commit/PR/workflow refs.

---

# Phase 5 - Update planning UX and consent

## Slice 5.1 - `aiverse update` preview

**Status:** NOT STARTED  
**Repos:** ai-verse-distribution  
**Dependencies:** 4.1

### Acceptance criteria

Human preview truthfully shows:

- current and target release;
- per-component version/revision changes;
- preserved state claims;
- migration implications;
- authority changes or `none`;
- blocking conditions;
- exact apply command.

No software changes occur on preview.

### Evidence required

- CLI tests/snapshots;
- commit/PR/workflow refs.

## Slice 5.2 - `aiverse update --json`

**Status:** NOT STARTED  
**Repos:** ai-verse-distribution  
**Dependencies:** 5.1

### Acceptance criteria

Stable structured preview includes all human-visible safety facts and stable blocked/migration-required states.

### Evidence required

- JSON contract tests;
- commit/PR/workflow refs.

## Slice 5.3 - Explicit apply and accepted-channel enforcement

**Status:** NOT STARTED  
**Repos:** ai-verse-distribution  
**Dependencies:** 5.2

### Acceptance criteria

- `aiverse update` only previews/checks;
- `aiverse update --apply` is explicit consent;
- normal update consumes only accepted release sets;
- optional candidate selection, if supported, is explicit;
- no implicit `latest` or floating branch.

### Evidence required

- positive/negative CLI tests;
- commit/PR/workflow refs.

---

# Phase 6 - Safe update transaction and recovery

## Slice 6.1 - Existing recovery audit

**Status:** NOT STARTED  
**Repos:** ai-verse-distribution  
**Dependencies:** 5.3

### Acceptance criteria

Document whether current Distribution already has sufficient durable transaction/recovery state. If insufficient, define the minimal operational journal only.

### Evidence required

- code audit notes in plan/maintainer doc;
- explicit decision: reuse/extend/new minimal journal.

## Slice 6.2 - Durable update journal

**Status:** NOT STARTED  
**Repos:** ai-verse-distribution  
**Dependencies:** 6.1 only if gap exists

### Acceptance criteria

Journal records:

- source set;
- target set;
- active component;
- staged components;
- lifecycle results;
- migration started/completed;
- activation state;
- recovery instructions.

Journal does not duplicate canonical owner state.

### Evidence required

- persistence/crash tests;
- commit/PR/workflow refs.

## Slice 6.3 - Resume/recover/software rollback truth

**Status:** NOT STARTED  
**Repos:** ai-verse-distribution  
**Dependencies:** 6.2 or reuse decision

### Acceptance criteria

After interruption:

- status/doctor does not claim a clean completed update;
- resume/recover path is truthful;
- software rollback is only allowed when explicitly compatible;
- no canonical-state rewind is implied unless owner supports it.

### Evidence required

- crash/restart tests;
- rollback refusal tests;
- commit/PR/workflow refs.

---

# Phase 7 - Package-owned file safety and uninstall safety

## Slice 7.1 - Package ownership manifest and unknown-file preservation

**Status:** NOT STARTED  
**Repos:** ai-verse-distribution  
**Dependencies:** 5.3

### Acceptance criteria

Updater replaces only package-owned software files. Unknown/user-created compatible files survive. Collision with target package path fails closed or uses explicit owner-approved resolution.

### Evidence required

- user-file collision tests;
- byte-preservation tests;
- commit/PR/workflow refs.

## Slice 7.2 - Uninstall/purge lifecycle audit

**Status:** NOT STARTED  
**Repos:** Distribution plus included public-beta component repos only where needed  
**Dependencies:** 7.1

### Acceptance criteria

Normal uninstall preserves canonical user state by default. Destructive purge, where present, is separate, explicit, never called by update, and never implied by normal uninstall.

### Evidence required

- per-component audit table;
- focused lifecycle tests;
- corrective PRs only where genuinely unsafe.

---

# Phase 8 - Real old-release to new-release preservation acceptance

## Slice 8.1 - Upgrade harness foundation

**Status:** NOT STARTED  
**Repos:** ai-verse-distribution  
**Dependencies:** 4.2, 5.3, 6.3, 7.1

### Acceptance criteria

Harness can install released set A, create realistic state, snapshot identities/digests/counts/bytes/enablement/authority, apply candidate B, restart, and verify post-update truth.

### Evidence required

- harness code;
- deterministic fixture setup;
- CI runnable entrypoint;
- commit/PR/workflow refs.

## Slice 8.2 - Core state preservation proof

**Status:** NOT STARTED  
**Repos:** ai-verse-distribution; owners only for genuine blockers  
**Dependencies:** 8.1

### Acceptance criteria

Prove preservation for Brain, Memory, Data, Skills, OS/workspace config and user files, including disabled-state and authority preservation.

### Evidence required

- old->new run ID(s);
- exact source/target sets;
- snapshots/digests;
- passing CI evidence.

## Slice 8.3 - Agent state preservation proof

**Status:** NOT STARTED  
**Repos:** ai-verse-distribution; owners only for genuine blockers  
**Dependencies:** 8.2

### Acceptance criteria

Also prove Multiple Bots coordination state, Token telemetry evidence, Gateway/runtime configuration where durable, Automations state where applicable, and composed post-restart status/doctor truth.

### Evidence required

- old->new run ID(s) on supported platforms;
- exact source/target sets;
- state evidence;
- passing CI.

## Slice 8.4 - Explicit migration-required path

**Status:** NOT STARTED  
**Repos:** ai-verse-distribution plus owner fixture/stub as appropriate  
**Dependencies:** 8.1

### Acceptance criteria

Unsupported transition returns update-blocked/migration-required with unchanged state. Supported explicit migration proves owner checkpoint contract, apply, verify, and interrupted-recovery behavior where applicable.

### Evidence required

- negative and positive migration runs;
- before/after digests;
- commit/PR/workflow refs.

---

# Phase 9 - Destructive transition negative tests

## Slice 9.1 - Unsupported migration and source drift

**Status:** NOT STARTED  
**Repos:** ai-verse-distribution  
**Dependencies:** 8.1

### Acceptance criteria

Unsupported migration, wrong release SHA, or source drift fails closed and leaves user state unchanged.

## Slice 9.2 - Disabled-state, permission-floor, and Brain-ownership preservation

**Status:** NOT STARTED  
**Repos:** ai-verse-distribution with composed owners  
**Dependencies:** 8.1

### Acceptance criteria

Update does not re-enable disabled components, expand permissions/scope, or transfer strategic direction ownership.

## Slice 9.3 - Partial failure recovery

**Status:** NOT STARTED  
**Repos:** ai-verse-distribution  
**Dependencies:** 6.3, 8.1

### Acceptance criteria

Injected component-N failure leaves canonical state intact, reports incomplete state, exposes recovery, and never reports fake success.

### Evidence required for Phase 9

Focused failing-transition tests, unchanged-state snapshots, exact CI workflow/run IDs, commit/PR refs.

---

# Phase 10 - Automated component to Distribution PR train

## Slice 10.1 - Candidate discovery automation

**Status:** NOT STARTED  
**Repos:** ai-verse-distribution and/or component workflow templates as chosen  
**Dependencies:** 2.1, 2.2, 3.3

### Acceptance criteria

Automation discovers accepted component candidates using the descriptor contract and exact immutable SHA.

### Evidence required

- workflow/script;
- dry-run fixture;
- commit/PR/workflow refs.

## Slice 10.2 - Automatic candidate PR creation/update

**Status:** NOT STARTED  
**Repos:** ai-verse-distribution  
**Dependencies:** 10.1

### Acceptance criteria

Automation:

1. validates descriptor;
2. compares against accepted set;
3. determines affected profiles;
4. creates/updates candidate set;
5. opens or updates a Distribution PR;
6. includes old/new SHA, versions, migration/state implications, and CI evidence;
7. avoids duplicate PR spam and uses deterministic coalescing where practical.

### Evidence required

- end-to-end automation test or real generated PR;
- exact PR number;
- workflow run ID.

## Slice 10.3 - Promotion gate

**Status:** NOT STARTED  
**Repos:** ai-verse-distribution  
**Dependencies:** 10.2, Phase 8, Phase 9

### Acceptance criteria

Failed candidate cannot alter current released channel. Passing candidate is only marked eligible after all defined acceptance evidence is green. User-facing promotion remains policy-gated.

### Evidence required

- bad-candidate proof;
- safe-candidate proof;
- exact workflow/PR refs.

---

# Phase 11 - Whole-release evidence and maintainer documentation

## Slice 11.1 - Machine-readable release preservation evidence

**Status:** NOT STARTED  
**Repos:** ai-verse-distribution  
**Dependencies:** Phase 8 and Phase 9

### Acceptance criteria

Each candidate/released set can publish a preservation result conforming to System contract. Distribution never labels update-safe without required evidence.

## Slice 11.2 - Maintainer release-train documentation

**Status:** NOT STARTED  
**Repos:** ai-verse-distribution, AI-Verse-System  
**Dependencies:** 10.3, 11.1

### Acceptance criteria

Docs explain candidate creation, descriptor validation, compatibility, migrations, state-preservation testing, promotion, recovery, rollback limits, and incident handling.

## Slice 11.3 - Living-spec synchronization

**Status:** NOT STARTED  
**Repos:** AI-Verse-System  
**Dependencies:** 11.2

### Acceptance criteria

Final Blueprint, Public Beta plan/tracker, relevant component specs/QC/source maps, and System Changelog reflect implemented CURRENT behavior and deliberately deferred post-beta work.

---

# Phase 12 - Final project acceptance

## Slice 12.1 - Required acceptance scenarios A-J

**Status:** NOT STARTED  
**Repos:** cross-repo, primarily ai-verse-distribution  
**Dependencies:** all prior required slices

### Acceptance criteria

Prove all:

A. component update proposal automatically produces exact immutable Distribution candidate change;  
B. bad candidate cannot change current release;  
C. safe candidate becomes promotion-eligible;  
D. real existing installation upgrades with state intact;  
E. unsupported migration refuses safely;  
F. crash reports incomplete/recoverable state and preserves canonical data;  
G. disabled component remains disabled;  
H. permissions/scope/Brain ownership remain unchanged absent explicit user action;  
I. user-created compatible files survive;  
J. rollback obeys explicit compatibility and does not pretend to rewind canonical user state.

### Evidence required

Exact source/target release sets, PRs, merge SHAs, workflow/run/job IDs, snapshots/digests, and owner evidence.

## Slice 12.2 - Final release-train gate

**Status:** NOT STARTED  
**Repos:** AI-Verse-System, ai-verse-distribution, any owner with accepted corrective fixes  
**Dependencies:** 12.1

### Acceptance criteria

All required slices COMPLETE. No unresolved destructive update path. No duplicate release/update/canonical authority. Final project report can truthfully answer:

- repos changed;
- PRs/merge SHAs;
- workflows/run IDs;
- implemented now;
- deliberately post-beta;
- whether automatic component -> Distribution candidate flow is live;
- whether old-release -> new-release preservation is actually tested;
- whether any component still has unsafe lifecycle behavior;
- whether any update path can still silently delete canonical user state.

---

# 3. Deferred/post-beta rule

A feature is deliberately post-beta when it is not required to preserve update safety, state, authority, compatibility, recovery, or the defined current public-beta release workflow. Optional future public `aiverse-filmmakers/AI-Verse` landing repo, automatic user auto-update, extra release channels, hosted control services, and marketplace/enterprise release complexity stay out unless a later explicit requirement promotes them.

# 4. Overall progress

- Total planned slices: 34
- COMPLETE: 2
- IN PROGRESS: 1
- BLOCKED: 0
- NOT STARTED: 31
- Project completion: 6%

**Current slice:** 1.2  
**Exact NEXT after current slice:** 1.3 - Whole-release preservation result contract.
