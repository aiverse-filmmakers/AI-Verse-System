# AI-Verse System Documentation Master Plan

## Objective

Build a durable, evidence-backed specification of the entire AI-Verse system family.

The goal is not to restate source code. The goal is to capture the architecture, product intent, ownership boundaries, operating laws, historical lessons, installation and migration expectations, inspirations, current gaps, and desired end state of every component.

The final result must answer two questions at the same time:

1. **What is AI-Verse today?**
2. **What is AI-Verse intentionally becoming?**

Those answers must never be conflated.

## Core philosophy to preserve

AI-Verse components are developed using a curating approach: study strong systems in the relevant category, identify the best ideas and failure modes, then combine the strongest compatible concepts into a cleaner system with stricter ownership boundaries and better interoperability.

Components should be:

- first-class inside AI-Verse OS;
- useful outside AI-Verse OS where the component's purpose permits;
- portable across compatible agents/runtimes such as Hermes, Codex, Claude Code and other hosts;
- independently installable;
- install-order independent wherever technically possible;
- explicitly attachable/activatable after installation;
- able to coexist without editing or corrupting sibling-owned state;
- upgradeable without silently overwriting user-owned truth;
- migration-aware for existing users with older state;
- safe to disable, detach, reinstall or replace without unnecessary loss of canonical user data.

## Canonical lifecycle target

Every component should eventually distinguish these states:

```text
AVAILABLE / INSTALLED
        ↓
SUPPORTED BY HOST
        ↓
ATTACHED TO HOST
        ↓
ENABLED
        ↓
HEALTHY
        ↓
INITIALIZED FOR SCOPE
        ↓
AUTHORIZED
```

These states must not be treated as synonyms.

### Package installation

A component may be installed before or after AI-Verse OS or another host.

Package installation should not require sibling components.

### Attachment

Attaching a component to an OS/host should be an explicit, idempotent operation that:

- discovers the host;
- validates compatibility;
- registers only component-owned integration state;
- preserves unrelated registry entries and host-owned files;
- exposes the component to the host runtime;
- does not silently grant permissions or authority.

### Activation / adoption

A host or agent must be able to adopt a newly attached component at any time, including when the host or agent existed before the component.

Long-term target examples include commands/concepts such as:

- `activate memory`
- `activate data`
- `activate brain`
- `activate skills`
- `reconcile components`

The exact CLI syntax may differ by repository, but the architectural requirement is that an agent can be told: **this component now becomes the canonical infrastructure for this responsibility**, without reinstalling the entire system.

Activation must respect ownership. It must not make two systems canonical for the same responsibility.

### Migration / history integration

Stateful components, especially Memory and Data, should support explicit history import/migration for users who already have older agents, existing memory stores, structured data, legacy AI-Verse layouts or standalone component state.

Migration must:

- preserve original evidence;
- avoid silent destructive conversion;
- distinguish import from activation;
- be resumable/idempotent where feasible;
- verify the new state before retiring the old route;
- avoid two editable canonical copies;
- record provenance.

### Disable / detach / uninstall

Disabling or detaching capability should not automatically delete canonical user data.

Uninstall should preserve user-owned state by default unless the user explicitly requests destructive removal.

Reinstall should be able to rediscover and reattach preserved compatible state.

## Component research order

Each component is processed separately to avoid context compression and accidental cross-repo assumptions.

Initial order:

1. AI-Verse OS
2. AI-Verse Brain
3. AI-Verse Memory
4. AI-Verse Skills
5. AI-Verse Data
6. AI-Verse Multiple Bots
7. AI-Verse Connections
8. AI-Verse Apps
9. AI-Verse Dashboard
10. AI-Verse Token

The order may be adjusted only if the documented dependency/ownership architecture establishes a better canonical sequence.

## Per-component research procedure

For every repository:

1. Inventory the repository tree and current default branch.
2. Read the top-level identity/runtime files.
3. Read architecture, PRD, build-map, status, release and integration documents.
4. Inspect current installation and lifecycle surfaces.
5. Inspect relevant tests/CI because they often encode stronger truth than prose.
6. Inspect important recent commit history.
7. Search for repair, audit, migration, integration, compatibility, security and release-hardening history.
8. Search for recorded inspirations/reference projects.
9. Compare the implementation's current state against the desired system-wide lifecycle.
10. Identify contradictions between README, runtime, tests, status docs and desired future state.
11. Write the component specification.
12. Run the QC gates below.
13. Only then move to the next component.

## Required component outputs

Each component gets:

```text
components/<component>/
  COMPONENT-SPEC.md
  SOURCE-MAP.md
  QC.md
```

### COMPONENT-SPEC.md

The big-picture specification containing current state, future state, laws, ownership, lifecycle, integration, historical repairs, inspirations and gaps.

### SOURCE-MAP.md

Evidence map of the most important source files, architecture docs, tests, commits, research references and historical documents used to derive the specification.

### QC.md

Independent review results and contradictions/gaps found during documentation.

## Quality-control perspectives

Every component document is reviewed from several perspectives.

### 1. Architecture QC

- Is there exactly one owner for each canonical responsibility?
- Are derived state and canonical truth separated?
- Are there duplicate stores or hidden parallel authorities?
- Are component boundaries coherent?

### 2. Lifecycle QC

- Can it install independently?
- Can it attach after the host already exists?
- Can it coexist regardless of reasonable installation order?
- Can it enable/disable/detach/reinstall safely?
- Does state survive where it should?

### 3. Migration QC

- What happens to older state?
- Can standalone/legacy state be imported deliberately?
- Are migrations reversible or at least safely resumable?
- Is provenance retained?

### 4. Integration QC

- Does it compose through supported contracts rather than direct internal coupling?
- Does it preserve sibling ownership?
- Does missing optional infrastructure fail gracefully?
- Can newly installed components become visible without rebuilding the whole OS?

### 5. Security and isolation QC

- Workspace isolation.
- permission/approval boundaries.
- symlink/path containment.
- secrets.
- cross-scope leakage.
- fail-closed behavior.

### 6. Agent/runtime portability QC

- What is AI-Verse-specific?
- What is portable?
- Can Hermes/Codex/Claude/other hosts adopt it?
- Does portability accidentally weaken canonical AI-Verse behavior?

### 7. Product/UX QC

- Is there a simple install command?
- Is setup understandable?
- Can the agent itself explain and perform activation/reconciliation?
- Are health/status/doctor surfaces clear?
- Are errors actionable?

### 8. Historical-learning QC

- What important bugs or architectural repairs occurred?
- What invariant did each repair establish?
- Is that lesson now expressed as a permanent system law?
- Are old repaired patterns accidentally reappearing elsewhere?

### 9. Inspiration QC

- Which external projects/models/frameworks materially influenced the component?
- Which ideas were adopted?
- Which were deliberately rejected?
- Did AI-Verse improve on the source idea or merely copy it?

### 10. Future-state QC

- Does the desired end state follow naturally from the current architecture?
- Are aspirations clearly labeled as future requirements?
- Does the component fit the supreme system vision without scope creep?

## Cross-component laws to test repeatedly

1. One canonical owner per responsibility.
2. Optional components add capability rather than create competing OSes.
3. Installation is not attachment.
4. Attachment is not enablement.
5. Enablement is not health.
6. Health is not authorization.
7. Registration is not permission.
8. Runtime availability must not silently change strategic authority.
9. User-owned state survives upgrades and normal uninstall.
10. Derived indexes/caches/views never become canonical truth.
11. Installation order should not determine correctness.
12. Components should be discoverable/reconcilable after later installation.
13. Existing/legacy state must have an explicit migration path.
14. Cross-repo changes are explicit, never hidden side effects.
15. A missing optional component should degrade the dependent capability, not corrupt unrelated system behavior.
16. Public/member installation paths must match the paths actually tested in acceptance.
17. Stable releases should use immutable versions/tags rather than moving branches.

## Final synthesis phase

Only after all component documents pass QC:

1. Compare ownership maps across every component.
2. Build the complete system topology.
3. Build the canonical lifecycle model.
4. Build the install-order matrix.
5. Build the activation/reconciliation model.
6. Build the migration model.
7. Build the host/runtime portability model.
8. Trace historical fixes into permanent system laws.
9. Reconcile current gaps into a single roadmap.
10. Produce the supreme document.

The final supreme document must tell the story of:

- the original problem;
- the architectural evolution;
- the present system;
- why the system is separated into these components;
- how they work together;
- how they can work outside AI-Verse OS;
- what has been learned through audits and repairs;
- what "finished" means;
- the path from the current implementation to that end state.
