# AI-Verse Safe Infrastructure Qualification Invariants Contract v1

**Status:** canonical System contract  
**Contract ID:** `ai-verse.safe-infrastructure-qualification/v1`  
**Owner:** AI-Verse-System  
**Purpose:** define the minimum testable invariants for infrastructure convergence, whole-install restore, doctor aggregation and member-facing lifecycle UX without taking ownership of component domain logic.

## 1. Scope

This contract defines what later implementation and qualification must prove.

It does not implement:

- an owner migration;
- a Workspace relocation engine;
- a Skill re-scope engine;
- a Last-Known-Good storage engine;
- restore orchestration;
- doctor owner logic;
- the final member-facing formatter.

Those remain with their canonical owners and later Safe Infrastructure slices.

The machine-readable qualification envelope defined here is evidence about a tested installation/fixture. It is not live canonical state and must never become a second owner store.

## 2. Imported canonical contracts

This contract consumes, and does not redefine:

- `ai-verse.durable-identity-reference/v1` for durable identity/reference law;
- `ai-verse.infrastructure-upgrade/v1` for owner-published infrastructure generations and upgrade recipes;
- the Slice 2.1 whole-install Last-Known-Good and restore law recorded in Distribution's Core Update Transition Contract.

If an owner publishes stronger domain-specific guarantees, qualification may rely on them only when they are explicit and evidenced.

## 3. Convergence invariant

A historical installation that completes an admitted structural upgrade MUST converge to the same target architecture contract as a fresh installation of the exact same admitted target release, for package-owned/generated/migratable infrastructure.

Convergence does **not** mean whole-directory byte equality.

The comparison MUST preserve legitimate differences that are user-owned or owner-defined history, including custom files, real Workspace content, Memory/Data state, history and durable identities.

A convergence qualification PASS requires all of the following:

1. the fresh fixture and upgraded fixture are bound to the exact same admitted target release/revisions;
2. both satisfy the same target owner structural/postcondition checks for every domain in scope;
3. no required target owner check is skipped merely because the installation arrived through upgrade rather than fresh install;
4. user-owned/custom state required by ownership law is preserved;
5. durable identities and cross-owner references are preserved or intentionally changed only where the canonical owner contract explicitly permits that identity change;
6. unsupported/ambiguous owner state is not normalized by guesswork;
7. legacy writable infrastructure is retired only where the admitted recipe and owner postconditions authorize retirement.

A difference in cache layout, rebuildable runtime material or other owner-declared derived state does not by itself violate convergence.

## 4. Restore invariant

After a successful `aiverse restore --apply`, the declared **covered local recovery scope** MUST match or reproducibly represent the retained Last-Known-Good point.

A restore qualification PASS requires:

1. every `CAPTURE` item in the retained recovery manifest is restored byte-exactly or through an owner mechanism whose explicit verification proves equivalent canonical state;
2. every `RECONSTRUCT` software/material item resolves to the exact immutable retained release/revision/digest evidence;
3. every `REBUILD` item is rebuilt only where its owner declares it derived/disposable and required postconditions pass;
4. every `EXTERNAL/EXCLUDED` item remains truthfully declared outside local restore scope;
5. the retained LKG target survives until restore verification succeeds;
6. partial restore failure cannot destroy the retained target;
7. durable identity/reference guarantees are revalidated after restore;
8. external services, remote side effects, credential stores and other excluded systems are never reported as rewound unless a later approved mechanism explicitly covers them.

Restore exactness applies only to the declared covered local scope. It is forbidden to turn an exclusion into an implicit success claim.

## 5. Doctor invariant

The canonical member health command is one command:

```text
aiverse doctor
```

Distribution aggregates owner truth. It does not duplicate owner health semantics.

A doctor qualification PASS requires:

1. every required owner doctor/check for the tested profile is invoked or explicitly proven not applicable;
2. each owner result remains independently identifiable in machine evidence;
3. an owner failure cannot be converted into a whole-system PASS;
4. one isolated owner failure does not silently suppress unrelated safe read-only owner checks unless a declared dependency makes continuation invalid;
5. the composed System/OS check, when supported, is additional evidence rather than a replacement for required owner checks;
6. the aggregate result is deterministic from the required included checks;
7. doctor remains read-only;
8. the member is not required to know which component owns a problem.

A qualification fixture MUST include injected-failure proof showing that one required owner failure yields aggregate failure while unrelated safe checks still run where permitted.

## 6. Member UX invariant

Default lifecycle output is for members, not maintainers.

Default output for doctor, upgrade preview and restore preview MUST:

- be plain English;
- lead with the practical result and next action;
- remain compact enough for a small screen;
- distinguish healthy, optional improvement, required change and review/blocked states unambiguously;
- state when nothing has changed yet for read-only previews;
- avoid requiring repository names, filesystem paths, Git SHAs, release-set IDs, infrastructure generations, migration recipe IDs, owner IDs or component-internal terminology;
- avoid exposing secrets or credential material;
- preserve access to detailed machine-readable evidence through JSON/details mode.

Technical identifiers MAY appear only when explicitly requested in details/JSON or when no safer human-readable conflict identifier exists.

A default summary MUST NOT be the only evidence surface. Human simplicity and machine evidence are both required.

## 7. Machine-readable qualification envelope

The normative evidence schema is:

`contracts/safe-infrastructure-qualification-v1.schema.json`

A qualification result contains:

- exact target release evidence;
- imported contract IDs;
- independent `convergence`, `restore`, `doctor` and `member_ux` sections;
- structured evidence entries;
- one overall result.

A whole qualification may report `PASS` only when every required section reports `PASS` and the cross-field invariants below are satisfied.

## 8. Convergence evidence requirements

The convergence section records:

- whether fresh and upgraded fixtures target the same exact release;
- whether both satisfy the same target architecture/owner checks;
- whether user-owned state is preserved;
- whether durable identity/reference behavior was verified;
- whether unsupported ambiguity was avoided rather than guessed;
- evidence references to the owner/System checks used.

The contract deliberately does not require byte-identical whole installations.

## 9. Restore evidence requirements

The restore section records:

- declared covered-state exactness;
- exact software reconstruction;
- owner rebuild verification;
- truthful exclusions;
- retained-target survival;
- identity/reference verification;
- evidence references to recovery manifests, hashes, owner verification and health checks.

A PASS is invalid if any covered category is unknown or silently omitted.

## 10. Doctor evidence requirements

The doctor section records:

- the canonical command;
- required owner checks;
- independently reported owner results;
- aggregate result;
- read-only status;
- optional composed-system evidence;
- injected-failure proof.

Required owner names in evidence are orchestration identifiers only. They do not transfer ownership to System or Distribution.

Duplicate owner results or a missing required owner result fail closed.

## 11. UX evidence requirements

The member UX section records:

- a representative default summary;
- plain-English/small-screen/read-only-preview assertions;
- absence of internal-jargon requirements in the default summary;
- confirmation that technical evidence remains available separately.

The validator applies conservative checks to the representative default summary. It is not a prose-style engine and does not replace later usability tests.

## 12. Fail-closed rules

Qualification MUST fail when any of the following is true:

- target release/revision evidence is incomplete;
- one required section is missing or not PASS;
- fresh and upgraded fixtures were not compared against the same exact target;
- convergence skipped a required owner contract check;
- user-owned state preservation is unproven;
- durable identity/reference behavior is unproven;
- restore claims exactness while covered state or exact software reconstruction is unproven;
- restore claims external/excluded systems were restored without an approved mechanism;
- required doctor owner results are missing or duplicated;
- injected doctor failure can become aggregate PASS;
- doctor mutation is observed;
- default member output requires internal architecture jargon;
- technical evidence is unavailable because the human summary replaced it.

Unknown evidence is not PASS.

## 13. Relationship to later phases

Phase 3 owner implementation MUST satisfy the convergence and identity requirements here.

Phase 4 Distribution implementation MUST satisfy the restore, doctor and member UX requirements here.

Phase 5 qualification MUST emit or otherwise prove equivalent evidence for this contract and MUST include destructive-negative cases.

This contract therefore establishes the test oracle before implementation proceeds.

## 14. Non-goals

This contract does not create:

- a second release registry;
- a second identity registry;
- a global owner-health model;
- a generic migration engine;
- a universal filesystem layout;
- a universal byte-for-byte installation fingerprint;
- a new backup store;
- a final UX renderer.

It defines only the cross-system invariants and qualification evidence required to prove the later implementation is safe and truthful.