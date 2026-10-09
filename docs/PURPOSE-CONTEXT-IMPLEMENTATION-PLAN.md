# AI-Verse Purpose Context Implementation Plan

**Status:** COMPLETE / ACCEPTED / CORE ADMITTED  
**Project:** Purpose Context / Telos-inspired trajectory layer  
**Canonical planning repo:** `aiverse-filmmakers/AI-Verse-System`  
**Primary implementation repo:** `aiverse-filmmakers/AI-Verse-OS`  
**Cross-owner repos:** `AI-Verse-Brain`, `AI-Verse-Data`, `AI-Verse-Memory`, and only the existing runtime/Dashboard owners when a slice proves they are required  
**Started:** 2026-10-06  
**Completed:** 2026-10-09  
**Final Core release:** `core-purpose-context-public-beta-2026-10-09`  
**Final completion record:** `docs/PURPOSE-CONTEXT-FINAL-COMPLETION.md`  
**Final execution/closure record:** `docs/PURPOSE-CONTEXT-EXECUTION-STATE.md`  
**External inspiration:** `danielmiessler/Telos` (MIT)  
**Parent intent:** `docs/PURPOSE-CONTEXT-TELOS-ADOPTION-PLAN.md`  
**Rule:** Update this file before and after every implementation slice. A slice is COMPLETE only when implementation, focused tests, exact repository refs, and acceptance evidence are recorded here.

> **Final-status note:** the per-slice `Status:` labels below are retained as historical planning-time markers from the original canonical plan. Authoritative executed-task state, exact evidence, admitted refs, and slice/phase closure are recorded in `docs/PURPOSE-CONTEXT-EXECUTION-STATE.md`, the individual closure/evidence documents, and `docs/PURPOSE-CONTEXT-FINAL-COMPLETION.md`. Purpose Context v1 is fully complete and admitted.

---

## 0. Mission

Build a first-class AI-Verse **Purpose Context** capability that lets an agent understand, when relevant:

- why the person/workspace is doing the work;
- what larger problem or desired outcome the work serves;
- the active mission/purpose;
- goals and their status;
- current challenges/blockers;
- strategies being used to address them;
- initiatives/projects executing those strategies;
- current work;
- KPIs/success measures and current values;
- risks where relevant;
- recent material changes that alter feasibility, priority, blockers, or direction;
- the exact provenance and owner of each claim.

The capability must support both:

- `operator` scope: personal/global trajectory;
- `workspace:<id>` scope: product/project/client/team/business trajectory.

Purpose Context is a **derived, rebuildable projection**, never a new canonical database or strategic owner.

The user-facing question it should answer is:

> **Where are we going, why are we doing this, what matters now, and how does the current work connect to the larger goal?**

---

## 0A. Telos concepts being adopted

The Telos repository is a conceptual/context framework, not a runtime implementation. AI-Verse adopts the useful model while preserving AI-Verse ownership and isolation laws.

The key trajectory chain to preserve is:

```text
Problems
  -> Mission
  -> Narratives
  -> Goals
  -> Challenges
  -> Strategies
  -> Initiatives / Projects
  -> Current Work
  -> Material Changes / Activity
```

Supporting context may include:

- KPIs / metrics;
- risks;
- team/resources;
- customers;
- infrastructure;
- budget/cost;
- historical lessons;
- current state.

Not every scope needs every field.

The critical Telos advantage is **explainable lineage of work**: a current task or initiative should be traceable upward to the strategy, goal, mission, and problem it serves.

---

## 0B. Non-negotiable architecture laws

1. **No new `AI-Verse-Telos` repository.**
2. **No new canonical Purpose database.**
3. **No canonical `TELOS.md` or `PURPOSE.md` file that can drift from owner state.**
4. **Purpose Context is read-only as a projection.** Durable writes always route to the canonical owner.
5. **No duplicate goals.** Brain or OS remains the strategic direction owner for each scope.
6. **No duplicate KPI truth.** Strategic KPI definitions may be Brain-owned; current measured values remain Data-owned where Data is the declared owner.
7. **No duplicate history/activity store.** Material changes are projected from existing owner-backed events/receipts/Data/Memory.
8. **No Memory promotion into current strategic authority.** Memory can inform/provide provenance but does not become the current owner.
9. **No cross-workspace leakage.** Purpose Context must preserve existing workspace isolation.
10. **No stale projection may overrule a current owner read.**
11. **No silent strategic mutation.** Mission, top-level goals, priority ordering, strategic constraints, or equivalent high-impact changes require the existing confirmation/authority path.
12. **The projection must be disposable.** Deleting any generated/cached Purpose view must not destroy canonical state.
13. **No mandatory rich corporate schema for small workspaces.** Rich fields are optional and relevance-driven.
14. **No automatic Core release mutation.** The currently admitted Core remains immutable; this work creates descendant component refs and, after full qualification, a new Core release.
15. **No feature expansion without demonstrated user value.** After runtime integration, Purpose Context must prove that it improves real strategic work without unacceptable token, latency, noise, or complexity overhead before mutation/UI/rich-workspace expansion continues.

---

## 0C. Canonical owner map

| Purpose field | Canonical owner / source rule |
|---|---|
| operator/workspace identity and scope | OS |
| current workspace/operator operational context | OS/current-context resolver |
| strategic direction ownership marker | OS/Brain direction ownership contract |
| mission/purpose | active strategic direction owner: Brain, or OS while OS still owns direction |
| goals / desired states / priorities | active strategic direction owner |
| strategies / initiatives / strategic constraints | active strategic direction owner |
| problems / challenges | Brain when strategic objects; may cite Data/Memory evidence |
| narratives | Brain when strategic belief/context; Memory only for historical evidence |
| KPI definitions / targets | Brain when strategic |
| current KPI values | Data or another explicitly declared current-truth owner |
| current structured operational state | Data / OS according to existing owner contract |
| historical lessons / provenance | Memory |
| recent material changes | derived from owner-backed events, receipts, Data changes, Goal changes, and Memory provenance |
| capabilities | Skills, only when relevant to a Purpose decision |
| live session/run state | existing runtime/Gateway owner |
| recurring cadence | Automations, only if later surfaced |
| multi-agent durable coordination | Multiple Bots, only if later surfaced |
| Dashboard | projection/UI only; never owner |

Any field added later must declare its owner before implementation.

---

## 0D. Scope model

Purpose Context uses existing AI-Verse strategic scopes only:

```text
operator
workspace:<id>
```

### Operator scope

Represents the person's/global operator trajectory. It may include:

- problems;
- mission;
- narratives;
- goals;
- challenges;
- strategies;
- initiatives;
- metrics;
- current state;
- recent material changes.

### Workspace scope

Represents the trajectory of a project/product/client/team/business/custom workspace.

Every purposeful workspace may use the basic chain:

```text
Purpose -> Goals -> Challenges -> Strategies -> Initiatives -> Current Work
```

Richer workspace contexts may additionally expose:

- KPIs;
- risks;
- team/resources;
- customers;
- infrastructure;
- budget/cost;
- operational metrics.

These fields remain optional. No workspace should be populated with meaningless empty corporate structure merely to satisfy a template.

### Isolation law

`workspace:A` must not silently read Purpose state from `workspace:B`.

Cross-scope relationships must be explicit, provenance-bearing, and allowed by existing workspace isolation rules.

---

## 0E. Purpose Context v1 conceptual envelope

The exact serialization must be frozen in Phase 2, but the implementation target is equivalent to:

```yaml
schema_version: 1
scope: workspace:ai-verse
scope_kind: workspace

identity:
  name: AI-Verse
  type: product

problems:
  - id: ...
    statement: ...
    source_refs: [...]

purpose:
  mission: ...
  desired_outcomes: [...]

narratives:
  - id: ...
    statement: ...
    source_refs: [...]

goals:
  - id: ...
    objective: ...
    status: ...
    completion_contract: ...
    serves: [...]
    source_refs: [...]

challenges:
  - id: ...
    statement: ...
    blocks: [...]
    source_refs: [...]

strategies:
  - id: ...
    statement: ...
    addresses: [...]
    advances: [...]
    source_refs: [...]

initiatives:
  - id: ...
    title: ...
    status: ...
    executes: [...]
    serves: [...]
    addresses: [...]
    source_refs: [...]

kpis:
  - id: ...
    definition: ...
    target: ...
    current_value: ...
    trend: ...
    definition_source_ref: ...
    value_source_ref: ...

risks:
  - id: ...
    statement: ...
    severity: ...
    affects: [...]
    source_refs: [...]

current_state:
  - ...

current_work:
  - ...

recent_material_changes:
  - event: ...
    effect: ...
    source_ref: ...

trajectory:
  - from: ...
    relation: ...
    to: ...

provenance:
  generated_at: ...
  owner_refs: [...]
  freshness: ...
```

All generated IDs/refs and relation semantics must be deterministic or canonical-owner-backed where required for stable explainability.

---

## 0F. Minimum trajectory relations

Phase 2 must either adopt or deliberately revise a bounded relation vocabulary. The starting proposal is:

- `addresses` — a mission/strategy/initiative addresses a problem/challenge;
- `serves` — a goal/initiative serves a higher-level mission/goal;
- `advances` — a strategy/current work advances a goal;
- `blocks` — a challenge/risk blocks or impedes a goal/initiative;
- `executes` — an initiative/project executes a strategy;
- `measures` — a KPI measures a goal/outcome;
- `affects` — a risk/material change affects a goal/initiative/strategy;
- `supersedes` — a confirmed strategic object replaces an older object when the owner already supports supersession.

No arbitrary free-form edge types should be admitted without a schema change.

---

## 0G. Current immutable Core starting baseline

Purpose Context development begins **after** the repaired Core baseline and must advance from it.

Current admitted Core release:

`core-repaired-public-beta-2026-10-06`

Protected component refs:

- OS: `e74a4e05b1f891e6f871f34a298bf10363a11d88`
- Brain: `7c77b053df627e61b3d7f11d029500ab61095c9c`
- Memory: `b0cae8cd8da38aa657fbc736c575177aa75e5ec7`
- Skills: `afde5c06307fba7d074de2929c2eb6c3dc6bdab8`
- Data: `6e8781ff1dcd96a35dfb27868bd60605361483d0`

Distribution lineage policy: `append-only-same-or-descendant`.

Any changed Core component used by the eventual Purpose Context release must be the same ref or a Git descendant of this baseline. The current release is never edited in place.

---

## 0H. Status vocabulary and execution discipline

Allowed slice states:

- `NOT STARTED`
- `IN PROGRESS`
- `BLOCKED`
- `COMPLETE`

Every slice must record:

- affected repo(s);
- exact starting refs inspected;
- exact files/interfaces changed;
- ownership decision;
- scope/isolation decision;
- acceptance criteria;
- focused tests;
- cross-owner tests when applicable;
- exact commit/PR/workflow evidence;
- explicit NEXT slice.

### Hard rule

Do not jump directly to Dashboard/UI or a giant end-to-end implementation. Build and qualify each owner contract first, then compose them.

---

# Phase 0 - Persistent execution plan

## Slice 0.1 - Create canonical implementation plan

**Status:** COMPLETE  
**Repos:** AI-Verse-System  
**Dependencies:** repaired Core baseline admitted

### Tasks

- create this persistent execution plan;
- connect it to the accepted Telos adoption intent;
- record the repaired Core baseline;
- represent every implementation area as bounded phases/slices;
- make final full-Core requalification mandatory;
- ensure another agent can resume work from this document without the original chat.

### Acceptance criteria

- the plan exists in `AI-Verse-System/docs/`;
- architecture laws are explicit;
- scope model is explicit;
- Telos trajectory model is explicit;
- owner boundaries are explicit;
- all planned repos are bounded by owner responsibilities;
- no implementation changes occur before Phase 1 audits the current owner interfaces;
- final Core requalification/admission is represented as a hard gate.

### Evidence

- initial plan commit: `63ae95ab101ab693ed368ba474fec7915a831a81`
- merged planning PR: `#189`
- merge commit: `b0b4a356ee33d86161e4ec9b3a6f9ed95b958c8e`
- canonical path: `docs/PURPOSE-CONTEXT-IMPLEMENTATION-PLAN.md`

### NEXT

**Slice 1.1 - Fresh audit of current exact Core owner interfaces.**

---

# Phase 1 - Fresh owner/interface audit before implementation

## Slice 1.1 - Audit current OS scope, current-context, workspace, and direction-owner contracts

**Status:** NOT STARTED  
**Repos:** AI-Verse-OS  
**Dependencies:** 0.1

### Tasks

Inspect the current descendant of the repaired Core baseline, including:

- `operator` and `workspace:<id>` scope validation;
- workspace isolation contract;
- `WORKSPACE.yaml` schema/extension rules;
- current-context resolver;
- strategic direction ownership marker;
- OS-owned strategic files/sections;
- Brain-owned generated direction views;
- write assertions and handover/handback behavior;
- current context-ladder/relevance surfaces if OS owns them;
- tests and CI touching direction/current-context/workspaces.

### Acceptance criteria

- write a source-backed map of every OS interface Purpose Context may consume;
- identify which reads are safe/public vs internal/private;
- identify whether optional `purpose_context` workspace metadata is needed or whether auto-discovery is sufficient;
- make no behavior changes yet.

### NEXT

**Slice 1.2 - Audit Brain strategic model and read surfaces.**

## Slice 1.2 - Audit Brain strategic model and direction objects

**Status:** NOT STARTED  
**Repos:** AI-Verse-Brain  
**Dependencies:** 1.1

### Tasks

Inspect:

- Brain object kinds;
- intent / goal / objective / gap / opportunity / initiative / strategy_rule semantics;
- goal API;
- direction service;
- direction ownership integration;
- source/evidence refs;
- supersession/versioning;
- query/list/read surfaces;
- current strategy rollback behavior;
- tests/CI.

### Acceptance criteria

Produce a mapping from Telos concepts to existing Brain objects:

```text
Problem -> ?
Mission -> ?
Narrative -> ?
Goal -> ?
Challenge -> ?
Strategy -> ?
Initiative -> ?
```

For every concept, decide one of:

- use existing canonical Brain object;
- derive from existing Brain objects;
- add a new canonical Brain kind because semantics genuinely do not fit;
- exclude from v1.

Do not create fake one-to-one mappings merely to match Telos wording.

### NEXT

**Slice 1.3 - Audit Data, Memory, runtime/context-ladder, and Dashboard owner surfaces.**

## Slice 1.3 - Audit Data, Memory, runtime, and Dashboard integration surfaces

**Status:** NOT STARTED  
**Repos:** AI-Verse-Data, AI-Verse-Memory, and current runtime/Dashboard owner repos only as discovered  
**Dependencies:** 1.2

### Tasks

Audit current supported read interfaces for:

- Data current KPI values and operational truth;
- Data freshness/provenance metadata;
- Memory recent changes/history/provenance queries;
- runtime/context-ladder injection points;
- Dashboard read/write boundaries;
- exact workspace scoping behavior in each component.

### Acceptance criteria

- every planned integration has a declared existing or required new owner API;
- no Purpose code is allowed to read private storage formats directly when a stable owner API can be added instead;
- exact repos required for P1-P5 are known before implementation begins.

### NEXT

**Slice 2.1 - Freeze Purpose Context v1 schema and semantics.**

---

# Phase 2 - Freeze the Purpose Context v1 contract

## Slice 2.1 - Versioned envelope schema

**Status:** NOT STARTED  
**Repos:** AI-Verse-System + AI-Verse-OS  
**Dependencies:** Phase 1 complete

### Tasks

Freeze:

- `schema_version`;
- supported scope kinds;
- required vs optional fields;
- provenance format;
- freshness format;
- canonical ref format;
- deterministic ordering rules;
- unknown/unavailable field behavior;
- bounded size/budget rules;
- rebuildability contract.

### Acceptance criteria

- a versioned schema exists;
- absent optional fields are distinguishable from unknown/unavailable owner reads;
- stale owner reads are represented, not silently treated as current;
- no generated field can become independently editable.

### NEXT

**Slice 2.2 - Freeze trajectory relationship semantics.**

## Slice 2.2 - Trajectory graph contract

**Status:** NOT STARTED  
**Repos:** AI-Verse-System + AI-Verse-Brain + AI-Verse-OS  
**Dependencies:** 2.1

### Tasks

Freeze:

- relation vocabulary;
- allowed source/target kinds;
- cycle behavior;
- missing-parent behavior;
- supersession behavior;
- orphan initiative/current-work behavior;
- explain traversal rules;
- deterministic graph ordering.

### Acceptance criteria

The contract can answer, from owner-backed refs:

> Why are we doing this current work?

by tracing upward through the available chain without inventing missing relationships.

### NEXT

**Slice 2.3 - Freeze operator/workspace profile behavior.**

## Slice 2.3 - Operator and workspace profile rules

**Status:** NOT STARTED  
**Repos:** AI-Verse-System + AI-Verse-OS  
**Dependencies:** 2.2

### Tasks

Define:

- operator default shape;
- workspace default/basic shape;
- rich workspace optional fields;
- auto-detection rules;
- whether `WORKSPACE.yaml` gets an optional `purpose_context` block;
- what happens when Purpose is disabled/irrelevant;
- explicit cross-scope relationship rules.

### Acceptance criteria

- tiny workspaces do not receive fake corporate structure;
- rich workspaces can expose KPIs/risks/resources/etc. without changing the core engine;
- workspace isolation remains fail-closed.

### NEXT

**Slice 3.1 - Implement Brain strategic snapshot/read contract.**

---

# Phase 3 - Brain canonical strategic read surface

## Slice 3.1 - Purpose/strategy snapshot API

**Status:** NOT STARTED  
**Repos:** AI-Verse-Brain  
**Dependencies:** Phase 2 complete

### Target public surface

Final naming is confirmed during implementation, but the intended capability is equivalent to:

```bash
ai-verse-brain purpose-snapshot . --scope operator --json
ai-verse-brain purpose-snapshot . --scope workspace:ai-verse --json
```

### Tasks

- expose confirmed/current strategic objects only;
- expose source/evidence refs;
- expose relationships needed by the trajectory graph;
- preserve direction-owner authority;
- expose unavailable/partial state explicitly;
- avoid leaking internal storage layout into OS.

### Acceptance criteria

- read-only;
- stable JSON contract;
- scope-safe;
- no strategic write side effects;
- no duplicate Purpose store;
- existing Brain direction/goal tests remain green.

### NEXT

**Slice 3.2 - Add only genuinely missing Brain semantics.**

## Slice 3.2 - Missing strategic semantics, if required

**Status:** NOT STARTED  
**Repos:** AI-Verse-Brain  
**Dependencies:** 3.1

### Rule

Do this slice only if Phase 1 proved that a Telos concept required for v1 cannot be represented correctly by existing Brain semantics.

### Tasks

If required:

- add the minimal new canonical kind/field/relationship;
- define lifecycle/status rules;
- define confirmation authority;
- define supersession/versioning;
- migrate nothing silently;
- add exhaustive unit tests.

If no new canonical semantics are required, mark this slice COMPLETE with evidence explaining why.

### NEXT

**Slice 4.1 - Implement OS Purpose Context composer.**

---

# Phase 4 - OS read-only Purpose Context composer

## Slice 4.1 - Core composer and CLI

**Status:** NOT STARTED  
**Repos:** AI-Verse-OS  
**Dependencies:** Phase 3 complete

### Target files/surfaces

Equivalent to:

```text
system/architecture/purpose-context.md
system/schemas/purpose-context.schema.json
scripts/purpose-context-core.mjs
scripts/purpose-context.mjs
```

### Target CLI

```bash
node scripts/purpose-context.mjs read --scope operator
node scripts/purpose-context.mjs read --scope workspace:ai-verse
```

### Tasks

- resolve scope;
- use ownership-aware current-context reads;
- read strategic direction only through the declared owner path;
- compose v1 envelope;
- preserve exact refs/provenance;
- deterministic ordering;
- bounded output;
- no cache required for v1;
- fail closed on malformed ownership records.

### Acceptance criteria

- `operator` works;
- `workspace:<id>` works;
- deleting all generated Purpose output changes no canonical state;
- repeated reads with unchanged owner state are semantically stable;
- no direct Brain private-file parsing from OS;
- no new editable Purpose store exists.

### NEXT

**Slice 4.2 - Workspace profile and isolation behavior.**

## Slice 4.2 - Workspace Purpose integration

**Status:** NOT STARTED  
**Repos:** AI-Verse-OS  
**Dependencies:** 4.1

### Tasks

- implement basic/auto/rich profile behavior as frozen in 2.3;
- add optional workspace configuration only if approved in Phase 2;
- ensure no cross-workspace scans;
- support explicit parent/related scope refs only through declared rules;
- test missing/deleted workspaces and symlink/path boundary attacks.

### Acceptance criteria

- workspace A cannot leak workspace B data;
- a simple workspace remains simple;
- a rich workspace may expose optional corporate-style fields;
- user-created workspace state remains user-owned and compatible with existing template rules.

### NEXT

**Slice 4.3 - Trajectory explain endpoint.**

## Slice 4.3 - Explainable trajectory graph

**Status:** NOT STARTED  
**Repos:** AI-Verse-OS + AI-Verse-Brain if required by final graph contract  
**Dependencies:** 4.2

### Target capability

Equivalent to:

```bash
node scripts/purpose-context.mjs explain \
  --scope workspace:ai-verse \
  --ref initiative:<id>
```

### Tasks

- traverse only explicit/canonical relationships;
- show path from current work/initiative toward goal/mission/problem where available;
- expose missing links rather than hallucinating them;
- include owner/source refs for each hop;
- prevent graph cycles from causing unbounded traversal.

### Acceptance criteria

The system can explain:

```text
Current work
 -> executes Strategy S
 -> addresses Challenge C
 -> advances Goal G
 -> serves Mission M
 -> addresses Problem P
```

only when those relationships are present in owner-backed state.

### NEXT

**Slice 5.1 - Add Data current-value adapter.**

---

# Phase 5 - Data-backed current truth and KPIs

## Slice 5.1 - KPI/current-state read contract

**Status:** NOT STARTED  
**Repos:** AI-Verse-Data + AI-Verse-OS  
**Dependencies:** Phase 4 complete

### Tasks

- expose a bounded Data read surface for Purpose-referenced current values;
- preserve scope and provenance;
- include freshness/timestamp;
- distinguish missing value, stale value, and zero/false values;
- do not copy Data rows into Brain or OS as canonical state.

### Acceptance criteria

Purpose can combine:

```text
Brain: KPI definition / target
Data: current measured value
```

without confusing ownership.

### NEXT

**Slice 5.2 - Current-state composition and failure behavior.**

## Slice 5.2 - Current operational truth projection

**Status:** NOT STARTED  
**Repos:** AI-Verse-Data + AI-Verse-OS  
**Dependencies:** 5.1

### Tasks

- project only Purpose-relevant current state;
- add stale/unavailable diagnostics;
- ensure Data outage does not cause fallback to stale generated Purpose values;
- add exact-source descent tests.

### NEXT

**Slice 6.1 - Add Memory material-change adapter.**

---

# Phase 6 - Memory-backed history and material changes

## Slice 6.1 - Bounded history/provenance read

**Status:** NOT STARTED  
**Repos:** AI-Verse-Memory + AI-Verse-OS  
**Dependencies:** Phase 5 complete

### Tasks

- expose bounded recent history relevant to Purpose;
- preserve Memory provenance;
- separate historical evidence from current authority;
- avoid dumping raw memory into every Purpose read.

### Acceptance criteria

- Memory can explain how/why state changed;
- Memory cannot override current Brain/Data/OS owner state;
- workspace Memory remains workspace-isolated.

### NEXT

**Slice 6.2 - Material-change classifier/projection.**

## Slice 6.2 - Material changes

**Status:** NOT STARTED  
**Repos:** AI-Verse-OS + AI-Verse-Memory + Data/Brain only as required by owner events  
**Dependencies:** 6.1

### Materiality definition

A change is Purpose-material when it changes at least one of:

- goal status;
- priority;
- feasibility;
- blocker/challenge state;
- strategy validity;
- risk;
- KPI trend/threshold;
- initiative status;
- scope/direction ownership.

### Acceptance criteria

- raw event spam is excluded;
- each material change has an owner-backed source ref;
- a newer material fact can invalidate or alter the relevance of an older goal/strategy in the projection without rewriting historical evidence.

### NEXT

**Slice 7.1 - Integrate Purpose Context into the relevance/context ladder.**

---

# Phase 7 - Agent/runtime context-ladder integration

## Slice 7.1 - Relevance gate

**Status:** NOT STARTED  
**Repos:** exact runtime/context-ladder owner determined in Phase 1; OS always participates as Purpose composer  
**Dependencies:** Phase 6 complete

### Tasks

Add bounded Purpose loading for questions/tasks such as:

- what should I work on next?;
- why are we doing this?;
- which project should take priority?;
- does this still serve our goal?;
- what changed?;
- what is blocking this goal?;
- compare two strategic options.

Avoid Purpose loading for irrelevant micro-tasks such as simple file renames or deterministic formatting operations.

### Acceptance criteria

- relevance rule is deterministic/testable enough to avoid always-on bloat;
- Purpose envelope has a token/size budget;
- exact owner evidence can be fetched when a sensitive claim requires it;
- ordinary agent turns do not gain unnecessary cross-owner reads.

### NEXT

**Slice 7.2 - Freshness, budget, and fallback behavior.**

## Slice 7.2 - Context budget/freshness policy

**Status:** NOT STARTED  
**Dependencies:** 7.1

### Tasks

- define maximum envelope size;
- define truncation priority;
- preserve trajectory-critical fields ahead of optional rich context;
- define refresh conditions;
- define unavailable-owner behavior;
- ensure stale cached UI/output cannot outrank a fresh owner read.

### Acceptance criteria

- a trivial deterministic task produces zero Purpose owner reads;
- a strategic task loads Purpose only after the relevance gate passes;
- no unrelated workspace is read as a side effect of Purpose loading;
- Purpose-unavailable fallback preserves ordinary task execution without silently substituting stale Purpose state;
- token/size and freshness limits are measurable and testable.

### NEXT

**Slice 7.3 - Prove real user value before feature expansion.**

## Slice 7.3 - Real-world Purpose Context value gate

**Status:** NOT STARTED  
**Repos:** all repos participating in the Phase 7 composed path  
**Dependencies:** 7.2

### Purpose

This is a hard product-value gate, not a cosmetic review. Purpose Context must prove that it materially improves real agent behavior before AI-Verse invests in mutation workflows, rich corporate extensions, or Dashboard surfaces.

### Evaluation method

Run representative `operator` and `workspace:<id>` scenarios both:

- **with Purpose Context enabled**; and
- **with Purpose Context absent/disabled** where a fair comparison is possible.

Use the same underlying canonical owner state and comparable prompts/tasks. Record concrete examples, output differences, context size, owner reads, and observed latency/cost where measurable.

### Required value proofs

Purpose Context should demonstrate meaningful improvement in several of these areas without material regressions elsewhere:

1. **Less repeated explanation** — the user does not need to restate mission, active goals, blockers, or recent strategic changes that canonical owners already know.
2. **Better next-action decisions** — answers to “what should I work on next?” use current goal/priority/blocker/strategy context instead of nearest-TODO heuristics.
3. **Better prioritization** — competing projects/options are compared against active purpose, goals, constraints, current state, and material changes.
4. **Better blocker awareness** — the agent notices when a challenge or material event changes feasibility or invalidates an older strategy.
5. **Better explainability** — “why are we doing this?” can be answered through owner-backed trajectory relations rather than post-hoc narrative invention.
6. **Better continuity across sessions** — strategic orientation survives session boundaries through owner-backed context rather than chat-history dependence.
7. **No regression on irrelevant work** — micro-tasks remain fast, focused, and free of irrelevant Purpose context.
8. **Acceptable token overhead** — Purpose is bounded and does not consume a disproportionate share of the context window.
9. **Acceptable latency/cost overhead** — strategic benefit is not purchased with unreasonable extra owner reads or model/runtime delay.
10. **No noticeable context-noise increase** — Purpose improves decisions instead of distracting the model with broad but irrelevant strategic data.

### Mandatory anti-bloat measurements

At minimum record and compare:

- Purpose owner-read count per scenario;
- Purpose envelope size/tokens or equivalent serialized size;
- whether unrelated workspaces were touched;
- whether a trivial task loaded Purpose at all;
- whether the agent still completed the task when Purpose was unavailable;
- latency/cost delta when the runtime can measure it;
- qualitative decision-quality delta using predefined scenarios rather than cherry-picked examples.

### Gate outcomes

Record exactly one outcome:

- **VALUE PROVEN** — clear strategic benefit with acceptable overhead. Proceed to Phase 8.
- **PARTIALLY PROVEN** — useful signal exists but overhead, relevance, schema, or retrieval behavior needs simplification. Return to the relevant Phase 4-7 slice, revise, and rerun Slice 7.3 before expansion.
- **NOT PROVEN** — no sufficient benefit over the existing system. Stop Purpose expansion; do not build Phases 8-10 merely because they are planned. Preserve useful minimal pieces only if independently justified.

### Acceptance criteria

- real operator/workspace scenarios are recorded;
- with/without-Purpose comparisons exist where technically fair;
- at least one strategic planning/prioritization scenario shows a clear improvement attributable to Purpose Context;
- trivial-task behavior shows no unnecessary Purpose loading;
- token/size overhead is within the Phase 7 budget;
- no workspace-isolation or authority regression appears;
- outcome is explicitly recorded as `VALUE PROVEN`, `PARTIALLY PROVEN`, or `NOT PROVEN`;
- Phase 8 cannot begin unless the outcome is `VALUE PROVEN`.

### NEXT

If `VALUE PROVEN`: **Slice 8.1 - Implement controlled mutation proposals.**  
If `PARTIALLY PROVEN`: return to the identified Phase 4-7 slice and rerun 7.3.  
If `NOT PROVEN`: stop expansion and record the bounded retained/deferred scope.

---

# Phase 8 - Owner-routed strategic mutation proposals

## Slice 8.1 - Detect and classify proposed strategic changes

**Status:** NOT STARTED  
**Repos:** OS + Brain and existing confirmation/runtime owner as required  
**Dependencies:** Slice 7.3 outcome = `VALUE PROVEN`

### High-impact changes

At minimum:

- mission/purpose;
- top-level goals;
- priority ordering;
- values;
- strategic constraints;
- replacement/deletion of durable strategic intent;
- direction-owner transfer.

### Tasks

- detect when user intent implies a durable strategic change;
- generate a proposed owner mutation;
- never mutate the Purpose projection itself;
- route by current direction owner;
- require explicit confirmation according to existing law.

### NEXT

**Slice 8.2 - Idempotent application and receipts.**

## Slice 8.2 - Mutation execution safety

**Status:** NOT STARTED  
**Dependencies:** 8.1

### Tasks

- preserve operation IDs/idempotency;
- emit owner-backed receipts;
- rebuild Purpose after successful mutation;
- prove failed/interrupted writes cannot leave Purpose as a second truth store;
- preserve handover/handback rules.

### Acceptance criteria

- repeated confirmation cannot create duplicate goals/intent;
- rejected proposals create no canonical change;
- Brain outage does not silently return authority to OS;
- Purpose immediately reflects the canonical owner after successful change.

### NEXT

**Slice 9.1 - Complete rich workspace extensions.**

---

# Phase 9 - Optional rich workspace / corporate-style extensions

## Slice 9.1 - Risks and resource context

**Status:** NOT STARTED  
**Repos:** owner repos discovered in Phase 1; OS projection only  
**Dependencies:** Phase 8 complete + Slice 7.3 `VALUE PROVEN`

### Tasks

Add optional, owner-backed support for relevant workspace types:

- risks;
- team/resources;
- customers;
- infrastructure;
- budget/cost;
- project/initiative operational status.

### Rule

Do not invent canonical owners merely to copy every field from `corporate_telos.md`. If an AI-Verse owner does not exist and the field is not required for v1, leave it unsupported/optional rather than creating a parallel store.

### Acceptance criteria

- rich fields appear only when owner-backed and relevant;
- basic workspaces remain lightweight;
- no corporate-only assumptions leak into operator or simple project scopes.

### NEXT

**Slice 10.1 - Product/Dashboard Purpose view.**

---

# Phase 10 - Product surface / Dashboard

## Slice 10.1 - Read-only Purpose view

**Status:** NOT STARTED  
**Repos:** current Dashboard/product-shell owner + OS  
**Dependencies:** Phase 9 complete + Slice 7.3 `VALUE PROVEN`

### Target UX

Show, when available:

- mission/purpose;
- active goals;
- current trajectory;
- blockers/challenges;
- strategies/initiatives;
- KPIs;
- risks;
- current work;
- recent material changes;
- “Why does this exist?” / explain links;
- source/freshness diagnostics where useful.

### Acceptance criteria

- Dashboard is a projection only;
- no private local Purpose database;
- refresh reads owner-backed state;
- missing owners are shown as unavailable rather than replaced by stale local data.

### NEXT

**Slice 10.2 - Owner-routed editing surface.**

## Slice 10.2 - Controlled edits from UI

**Status:** NOT STARTED  
**Dependencies:** 10.1 + Phase 8

### Tasks

- allow UI to propose owner-routed changes;
- show confirmation for high-impact strategic changes;
- show canonical owner outcome after application;
- never write directly to a Dashboard Purpose model.

### NEXT

**Slice 11.1 - Whole capability security/isolation/rebuild audit.**

---

# Phase 11 - Purpose Context hardening and independent acceptance

## Slice 11.1 - Rebuildability and stale-state audit

**Status:** NOT STARTED  
**Repos:** all changed repos  
**Dependencies:** Phases 3-10 complete

### Required proofs

- delete all generated Purpose views/caches -> canonical state remains intact;
- restart -> same owner-backed Purpose projection can be rebuilt;
- no duplicate Purpose state appears after repeated setup/restart;
- stale projection cannot overrule fresh owner state;
- partial owner outage is represented explicitly.

### NEXT

**Slice 11.2 - Scope/isolation/security audit.**

## Slice 11.2 - Scope and security boundaries

**Status:** NOT STARTED  
**Dependencies:** 11.1

### Required tests

- operator scope isolation;
- workspace A cannot leak workspace B;
- symlink/path escape attempts fail closed;
- malformed ownership records fail closed;
- Brain-owned direction never falls back to frozen OS strategy;
- Data/Memory reads remain within allowed scope;
- exact-source descent respects owner permissions;
- no Purpose surface grants additional action permissions.

### NEXT

**Slice 11.3 - End-to-end semantic acceptance.**

## Slice 11.3 - Purpose/trajectory acceptance scenarios

**Status:** NOT STARTED  
**Dependencies:** 11.2

### Required scenarios

1. operator with OS-owned strategic direction;
2. operator with Brain-owned strategic direction;
3. simple workspace using only basic trajectory fields;
4. rich product/business workspace with KPI/risk/current-state context;
5. two isolated workspaces with conflicting goals;
6. material event closes a blocker;
7. material event invalidates the feasibility of a strategy;
8. Data value becomes stale/unavailable;
9. Memory contains old history conflicting with current Brain/Data truth;
10. high-impact goal change proposed but not confirmed;
11. high-impact goal change confirmed and Purpose rebuilt;
12. explain trajectory contains a missing relationship and reports the gap instead of inventing it.

### Acceptance criteria

All scenarios pass with exact provenance and no ownership violation.

### NEXT

**Phase 12 - Full Core and composed-system requalification.**

---

# Phase 12 - Full Core requalification and new release admission

This phase is mandatory even if every focused Purpose test is green.

The repaired Core release remains unchanged. Purpose Context produces a **new descendant Core candidate**.

## Slice 12.1 - Freeze exact candidate refs

**Status:** NOT STARTED  
**Repos:** Distribution + every changed Core repo  
**Dependencies:** Phase 11 complete + Slice 7.3 `VALUE PROVEN`

### Tasks

- record exact final descendant refs for OS/Brain/Memory/Data and unchanged refs for Skills if Skills is untouched;
- verify each changed protected component is same-or-descendant of `core-repaired-public-beta-2026-10-06`;
- freeze dependency locks required by candidate refs;
- do not qualify against moving branch heads.

### NEXT

**Slice 12.2 - Rerun all changed-repo test suites.**

## Slice 12.2 - Component tests

**Status:** NOT STARTED  
**Dependencies:** 12.1

### Required minimum

- full OS tests;
- full Brain tests;
- full Memory tests if changed;
- full Data tests if changed;
- Skills tests if Skills changed;
- all new Purpose tests;
- all existing direction-owner/current-context/workspace-isolation regressions.

### NEXT

**Slice 12.3 - Full Core/composed acceptance.**

## Slice 12.3 - Cross-platform Core qualification

**Status:** NOT STARTED  
**Repos:** ai-verse-distribution + changed component repos  
**Dependencies:** 12.2

### Required qualification

Rerun the full currently applicable Core stack against the **same exact candidate refs**, including at minimum:

- Distribution CI;
- Core Lineage Guard;
- Clean Machine Core Acceptance on Linux;
- Clean Machine Core Acceptance on macOS;
- Clean Machine Core Acceptance on Windows;
- member/project bootstrap acceptance on Linux;
- member/project bootstrap acceptance on macOS;
- member/project bootstrap acceptance on Windows;
- OS↔Brain direction/ownership contract tests;
- workspace isolation tests;
- Data/Memory integration tests used by Purpose Context;
- context-ladder/runtime integration tests;
- clean restart/rebuild tests;
- composed cross-system acceptance affected by changed refs;
- Agent/composed release checks too if implementation touched Gateway/runtime or any Agent-profile component.

### Hard rule

Do not treat separate green runs from different component SHA combinations as release evidence. Final qualification must correspond to one frozen candidate set.

### NEXT

**Slice 12.4 - Independent final review and release admission.**

## Slice 12.4 - Final independent review

**Status:** NOT STARTED  
**Dependencies:** 12.3

### Review questions

- Did Purpose Context introduce any second source of truth?
- Can any generated state become stronger than owner state?
- Can one workspace leak another workspace's Purpose?
- Can Memory override current truth?
- Can Dashboard mutate strategy without owner routing?
- Can high-impact changes bypass confirmation?
- Can stale KPI/current-state values appear current?
- Can a trajectory edge be hallucinated or inferred without being marked as such?
- Did Purpose Context actually improve strategic agent behavior enough to justify its runtime/context cost?
- Do trivial tasks remain free of unnecessary Purpose reads?
- Did any Core component regress from the repaired baseline?
- Are all final refs exact and immutable?

### NEXT

**Slice 12.5 - Admit new Core release.**

## Slice 12.5 - Distribution admission

**Status:** NOT STARTED  
**Dependencies:** 12.4 accepted

### Tasks

- create a new Core release entry; do not modify `core-repaired-public-beta-2026-10-06`;
- set lineage parent to the then-current Core release according to Distribution rules;
- include exact candidate refs;
- include qualification evidence;
- preserve rollback/update policy intentionally;
- run final same-head Distribution/Core Lineage validation;
- merge only after all final same-head checks are green.

### Acceptance criteria

Purpose Context is considered **Core-complete** only when:

1. the new descendant Core release is admitted;
2. all protected component lineage checks pass;
3. Linux/macOS/Windows clean-machine and bootstrap acceptance pass;
4. Purpose-specific semantic/isolation/rebuild tests pass;
5. the Slice 7.3 value gate is `VALUE PROVEN` with acceptable overhead;
6. no owner contract is weakened;
7. the final exact release refs and evidence are recorded in this plan.

---

# Phase 13 - Post-admission documentation and operational handoff

## Slice 13.1 - Update architecture/user docs

**Status:** NOT STARTED  
**Dependencies:** 12.5

### Tasks

- update `PURPOSE-CONTEXT-TELOS-ADOPTION-PLAN.md` status from intent to implemented/admitted as appropriate;
- document CLI/API usage;
- document operator vs workspace behavior;
- document optional rich workspace fields;
- document explain/trajectory behavior;
- document mutation confirmation behavior;
- document the measured user-value/anti-bloat result from Slice 7.3;
- record final Core release ID and exact refs.

### NEXT

**Slice 13.2 - Close implementation plan.**

## Slice 13.2 - Final closure

**Status:** COMPLETE  
**Dependencies:** 13.1

### Completion statement must include

- final Core release ID;
- exact OS/Brain/Memory/Skills/Data refs;
- all final qualification workflow IDs;
- final Purpose schema version;
- supported scope/profile behavior;
- Slice 7.3 value-gate outcome and measured overhead;
- known limitations/deferred fields;
- any post-v1 follow-up work.

All eight items are recorded in `docs/PURPOSE-CONTEXT-FINAL-COMPLETION.md`. This implementation plan is COMPLETE.

---

# Global acceptance criteria

Purpose Context is not complete until all of the following are true:

1. no new canonical Purpose/Telos database exists;
2. every projected field resolves to a declared owner or is explicitly marked unavailable/derived;
3. `operator` and `workspace:<id>` are both supported;
4. workspace isolation is proven;
5. simple workspaces do not require rich corporate fields;
6. rich workspaces can expose owner-backed KPI/risk/resource context;
7. the Telos-style trajectory can explain current work upward through available relationships;
8. missing trajectory links are reported, not hallucinated;
9. current KPI values come from Data/current-truth owner;
10. historical evidence remains Memory-owned;
11. strategic direction obeys OS/Brain ownership;
12. high-impact strategic writes require correct confirmation;
13. the Purpose projection is deletable/rebuildable;
14. stale projection state cannot overrule current owners;
15. relevance/budget rules prevent Purpose from loading on every trivial task;
16. trivial deterministic tasks produce zero Purpose owner reads;
17. Purpose-unavailable fallback preserves ordinary task execution without using stale Purpose state as truth;
18. real operator/workspace comparisons demonstrate measurable strategic benefit from Purpose Context before feature expansion;
19. token/size and latency/cost overhead are measured and acceptable for the demonstrated benefit;
20. Slice 7.3 is explicitly recorded as `VALUE PROVEN` before Phases 8-10 and final release admission proceed;
21. Dashboard remains a view, not an owner;
22. all changed repos pass their full regression suites;
23. full Core clean-machine/bootstrap qualification passes Linux/macOS/Windows;
24. Core Lineage Guard proves all protected component refs are same-or-descendant;
25. a new exact-ref Core release is admitted rather than modifying the repaired baseline.

---

# Explicit non-goals

Do not:

- clone the Telos repository into AI-Verse;
- create an `AI-Verse-Telos` component;
- create a giant canonical Markdown file containing everything;
- force every Telos example field into AI-Verse;
- duplicate Brain goals in OS;
- duplicate Data values in Brain;
- let Memory become current strategy;
- let Dashboard become a strategy database;
- silently scan unrelated workspaces;
- infer relationship edges and present them as canonical facts;
- load Purpose for every task simply because the capability exists;
- continue building mutation/UI/corporate expansion when the real-world value gate is not proven;
- rewrite the repaired Core release;
- skip full Core requalification because focused Purpose tests passed.

---

# Current execution pointer

**CURRENT:** COMPLETE — Purpose Context v1 is implemented, qualified, documented, and admitted as `core-purpose-context-public-beta-2026-10-09`.  
**NEXT:** No canonical Purpose Context v1 tasks remain. Optional post-v1 follow-up is recorded in `docs/PURPOSE-CONTEXT-FINAL-COMPLETION.md`.