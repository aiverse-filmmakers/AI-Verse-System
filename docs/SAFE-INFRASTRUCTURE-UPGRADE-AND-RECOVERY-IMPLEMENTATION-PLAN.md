# AI-Verse Safe Infrastructure Upgrade, Convergence and Recovery Implementation Plan

**Status:** ACTIVE  
**Canonical planning repo:** `aiverse-filmmakers/AI-Verse-System`  
**Primary orchestration repo:** `aiverse-filmmakers/ai-verse-distribution`  
**Initial owner repos:** `aiverse-filmmakers/AI-Verse-OS`, `aiverse-filmmakers/AI-Verse-Skills`  
**Started:** 2026-10-12  
**Planning method:** `docs/ADAPTIVE-IMPLEMENTATION-PLANNING-SKILL.md`  
**Program size:** 18 slices  
**Completed:** 1  
**Remaining:** 17  
**Overall progress:** 5.6%  
**Current phase:** Phase 1 - Audit current update, infrastructure and recovery reality  
**Current phase progress:** 0/3  
**Slices until Phase 2:** 3  
**Next:** Slice 1.1 - Audit existing update, doctor, migration, workspace, Skills and recovery mechanisms  
**Next slice task list:** NOT YET DERIVED - derive from live evidence at slice start

> This plan is intentionally stable at the level of laws, phase purpose, slice outcome and acceptance criteria, while low-level tasks remain adaptive. Discovery may adapt the route; it may not silently change the destination.

---

# 0. Mission

Make AI-Verse upgrades improve existing installations, not only fresh installs.

A member who has used AI-Verse for months must be able to receive newer software, audit whether their existing project structure is behind the current architecture, preview a safe modernization plan, explicitly apply it, and restore the entire local installation to the previous known-good state if the result is not acceptable.

The target user model is intentionally small:

```text
aiverse update
    preview available software/release changes

aiverse update --apply
    create/refresh one verified last-known-good recovery point
    apply/stage admitted software changes
    do not perform optional structural modernization

aiverse doctor
    read-only audit of release health + infrastructure drift

aiverse upgrade
    read-only preview of recommended/required infrastructure convergence

aiverse upgrade --apply
    create/refresh one verified last-known-good recovery point
    apply explicit owner-controlled structural migrations
    repair references
    verify the result

aiverse restore
    restore the latest valid last-known-good local recovery point
```

The default UI must remain short. Detailed evidence exists on demand.

---

# 1. Permanent laws

These are protected program outcomes. Adaptive discovery may not weaken them automatically.

## 1.1 User-owned state is never guessed away

Nothing user-owned may be deleted, reset, overwritten, silently relocated, silently re-scoped or discarded merely because a newer architecture exists.

Unknown/custom files remain user-owned unless canonical ownership can be proved.

## 1.2 Update and infrastructure convergence are separate concepts

`update` is primarily software/release delivery.

`upgrade` is infrastructure convergence: bringing an existing installation's owned/migratable structure toward the architecture expected by the admitted target release.

Optional structural modernization must not be hidden inside a normal software update.

If target software cannot safely activate against the current infrastructure, the release may be staged but activation must remain blocked until the required admitted migration succeeds.

## 1.3 Doctor and preview commands are read-only

`aiverse doctor`, `aiverse update`, and `aiverse upgrade` without `--apply` must not mutate project/user state.

## 1.4 Canonical owners define migrations

OS owns OS/workspace structure semantics and migrations.

Skills owns Skills state/layout/scope semantics and migrations.

Future components own their own migrations.

Distribution discovers, plans, coordinates, checkpoints, invokes, verifies and records migrations. It must not invent sibling domain migration semantics.

## 1.5 Machine-readable upgrade recipes, never AI guesswork

Structural change must be driven by versioned, owner-published migration/upgrade metadata and executable owner handlers.

AI reasoning may help explain, classify or propose, but `upgrade --apply` must not reorganize infrastructure merely because an agent thinks a newer arrangement looks better.

## 1.6 Explicit infrastructure generations

Movable/migratable structural domains must expose enough generation/schema identity for the system to determine source state, target state and admitted migration path without guessing from filenames alone.

Skip-version behavior must be explicit: direct migration or a validated migration chain.

## 1.7 Stable identity over filesystem path

Any first-class entity that may move during a legitimate upgrade should use stable identity independent of its current path where technically applicable.

Moving `workspaces/ChannelName` to `workspaces/YouTube/ChannelName` must not silently create a new logical workspace or orphan references.

## 1.8 Migrations are idempotent and evidence-bound

A migration applied twice must not duplicate content, repeat destructive moves or corrupt state.

Upgrade plans must be bound to source generation/state fingerprints and exact target release evidence. Source drift before apply forces re-plan or safe refusal.

## 1.9 Reference repair is part of migration

A move is incomplete until affected references, indexes, manifests, automations, links and owner-declared dependants are either repaired or explicitly proven unaffected.

## 1.10 Legacy infrastructure retires only after proof

Old writable structures/routes may be retired only after the new structure verifies successfully and no supported dependency still requires the old path.

Compatibility clutter must not accumulate forever, but cleanup must never precede proof.

## 1.11 One rotating Last-Known-Good recovery point

Before every mutating `update --apply` or `upgrade --apply`, AI-Verse must have one verified recoverable pre-action snapshot/checkpoint representing the local installation immediately before that action.

Only one retained last-known-good recovery point is required by this program.

The sole usable recovery point must never be destroyed before a valid successor exists.

A new candidate recovery point must be staged and verified before it replaces the previous one. If the current installation is too unhealthy or ambiguous to become a trustworthy recovery point, preserve the existing known-good point and fail safely rather than rotating it away.

## 1.12 Restore means exact local restoration within declared scope

`aiverse restore` must restore the covered local AI-Verse installation/project state to the retained pre-action snapshot, including the exact admitted software/release selection and covered files/state needed to reproduce that local point.

The restore contract must explicitly define exclusions such as external services, remote side effects, external credential stores and disposable caches. It must never claim to rewind things it cannot actually rewind.

## 1.13 Recovery snapshot is not a second canonical live store

The retained recovery point is immutable recovery material, not another writable canonical Memory/Data/Skills/OS source.

Normal runtime must never read/write it as live state.

## 1.14 Simple UX, deep evidence on demand

Default member-facing output should fit on a small screen and communicate only:

```text
Safe improvements: N
Needs review: N
Blocked: N
Risk: LOW | MEDIUM | HIGH
User-owned files deleted: NO
Recommended action: <command>
```

Full migration detail, evidence and provenance remain available through an explicit details mode or machine-readable output.

## 1.15 No concurrent-plan overwrite

This program may coexist with the active repository-network governance program, but implementation must refetch current files/refs before every write and must not overwrite overlapping work from another active plan.

If another program is actively changing the same contract/surface incompatibly, block and reconcile rather than racing it.

---

# 2. Intended ownership

## AI-Verse-System

Owns canonical cross-repo laws for:

- update versus infrastructure upgrade semantics;
- infrastructure convergence;
- recovery-point/restore guarantees;
- migration ownership;
- upgrade-recipe semantics;
- generation/identity invariants;
- non-invasive member UX expectations;
- cross-component acceptance requirements.

System does not implement migrations or runtime backup engines.

## AI-Verse-OS

Initially owns:

- workspace/domain hierarchy semantics;
- workspace stable identity where appropriate;
- workspace infrastructure generation;
- detection of OS/workspace structural drift;
- workspace migration planning/handlers;
- reference repair for OS-owned references;
- retirement of obsolete OS-owned workspace infrastructure.

The motivating fixture is the current class of problem:

```text
Current:
workspaces/<ChannelName>/youtube/...

Target style:
workspaces/YouTube/<ChannelName>/...
```

The exact target structure must be validated from current OS architecture during Phase 1 rather than assumed solely from this example.

## AI-Verse-Skills

Initially owns:

- skill scope semantics;
- workspace-local versus domain/shared versus OS-wide decisions where canonically representable;
- Skills structural/state generations;
- safe promotion/re-scoping migrations;
- Skills stable identity/provenance across moves where applicable;
- Skills-owned reference repair;
- retirement of stale writable legacy Skill locations only after proof.

The motivating fixture is a reusable YouTube transcript/book Skill incorrectly created inside one channel/project and then reused from another project.

## ai-verse-distribution

Owns orchestration and member-facing lifecycle:

- current/target release awareness;
- gathering owner upgrade recipes;
- read-only doctor/upgrade plan aggregation;
- one rotating Last-Known-Good recovery point;
- update/upgrade transaction state;
- invoking owner migrations;
- whole-install verification;
- activation gating;
- restore orchestration;
- short traffic-light UX and detailed/machine-readable views.

Distribution must not decide workspace hierarchy or Skill scope rules itself.

## Future component repos

No future component is modified merely because this framework exists.

A component adopts the recipe/generation model only when it has a real structural/state migration requirement. The framework must be extensible without forcing ceremonial migration code into every repository.

---

# 3. Existing canonical law that must be reconciled deliberately

`docs/SAFE-UPDATE-AND-STATE-PRESERVATION-CONTRACT.md` currently states that Distribution should not duplicate every canonical store merely to claim update safety and should rely on owner-backed recovery guarantees.

This new program intentionally introduces a different product guarantee: one rotating whole-local-installation Last-Known-Good recovery point before every mutating update/upgrade apply.

Therefore implementation must not simply violate the old law.

Phase 2 must explicitly amend/reconcile the canonical contract so that:

- owner-native checkpoints remain authoritative for component-internal transactional safety;
- the single Distribution-orchestrated Last-Known-Good recovery point exists for whole-install/user recovery;
- the recovery snapshot remains immutable/non-canonical;
- only one retained recovery point is required;
- rotation cannot destroy the sole valid recovery point prematurely;
- restore scope/exclusions are truthful.

---

# 4. Adaptive execution and change authority

This program follows `docs/ADAPTIVE-IMPLEMENTATION-PLANNING-SKILL.md`.

At the start of every substantial slice:

1. read the latest plan and completed findings;
2. refetch the exact live repos/files in scope;
3. inspect what already exists;
4. classify needs as `REUSE`, `EXTEND`, `CREATE`, `RETIRE` or `BLOCK/UNKNOWN`;
5. derive the smallest task list necessary for the fixed slice acceptance criteria;
6. record the task list and starting refs before implementation.

Tasks and implementation technique are adaptive.

Permanent laws, phase purpose, slice purpose and acceptance floors are protected.

If evidence requires changing one of those, use:

`BLOCKED - PLAN AMENDMENT REQUIRED`

and prepare the amendment proposal required by the adaptive planning skill.

---

# 5. Progress bookkeeping

Overall progress is slice-based:

`completed slices / 18 * 100`

Task counts are local to the current slice and may change from evidence.

Before a slice becomes COMPLETE, this plan must record:

- final derived tasks and statuses;
- exact implementation refs;
- exact tests/evidence;
- owner/System/Distribution impact;
- preservation/recovery impact;
- blockers/drift/amendments;
- phase and overall counters;
- explicit NEXT slice.

Mandatory completion report:

```text
Completed: Slice X.Y - <title>
Tasks: <completed>/<final derived total>
Overall: <completed>/18 slices (<percent>%)
Phase: <phase number> - <title>
Phase progress: <completed>/<total>
Until next phase: <N> slice(s)
Next: <next slice>
Blockers/drift/amendments: <none or concise status>
```

---

# Phase 0 - Program foundation

## Slice 0.1 - Create the canonical implementation program

**Status:** COMPLETE  
**Repos:** AI-Verse-System  
**Dependencies:** none

### Acceptance criteria

- adaptive implementation plan exists in the canonical System repo;
- user-facing update/doctor/upgrade/restore model is explicit;
- one rotating Last-Known-Good recovery guarantee is explicit;
- conflict with current safe-update backup law is identified rather than ignored;
- OS, Skills, Distribution and System ownership is explicit;
- workspace and Skill problems are represented as mandatory real-world fixtures;
- low-level tasks remain adaptive;
- future agents can resume without this conversation.

### Evidence

- canonical plan: `docs/SAFE-INFRASTRUCTURE-UPGRADE-AND-RECOVERY-IMPLEMENTATION-PLAN.md`
- planning method: `docs/ADAPTIVE-IMPLEMENTATION-PLANNING-SKILL.md`

### NEXT

Slice 1.1.

---

# Phase 1 - Audit current update, infrastructure and recovery reality

**Phase size:** 3 slices  
**Current phase progress:** 0/3  
**Purpose:** prove what already exists before defining new machinery.

## Slice 1.1 - Audit existing update, doctor, migration, workspace, Skills and recovery mechanisms

**Status:** NOT STARTED  
**Dependencies:** 0.1  
**Adaptive tasks:** derive from live evidence at slice start

Audit at minimum:

- current Distribution update/check/apply/status/doctor/rollback/recovery behavior;
- current release-set activation semantics;
- existing package manifests and owned-path tracking;
- current checkpoint/backup/recovery mechanisms;
- current OS workspace identity, layout, creation logic and references;
- current Skills storage, identity, generations, provenance and local/global scoping;
- existing migration schemas/handlers in OS and Skills;
- existing generated/member-facing files affected by moves;
- existing tests for path moves, user-file preservation and recovery;
- active overlapping work from the repository-network governance plan.

### Acceptance criteria

- exact current behavior is evidenced before new implementation is proposed;
- existing reusable mechanisms are identified;
- workspace and Skills motivating problems are reproduced/classified from real implementation;
- current restore capability and gaps are known;
- no implementation change occurs before the audit is recorded.

### NEXT

Slice 1.2.

---

## Slice 1.2 - Build ownership, identity, reference, migration and recovery inventory

**Status:** NOT STARTED  
**Dependencies:** 1.1  
**Adaptive tasks:** derive from Slice 1.1 findings

Classify relevant mechanisms as `REUSE`, `EXTEND`, `CREATE`, `RETIRE` or `BLOCK/UNKNOWN`.

Inventory:

- canonical owner for every movable structure/state surface;
- stable ID versus path-based identity;
- reference/dependency edges affected by moves;
- current structure/schema generations if any;
- migration-chain capabilities;
- user-owned versus package-owned/generated boundaries;
- recovery-point scope and exclusions;
- snapshot size/performance risks;
- current health signals needed before safe recovery-point rotation;
- legacy writable routes that may need retirement.

### Acceptance criteria

- Distribution shadow-domain logic is prohibited/identified;
- path-identity risks are explicit;
- exact recovery coverage required for truthful `restore` is known;
- no duplicate migration/backup framework is planned where existing machinery can be extended.

### NEXT

Slice 1.3.

---

## Slice 1.3 - Freeze implementation architecture and acceptance matrix

**Status:** NOT STARTED  
**Dependencies:** 1.2  
**Adaptive tasks:** derive from evidence-backed inventory

Freeze evidence-backed decisions for:

- update versus upgrade activation semantics;
- doctor/preview read-only contract;
- upgrade-recipe schema/home;
- generation/state-fingerprint semantics;
- stable identity requirements;
- reference-repair ownership;
- Last-Known-Good snapshot location/scope/exclusions;
- atomic snapshot rotation policy;
- restore semantics;
- health gate before snapshot replacement;
- simple traffic-light member UX;
- machine-readable detailed output;
- test matrix for current->target convergence and restore.

### Acceptance criteria

- every new mechanism has one canonical owner;
- no unresolved source-of-truth duplication remains;
- snapshot/restore promise is technically truthful;
- Phase 2 can change canonical law without architectural guessing.

### NEXT

Phase 2 / Slice 2.1.

---

# Phase 2 - Define canonical convergence, migration and recovery contracts

**Phase size:** 3 slices

## Slice 2.1 - Amend the Safe Update and State Preservation Contract

**Status:** NOT STARTED  
**Dependencies:** 1.3  
**Adaptive tasks:** derive from the frozen Phase 1 architecture

Explicitly reconcile the current owner-backed backup law with the approved one-rotating-Last-Known-Good product guarantee.

Also define the separation between:

- software update;
- structural/infrastructure upgrade;
- software rollback;
- whole-local-install restore.

### Acceptance criteria

- no contradiction remains between canonical law and intended implementation;
- owner-native checkpoints remain authoritative for component transaction safety;
- one rotating whole-install recovery point is canonical and bounded;
- restore does not falsely claim reversal of external systems;
- sole valid recovery point cannot be destroyed before a verified successor exists.

### NEXT

Slice 2.2.

---

## Slice 2.2 - Define versioned infrastructure generation and upgrade-recipe contract

**Status:** NOT STARTED  
**Dependencies:** 2.1  
**Adaptive tasks:** reuse/extend existing component release metadata if Phase 1 proves appropriate

Define the minimum machine-readable semantics required for an owner to publish a structural migration, including as applicable:

- migration/recipe ID and version;
- canonical owner;
- source generation/range;
- target generation;
- target release binding;
- detection/preconditions;
- migration handler/entrypoint;
- reference-repair obligations;
- postconditions;
- risk/recovery requirements;
- idempotency declaration/proof;
- skip-version/direct-versus-chain behavior;
- legacy retirement conditions;
- user-visible summary text.

Do not create a parallel release metadata system if the existing component release descriptor can safely own these fields through versioned extension.

### Acceptance criteria

- `upgrade --apply` never depends on free-form AI inference to know what structural mutation to execute;
- exact owner and exact migration path are machine-resolvable;
- unsupported/unknown path fails closed.

### NEXT

Slice 2.3.

---

## Slice 2.3 - Define convergence, restore and member UX invariants

**Status:** NOT STARTED  
**Dependencies:** 2.2

Define permanent acceptance invariants, including:

### Convergence invariant

After a successful admitted upgrade, package-owned/generated/migratable infrastructure should conform to the target release's current architecture while legitimate user state/history remains preserved.

### Restore invariant

After a successful `aiverse restore`, all locally covered state must match the retained Last-Known-Good recovery point exactly according to the declared restore scope and verification method.

### UX invariant

Default output remains small-screen friendly; details/evidence are opt-in.

### Acceptance criteria

- fresh-install versus upgraded-install structural equivalence is testable;
- restore exactness is testable;
- user-facing simplicity does not remove machine-readable evidence.

### NEXT

Phase 3 / Slice 3.1.

---

# Phase 3 - Implement canonical owner migrations for the motivating problems

**Phase size:** 4 slices

## Slice 3.1 - Implement OS workspace identity, hierarchy and generation semantics

**Status:** NOT STARTED  
**Dependencies:** 2.3  
**Adaptive tasks:** derive from actual OS implementation

Implement only what Phase 1 proves necessary for OS to understand and create maintainable workspace hierarchy.

Mandatory fixture: domain/category-first grouping such as YouTube -> channel/project, while preserving the ability to represent client/project structures such as Clients -> Nike where appropriate.

### Acceptance criteria

- OS owns the rule, not Distribution;
- movable workspaces have stable identity where needed;
- new workspace creation no longer reproduces the proven bad hierarchy case;
- user custom hierarchy is not blindly normalized without evidence/approval.

### NEXT

Slice 3.2.

---

## Slice 3.2 - Implement OS workspace migration, reference repair and legacy retirement

**Status:** NOT STARTED  
**Dependencies:** 3.1  
**Adaptive tasks:** derive from proven OS reference graph

Provide admitted owner-controlled migration from the old fixture to the accepted target structure.

### Acceptance criteria

- migration is idempotent;
- files/content are preserved;
- stable workspace identity survives the move;
- OS-owned references are repaired or proven unaffected;
- old writable structure retires only after verification;
- ambiguous/custom layouts fail safely or require review.

### NEXT

Slice 3.3.

---

## Slice 3.3 - Implement Skills scope and generation semantics

**Status:** NOT STARTED  
**Dependencies:** 2.3  
**Adaptive tasks:** derive from actual Skills implementation

Define/implement evidence-backed reusable Skill scopes. The expected conceptual model is:

```text
OS-wide
Domain/shared
Workspace-local
```

Exact names/storage must follow current Skills architecture rather than this plan guessing file layout.

### Acceptance criteria

- Skills owns scope semantics;
- scope is represented canonically rather than inferred only from directory location;
- new reusable Skills are not forced into one project's private location when wider scope is clearly canonical;
- provenance/history survives scope changes.

### NEXT

Slice 3.4.

---

## Slice 3.4 - Implement Skills promotion/migration and reference repair

**Status:** NOT STARTED  
**Dependencies:** 3.3  
**Adaptive tasks:** derive from actual Skills references/consumers

Mandatory fixture: a reusable YouTube transcript/book Skill initially created inside one channel/project and already consumed from another project.

### Acceptance criteria

- migration/promotion is owner-controlled and idempotent;
- Skill identity/provenance/history survives;
- consumers/references continue resolving;
- duplicate canonical Skill copies are not created;
- ambiguous user-created/local-only Skills are not silently promoted.

### NEXT

Phase 4 / Slice 4.1.

---

# Phase 4 - Implement Distribution orchestration and simple member UX

**Phase size:** 4 slices

## Slice 4.1 - Implement one rotating Last-Known-Good snapshot and restore engine

**Status:** NOT STARTED  
**Dependencies:** 2.3  
**Adaptive tasks:** extend existing recovery/checkpoint machinery where possible

Implement the bounded recovery guarantee.

### Acceptance criteria

- before every mutating update/upgrade apply, a valid recovery point exists;
- candidate snapshot is verified before replacing the previous recovery point;
- unhealthy/ambiguous current installation cannot destroy the sole known-good recovery point;
- only one retained recovery point remains after successful rotation;
- recovery material is immutable/non-canonical during normal operation;
- `aiverse restore` restores and verifies the declared local scope;
- external/non-restorable effects are reported truthfully.

### NEXT

Slice 4.2.

---

## Slice 4.2 - Separate update staging/activation from structural upgrade

**Status:** NOT STARTED  
**Dependencies:** 4.1, 2.2  
**Adaptive tasks:** derive from current Distribution activation flow

### Acceptance criteria

- normal update does not perform optional infrastructure rearrangement;
- target software incompatible with current infrastructure is not falsely activated;
- required upgrade state is visible and actionable;
- release/update transaction remains truthful after interruption.

### NEXT

Slice 4.3.

---

## Slice 4.3 - Implement doctor and upgrade-plan aggregation with traffic-light UX

**Status:** NOT STARTED  
**Dependencies:** 3.2, 3.4, 4.2  
**Adaptive tasks:** derive from owner doctor/recipe surfaces

Aggregate owner findings without duplicating owner logic.

Default experience should resemble:

```text
AI-Verse Upgrade Check

Safe improvements: 6
Needs review: 1
Blocked: 0

Risk: LOW
User files deleted: NO

Run: aiverse upgrade --apply
Details: aiverse upgrade --details
```

### Acceptance criteria

- default summary is concise;
- full evidence is available on demand and machine-readable;
- doctor/upgrade preview mutate nothing;
- review-required/blocked cases are impossible to misread as safe automatic work.

### NEXT

Slice 4.4.

---

## Slice 4.4 - Implement `upgrade --apply` orchestration, resume and verification

**Status:** NOT STARTED  
**Dependencies:** 4.3  
**Adaptive tasks:** derive from real owner handlers and Distribution transaction engine

### Acceptance criteria

- exact upgrade plan is revalidated against source state immediately before apply;
- Last-Known-Good point is secured first;
- owner handlers execute in dependency-safe order;
- partial failure remains resumable/recoverable/truthful;
- reference repairs and postconditions are verified;
- failed upgrade never reports success;
- restore remains available after the upgrade.

### NEXT

Phase 5 / Slice 5.1.

---

# Phase 5 - Prove safety, convergence, restore and closeout

**Phase size:** 3 slices

## Slice 5.1 - Add cross-repo regression and destructive-negative tests

**Status:** NOT STARTED  
**Dependencies:** 4.4  
**Adaptive tasks:** derive from implemented invariants

Test at minimum:

- doctor/preview commands are read-only;
- unsupported migration blocks safely;
- source drift invalidates stale plan;
- migration applied twice is safe;
- skip-version migration/chain behavior;
- path move preserves stable identity;
- references remain valid;
- user custom files survive;
- sole valid recovery point cannot be lost during failed rotation;
- injected mid-upgrade failure remains recoverable;
- external side effects are not falsely claimed as restored.

### Acceptance criteria

- all permanent laws have executable proof or explicit canonical evidence owner;
- negative tests prove blocked operations leave protected state unchanged.

### NEXT

Slice 5.2.

---

## Slice 5.2 - Run real old-install -> current-architecture convergence and restore qualification

**Status:** NOT STARTED  
**Dependencies:** 5.1  
**Adaptive tasks:** derive from real historical/current fixtures

Run representative end-to-end cases including:

### Workspace fixture

Old scattered channel workspace structure -> doctor -> upgrade plan -> apply -> category/domain-first structure -> reference verification.

### Skills fixture

Project-local reusable YouTube Skill -> doctor -> promotion recommendation -> apply -> shared/domain scope -> consumer verification.

### Restore fixture

Capture pre-action Last-Known-Good -> perform software update + infrastructure upgrade -> create additional realistic changes only where test design allows -> restore -> verify covered local state exactly matches the retained recovery point.

### Fresh-versus-upgraded convergence fixture

Compare a fresh current install with a historical install upgraded to current. Current package-owned/generated/migratable infrastructure must satisfy the same target contracts while historical user state remains preserved.

### Acceptance criteria

- motivating real-world problems are fixed for both future creation and existing installations;
- convergence invariant passes;
- restore invariant passes;
- member UX remains concise.

### NEXT

Slice 5.3.

---

## Slice 5.3 - Canonical closeout and handoff

**Status:** NOT STARTED  
**Dependencies:** 5.2  
**Adaptive tasks:** derive only from real remaining closeout debt

Update canonical System truth, owner docs, Distribution lifecycle docs, changelog/readiness and any repository-network state required by the active governance program.

### Acceptance criteria

- all 18 slices COMPLETE with exact evidence;
- no duplicate update/migration/backup owner exists;
- update remains clean and non-invasive;
- existing installations can converge safely when explicitly requested;
- one rotating Last-Known-Good recovery point is operational;
- restore is truthful and tested;
- OS workspace and Skills scope fixtures pass;
- user-owned data/state protection remains satisfied;
- program becomes COMPLETE only now.

### NEXT

None. Program complete.

---

# Program Change Log

## 2026-10-12 - Program created

- Created canonical adaptive implementation plan for safe infrastructure convergence and recovery.
- Separated software update from optional structural upgrade.
- Added read-only `doctor` and upgrade preview semantics.
- Added owner-published machine-readable upgrade recipes and infrastructure generations.
- Added stable-ID/reference-repair/idempotency/legacy-retirement requirements.
- Added one rotating Last-Known-Good recovery point before every mutating update/upgrade apply.
- Added atomic recovery-point rotation so the sole usable recovery point cannot be destroyed before a verified successor exists.
- Added truthful whole-local-install `restore` semantics with explicit external exclusions.
- Added concrete OS workspace and Skills scope problems as mandatory qualification fixtures.
- Identified the existing Safe Update contract backup policy as an intentional contract amendment required before implementation.
- Limited initial implementation repos to System, Distribution, OS and Skills; future components adopt the framework only when a real migration need exists.

---

# Current execution pointer

**Completed:** 1/18  
**Overall:** 5.6%  
**Phase:** Phase 1 - Audit current update, infrastructure and recovery reality  
**Phase progress:** 0/3  
**Until Phase 2:** 3 slices  
**Next:** Slice 1.1 - Audit existing update, doctor, migration, workspace, Skills and recovery mechanisms  
**Next task:** not yet derived; generate from live Slice 1.1 evidence at slice start  
**Blockers/drift/amendments:** canonical Safe Update backup law requires explicit amendment in Phase 2; this is expected program work, not an implementation blocker for Phase 1 audit.