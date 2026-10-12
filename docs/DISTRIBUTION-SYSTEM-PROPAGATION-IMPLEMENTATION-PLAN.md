# AI-Verse Repository Network Governance, Release Safety and Self-Checking Implementation Plan

**Status:** ACTIVE  
**Canonical planning repo:** `aiverse-filmmakers/AI-Verse-System`  
**Primary implementation repo:** `aiverse-filmmakers/ai-verse-distribution`  
**Affected repos:** AI-Verse-System, ai-verse-distribution, all releasable AI-Verse component repositories  
**Started:** 2026-10-12  
**Program size:** 20 slices  
**Completed:** 1  
**Remaining:** 19  
**Overall progress:** 5.0%  
**Current execution phase:** Phase 1 - Audit and normalize current reality  
**Current phase progress:** 0/3 slices complete  
**Slices until next phase:** 3  
**Next slice:** 1.1 - Audit the live repository network and existing safety machinery  
**Next slice task list:** NOT YET DERIVED - generate from live evidence when Slice 1.1 starts

> This file is the execution tracker. It must update before and after every implementation slice. A slice is not COMPLETE until its implementation, tests, evidence, plan update and progress accounting are all committed.

---

# 0. Program mission

Make the AI-Verse repository network behave as one controlled, self-checking product without collapsing the repositories into one codebase.

The finished system must satisfy all of the following at once:

1. **System stays current.** Meaningful product, architecture, lifecycle, ownership, readiness and release truth is reflected appropriately in AI-Verse-System.
2. **Canonical owners remain canonical.** Skills, Brain, Memory, Data, OS and every other component remain the implementation authority for their own behavior. Distribution must never become a permanent shadow implementation.
3. **Distribution ships only accepted compositions.** A component revision must pass its owner-repo acceptance first, then the exact composed release must pass Distribution qualification before admission.
4. **Repository drift is visible.** The system can distinguish live repo HEAD, owner-accepted revision, Distribution-shipped revision and System-synchronized truth.
5. **Stale documentation cannot regress newer accepted implementation.** Disagreement causes explicit reconciliation, not automatic rollback or automatic doc overwrite.
6. **Member-owned state remains protected.** Nothing in this program may weaken the existing safe-update/state-preservation floor.
7. **Maintainer governance remains outside member installs.** Internal repository-network controls must not leak into generated member projects.
8. **Every admitted release is reconstructable.** Exact software composition and durable release evidence remain recoverable later.
9. **The repository network can detect its own decay.** Missing repos, stale watchdogs, stale System truth, invalid handoffs and mismatched release refs become visible failures rather than silent drift.
10. **Execution adapts to evidence.** Slice outcomes stay stable, but low-level tasks are discovered/refined from current reality rather than fully guessed at program creation time.
11. **Adaptive discovery cannot silently redirect the program.** Discovery may optimize tasks and implementation tactics, but protected roadmap intent, laws, ownership, safety floors and acceptance outcomes require an explicit plan-amendment decision.

The central design rule is:

> **Define centrally. Enforce at the canonical owner. Verify again at composition.**

The execution-planning rule is:

> **Fix the destination. Discover the safest route from current reality.**

The adaptive-authority rule is:

> **Discovery may adapt the route. It may not silently change the destination.**

Reusable planning method: `docs/ADAPTIVE-IMPLEMENTATION-PLANNING-SKILL.md`.

---

# 1. Canonical roles

## AI-Verse-System

Owns:

- architecture and product intent;
- component responsibility/ownership;
- system invariants;
- cross-repo governance contracts;
- repository registry;
- repository-state model and human ledger;
- architecture tombstones/history;
- shared release/compatibility semantics;
- current-versus-intended system truth;
- system changelog and readiness/QC truth.

System is not a second implementation home and is not the member installer.

## Component repositories

Each canonical component repo owns:

- its implementation;
- component-local tests/CI/acceptance;
- its interfaces/contracts/schemas;
- component-local migrations and recovery semantics;
- component release descriptor/evidence;
- component-local implementation provenance.

A component repo does not directly decide that a revision ships to members.

## ai-verse-distribution

Owns:

- exact release sets;
- immutable component refs;
- compatibility/composition;
- candidate admission flow;
- source acquisition;
- install/setup/update/rollback orchestration;
- member payload boundaries;
- whole-product qualification;
- promotion/release channels;
- release receipts and reconstructability;
- Distribution-specific recovery/rollback evidence.

Distribution does not own sibling component domain logic or canonical user state.

## Member installation

Receives only admitted runtime/product artifacts plus legitimate generated member-facing files.

It must not receive internal repository-network governance except narrowly required machine-readable runtime compatibility metadata.

---

# 2. Existing contracts to reuse, not duplicate

Before creating new machinery, implementation must reuse and extend existing canonical contracts where they already solve the problem.

At minimum:

- `docs/SAFE-UPDATE-AND-STATE-PRESERVATION-CONTRACT.md`
- `docs/COMPONENT-RELEASE-DESCRIPTOR-CONTRACT.md`
- `docs/WHOLE-RELEASE-PRESERVATION-RESULT-CONTRACT.md`
- `docs/LIVING-SPEC-PROTOCOL.md`
- `docs/OWNER-PRODUCT-INTENT.md`
- `docs/FINAL-AI-VERSE-BLUEPRINT.md`

Important consequences:

- do **not** create a second safe-update system;
- do **not** create a second component release-metadata format if the existing component release descriptor can be versioned/extended;
- do **not** create a second whole-release acceptance database when the existing release-preservation result and Distribution release records can carry the evidence;
- do **not** duplicate canonical user-state ownership in Distribution;
- do **not** maintain the same global repository truth manually in multiple files.

---

# 3. Permanent laws for this program

## 3.1 Canonical owner routing

Discovery location does not determine ownership.

If Distribution discovers a sibling-owned defect/improvement:

```text
Discover change
-> determine canonical owner
-> fix owner repo
-> owner CI/acceptance passes
-> record exact immutable owner revision
-> Distribution adopts exact accepted revision
-> Distribution qualifies exact composition
-> System synchronizes meaningful product truth
-> release may be admitted
```

If ownership is ambiguous: `BLOCKED - OWNER UNRESOLVED`.

## 3.2 Two validation layers

```text
Owner validation
"Does this component revision satisfy its own contract?"
        ↓
Distribution qualification
"Do these exact accepted revisions work together as AI-Verse?"
```

A SHA merely existing is never release evidence.

## 3.3 Static truth versus dynamic state

Do not make the Repository State Ledger duplicate the Repository Registry.

- **Repository Registry** = what each repo is, its stable identity, ownership and declared role.
- **Repository State** = where that repo currently stands.
- **Generated Markdown ledger** = human-readable projection of repository state.

Target shape:

```text
repository-registry.json
        ↓
repository-state.json
        ↓
generated docs/REPOSITORY-STATE-LEDGER.md
```

The Markdown ledger is not the machine source of truth.

## 3.4 Freshness without unnecessary full scans

Use scoped refreshes for scoped decisions.

Examples:

- Skills candidate decision -> refresh Skills + Distribution + relevant System contracts + declared direct dependencies.
- Core release admission -> refresh all Core repos + System + Distribution.
- whole-system architecture review/watchdog -> full registered-repo scan.

A full scan before every small change is prohibited unless the contract actually requires it.

## 3.5 Git identity and ancestry over timestamps

Dates are display/context information only.

Freshness and lineage decisions must use exact immutable refs, repository identity and Git ancestry/compare evidence where applicable. Rebase/cherry-pick timestamps must not be treated as canonical ordering proof.

Repository Registry should use stable repository identity where available in addition to `owner/name` so renames do not silently create a new logical component.

## 3.6 Canonical drift/non-regression

A stale System document cannot automatically revert newer accepted implementation.

A newer implementation commit cannot automatically rewrite canonical System intent merely because it is newer.

Use:

`CANONICAL-DRIFT-DETECTED`

Then reconcile evidence-first.

```text
Mismatch
-> freeze automatic correction
-> compare exact refs, owner acceptance, Distribution release truth, System intent/history and migration impact
-> determine stale/incorrect side
-> synchronize System forward OR repair owner implementation
-> requalify when product composition changed
```

## 3.7 Drift severity and scope

Not every drift condition blocks every release.

Every drift result should carry:

```text
severity: INFO | WARNING | BLOCKING
scope: component | Core | Agent | Full | global
reason
relevant refs
required action
```

A Dashboard warning must not automatically block an unrelated Core release.

## 3.8 Member isolation

Source maintainer `AGENTS.md`, `CLAUDE.md`, roadmaps, repository registry/state, drift reports, tombstones, internal qualification material and governance must not leak into member installs.

Prefer explicit/deterministic member payload inclusion over broad copy + delete.

Unknown/user files remain protected by the existing preservation contract.

## 3.9 Immutable qualification snapshot

Every composed release qualification must be bound to an immutable evidence snapshot so moving `main` branches cannot change what was tested halfway through.

The candidate snapshot should bind, as applicable:

- exact Distribution candidate revision;
- exact System governance/contract revision used;
- exact Repository Registry revision;
- exact component refs;
- exact component release descriptors;
- exact owner acceptance evidence;
- exact compatibility/migration metadata;
- exact whole-release preservation evidence;
- applicable toolchain/runtime/lock information.

If a bound input changes, the candidate must be re-evaluated/requalified rather than silently inheriting the previous result.

## 3.10 Durable release evidence

Important admitted-release evidence must not exist only in expiring GitHub Actions logs/artifacts.

For every admitted release, persist a compact durable release receipt with enough immutable data to reconstruct the shipped software composition later.

## 3.11 Emergency safety release path

Support a tightly bounded break-glass path for urgent security, corruption or user-data-protection fixes.

It must **not** bypass owner validation, exact refs, preservation requirements or Distribution qualification.

It may temporarily allow non-safety documentation synchronization debt only when explicitly recorded as `SYSTEM-SYNC-DEBT`.

A later normal promotion must be blocked until required debt is reconciled.

## 3.12 Architecture tombstones

Retired/replaced architecture must leave durable evidence so stale docs, old audits or future agents cannot resurrect superseded structures accidentally.

Tombstones belong primarily in System; component-local tombstones are used only for local APIs/schemas/migrations when needed.

## 3.13 No silent contract deletion

A component must not silently remove/redefine a depended-on API/schema/interface simply because local tests pass.

Breaking changes require a compatible replacement, versioned coexistence, or an explicit coordinated breaking release/migration with affected owners and Distribution qualification.

## 3.14 Rollout waves

Implement this governance in dependency-safe waves:

- **Wave 1:** System + Distribution + Core (`OS`, `Brain`, `Memory`, `Skills`, `Data`).
- **Wave 2:** Agent-profile repos (Gateway, Automations, Multiple Bots and other Agent dependencies confirmed by registry).
- **Wave 3:** Full/future ecosystem (Connections, Apps, Dashboard, Token and future first-class repos).

Prove the pattern on Core before assuming it scales unchanged.

## 3.15 Adaptive execution authority boundary

Self-discovery is powerful only inside a bounded execution authority.

It may automatically adapt:

- low-level tasks;
- implementation techniques within the current slice;
- `CREATE` into `REUSE`/`EXTEND` when evidence proves existing machinery is sufficient;
- tests/evidence that strengthen the acceptance proof;
- the smallest dependency/blocker tasks needed to finish the existing slice safely.

It may **not** automatically change:

- permanent laws or invariants;
- product intent;
- canonical ownership;
- phase purpose;
- slice purpose/outcome;
- acceptance criteria in a weaker direction;
- preservation, safety, validation, member-isolation or evidence floors;
- major architecture direction;
- slice removal/major reordering;
- program denominator.

Those are plan amendments, not task adaptation.

When evidence suggests a protected change is required, the affected work must stop as:

`BLOCKED - PLAN AMENDMENT REQUIRED`

The implementation agent must propose the amendment with exact evidence and impact instead of self-approving it.

Non-degradation law:

> **Discovery may reduce unnecessary work. It may never reduce safety, ownership, preservation, validation, member-isolation, or required evidence on its own authority.**

When uncertain whether a proposed change is task adaptation or roadmap redirection, fail safely into the amendment path.

---

# 4. Protection placement map

| Protection | Canonical definition | Local enforcement/publication | Composition verification |
|---|---|---|---|
| Repository Registry | System | System | Distribution consumes relevant subset |
| Repository State + Ledger | System | System refresh tooling | Distribution checks scoped freshness |
| Drift Watchdog | System | System automation | Distribution consumes relevant blocking drift |
| Architecture Tombstones | System | component-local only when needed | System/Distribution inspect when relevant |
| System Invariants | System | canonical owner of each behavior | Distribution verifies cross-component invariants |
| Compatibility metadata | System contract/schema | component release descriptor | Distribution validates selected exact set |
| Promotion rings | System policy | Distribution | Distribution |
| Reproducibility guarantee | System | component immutable refs/metadata | Distribution release receipt |
| No silent contract deletion | System law | interface-owning component | Distribution composed compatibility |
| Decision/recovery provenance | System law | System/component/Distribution each own their layer | cross-repo validation |

Do not copy all of these as full documents into every repository.

---

# 5. Required evidence model

Meaningful work must record the applicable fields:

```text
Canonical owner: <repo/component>
Owner change required: YES | NO
Owner reason: <why>
Owner implementation evidence: <commit/PR/ref>
Owner CI/acceptance evidence: <run/check/report/ref>

Distribution adoption required: YES | NO
Distribution adopted revision: <exact ref>
Distribution evidence: <commit/PR/ref>
Distribution qualification evidence: <run/report/receipt>

System impact: YES | NO
System reason: <why>
System destinations evaluated: <paths/categories>
System evidence: <commit/PR/ref>

Repository-state impact: YES | NO
Refresh scope: <component/Core/Agent/Full/global>
Repository-state evidence: <state/ledger ref>
Drift severity/scope: <value>

Member payload impact: YES | NO
Member-isolation check: PASS | NOT APPLICABLE | BLOCKED

Reproducibility impact: YES | NO
Release receipt evidence: <ref when applicable>

Plan-amendment impact: YES | NO
Protected roadmap element affected: <law/phase/slice/acceptance/ownership/denominator/etc.>
Amendment status/evidence: <none | BLOCKED - PLAN AMENDMENT REQUIRED | approved ref>
```

A required `NO` decision needs a reason. Missing mandatory evidence blocks completion.

---

# 6. Mandatory progress bookkeeping and user reporting

This program is deliberately self-maintaining through the supported maintainer workflow.

## Before starting every slice

Update this file to:

- mark the slice `IN PROGRESS`;
- record the exact starting refs in scope;
- refresh only the current state needed to plan the slice safely;
- derive and record the current adaptive task list for that slice;
- record task count and task status;
- verify that derived tasks stay inside the slice's protected purpose/acceptance boundary;
- record the current phase and progress counters;
- preserve the previous evidence/history.

No substantial slice should begin implementation from an old guessed task list.

## Before marking a slice COMPLETE

The same body of work must update this file with:

- final status = `COMPLETE`;
- final task list with every required task closed or explicitly superseded with reason;
- exact implementation commits/PRs;
- exact tests/workflows/reports;
- owner/System/Distribution/ledger/release evidence as applicable;
- blockers discovered/resolved;
- changed assumptions or task-list changes and their evidence;
- confirmation that no protected roadmap element was silently changed;
- plan-amendment evidence if any amendment was required and approved;
- current phase progress;
- overall completed/total;
- overall percentage;
- slices until next phase;
- explicit NEXT slice.

A slice is **not complete** until this plan update is committed successfully.

## Overall percentage rule

Overall progress is slice-based:

`completed slices / total program slices * 100`

Display to one decimal place unless exactly integral.

Task count is local execution detail only. If discovery adds or removes legitimate tasks, overall program percentage does not move backward because slices are the stable acceptance unit.

A pending plan amendment does not count as progress and must not be hidden by manipulating task counts.

If the slice/program denominator changes through an approved amendment, update the Program Change Log and all counters immediately. Never change the denominator silently.

## Mandatory user-facing completion report

At the end of every completed slice, report in this compact format:

```text
Completed: Slice X.Y - <title>
Tasks: <completed>/<final derived task total>
Overall: <completed>/<total> slices complete (<percent>%)
Phase: <phase number> - <phase title>
Phase progress: <completed in phase>/<total in phase>
Until next phase: <N> slice(s)
Next: <next slice; first task remains adaptive until derived>
Blockers/drift/amendments: <none or concise status>
```

While a slice is in progress, progress updates may also report:

```text
Current task: X.Y.N - <title>
Task progress: <completed>/<current derived task total>
Slice: IN PROGRESS
Overall: <slice-based overall percentage>
```

If the slice is blocked, report the same structure with `Blocked:` and do not increment slice progress.

---

# 6A. Adaptive task discovery and execution law

The 20 slices are the stable implementation roadmap. Their purpose, dependencies and acceptance criteria are intentionally more stable than their low-level task lists.

Low-level tasks are **adaptive execution units** and must not all be frozen at program creation time.

## Rigidity hierarchy

Use four levels of rigidity:

1. **Permanent laws / product intent / canonical ownership** - LOCKED for self-discovery. Changes require explicit plan amendment and architectural evidence.
2. **Phase and slice purpose/outcome + acceptance floor** - LOCKED for self-discovery. May only be changed through explicit amendment; acceptance may be strengthened automatically but never weakened.
3. **Slice implementation method** - ADAPTIVE inside the protected slice outcome.
4. **Tasks** - ADAPTIVE; derive/refine from current evidence while implementing the slice.

Do not confuse task flexibility with roadmap authority.

## Task derivation at slice start

For every substantial slice, derive tasks only after:

1. reading the latest version of this plan and the adaptive planning skill;
2. reviewing findings/evidence from completed dependencies;
3. refreshing the live repositories/state relevant to the slice;
4. inspecting existing implementation before proposing new implementation;
5. classifying relevant needs as `REUSE`, `EXTEND`, `CREATE`, `RETIRE` or `BLOCK/UNKNOWN`;
6. identifying the smallest task set necessary to satisfy the fixed slice acceptance criteria;
7. checking that none of those tasks silently changes a protected law, owner, phase/slice purpose or acceptance floor.

A recommended first task for substantial slices is:

`X.Y.1 - Refresh current state and derive/refine the execution tasks for this slice.`

That discovery task is not permission for endless planning or architectural redirection. It should produce a bounded current task list and move directly into execution.

## Task eligibility rule

Do not create speculative implementation tasks.

A task is justified only when at least one is true:

- required by the slice acceptance criteria;
- required by a verified implementation/audit finding;
- required to resolve a blocker or drift condition;
- required to test/prove an important claim;
- required to reuse/extend an existing mechanism safely;
- required because a previous planned approach was proven invalid or duplicative.

`It sounds sophisticated` is not valid justification.

## Allowed adaptive changes

Tasks may be added, removed, split, merged or reordered when new evidence justifies the change.

Implementation technique may also change when the slice outcome remains unchanged.

Examples:

- if an audited mechanism already solves the need, remove a duplicate CREATE task and replace it with REUSE/EXTEND validation;
- if a hidden dependency appears, add the smallest task needed to understand/fix it;
- if ownership routing within a task was based on a mistaken discovery location, route implementation to the already-canonical owner rather than duplicate the behavior elsewhere;
- if stronger validation is needed, add it without weakening existing acceptance.

When the task list changes:

- update this plan before relying on the new task structure;
- record the finding/reason;
- preserve completed task history;
- do not silently delete failed/superseded work from the record;
- do not weaken acceptance criteria merely to close the slice;
- do not inflate or manipulate task counts to improve apparent progress.

## Protected changes: plan amendment required

Self-discovery must not silently:

- change product intent;
- change permanent laws/invariants;
- transfer canonical ownership;
- redefine a phase's purpose;
- redefine a slice's purpose/outcome;
- weaken/delete acceptance criteria;
- lower preservation, safety, validation, member-isolation or evidence requirements;
- remove a slice merely because implementation is inconvenient;
- perform major phase/slice reordering;
- change the program denominator;
- turn an experimental/newer implementation into canonical architecture only because it is newer.

If evidence indicates one of these is genuinely necessary:

1. stop the affected task/path;
2. mark it `BLOCKED - PLAN AMENDMENT REQUIRED`;
3. record exact evidence;
4. prepare:

```text
PLAN AMENDMENT PROPOSED
Finding: <verified evidence>
Current plan/law: <current governing rule>
Proposed change: <exact protected change>
Why the current route is unsafe/wrong/obsolete: <reason>
Affected phases/slices/repos/contracts: <scope>
Safety/compatibility/user-state impact: <impact>
Alternatives considered: <short list>
Recommendation: <resolution>
```

5. do not execute the protected directional change until explicitly resolved;
6. if approved, update the plan/changelog/counters before resuming;
7. preserve previous plan history and rationale.

When uncertain whether a change is ordinary task adaptation or roadmap redirection, choose the amendment path.

## Non-degradation rule

> **Discovery may reduce unnecessary work. It may never reduce safety, ownership, preservation, validation, member-isolation, or required evidence on its own authority.**

This applies even when reducing those requirements would make implementation easier or faster.

## Task progress accounting

Task progress is local to the current slice and may legitimately change as tasks are discovered.

Example:

```text
Slice 2.1 tasks: 4/7 complete
```

If two evidence-backed tasks are discovered:

```text
Slice 2.1 tasks: 4/9 complete
```

This does not reduce overall program progress. Overall percentage remains slice-based.

## Roadmap amendment, not automatic self-correction

If implementation proves a protected slice/phase/law/ownership decision may be wrongly scoped, ordered or unnecessary, the agent must **propose** rather than silently apply the roadmap change.

The roadmap may evolve, but directional changes require an explicit amendment record and resolution. Adaptive execution itself has no authority to approve them.

---

# 7. Status vocabulary

Slice status:

- `NOT STARTED`
- `IN PROGRESS`
- `BLOCKED`
- `BLOCKED - PLAN AMENDMENT REQUIRED`
- `COMPLETE`

Task status:

- `NOT STARTED`
- `IN PROGRESS`
- `BLOCKED`
- `BLOCKED - PLAN AMENDMENT REQUIRED`
- `COMPLETE`
- `SUPERSEDED` with reason/evidence
- `NOT NEEDED` only when evidence proves it unnecessary and no protected acceptance outcome is removed

Do not mark work COMPLETE merely because code exists.

---

# Phase 0 - Persistent program foundation

## Slice 0.1 - Create and normalize the canonical implementation program

**Status:** COMPLETE  
**Repos:** AI-Verse-System  
**Dependencies:** none

### Acceptance criteria

- canonical resumable plan exists;
- System/Distribution/component/member roles are explicit;
- owner routing, two-layer validation, System propagation and member isolation are represented;
- Repository Registry/State/Ledger, drift protection, reproducibility and non-regression are represented;
- existing safe-update/release contracts are explicitly reused rather than duplicated;
- implementation order is dependency-safe;
- mandatory plan bookkeeping and user progress reporting are defined;
- adaptive task discovery is bounded to execution and cannot silently redirect protected roadmap intent;
- reusable future planning skill exists;
- future agents can resume without this conversation.

### Evidence

- canonical path: `docs/DISTRIBUTION-SYSTEM-PROPAGATION-IMPLEMENTATION-PLAN.md`
- planning skill: `docs/ADAPTIVE-IMPLEMENTATION-PLANNING-SKILL.md`
- original program created 2026-10-12
- normalized into this 20-slice dependency-safe program on 2026-10-12
- adaptive task-discovery model added on 2026-10-12
- adaptive change-authority boundary tightened on 2026-10-12

### NEXT

**Slice 1.1 - Audit the live repository network and existing safety machinery.**

---

# Phase 1 - Audit and normalize current reality

**Phase size:** 3 slices  
**Current phase progress:** 0/3  
**Purpose:** prove what already exists before adding anything.

## Slice 1.1 - Audit the live repository network and existing safety machinery

**Status:** NOT STARTED  
**Dependencies:** 0.1  
**Adaptive tasks:** NOT YET DERIVED - derive from live state at slice start

Audit current source and live repository state.

Trace at minimum:

- every currently shipped Core repo and Distribution exact refs;
- current default-branch HEADs and stable repository identities;
- component native CI/acceptance surfaces;
- component release descriptors and their current fields;
- Distribution candidate/release/preservation evidence flows;
- install/update/rollback/member payload generation;
- existing promotion/candidate/released mechanics;
- existing reproducibility/receipt evidence;
- existing maintainer instructions;
- current System component ownership/spec/blueprint truth;
- current Purpose Context implementation/release truth versus System wording;
- existing API/schema compatibility/versioning mechanisms;
- current source-only versus member-facing file boundaries.

### Acceptance criteria

- exact current implementation and release topology is evidenced;
- existing protections are identified before replacements are proposed;
- Purpose Context drift is classified from exact evidence;
- current Core repo list and identities are known;
- no implementation change is made before the audit is recorded.

### Evidence

To be recorded on completion.

### NEXT

**Slice 1.2 - Build the reuse, ownership, payload and drift inventory.**

---

## Slice 1.2 - Build the reuse, ownership, payload and drift inventory

**Status:** NOT STARTED  
**Dependencies:** 1.1  
**Adaptive tasks:** derive from Slice 1.1 findings when this slice starts

Classify every relevant concern as:

- existing and sufficient;
- existing but extend;
- missing and must implement;
- obsolete/retire;
- ambiguous/block.

Build one inventory covering:

- canonical owner;
- maintainer/member surface;
- existing contract/tooling to reuse;
- owner CI status;
- live HEAD;
- owner-accepted revision;
- Distribution-pinned revision;
- System synchronization state;
- drift severity/scope;
- duplicate-mechanism risks.

### Acceptance criteria

- `COMPONENT-RELEASE-DESCRIPTOR-CONTRACT` is explicitly evaluated as the home for compatibility fingerprints rather than creating another format;
- existing update/preservation/promotion machinery is mapped;
- Registry static fields and Repository State dynamic fields are separated;
- any Distribution shadow implementation/workaround is identified;
- any duplicated or obsolete planned mechanism is removed from the target design only when doing so does not remove a protected acceptance outcome; otherwise use the plan-amendment path.

### Evidence

To be recorded on completion.

### NEXT

**Slice 1.3 - Freeze the implementation architecture and acceptance matrix.**

---

## Slice 1.3 - Freeze the implementation architecture and acceptance matrix

**Status:** NOT STARTED  
**Dependencies:** 1.2  
**Adaptive tasks:** derive from the evidence-backed inventory when this slice starts

Before coding, freeze the implementation decisions for:

- registry schema/location;
- repository-state schema/location;
- generated Markdown ledger;
- scoped/full refresh rules;
- drift severity/scope rules;
- watchdog trigger/heartbeat rules;
- immutable candidate evidence snapshot;
- reuse/extension of component release descriptor;
- promotion rings based on existing Distribution mechanics;
- durable release receipt/reproducibility;
- emergency safety-release path;
- architecture tombstone format;
- rollout waves;
- member payload boundary.

### Acceptance criteria

- no unresolved duplicate source of truth remains in the target design;
- every planned new file/tool has one canonical owner;
- release-blocking versus informational drift is explicit;
- Core Wave 1 acceptance matrix is defined;
- Phase 2 can proceed without architectural guessing.

### Evidence

To be recorded on completion.

### NEXT

**Phase 2 / Slice 2.1 - Create the canonical repository-network governance and invariant contract.**

---

# Phase 2 - Define the canonical System control plane

**Phase size:** 3 slices

## Slice 2.1 - Create the repository-network governance, invariant and tombstone contract

**Status:** NOT STARTED  
**Dependencies:** 1.3  
**Adaptive tasks:** derive at slice start from the frozen Phase 1 architecture

Create the permanent System contract that defines:

- canonical owner routing;
- component -> System handoff;
- component -> Distribution handoff;
- System propagation;
- two-layer validation;
- non-regression/canonical drift;
- permanent system invariants;
- breaking-change/no-silent-contract-deletion law;
- architecture tombstones;
- decision/recovery provenance;
- member isolation;
- emergency safety-release semantics;
- rule against broad unattended cross-repo writes.

### Acceptance criteria

- permanent law is separate from this implementation plan;
- existing updater/preservation laws are referenced rather than copied;
- future agents can find the rules without reading this program history;
- tombstones prevent superseded architecture from being silently resurrected.

### Evidence

To be recorded on completion.

### NEXT

**Slice 2.2 - Create the machine-readable Repository Registry and initial Wave 1 registry.**

---

## Slice 2.2 - Create the machine-readable Repository Registry

**Status:** NOT STARTED  
**Dependencies:** 2.1  
**Adaptive tasks:** derive at slice start; reuse existing machine-readable surfaces if Phase 1 found them

Create a versioned machine-readable Registry, for example:

`ai-verse.repository-registry/v1`

It must separate stable registry truth from dynamic state.

Minimum fields should include, where available:

- stable repository ID;
- current `owner/name`;
- canonical component ID;
- canonical responsibility;
- lifecycle: active/experimental/retired/external;
- release profile participation;
- whether Distribution ships it;
- expected component release descriptor path;
- expected owner CI/acceptance surface;
- System spec/ownership references;
- direct compatibility dependency declarations only where canonically known.

Register Wave 1/Core first.

### Acceptance criteria

- one canonical global registry exists;
- renames do not silently create a new logical component when stable identity is available;
- Distribution does not maintain a competing independent registry;
- unknown first-class repos cannot silently enter release composition.

### Evidence

To be recorded on completion.

### NEXT

**Slice 2.3 - Define Repository State, generated ledger and maintainer entrypoint.**

---

## Slice 2.3 - Define Repository State, generated ledger and maintainer entrypoint

**Status:** NOT STARTED  
**Dependencies:** 2.2  
**Adaptive tasks:** derive at slice start from the accepted Registry and existing maintainer surfaces

Create versioned dynamic repository-state semantics, for example:

`ai-verse.repository-state/v1`

Define:

- live observed HEAD/ref;
- owner-accepted revision and evidence;
- Distribution-shipped revision/release;
- System synchronization checkpoint;
- last scoped/full refresh;
- drift severity/scope/status;
- access-unverified/watchdog-stale states;
- generation of `docs/REPOSITORY-STATE-LEDGER.md` from machine state;
- `MAINTAINER-START-HERE` read order and freshness requirement.

### Acceptance criteria

- Markdown ledger is generated/projected rather than hand-maintained as canonical state;
- Registry fields are not redundantly copied as independent truth;
- scoped refresh requirements are explicit;
- `WATCHDOG-STALE`/equivalent exists so silence cannot masquerade as CLEAN.

### Evidence

To be recorded on completion.

### NEXT

**Phase 3 / Slice 3.1 - Implement repository refresh tooling and generated ledger.**

---

# Phase 3 - Build System self-checking machinery and synchronize current truth

**Phase size:** 3 slices

## Slice 3.1 - Implement scoped/full repository refresh and generated ledger

**Status:** NOT STARTED  
**Dependencies:** 2.3  
**Adaptive tasks:** derive at slice start from accepted state/registry schemas and available GitHub/CI surfaces

Implement System maintainer tooling that:

- reads Registry;
- resolves live repositories;
- compares exact refs/ancestry;
- inspects commits since previous checkpoint;
- reads owner acceptance evidence where available;
- reads Distribution pins/releases;
- records System synchronization state;
- emits versioned repository-state data;
- generates the Markdown ledger;
- supports scoped and full refresh.

### Acceptance criteria

- refresh is deterministic/evidence-backed;
- inaccessible repos become explicit `ACCESS-UNVERIFIED` rather than CLEAN;
- dates are informational, not lineage authority;
- generated ledger accurately reflects machine state;
- no member-facing files are affected.

### Evidence

To be recorded on completion.

### NEXT

**Slice 3.2 - Implement Drift Watchdog, severity/scope and heartbeat.**

---

## Slice 3.2 - Implement Drift Watchdog and heartbeat

**Status:** NOT STARTED  
**Dependencies:** 3.1  
**Adaptive tasks:** derive at slice start from the proven refresh tooling; do not duplicate its logic

Implement whole-network maintainer automation that:

- performs scheduled full scans and/or safe event-triggered scans;
- records last successful full scan, watchdog version, scanned repos and failures;
- classifies INFO/WARNING/BLOCKING drift with scope;
- detects unregistered release-relevant repos;
- detects System-behind, Distribution-behind, release mismatch, owner-validation missing and stale watchdog state;
- reports drift without silently rewriting other repos or promoting commits.

### Acceptance criteria

- stale watchdog cannot present as green/clean;
- unrelated warnings do not block unrelated release scopes;
- watchdog has least-privilege read/validation behavior by default;
- no broad cross-repo write token is required.

### Evidence

To be recorded on completion.

### NEXT

**Slice 3.3 - Reconcile current System truth, including Purpose Context.**

---

## Slice 3.3 - Reconcile current System truth and known drift

**Status:** NOT STARTED  
**Dependencies:** 3.2  
**Adaptive tasks:** derive from actual drift results at slice start; do not pre-assume Purpose Context is the only drift

Use exact accepted owner/Distribution evidence to reconcile System forward where System is stale.

Purpose Context is the first mandatory regression fixture:

- System adopted Purpose Context intent on 2026-10-02;
- Distribution admitted `core-purpose-context-public-beta-2026-10-09`;
- older blueprint wording still describes parts as intended/future.

Update only the canonical System records that actually own the truth.

### Acceptance criteria

- accepted newer implementation is not reverted merely because old docs lag;
- newer unvalidated code is not promoted to canonical truth merely because it is newer;
- Blueprint architecture stays architecture-focused rather than duplicating volatile exact release facts unnecessarily;
- changelog/tombstones record meaningful reconciliation;
- repository state returns to truthful status for the reconciled scope.

### Evidence

To be recorded on completion.

### NEXT

**Phase 4 / Slice 4.1 - Extend the existing component release descriptor for shared compatibility semantics.**

---

# Phase 4 - Integrate canonical component owners

**Phase size:** 3 slices

## Slice 4.1 - Extend/reuse the existing component release descriptor

**Status:** NOT STARTED  
**Dependencies:** 3.3  
**Adaptive tasks:** derive at slice start; only add descriptor fields Phase 1/3 evidence proves necessary

Do not create a separate compatibility fingerprint format.

Version/extend `COMPONENT-RELEASE-DESCRIPTOR-CONTRACT` only where the Phase 1 audit proved missing fields are necessary.

Potential additions may include:

- interface/contract generation;
- state-schema generation;
- explicit required contract ranges;
- breaking-change classification;
- migration requirements;
- compatibility dependency declarations that the component canonically owns.

### Acceptance criteria

- one component release metadata format remains canonical;
- descriptor still does not become live health/readiness/authority truth;
- compatibility metadata is tied to exact immutable component revision;
- breaking contract change cannot silently present as ordinary compatible update.

### Evidence

To be recorded on completion.

### NEXT

**Slice 4.2 - Add Wave 1/Core maintainer handoff and owner-acceptance rules.**

---

## Slice 4.2 - Add Wave 1/Core component maintainer handoff rules

**Status:** NOT STARTED  
**Dependencies:** 4.1  
**Adaptive tasks:** derive per Core repo from its real maintainer/CI conventions

For OS, Brain, Memory, Skills and Data, add minimal source-only maintainer guidance using existing repo conventions where possible.

Required semantics:

- read the canonical System maintainer entrypoint before meaningful cross-system work;
- component remains canonical implementation owner;
- meaningful changes evaluate System impact;
- release-intended revision must pass owner-native acceptance;
- exact accepted revision/evidence is handed to Distribution;
- breaking contract changes follow the coordinated contract law;
- component does not auto-write System/Distribution main by default;
- member/runtime files do not inherit these maintainer instructions.

### Acceptance criteria

- all Core owners have discoverable handoff rules;
- owner CI evidence is tied to exact candidate revision where technically possible;
- no duplicate global governance documents are copied into component repos;
- no component can claim member release solely from local CI.

### Evidence

To be recorded per repo.

### NEXT

**Slice 4.3 - Apply the proven handoff pattern to Wave 2/3 release-relevant repos.**

---

## Slice 4.3 - Extend handoff governance to Wave 2 and Wave 3 repos

**Status:** NOT STARTED  
**Dependencies:** 4.2  
**Adaptive tasks:** derive from Registry status and Wave 1 lessons; do not assume every future repo needs identical work

Use the Core-proven pattern for Agent/Full/future release-relevant repos registered by System.

Do not force identical file layouts; enforce identical semantics.

### Acceptance criteria

- every active first-class release-relevant repo is registered and has a valid handoff path;
- retired/experimental/external repos are explicitly classified rather than accidentally treated as shippable;
- repo-specific CI gaps are visible, not papered over;
- no broad cross-repo write authority is introduced.

### Evidence

To be recorded on completion.

### NEXT

**Phase 5 / Slice 5.1 - Add immutable candidate evidence snapshots and adoption gates to Distribution.**

---

# Phase 5 - Enforce safe composition and delivery in Distribution

**Phase size:** 4 slices

## Slice 5.1 - Add immutable candidate evidence snapshot and owner-adoption gates

**Status:** NOT STARTED  
**Dependencies:** 4.3  
**Adaptive tasks:** derive from audited Distribution candidate machinery; extend existing flow rather than parallel it

Integrate into existing Distribution candidate/release machinery rather than creating a parallel release database.

A candidate must bind the exact refs/evidence described in section 3.9.

### Acceptance criteria

- arbitrary component SHA cannot silently enter an admitted release;
- owner acceptance evidence is required where contract says so;
- candidate points to exact accepted component revisions;
- relevant Registry/State/System contract refs are frozen for qualification;
- bound input change forces re-evaluation/requalification.

### Evidence

To be recorded on completion.

### NEXT

**Slice 5.2 - Enforce member payload isolation across install/update/rollback.**

---

## Slice 5.2 - Enforce member payload isolation

**Status:** NOT STARTED  
**Dependencies:** 5.1  
**Adaptive tasks:** derive from the actual install/update/rollback payload paths found in Phase 1

Enforce deterministic member-facing payload boundaries for:

- fresh install;
- setup/reconcile;
- update;
- rollback;
- generated `AGENTS.md`/`CLAUDE.md`/`AI-VERSE.yaml` and adapters.

### Acceptance criteria

- maintainer governance, Registry/State/Ledger, tombstones, plans and qualification docs remain outside member install;
- future maintainer files do not enter member payload by default;
- user-owned files are not removed because of internal filename conventions;
- existing zero-loss preservation tests continue to pass.

### Evidence

To be recorded on completion.

### NEXT

**Slice 5.3 - Formalize promotion rings, whole-product qualification and emergency safety release.**

---

## Slice 5.3 - Formalize promotion and qualification

**Status:** NOT STARTED  
**Dependencies:** 5.2  
**Adaptive tasks:** derive from existing candidate/released/preservation mechanics and current release policy

Build on existing candidate/released/preservation mechanics.

Target conceptual progression:

```text
owner accepted
-> Distribution candidate
-> dogfood/canary/limited validation where supported
-> stable admitted release
```

Exact names/rings must follow audited Distribution mechanics rather than ceremony.

Integrate:

- component release descriptors;
- candidate evidence snapshot;
- whole-release preservation result;
- drift severity/scope;
- scoped repository freshness;
- compatibility/migration rules;
- clean-machine/composed qualification;
- emergency safety-release path.

### Acceptance criteria

- failed owner acceptance blocks candidate adoption;
- failed whole-product qualification blocks promotion;
- unrelated INFO/WARNING drift does not falsely block unrelated scope;
- blocking release-scope drift does block;
- break-glass never bypasses state safety, owner validation or whole-product qualification;
- `SYSTEM-SYNC-DEBT` from emergency use blocks later normal promotion until reconciled.

### Evidence

To be recorded on completion.

### NEXT

**Slice 5.4 - Implement durable reproducibility/release receipts.**

---

## Slice 5.4 - Implement reproducibility and durable release receipts

**Status:** NOT STARTED  
**Dependencies:** 5.3  
**Adaptive tasks:** derive from existing release receipts/evidence discovered earlier; do not duplicate durable data already stored canonically

For every admitted release persist a compact durable receipt containing enough immutable evidence to reconstruct the shipped software composition later.

At minimum where applicable:

- release ID;
- exact Distribution revision;
- exact component revisions/artifacts;
- component descriptor revisions;
- Registry/System contract refs used;
- relevant dependency locks/toolchain/runtime versions;
- migration/compatibility classification;
- qualification/preservation result refs;
- promotion channel/ring;
- previous known-good release reference;
- emergency/debt state if applicable.

### Acceptance criteria

- reconstructability does not depend solely on expiring CI artifacts;
- release receipt does not contain user-owned state/secrets;
- software reconstruction is explicitly separate from user-state rollback;
- old admitted release composition can be explained from durable evidence alone.

### Evidence

To be recorded on completion.

### NEXT

**Phase 6 / Slice 6.1 - Add cross-repo regression and evidence validation.**

---

# Phase 6 - Prove the whole repository network and close the program

**Phase size:** 3 slices

## Slice 6.1 - Add cross-repo regression and evidence validation

**Status:** NOT STARTED  
**Dependencies:** 5.4  
**Adaptive tasks:** derive from the invariants and actual implemented enforcement surfaces; do not create redundant tests

Automate regression scenarios including:

- sibling-owned defect cannot close with only Distribution evidence;
- owner CI failure blocks adoption;
- owner pass + Distribution qualification failure blocks promotion;
- wrong/older pinned owner ref blocks claimed inclusion;
- stale System versus newer accepted release becomes drift, not code rollback;
- newer unvalidated code does not rewrite System automatically;
- unregistered first-class repo is detected;
- stale watchdog is detected;
- breaking contract deletion is detected;
- candidate evidence snapshot drift forces requalification;
- member governance leakage fails;
- user-owned state survives update/rollback;
- durable release receipt validates against admitted composition.

### Acceptance criteria

- every permanent System invariant has an enforcement/evidence owner;
- cross-repo validation distinguishes unavailable evidence from failed evidence;
- validation fails closed where required;
- no secret/broad credential is introduced unnecessarily.

### Evidence

To be recorded on completion.

### NEXT

**Slice 6.2 - Run end-to-end qualification across all repository directions.**

---

## Slice 6.2 - Run end-to-end qualification

**Status:** NOT STARTED  
**Dependencies:** 6.1  
**Adaptive tasks:** derive from the implemented paths and any remaining drift/blockers at slice start

Run representative scenarios:

### A. Distribution-owned improvement

Distribution change -> Distribution tests -> System impact decision -> scoped refresh -> qualification -> release receipt -> clean member install.

### B. Component-originated improvement

Owner change -> owner acceptance -> System impact -> repository state -> Distribution adoption -> immutable candidate snapshot -> whole-product qualification -> promotion -> member install/update -> release receipt.

### C. Sibling defect discovered by Distribution

Distribution discovers -> routes owner -> owner fix/acceptance -> System sync -> Distribution adopts -> qualifies -> promotes -> member install/update.

### D. Stale canonical documentation

Use Purpose Context or equivalent: detect stale System wording -> verify accepted release reality -> synchronize System forward -> no regression of valid implementation.

### E. Breaking contract change

Owner introduces breaking interface/schema change -> local metadata/validation detects -> coordinated migration/version path required -> Distribution composes only accepted compatible set.

### F. Emergency safety release

Urgent safety fix -> owner validation + Distribution qualification remain mandatory -> bounded System sync debt recorded -> later normal promotion blocked until debt cleared.

For all scenarios verify preservation, member isolation, exact refs, drift handling, provenance and reconstructability.

### Acceptance criteria

- System, component repos, Distribution, Repository State and admitted release receipts agree on shipped truth;
- all directions work without duplicate ownership;
- member state survives;
- member-facing product remains clean;
- evidence is sufficient to diagnose/recover from a mistaken maintainer or AI decision.

### Evidence

To be recorded on completion.

### NEXT

**Slice 6.3 - Canonical closeout and program handoff.**

---

## Slice 6.3 - Canonical closeout and program handoff

**Status:** NOT STARTED  
**Dependencies:** 6.2  
**Adaptive tasks:** derive from actual remaining closeout debt; do not perform ceremonial changes with no evidence-backed need

Close only after all previous acceptance criteria pass.

Update as applicable:

- this plan;
- repository-network governance contract;
- System invariants;
- Repository Registry;
- Repository State schema/current state;
- generated Repository State Ledger;
- maintainer start-here;
- Blueprint/Living Spec/Product Intent/Changelog;
- architecture tombstones;
- component handoff docs;
- Distribution release/qualification docs;
- durable release receipts.

### Acceptance criteria

- all 20 slices COMPLETE with exact evidence;
- all rollout waves covered as required by Registry status;
- no duplicate source of truth introduced;
- no stale canonical regression path remains under the supported workflow;
- all admitted releases use accepted owner refs and whole-product qualification;
- member-isolation and zero-loss preservation remain satisfied;
- watchdog/registry/state/release evidence are operational and self-checking;
- program status becomes COMPLETE only now.

### Evidence

To be recorded on completion.

### NEXT

None. Program complete.

---

# Program Change Log

## 2026-10-12 - Adaptive discovery authority tightened

- Added an explicit boundary between adaptive execution and protected roadmap direction.
- Tasks and implementation techniques may adapt from evidence, but permanent laws, product intent, canonical ownership, phase/slice purpose, acceptance floors, safety requirements, major ordering and program denominator cannot be silently changed by self-discovery.
- Added `BLOCKED - PLAN AMENDMENT REQUIRED` for findings that would redirect protected program intent.
- Added a required evidence-backed `PLAN AMENDMENT PROPOSED` format.
- Added the non-degradation law: discovery may reduce unnecessary work but cannot reduce safety, ownership, preservation, validation, member-isolation or required evidence on its own authority.
- Changed roadmap self-correction into roadmap amendment: adaptive execution may propose directional changes but cannot approve them itself.
- Added plan-amendment fields to the evidence model and progress reporting.
- Tightened `docs/ADAPTIVE-IMPLEMENTATION-PLANNING-SKILL.md` with the same authority boundary.

## 2026-10-12 - Adaptive task discovery and reusable planning skill added

- Added `docs/ADAPTIVE-IMPLEMENTATION-PLANNING-SKILL.md` as the reusable method for future complex implementation plans.
- Kept phases/slices as stable outcome and acceptance milestones while making low-level task lists intentionally adaptive.
- Required each substantial slice to refresh relevant reality and derive/refine its task list at slice start rather than pre-guessing all future tasks.
- Added task eligibility rules to prevent speculative implementation work.
- Allowed evidence-backed task add/remove/split/merge/reorder with preserved history and explicit reasons.
- Kept overall percentage slice-based so task discovery cannot make program progress artificially move backward.
- Added task-level progress reporting for the current slice.
- Added roadmap self-correction when verified evidence proves a slice/phase itself is wrongly scoped or ordered; this is now constrained by the later amendment-authority rule above.
- Marked future slice task lists as adaptive rather than falsely complete today.

## 2026-10-12 - Program normalized into dependency-safe 20-slice execution sequence

- Increased denominator from 14 to 20 because the original slices had become overloaded after adding Registry, Repository State/Ledger, Watchdog, invariants, tombstones, compatibility governance, promotion, reproducibility and provenance.
- Preserved Slice 0.1 as the only completed slice. New progress is 1/20 = 5.0%.
- Reordered work into six execution phases: audit/normalize -> canonical System control plane -> System self-checking machinery -> component-owner integration -> Distribution enforcement -> end-to-end proof/closeout.
- Added mandatory before/after plan updates for every slice.
- Added mandatory user-facing progress reports with completed/total, current phase, phase progress, steps until next phase, percentage and next slice.
- Split static Registry truth from dynamic Repository State and generated Markdown ledger.
- Required machine-readable versioned governance formats.
- Replaced blanket full refreshes with scoped refreshes plus scheduled full watchdog scans.
- Added Git ancestry/exact-ref rules so dates are not mistaken for lineage authority.
- Added drift severity/scope so unrelated drift does not block unrelated releases.
- Added immutable candidate evidence snapshots to prevent moving branches from changing what was qualified.
- Explicitly reused/extensible existing Component Release Descriptor instead of inventing a second compatibility fingerprint format.
- Added durable release receipts so reproducibility does not depend on expiring CI logs/artifacts.
- Added bounded emergency safety-release semantics without bypassing owner validation, preservation or whole-product qualification.
- Added rollout waves so Core proves the pattern before Agent/Full ecosystem expansion.
- Separated permanent governance from this execution plan so Phase 2 creates the durable contracts and the plan remains an execution tracker.

## 2026-10-12 - Future-proof protection placement model added

- Added the rule: Define centrally. Enforce at the canonical owner. Verify again at composition.
- Added Repository Registry, Drift Watchdog, architecture tombstones, System invariants, compatibility metadata, promotion, reproducibility, no-silent-contract-deletion and decision/recovery provenance.

## 2026-10-12 - Repository State Ledger and non-regression guard added

- Added live/accepted/shipped/System-synchronized state distinction.
- Added freshness-before-trust and Purpose Context as the first stale-canonical regression fixture.

## 2026-10-12 - Component handoff and two-layer validation added

- Added component -> System and component -> Distribution handoffs.
- Added owner-native acceptance plus Distribution whole-product qualification.

## 2026-10-12 - Canonical owner routing added

- Added the rule that Distribution must not permanently substitute for sibling implementation owners.

## 2026-10-12 - Program created

- Created the canonical program and member-isolation direction.

---

# Current execution pointer

**Completed:** 1/20  
**Overall:** 5.0%  
**Phase:** Phase 1 - Audit and normalize current reality  
**Phase progress:** 0/3  
**Until Phase 2:** 3 slices  
**Next:** Slice 1.1 - Audit the live repository network and existing safety machinery  
**Next task:** not yet derived; generate from live Slice 1.1 evidence at slice start  
**Blockers/drift/amendments:** none recorded by the plan yet; Slice 1.1 must establish the evidence-backed baseline before implementation changes begin.
