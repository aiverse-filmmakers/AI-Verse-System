# AI-Verse Repository Network Audit 2026-10-12

**Status:** COMPLETE AUDIT BASELINE  
**Program:** `docs/DISTRIBUTION-SYSTEM-PROPAGATION-IMPLEMENTATION-PLAN.md`  
**Slice:** 1.1 - Audit the live repository network and existing safety machinery  
**Scope:** AI-Verse-System, ai-verse-distribution, and the five currently shipped Core owners  
**Audit rule:** evidence only. No product/runtime implementation change is authorized by this document.

## 1. Audit boundary and starting refs

Slice 1.1 began after a scoped live refresh and before any product implementation change.

Starting refs:

| Repository | Stable GitHub repository ID | `main` at slice start |
|---|---:|---|
| `AI-Verse-System` | `1367664026` | `b9e803a27184c9f148f32157e9025157fd942c9b` |
| `ai-verse-distribution` | `1350081263` | `def78ade8b11d415b8111f6b5f0d267044520769` |
| `AI-Verse-OS` | `1361862361` | `64f7325444d18f94c9d4755d32eb89f3468bda6b` |
| `AI-Verse-Brain` | `1362233598` | `69f7912eeb35f0178f6952ff0554aec8d7f2c496` |
| `AI-Verse-Memory` | `1361910454` | `f1327be48ba2ee0043959021365e6dbb9dcb1d3a` |
| `AI-Verse-Skills` | `1362243580` | `afde5c06307fba7d074de2929c2eb6c3dc6bdab8` |
| `AI-Verse-Data` | `1364457521` | `f8978f8f7a1bc94edecddc2662112233289159a3` |

The only repository write before this audit record was the execution-tracker bookkeeping commit `20515a27625ca8924a40c01db2fc964ffaa798c0` in AI-Verse-System. It marked Slice 1.1 IN PROGRESS, recorded the starting refs, and derived the bounded audit task list. It changed no product/runtime implementation.

## 2. Current shipped Core composition

Distribution release set `release-sets/core-first-run-rc1-2026-10-12.json` is recorded as `released` and pins:

| Component | Exact Distribution ref at audit start | Same as owner `main` at audit start |
|---|---|---|
| OS | `64f7325444d18f94c9d4755d32eb89f3468bda6b` | YES |
| Brain | `69f7912eeb35f0178f6952ff0554aec8d7f2c496` | YES |
| Memory | `f1327be48ba2ee0043959021365e6dbb9dcb1d3a` | YES |
| Skills | `afde5c06307fba7d074de2929c2eb6c3dc6bdab8` | YES |
| Data | `f8978f8f7a1bc94edecddc2662112233289159a3` | YES |

The release set is a child of `core-stable-2026-10-10` and carries explicit transition policy. Distribution `main` is newer than the component refs because U35 real-member pilot tooling is active in Distribution itself. That Distribution-only movement is not evidence that a component changed.

Distribution's `docs/RELEASE-SET-CONTRACT.md` already establishes these useful controls:

- release sets are the smallest unit Distribution may call compatible;
- public-beta Git component identity is a full immutable 40-character SHA;
- moving branches and `latest` are not admitted identities;
- component source revision, Distribution companion dependency locks, and canonical user/domain state are distinct truths;
- only `released` sets may be selected by install/update/rollback;
- rollback is software rollback and does not silently rewind owner state;
- new release promotion requires exact artifacts, compatibility, lifecycle adapters, clean-machine acceptance, deterministic dependency evidence, explicit update/rollback impact, authority/preservation rules, and System documentation synchronization.

## 3. Core owner acceptance and release-descriptor reality

All five Core owners have native GitHub Actions validation surfaces. They are not uniform, which is an audit fact rather than a defect to normalize inside Slice 1.1.

Observed owner-local validation surfaces include:

- OS: release/acceptance, CLI, Data host-boundary, Brain permission/direction, five-component/public-beta, Purpose Context, update request, and other owner/composed workflows.
- Brain: `ci.yml`, `os-direction-contract.yml`, `release-descriptor.yml`, `skills-receipt-contract.yml`.
- Memory: `test.yml`, `migration-handoff-atomicity.yml`, `release-descriptor.yml`.
- Skills: validation, readiness, install, lifecycle containment, release descriptor, Video Editor acceptance, and generation-lease workflows.
- Data: `ci.yml`, `five-component-acceptance.yml`, `release-descriptor.yml`, `release-smoke.yml`.

Current component release descriptors do not line up with the exact refs Distribution currently pins:

| Component | Descriptor status | Descriptor `revision` | Distribution-pinned ref | Exact match |
|---|---|---|---|---|
| OS | `accepted` | `9600929b946746c25c64e48471fcc83031fddda9` | `64f7325444d18f94c9d4755d32eb89f3468bda6b` | NO |
| Brain | `development` | `75e1d713a422eec4caea89bdab5053cae23218c6` | `69f7912eeb35f0178f6952ff0554aec8d7f2c496` | NO |
| Memory | `development` | `3f715bf43c8dc5f0ad8888e07d857b581482569e` | `f1327be48ba2ee0043959021365e6dbb9dcb1d3a` | NO |
| Skills | `development` | `fa455961c17691862bd86b7e0f658690e9ecb86d` | `afde5c06307fba7d074de2929c2eb6c3dc6bdab8` | NO |
| Data | `development` | `5cbf9908440ca7e11506991ba1dd7d3344f2b1fd` | `f8978f8f7a1bc94edecddc2662112233289159a3` | NO |

This must not be simplified into “the owner refs are untested.” Owner-local and Distribution qualification evidence exists outside those current descriptor files. The narrower proven finding is that the current descriptor surface cannot, by itself, establish accepted owner evidence for the exact refs currently shipped.

There is also a schema/implementation split:

- System contract `docs/COMPONENT-RELEASE-DESCRIPTOR-CONTRACT.md` and `contracts/component-release-descriptor.schema.json` define `ai-verse.component-release/v1` with release status `candidate | accepted`.
- Brain, Memory, Skills, and Data currently publish/validate a third local `development` status and allow its evidence arrays to remain empty.

Therefore the canonical v1 System schema and four owner-local descriptor workflows are not one executable contract today.

### Compatibility/versioning already exists locally

Compatibility/versioning is not absent. Existing examples include:

- Brain has explicit `protocol/` contracts, many `schemas/*.schema.json` files, owner tests, release metadata, and version surfaces.
- Memory has explicit `protocol/`, `migration/`, manifest, tests, and release metadata.
- Skills has version, package-generation, lifecycle and readiness machinery.
- Data has package/version metadata, migrations/state semantics, release metadata and dedicated acceptance/smoke workflows.
- OS has host contracts and cross-component owner-boundary acceptance surfaces.

The later program should reuse/extend these owner-local mechanisms rather than invent a parallel compatibility owner in Distribution.

## 4. Distribution safety machinery that already exists

The audit found substantial existing machinery that later slices must REUSE or EXTEND rather than replace.

### Exact composition and candidate evidence

Distribution already has:

- append-only style `release-sets/*.json` with exact immutable component refs;
- `compatibility/matrix.json`;
- exact dependency locks, including revision-bound Data companion locks;
- candidate snapshots under `qualification/**`;
- Git-lineage verification tooling and CI;
- clean-machine workflows;
- composed acceptance workflows;
- purpose-specific qualification records;
- a copied immutable System contract snapshot under `.qualification/system-contract-<ref>/` with origin, schemas, validators and tests.

`qualification/core-stable-2026-10-10/candidate.json` proves candidate refs can already be frozen, ancestry-checked and bound to dependency digests before release admission.

### Update, preservation and rollback

The existing Core update program has already built a conservative update-sensitive path inventory in `docs/CORE-UPDATE-PATH-INVENTORY.md`. It treats unknown files, unknown children, local edits, symlinks, unreadable paths, missing provenance and ambiguous ownership as preservation boundaries.

The current preservation implementation in `src/aiverse_distribution/preservation.py` already fingerprints canonical member files, workspaces, local Skills, Distribution history, and Data records. Data comparison is semantic rather than raw SQLite-byte comparison so an admitted owner migration can alter physical/schema layout without losing member rows.

`qualification/core-update-program-u35/qualification.json` records passing exact-transition admission, populated-member preservation, dirty-local-edit conflict handling, interruption recovery, repeat/no-op/resume behavior, final status/doctor and a six-job Linux/macOS/Windows x Python matrix. It does not advertise rollback because no exact reverse-transition preservation qualification exists.

The same U35 record keeps the owner real-installation pilot as `pending-external-execution` and records `release_gate: blocked-until-owner-real-installation-pilot-passes`. This is separate from the release-set file's packaging `released` state and must remain separate in later governance.

### Lifecycle receipts and crash recovery

`src/aiverse_distribution/state.py` already provides:

- `locks/current.json` as the active Distribution receipt;
- monotonic receipt generations;
- atomic replacement;
- archived previous receipts in `history/`;
- cross-process lifecycle locking;
- `pending-lifecycle.json` as crash-recovery authority;
- exact-operation resume semantics;
- stale-receipt and unresolved-owner-effect failure modes.

This is existing preservation/recovery machinery, not a new system to replace.

### Reproducibility evidence

Current reproducibility evidence is substantial but distributed across several durable repository records:

- exact release-set refs;
- compatibility data;
- dependency-lock digests;
- frozen qualification candidate files;
- System contract snapshots;
- qualification JSON records;
- local Distribution current/history receipts.

The later durable-release-receipt slice should consolidate only the missing admitted-release reconstruction binding. It must not duplicate data already canonical in these records.

## 5. Member-facing versus maintainer/source-only boundary

### Existing member-facing boundary

The canonical member-visible root is the OS project root.

`ProjectLayout` requires the private Distribution tool stack to be a sibling, non-nested directory such as:

`<project-parent>/.ai-verse-tools/<project-identity>/`

It refuses an occupied project unless a matching project receipt and Core installation receipt prove the layout. It does not treat a directory marker alone as authority.

`project_install.py` additionally requires the Distribution source checkout to remain outside the member OS destination. Private Python, Node/npm, downloads, staging, Distribution state and lifecycle tooling remain in the sibling tool stack.

The generated member-facing Distribution helper is narrowly placed under:

`.aiverse/extensions/project-bootstrap/INSTRUCTIONS.md`

and is registered through the OS extension registry. Distribution's source `AGENTS.md`, `CLAUDE.md`, qualification records, tests and governance documents are not copied into the member project by this path.

The installed OS project intentionally exposes its runtime contract and generated project adapters such as `AGENTS.md`, `CLAUDE.md`, `AI-VERSE.yaml` and capability adapters. Those are member/runtime surfaces, not evidence that internal repository-network governance should be copied there later.

### Fail-closed bootstrap-owned writes

Distribution tracks hashes for bootstrap-owned files. It only replaces a previously owned file when the existing digest still matches its recorded owned or pending digest. Otherwise it preserves the existing/local file and refuses the write.

The Core path inventory additionally protects operator profile/preferences/goals, Brain direction/history, Memory history/provenance, workspaces, Data databases, connections, automations, local/workspace Skills, extensions, custom files, project history and unknown content.

### Maintainer instruction coverage

Maintainer/source guidance is uneven across Core today:

- Distribution has a root `AGENTS.md` describing canonical install/update routing and fail-closed preservation.
- OS has a root `AGENTS.md` that participates in the installed runtime contract.
- Brain, Memory, Skills and Data do not currently expose the same root-level cross-repository maintainer handoff surface.

This is a governance coverage gap for later Wave 1 handoff work, not a reason to copy global governance wholesale into each repository.

## 6. System ownership and Purpose Context truth

The current System Blueprint still provides the canonical big-picture ownership map:

- OS owns host constitution, workspace/scope, current operating context, host composition, routing and permission floor.
- Brain owns strategic intent/direction while handed over, goals, initiatives, verification and learning.
- Memory owns historical atomic memory/provenance/supersession and derived recall index state.
- Data owns structured current operational truth.
- Skills owns capability package distribution and immutable generations, not execution authority.

This owner separation remains compatible with the current program direction.

### Proven Purpose Context canonical drift

`docs/FINAL-AI-VERSE-BLUEPRINT.md` is stale in two material places:

1. Section 14A still says Purpose Context “should add” a first-class layer and calls it an `INTENDED derived context layer`.
2. Its implementation sequence still labels Purpose Context `EARLY P1` and describes it as future work after the then-active repair program.

Later exact evidence proves implementation and admission happened:

- `docs/PURPOSE-CONTEXT-SLICE-12.3-CLOSURE.md`: COMPLETE / ACCEPTED qualification against exact frozen Core refs and applicable Agent/runtime refs.
- `docs/PURPOSE-CONTEXT-SLICE-12.4-CLOSURE.md`: COMPLETE / ACCEPTED independent review, 12/12 questions accepted.
- `docs/PURPOSE-CONTEXT-SLICE-12.5-CLOSURE.md`: COMPLETE / ACCEPTED Distribution admission and explicit statement that Distribution `main` resolved Core to `core-purpose-context-public-beta-2026-10-09` at that point.
- Distribution `release-sets/core-purpose-context-public-beta-2026-10-09.json`: `released`, exact refs frozen, accepted qualification and independent-review evidence recorded.

Classification:

`CANONICAL-DRIFT-DETECTED`

- severity: `WARNING`
- scope: `Core / System`
- stale side: Blueprint implementation/readiness wording
- trusted evidence: exact System closure records plus admitted Distribution release set
- automatic action: NONE
- required later action: reconcile System forward in Slice 3.3 without regressing the accepted implementation

This does not transfer Purpose Context ownership to Distribution and does not authorize automatic Blueprint rewriting during the audit.

## 7. Drift and gap classification

### Finding A: component release-descriptor executable-contract split

`CANONICAL-DRIFT-DETECTED`

- severity: `BLOCKING`
- scope: `Core release-governance evidence`
- finding: System v1 descriptor schema accepts only `candidate | accepted`, while four Core owner workflows/descriptors use `development`; no current owner descriptor exactly matches the current Distribution-pinned ref.
- impact: the current descriptor surface cannot be used as the sole owner-acceptance gate for the exact shipped Core composition.
- what this does not prove: it does not prove the current runtime composition lacks other owner/Distribution test evidence.
- required later action: Slice 1.2 must inventory the exact reuse/extension path; Slice 4.1 must keep one canonical descriptor format; Slice 5.1 must bind exact owner acceptance evidence before governed candidate admission.

### Finding B: Purpose Context Blueprint lag

`CANONICAL-DRIFT-DETECTED`

- severity: `WARNING`
- scope: `Core / System`
- finding: Blueprint still describes accepted/admitted Purpose Context as intended/future.
- required later action: Slice 3.3 evidence-first forward reconciliation.

### Finding C: uneven Core maintainer handoff surface

- severity: `WARNING`
- scope: `Core maintainer governance`
- finding: cross-repository maintainer handoff guidance is not uniformly discoverable across the five Core owner repositories.
- required later action: Slice 4.2, using each owner's real repo conventions and preserving member isolation.

### Finding D: durable release reconstruction is distributed, not yet one receipt

- severity: `INFO`
- scope: `Distribution reproducibility`
- finding: exact refs, locks, qualification snapshots and evidence are durable, but the program's target single compact admitted-release reconstruction receipt is not yet a canonical surface.
- required later action: Slice 5.4 should EXTEND/reuse current durable evidence rather than create a parallel release database.

### Finding E: current U35 owner-real-install pilot remains external/pending

- severity: `INFO`
- scope: `current Core transition program`
- finding: U35's repository qualification bundle passes its automated matrix but retains a separate external real-install pilot gate.
- required action here: none. Slice 1.1 only records it and must not interfere with the independent Core update program.

## 8. Existing protection classification for the next slice

Evidence-backed starting classification for Slice 1.2:

| Concern | Audit classification |
|---|---|
| Exact release-set SHAs and release-set semantics | REUSE |
| Distribution compatibility matrix | REUSE / evaluate extension |
| Dependency-lock provenance/digests | REUSE |
| Candidate freeze and Git ancestry evidence | REUSE |
| System contract snapshot in Distribution qualification | REUSE / evaluate generalization |
| Core update path inventory | REUSE |
| Member-state preservation fingerprinting | REUSE |
| Fail-closed local-edit/unknown-file handling | REUSE |
| Distribution lifecycle current/history/pending receipts | REUSE |
| Component owner CI/acceptance | REUSE, then normalize handoff semantics |
| Component release-descriptor format | EXTEND/RECONCILE, do not create a second format |
| Repository Registry/Repository State/Drift Watchdog | MISSING by target definition, later System work |
| Purpose Context Blueprint wording | RECONCILE later, do not roll code back |
| Core maintainer handoff guidance | EXTEND per owner conventions |
| Compact admitted-release reconstruction receipt | EXTEND existing evidence |
| Broad internal governance in member install | PROHIBITED |

## 9. Slice 1.1 acceptance disposition

- Exact current implementation and release topology: EVIDENCED.
- Existing protections identified before replacements are proposed: PASS.
- Purpose Context drift classified from exact evidence: PASS.
- Current Core repository list and stable identities: EVIDENCED.
- No product/runtime implementation change before audit recording: PASS.

The audit itself introduces no implementation, release, migration, payload or ownership change. Its output is evidence for Slice 1.2.
