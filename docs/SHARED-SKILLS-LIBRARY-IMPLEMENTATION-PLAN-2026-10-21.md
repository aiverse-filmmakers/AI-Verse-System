# Shared Skills Library — implementation plan

Date: 2026-10-21. Status: COMPLETE — closed 23 October 2026.
Implementation milestones: 6/6 complete. Accepted source, qualified Core release, personal rollout and explicit manual skill migration are complete.

## Authorization and scope

The operator approved the researched first-layer architecture: reusable skills
created while working in any AI-Verse workspace must be available from other
authorized workspaces, with one discovery experience, explicit identity and safe
updates. Deliver through canonical component repositories and Distribution,
then update the member installation through its supported lifecycle.

Clarification, 21 October: the operator requests a separate manual move of his
local skills only after the shared implementation is complete. Core must not
automatically reorganize his skills. Fresh installations use the new layout from the start. Deliver a small explicit
import workflow for members bringing skills, preserve existing skills and
references on update, and exclude a broad automatic legacy-reorganization
framework. The personal manual move follows completed shared delivery.

The subsequent Skills-repository curation (foundation/imported/first-party
organization, consolidation, retirement and an understandable change log) is
recorded as a separate follow-on. No skill deletion or broad content rewrite is
part of this program. Dashboard work and the closed repository-network program
are not reopened.

Planning depth: extended, because the work crosses component owners, persistent
member state, workspace isolation and release/migration boundaries. This is the
one living implementation plan; supporting evidence should link here.

## Starting evidence

Inspected owner sources:

- OS main `906d70d0c89621a805515d769ee601027c294ef4`.
- Skills main `23779f10515951ac92c83cba34a1a868c02c4d87`.
- Distribution main `66e0ac2c5c631d450cf0708fec208b30fb784402`.
- System main `3b414e3c77dbc23e43a9af59b4a18a16d4806361`.
- Admitted member release: `core-member-polish-candidate-2026-10-21`.

Current flow: the host selects an OS scope, OS combines built-in, managed Skills,
personal local and only the bound workspace provider, then selects a qualified
capability. Exact short-name collisions silently use provider precedence;
protected OS aliases use the OS capability. The Skills root defaults to a home
path unless a caller supplies the installation-specific root. Personal direct
authoring and managed learned-package promotion are separate paths. Existing
workspace-to-personal promotion preserves originals and records compatibility.

## Permanent outcomes and ownership

1. Reusable procedure is member-owned/shared by default after admission. The
   workspace where it originated is provenance, not an implicit access limit.
2. Context-specific values, private resources, credentials, Connections,
   permissions and current direction remain with their canonical scoped owners.
   Unproven/private legacy workspace packages remain restricted until reviewed.
3. A unified catalog does not merge ownership. OS owns routing/access/bindings;
   Skills owns reusable package authoring, revisions and admission; Brain routes
   learned candidates; Distribution composes lifecycle; System governs releases.
4. One original package/revision has one owner. Indexes and runtime adapters are
   derived. Existing immutable managed generations remain immutable.
5. A friendly name is not identity. Colliding packages remain discoverable and
   explicitly selectable. An explicit source/identity choice wins; an ambiguous
   short name must not silently execute a materially different package.
6. Old references, personal files, unknown runtime files and package provenance
   survive. Imports and explicit moves are previewable, retry-safe and recoverable; no guessed
   cross-workspace reads or bulk promotion of private content.
7. All entry points bind to the same installation's provider configuration.
   Missing/unhealthy configured roots are reported, not replaced by a different
   global installation. Separate member/test profiles remain isolated.
8. Skill availability does not grant permission or guarantee runtime readiness.
   Catalog metadata is bounded; complete authorized search remains available
   when initial model context omits packages.

The existing Provider v1, placement v1 and promotion contracts remain valid for
legacy callers. Any new metadata must be explicitly versioned/additive or have
an owner-reviewed compatibility change. Existing protected OS operations remain
available by qualified identity; external same-named skills remain selectable.

## Requirements and observable acceptance

| ID | Observable requirement | Proof / failure case |
|---|---|---|
| R01 | A validated reusable skill authored in workspace A is discovered and selected in B | Real package create/import through owner, then scoped discovery in both; private A content absent |
| R02 | Workspace settings attach to a shared identity/version without another editable procedure copy | A/B bind different non-secret inputs; shared revision unchanged; incompatible/missing binding is explicit |
| R03 | OS, managed, personal and supported registered external sources have one searchable catalog | Same installation metadata from native/CLI/Brain paths; unavailable external source visible as diagnostic |
| R04 | Same names do not silently hide a requested package | Both identities visible; explicit publisher choice honored; ambiguity/default selection is explicit and scoped |
| R05 | New and learned creation share placement/admission semantics | Generic validated procedure shared; private/uncertain candidate stays restricted/draft; no privilege expansion |
| R06 | Old workspace/personal/learned skills and references survive | Fingerprints/originals and compatibility receipts preserved; repeat import idempotent; same-name conflicts not overwritten |
| R07 | Updates keep source ownership, versions and recovery | Publisher update cannot overwrite member package; interrupted import/update recovers; old supported versions selectable |
| R08 | No workspace information/permission escapes through reuse | Traversal/symlink, private resource, wrong-scope and secret admission cases refused; bindings cannot grant access |
| R09 | Fresh and populated member installs converge through public lifecycle | Official install/update/upgrade, final owner doctors and preservation checks on supported platforms |
| R10 | Documentation and adapters teach the same current route | Correct stale Claude-authoring guidance; ordinary language creation does not require choosing internal providers |

## Reuse and design decisions

- REUSE immutable Skills generations, security admission, governed learning,
  package digests, provider-v1, OS scoped resolver, promotion compatibility and
  Distribution last-known-good recovery.
- EXTEND the personal-library authoring/lifecycle and explicit shared identity
  metadata, scoped bindings/preferences and installation-root resolution.
- EXTEND deterministic name selection to return alternatives/ambiguity rather
  than discarding nonwinning identities.
- RETIRE ordinary direct authoring in generated `.agents/skills` or
  `.claude/skills` surfaces and accidental workspace-private default for reusable
  methods. Preserve existing files in place; use explicit import for relocation.
- No new service, database owner, background agent or strategy store is needed.
  Exact storage/API details are derived in each owner slice from current code.
- Imported/foundation directory curation is deliberately deferred until stable
  identity and catalog behavior can preserve references through that work.

## Fixed implementation outcomes

### 1 — Contracts and current-state characterization (COMPLETE LOCALLY)

Owner: System with OS/Skills contract definitions. Requirements R01–R10.
Tasks: inspect current owner code/contracts; map observed caller flows; settle
identity/placement/binding/import semantics; publish one plan and requirement
matrix. This slice changes no member files. Acceptance: bounded contract covers
all requirements and preserves existing owner/version boundaries.

Completion artifact: [structure and behavior contract](SHARED-SKILLS-LIBRARY-CONTRACT-2026-10-21.md).
Source characterization and R01–R10 mapping are complete; documentation links and
scope consistency checked. This is local design completion, not merged owner
approval or released implementation. Step 1 was completed separately; the operator subsequently authorized step 2 only.

### 2 — Skills-owned shared personal package lifecycle (COMPLETE LOCALLY)

Owner: Skills. Depends on 1. R01, R05–R08.
Extend existing authoring/admission/revision machinery for central reusable
member packages and legacy personal imports, with explicit ownership/scope,
source provenance, revisions, audit receipts and safe preview/apply. Never
silently activate proposals or expose workspace-private learned content.

Completion: Skills local commit `ac38ab8`; public CLI and API support read-only
import preview, explicit apply, stable IDs, retained immutable revisions,
revision selection, doctor, source/provenance retention and owner locking.
Existing learning behavior is unchanged; routing integration remains step 4.
Evidence: [step 2 completion](SHARED-SKILLS-LIBRARY-STEP-2-2026-10-21.md).

### 3 — Unified OS discovery, selection and workspace bindings (COMPLETE LOCALLY)

Owner: OS. Depends on 1–2. R01–R04, R06, R08, R10.
Use one configured provider view across callers; preserve legacy IDs; show all
colliding identities; support explicit scoped choice and non-secret workspace
configuration for shared packages. All access/containment checks still apply.

Completion: OS local commit `fde3a27`; Node discovery, bindings, collision
selection, version pins, configuration and read-only registered external sources
implemented. Existing resolver/promotion/placement and real owner fixture pass.
Evidence: [step 3 completion](SHARED-SKILLS-LIBRARY-STEP-3-2026-10-21.md).
Cross-runtime integration remains step 4, not acceptance inferred from Node tests.

### 4 — Learning, runtime and Distribution integration (COMPLETE LOCALLY)

Owners: Brain/OS runtime bridge/Distribution, with Skills authoring owner.
Depends on 2–3. R03, R05, R07–R10.
Converge learned and ordinary creation routing, install-specific root binding,
canonical lifecycle preview/apply and adapters. Generate runtime peers through
their owner tooling; preserve unknown files and native trust decisions.

Completion: four owner commits recorded in [step 4 completion](SHARED-SKILLS-LIBRARY-STEP-4-2026-10-21.md).
Actual owner-composition fixture and focused regressions pass. Native independent
callbacks, owner review/merge and release/platform qualification remain step 5.

### 5 — Fresh install, skill import and release qualification (COMPLETE)

Owners: Distribution and component owners. Depends on 2–4. R01–R10.
Exercise fresh/public install, explicit skill import and populated member updates, collisions,
workspace privacy, interruption, retry, old references and recovery. Bind exact
source refs to real evidence; publish through normal Core admission/promotion.
No qualification based solely on synthetic metadata or file presence.

### 6 — Member rollout, audit and handoff (ACTIVE)

Owners: Distribution/local installed owners/System. Depends on 5. R01–R10.
Deliver through the canonical updater with preservation and final owner
health; only after shared delivery, manually move the operator's local skills
with an inventory, retained originals and a move log; verify actual cross-workspace creation/discovery and exact selected
revision. Record completion/limitations and the separate curation backlog. Subsequent
Skills-repository curation must have its own inventory and consolidation/retirement
plan before content changes; it is not silently included in this first layer.

## Risk and recovery decisions

- Scope/permission: shared availability never shares Connections, secrets,
  private files or strategic authority. Retrieval and execution enforce scope.
- Untrusted packages: preserve security/admission gates and origin; validation
  does not imply authorization. No private package is made public.
- Persistence/concurrency: preview includes exact source/target revisions;
  stale apply refuses; owner transactions/locks and audit receipts govern writes.
- Update/rollback: retain originals and admitted last-known-good; no manual
  reset/reclone or replay of old publication receipts.
- Runtime compatibility: CLI/native/Brain use the same identities; native
  runtime limitations must be explicit rather than fabricated by an adapter.
- Performance: bounded metadata/targeted package loading; measure actual
  discovery behavior in slice 3 before adding caches or services.

## Progress and next action

Implementation milestones: 6/6 complete (100% of milestones).
Steps1–4 have implementation evidence. OS/Skills/Brain source changes and accepted
release descriptors are merged; System source snapshots and qualification records
are merged. Distribution PR75 is merged with qualified Core promotion.
Final owner sources: OS4a134190355e590f4f52e0607ca13bbddd1ac36e,
Skills390c6e1633afc809040bd1159840045f4f9ff27e and
Brain7e6f7a7e8a3d541815bc7f65c11dca7824c35d8f.
Current released Core is core-shared-skills-candidate-2026-10-23-v4; superseded
v1/v2/v3 evidence is historical and must not be promoted. V4 fixes exact
Distribution lifecycle mapping for the final owner revisions.558 final local tests pass
with11 skips; authenticated candidate admission passes. Three-platform and isolated
populated-update qualification passed; all62 final publication checks passed.
Actual canonical member update, separate optional package upgrade, explicit manual imports and bounded audit are complete. No originals were deleted.
Execution pointer: NONE. See the step6 completion evidence.
See STEP-5 evidence and the private execution pointer for dated run IDs/results.

## Shared release published — 23 October 2026

Distribution PR75 merged at2257ecb23f5aa21d033d85b48f0fdadc59bd0c23 after all62 checks passed on exact head2219c65c6c723ed9c5d063beaf686e8fa84707df. Live Core default is core-shared-skills-candidate-2026-10-23-v4. Final corrected Core run39966657286 passed every platform/job. Canonical whole-product qualification and normal synchronized promotion have zero debt; superseded evidence remains historical. Step5 is complete.

Historical pre-update checkpoint: actual member repeated bootstrap refreshed private tooling and stopped without overwriting a new root package.json customization. Network-enabled official-source preview verifies allthree changed owner descriptors and compatible infrastructure, but package.json is outside the existing owner-adoption allowlist and remains review-required. At that checkpoint step6 remained incomplete; no actual Core activation or manual skills move had occurred. Exact original package, lock and script copies plus134 selected preservation fingerprints are retained privately. Resolve through an explicitly reviewed local customization decision; do not weaken the updater's unknown-path refusal.


## Final personal rollout — 23 October 2026

Step6 is complete. The operator explicitly approved isolating the personal tool dependencies and reconciling the exact Core manifest, with original files and credentials preserved. The canonical update then succeeded, allfive component health checks passed, and installed/latest OS version matched0.3.8. The selected138-file personal preservation baseline was unchanged by Core update. The separate optional package upgrade reports READY with six trusted hooks and execution/review observed.

Twenty manually approved skill imports are verified:18 shared and2 workspace-restricted. All20 source packages are unchanged, import retries deduplicate, library doctor passes, and66 resolver checks confirm shared discovery and private isolation. The manual migration is private member work, not an automatic Core migration feature. No private skill contents or member credentials are published here.

Live postmerge Core workflow39969515000 and System workflow39970078008 succeeded. See [step6 completion](SHARED-SKILLS-LIBRARY-STEP-6-2026-10-23.md) for bounded evidence and follow-ups. Skills repository content curation remains a separate effort.
