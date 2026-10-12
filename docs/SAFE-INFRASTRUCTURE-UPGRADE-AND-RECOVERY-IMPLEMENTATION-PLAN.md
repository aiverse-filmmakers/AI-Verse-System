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

Make AI-Verse improve existing installations safely over time, not only fresh installs.

A member who has used AI-Verse for months or years must be able to:

- receive newer admitted AI-Verse software without reinstalling;
- ask AI-Verse in normal English whether everything is healthy;
- discover whether their existing local structure can be safely improved;
- preview any structural modernization before it happens;
- explicitly apply approved structural changes;
- restore the covered local installation to the retained previous known-good point when they intentionally choose to do so.

The member is not expected to understand repositories, release IDs, Git SHAs, infrastructure generations, schema versions, workspace IDs, migration chains, component owners, internal paths, fingerprints, recovery internals or reference graphs.

Those mechanisms may exist internally and in detailed/machine-readable evidence. They are not the normal user interface.

## 0.1 Canonical member experience

### Spoken / agent experience

A member should be able to say things such as:

```text
Update AI-Verse.
Check AI-Verse.
Is everything healthy?
Can AI-Verse improve my setup?
Upgrade AI-Verse.
What would restore change?
Restore AI-Verse.
```

The agent/runtime must map clear intent to the canonical lifecycle command rather than asking the member for internal implementation details.

### Terminal experience

```text
aiverse update
    apply the newest admitted software update safely
    create/refresh the verified Last-Known-Good point first when mutation is required
    do not perform optional structural modernization

aiverse update --plan
    read-only preview of the software update

aiverse doctor
    one read-only whole-system health/infrastructure check
    internally run the relevant owner checks in a controlled sequence
    return one concise combined answer

aiverse upgrade
    read-only preview of recommended or required structural improvements

aiverse upgrade --apply
    create/refresh the verified Last-Known-Good point first
    apply only admitted owner-controlled structural migrations
    repair declared references
    verify the result

aiverse restore
    read-only preview of the retained recovery point and what covered local state would be replaced

aiverse restore --apply
    explicitly restore the retained Last-Known-Good local recovery point
    verify the restored result
```

The completed Core Update Program v1 already established that plain `aiverse update` performs the safe admitted software update and `aiverse update --plan` is the preview. This program must preserve that shipped behavior rather than reintroducing `update --apply`.

The default UI must remain short, plain-English and small-screen friendly. Detailed evidence exists on demand.

---

# 1. Permanent laws

These are protected program outcomes. Adaptive discovery may not weaken them automatically.

## 1.1 User-owned state is never guessed away

Nothing user-owned may be deleted, reset, overwritten, silently relocated, silently re-scoped or discarded merely because a newer architecture exists.

Unknown/custom files remain user-owned unless canonical ownership can be proved.

## 1.2 Update and infrastructure convergence are separate concepts

`update` is software/release delivery.

`upgrade` is infrastructure convergence: bringing an existing installation's owned/migratable structure toward the architecture expected by the admitted target release.

Optional structural modernization must never be hidden inside a normal software update.

If target software cannot safely activate against the current infrastructure, it may be staged only if staging itself is safe, but activation must remain blocked until the required admitted migration succeeds.

## 1.3 Shipped update semantics are preserved; previews stay read-only

The canonical command semantics are:

- `aiverse update` may mutate by applying the newest admitted safe software update;
- `aiverse update --plan` is read-only;
- `aiverse doctor` is read-only;
- `aiverse upgrade` is read-only;
- `aiverse upgrade --apply` may mutate through admitted owner migrations;
- `aiverse restore` is read-only preview;
- `aiverse restore --apply` may mutate by restoring the retained recovery point.

No implementation slice may silently reverse these meanings.

## 1.4 Member language is plain English; internal architecture stays internal

Default member-facing output must describe outcomes and choices in language a non-technical member can understand.

Do not require or normally expose terms such as infrastructure generation, schema generation, workspace ID, migration recipe ID, release SHA, source fingerprint, reference graph, owner lifecycle or filesystem migration path.

Technical identifiers remain available in details/JSON/evidence for debugging, qualification and support.

A good default explanation is:

```text
AI-Verse is healthy.
2 safe improvements are available.
1 change needs your review.
Nothing will be deleted.
```

not:

```text
workspace generation 2 -> 3
recipe os.workspace.move.v3
source fingerprint ...
```

## 1.5 One doctor command, many owner checks internally

The member runs or asks for one health check: `aiverse doctor` / "Check AI-Verse."

Distribution may invoke OS, Skills and future owner-specific doctor/check surfaces internally, one by one in a bounded dependency-safe sequence, then aggregate the results.

The user must not need to run `doctor os`, `doctor skills`, `doctor data`, or learn which component owns a problem.

Distribution must aggregate owner findings; it must not duplicate owner domain logic.

One owner check failing must be surfaced truthfully without causing the remaining safe read-only checks to be silently skipped unless a dependency makes continuing invalid.

## 1.6 Canonical owners define migrations

OS owns OS/workspace structure semantics and migrations.

Skills owns Skills state/layout/scope semantics and migrations.

Future components own their own migrations.

Distribution discovers, plans, coordinates, checkpoints, invokes, verifies and records migrations. It must not invent sibling domain migration semantics.

## 1.7 Machine-readable upgrade recipes, never AI guesswork

Structural change must be driven by versioned, owner-published migration/upgrade metadata and executable owner handlers.

AI reasoning may help explain, classify or propose, but `upgrade --apply` must not reorganize infrastructure merely because an agent thinks a newer arrangement looks better.

The agent must not substitute ad-hoc `mv`, copy/delete, Git operations or hand-written migration steps for an admitted owner recipe.

## 1.8 Explicit internal generations, hidden from normal users

Movable/migratable structural domains must expose enough generation/schema identity internally for the system to determine source state, target state and admitted migration path without guessing from filenames alone.

Skip-version behavior must be explicit: direct migration or a validated migration chain.

These generations are machine control data, not concepts the member must understand.

## 1.9 Stable identity over filesystem path

Any first-class entity that may move during a legitimate upgrade should use stable identity independent of its current path where technically applicable.

Moving a workspace or Skill must not silently create a new logical entity or orphan references merely because its path changed.

Apply this principle to any future first-class movable entity only when evidence shows path-independent identity is needed; do not create ceremonial IDs everywhere.

## 1.10 Migrations are idempotent and evidence-bound

A migration applied twice must not duplicate content, repeat destructive moves or corrupt state.

Upgrade plans must be bound to source generation/state fingerprints and exact target release evidence. Source drift before apply forces re-plan or safe refusal.

## 1.11 Reference repair is part of migration

A move is incomplete until affected references, indexes, manifests, automations, links and owner-declared dependants are either repaired or explicitly proven unaffected.

## 1.12 Upgrade findings have an explicit disposition

Every structural finding must resolve internally to one of these outcomes:

- `OPTIONAL`: current installation remains supported; improvement is recommended but not required;
- `REQUIRED`: admitted target software cannot safely activate or remain supported without the migration;
- `BLOCKED/REVIEW`: safe automatic migration cannot currently be proved.

The member-facing wording must stay simple. For example:

```text
Optional: 2 safe improvements are available.
Required: AI-Verse needs one setup upgrade before the new version can finish.
Review: One custom item needs your decision before AI-Verse changes it.
```

A normal `update` must never silently apply an OPTIONAL structural upgrade.

## 1.13 Legacy infrastructure retires only after proof

Old writable structures/routes may be retired only after the new structure verifies successfully and no supported dependency still requires the old path.

Compatibility clutter must not accumulate forever, but cleanup must never precede proof.

## 1.14 One rotating Last-Known-Good recovery point

Before every mutating `aiverse update` or `aiverse upgrade --apply`, AI-Verse must have one verified recoverable pre-action Last-Known-Good point representing the covered local installation immediately before that action.

Only one retained Last-Known-Good recovery point is required by this program.

The sole usable recovery point must never be destroyed before a valid successor exists.

A new candidate recovery point must be staged and verified before it replaces the previous one. If the current installation is too unhealthy or ambiguous to become a trustworthy recovery point, preserve the existing known-good point and fail safely rather than rotating it away.

## 1.15 Recovery means a complete recoverable representation, not necessarily a blind folder copy

The recovery system must truthfully classify local state into at least these conceptual categories:

- state/files that must be captured because they are canonical or user-created;
- exact software/release state that may be reconstructed from immutable verified references/receipts;
- derived/disposable state that may be safely rebuilt and therefore need not consume recovery storage;
- external or security-sensitive state that is outside restore scope unless a safe explicit mechanism exists.

A recovery point may use snapshots, archives, copy-on-write, deduplicated storage, immutable refs or other proven techniques. The implementation must be chosen from Phase 1 evidence.

The product promise is recoverability of the declared local scope, not an unnecessarily huge duplicate of caches, dependency folders, render outputs or other reconstructible/disposable material.

Secrets/credentials must not be copied into recovery material merely for completeness unless the approved recovery design explicitly proves secure handling and restore semantics.

## 1.16 Restore is preview-first, explicit and transactional

`aiverse restore` must not immediately replace current state. It is a read-only preview that tells the member, in plain English:

- when the retained recovery point was created;
- what broad local categories are covered;
- what is not covered;
- whether newer covered local changes would be replaced;
- whether restore is currently safe to apply.

Actual restore requires explicit `aiverse restore --apply` or an equivalent unambiguous conversational confirmation.

`restore --apply` must restore the covered local AI-Verse installation/project state to the retained Last-Known-Good point, including the exact admitted software/release selection and covered state needed to reproduce that local point.

The restore transaction must protect against a partial failed restore. It may use a temporary transaction checkpoint of the current state, but that temporary checkpoint must not replace or destroy the retained Last-Known-Good target before restore succeeds.

The restore contract must explicitly define exclusions such as external services, remote side effects, external credential stores and disposable caches. It must never claim to rewind things it cannot actually rewind.

## 1.17 Recovery material is not a second canonical live store

The retained recovery point and any temporary restore checkpoint are recovery material, not writable canonical Memory/Data/Skills/OS sources.

Normal runtime must never read/write them as live state.

## 1.18 All supported agent runtimes converge on the same lifecycle

Claude Code, Codex-compatible agents, Gateway-hosted agents and other supported runtimes must map natural-language lifecycle requests to the same canonical commands and contracts.

Runtime-specific adapter files may point into the canonical contract, but must not invent different update/doctor/upgrade/restore semantics.

Normal conversational intent should route approximately as follows:

```text
"Update AI-Verse"          -> aiverse update
"Check AI-Verse"           -> aiverse doctor
"Can this setup improve?"  -> aiverse upgrade
"Upgrade AI-Verse"         -> preview/confirm the structural upgrade, then apply only with explicit intent
"What would restore do?"   -> aiverse restore
"Restore AI-Verse"         -> show restore impact and obtain explicit apply confirmation before mutation
```

## 1.19 Simple UX, deep evidence on demand

Default member-facing output should fit on a small screen and communicate decisions, not internals.

A doctor/upgrade summary should resemble:

```text
AI-Verse Check

Healthy: YES
Safe improvements: 2
Needs your review: 1
Blocked: 0
Risk: LOW
Nothing will be deleted.

Recommended: Upgrade AI-Verse
```

A restore preview should resemble:

```text
AI-Verse Restore

Recovery point: Today, 14:20
Ready to restore: YES
Your AI-Verse files covered: YES
External services covered: NO
Newer covered local changes would be replaced: YES

Nothing has changed yet.
To continue: Restore AI-Verse
```

Exact wording may evolve through usability testing, but default output must not require technical knowledge.

Full migration detail, evidence and provenance remain available through an explicit details mode or machine-readable output.

## 1.20 No concurrent-plan overwrite

This program may coexist with the active repository-network governance program and future active programs, but implementation must refetch current files/refs before every write and must not overwrite overlapping work from another active plan.

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
- non-invasive plain-English member UX expectations;
- natural-language lifecycle intent semantics across runtimes;
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

Possible target style:
workspaces/YouTube/<ChannelName>/...
```

The exact target structure must be validated from current OS architecture during Phase 1 rather than assumed solely from this example.

The member-facing product must not require the user to understand or choose these filesystem structures. The OS decides canonical structure from real-world meaning and owner rules; ambiguous/custom cases require natural-language clarification rather than architecture questions.

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

The member should never be asked to choose an internal Skills storage directory. When real-world scope is ambiguous, ask what the Skill is for and where it should be usable in normal language; Skills converts that meaning into canonical scope.

## ai-verse-distribution

Owns orchestration and member-facing lifecycle:

- current/target release awareness;
- gathering owner upgrade recipes;
- one-command doctor aggregation across owner checks;
- read-only upgrade/restore preview aggregation;
- one rotating Last-Known-Good recovery point;
- update/upgrade/restore transaction state;
- invoking owner migrations;
- whole-install verification;
- activation gating;
- restore orchestration;
- short plain-English traffic-light UX and detailed/machine-readable views.

Distribution must not decide workspace hierarchy, Skill scope rules or other owner-domain semantics itself.

## Future component repos

No future component is modified merely because this framework exists.

A component adopts the recipe/generation/doctor model only when it has a real structural/state migration or health responsibility. The framework must be extensible without forcing ceremonial migration code into every repository.

---

# 3. Existing canonical law and shipped behavior that must be reconciled deliberately

Two existing truths must be preserved rather than accidentally overwritten by this program.

## 3.1 Safe Update recovery ownership law

`docs/SAFE-UPDATE-AND-STATE-PRESERVATION-CONTRACT.md` currently states that Distribution should not duplicate every canonical store merely to claim update safety and should rely on owner-backed recovery guarantees.

This program intentionally introduces a bounded additional product guarantee: one rotating whole-local-installation Last-Known-Good recovery point before every mutating software update or structural upgrade.

Implementation must explicitly reconcile the laws so that:

- owner-native checkpoints remain authoritative for component-internal transactional safety;
- the single Distribution-orchestrated Last-Known-Good recovery point exists for whole-install/user recovery;
- the recovery point may reconstruct exact software from immutable refs rather than blindly duplicating reconstructible software trees when proven safe;
- the recovery snapshot remains immutable/non-canonical;
- only one retained recovery point is required;
- rotation cannot destroy the sole valid recovery point prematurely;
- restore scope/exclusions are truthful;
- restore itself cannot destroy its target recovery point before success.

## 3.2 Completed Core Update Program v1 behavior

The completed Core Update Program v1 in `aiverse-filmmakers/ai-verse-distribution/docs/CORE-UPDATE-PROGRAM.md` established and qualified:

```text
aiverse update
    apply newest admitted safe Core update

aiverse update --plan
    preview only
```

It also established natural-language update routing through the runtime contract.

This program must EXTEND that lifecycle, not regress it. In particular:

- do not change plain `aiverse update` back into a preview;
- do not require ordinary members to learn `update --apply`;
- preserve its fail-closed ownership/local-edit behavior;
- preserve status + doctor as mandatory update health gates;
- extend recovery/convergence around it rather than creating a second updater.

Phase 1 must audit the live implementation before any changes, and Phase 2 must make the combined contract explicit.

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

## Slice 0.1 - Create and refine the canonical implementation program

**Status:** COMPLETE  
**Repos:** AI-Verse-System  
**Dependencies:** none

### Acceptance criteria

- adaptive implementation plan exists in the canonical System repo;
- user-facing update/doctor/upgrade/restore model is explicit and consistent with shipped Core Update v1 behavior;
- one rotating Last-Known-Good recovery guarantee is explicit;
- restore is preview-first and explicit before mutation;
- one-command doctor aggregation is explicit;
- default member UX is plain English and hides internal architecture jargon;
- OPTIONAL / REQUIRED / BLOCKED structural findings are explicit internally and understandable externally;
- conflict with current Safe Update backup law is identified rather than ignored;
- OS, Skills, Distribution and System ownership is explicit;
- workspace and Skill problems are represented as mandatory real-world fixtures;
- low-level tasks remain adaptive;
- future agents can resume without this conversation.

### Evidence

- canonical plan: `docs/SAFE-INFRASTRUCTURE-UPGRADE-AND-RECOVERY-IMPLEMENTATION-PLAN.md`
- planning method: `docs/ADAPTIVE-IMPLEMENTATION-PLANNING-SKILL.md`
- shipped update behavior: `aiverse-filmmakers/ai-verse-distribution/docs/CORE-UPDATE-PROGRAM.md`

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

- completed Core Update Program v1 behavior and exact current `aiverse update` / `--plan` semantics;
- current Distribution update/status/doctor/rollback/recovery/journal/checkpoint behavior;
- current natural-language update routing across `AGENTS.md`, `CLAUDE.md` and other supported runtime adapters;
- current release-set staging/activation semantics;
- existing package manifests and owned-path tracking;
- current checkpoint/backup/recovery mechanisms and what they actually cover;
- current OS workspace identity, layout, creation logic and references;
- current Skills storage, identity, generations, provenance and local/global scoping;
- existing migration schemas/handlers in OS and Skills;
- existing owner health/doctor/check surfaces that Distribution can aggregate instead of duplicating;
- existing generated/member-facing files affected by moves;
- existing tests for path moves, user-file preservation and recovery;
- active overlapping work from the repository-network governance plan or other plans.

### Acceptance criteria

- exact current behavior is evidenced before new implementation is proposed;
- existing reusable mechanisms are identified;
- the shipped safe updater is classified for REUSE/EXTEND rather than duplicated;
- workspace and Skills motivating problems are reproduced/classified from real implementation;
- current restore capability and gaps are known;
- existing owner doctor/check surfaces and gaps are known;
- no implementation change occurs before the audit is recorded.

### NEXT

Slice 1.2.

---

## Slice 1.2 - Build ownership, identity, reference, migration, health and recovery inventory

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
- owner doctor/check entrypoints and how a single Distribution doctor can call them sequentially;
- OPTIONAL / REQUIRED / BLOCKED finding semantics;
- user-owned versus package-owned/generated boundaries;
- recovery-point scope and exclusions;
- which state must be captured versus exactly reconstructible versus disposable versus external;
- snapshot size/performance risks, including large media/render/dependency/cache surfaces;
- credential/secret handling requirements;
- current health signals needed before safe recovery-point rotation;
- temporary transaction checkpoint needs for failed restore recovery;
- legacy writable routes that may need retirement;
- which technical evidence is internal-only versus suitable for default member output.

### Acceptance criteria

- Distribution shadow-domain logic is prohibited/identified;
- path-identity risks are explicit;
- one-command doctor fan-out ownership is explicit;
- exact recovery coverage required for truthful `restore` is known;
- recovery design does not assume a blind copy of all local bytes;
- no duplicate migration/backup/update framework is planned where existing machinery can be extended;
- ordinary user output can remain free of paths/generations/IDs without losing machine-verifiable evidence.

### NEXT

Slice 1.3.

---

## Slice 1.3 - Freeze implementation architecture and acceptance matrix

**Status:** NOT STARTED  
**Dependencies:** 1.2  
**Adaptive tasks:** derive from evidence-backed inventory

Freeze evidence-backed decisions for:

- shipped `update` versus structural `upgrade` activation semantics;
- `update --plan`, doctor, upgrade preview and restore preview read-only contracts;
- natural-language lifecycle routing for Claude/Codex/Gateway-compatible runtimes;
- single-command doctor owner fan-out and aggregation order/failure behavior;
- OPTIONAL / REQUIRED / BLOCKED convergence disposition;
- upgrade-recipe schema/home;
- generation/state-fingerprint semantics;
- stable identity requirements;
- reference-repair ownership;
- Last-Known-Good location/scope/exclusions;
- capture versus reconstruct versus rebuild versus external recovery classes;
- credential/secret recovery policy;
- atomic snapshot rotation policy;
- restore preview, explicit apply and failed-restore transaction semantics;
- health gate before snapshot replacement;
- plain-English small-screen UX;
- technical details/machine-readable output;
- test matrix for current->target convergence and restore.

### Acceptance criteria

- every new mechanism has one canonical owner;
- no unresolved source-of-truth duplication remains;
- shipped Core Update v1 command behavior is preserved;
- snapshot/restore promise is technically truthful and storage-bounded by evidence;
- one-command doctor does not become a shadow implementation of owner logic;
- normal member experience requires no architecture knowledge;
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

- normal one-action software update;
- software update preview;
- structural/infrastructure upgrade preview/apply;
- software rollback/recovery internal to failed transactions;
- whole-local-install restore preview/apply.

### Acceptance criteria

- no contradiction remains between canonical law and intended implementation;
- `aiverse update` remains the shipped one-action safe updater and `--plan` remains its preview;
- owner-native checkpoints remain authoritative for component transaction safety;
- one rotating whole-install recovery point is canonical and bounded;
- recoverability may use exact reconstruction for proven reconstructible state;
- restore is preview-first and explicit before mutation;
- restore does not falsely claim reversal of external systems;
- restore transaction failure cannot destroy the retained recovery target;
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
- applicability/disposition (`OPTIONAL` / `REQUIRED` / blocked when no safe recipe applies);
- detection/preconditions;
- migration handler/entrypoint;
- reference-repair obligations;
- postconditions;
- risk/recovery requirements;
- idempotency declaration/proof;
- skip-version/direct-versus-chain behavior;
- legacy retirement conditions;
- concise plain-English member summary text;
- technical detail/evidence fields kept out of normal member output.

Do not create a parallel release metadata system if the existing component release descriptor can safely own these fields through versioned extension.

### Acceptance criteria

- `upgrade --apply` never depends on free-form AI inference to know what structural mutation to execute;
- exact owner and exact migration path are machine-resolvable;
- OPTIONAL versus REQUIRED behavior is machine-resolvable;
- unsupported/unknown path fails closed or becomes REVIEW/BLOCKED;
- recipe internals are not required knowledge for the member.

### NEXT

Slice 2.3.

---

## Slice 2.3 - Define convergence, restore, doctor and member UX invariants

**Status:** NOT STARTED  
**Dependencies:** 2.2

Define permanent acceptance invariants, including:

### Convergence invariant

After a successful admitted upgrade, package-owned/generated/migratable infrastructure should conform to the target release's current architecture while legitimate user state/history remains preserved.

### Restore invariant

After a successful `aiverse restore --apply`, all locally covered state must match or reproduce the retained Last-Known-Good recovery point exactly according to the declared restore scope and verification method. Reconstructed software must resolve to the exact retained admitted release/revisions.

### Doctor invariant

One `aiverse doctor` command must aggregate the relevant owner health/infrastructure checks without duplicating their domain logic and without requiring the member to know component boundaries.

### UX invariant

Default output remains plain-English and small-screen friendly; technical details/evidence are opt-in.

### Acceptance criteria

- fresh-install versus upgraded-install structural equivalence is testable at the target contract level;
- restore exactness/reproducibility is testable;
- doctor fan-out and aggregation are testable;
- user-facing simplicity does not remove machine-readable evidence;
- member output does not require paths, generations, IDs or migration jargon.

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

This structure is an internal owner concern. User interaction should remain based on real-world meaning such as "my YouTube channel" or "the Nike client project," not filesystem hierarchy selection.

### Acceptance criteria

- OS owns the rule, not Distribution;
- movable workspaces have stable identity where needed;
- new workspace creation no longer reproduces the proven bad hierarchy case;
- user custom hierarchy is not blindly normalized without evidence/approval;
- ambiguous cases ask natural real-world questions rather than internal architecture questions.

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
- ambiguous/custom layouts fail safely or require natural-language review;
- default user output explains the practical effect without exposing source/target filesystem paths unless details are requested.

### NEXT

Slice 3.3.

---

## Slice 3.3 - Implement Skills scope and generation semantics

**Status:** NOT STARTED  
**Dependencies:** 2.3  
**Adaptive tasks:** derive from actual Skills implementation

Define/implement evidence-backed reusable Skill scopes. An internal conceptual model may include scopes such as:

```text
OS-wide
Domain/shared
Workspace-local
```

Exact names/storage must follow current Skills architecture rather than this plan guessing file layout.

The member should deal in practical meaning: "use this everywhere," "use this for all YouTube work," or "only use this in this project." AI-Verse maps that meaning to canonical Skills scope.

### Acceptance criteria

- Skills owns scope semantics;
- scope is represented canonically rather than inferred only from directory location;
- new reusable Skills are not forced into one project's private location when wider scope is clearly canonical;
- provenance/history survives scope changes;
- the member is not required to choose storage folders or internal scope identifiers.

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
- ambiguous user-created/local-only Skills are not silently promoted;
- review questions are framed in practical user language, not repository/path terminology.

### NEXT

Phase 4 / Slice 4.1.

---

# Phase 4 - Implement Distribution orchestration and simple member UX

**Phase size:** 4 slices

## Slice 4.1 - Implement one rotating Last-Known-Good recovery point and restore engine

**Status:** NOT STARTED  
**Dependencies:** 2.3  
**Adaptive tasks:** extend existing recovery/checkpoint machinery where possible

Implement the bounded recovery guarantee without assuming that recoverability requires copying every local byte.

### Acceptance criteria

- before every mutating `aiverse update` or `aiverse upgrade --apply`, a valid recovery point exists;
- candidate recovery point is verified before replacing the previous recovery point;
- unhealthy/ambiguous current installation cannot destroy the sole known-good recovery point;
- only one retained Last-Known-Good point remains after successful rotation;
- canonical/user state required for recovery is captured or otherwise durably represented;
- exact software may be reconstructed from verified immutable refs/receipts when Phase 1 proves that safe;
- disposable/rebuildable caches, indexes and dependency trees are not copied merely to make the snapshot look complete;
- large media/render/output surfaces have an explicit evidence-backed coverage policy rather than accidental inclusion;
- secrets/credentials follow an explicit safe coverage policy;
- recovery material is immutable/non-canonical during normal operation;
- `aiverse restore` is preview-only and mutates nothing;
- restore preview says what is covered, excluded and at risk of being replaced in plain English;
- `aiverse restore --apply` restores and verifies the declared local scope;
- failed restore has a transaction-safe recovery path without destroying the retained Last-Known-Good target;
- external/non-restorable effects are reported truthfully.

### NEXT

Slice 4.2.

---

## Slice 4.2 - Extend shipped update staging/activation around structural upgrade requirements

**Status:** NOT STARTED  
**Dependencies:** 4.1, 2.2  
**Adaptive tasks:** derive from the current qualified Distribution update flow

The completed Core Update Program v1 updater is the base. Extend it; do not replace it.

### Acceptance criteria

- `aiverse update` remains the one-action admitted software update;
- `aiverse update --plan` remains read-only preview;
- normal update does not perform OPTIONAL infrastructure rearrangement;
- target software incompatible with current infrastructure is not falsely activated;
- REQUIRED upgrade state is visible and actionable in plain English;
- BLOCKED/REVIEW state cannot be misrepresented as safe automatic work;
- update may safely stage only when staging is evidence-backed and activation truth remains explicit;
- release/update transaction remains truthful after interruption;
- the member is never asked for release IDs, repository paths, migration recipe IDs or infrastructure generations.

### NEXT

Slice 4.3.

---

## Slice 4.3 - Implement one-command doctor and upgrade-plan aggregation with plain-English traffic-light UX

**Status:** NOT STARTED  
**Dependencies:** 3.2, 3.4, 4.2  
**Adaptive tasks:** derive from owner doctor/recipe surfaces

`aiverse doctor` is one member command. Distribution invokes the relevant owner checks internally in a controlled sequence and aggregates them without duplicating owner logic.

`aiverse upgrade` consumes the owner findings/recipes and produces the structural convergence preview.

Default experience should resemble:

```text
AI-Verse Check

Healthy: YES
Safe improvements: 2
Needs your review: 1
Blocked: 0
Risk: LOW
Nothing will be deleted.

Recommended: Upgrade AI-Verse
```

When an upgrade is required for activation, wording should resemble:

```text
AI-Verse found one setup change that must be completed before the new version can finish.
Nothing has been changed yet.

Recommended: Upgrade AI-Verse
```

### Acceptance criteria

- one `aiverse doctor` command checks the whole supported installation from the member's perspective;
- owner checks execute internally with isolated evidence/results;
- one owner check failure is surfaced accurately and does not become a false whole-system PASS;
- the member never needs component-specific doctor commands;
- default summary is concise and plain English;
- full technical evidence is available on demand and machine-readable;
- doctor/upgrade preview mutate nothing;
- OPTIONAL / REQUIRED / REVIEW/BLOCKED cases are impossible to misread;
- default output does not expose internal paths/generations/IDs unless required to explain a conflict and no friendlier identifier exists.

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
- restore remains available after the upgrade;
- OPTIONAL upgrades require explicit apply intent;
- REQUIRED upgrades remain explicit rather than being hidden inside normal update;
- member completion output explains what practically improved, what was preserved and whether health passed without requiring technical migration knowledge.

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

- `aiverse update` retains shipped apply semantics;
- `aiverse update --plan`, doctor, upgrade preview and restore preview are read-only;
- one-command doctor fan-out invokes owner checks without duplicating owner logic;
- owner doctor failure cannot become false aggregate PASS;
- OPTIONAL migration is not hidden inside update;
- REQUIRED migration blocks unsafe activation and gives one clear next action;
- BLOCKED/REVIEW findings preserve protected state;
- unsupported migration blocks safely;
- source drift invalidates stale plan;
- migration applied twice is safe;
- skip-version migration/chain behavior;
- path move preserves stable identity;
- references remain valid;
- user custom files survive;
- sole valid recovery point cannot be lost during failed rotation;
- recovery can reproduce covered state without requiring blind cache/dependency duplication;
- restore preview does not mutate;
- restore apply replaces exactly the declared covered scope;
- failed restore does not destroy the retained restore target;
- injected mid-upgrade failure remains recoverable;
- secrets/credential exclusions or secure coverage behave exactly as declared;
- external side effects are not falsely claimed as restored;
- Claude/Codex/Gateway-compatible runtime adapters converge on the same lifecycle commands;
- default member output remains understandable without paths, generations, IDs or migration terminology.

### Acceptance criteria

- all permanent laws have executable proof or explicit canonical evidence owner;
- negative tests prove blocked operations leave protected state unchanged;
- user-flow tests prove one normal-language request/one command is sufficient for update, doctor, upgrade preview and restore preview.

### NEXT

Slice 5.2.

---

## Slice 5.2 - Run real old-install -> current-architecture convergence and restore qualification

**Status:** NOT STARTED  
**Dependencies:** 5.1  
**Adaptive tasks:** derive from real historical/current fixtures

Run representative end-to-end cases including:

### Workspace fixture

Old scattered channel workspace structure -> one doctor command -> plain-English upgrade preview -> explicit apply -> accepted current structure -> reference verification.

The member-facing fixture must not require the tester to choose filesystem hierarchy or internal generation numbers.

### Skills fixture

Project-local reusable YouTube Skill -> one doctor command -> practical promotion recommendation -> explicit apply -> shared/domain-appropriate scope -> consumer verification.

The member-facing fixture must reason in terms of where the Skill should be usable, not where its files should live.

### Restore fixture

Retain pre-action Last-Known-Good -> perform software update + infrastructure upgrade -> create additional realistic covered local changes where test design allows -> run restore preview -> verify preview is truthful/read-only -> explicitly apply restore -> verify covered local state exactly matches/reproduces the retained recovery point.

### Fresh-versus-upgraded convergence fixture

Compare a fresh current install with a historical install upgraded to current. Current package-owned/generated/migratable infrastructure must satisfy the same target contracts while historical user state remains preserved.

### Runtime fixture

For supported agent runtimes, natural-language lifecycle requests must resolve to the same canonical update/doctor/upgrade/restore behavior without requiring release IDs, paths or component-specific commands.

### Acceptance criteria

- motivating real-world problems are fixed for both future creation and existing installations;
- convergence invariant passes;
- restore invariant passes;
- doctor aggregation invariant passes;
- runtime convergence passes;
- member UX remains concise, plain-English and non-technical.

### NEXT

Slice 5.3.

---

## Slice 5.3 - Canonical closeout and handoff

**Status:** NOT STARTED  
**Dependencies:** 5.2  
**Adaptive tasks:** derive only from real remaining closeout debt

Update canonical System truth, owner docs, Distribution lifecycle docs, runtime adapters, changelog/readiness and any repository-network state required by the active governance program.

### Acceptance criteria

- all 18 slices COMPLETE with exact evidence;
- no duplicate update/migration/backup/doctor owner exists;
- shipped `aiverse update` remains clean, safe and non-invasive to optional structure;
- one-command doctor is operational without user component knowledge;
- existing installations can converge safely when explicitly requested;
- OPTIONAL / REQUIRED / BLOCKED behavior is deterministic and understandable;
- one rotating Last-Known-Good recovery point is operational;
- restore is preview-first, explicit, truthful and tested;
- recovery scope is storage-conscious and technically reproducible rather than a blind-copy promise;
- OS workspace and Skills scope fixtures pass;
- supported runtime adapters converge on one lifecycle contract;
- user-owned data/state protection remains satisfied;
- default member UX requires no repository/path/generation/migration knowledge;
- program becomes COMPLETE only now.

### NEXT

None. Program complete.

---

# Program Change Log

## 2026-10-12 - Program created

- Created canonical adaptive implementation plan for safe infrastructure convergence and recovery.
- Separated software update from optional structural upgrade.
- Added read-only doctor and upgrade preview semantics.
- Added owner-published machine-readable upgrade recipes and infrastructure generations.
- Added stable-ID/reference-repair/idempotency/legacy-retirement requirements.
- Added one rotating Last-Known-Good recovery point before every mutating update/upgrade operation.
- Added atomic recovery-point rotation so the sole usable recovery point cannot be destroyed before a verified successor exists.
- Added truthful whole-local-install restore semantics with explicit external exclusions.
- Added concrete OS workspace and Skills scope problems as mandatory qualification fixtures.
- Identified the existing Safe Update contract backup policy as an intentional contract amendment required before implementation.
- Limited initial implementation repos to System, Distribution, OS and Skills; future components adopt the framework only when a real migration need exists.

## 2026-10-12 - Owner-approved plan refinement before Phase 1 implementation

- Preserved the already-shipped Core Update Program v1 semantics: `aiverse update` applies the safe admitted update and `aiverse update --plan` previews it. Removed the proposed regression to `update --apply`.
- Made the normal member experience conversational and plain-English; paths, generations, stable IDs, recipe IDs, fingerprints and owner internals are evidence-layer concepts rather than required user knowledge.
- Defined one `aiverse doctor` command that internally invokes owner health checks in a controlled sequence and returns one combined result; members do not run component-specific doctor commands.
- Added deterministic OPTIONAL / REQUIRED / BLOCKED-REVIEW structural finding semantics so optional modernization never hides inside update and required convergence can safely gate activation.
- Made `aiverse restore` preview-only and `aiverse restore --apply` the explicit mutating action.
- Added transactional failed-restore protection without replacing/destroying the retained Last-Known-Good target before restore succeeds.
- Refined the Last-Known-Good guarantee from a naive whole-folder duplicate into a complete recoverable representation: capture canonical/user state, reconstruct exact software from verified immutable references where safe, rebuild disposable state, and state external/security-sensitive exclusions truthfully.
- Added explicit large-media/cache/dependency/credential recovery-scope audit requirements.
- Generalized stable identity to first-class movable entities only where evidence proves path-independent identity is needed.
- Added cross-runtime lifecycle convergence requirements so Claude Code, Codex-compatible, Gateway-hosted and other supported runtimes route the same natural-language lifecycle intent to the same canonical commands.
- Strengthened Phase 5 with user-flow, doctor aggregation, restore preview/apply, runtime convergence and non-technical UX acceptance.

---

# Current execution pointer

**Completed:** 1/18  
**Overall:** 5.6%  
**Phase:** Phase 1 - Audit current update, infrastructure and recovery reality  
**Phase progress:** 0/3  
**Until Phase 2:** 3 slices  
**Next:** Slice 1.1 - Audit existing update, doctor, migration, workspace, Skills and recovery mechanisms  
**Next task:** not yet derived; generate from live Slice 1.1 evidence at slice start  
**Blockers/drift/amendments:** canonical Safe Update backup law requires explicit amendment in Phase 2; shipped Core Update v1 command semantics are now explicitly preserved by this plan.