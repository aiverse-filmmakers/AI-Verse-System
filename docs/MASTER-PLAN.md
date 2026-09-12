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
- explicitly adoptable/activatable after installation, using attachment only where host-local integration state is actually required;
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

#### External-provider adoption exception

Not every independently installed component requires a host-local attachment record.

For a read-only external provider whose host integration is discovery-only, dynamic discovery from a canonical/configured provider root may be the correct adoption mechanism when:

- provider appearance does not transfer canonical authority;
- discovery grants no permission or approval;
- no tracked host file or host-owned canonical state must be mutated;
- late installation and later absence are discovered dynamically;
- damaged/incompatible provider state fails closed without corrupting unrelated host behavior;
- the provider retains ownership of its own lifecycle.

AI-Verse Skills is the current concrete example.

Do not create attachment state merely for lifecycle symmetry when external discovery already provides the correct ownership boundary.

### Activation / adoption

A host or agent must be able to adopt a newly available component at any time, including when the host or agent existed before the component. Adoption may be explicit attachment or dynamic external-provider discovery, depending on ownership.

Long-term target examples include commands/concepts such as:

- `activate memory`
- `activate data`
- `activate brain`
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
- bind a reviewed migration plan to a source snapshot/fingerprint or explicitly detect source drift before apply;
- verify the new state before retiring the old route;
- avoid two editable canonical copies;
- record provenance.
- after a verified stateful migration, explicitly record canonical authority handoff and retire the legacy writable route while preserving old evidence as needed.

### Disable / detach / uninstall

Disabling or detaching capability should not automatically delete canonical user data.

Uninstall should preserve user-owned state by default unless the user explicitly requests destructive removal.

Reinstall should be able to rediscover and reattach preserved compatible state.

## Continuous evolution protocol

The first component-by-component pass is only the baseline.

After a component has been documented, it remains live.

Whenever new information appears, apply the rules in `docs/LIVING-SPEC-PROTOCOL.md`.

At minimum:

- capture unscoped ideas in `docs/IDEA-INBOX.md`;
- update the owning component spec when an idea becomes accepted intent;
- update CURRENT/GAP/INTENDED state when implementation changes;
- update SOURCE-MAP when new implementation/release evidence exists;
- rerun the affected QC/readiness dimensions;
- append `docs/SYSTEM-CHANGELOG.md`;
- update the future supreme blueprint when a system-wide law/topology/lifecycle changes.

A component does not become "frozen documentation" merely because its initial review is complete.

A completed component review means: **baseline established and ready for continuous maintenance**.

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

The canonical forensic procedure is `docs/AUDIT-METHODOLOGY.md`.

The steps below are the high-level summary. The methodology document is authoritative for the full evidence hierarchy, 46 required audit lenses, contradiction scan, negative-space analysis, lifecycle/completeness matrices, historical archaeology, health-depth classification and completion checklist.

A component review is not complete merely because the summary steps below were followed if the applicable methodology lenses were skipped.

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
11. Identify the component's **current intended milestone** and audit whether it is actually complete for that milestone.
12. Build the command/lifecycle matrix for install, attach, activate, initialize, migrate, doctor, update, disable, detach/uninstall and reinstall/reconcile.
13. Separate engine completeness from implementation/wiring/UX completeness.
14. List the exact blockers between today's state and "works perfectly together like a glove".
15. Write the component specification.
16. Run the QC gates below.
17. Only then move to the next component.

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

The perspective list below is a compact overview only. `docs/AUDIT-METHODOLOGY.md` expands this into the mandatory multi-lens review used for the fresh AI-Verse OS re-audit, including ownership, provenance, isolation, privacy, lifecycle, discovery, readiness, health depth, permissions, path security, idempotency, concurrency, failure behavior, cross-component read/write paths, scalability, documentation drift, negative-space analysis, architecture-vs-operation classification, scope-creep checks and component-specific definition of done.

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

### 10. Current-target readiness QC

- What is the component supposed to achieve at the current milestone?
- Is the engine complete but implementation/wiring incomplete?
- Are install, attach and activation commands real and supported?
- Can an already-running agent adopt it later?
- Is legacy-state migration real?
- Has the real member path been tested?
- What exact tasks remain before it works seamlessly with the rest of the system?
- Is the component truly ready, partially ready, or externally blocked?

A component is not "100% complete" merely because its internal code/tests are green if the current product goal also requires missing lifecycle or host integration.

### 11. Future-state QC

- Does the desired end state follow naturally from the current architecture?
- Are aspirations clearly labeled as future requirements?
- Does the component fit the supreme system vision without scope creep?

## Current-stage completeness rule

Every component document must distinguish:

```text
ENGINE COMPLETE
INTEGRATION COMPLETE
LIFECYCLE COMPLETE
MIGRATION COMPLETE
COMMAND/UX COMPLETE
ACCEPTANCE COMPLETE
RELEASE/DISTRIBUTION COMPLETE
```

These are separate dimensions.

The final supreme document must be able to say, for example:

> Brain's core engine is complete, but its current intended product state is only 85% complete because activation/migration/member-path wiring is still missing.

or:

> Memory is functionally complete and fully integrated, but the remaining blocker is a missing implementation command.

Do not invent numerical percentages unless the evidence supports a meaningful task/acceptance denominator. Prefer categorical readiness plus an explicit missing-work list when precision would be false.

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
18. Integrity-valid content is not automatically trusted/admitted, ready, authorized, approved or verified.
19. Dynamic external-provider discovery may satisfy late adoption without attachment only when discovery changes no canonical host authority/state and grants no permission.
20. A runtime-support claim should require a tested discover -> select -> load -> invoke -> verified-outcome path, not merely directory exposure or package visibility.
18. Apps, dashboards and other interfaces must remain rebuildable projections/clients of declared canonical owners; UI convenience must never create hidden canonical truth.
19. A component may define a registration or extension schema without owning the host's canonical registration records; for Apps, the intended split is Apps-owned app contract/schema and OS-owned authoritative system registration state.
20. Scoped canonical storage must validate physical containment at both read and write boundaries; later read rejection cannot undo an escaped write.
21. Migration completion is an authority transition, not merely a successful copy: preserved legacy bytes may remain, but duplicate writable canonical authority must not.
22. A detach operation must close every host discovery route it opened, or its narrower scope must be named and documented explicitly.
23. Projection layers may normalize and aggregate owner-declared schemas, but must not become semantic owners by inferring canonical health, work, Bot, approval, readiness or runtime meaning from private files or transient UI/session state. Unavailable owner state must remain unavailable rather than becoming empty, zero or healthy.

24. Telemetry observations and projections are evidence, not authority transfers: a usage event may describe a workspace, project, Bot, task, Skill or connection, but it must not become the canonical operational state of that component.
25. Attribution is not authorization: telemetry scope IDs and actor labels cannot grant access, workspace membership, execution authority or permission. Host read/write boundaries must intersect telemetry requests with the caller's authorized scope.
26. Telemetry readiness is multi-dimensional: installed, attached and enabled must remain separate from source-active, collecting, pricing-ready, cost-ready, authorized and operationally ready.
27. Monetary telemetry preserves truth provenance: UNKNOWN is never zero, ACTUAL and CALCULATED remain visibly distinct, and a derived/calculated cost must never be silently presented as invoice-confirmed billing.

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
11. Put the supreme document under the same living-spec protocol so later ideas/fixes/plans propagate into it.

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


## Change propagation rule

When implementation work occurs in any AI-Verse repository, the follow-up documentation check is:

```text
Did this change alter:
- what the component is?
- what it owns?
- how it integrates?
- its current target?
- its readiness?
- lifecycle commands?
- migration?
- a known gap?
- a permanent law?
- the system roadmap?
```

If yes, AI-Verse-System must be updated.

A code fix that changes an architectural invariant is incomplete as system documentation until that invariant is captured here.


---

## Shared laws established by the Multiple Bots audit

### Authenticated principal is not protocol actor text

**LAW:** network/control-plane authentication and protocol actor identity are different layers.

A component may use durable IDs such as Bot IDs, Worker IDs or operator actor IDs internally, but a network client must not gain that authority merely by submitting the string.

Any mutating Gateway or host API exposed outside a trusted in-process/loopback boundary must:

1. authenticate the caller;
2. determine which protocol principals that caller may act as;
3. authorize the requested operation;
4. then apply component-level scope/permission/lease checks.

Internal least-authority checks do not substitute for authenticated ingress.

### Dynamic component consumers must follow the current owner lifecycle contract

**LAW:** a consumer must not keep a stale private parser for another component's old installation/enablement signal after that owner has migrated to a new lifecycle contract.

For local AI-Verse extensions, current attachment state belongs in the local extension lifecycle/registry contract rather than a copied tracked-manifest convention.

Compatibility suites must test the current owner-supported path.

### Canonical operational state is not the same as a derived cache

**LAW:** “derived state is disposable” applies only when a proven canonical source can rebuild it completely.

A component-owned database that contains unique coordination history, delivery state, recovery state or other owner records is canonical component state even if other AI-Verse domain truth lives elsewhere.

Such state requires migration, backup/recovery and uninstall preservation appropriate to its canonicality.

### Structured Data remains owner-routed

**LAW:** collaboration does not transfer Data ownership to Multiple Bots or another execution layer.

A Bot/Worker that needs structured Data must use the Data owner boundary through the host/OS integration contract. It must not open Data storage directly or create a second editable structured-data store.

### Current-generation compatibility is a release property

**LAW:** a historical integration slice passing its original tests does not prove present sibling compatibility forever.

Before a system/component claims seamless integration, compatibility/evaluation must exercise the current supported owner contracts, lifecycle generation and absence/degraded behavior.

This may use versioned contract fixtures or owner-supported interfaces. It should not create hidden source-repository dependencies merely to make CI green.
