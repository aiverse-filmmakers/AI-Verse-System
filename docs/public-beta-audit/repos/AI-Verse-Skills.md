# A1.5 — Independent Repository Audit: AI-Verse-Skills

**Audit date:** 2026-09-15  
**Frozen ref:** `8c321c03421a2e0e470280cc40e588a27c1a510d`  
**System baseline:** `a33abb2f3f839058037c90569305b43fa9be0a52`  
**Status:** COMPLETE  
**Standalone verdict:** DOGFOOD BLOCKED  
**R-a:** COMPLETE / PASS  
**R-b:** COMPLETE / MATERIAL FAILURES FOUND  
**R-c:** COMPLETE / BLOCKED  
**Findings:** `WSA-2026-016` through `WSA-2026-019`  
**Next:** A1.6 AI-Verse-Data

## Independence and drift control

A1.5 used only the frozen Skills repository, Skills-owned tests/workflows, and Skills GitHub metadata/history. No sibling implementation was used to fill a standalone gap.

At task start and pre-write recheck:

- Skills main remained `8c321c03421a2e0e470280cc40e588a27c1a510d`.
- System main remained `a33abb2f3f839058037c90569305b43fa9be0a52`.
- no open Skills/System PRs existed;
- no Skills product file was modified;
- Dashboard MC1.4 remained paused.

## Reconstruction

The frozen tree contains 303 tracked entries. Registry metadata declares 20 foundation capabilities, 100 employee capabilities, and 16 support packages.

Skills owns reusable procedure packages, exact source pins, immutable generations, provider metadata, admission/trust projections, readiness projections, execution receipt validation, and governed Skill Workshop state.

Skills does not own workspace identity, secrets, Connections, approvals, scheduling, Brain strategy, or OS execution authority.

The repository implements the separation:

`integrity != admitted != trusted != ready != authorized`

### Immutable generations

Installed package bytes are stored under `.aiverse/generations/<generation_id>/`; `.aiverse/active.json` is the mutable activation pointer.

Normal install/update builds and verifies a new stage, commits one immutable generation, verifies it, and then atomically changes the active pointer.

Executions pin one exact generation before loading package content. Normal update, rollback and uninstall preserve prior generation bytes.

### Provider and admission

Provider contract: `aiverse-capability-provider-v1`.

Provider verification enforces relative package paths, physical generation containment, valid `SKILL.md`, safe package symlinks, exact package digests, exact generation identity, exact manifest/index binding and exact installed capability membership.

Admission recomputes integrity, deterministic security findings, source trust, ownership, license and redistribution policy. Admission metadata never grants execution authorization.

### Readiness

Authenticated operators require a registered live probe proving identity, authentication, reachability and usability. Static environment hints or binary presence alone do not become readiness.

### Execution receipts

`aiverse-execution-receipt-v2` binds request fingerprint, scope, action class, operation, provider, capability, generation and package digest.

Successful consequential side effects require OS-origin effect verification. Strong evidence cannot be self-asserted by unsupported sources. `trace_id` is correlation only.

### Governed learning

Learning modes are off/propose/auto, with propose as default.

Evaluation gates include security, duplicates, permission/dependency expansion, Connection/credential expansion, provenance, scope, ownership, risk, confidence, current generation and target package digest.

Production changes create a new verified immutable generation. Protected first-party/curated packages are not autonomously rewritten. Proposal rollback is compare-and-set.

### Video Editor

Frozen Skills includes the accepted Video Editor integration.

PR #14 final head: `47ca55b11850b1432882a1c1c015e0a253d4c1d0`.

Dedicated release acceptance run `34901198219` passed. Release evidence pins Nate source `b1afdb1dcbcad39dd27638ea699f132fe44ce6df` and HyperFrames `0.8.40@cfe5dcfad310ced2a5844998628daa2b8a0f53d7`.

## Enforcement findings

### C-A1.5-001 — lifecycle controller containment is incomplete

Package-level containment is strong, but the lifecycle controller path `root/.aiverse` is not independently validated as a non-link, root-confined controller before generation/state/retention operations derive from it.

**Finding:** `WSA-2026-016`.

### C-A1.5-002 — stale lifecycle lock recovery is age-only

Docs state lifecycle mutations are serialized and only stale locks recover. Implementation uses the age threshold without verifying recorded-holder liveness.

**Finding:** `WSA-2026-017`.

### C-A1.5-003 — retention cleanup does not account for active execution pins

The immutable-generation contract gives one pin for an execution lifetime. Retention cleanup protects current/history and learning provenance, but does not track live execution pins.

**Finding:** `WSA-2026-018`.

### C-A1.5-004 — accepted component identity has drifted from current source

Accepted component descriptor:

- version `1.1.0-beta.1`;
- revision `042fda1ea2ddd8b79b74f1db9d3f65212953b64a`.

Frozen current main is 190 commits ahead while still reporting `1.1.0-beta.1`. Repository bootstrap follows mutable `main`.

**Finding:** `WSA-2026-019`.

## WSA-2026-016 — Skills lifecycle controller containment defect

**Severity:** BLOCKER  
**Confidence:** PROVEN  
**State:** OPEN  
**Root area:** destructive lifecycle / filesystem containment

The lifecycle controller does not apply the same physical-containment law that provider package paths use. State and retention operations can therefore resolve through an unsafe controller location.

**Closure evidence:** introduce one controller-path safety primitive, reject unsafe controller indirection, prove controller/generation/state paths stay within the selected root, and add platform lifecycle containment tests.

## WSA-2026-017 — lifecycle lock can be reclaimed while its owner is still live

**Severity:** HIGH  
**Confidence:** PROVEN  
**State:** OPEN  
**Root area:** lifecycle concurrency / serialization

The lock records PID/token metadata but the 300-second recovery branch does not validate holder liveness.

**Impact:** long install/update/rollback/learning operations can overlap a second mutation and lose semantic state updates.

**Closure evidence:** holder-aware stale recovery and tests for both a live old holder and a dead/crashed holder.

## WSA-2026-018 — retention cleanup can invalidate an in-use generation pin

**Severity:** MEDIUM  
**Confidence:** PROVEN  
**State:** OPEN  
**Root area:** immutable generation retention

Retention protects active/history generations and learning rollback/archive provenance, but has no live execution lease/reference mechanism.

**Impact:** a valid long-running execution can lose its pinned generation during explicitly requested retention maintenance.

**Closure evidence:** execution-generation leases or equivalent in-use protection plus retention tests.

## WSA-2026-019 — accepted beta identity and bootstrap are not immutable-current aligned

**Severity:** LOW  
**Confidence:** PROVEN  
**State:** OPEN  
**Root area:** release/version/bootstrap reproducibility

Frozen main is 190 commits beyond the accepted component revision while still using the same distribution version. Bootstrap follows mutable `main`.

**Closure evidence:** distinct post-release versioning or a new accepted immutable revision, plus immutable public-beta bootstrap pinning.

## Exact-head executable evidence

Frozen Skills head: `8c321c03421a2e0e470280cc40e588a27c1a510d`.

- Validate AI-Verse Skills `34901693154`: SUCCESS.
- Runtime Readiness `34901693118`: SUCCESS across Ubuntu/macOS/Windows on Python 3.9 and 3.12.
- Full E2E Install `34901693143`: SUCCESS.

Frozen-head jobs inspected: **8 / 8 successful**, all with executed steps.

Full E2E covered registry validation, full tests, pinned upstream install, provider-v1 metadata, setup/doctor, generation pinning, adapter exposure, update, stale-adapter rejection, rollback, uninstall preservation and recovery.

## Negative-space checks

A1.5 found no evidence that Skills:

- turns installation/admission/trust into authorization;
- treats static connection hints as authenticated readiness;
- allows package paths to escape an immutable generation;
- injects capabilities absent from the generation manifest;
- silently mixes files from two generations in one pin;
- mutates committed generations during normal update;
- autonomously rewrites protected first-party/curated packages;
- auto-promotes permission/Connection/credential expansion;
- accepts stale proposal evaluation over a changed generation;
- lets Skill runtime self-assert OS proof for successful consequential effects;
- treats trace correlation as verification evidence;
- exposes internal HyperFrames support as a duplicate public capability.

## Evidence IDs

- `E-A1.5-001` frozen tree/repository metadata.
- `E-A1.5-002` README/architecture ownership model.
- `E-A1.5-003` registry counts, source pins and trust policy.
- `E-A1.5-004` immutable generation lifecycle.
- `E-A1.5-005` provider path/digest/index validation.
- `E-A1.5-006` admission/security/trust implementation.
- `E-A1.5-007` readiness v2.
- `E-A1.5-008` execution receipt v2.
- `E-A1.5-009` governed learning lifecycle.
- `E-A1.5-010` public lifecycle/retention implementation.
- `E-A1.5-011` controller-path construction.
- `E-A1.5-012` stale-lock recovery implementation.
- `E-A1.5-013` retention protection inputs and missing execution leases.
- `E-A1.5-014` generation lifecycle tests.
- `E-A1.5-015` exact-head Validate run.
- `E-A1.5-016` exact-head Readiness run.
- `E-A1.5-017` exact-head Full E2E run.
- `E-A1.5-018` Video Editor PR #14 release evidence.
- `E-A1.5-019` Video Editor acceptance run.
- `E-A1.5-020` accepted component descriptor.
- `E-A1.5-021` accepted-to-current 190-commit comparison.
- `E-A1.5-022` current distribution version.
- `E-A1.5-023` mutable-main bootstrap route.
- `E-A1.5-024` live pre-write ref/open-PR recheck.

## Verdict and progress

**AI-Verse-Skills at `8c321c03421a2e0e470280cc40e588a27c1a510d`: AUDIT COMPLETE, DOGFOOD BLOCKED.**

Current findings:

1. `WSA-2026-016` BLOCKER lifecycle controller containment.
2. `WSA-2026-017` HIGH lifecycle serialization.
3. `WSA-2026-018` MEDIUM in-use generation retention.
4. `WSA-2026-019` LOW release/bootstrap identity drift.

No Skills product repair is made during A1.5.

After acceptance:

- weighted audit: **15 / 100 = 15%**
- remaining: **85%**
- tracker tasks: **10 / 51 complete**, **41 / 51 remaining**
- phases: **1 / 7 complete**, **6 / 7 incomplete**
- A1 repositories: **5 / 14 complete**, **9 / 14 remaining**
- A1 weight: **10 / 28**
- next task: **A1.6 AI-Verse-Data**
