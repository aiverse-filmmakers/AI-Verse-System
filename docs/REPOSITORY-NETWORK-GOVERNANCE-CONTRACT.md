# AI-Verse Repository Network Governance Contract

**Status:** Canonical system law  
**Canonical owner:** `aiverse-filmmakers/AI-Verse-System`  
**Applies to:** AI-Verse-System, ai-verse-distribution, every registered AI-Verse component repository, and all maintainers/agents acting across those repositories  
**Architecture baseline:** `docs/REPOSITORY-NETWORK-IMPLEMENTATION-ARCHITECTURE-2026-10-12.md`

## 1. Purpose

AI-Verse is one product built from multiple repositories with deliberately separate ownership boundaries.

This contract defines the permanent governance rules that make those repositories behave as one controlled product without turning System or Distribution into duplicate implementation homes.

The governing rule is:

> **Define centrally. Enforce at the canonical owner. Verify again at composition.**

This contract governs ownership, evidence routing, synchronization, drift, cross-repository safety and architecture history.

It does not replace the more specific canonical contracts that already govern update safety, component release metadata or whole-release preservation evidence.

## 2. Related canonical contracts and precedence

The following contracts retain authority over their existing domains:

- `docs/SAFE-UPDATE-AND-STATE-PRESERVATION-CONTRACT.md` owns install/update/migration/rollback/user-state/authority preservation and fail-closed transition safety.
- `docs/COMPONENT-RELEASE-DESCRIPTOR-CONTRACT.md` owns the canonical component release metadata format and exact revision evidence semantics.
- `docs/WHOLE-RELEASE-PRESERVATION-RESULT-CONTRACT.md` owns executable whole-release preservation result semantics.
- `docs/LIVING-SPEC-PROTOCOL.md` owns how meaningful product and architecture changes propagate into AI-Verse-System.
- `docs/OWNER-PRODUCT-INTENT.md` owns product-direction intent but does not override implementation evidence, canonical ownership, security, migration safety or accepted release evidence.

When two documents appear to disagree:

1. use the most specific canonical contract for the behavior being decided;
2. do not infer authority from file age or commit date alone;
3. use exact implementation/evidence refs and Git ancestry where applicable;
4. classify unresolved disagreement as canonical drift;
5. fail safely rather than inventing a merged interpretation.

This contract must not be used to weaken any existing preservation, migration, authority or release-acceptance requirement.

---

# 3. Canonical ownership law

## LAW 1 - Discovery location does not determine ownership

A defect, opportunity or missing behavior belongs to the repository that canonically owns the behavior, not the repository where the issue happened to be discovered.

The normal route is:

```text
Discover change
-> identify canonical owner
-> implement at canonical owner
-> owner-native validation/acceptance
-> record exact immutable owner revision and evidence
-> Distribution adopts exact accepted revision when release-relevant
-> Distribution qualifies exact composition
-> System synchronizes meaningful architecture/product truth
-> release may be admitted
```

If ownership cannot be determined safely:

`BLOCKED - OWNER UNRESOLVED`

No maintainer or agent may resolve ambiguity by copying the behavior into Distribution or System merely because those repositories are convenient places to make a change.

## LAW 2 - System is the control-plane authority, not a component implementation authority

AI-Verse-System owns:

- cross-repository architecture and product intent;
- canonical component responsibility boundaries;
- system invariants;
- repository-network governance contracts;
- Repository Registry;
- Repository State semantics and generated human ledger;
- cross-system architecture tombstones;
- current-versus-intended System truth;
- shared governance semantics used by owners and Distribution.

System must not become a second implementation home for component engines or a second release installer.

## LAW 3 - Component repositories remain implementation authorities

Each component repository owns:

- its domain implementation;
- its local interfaces, APIs and schemas;
- its local migration and recovery semantics;
- its native tests and acceptance process;
- its canonical state semantics;
- its component release descriptor/evidence.

Distribution and System may consume or validate this evidence. They must not silently redefine component-owned behavior.

## LAW 4 - Distribution is composition/release authority, not sibling domain authority

Distribution owns:

- exact release-set composition;
- candidate admission;
- cross-component compatibility/composition checks;
- source acquisition and lifecycle orchestration;
- install/update/rollback orchestration;
- member payload boundary;
- whole-product qualification;
- promotion and release channels;
- durable release reconstruction evidence.

Distribution must not become the canonical owner of sibling component domain logic, sibling canonical state or sibling acceptance truth.

Distribution's own accepted source revision may be recorded from its canonical owner descriptor. That records owner acceptance of Distribution's implementation only; it does not qualify or promote a member release.

---

# 4. Required cross-repository handoffs

## LAW 5 - Component to System handoff

A meaningful component change must evaluate whether System-level truth changes.

System impact exists when the change materially affects any of the following:

- component responsibility or ownership;
- system topology or integration;
- public/shared interface semantics;
- lifecycle semantics;
- compatibility or migration requirements;
- safety, authority or preservation invariants;
- release profile participation;
- architecture status such as current, intended, retired or replaced;
- system-wide readiness or definition of done.

When System impact exists, the component change is not fully propagated until the appropriate canonical System surface is updated or an explicit synchronization debt/blocker is recorded.

This handoff follows `docs/LIVING-SPEC-PROTOCOL.md`. System synchronization must describe truth; it must not override newer accepted implementation merely because an older System document differs.

## LAW 6 - Component to Distribution handoff

A release-relevant component revision must not enter Distribution merely because the commit exists or local tests happened to pass.

The component owner must provide the exact immutable revision and the owner acceptance/release evidence required by the canonical component release contract.

Distribution must adopt that exact accepted revision. Substituting a different SHA, a floating branch, or a newer convenient revision invalidates the handoff and requires fresh owner evidence.

## LAW 7 - Distribution to System handoff

Distribution release truth that materially changes current System architecture, supported lifecycle, release profile, compatibility policy, current-vs-intended status or other canonical System truth must be propagated back to System.

Exact volatile release composition remains Distribution-owned. System should record durable architectural/product truth, not duplicate every release-set fact as independently maintained data.

---

# 5. Two-layer validation and exact evidence

## LAW 8 - Owner validation and Distribution qualification are separate gates

Layer 1:

```text
Owner validation
Does this exact component revision satisfy its own contract?
```

Layer 2:

```text
Distribution qualification
Do these exact owner-accepted revisions work together safely as AI-Verse?
```

Neither layer substitutes for the other.

Owner success does not imply whole-product success. Distribution success cannot manufacture missing owner acceptance.

## LAW 9 - Moving references are not acceptance evidence

Release-governance decisions use exact immutable repository identity/ref evidence.

A branch name, `main`, implicit `latest`, timestamp, issue statement or approximate version is not sufficient evidence for an admitted release decision when an exact revision is required.

Dates may be displayed for context. They are not canonical lineage proof.

## LAW 10 - Unavailable required evidence is not a passing result

Validation must distinguish:

- evidence passed;
- evidence failed;
- evidence unavailable/unverified.

When required evidence is unavailable, the affected decision fails closed. It must not be represented as CLEAN or PASS merely because failure could not be observed.

---

# 6. System synchronization and canonical drift

## LAW 11 - Stale System text cannot regress accepted implementation

When System wording disagrees with newer implementation, neither side wins automatically based on age.

Use:

`CANONICAL-DRIFT-DETECTED`

Then compare:

- exact component implementation refs;
- owner acceptance evidence;
- Distribution release/admission evidence;
- canonical System intent/history;
- migration/compatibility impact;
- architecture tombstones where relevant.

Automatic correction is frozen until the evidence identifies the stale or incorrect side.

If accepted implementation is newer and System is stale, synchronize System forward.

If newer implementation violates canonical intent or lacks required acceptance, repair the implementation at its canonical owner and requalify when composition changes.

## LAW 12 - Newer code does not automatically rewrite canonical intent

A newer commit is not automatically the new architecture.

Experimental, accidental, unaccepted or ownership-violating implementation must not become canonical System truth merely because its timestamp is newer.

## LAW 13 - System synchronization must avoid duplicate volatile truth

System owns architecture and product truth. Distribution owns exact release composition and promotion state. Components own their implementation details.

System documentation must not copy volatile release facts into independently maintained canonical records unless those facts are genuinely needed as durable architecture/product truth.

---

# 7. Repository Registry, Repository State and human ledger authority

## LAW 14 - Registry and State are different authorities

The Repository Registry is System-owned stable/declarative truth about what repositories are, who owns them and how they participate.

Repository State is System-owned dynamic observed truth about where those repositories currently stand.

The human Markdown ledger is generated from Registry/State and is not an independently editable machine authority.

Distribution may freeze relevant Registry/State evidence for a candidate. That frozen copy is qualification evidence, not a competing Registry or State authority.

## LAW 15 - Unknown first-class release repositories fail closed

A first-class repository must be registered before it may participate in an admitted release composition.

An unregistered repository may be inspected or experimented with, but it cannot silently become a shippable component.

---

# 8. Drift scope and release effect

## LAW 16 - Drift carries severity and scope

Every repository-network drift finding must identify:

```text
severity: INFO | WARNING | BLOCKING
scope: component | Core | Agent | Full | global
reason
relevant refs
required action
```

`BLOCKING` drift blocks a release only when its scope intersects the release decision, unless the finding is global.

INFO/WARNING drift does not automatically block unrelated release scopes.

Required acceptance evidence missing, exact-ref mismatch, unregistered release component, preservation failure, member governance leakage, unresolved breaking contract change, changed bound candidate evidence or other contract-defined release blockers must fail closed for the affected scope.

---

# 9. Breaking changes and contract preservation

## LAW 17 - No silent depended-on contract deletion

A component must not silently remove, redefine or repurpose an API, schema, interface or state contract that another registered component or admitted release depends on simply because its local tests pass.

A breaking change requires one of:

- compatible replacement;
- versioned coexistence;
- explicit coordinated breaking release/migration accepted by affected owners and qualified by Distribution.

The canonical component release descriptor is the one release metadata surface to extend for shared compatibility semantics when additional fields are required. A second compatibility fingerprint format is prohibited unless this architecture is explicitly replaced through governed change and tombstoned.

---

# 10. Member isolation

## LAW 18 - Maintainer governance is source-only by default

The following are internal governance surfaces and must not enter member installs by default:

- Repository Registry and Repository State;
- generated repository-state ledger;
- drift/watchdog reports;
- architecture tombstones;
- repository-network governance/planning/audit documents;
- internal qualification snapshots and receipts;
- cross-repository maintainer handoff instructions;
- internal promotion/governance tooling.

Legitimate product-facing generated files may share names such as `AGENTS.md` or `CLAUDE.md`. Filename similarity never grants permission to delete or replace user/local files.

Member payload construction must follow deterministic ownership/inclusion rules and the separate safe-update/state-preservation contract.

---

# 11. Decision and recovery provenance

## LAW 19 - Every layer owns its own provenance

System records architecture/governance decisions and reconciliation history.

Component owners record component implementation, migration and acceptance provenance.

Distribution records composition, qualification, transition, promotion and release evidence.

No layer should copy another layer's canonical state merely to appear self-contained.

Important release decisions must be diagnosable later from durable exact evidence, including enough information to identify:

- what was believed;
- which exact refs/evidence supported the decision;
- which owner made the relevant claim;
- what Distribution qualified;
- what System truth was synchronized or left as explicit debt;
- what recovery path was available.

Software reconstruction evidence and user-state recovery remain separate concerns.

---

# 12. Architecture tombstones

## LAW 20 - Superseded architecture must leave durable evidence

Retired, replaced or explicitly prohibited architecture must be recorded in:

`docs/ARCHITECTURE-TOMBSTONES.md`

A cross-system tombstone must identify at minimum:

- tombstone ID;
- date;
- status: `retired`, `replaced` or `prohibited-resurrection`;
- affected architecture/surface;
- superseded refs/paths;
- replacement architecture/ref;
- reason/evidence;
- compatibility/migration impact;
- cleanup obligations, if any;
- canonical owner;
- relevant release/qualification refs;
- resurrection condition, default `none` unless explicitly approved.

A future agent encountering an old plan, stale audit, branch, issue or document that describes tombstoned architecture must not recreate it merely because the old source is detailed or newer-looking.

If resurrection appears necessary, treat it as a protected architecture change. Record evidence and use the applicable plan/governance amendment process before implementation.

Component-local tombstones are appropriate only for local component-owned APIs/schemas/migrations. They do not replace the System cross-architecture ledger.

---

# 13. Emergency safety release

## LAW 21 - Break-glass is a bounded policy path, not a bypass

An emergency release is limited to urgent security, corruption or user-data-protection fixes.

It must use the same canonical owner routing and Distribution composition machinery as normal release work.

It must not bypass:

- owner validation;
- exact immutable refs;
- required compatibility/migration evidence;
- state preservation requirements;
- whole-product qualification;
- member isolation.

The only permitted temporary debt is non-safety System documentation synchronization debt explicitly recorded as:

`SYSTEM-SYNC-DEBT`

A later normal promotion is blocked until required sync debt is reconciled.

The detailed state/update safety requirements remain governed by `docs/SAFE-UPDATE-AND-STATE-PRESERVATION-CONTRACT.md` and whole-release preservation evidence remains governed by `docs/WHOLE-RELEASE-PRESERVATION-RESULT-CONTRACT.md`.

---

# 14. Cross-repository write authority

## LAW 22 - Broad unattended cross-repo writes are prohibited by default

Repository-network governance must not depend on a maintainer agent or watchdog having broad write authority across every repository.

Default automation should use least-privilege read/validation access.

A workflow may propose or route a change to the canonical owner. It must not silently patch sibling repositories, change release pins or promote releases merely because it detected drift.

When a cross-repository write is genuinely required, it must be explicit, scoped to the intended repository/action, attributable and supported by the relevant owner/release evidence.

Watchdog and refresh tooling must not require broad cross-repo write credentials merely to determine current truth.

---

# 15. Rollout waves

## LAW 23 - Governance expands only after the previous wave proves the pattern

Rollout order is:

1. Wave 1: System + Distribution + Core (`OS`, `Brain`, `Memory`, `Skills`, `Data`).
2. Wave 2: Registry-confirmed active Agent-profile repositories.
3. Wave 3: Registry-confirmed active Full/future repositories.

Later-wave repository names and participation are Registry-driven, not guessed from old plans.

Experimental, retired and external repositories must be explicitly classified and cannot silently inherit shippable status.

Repository-specific file layout may differ. Semantic ownership, acceptance, evidence and handoff requirements may not be weakened merely for layout convenience.

---

# 16. Permanent system invariants

The following invariants must remain true throughout supported repository-network workflows:

1. One canonical implementation owner exists for each behavior/domain.
2. System is not a duplicate component implementation home.
3. Distribution is not a duplicate sibling implementation or acceptance home.
4. Component release evidence names an exact immutable revision.
5. Owner validation precedes release adoption where required.
6. Distribution qualification applies to the exact composed revisions.
7. Registry stable truth and Repository State dynamic truth are separate.
8. Human repository-state Markdown is generated projection only.
9. Stale System text cannot automatically regress accepted implementation.
10. Newer unvalidated code cannot automatically rewrite canonical intent.
11. Breaking depended-on contracts cannot disappear silently.
12. Member governance cannot leak into member payload by default.
13. User-owned state/file safety is governed by the existing preservation contract and cannot be weakened here.
14. Important admitted releases remain reconstructable from durable exact evidence.
15. Missing required evidence fails closed and is distinguishable from evidence failure.
16. Architecture retirement leaves tombstones.
17. Emergency release does not bypass owner validation, preservation or whole-product qualification.
18. Watchdog/refresh machinery may observe and report but does not silently rewrite owners or promote releases.
19. No unregistered first-class component silently enters an admitted release.
20. A discovered issue is routed to its canonical owner even when discovered elsewhere.

A future change that would intentionally invalidate one of these invariants is a protected architecture/governance change and must be handled explicitly rather than smuggled through implementation work.

---

# 17. Enforcement and evidence placement

| Concern | Definition authority | Local enforcement/publication | Composition verification |
|---|---|---|---|
| Cross-repo governance | System | canonical owners | System + Distribution as applicable |
| Repository identity/role | System Registry | System | Distribution consumes relevant evidence |
| Dynamic repo state/drift | System Repository State | System refresh/watchdog | Distribution consumes scoped blocking state |
| Component implementation/API/schema | component owner | component owner | Distribution verifies composed compatibility |
| Component release metadata | System descriptor contract | component owner descriptor | Distribution |
| Owner native acceptance | component owner | component owner | Distribution requires exact evidence |
| Update/state preservation | existing System safety contract | owner + Distribution orchestration | Distribution qualification |
| Whole-release preservation result | existing System result contract | Distribution qualification | Distribution promotion gate |
| Exact shipped composition | Distribution | Distribution release set | Distribution |
| Promotion/current channel | System policy + Distribution implementation | Distribution | Distribution |
| Architecture tombstones | System | System ledger | System/Distribution inspect when relevant |
| Durable reconstruction | System law | owner immutable evidence + Distribution receipt | Distribution admission/recovery |

---

# 18. Change control

This contract is permanent governance law, not an implementation checklist.

Implementation plans may refine tasks, tools and file layouts where the semantic ownership and safety outcomes remain unchanged.

A change that would intentionally alter canonical ownership, weaken validation/preservation/member-isolation/evidence floors, remove a permanent invariant, resurrect prohibited architecture, or transfer an authority between System/component/Distribution requires explicit governed architectural change with evidence and corresponding tombstone/history updates.

Do not edit history to make a new direction appear as though it was always the rule.

---

# 19. Maintainer/agent entry rule

Until `docs/MAINTAINER-START-HERE.md` is created in the planned Repository State slice, maintainers and agents performing meaningful cross-repository work must read, in order:

1. `docs/REPOSITORY-NETWORK-GOVERNANCE-CONTRACT.md`;
2. the relevant specific canonical safety/release contract;
3. the relevant System/component specification and current evidence;
4. `docs/ARCHITECTURE-TOMBSTONES.md` for prohibited/replaced architecture;
5. the current implementation program only when executing that program.

This ensures future work can find permanent rules without depending on historical program context.
