# Safe Infrastructure Slice 3.4 - Capability Promotion / Re-scoping Evidence

Status: COMPLETE

## Refreshed refs

Slice-start refs:

- System: `aiverse-filmmakers/AI-Verse-System@181cdee251e6d76dac50ff2cfde484f7e4be3b4d`
- task-list commit: `aiverse-filmmakers/AI-Verse-System@84afaa49a77bc8c9869a0172e13f2c9f61718ddc`
- OS: `aiverse-filmmakers/AI-Verse-OS@866359d877bfb3df0d8011d2d651a5ff947e21ca`
- Skills: `aiverse-filmmakers/AI-Verse-Skills@d4a02888ba8d83c4a15ce1b538ffdafaaf83bee1`

Implementation/validation refs:

- OS implementation head: `aiverse-filmmakers/AI-Verse-OS@470ad89e6b96d898161dee36d4e4fa8064dd6a8d`
- Skills validation head: `aiverse-filmmakers/AI-Verse-Skills@d4a02888ba8d83c4a15ce1b538ffdafaaf83bee1` (unchanged)
- System live head observed before evidence closure: `aiverse-filmmakers/AI-Verse-System@0b341181424f0461898e180a0ad769721e7b1424`; concurrent commits belonged to a separate Core-maintainer program and did not alter this Safe Infrastructure evidence file or roadmap section.

## Canonical decision

Slice 3.4 admits only the proven motivating promotion required by the roadmap fixture: a user-owned Workspace capability promoted to the user-owned personal `local` provider for reuse beyond one Workspace.

This is not an identity-preserving move. Under `ai-verse.durable-identity-reference/v1`, provider/scope participates in the current qualified identity, so `workspace:<workspace-id>:<name>` and `local:<name>` are different qualified identities. Promotion therefore records an explicit source-to-target relationship, preserves source provenance/history, and repairs exact old qualified-ID consumers through an OS-owned compatibility mechanism without pretending the old and new IDs are the same identity.

Managed `aiverse-skills` and `os` sources remain outside this personal promotion path. No generic cross-provider migration framework, local-to-Workspace demotion, distributed publication path, Workspace relocation, or new identity registry was created.

## Consumer/reference inventory

The shipped OS resolver is the canonical consumer boundary for user-owned capability qualified IDs. The host/runtime binds executions and receipts to qualified capability identity plus generation/digest, but there is no canonical cross-owner database of durable user-capability references that can safely be batch-rewritten today.

Reference repair for the proven fixture is therefore implemented at the resolver boundary through a verified promotion compatibility record: an exact request for the retired Workspace-qualified identity may resolve to the promoted local identity only when OS-owned active promotion evidence authorizes that relationship. The returned selection exposes the actual `local:<name>` identity plus a separate `promoted-to` relationship and `qualified_identity_preserved: false`.

Discovery continues to advertise only the real current local capability. The retired Workspace ID is not emitted as a duplicate canonical candidate.

Workspace and local providers remain directory-backed OS providers with deterministic `aiverse-package-sha256-v1` content evidence. Skills' immutable managed-generation lifecycle remains separate and unchanged.

## Final adaptive task list

- [x] **3.4-T1** Refresh System, OS and Skills refs and re-read Slice 3.4, the durable identity law, provider contract, placement planner, resolver and current managed Skills boundary.
- [x] **3.4-T2** Inventory actual qualified-ID consumers/reference surfaces and determine the narrowest admitted repair mechanism. Confirm there is no owner-published durable user-capability reference registry to mutate; exact resolver selection is the compatibility boundary for the proven fixture.
- [x] **3.4-T3** Freeze the admitted migration semantics before implementation: Workspace -> local only; new qualified identity; source digest/generation-bound plan; provenance/history receipt; exact-ID compatibility repair; managed/OS sources blocked; ambiguity/conflict/source drift fail closed; no silent promotion.
- [x] **3.4-T4** Implement the OS-owned promotion plan/apply transaction with verified staging, target conflict checks, source-drift invalidation, source-history preservation, deterministic receipt/compatibility metadata, source live-route retirement only after target verification, and idempotent replay/recovery behavior.
- [x] **3.4-T5** Extend explicit qualified-ID selection to consume only validated active promotion compatibility records, returning the real target identity plus relationship evidence. Add the mandatory cross-context YouTube transcript/book fixture and destructive-negative tests for stale plans, conflicts, ambiguity, managed sources and replay.
- [x] **3.4-T6** Document the owner boundary and validate exact current OS/Skills behavior. Skills remains unchanged because validation exposed no managed-provider lifecycle defect.
- [x] **3.4-T7** Record exact commits and CI evidence, close all Slice 3.4 acceptance criteria in the canonical roadmap, complete Safe Infrastructure Phase 3, and stop before Phase 4 / Slice 4.1.

## OS implementation

Implemented on OS main at `470ad89e6b96d898161dee36d4e4fa8064dd6a8d`, advanced from exact leased base `866359d877bfb3df0d8011d2d651a5ff947e21ca` with an expected-head guard after validating the full eight-file change set on a temporary branch.

Implemented surfaces:

- `scripts/capability-promotion.mjs`
  - contract `aiverse-capability-promotion-v1`;
  - only Workspace-owned personal sources are admitted;
  - exact source selection, provider, generation and `aiverse-package-sha256-v1` digest are validated;
  - target conflicts fail closed;
  - symlinks/special filesystem entries fail closed;
  - complete package is staged and digest-verified before publication;
  - pending evidence is written before source retirement;
  - source is re-verified before retirement;
  - original package is moved into hidden non-live Workspace promotion history instead of deleted;
  - active receipt records source/target qualified IDs, generations/digests, history evidence and explicit false identity continuity;
  - successful replay returns `already-promoted` with no duplicate mutation;
  - incomplete/pending transactions require recovery review instead of guessing.
- `scripts/capability-resolver.mjs`
  - adds explicit plan/apply promotion lifecycle;
  - requires the current trusted owning Workspace for promotion;
  - consumes only validated active promotion receipts when an exact retired Workspace-qualified ID is otherwise unavailable;
  - returns the real local target identity plus separate compatibility relationship evidence.
- `scripts/capability-placement.mjs`
  - admits only same-name Workspace -> local personal promotion;
  - keeps other cross-provider directions unsupported;
  - keeps `os` and `aiverse-skills` non-writable personal-promotion sources.
- `scripts/capability-resolver-cli.mjs`
  - exposes internal owner lifecycle operations `plan-promotion` and explicit `apply-promotion` bound to previewed generation/digest evidence.
- `system/architecture/capability-resolution.md`
  - documents owner boundaries, transaction ordering, identity semantics, compatibility repair and fail-closed behavior.
- `.github/workflows/capability-placement.yml`
  - validates syntax, practical placement, admitted promotion/reference repair and existing resolver/managed-generation regression.

No Skills source was changed.

## Mandatory fixture and destructive-negative proof

`tests` are implemented in `scripts/test-capability-promotion.mjs` and the updated placement test.

The mandatory cross-context fixture creates Workspace `alpha`, Workspace `beta`, and a user-owned `workspace:alpha:transcript-book` capability containing normal skill content plus custom/history files.

It proves:

1. Workspace `beta` cannot directly consume Workspace `alpha`'s private source before promotion.
2. Preview resolves the admitted target as `local:transcript-book` and explicitly reports that qualified identity is not preserved.
3. Apply copies and verifies the complete package before retiring the live Workspace source.
4. Custom files survive byte-for-byte in the reusable target.
5. The original package survives in non-live hidden promotion history with the same digest.
6. An active receipt records the source -> target relationship without claiming identity continuity.
7. From Workspace `beta`, an exact request for the retired `workspace:alpha:transcript-book` resolves the real `local:transcript-book` target through the active compatibility record.
8. The returned compatibility evidence identifies the originally requested ID and relationship `promoted-to` while the selection keeps its actual local identity.
9. Bare-name discovery from the second context selects the reusable local capability.
10. Discovery does not expose the retired Workspace identity as a second canonical copy.
11. Applying the same promotion again is a no-op (`already-promoted`).
12. Source drift after preview invalidates apply before promotion mutation.
13. A different existing local target blocks promotion without overwrite.
14. Attempting promotion from the wrong Workspace context blocks safely.
15. Managed `aiverse-skills` sources are rejected by the personal promotion flow.
16. Symlink-bearing automatic-promotion sources are rejected on platforms where the fixture can exercise symlinks.

## Exact CI evidence

### OS

Exact implementation head: `470ad89e6b96d898161dee36d4e4fa8064dd6a8d`.

`Capability Placement Contract` run `38306623956`: **SUCCESS**.

The single `placement` job passed:

- placement/resolver/promotion/CLI syntax;
- practical placement semantics;
- admitted Workspace-to-personal promotion and compatibility repair;
- scoped discovery and managed-generation selection regression.

`Repository QC` run `38306623950`: **SUCCESS**.

All three jobs passed:

- `qc`: **SUCCESS**;
- `adapter-integration`: **SUCCESS**;
- `skills-provider-integration`: **SUCCESS**, including installation of a real pinned Provider-v1 Skills generation and immutable-provider discovery/selection.

### Skills

Exact unchanged head: `d4a02888ba8d83c4a15ce1b538ffdafaaf83bee1`.

`Validate AI-Verse Skills` run `38298548847`: **SUCCESS**.

The validation job passed:

- registry validation;
- full Python unit-test discovery;
- installer list operation;
- full-profile install dry-run.

`Release Descriptor` run `38298549229`: **SUCCESS**.

No Skills code or lifecycle semantics were modified by Slice 3.4.

## Acceptance criteria

- promotion is owner-controlled and explicit: **PASS**; OS owns plan/apply and requires the trusted owning Workspace plus exact preview evidence;
- promotion is idempotent: **PASS**; successful replay is `already-promoted` with no duplicate live copy or repeated retirement;
- source/destination identity relationship follows the canonical Identity contract: **PASS**; source and target remain different qualified identities and all evidence records `qualified_identity_preserved: false`;
- provenance/history survives: **PASS**; receipt plus digest-verified hidden source archive preserve source relationship/history and full custom files;
- consumers/references continue through admitted repair or compatibility: **PASS**; exact old qualified-ID requests may use only an active validated OS-owned receipt to resolve the real promoted local target with explicit relationship evidence;
- no duplicate canonical copies remain: **PASS**; source live route retires only after target verification, history is hidden/non-live, and discovery exposes only the local target;
- source drift invalidates stale apply: **PASS**;
- conflicting target does not overwrite user state: **PASS**;
- ambiguous/unsupported filesystem structure fails closed: **PASS**;
- managed Skills and OS built-ins are not silently promoted: **PASS**;
- Skills continues owning managed immutable generations: **PASS**; exact-head Skills CI remains green and no Skills change was made;
- normal member placement UX does not require provider IDs or folders: **PASS**; practical placement from Slice 3.3 remains the member-facing surface;
- no generic identity registry, Workspace relocation, distributed publication path, or broad provider migration framework was introduced: **PASS**;
- mandatory cross-context transcript/book fixture passes: **PASS**.

## Phase result

Slice 3.4 completes the fourth and final Safe Infrastructure Phase 3 slice. The proven motivating owner migrations/decisions now include:

1. OS Workspace generation and conservative structural semantics;
2. evidence-backed decision that Workspace relocation is not currently admitted/required;
3. practical cross-provider placement semantics aligned with managed Skills ownership;
4. admitted Workspace-to-personal capability promotion with explicit new identity, provenance/history preservation and exact-ID compatibility repair.

No protected-law amendment was required.

Next execution unit after canonical roadmap closure is Phase 4 / Slice 4.1. Under the one-at-a-time rule, no Phase 4 implementation is started by this slice.
