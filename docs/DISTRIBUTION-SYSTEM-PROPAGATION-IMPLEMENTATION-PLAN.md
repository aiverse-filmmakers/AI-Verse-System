# Distribution -> System Propagation, Canonical Owner Routing, Component Handoff, Repository State Ledger and Member Isolation Implementation Plan

**Status:** ACTIVE  
**Canonical planning repo:** `aiverse-filmmakers/AI-Verse-System`  
**Primary implementation repo:** `aiverse-filmmakers/ai-verse-distribution`  
**Affected implementation repos:** AI-Verse component repositories that are shipped by Distribution  
**Started:** 2026-10-12  
**Program size:** 14 slices  
**Completed:** 1  
**Remaining:** 13  
**Progress:** 7.1%  
**Rule:** Update this file before and after every implementation slice. A slice is COMPLETE only when its acceptance criteria are satisfied and exact implementation/test evidence is recorded here.

## 0. Mission

Make the AI-Verse repository network behave as one controlled, self-checking product without collapsing the repositories into one codebase.

The finished behavior must achieve five goals at once:

1. **System stays current.** Meaningful product, architecture, lifecycle, readiness, compatibility, release, safety and member-experience changes are reflected appropriately in `aiverse-filmmakers/AI-Verse-System`.
2. **Canonical component owners stay current.** Skills, Brain, Memory, Data, OS and every other component remain the canonical implementation home for their own behavior. Distribution must not hide or permanently patch sibling-owned defects.
3. **Distribution ships only accepted component revisions.** A component revision must first satisfy its own owner-repo validation, then Distribution must qualify that exact revision as part of the composed AI-Verse release before it can become an admitted member release.
4. **Cross-repo drift is visible before it can cause regression.** A canonical repository-state ledger must distinguish live repo HEAD, owner-accepted revision, Distribution-shipped revision and System synchronization state. Stale documentation must never silently drive newer accepted implementation backward.
5. **Members receive only product-relevant files.** Maintainer governance, cross-repo synchronization rules, internal roadmaps, qualification records and developer-only instructions remain outside the member-facing installation.

This program does not create blind repository synchronization. It creates explicit ownership, evidence, handoff, freshness and reconciliation rules.

---

## 0A. Repository roles

### AI-Verse-System

Owns the evolving big picture:

- canonical architecture;
- component responsibilities and ownership;
- system-wide lifecycle truth;
- current versus intended behavior;
- readiness and QC truth;
- product intent;
- cross-repo contracts;
- canonical changelog and historical architectural decisions.

System is not the runtime implementation of the component repos and is not the member installer.

### AI-Verse component repositories

Examples include:

- `AI-Verse-OS`
- `AI-Verse-Brain`
- `AI-Verse-Memory`
- `AI-Verse-Skills`
- `AI-Verse-Data`
- Gateway
- Automations
- Multiple Bots
- Connections
- Apps
- Dashboard
- Token
- any future canonical component owner

Each component repo owns its real implementation, native tests, component-specific lifecycle behavior and component-local defects/improvements.

### ai-verse-distribution

Owns product composition and delivery:

- release sets;
- exact immutable component refs;
- compatibility resolution;
- source acquisition;
- installation;
- setup orchestration;
- update;
- rollback;
- Distribution receipts/locks;
- clean-machine qualification;
- whole-product acceptance;
- release admission;
- member delivery boundaries.

Distribution does not become a second copy of the component engines.

### Member installation

The member receives the admitted product assembled by Distribution from the exact approved component revisions plus legitimate Distribution-owned runtime/generated artifacts.

The member does not receive internal maintainer governance merely because that governance exists in source repos.

---

## 0B. Canonical System propagation rule

Any meaningful change in Distribution or a shipped component repo must evaluate whether AI-Verse-System needs to change.

Meaningful changes include, where relevant:

- new capability;
- meaningful improvement;
- important defect repair;
- lifecycle behavior change;
- install/update/rollback change;
- compatibility change;
- preservation or user-state safety change;
- security/trust change;
- component ownership change;
- member-facing behavior change;
- release/readiness change;
- architecture or topology change;
- previously missing capability becoming implemented.

If the change affects canonical product truth, update the relevant System records as part of the same body of work.

Purely internal changes with no meaningful effect on product truth may be classified `NO SYSTEM IMPACT`, but the reason must be explicit where the governance gate requires it.

Not every change must touch every System file. System must stay accurate, not noisy.

---

## 0C. Canonical owner routing law

Discovery location does not determine ownership.

If Distribution work discovers a problem, first determine the canonical owner.

Examples:

- Skills engine, Skill package, registry/provider, generation, provenance or Skills-specific lifecycle defect -> `AI-Verse-Skills`
- Brain-specific domain behavior -> `AI-Verse-Brain`
- Memory-specific domain behavior -> `AI-Verse-Memory`
- Data-specific domain behavior -> `AI-Verse-Data`
- OS/host-specific domain behavior -> `AI-Verse-OS`
- release-set selection, immutable acquisition, packaging, compatibility, install/update/rollback orchestration or Distribution receipt behavior -> `ai-verse-distribution`

Required flow for sibling-owned work:

```text
Problem or improvement discovered
        |
        v
Determine canonical owner
        |
        v
Fix in owner repository
        |
        v
Owner-repo tests / CI / acceptance pass
        |
        v
Record exact immutable owner commit/ref
        |
        v
Distribution adopts that exact accepted ref
        |
        v
Distribution qualifies the composed AI-Verse release
        |
        v
System reflects meaningful product truth
        |
        v
Release may be admitted
```

Non-negotiable rules:

1. Do not permanently fix a sibling-owned defect only in Distribution.
2. Do not duplicate sibling domain logic into Distribution merely to make qualification pass.
3. Do not claim a sibling problem is fixed until the owner repo contains the accepted fix.
4. Distribution adapters are allowed only for genuine Distribution-owned orchestration/compatibility concerns.
5. Distribution must ship an immutable owner revision that contains the accepted fix before claiming the product includes it.
6. If ownership is ambiguous, use `BLOCKED - OWNER UNRESOLVED` until canonical ownership is established.

---

## 0D. Component -> System and Component -> Distribution handoff law

Component repositories must not be passive islands.

A meaningful component change must evaluate two separate handoffs.

### System handoff

If the component change alters meaningful AI-Verse product truth, the relevant System records must be updated.

### Distribution handoff

If the component change is intended to ship as part of an AI-Verse release:

1. the exact component revision must pass the component repo's own applicable tests/CI/acceptance;
2. exact evidence for that tested revision must be recorded;
3. the revision becomes eligible for Distribution adoption;
4. Distribution must still independently qualify that exact revision as part of the whole composed AI-Verse system;
5. only the Distribution release/admission process determines whether the new component revision ships to members.

Component repos must not directly mutate Distribution or System main branches automatically. Prefer evidence, handoff records, pull requests or explicit maintainer workflow over broad cross-repo write authority.

This creates two validation layers:

```text
Component CI
"Does this component work correctly?"
        |
        v
Distribution qualification
"Does this exact component revision work correctly inside AI-Verse?"
```

A commit merely existing is not sufficient release evidence.

---

## 0E. No blind cross-repo mirroring

Do not create a web where every repository automatically edits every other repository.

Preferred model:

```text
Component repo
  -> owns implementation
  -> validates its own revision
  -> evaluates System impact
  -> offers exact tested ref for Distribution adoption

Distribution
  -> owns composition
  -> validates exact refs together
  -> controls release admission
  -> routes discovered sibling defects back to their owners
  -> evaluates System impact

System
  -> owns canonical big-picture truth
  -> records ownership, architecture, readiness and meaningful evolution
```

Automation may validate references or create/request pull requests when safely designed. Direct unattended writes to other repositories' default branches are not the default.

---

## 0F. Member-isolation law

Maintainer governance must remain separate from the installed member product.

The implementation must prove that:

- source-repo maintainer `AGENTS.md` or `CLAUDE.md` rules are not blindly reused as member instructions;
- System propagation rules are absent from generated member instructions;
- owner-routing, component-handoff and repository-ledger governance are absent from normal member runtime files;
- internal roadmaps, qualification material and maintainer docs are excluded from member payloads;
- fresh install, update and rollback all respect the same boundary;
- future maintainer files are excluded by default where practical;
- user-owned files are never deleted merely to enforce internal packaging rules.

Prefer explicit member payload allowlists or deterministic generation over broad source-tree copying followed by deletion.

---

## 0G. Preservation law

Nothing in this program may weaken zero-loss update behavior.

Preserve member-owned state including, where applicable:

- memories;
- goals;
- preferences;
- profile;
- Brain direction;
- workspaces;
- decisions;
- Data databases;
- connections;
- custom files;
- user-created Skills;
- automations;
- extensions;
- project history;
- other user-owned state covered by the current preservation contract.

If packaging, routing, propagation, handoff or drift-reconciliation logic conflicts with user ownership, fail safely.

---

## 0H. Required decision/evidence fields

For meaningful work, use the applicable fields:

```text
Canonical owner: <repo/component>
Owner change required: YES | NO
Owner reason: <why>
Owner implementation evidence: <commit/PR/ref when required>
Owner CI/acceptance evidence: <workflow/run/check/ref when applicable>

Distribution adoption required: YES | NO
Distribution adopted revision: <exact immutable component ref when applicable>
Distribution evidence: <commit/PR/ref>
Distribution qualification evidence: <workflow/run/report>

System impact: YES | NO
System reason: <why>
System destinations evaluated: <paths/categories>
System evidence: <commit/PR/ref when YES>

Ledger impact: YES | NO
Ledger evidence: <refresh/update ref when applicable>
Drift status: <CLEAN or explicit drift state>

Member payload impact: YES | NO
Member-isolation check: PASS | NOT APPLICABLE | BLOCKED
```

A missing required evidence field blocks completion. A `NO` decision must have a reason when the gate requires classification.

---

## 0I. Status vocabulary

- `NOT STARTED`
- `IN PROGRESS`
- `BLOCKED`
- `COMPLETE`

Every slice records:

- affected repos;
- exact starting refs inspected;
- ownership decision;
- owner CI/acceptance decision where applicable;
- Distribution adoption/qualification decision;
- System impact decision;
- repository-ledger freshness/drift decision where applicable;
- member-isolation decision;
- acceptance criteria;
- tests/validation;
- exact evidence;
- explicit NEXT slice.

Code existing is not enough to mark a slice COMPLETE.

---

## 0J. Repository State Ledger, freshness and non-regression law

Create and maintain the canonical maintainer index:

`docs/REPOSITORY-STATE-LEDGER.md`

The ledger is a **freshness/drift index**, not a replacement source of truth. Live repositories, accepted CI evidence, Distribution release records and canonical System documents remain authoritative for their respective responsibilities.

### Required per-repository state

For every registered AI-Verse repository, the ledger should record at minimum:

```text
Repository: <owner/name>
Role / canonical responsibility: <summary>
Latest observed default-branch HEAD: <sha>
HEAD date: <timestamp/date>
Latest meaningful changes since previous checkpoint: <summary + refs>
Latest owner-tested/accepted revision: <sha/ref or NONE>
Owner acceptance evidence: <workflow/check/report/ref>
Distribution-pinned revision: <sha/ref or NOT SHIPPED>
Distribution release(s): <release id(s) or NONE>
System synchronized through: <sha/ref or UNKNOWN>
Last ledger refresh: <timestamp/date + evidence>
Drift status: <status>
```

The ledger must distinguish these facts because they are not equivalent:

```text
latest repository HEAD
        !=
latest owner-tested/accepted revision
        !=
revision currently shipped by Distribution
        !=
revision/product truth already synchronized into System
```

### Drift vocabulary

Use explicit states such as:

- `CLEAN`
- `UNREVIEWED-COMMITS`
- `OWNER-VALIDATION-MISSING`
- `DISTRIBUTION-BEHIND`
- `SYSTEM-BEHIND`
- `RELEASE-MISMATCH`
- `OWNERSHIP-CONFLICT`
- `ACCESS-UNVERIFIED`
- `CANONICAL-DRIFT-DETECTED`

A newer HEAD is not automatically a problem and is not automatically releasable. `DISTRIBUTION-BEHIND` means newer eligible/accepted work exists that has not yet been adopted, not that Distribution must blindly move to HEAD.

### Freshness-before-trust rule

The ledger cannot literally update itself merely because a Markdown viewer opens it. Therefore any maintainer/agent workflow that **uses the ledger for a meaningful cross-repo, architecture, readiness or release decision** must refresh it first.

Required refresh behavior:

1. query the live default-branch HEAD for every registered repository in scope;
2. compare live refs with the ledger checkpoint;
3. inspect commits newer than the checkpoint rather than merely recording a new SHA;
4. determine whether each new commit is meaningful to architecture/product/release truth;
5. check owner CI/acceptance state where applicable;
6. compare accepted owner refs with Distribution-pinned refs;
7. compare meaningful accepted/released changes with System synchronization state;
8. update the ledger with exact refs, dates, summaries and drift states;
9. only then use the ledger as a navigation/index surface for the decision.

If live repository state cannot be checked, mark the affected entry `ACCESS-UNVERIFIED`; do not silently treat the recorded ledger state as fresh.

### Non-regression / stale-canonical guard

A stale System document must never automatically drive newer accepted implementation backward.

Likewise, a newer code commit must never automatically overrule canonical System intent merely because it is newer.

When System documentation, component implementation, owner acceptance evidence and Distribution release truth disagree, use:

`CANONICAL-DRIFT-DETECTED`

and block destructive reconciliation until the disagreement is understood.

Required reconciliation sequence:

```text
Mismatch detected
        |
        v
Freeze automatic "correction" in either direction
        |
        v
Compare dates, commits, owner CI/acceptance, Distribution release evidence,
System intent/history and migration/compatibility implications
        |
        v
Determine which side is stale or incorrect
        |
        +--> accepted implementation/release is newer valid truth
        |       -> synchronize System forward
        |
        +--> implementation violates canonical intent/contract
                -> repair through canonical owner and requalify
```

No agent may "restore the blueprint" by reverting newer accepted implementation merely because an older canonical document still describes a previous state.

### Known seed drift to reconcile

Purpose Context is the first concrete regression fixture for this program:

- System adopted Purpose Context intent on 2026-10-02;
- Distribution later admitted `core-purpose-context-public-beta-2026-10-09`;
- parts of `docs/FINAL-AI-VERSE-BLUEPRINT.md` still describe Purpose Context as intended/future work.

Phase 1 must verify the exact shipped owner revisions and acceptance evidence, then classify this mismatch and synchronize the stale System truth forward if the October 9 release is confirmed as the accepted product reality. The older blueprint wording must not be used to remove a valid newer implementation.

### Ledger scope growth

New first-class AI-Verse repos must be registered in the ledger as part of introducing them. An implementation repo that participates in product composition must not remain invisible to the cross-repo freshness model.

The ledger and its refresh machinery are maintainer-only and must never be copied into member installations.

---

## 0K. Program accounting

This plan remains 14 slices unless implementation genuinely requires a denominator change.

If slices are added, split, merged or removed:

1. update Program size, Completed, Remaining and Progress;
2. explain the change in the Program Change Log;
3. preserve completed history;
4. do not manipulate the denominator to inflate progress.

---

# Phase 0 - Persistent canonical program

## Slice 0.1 - Create persistent implementation plan

**Status:** COMPLETE  
**Repos:** AI-Verse-System  
**Dependencies:** none

### Acceptance criteria

- persistent plan exists in System;
- Distribution -> System propagation is represented;
- Distribution -> canonical owner routing is represented;
- component -> System and component -> Distribution handoff is represented;
- owner-native validation and whole-product Distribution qualification are distinguished;
- repository-state freshness and non-regression protection are represented;
- member-isolation requirement is represented;
- blind repo mirroring is rejected;
- program is resumable without the original conversation.

### Evidence

- canonical path: `docs/DISTRIBUTION-SYSTEM-PROPAGATION-IMPLEMENTATION-PLAN.md`
- created: 2026-10-12
- expanded on 2026-10-12 as additional repository relationships and drift protections were clarified

### NEXT

**Slice 1.1 - Audit current source, ownership, validation, handoff and repository-drift boundaries.**

---

# Phase 1 - Audit reality before changing it

## Slice 1.1 - Audit Distribution, component, System, ledger and member boundaries

**Status:** NOT STARTED  
**Repos:** AI-Verse-System, ai-verse-distribution, all currently shipped Core component repos, other release-relevant component repos as needed  
**Dependencies:** 0.1

Audit current source rather than relying on assumptions.

Trace:

- Distribution install/bootstrap/update/rollback paths;
- generated member `AGENTS.md`, `CLAUDE.md`, `AI-VERSE.yaml`;
- release-set materialization and exact component refs;
- Distribution component adapters;
- any local vendoring, patching or shadow implementations;
- member file tree and private source/cache locations;
- each shipped component repo's maintainer instructions;
- each shipped component repo's CI/tests/acceptance surfaces;
- whether component repos currently reference System or Distribution;
- how an accepted component commit currently becomes a Distribution release candidate;
- current default-branch HEAD and recent meaningful commits for every repo in scope;
- latest owner-tested/accepted refs where they exist;
- Distribution-pinned refs and admitted release refs;
- System ownership records, blueprint state and living-spec rules;
- known cases where current System wording is older than accepted Distribution/component reality, including Purpose Context.

### Acceptance criteria

- member payload boundary is proven;
- canonical owner of every component-specific behavior inspected is identified;
- current Distribution-to-owner relationship is documented;
- current owner-to-Distribution handoff is documented;
- current owner-to-System handoff is documented;
- native CI/acceptance capability of each shipped component is documented;
- live repo HEAD, owner-accepted ref, Distribution-pinned ref and System-sync state are separately established for every repo in scope;
- Purpose Context's October 9 released state versus older blueprint wording is explicitly resolved or classified as active drift;
- any missing maintainer handoff rule is identified;
- any Distribution shadow-fix risk is identified;
- no implementation change is made before the current boundaries and drift state are understood.

### Evidence

To be recorded on completion.

### NEXT

**Slice 1.2 - Build canonical surface, ownership, handoff and repository-state inventory.**

---

## Slice 1.2 - Classify surfaces, ownership, handoff and drift state

**Status:** NOT STARTED  
**Repos:** AI-Verse-System, ai-verse-distribution, shipped component repos  
**Dependencies:** 1.1

Classify Distribution/member surfaces:

- `MAINTAINER-SOURCE-ONLY`
- `BUILD/QUALIFICATION-ONLY`
- `PACKAGING-INTERNAL`
- `MEMBER-RUNTIME`
- `MEMBER-GENERATED-INSTRUCTION`
- `USER-OWNED/PRESERVED`
- `AMBIGUOUS - BLOCK`

Classify implementation ownership:

- `DISTRIBUTION-OWNED`
- `COMPONENT-OWNED`
- `DISTRIBUTION-ADAPTER-TO-OWNER`
- `AMBIGUOUS-OWNER - BLOCK`

Classify component handoff readiness:

- `OWNER-CI-PRESENT`
- `OWNER-CI-MISSING/INSUFFICIENT`
- `SYSTEM-HANDOFF-PRESENT`
- `SYSTEM-HANDOFF-MISSING`
- `DISTRIBUTION-HANDOFF-PRESENT`
- `DISTRIBUTION-HANDOFF-MISSING`

Build the initial repository-state inventory needed for `docs/REPOSITORY-STATE-LEDGER.md`, including live HEAD, accepted owner ref, Distribution ref, System sync checkpoint and drift classification.

### Acceptance criteria

- every relevant install route has a surface class;
- every component concern has an owner class;
- every shipped component has a validation/handoff class;
- every repo in scope has distinct live/accepted/shipped/System-sync state;
- unknown maintainer files default to exclusion from member payload;
- ambiguous ownership blocks rather than defaults to Distribution;
- a component revision cannot be considered release-ready solely because a SHA exists;
- disagreement between System and accepted implementation is represented as drift rather than automatically resolved in either direction.

### Evidence

To be recorded on completion.

### NEXT

**Slice 1.3 - Define enforceable contracts.**

---

## Slice 1.3 - Define member payload, owner routing, component handoff, release evidence, ledger freshness and non-regression contracts

**Status:** NOT STARTED  
**Repos:** AI-Verse-System, ai-verse-distribution  
**Dependencies:** 1.2

Define canonical contracts for:

1. member payload isolation;
2. canonical owner routing;
3. component -> System handoff;
4. component -> Distribution release handoff;
5. owner-native acceptance evidence;
6. Distribution whole-product qualification;
7. immutable release ref adoption;
8. repository-state ledger structure and refresh semantics;
9. stale-canonical/non-regression reconciliation;
10. safe cross-repo evidence without broad write authority.

Threats to cover:

- Distribution hiding a broken owner repo;
- Distribution shipping an arbitrary unvalidated component SHA;
- component repo claiming "ready" without native CI evidence where applicable;
- Distribution claiming inclusion while pinning an older revision;
- component change shipping without whole-product qualification;
- System becoming stale;
- stale System text causing a future agent to revert newer accepted implementation;
- newer unvalidated code being treated as truth merely because it is newer;
- ledger being trusted without live refresh;
- new first-class repositories remaining unregistered/invisible;
- broad source copy leaking maintainer docs to members;
- automated repos silently editing each other's main branches.

### Acceptance criteria

- contracts distinguish owner tests from Distribution integration tests;
- owner validation is necessary but not sufficient for release;
- Distribution qualification is required for composed-product release;
- exact immutable refs are mandatory;
- missing required owner evidence blocks adoption;
- missing required System evidence blocks documentation completeness;
- stale ledger state cannot silently authorize a release/architecture decision;
- canonical drift blocks destructive reconciliation until evidence determines the stale side;
- member isolation remains explicit;
- no duplicate release database is introduced unnecessarily.

### Evidence

To be recorded on completion.

### NEXT

**Slice 2.1 - Create canonical System governance contract.**

---

# Phase 2 - Make the rules canonical in System

## Slice 2.1 - Create canonical repository-network governance contract

**Status:** NOT STARTED  
**Repos:** AI-Verse-System  
**Dependencies:** 1.3

Create the canonical System-side contract covering:

- System propagation;
- canonical owner routing;
- component -> System handoff;
- component -> Distribution handoff;
- owner CI/acceptance evidence;
- immutable component refs;
- Distribution whole-product qualification;
- release admission;
- repository-state ledger and refresh-before-trust semantics;
- canonical-drift/non-regression behavior;
- member isolation;
- no blind mirroring;
- no broad cross-repo auto-write authority.

### Acceptance criteria

- contract is self-contained;
- future agents can understand all repository directions without this conversation;
- discovery location is clearly separated from ownership;
- owner validation and Distribution qualification are clearly different gates;
- component repos are not treated as passive implementation islands;
- Distribution remains the release/composition authority;
- System remains the canonical big-picture authority;
- System explicitly forbids stale canonical docs from automatically reverting newer accepted implementation;
- newer HEAD alone is explicitly insufficient to override System or Distribution release truth.

### Evidence

To be recorded on completion.

### NEXT

**Slice 2.2 - Integrate governance into living System truth.**

---

## Slice 2.2 - Integrate rules into living System governance

**Status:** NOT STARTED  
**Repos:** AI-Verse-System  
**Dependencies:** 2.1

Evaluate and update where appropriate:

- `docs/LIVING-SPEC-PROTOCOL.md`;
- `docs/OWNER-PRODUCT-INTENT.md`;
- `docs/FINAL-AI-VERSE-BLUEPRINT.md`;
- new `docs/REPOSITORY-STATE-LEDGER.md`;
- component specs/source maps/QC where ownership needs clarification;
- Distribution-related System records;
- `docs/SYSTEM-CHANGELOG.md`.

Reconcile known stale canonical truth, including Purpose Context, from exact accepted implementation/release evidence rather than assumption.

### Acceptance criteria

- System agents discover all four relationships naturally:
  - Distribution -> System
  - Distribution -> component owners
  - component repos -> System
  - component repos -> Distribution
- the repository-state ledger exists with its first evidence-backed checkpoint;
- the ledger declares itself non-authoritative until refreshed against live repositories;
- Purpose Context current-vs-intended wording is synchronized to confirmed accepted reality;
- no false claim that other implementation already exists before Phase 3;
- changelog records the governance and reconciliation decisions;
- canonical files are updated only where they actually own the truth.

### Evidence

To be recorded on completion.

### NEXT

**Slice 2.3 - Finalize evidence schema, ledger refresh semantics and release handoff.**

---

## Slice 2.3 - Define evidence schema, ledger refresh and release handoff semantics

**Status:** NOT STARTED  
**Repos:** AI-Verse-System, ai-verse-distribution  
**Dependencies:** 2.2

Finalize the lightweight evidence format from section 0H.

Define specifically:

- what counts as accepted owner CI/acceptance evidence;
- what happens when a component repo has no suitable native CI;
- exact immutable revision requirements;
- lineage/descendant rules if explicitly allowed;
- how Distribution records adoption;
- how System impact is recorded;
- how live repo checkpoints are refreshed into the ledger;
- how commits since the previous ledger checkpoint are summarized/classified;
- what decisions require a fresh ledger versus a limited scoped refresh;
- how inaccessible repos are represented without pretending freshness;
- how `CANONICAL-DRIFT-DETECTED` is resolved and evidenced;
- where these maintainer records live;
- how release admission fails when required evidence is absent.

### Acceptance criteria

- arbitrary SHA adoption cannot silently become a released Core;
- owner CI evidence is tied to the exact candidate revision where technically possible;
- missing native CI is visible and must be resolved or explicitly qualified before release;
- Distribution qualification remains independent;
- ledger refresh is evidence-based rather than timestamp-only;
- read/use of the ledger for meaningful decisions cannot silently proceed from known stale state;
- records stay outside member runtime files.

### Evidence

To be recorded on completion.

### NEXT

**Slice 3.1 - Add Distribution maintainer instructions.**

---

# Phase 3 - Enforce the repository network

## Slice 3.1 - Add source-only Distribution maintainer instructions

**Status:** NOT STARTED  
**Repos:** ai-verse-distribution  
**Dependencies:** 2.3

Update source-only Distribution instructions so maintainers/agents must:

- determine canonical owner;
- route sibling-owned changes to the owner repo;
- require accepted owner evidence;
- require exact immutable revision adoption;
- evaluate System impact;
- refresh/reconcile relevant repository-ledger state before meaningful cross-repo/release decisions;
- stop on canonical drift rather than automatically rewriting either side;
- keep governance out of member instructions;
- never treat a random component SHA as automatically releasable.

### Acceptance criteria

- rules are discoverable from Distribution development context;
- member-generated instructions remain clean;
- Distribution-only work remains possible when Distribution truly owns the concern;
- sibling-owned work cannot be declared complete with only a Distribution commit;
- stale ledger/System state cannot silently justify changing accepted component behavior backward.

### Evidence

To be recorded on completion.

### NEXT

**Slice 3.2 - Add component-repo maintainer handoff instructions.**

---

## Slice 3.2 - Add source-only component -> System / Distribution handoff instructions

**Status:** NOT STARTED  
**Repos:** currently shipped Core component repos first, then other release-relevant component repos according to System ownership  
**Dependencies:** 3.1

Add a minimal maintainer rule to each relevant canonical component repo, using the repo's existing instruction surface where possible instead of forcing identical file layouts.

Required semantics:

1. the component repo remains canonical for its own implementation;
2. meaningful component changes evaluate System impact;
3. if intended to ship, the exact revision must pass the repo's applicable native tests/CI/acceptance;
4. exact accepted revision/evidence is handed to Distribution for adoption;
5. meaningful accepted changes update the repository-state ledger checkpoint through the supported maintainer workflow;
6. Distribution, not the component repo, performs final whole-product qualification/release admission;
7. component repos do not directly auto-write Distribution or System main by default;
8. these are source-maintainer rules, not member runtime instructions.

### Acceptance criteria

- each shipped Core owner has an explicit handoff rule;
- existing repo conventions are respected;
- no unnecessary runtime/member files are changed;
- no repo receives broad credentials to mutate other repos;
- future maintainers can discover how a component change becomes part of AI-Verse;
- a new accepted component change cannot remain invisible to the freshness/drift model indefinitely under the supported workflow.

### Evidence

To be recorded per repo.

### NEXT

**Slice 3.3 - Enforce adoption, qualification, ledger and member-isolation gates.**

---

## Slice 3.3 - Enforce owner evidence, Distribution adoption, release qualification, ledger freshness and member isolation

**Status:** NOT STARTED  
**Repos:** ai-verse-distribution  
**Dependencies:** 3.2

Integrate the contracts into the most authoritative existing Distribution release/qualification flow.

Required behavior:

- component change intended for release requires exact owner ref;
- applicable owner CI/acceptance must be passing or explicitly resolved;
- Distribution release candidate must point to the accepted ref;
- Distribution performs clean-machine/composed-product qualification;
- failed whole-product qualification blocks admission;
- System evidence is required when System impact is `YES`;
- relevant ledger state must be refreshed before release admission and must reflect the candidate/shipped refs accurately;
- unresolved `CANONICAL-DRIFT-DETECTED`, `RELEASE-MISMATCH` or required `SYSTEM-BEHIND` state blocks admission when the contract says product truth would otherwise be inconsistent;
- member payload isolation applies to fresh install, update and rollback;
- Distribution does not vendor a shadow copy of sibling implementation as a shortcut.

### Acceptance criteria

- arbitrary new component commit is not automatically accepted;
- owner tests and Distribution tests are both represented as separate gates;
- release cannot claim a sibling fix while pinning an older ref;
- release cannot ship when required owner evidence is missing;
- release cannot ship when whole-product qualification fails;
- release cannot silently proceed from a stale or contradictory repository-state checkpoint;
- maintainer files remain outside member payload;
- zero-loss preservation remains intact.

### Evidence

To be recorded on completion.

### NEXT

**Slice 3.4 - Add regression coverage.**

---

## Slice 3.4 - Add automated regression coverage

**Status:** NOT STARTED  
**Repos:** ai-verse-distribution, representative component repos where needed  
**Dependencies:** 3.3

Required scenarios:

- Distribution-owned change with no sibling commit required;
- sibling-owned Skills-like defect cannot close with only Distribution evidence;
- owner commit exists but owner CI fails -> Distribution adoption/release blocked;
- owner commit passes owner CI but Distribution whole-Core qualification fails -> release blocked;
- owner commit passes both layers -> candidate may proceed;
- Distribution pins wrong/older owner ref -> blocked;
- required System evidence missing -> documentation/release gate blocked according to contract;
- legitimate `NO SYSTEM IMPACT` requires rationale;
- live repo HEAD advances beyond ledger -> `UNREVIEWED-COMMITS`, not automatic adoption;
- accepted owner ref advances beyond Distribution -> `DISTRIBUTION-BEHIND`, not automatic release;
- Distribution ships newer accepted behavior while System remains old -> `SYSTEM-BEHIND`/`CANONICAL-DRIFT-DETECTED`, never automatic code rollback;
- newer unvalidated code conflicts with System -> no automatic System rewrite;
- inaccessible live repo -> `ACCESS-UNVERIFIED`, not false freshness;
- new registered first-class repo missing from ledger -> governance failure;
- fresh install excludes maintainer governance;
- update excludes maintainer governance;
- rollback excludes maintainer governance;
- user-owned state survives;
- fake future maintainer file remains excluded.

### Acceptance criteria

- tests prove both validation layers;
- tests prove canonical owner routing;
- tests prove System propagation gate;
- tests prove ledger freshness and non-regression behavior;
- tests prove member isolation;
- tests do not weaken existing qualification/preservation coverage.

### Evidence

To be recorded on completion.

### NEXT

**Slice 4.1 - Add cross-repo evidence and freshness validation.**

---

# Phase 4 - Qualify and close the loop

## Slice 4.1 - Add cross-repo evidence and freshness validation

**Status:** NOT STARTED  
**Repos:** ai-verse-distribution, AI-Verse-System, relevant component repos  
**Dependencies:** 3.4

Implement the strongest safe verification available.

Preferred validation:

- owner commit/ref exists;
- owner acceptance evidence corresponds to the intended revision where possible;
- Distribution release candidate actually adopts that revision;
- System evidence exists when required;
- ledger checkpoint corresponds to live repository state at the required scope;
- commits newer than the previous checkpoint are inspected/classified;
- Distribution-pinned and System-synchronized refs match the facts recorded in the ledger;
- evidence failures are distinct from permission/access failures;
- no broad cross-repo write credential is introduced merely for convenience.

### Acceptance criteria

- stale/missing owner evidence is detectable;
- stale/missing System evidence is detectable;
- wrong pinned component ref is detectable;
- stale/unverified ledger state is detectable;
- canonical drift is surfaced without automatic regression;
- validation fails closed where the contract requires it;
- evidence validation does not leak secrets or maintainer metadata into member installs.

### Evidence

To be recorded on completion.

### NEXT

**Slice 4.2 - Run end-to-end repository-network qualification.**

---

## Slice 4.2 - End-to-end qualification

**Status:** NOT STARTED  
**Repos:** AI-Verse-System, ai-verse-distribution, at least one representative component owner, plus current Core as needed  
**Dependencies:** 4.1

Run four representative paths.

### Scenario A - Distribution-owned improvement

Distribution change -> Distribution tests -> System impact decision -> ledger refresh -> whole-product qualification -> member install.

### Scenario B - component-owned change initiated in the component repo

Component improvement -> owner CI pass -> System impact update -> ledger refresh -> exact ref handed to Distribution -> Distribution adopts ref -> whole-product qualification -> member install/update.

### Scenario C - sibling-owned problem discovered by Distribution

Distribution discovers problem -> routes to owner -> owner fixes and passes CI -> ledger refresh -> Distribution adopts exact ref -> Distribution qualification -> System truth synchronized -> member install/update.

### Scenario D - stale canonical documentation versus newer accepted/released reality

Use Purpose Context or an equivalent fixture: confirm accepted owner/release evidence -> detect stale System wording -> mark drift -> reconcile System forward without reverting valid implementation -> refresh ledger -> re-run relevant qualification/readiness checks.

For all scenarios verify:

- correct ownership;
- exact refs;
- owner evidence;
- Distribution evidence;
- System evidence;
- fresh ledger state;
- no maintainer governance leakage;
- protected member state survives;
- rollback behavior remains safe where supported.

### Acceptance criteria

- all four paths work;
- component repos, Distribution, System and repository ledger agree on the shipped truth;
- owner CI alone cannot ship a release;
- Distribution qualification cannot substitute for repairing a broken owner repo;
- stale System text cannot automatically regress accepted implementation;
- newer unvalidated code cannot automatically rewrite canonical System truth;
- member experience remains one cohesive AI-Verse product.

### Evidence

To be recorded on completion.

### NEXT

**Slice 4.3 - Canonical closeout.**

---

## Slice 4.3 - Canonical closeout

**Status:** NOT STARTED  
**Repos:** AI-Verse-System, ai-verse-distribution, affected component repos  
**Dependencies:** 4.2

Close only after the repository network is proven.

Update as applicable:

- this plan;
- `docs/REPOSITORY-STATE-LEDGER.md`;
- System living-spec/product-intent/blueprint;
- component ownership/spec/QC/source maps;
- System changelog;
- Distribution maintainer docs;
- component maintainer handoff docs;
- release/qualification evidence.

### Acceptance criteria

- all 14 slices are COMPLETE with exact evidence;
- Distribution -> System propagation works;
- Distribution -> component owner routing works;
- component -> System handoff works;
- component -> Distribution handoff works;
- owner-native validation and Distribution whole-product qualification are both enforced;
- arbitrary component SHAs cannot silently become admitted releases;
- repository ledger distinguishes latest, accepted, shipped and System-synchronized state;
- ledger freshness is verified before supported meaningful cross-repo/release decisions;
- canonical drift is detected and reconciled without automatic regression;
- newly introduced first-class product repos cannot remain invisible to the ledger under the supported workflow;
- released component behavior traces to accepted canonical owner revisions;
- Distribution cannot hide sibling defects with permanent local patches;
- System accurately reflects meaningful product truth;
- member installation contains no internal governance leakage;
- zero-loss preservation remains satisfied;
- program status changes to COMPLETE only after all gates pass.

### Evidence

To be recorded on completion.

### NEXT

None. Program v1 complete.

---

# Program Change Log

## 2026-10-12 - Repository State Ledger, freshness and non-regression guard added

- Added planned canonical maintainer index `docs/REPOSITORY-STATE-LEDGER.md`.
- Required separate tracking of live repo HEAD, latest owner-tested/accepted revision, Distribution-pinned revision and System synchronization checkpoint.
- Added explicit drift states including `UNREVIEWED-COMMITS`, `DISTRIBUTION-BEHIND`, `SYSTEM-BEHIND`, `RELEASE-MISMATCH`, `ACCESS-UNVERIFIED` and `CANONICAL-DRIFT-DETECTED`.
- Added refresh-before-trust semantics: meaningful cross-repo, architecture, readiness and release decisions must compare the ledger with live repository state first.
- Added the rule that latest HEAD is not automatically accepted or releasable.
- Added the non-regression guard: stale System documentation cannot automatically revert newer accepted implementation, and newer code cannot automatically override System merely because it is newer.
- Added evidence-led reconciliation rather than automatic correction in either direction.
- Added automatic registration requirement for future first-class AI-Verse repos entering product composition.
- Added Purpose Context as the first concrete stale-canonical regression fixture because Distribution admitted `core-purpose-context-public-beta-2026-10-09` while older blueprint wording still describes Purpose Context as intended/future work.
- Integrated ledger/drift requirements into all existing audit, governance, enforcement, regression, qualification and closeout slices.
- Kept the program at 14 slices and Slice 0.1 as the only completed slice; this change strengthens the plan without falsely claiming implementation is already complete.

## 2026-10-12 - Component handoff and two-layer validation added

- Added explicit component -> System handoff for meaningful component changes.
- Added explicit component -> Distribution release handoff for component revisions intended to ship.
- Added the rule that a component SHA is not releasable merely because it exists.
- Added owner-native CI/test/acceptance evidence as the first validation layer.
- Preserved Distribution whole-product qualification as the second, independent validation layer.
- Added the requirement that shipped Core component repos receive lightweight maintainer handoff instructions.
- Explicitly rejected making component repos directly auto-edit Distribution or System main by default.
- Extended end-to-end qualification to cover Distribution-owned, component-originated and Distribution-discovered sibling changes.
- Kept the program at 14 slices by using Slice 3.2 for component maintainer handoff and consolidating release gates into Slice 3.3.
- Kept Slice 0.1 as the only completed slice. This update strengthens the plan and does not claim implementation is already complete.

## 2026-10-12 - Canonical owner routing added

- Added the rule that Distribution must not become a substitute implementation repo for sibling components.
- Added owner routing, immutable owner refs and composed release qualification.
- Added owner evidence fields and regression requirements.
- Kept the program at 14 slices.

## 2026-10-12 - Program created

- Created the persistent implementation program.
- Required meaningful Distribution evolution to propagate into System.
- Required maintainer governance to stay outside member installations.
- Chose semantic propagation instead of blind commit mirroring.
- Marked only Slice 0.1 complete.

---

# Current execution pointer

**Completed:** Slice 0.1  
**Next:** Slice 1.1 - Audit current source, ownership, validation, handoff and repository-drift boundaries  

Do not skip directly to maintainer-rule edits. Slice 1.1 must first prove the current member boundary, component ownership, component CI/acceptance surfaces, current Distribution adoption path, existing cross-repo handoff behavior and the live-vs-accepted-vs-shipped-vs-System-synchronized state of the repository network.