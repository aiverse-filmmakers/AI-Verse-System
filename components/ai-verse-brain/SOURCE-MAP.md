# AI-Verse Brain Source Map

**Repository:** `aiverse-filmmakers/AI-Verse-Brain`  
**Reviewed branch:** `main`  
**Reviewed head:** `bef8261ad35d126d29aeff5d496f46904125b7b6`  
**Audit date:** 2026-09-13  
**Methodology:** `AI-Verse-System/docs/AUDIT-METHODOLOGY.md`  
**Evidence scope:** Brain itself. Other repositories were not independently audited. Cross-repo facts below are admitted only when Brain contains the contract/test/workflow evidence.

---

## 1. Revision anchor

Fresh audit anchor:

```text
repo:   aiverse-filmmakers/AI-Verse-Brain
branch: main
head:   bef8261ad35d126d29aeff5d496f46904125b7b6
```

Latest reviewed commit message:

```text
Release hardening: canonical workspace scope ids
```

The preceding major lifecycle merge was PR #16, merged at commit:

```text
9ca1b5d5103e68b85d170660ffea85669533b41a
```

The final workspace-scope hardening was PR #17.

---

## 2. Evidence precedence used

The audit followed this ordering when sources disagreed:

1. executable code;
2. tests and CI behavior;
3. schemas/protocol contracts;
4. current architecture and install docs;
5. README/status prose;
6. Git/PR history;
7. preserved research and inspiration material.

Research documents were never used to override current implementation.

---

## 3. Repository inventory

Relevant top-level structure:

```text
.github/
BRAIN.yaml
CHANGELOG.md
LICENSE
README.md
SECURITY.md
docs/
engine/
examples/
protocol/
pyproject.toml
research/
schemas/
tests/
```

Key characteristics:

- Python implementation under `engine/aiverse_brain/`;
- CLI package via `pyproject.toml`;
- no required third-party runtime Python dependencies declared;
- normative protocol documents under `protocol/`;
- JSON schemas under `schemas/`;
- extensive tests under `tests/`;
- three GitHub Actions workflows;
- preserved pre-implementation research under `research/`;
- compatibility/hardening facades preserve mature legacy implementations in several modules.

No build/vendor tree was treated as architecture evidence.

---

## 4. Root product sources

### `README.md`

CURRENT public identity and user-path evidence for:

- universal intelligence layer positioning;
- Brain/OS/Memory/Host responsibility split;
- current beta version label;
- standalone/native install model;
- local extension attachment lifecycle;
- direction handover/handback;
- onboarding;
- vendor reasoners;
- host adapter usage;
- cadence boundary;
- migration/doctor/security positioning.

### `BRAIN.yaml`

Machine-readable architecture source for:

- architecture name;
- modes;
- principles/laws;
- canonical object types;
- owned/non-owned state;
- native/standalone paths;
- runtime disposability;
- action and verification constraints;
- integration assumptions.

### `pyproject.toml`

Evidence for:

- Python >=3.9;
- package/CLI entry points;
- MIT license metadata;
- no mandatory runtime dependency list;
- package source layout.

### `SECURITY.md`

Evidence for:

- model/retrieved/host content treated as untrusted;
- explicit user authority boundary;
- secret-handling expectations;
- side-effect uncertainty posture;
- vendor reasoners as reasoners only;
- fail-closed native behavior.

### `CHANGELOG.md`

Release chronology through beta.1.

Negative-space finding: post-beta.1 September hardening is not represented as a newer immutable version/release.

### `docs/RELEASE.md`

CURRENT release checklist contract for `v0.1.0-beta.1`.

Important requirements recorded there:

- six OS/Python test legs;
- wheel clean-install smoke;
- exact CI-passed tag;
- vendor CLI flag recheck;
- GitHub prerelease creation;
- immutable tag install verification.

Audit finding: the tag exists, but GitHub releases endpoint returned no Release objects, and current `main` is 20 commits ahead of the tag.

---

## 5. Protocol sources

### `protocol/BRAIN-PROTOCOL.md`

Architecture/authority contract.

### `protocol/RUNTIME-PIPELINE.md`

Trigger, context, reasoner, proposal and deterministic-application boundary.

### `protocol/DIRECTION-ATTENTION.md`

Gap/opportunity/initiative/attention contract.

### `protocol/ACTION-VERIFICATION.md`

Objective, progress, evidence and verification contract.

### `protocol/COGNITION-ACTION-BOUNDARY.md`

Reasoning versus explicit action boundary, replay/idempotency behavior.

### `protocol/LEARNING-EVOLUTION.md`

Learning/evolution stages and privileged self-improvement limits.

### `protocol/INTEGRATION-CADENCE.md`

Cadence semantics while preserving host scheduler ownership.

### `protocol/ADAPTER-BRIDGE.md`

JSON subprocess bridge contract, host/reasoner operations, bounded transport behavior.

### `protocol/SKILLS-RECEIPT-VERIFICATION.md`

Skills receipt v2 consumption and objective-verification boundary.

### `protocol/WRITE-CONTRACT.md`

Canonical ownership classification and intended owner-routing boundary.

### `protocol/INSTALLATION-ONBOARDING.md`

Install/onboarding design history. Treat current lifecycle claims carefully because local registry lifecycle evolved after earlier installation assumptions.

---

## 6. Core state sources

### `engine/aiverse_brain/models.py`

CURRENT evidence for:

- scope grammar;
- object envelope;
- evidence classes;
- evidence provenance/independence;
- timestamp validation.

Latest scope grammar:

```text
operator
workspace:[a-z0-9][a-z0-9-]{0,127}
```

### `engine/aiverse_brain/validation.py`

Payload and lifecycle validation.

### `engine/aiverse_brain/state_machine.py`

Deterministic state transitions and authority requirements.

### `schemas/*.schema.json`

Machine-readable contracts covering Brain object and bridge/install surfaces.

`tests/test_contracts.py` verifies schema/protocol presence and JSON validity, but runtime validation remains code-enforced rather than proof that every JSON schema is dynamically applied at every write edge.

---

## 7. Storage and isolation sources

### `engine/aiverse_brain/storage.py`

CURRENT evidence for:

- standalone/native layout;
- incompatible-host refusal;
- operator/workspace mapping;
- path containment;
- object ID safety;
- optimistic revision control;
- atomic JSON writes;
- per-object runtime locks;
- native write readiness gate.

Important scale observation: listing is directory-scan based, with no persistent index/pagination layer.

### `engine/aiverse_brain/runtime_lock.py`

Cross-process runtime key locking with stale-lock semantics for Brain runtime resources.

This contrasts with the extension-registry lock, which has no stale-lock recovery.

---

## 8. Installation and lifecycle sources

### `engine/aiverse_brain/integration.py`

CURRENT host detection:

- standalone;
- compatible AI-Verse OS v2;
- incompatible AI-Verse.

Local Brain attachment is current authority. Legacy tracked manifest registration may be observed as obsolete evidence but is not current write authority.

### `engine/aiverse_brain/extension_registry.py`

CURRENT evidence for:

- `.aiverse/extensions/registry.json` local attachment;
- schema 1.0;
- Brain mutates only its entry;
- supported/installed/enabled requirements;
- attach;
- internal enable/disable setter;
- detach;
- symlink/file-type checks;
- atomic registry write;
- `O_EXCL` lock.

Critical negative-space findings:

- public CLI exposes disable but not enable;
- `attach_brain()` preserves an existing `enabled` value, so attach cannot serve as implicit re-enable;
- registry lock has no stale-lock TTL/token recovery.

### `engine/aiverse_brain/installation.py`

CURRENT evidence for:

- dry-run planning;
- clean native auto-attachment;
- idempotent installation marker;
- package/state schema checks;
- native bootstrap exception;
- tracked OS configuration remains untouched.

### `engine/aiverse_brain/write_gate.py`

CURRENT enforcement of native registration + initialization before writes.

### `engine/aiverse_brain/cli.py`

CURRENT public commands:

```text
init
attach
disable
detach
onboard
direction-owner
adapter-doctor
vendor-doctor
run-tick
doctor
migrate
plan-integration
plan-cadence
cadence-hooks
```

Negative evidence from parser inspection:

- no public `enable` command;
- no general `activate` command;
- no lifecycle `reconcile` command;
- no Brain-specific `uninstall` or `rollback` command.

These absences were evaluated relative to the lifecycle target, not treated automatically as defects where package-manager/host ownership is appropriate.

---

## 9. Strategic ownership sources

### `engine/aiverse_brain/direction_ownership.py`

CURRENT evidence for:

- durable `.aiverse/direction/ownership.json`;
- OS/Brain owner values;
- default OS ownership in native mode;
- standalone Brain ownership;
- explicit OS-to-Brain import;
- source path + SHA-256 provenance;
- staged activation;
- resumable interruption handling;
- generated refs view;
- explicit Brain-to-OS export/handback;
- bounded strategic-section update;
- per-scope plus registry-wide locking;
- concurrent-scope preservation;
- ownership-safe crash ordering.

### `engine/aiverse_brain/controller.py`

CURRENT enforcement that native Brain cannot write strategic intent while OS owns direction except for the non-active staging used by explicit handover.

### `engine/aiverse_brain/local_host.py`

CURRENT ownership-aware context read behavior.

### `tests/test_direction_ownership.py`
### `tests/test_frozen_strategy_read_boundary.py`

Strong acceptance evidence for ownership, concurrency, crash handling and frozen-strategy reads.

---

## 10. Policy and authority sources

### `engine/aiverse_brain/policy.py`

Default action policy, proactivity, attention/resource/evolution limits.

### `engine/aiverse_brain/effective_policy.py`

CURRENT evidence for:

- one active policy per scope;
- operator baseline;
- workspace only tightens;
- caller override only tightens;
- strict payload parsing.

### `engine/aiverse_brain/authority.py`

Authority tiers and mutation gates.

### `tests/test_effective_policy.py`

Restart/runtime/cadence/workspace enforcement evidence.

Historical provenance: PR #4 repaired this area after the beta tag.

---

## 11. Cognition/runtime sources

### `engine/aiverse_brain/cognition.py`

Cognition request/proposal structures.

### `engine/aiverse_brain/orchestrator.py`

Deterministic trigger-to-cognition planning.

### `engine/aiverse_brain/reasoner.py`

Reasoner adapter and bounded context assembly.

### `engine/aiverse_brain/retrieval.py`

CURRENT evidence for semantic history queries and capability ranking before final context truncation.

### `engine/aiverse_brain/proposal_apply.py`

Deterministic proposal mutation path.

### `engine/aiverse_brain/runtime.py`

CURRENT orchestration and strict separation between cognition and explicit actions.

### `engine/aiverse_brain/tick_output.py`

Bounded useful explicit tick/orientation rendering.

### Tests

- `tests/test_runtime_pipeline.py`
- `tests/test_runtime_hardening.py`
- `tests/test_meaningful_retrieval.py`
- `tests/test_explicit_tick_output.py`

---

## 12. Direction, attention, progress and learning sources

### Direction/attention

- `engine/aiverse_brain/direction.py`
- `engine/aiverse_brain/ranking.py`
- `engine/aiverse_brain/attention.py`

### Progress/verification

- `engine/aiverse_brain/progress.py`
- `engine/aiverse_brain/evaluator.py`
- `engine/aiverse_brain/verification.py`

### Belief freshness/learning

- `engine/aiverse_brain/freshness.py`
- `engine/aiverse_brain/learning.py`

### Tests

- `tests/test_slice2.py`
- `tests/test_core.py`

These tests cover attention budgets, objective evidence, stall semantics, learning progression and strategy evolution restrictions.

---

## 13. External action safety sources

### `engine/aiverse_brain/action_snapshot.py`

Deep/frozen action parameter handling.

### `engine/aiverse_brain/action_boundary.py`

CURRENT host permission hardening facade.

### `engine/aiverse_brain/action_boundary_legacy.py`

Mature underlying action/idempotency/receipt/reconciliation implementation retained behind stable facade.

### `engine/aiverse_brain/host_permission.py`

Exact host permission-decision binding.

### Tests

- `tests/test_action_approval_binding.py`
- `tests/test_cognition_action.py`
- `tests/test_permission_intersection.py`

Strong evidence for:

- exact approval fingerprinting;
- permission intersection;
- dispatch-edge recheck;
- duplicate suppression;
- uncertain-effect handling;
- verified reconciliation.

---

## 14. Skills receipt sources

### `engine/aiverse_brain/skills_receipt.py`
### `engine/aiverse_brain/skills_receipt_legacy.py`

CURRENT consumer for Skills receipt v2 and objective evidence translation.

### `tests/test_skills_receipt_contract.py`

Local contract acceptance.

### `.github/workflows/skills-receipt-contract.yml`

Cross-repo contract workflow pinned to Skills commit:

```text
558bbcb05ce9f42bb5be30730ea205a7e791bf86
```

This proves Brain against a fixed Skills receipt implementation without making Skills a Brain runtime dependency.

---

## 15. Host/bridge sources

### `engine/aiverse_brain/host.py`

Host protocol surface.

### `engine/aiverse_brain/bridge.py`
### `engine/aiverse_brain/bridge_legacy.py`

Bridge facade and mature transport implementation.

### `engine/aiverse_brain/host_selection.py`

CURRENT explicit host selection.

Required real-host read operations:

- read context;
- retrieve history;
- list capabilities;
- list connections.

### `engine/aiverse_brain/vendor.py`
### `engine/aiverse_brain/vendor_bridge.py`

Vendor reasoner configurations/wrappers.

### Tests

- `tests/test_bridge.py`
- `tests/test_host_selection.py`
- `tests/test_reference_adapter.py`
- vendor tests in `tests/test_release_candidate.py`

CI logs show a small quality defect: some subprocess tests produce unclosed-file `ResourceWarning`s while still passing.

---

## 16. Doctor and migration sources

### `engine/aiverse_brain/doctor.py`

CURRENT structural checks for:

- host contract;
- parallel store;
- attachment state;
- installation marker;
- JSON scope/kind integrity;
- onboarding minimums;
- optional Memory detection.

Contradiction/readiness finding:

- unattached native Brain is WARN, not FAIL;
- uninitialized Brain is WARN, not FAIL;
- therefore `DoctorReport.ok` may be true while normal native writes are unavailable.

### `engine/aiverse_brain/migration.py`

CURRENT behavior:

- same-schema package metadata refresh;
- unknown older state fails closed;
- newer state fails closed;
- no registered historical state conversion yet.

---

## 17. Installation-order evidence

Evidence chain:

1. `StorageLayout.detect()` switches to native mode when compatible `AI-VERSE.yaml` exists.
2. Standalone canonical state is `.ai-verse-brain/`.
3. Native canonical state is `operator/brain/` or workspace Brain paths.
4. `doctor.py` marks `.ai-verse-brain` inside native mode as `parallel-store` FAIL.
5. `migration.py` contains no standalone-to-native state relocation/adoption transaction.

Therefore:

```text
OS first -> Brain later     CURRENT supported
Brain standalone -> OS later  GAP
```

This is a lifecycle negative-space result, not an inferred design preference.

---

## 18. CI sources

### `.github/workflows/ci.yml`

Matrix:

```text
ubuntu-latest: Python 3.9, 3.12
macos-latest:  Python 3.9, 3.12
windows-latest: Python 3.9, 3.12
```

Plus wheel build and clean-environment CLI smoke.

### Final reviewed PR gate

PR #17 head:

```text
296b4d0238e1766b73bd01fb4741e51352b67121
```

Workflow results:

- CI: success;
- OS Direction Ownership Contract: success;
- Skills Receipt Contract: success.

Ubuntu/Python 3.12 job log reports:

```text
Ran 198 tests
OK
```

The same matrix workflow passed all six platform/Python test jobs.

### `.github/workflows/os-direction-contract.yml`

Strong Brain-contained cross-repo evidence for:

- explicit direction handover;
- OS strategic-write blocking while Brain owns direction;
- provenance import;
- frozen-strategy read behavior;
- Brain-state loss not silently returning ownership;
- no tracked OS dirt after fixture cleanup.

Evidence limitation:

- workflow clones current OS `main`, so result is time-sensitive compatibility evidence rather than a reproducible pinned pair;
- workflow still creates a legacy tracked manifest registration fixture before current local-registry initialization, which is not the exact clean member product path.

---

## 19. Release evidence

### Tag

`v0.1.0-beta.1` exists. Fetching repository content at that ref succeeds.

### Main versus tag

GitHub compare result:

```text
base: v0.1.0-beta.1
head: bef8261ad35d126d29aeff5d496f46904125b7b6
status: ahead
ahead_by: 20
behind_by: 0
```

The changed files include core lifecycle, direction, permission, retrieval and receipt code/tests/workflows.

### GitHub Release object

Releases endpoint returned:

```json
[]
```

This conflicts with the release checklist step requiring a GitHub prerelease for beta.1.

---

## 20. Documentation contradiction evidence

### `docs/INSTALLATION.md`

Observed current examples include `run-tick` invocations that omit required host selection.

### `engine/aiverse_brain/host_selection.py`

Requires exactly one mode:

```text
--host-adapter CONFIG
--read-only-context
```

### `tests/test_host_selection.py`

Explicitly tests parser rejection when neither mode is supplied.

Therefore the installation-doc command is CURRENTLY BROKEN as written.

### `research/README.md`

Top matter correctly marks research as pre-implementation record, but its “Current status” still says no production Brain engine has been implemented. That statement is HISTORICAL and must not be used as current implementation truth.

---

## 21. Historical PR map

Important merged PR chronology:

| PR | Meaning |
|---|---|
| #1 | Phase 4 deterministic Brain core |
| #2 | Phase 5 shipment/installability |
| #3 | public beta release candidate beta.1 |
| #4 | persisted effective policy enforcement repair |
| #5 | exact immutable action approval binding |
| #6 | native write readiness |
| #7 | single strategic direction owner |
| #8 | explicit real host selection |
| #9 | meaningful history/capability retrieval |
| #10 | Brain/host permission intersection |
| #11 | Skills receipt verification |
| #12 | useful explicit tick orientation |
| #13 | ownership-aware context reads |
| #14 | shared direction registry concurrency serialization |
| #15 | host adapter documentation repair |
| #16 | local attachment and safe lifecycle |
| #17 | canonical workspace scope IDs |

This history is important because the current safety architecture cannot be attributed fully to the original beta tag.

---

## 22. INSPIRATION sources

Preserved research directory:

- `research/PHASE-1-LANDSCAPE.md`
- `research/PHASE-2-ARCHITECTURE-DISSECTION.md`
- `research/PHASE-3-BRAIN-SPECIFICATION.md`
- `research/PHASE-3-QC-RISK-MATRIX.md`
- `research/SOURCE-MAP.md`

`research/README.md` explicitly records study of systems/projects including LifeOS, Hermes, AIS-OS, Letta, OpenClaw, ACE, Hermes Self-Evolution, GEPA, Voyager, Generative Agents, Reflexion, PersonalOS, Pascal Jarvis, DeerFlow, Honcho, LangMem, Agent Zero, Magentic-One and Anthropic long-running-agent work.

Classification rule:

- use these sources to explain design lineage and warnings;
- do not promote inspiration features to CURRENT unless implementation/tests prove them.

---

## 23. Evidence limitations

This audit intentionally did **not** independently inspect OS, Memory, Skills, Data, Connections, Multiple Bots, Apps, Dashboard or Token implementation.

Statements about sibling behavior are limited to what Brain itself embeds as:

- host contracts;
- schemas;
- tests;
- CI workflows;
- version-pinned receipt integration;
- current docs.

No claim that “the whole AI-Verse system works” is justified by this Brain-only audit.

The absence of workflow runs directly attached to final `main` commit was not treated as test failure because PR #17’s tested merge candidate and its three successful workflows are available as exact evidence. It should still be preferable for protected-main policy to make the post-merge status obvious.