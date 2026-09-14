# AI-Verse Safe Update and State Preservation Contract

**Status:** Canonical system law  
**Date:** 2026-09-14  
**Applies to:** AI-Verse Distribution and every releasable/updateable AI-Verse component  
**Canonical release owner:** `aiverse-filmmakers/ai-verse-distribution`  
**Implementation plan:** `docs/SAFE-UPDATE-AND-RELEASE-TRAIN-IMPLEMENTATION-PLAN.md`

## 1. Purpose

AI-Verse is modular software surrounding durable user-owned state. Updating software must never be treated as permission to recreate, replace, widen, re-own, or erase that state.

This contract defines the permanent cross-component safety floor for install, update, migration, recovery, rollback, uninstall, and release-set promotion.

Distribution orchestrates a release transition. Each component remains the owner of its own state semantics, migrations, status, doctor, and recovery guarantees.

A release candidate is not update-safe merely because clean installation succeeds. Update safety requires explicit compatibility plus executable preservation evidence.

## 2. Canonical separation: software versus user state

### LAW 1 - Software and canonical user state are separate

A software update changes package/runtime bytes and owner-approved metadata. It does not imply deletion, replacement, reset, migration, or reinitialization of canonical user state.

Canonical state includes, where applicable:

- Memory historical Markdown, memory records, provenance, supersession, and recall metadata owned by Memory;
- Data databases, Data Spaces, schemas, records, relations, transactions, structured provenance, idempotency state, and owner migration state;
- Brain Goals, practices, desired states, beliefs, verification state, direction handover state, and other Brain-owned strategic records;
- Skills immutable generations, active-generation selection, recoverable history, learning/proposal state, and package provenance;
- Multiple Bots durable Bots, Workers where durable by contract, Tasks, Rooms, Threads, Team Runs, approvals, handoffs, coordination history, leases, budgets, and coordination database state;
- Token normalized telemetry evidence, immutable usage/cost evidence, pricing evidence, and owner-specific indexes;
- OS/system/workspace configuration and registration state;
- component enable/disable state;
- operator configuration;
- opaque credential references and connection bindings;
- user-created files;
- component-owned durable state;
- additive/unknown compatible metadata.

A package installer or updater must not infer that state is disposable because it resides beneath a component directory.

### Package bytes are not ownership of the directory

Package ownership applies only to files explicitly owned by the installed package/release manifest.

Unknown files, compatible additive metadata, and user-created files are not package-owned merely because they share a parent directory with software.

## 3. Migration safety

### LAW 2 - Unknown migration means STOP

Before changing software in a way that requires state compatibility, the transition must be able to prove one of:

1. no state migration is required;
2. the installed state is explicitly compatible with the target software;
3. the owning component provides an admitted migration path with required verification/recovery evidence.

If none can be proved, the transition must return an explicit blocked result such as:

- `migration-required`;
- `update-blocked`;
- another stable machine-readable equivalent defined by the lifecycle contract.

The updater must not:

- recreate the state;
- silently initialize new state over existing state;
- delete existing state;
- overwrite existing state;
- mark migration complete without owner evidence;
- pretend the update succeeded.

### Owner-controlled migration

Only the canonical owner defines the meaning of its state and the legal transformation from one schema/generation/state format to another.

Distribution may:

- discover migration requirements;
- request an owner migration plan;
- verify declared preconditions;
- invoke the owner-controlled migration;
- persist release-transition operational evidence;
- require owner checkpoint/recovery evidence;
- verify the owner's declared postconditions.

Distribution must not invent a sibling component's migration semantics or directly rewrite sibling canonical state.

### Source drift

If migration/update planning was bound to a source revision, state fingerprint, schema generation, lock, or checkpoint and that source changes before apply, the transition must re-plan or fail closed.

A stale migration plan must never be applied as though the source were unchanged.

## 4. Release-set compatibility

### LAW 3 - Updates fail closed

Normal AI-Verse update targets are exact immutable release sets admitted by explicit compatibility rules.

A normal update must never target:

- floating `main`;
- floating branches;
- implicit `latest`;
- guessed component combinations;
- arbitrary cross-version mixing;
- a component revision whose integrity cannot be tied to the candidate release evidence.

Compatibility must not be inferred solely from semantic version ordering.

A release-set transition must explicitly identify the supported source set(s), target set, exact component revisions, runtime/platform requirements, migration requirements, preservation expectations, and known incompatible transitions.

### Released versus candidate

Candidate status and released/accepted status are different.

Automation may discover, generate, test, and propose candidates.

A candidate must not become the normal user-facing update target until the explicit release policy and required acceptance evidence are satisfied.

## 5. Unknown and user-owned files

### LAW 4 - Unknown compatible files survive

Installer/update logic must not blindly replace an entire component or user-state directory.

Only package-owned software paths may be replaced automatically.

If the target package wants to occupy a path currently containing an unknown or user-owned file, the update must:

- fail closed; or
- use an explicit owner-approved safe resolution that preserves the user's data and records the action.

Silent overwrite or deletion is forbidden.

Release acceptance must include explicit user-file preservation tests.

## 6. Authority preservation

### LAW 5 - No silent authority change

Update is not permission, approval, activation, handover, or scope expansion.

Unless the user performs a separate explicit authority-changing action, an update must not:

- transfer strategic/direction ownership to Brain;
- widen system/workspace scope;
- expand the OS permission floor;
- grant new permissions;
- approve Skills or tools;
- authorize Connections or external accounts;
- expose Gateway remotely;
- enable a disabled component;
- create Bots or workers;
- initialize every Data workspace;
- enable background/autonomous behavior that was disabled;
- convert optional capability availability into execution authority.

Authority, enabled state, scope, and approval state must be snapshotted and verified across release transitions where applicable.

### Authority-negative release metadata

Release metadata may declare facts such as "does not grant permissions" or "does not change direction owner", but metadata alone is not runtime authority.

Runtime authority remains with the canonical owner and must still be checked at the final execution edge.

## 7. Rollback semantics

### LAW 6 - Rollback is software rollback

Rollback means returning software/runtime/package selection to a previously admitted compatible release set.

Rollback must not claim to rewind canonical user state unless the owning component explicitly supports a state rollback from the current state and that rollback is part of an admitted recovery contract.

If old software cannot safely read the current state, software rollback must be refused or require the owner's explicit recovery procedure.

"Previous software revision exists" is not proof that rollback is safe.

## 8. Safe refusal

### LAW 7 - Safe refusal is better than destructive success

When integrity, compatibility, migration safety, authority preservation, state preservation, or recovery cannot be established, the update must refuse.

It is preferable for the user to remain on the current known-good release than to produce a nominally successful installation with missing, reset, duplicated, widened, or ambiguously owned state.

## 9. User consent and update planning

### LAW 8 - Release availability is separate from software application

A new release becoming available must not silently mutate an installed AI-Verse system.

The normal product flow is:

```text
aiverse update
```

for preview/check, and:

```text
aiverse update --apply
```

for explicit application.

The preview must truthfully report, at minimum:

- current release set;
- target release set;
- per-component changes;
- preservation claims;
- migration requirements;
- blocked conditions;
- authority changes or `none`;
- whether rollback is admitted;
- explicit command required to apply.

A machine-readable equivalent is required.

Any future automatic-update mode must be opt-in and may still consume only accepted release sets.

## 10. Update transaction and recovery

### LAW 9 - Partial update state must remain truthful

Distribution may keep durable operational update state describing the release transition, but it must not duplicate component canonical state.

Where an update can span multiple components or owner migrations, Distribution must be able to determine after interruption:

- source release set;
- target release set;
- component currently being processed;
- components staged/applied;
- lifecycle results;
- whether an owner migration started;
- whether an owner migration completed;
- whether target software became active;
- recovery/resume instructions.

After crash or restart, `status` or `doctor` must not claim a clean target release when the update is incomplete.

Recovery may support resume, recover, or compatible software rollback. It must not imply canonical-state rewind unless the owner explicitly supports it.

## 11. Owner-backed checkpoint and backup policy

### LAW 10 - Distribution requires owner evidence, not duplicate backups

Distribution must not make redundant copies of every canonical store merely to claim update safety.

Instead it must inspect and rely on the owning component's recovery guarantees.

Examples include:

- Data verified migration backups/checkpoints;
- Memory durable historical Markdown and migration provenance;
- Skills immutable generations;
- Multiple Bots durable coordination store and migration contract;
- Token immutable evidence semantics.

For a destructive or high-risk migration, promotion must be refused unless the owner supplies the checkpoint, backup, transactional, immutable-generation, or other recovery contract appropriate to that state.

The required evidence must be recorded as part of release-transition acceptance.

## 12. Uninstall and purge

### LAW 11 - Normal uninstall preserves canonical state

Normal public lifecycle uninstall removes package/runtime integration while preserving canonical user-owned state by default.

If a component supports destructive purge:

- purge must be a separate explicit operation;
- its destructive effect must be unmistakable;
- update must never invoke it;
- normal uninstall must never invoke it implicitly;
- release automation must never substitute purge for migration/recovery.

Reinstall must be able to discover/adopt preserved state according to the component's lifecycle contract rather than silently creating a competing canonical store.

## 13. Component release metadata versus runtime truth

### LAW 12 - Release metadata is not canonical live health

A Component Release Descriptor may state:

- immutable revision and version;
- supported lifecycle commands;
- state-preservation claims;
- migration compatibility;
- supported runtime/platforms;
- CI and acceptance evidence;
- authority-negative facts.

It must not become a second canonical health, readiness, permission, state, or ownership database.

Live `status`, `doctor`, authority, and canonical state remain with the component/host owners.

## 14. Modular ownership

### LAW 13 - Update infrastructure must not create duplicate owners

Do not:

- copy component engines into Distribution;
- merge component repositories into one implementation repository;
- create duplicate Memory/Data/Bots/Token truth;
- make Distribution own domain records;
- make AI-Verse-System an executable owner;
- create a second updater component;
- create a second telemetry/cost ledger;
- create another scheduler;
- create another canonical release owner.

The intended architecture remains:

```text
individual component repositories
        |
        v
exact accepted immutable component releases
        |
        v
AI-Verse Distribution
        |
        v
one installable AI-Verse product
```

## 15. Required release-transition acceptance

A release set may be called update-safe only when the release policy's required evidence proves the relevant source-to-target transition.

The permanent acceptance model includes:

### Clean installation

The target release set installs, sets up, and reports truthful status/doctor on supported platforms.

### Real upgrade

A previously released AI-Verse set is installed, realistic canonical state is created, identities/digests/counts/bytes/authority/enablement are snapshotted, the target update is applied, the system restarts, and preservation is verified.

### Preservation dimensions

Where included in the source/target profile, verify:

- Brain state;
- Memory history/provenance;
- Data records/schemas/relations/provenance;
- Skills generations/history/learning state;
- Multiple Bots coordination state;
- Token telemetry evidence;
- OS/workspace configuration;
- user-created files;
- disabled state;
- permission/scope floor;
- Brain direction ownership;
- absence of duplicate canonical stores;
- absence of revived stale writable legacy routes;
- truthful status and doctor after update.

### Negative/destructive transitions

At minimum test:

- unsupported migration;
- user-file collision;
- disabled component preservation;
- permission floor preservation;
- Brain ownership preservation;
- injected partial failure;
- wrong release SHA/source drift.

Negative tests must prove that blocked transitions leave protected state unchanged.

## 16. Release-train behavior

The long-term automated release flow is:

```text
component repo change
  -> component CI
  -> accepted component release candidate
  -> machine-readable release evidence
  -> Distribution candidate discovery
  -> exact immutable candidate release-set change
  -> Distribution PR
  -> compatibility + migration + preservation acceptance
  -> clean-machine + composed integration acceptance
  -> explicit promotion gate
  -> accepted Distribution release set
  -> user preview
  -> explicit user apply
```

Automation may create/update candidate PRs and run tests.

Automation must not push arbitrary component revisions directly into a released channel.

If candidate acceptance fails, the current known-good release remains the normal update target.

## 17. First Agent public-beta protection

The current Agent public-beta release has priority.

Release-train work must not destabilize an Agent candidate already undergoing acceptance.

If a release-train change would alter the exact current Agent candidate, classify it as one of:

1. a required safety fix for a real public-beta blocker; or
2. a post-Agent release-train enhancement.

Only category 1 should be forced into the current Agent candidate. Category 2 must wait for the immediately following release.

## 18. Definition of compliant update behavior

An AI-Verse update implementation is compliant with this contract only when all of the following are true:

- exact immutable source and target release sets are known;
- explicit transition compatibility is admitted;
- required owner migrations are known and owner-controlled;
- missing/unknown migration blocks safely;
- package-owned paths are distinguishable from unknown/user paths;
- canonical state is preserved or an explicit owner migration proves its transformation;
- disabled state and authority are preserved;
- partial failure is recoverable and truthfully reported;
- normal update requires explicit user consent;
- normal uninstall does not purge canonical state;
- rollback does not lie about canonical-state rewind;
- required source-to-target acceptance evidence exists.

Documentation alone is insufficient. The release train is complete only when executable implementation, tests, and release evidence prove these laws.
