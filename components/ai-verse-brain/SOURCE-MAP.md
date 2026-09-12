# AI-Verse Brain Source Map

**Repository:** `aiverse-filmmakers/AI-Verse-Brain`  
**Reviewed branch:** `main`  
**Reviewed head:** `bef8261ad35d126d29aeff5d496f46904125b7b6`  
**Fresh standalone review:** 2026-09-13  
**Scope rule:** the baseline Brain specification was reconstructed from AI-Verse-Brain itself. Other repositories were not treated as primary evidence; cross-component facts were accepted only where Brain's own code, tests, CI or research records them.

---


## 1. Repository inventory

**Reviewed repository:** `aiverse-filmmakers/AI-Verse-Brain`  
**Reviewed branch:** `main`  
**Reviewed head:** `bef8261ad35d126d29aeff5d496f46904125b7b6`  
**Tree inventory:** 135 entries, consisting of 125 tracked files and 10 directories. GitHub reported the recursive tree as not truncated.

Top-level tracked-file distribution:

- 53 files under `engine/`;
- 21 under `tests/`;
- 18 under `schemas/`;
- 11 under `protocol/`;
- 6 under `research/`;
- 5 under `docs/`;
- 3 workflow files under `.github/`;
- root identity/release files and two examples.

The repository contains:

- Python implementation under `engine/aiverse_brain/`;
- normative Brain contracts under `protocol/`;
- JSON schemas under `schemas/`;
- preserved research/inspiration history under `research/`;
- current test evidence under `tests/`;
- release/security/package identity at the root.

### Canonical / generated / vendor boundary

No generated build tree or vendored third-party implementation is tracked.

Files such as `action_boundary_legacy.py` and `bridge_legacy.py` are not generated artifacts. They remain active current implementation bodies wrapped by hardened public facades.

Canonical user state and disposable runtime state are created at installation/runtime and are intentionally not committed to the repository.

External vendor CLIs are dependencies at execution time through adapters; their source code is not vendored into Brain.

## 2. Root identity and release evidence

### `README.md`

Primary current public product description.

Evidence for:

- universal intelligence layer positioning;
- Brain/OS/Memory/Host responsibility split;
- core behaviors;
- beta install command;
- dry-run-first init;
- local attachment lifecycle;
- explicit direction handback;
- onboarding;
- Claude/Codex/Hermes reasoner wrappers;
- run-tick;
- native AI-Verse OS host path;
- Cadence without scheduler ownership;
- migration;
- doctor;
- security boundary;
- development/QC.

### `BRAIN.yaml`

Machine-readable architecture declaration.

Key evidence:

- architecture: `intent-cognition-initiative-learning`;
- modes: standalone + AI-Verse OS v2;
- core principles;
- native/standalone paths;
- canonical object kinds;
- implemented mechanisms;
- explicit non-ownership;
- runtime is disposable.

### `pyproject.toml`

Evidence for:

- package identity;
- Python >=3.9;
- no declared runtime dependencies;
- CLI entry points;
- beta classifier;
- MIT license;
- GitHub package metadata.

### `engine/aiverse_brain/_version.py`

Current main still reports:

- Python version `0.1.0b1`;
- display version `0.1.0-beta.1`;
- installation schema 1.0;
- state schema 1.0.

This is important because current main contains substantial post-beta.1 hardening without a new displayed version.

### `CHANGELOG.md`

Release history through beta.1.

It does not include the September 10-12 post-tag hardening.

### `SECURITY.md`

Security/trust model:

- model output untrusted;
- host/retrieved data untrusted;
- explicit user authority;
- no secret storage;
- reasoner-only vendor wrappers;
- effect uncertainty handling;
- fail-closed host boundaries.

### `docs/RELEASE.md`

Beta.1 release checklist and immutable tag intent.

Important evidence:

- six platform/Python CI legs;
- wheel clean-install smoke;
- tag exact passed commit;
- re-check vendor CLI flags before release;
- documented tag install;
- beta schema may evolve only with explicit migration or fail-closed behavior.

---

## 3. Brain protocol evidence

### `protocol/BRAIN-PROTOCOL.md`

Primary architecture contract.

Evidence for:

- three loops;
- authority hierarchy;
- hard rules;
- Direction/Action/Learning contracts;
- scheduler non-ownership;
- native/standalone path separation.

### `protocol/RUNTIME-PIPELINE.md`

Evidence for:

- trigger -> orientation -> bounded context -> reasoner -> proposals -> deterministic apply -> attention;
- external actions outside cognition;
- models cannot set control fields;
- retrieved context remains ephemeral;
- proposal-specific deterministic validation;
- surface items do not automatically notify;
- explicit action boundary;
- trigger receipt semantics.

### `protocol/DIRECTION-ATTENTION.md`

Evidence for:

- gap/opportunity/initiative chain;
- hard gates before rank;
- dedupe/cooldowns;
- initiative lineage;
- inspectable ranking;
- notification classes;
- P0-P4 proactivity;
- attention budget.

### `protocol/ACTION-VERIFICATION.md`

Evidence for:

- objective contracts;
- progress/stall semantics;
- attempt budgets;
- parallelism;
- V0-V3 verification;
- evaluator independence;
- criterion evidence requirements.

### `protocol/COGNITION-ACTION-BOUNDARY.md`

Evidence for:

- reasoner advisory-only;
- deterministic tick planning;
- explicit ActionRequest;
- approval authority;
- replay/idempotency;
- uncertain action reconciliation.

### `protocol/LEARNING-EVOLUTION.md`

Evidence for:

- staged learning;
- E0-E4 evolution;
- privileged self-improvement boundaries;
- rollback/evaluation requirements.

### `protocol/INTEGRATION-CADENCE.md`

Evidence for:

- Brain owns useful cognition timing semantics;
- host owns actual scheduler;
- trigger policy and background budgets.

### `protocol/ADAPTER-BRIDGE.md`

Normative `ai-verse-brain-bridge/1.0` transport.

Evidence for:

- JSON subprocess boundary;
- bounded I/O;
- shell-free execution;
- environment allowlisting;
- handshake;
- reasoner operations;
- host read/action operations;
- optional `query_data`;
- permission operation;
- semantic history retrieval;
- task-relevant capability retrieval;
- idempotency metadata;
- failure semantics.

### `protocol/SKILLS-RECEIPT-VERIFICATION.md`

Evidence for:

- Skills receipt v2 consumption;
- exact action/capability/generation/digest binding;
- effect certainty mapping;
- provenance-derived evidence class;
- objective closure remains Brain-owned.

### `protocol/WRITE-CONTRACT.md`

Evidence for canonical Brain ownership vs routes to OS/Memory/Knowledge/Capabilities.

Important negative-space finding:

- contract and symbolic routing exist;
- no general automatic durable cross-component write dispatcher was found in the current cognition/learning execution path.

### `protocol/INSTALLATION-ONBOARDING.md`

Historical/current protocol document.

**Drift found:** still states that native init requires an existing tracked-style Brain registration slot, while current main auto-attaches through the local extension registry.

---

## 4. Core object/state model

### `engine/aiverse_brain/models.py`

Evidence for:

- exact scope grammar;
- evidence classes/provenance;
- timestamps with timezone validation;
- common Brain object envelope;
- revision/provenance/supersession fields.

### `engine/aiverse_brain/validation.py`

Evidence for:

- required fields per object family;
- lifecycle status vocabulary;
- enums;
- confidence ranges;
- criterion/evidence constraints;
- strategy evolution tiers;
- learning counters.

### `engine/aiverse_brain/state_machine.py`

Evidence for deterministic allowed transitions across:

- intent;
- practice;
- gap;
- opportunity;
- initiative;
- objective;
- model belief;
- evaluation;
- learning;
- strategy rule;
- policy.

Also enforces stronger authority for user confirmation and policy mutations.

### Schemas

Reviewed schema set includes:

- common;
- intent;
- practice;
- gap;
- opportunity;
- initiative;
- objective;
- model belief;
- evaluation;
- learning;
- strategy rule;
- policy;
- cognition request/proposal;
- action request;
- installation;
- onboarding answers;
- adapter config.

Schemas reinforce the typed-contract nature of Brain rather than a loose document store.

---

## 5. Storage, concurrency and isolation

### `engine/aiverse_brain/storage.py`

Evidence for:

- standalone/native storage layout;
- no standalone fallback inside incompatible AI-Verse host;
- operator/workspace isolation;
- path-safe object IDs;
- atomic file replacement;
- optimistic revision checks;
- per-object locks;
- native write gate before save.

### `engine/aiverse_brain/runtime_lock.py`

Evidence for:

- cross-process runtime locks;
- token ownership;
- stale lock recovery.

### `engine/aiverse_brain/direction_ownership.py`

Evidence for:

- direction registry;
- safe atomic writes;
- path containment;
- import candidates;
- provenance;
- per-scope + registry-wide coordination;
- interrupted handover recovery;
- handback/export.

Historical PR #14 specifically hardened concurrent shared registry updates.

---

## 6. Policy and authority

### `engine/aiverse_brain/policy.py`

Evidence for:

- P0-P4;
- action classes;
- default action policy;
- attention budgets;
- resource budgets;
- evolution policy.

### `engine/aiverse_brain/effective_policy.py`

Evidence for:

- durable policy parsing;
- exactly one active policy per scope;
- operator policy baseline;
- workspace policy may only tighten;
- caller override may only tighten;
- persisted policy reloaded rather than trusting constructor-only configuration.

This code corresponds to the repair described by PR #4.

### `engine/aiverse_brain/authority.py`

Authority tier enforcement used by lifecycle/policy operations.

---

## 7. Direction and initiative implementation

### `engine/aiverse_brain/direction.py`

Evidence for:

- gap creation;
- opportunity fingerprinting;
- eligibility/ranking;
- duplicate/cooldown checks;
- qualified opportunity;
- initiative proposal lineage;
- runtime locking around shared semantic fingerprint.

### `engine/aiverse_brain/ranking.py`

Evidence for:

- hard gates;
- weighted positive/cost factors;
- Four-C readiness input;
- notification classification.

### `engine/aiverse_brain/attention.py`

Attention delivery/cooldown budgets.

---

## 8. Progress and verification implementation

### `engine/aiverse_brain/progress.py`

Evidence for:

- baseline state token;
- meaningful progress requires changed state + evidence;
- stall counter;
- max attempt block;
- blocker handling.

### `engine/aiverse_brain/evaluator.py`

Evidence for:

- V0-V3 floor;
- independence levels;
- fresh-context builder/evaluator separation;
- strong evidence requirements;
- criterion materialization;
- failed/insufficient/passed objective transitions.

### `engine/aiverse_brain/verification.py`

Verification helper behavior.

---

## 9. Belief freshness and learning

### `engine/aiverse_brain/freshness.py`

Evidence for:

- known/inferred/assumed/unknown/contradicted/stale;
- expiry/max age;
- evidence expiry;
- contradiction;
- verified refresh.

### `engine/aiverse_brain/learning.py`

Evidence for:

- observation counts;
- controlled evaluation;
- contradiction blocking;
- validated learning;
- strategy candidate generation;
- strategy outcome tracking;
- E1/E2 evidence gates;
- E3/E4 runtime activation prohibition.

This file is key evidence that current "self-improvement" means strategy-rule evolution, not autonomous source-code rewrite.

---

## 10. Cognition and proposal implementation

### `engine/aiverse_brain/cognition.py`

Cognition request/proposal structures.

### `engine/aiverse_brain/orchestrator.py`

Deterministic mapping of triggers to cognition purposes.

### `engine/aiverse_brain/reasoner.py`

Evidence for:

- ReasonerAdapter protocol;
- ContextBundle;
- bounded context assembly;
- semantic retrieval queries;
- Brain-state context selection;
- strict output parsing.

### `engine/aiverse_brain/proposal_apply.py`

Evidence for deterministic application of:

- gaps;
- opportunities;
- initiatives;
- objectives;
- beliefs;
- learning.

Model proposals remain bounded by canonical refs and policy.

### `engine/aiverse_brain/runtime.py`

Evidence for:

- native write-ready gate;
- policy refresh;
- trigger claim;
- bounded cognition/application;
- structured errors;
- attention output;
- explicit separate action execution.

---

## 11. External action safety

### `engine/aiverse_brain/action_boundary.py`
### `engine/aiverse_brain/action_boundary_legacy.py`
### `engine/aiverse_brain/action_snapshot.py`

Evidence for:

- exact immutable action requests;
- deep/frozen parameters;
- approvals;
- permission re-checking;
- idempotency;
- durable receipt refs;
- uncertain outcome blocking;
- reconciliation.

The current stable module wraps the mature legacy implementation with the host-permission hardening layer.

### `engine/aiverse_brain/host_permission.py`

Exact host permission decision binding.

### `docs/PERMISSION-INTERSECTION.md`

Normative restrictive-intersection rules.

---

## 12. Skills receipt bridge

### `engine/aiverse_brain/skills_receipt.py`
### `engine/aiverse_brain/skills_receipt_legacy.py`

Evidence for:

- execution identity;
- receipt translation;
- objective evaluation from receipt;
- provenance/effect constraints.

The stable wrapper retains the mature implementation behind a hardened contract.

---


## 13. Host and bridge implementation

### `engine/aiverse_brain/host.py`

The host protocol exposes a broad portable surface:

- current-context reads;
- historical retrieval;
- capability listing;
- connection listing;
- optional structured Data query;
- action authorization/execution;
- evaluation request;
- scheduler request/cancel;
- notification;
- owner-routed write request.

### `engine/aiverse_brain/bridge.py` / `bridge_legacy.py`

Hardened subprocess transport and compatibility facade.

### `engine/aiverse_brain/host_selection.py`

Evidence for explicit host selection and no silent fallback.

Current real-host selection requires:

- `read_context`;
- `retrieve_history`;
- `list_capabilities`;
- `list_connections`.

### `engine/aiverse_brain/local_host.py`

Evidence for:

- deliberate read-only limited host;
- OS current-context resolver delegation;
- native raw-context bypass prevention;
- no history/capability/action ownership in limited mode.

### Operational-consumption distinction

The normal cognition path consumes the four required read operations above.

The explicit external-action path consumes `authorize_action` and `request_action`.

The reviewed normal tick does **not** automatically consume:

- `query_data`;
- `request_evaluation`;
- `schedule_trigger`;
- `cancel_trigger`;
- `notify_user`;
- `write_route`.

Those are contract surfaces until a concrete current product path invokes them.

This distinction is important under the audit methodology: interface exposure is not equivalent to operational integration.

### `engine/aiverse_brain/vendor.py` / `vendor_bridge.py`

Claude/Codex/Hermes reasoner wrappers.

### `docs/ADAPTERS.md` / `docs/VENDOR-REASONERS.md`

Public adapter/vendor guidance, with current documentation drift noted later in this source map.


## 14. Installation and lifecycle

### `engine/aiverse_brain/integration.py`

Current evidence for:

- standalone vs compatible native vs incompatible host;
- local extension-registry attachment;
- obsolete tracked-manifest registration detection;
- Memory-presence hints;
- native path contract;
- integration planning;
- no standalone fallback on incompatible AI-Verse.

A clean compatible host without local Brain attachment is reported as not integration-ready even though initialization can auto-attach. This creates a plan/bootstrap semantic mismatch worth preserving as a product finding.

### `engine/aiverse_brain/extension_registry.py`

Evidence for:

- local registry authority;
- Brain-owned entry only;
- exclusive registry lock;
- atomic write;
- preservation of sibling fields;
- attach;
- internal enable/disable state mutation;
- detach registration;
- symlink rejection.

### `engine/aiverse_brain/installation.py`

Evidence for:

- dry-run-first plan;
- clean current OS auto-attachment;
- idempotent installation marker;
- package/state version safety;
- tracked OS preservation;
- explicit blocker when a standalone `.ai-verse-brain/` store exists inside a now-native AI-Verse host.

That last blocker proves safe duplicate-truth prevention but also proves that standalone Brain -> native OS adoption is not implemented.

### `engine/aiverse_brain/onboarding.py`

Evidence for:

- explicit intent only;
- adaptive questions;
- no strategic writes while OS owns scope;
- deduplication;
- minimal orientation readiness.

### `engine/aiverse_brain/doctor.py`

Evidence for structural checks and partial attachment/readiness warnings.

### `engine/aiverse_brain/migration.py`

Current limitation:

- can refresh package metadata at the same state schema;
- blocks newer state;
- blocks older state where no conversion is registered;
- contains no actual older-state conversion path;
- does not perform standalone -> native Brain-state adoption.

## 15. CLI evidence

### `engine/aiverse_brain/cli.py`

Current main commands:

- init;
- attach;
- disable;
- detach;
- onboard;
- direction-owner;
- adapter-doctor;
- vendor-doctor;
- run-tick;
- doctor;
- migrate;
- plan-integration;
- plan-cadence;
- cadence-hooks.

### Lifecycle contradiction

There is no public `enable` command.

The internal extension API can set `enabled=True`.

`attach_brain()` preserves an existing disabled flag, so re-running attach does not re-enable.

This is direct evidence of asymmetric public lifecycle.

---

## 16. Write-routing evidence

### `engine/aiverse_brain/write_router.py`

Provides symbolic classification to:

- OS profile;
- OS context;
- OS decisions;
- Memory history;
- OS knowledge;
- capability candidate;
- Brain state;
- transient.

### Host protocol

`HostAdapter.write_route(...)` exists as an optional operation and the bridge can proxy it.

### Negative-space result

No general use of `write_route` was found in the reviewed cognition/learning runtime path that completes arbitrary classified Brain learnings into sibling-owned canonical state.

Therefore the current system should be described as having:

- write ownership classification;
- a host route contract;

but not a complete automatic cross-component writeback engine.

---

## 17. Cadence evidence

### `engine/aiverse_brain/cadence.py`
### `engine/aiverse_brain/cadence_plan.py`
### `engine/aiverse_brain/cadence_hooks.py`

Evidence for:

- trigger envelope;
- claim/complete;
- stale recovery;
- scheduler requests;
- portable command hooks;
- effective persisted policy.

Brain explicitly does not own scheduler installation.

---

## 18. Main CI

### `.github/workflows/ci.yml`

Current matrix:

- Ubuntu 3.9/3.12;
- macOS 3.9/3.12;
- Windows 3.9/3.12.

Runs full unittest suite.

Package smoke:

- wheel build;
- clean venv;
- wheel install;
- installed CLI;
- standalone init;
- doctor;
- migrate;
- marker verification.

This is strong core/package evidence.

---

## 19. OS cross-repository CI

### `.github/workflows/os-direction-contract.yml`

Tests:

- current OS main;
- initial OS ownership;
- handover;
- provenance;
- OS independent ownership observation;
- frozen strategy read boundary;
- Brain-state loss;
- tracked OS cleanliness.

### Stale acceptance setup

The workflow still patches tracked `AI-VERSE.yaml` to add a legacy `extensions.brain` block before initialization.

Current main auto-attaches via the local extension registry and explicitly treats tracked Brain manifest registration as obsolete.

Therefore this workflow currently proves the direction semantics but not the exact current member attachment path.

---

## 20. Skills cross-repository CI

### `.github/workflows/skills-receipt-contract.yml`

Pins a merged Skills receipt-v2 revision and proves:

- exact action binding;
- immutable capability generation;
- digest;
- effect certainty;
- trace ID misuse rejection;
- V2 evidence handling;
- objective closure remains Brain-owned.

This is strong real cross-repo contract evidence.

---

## 21. Important tests reviewed

### `tests/test_shipment_init.py`

Confirms:

- dry-run init;
- standalone idempotency;
- state-schema fail closed;
- incompatible OS no fallback;
- clean native auto-attachment without tracked manifest edits;
- only Brain/local registry paths written;
- onboarding explicit/idempotent;
- doctor onboarding readiness.

### `tests/test_native_write_readiness.py`

Confirms:

- clean OS plan/init auto-attach;
- disabled/unsupported attachment blocks writes;
- enabled but uninitialized blocks writes;
- init is sole bootstrap exception;
- disable blocks SDK/runtime/CLI writes;
- detach blocked while Brain owns direction;
- handback allows detach preserving Brain state;
- incompatible host no writes.

### `tests/test_direction_ownership.py`

Direction ownership/handover/handback, crash/recovery, concurrency.

### `tests/test_frozen_strategy_read_boundary.py`

No raw frozen strategy fallback.

### `tests/test_effective_policy.py`

Persisted policy and tightening.

### `tests/test_action_approval_binding.py`

Exact immutable approval binding.

### `tests/test_permission_intersection.py`

Brain/host restrictive authority.

### `tests/test_runtime_pipeline.py`

Bounded cognition/proposals.

### `tests/test_runtime_hardening.py`

Runtime replay/locks/safety.

### `tests/test_host_selection.py`

Explicit host selection and fail-closed adapter behavior.

### `tests/test_meaningful_retrieval.py`

Semantic history query and rank-before-limit.

### `tests/test_skills_receipt_contract.py`

Receipt/evidence semantics.

### `tests/test_release_candidate.py`

Release packaging/contracts.

---

## 22. Historical PR sequence reviewed

All visible PRs #1 through #17 were closed at review time.

### #1 Deterministic Brain core

Phase 4 engine, object model, verification, learning, cadence, action boundary, runtime-neutral cognition.

### #2 Shipment and installability

Initialization/onboarding, universal bridge, adapter config, package/version, clean install.

### #3 Public beta.1 release candidate

Vendor wrappers, run-tick, cadence hooks, migration plan, packaging/security/release docs.

### #4 Persisted policy repair

Canonical effective policy/restart/cadence enforcement.

### #5 Exact approval binding

Immutable fingerprint approval safety.

### #6 Native write readiness

Originally tracked-style native registration requirement; later superseded in part by PR #16.

### #7 Single strategic direction owner

Explicit OS -> Brain handover.

### #8 Explicit real host adapter selection

Removed implicit host fallback.

### #9 Meaningful retrieval

Semantic Memory queries and relevance-before-limit capability ranking.

### #10 Brain/host permission intersection

Host can restrict but never grant Brain authority.

### #11 Skills receipt verification

Exact effect/provenance/criterion semantics.

### #12 Useful explicit tick output

Deterministic orientation and bounded output.

### #13 Frozen strategy read boundary

Brain delegates native current context to OS ownership-aware resolver.

### #14 Shared direction registry serialization

Cross-scope concurrency repair.

### #15 Host adapter docs correction

Astra docs repair.

### #16 Local attachment and safe lifecycle

Major post-beta.1 hardening:

- local extension registry;
- attach/disable/detach;
- native init auto-attachment;
- Data bridge;
- Brain -> OS handback.

### #17 Workspace scope alignment

Shared canonical workspace ID grammar.

---

## 23. Release-tag comparison

A direct repository comparison was performed between current main and the README's recommended `v0.1.0-beta.1`.

### Beta tag

At `v0.1.0-beta.1`:

- `engine/aiverse_brain/extension_registry.py` is absent;
- CLI has no `attach`;
- no `disable`;
- no `detach`;
- no `direction-owner`.

### Current main

All those surfaces exist.

The current main package version still reports beta.1.

### Conclusion

The recommended immutable install artifact is materially older than the current documented lifecycle architecture.

This is evidence, not inference.

---

## 24. Research lineage

### `research/README.md`

Maps the research project.

**Drift found:** its "Current status" still says no production Brain engine has been implemented, which is now historical.

### `research/SOURCE-MAP.md`

Detailed research source catalog covering:

- LifeOS;
- Hermes Agent;
- Hermes self-evolution;
- GEPA;
- ACE;
- Voyager;
- Letta;
- OpenClaw;
- Generative Agents;
- Reflexion;
- PersonalOS;
- Pascal Jarvis;
- DeerFlow;
- Honcho;
- LangMem;
- Agent Zero;
- Magentic-One/AutoGen;
- Anthropic long-running agent harness;
- AIS-OS;
- AI-Verse OS;
- AI-Verse Memory.

### `research/PHASE-1-LANDSCAPE.md`

Best evidence for ideas adopted/rejected from external systems.

### `research/PHASE-2-ARCHITECTURE-DISSECTION.md`

Evidence for:

- long-horizon intent vs execution objectives;
- three loops;
- privileged intent layer;
- user model separation;
- initiatives;
- attention;
- practices;
- stall detection;
- native verification vocabulary;
- epistemic lifecycle;
- atomic strategy evolution;
- deterministic control;
- anti-patterns.

### `research/PHASE-3-BRAIN-SPECIFICATION.md`

Pre-implementation architecture target.

Important historical day-one slice includes:

- OS write routing;
- Memory recall/write integration;
- scheduler interface;
- strategies;
- install/doctor.

This is useful for finding implementation gaps today.

### `research/PHASE-3-QC-RISK-MATRIX.md`

Pre-implementation safety blockers and quality equations.

---

## 25. Research inspiration summary

Evidenced systems and strongest adopted ideas:

- LifeOS: desired-state spine and verification;
- Hermes: bounded goals and separate evaluation;
- AIS-OS: Three Ms/Four Cs as partial lenses;
- Letta: persistent inspectable agent strategy;
- OpenClaw: proactivity/scheduler separation;
- ACE: atomic strategy/playbook evolution;
- Hermes Self-Evolution: candidate/eval/regression/promotion;
- GEPA: textual trajectory optimization;
- Voyager: initiative/curriculum discovery;
- Generative Agents: reflection from experience;
- Reflexion: evaluator/reflection loop;
- PersonalOS: capacity-aware prioritization;
- Pascal Jarvis: proactive intent state machine;
- DeerFlow: persistence classification/write gates;
- Honcho: derived user model caution;
- LangMem: memory vs behavior optimization;
- Agent Zero: modular/runtime independence;
- Magentic-One: progress ledger semantics;
- Anthropic long-running agents: unverified-first/fresh independent evaluation.

The research explicitly says not to copy these systems wholesale.

---

## 26. Current documentation contradictions

### A. Recommended release artifact vs current README features

README describes current-main lifecycle but installs beta.1 tag that lacks it.

**Classification:** material release/documentation mismatch.

### B. Installation protocol vs current auto-attachment

Protocol says existing Brain registration required.

Current main auto-attaches through local registry.

**Classification:** stale protocol.

### C. Research README status

Says no production engine exists.

Current repo has a mature beta engine.

**Classification:** historical text not marked historical.

### D. OS direction CI vs current local attachment

Workflow patches tracked OS manifest before init.

Current member path should not.

**Classification:** stale acceptance setup.

### E. Public disable without public enable

Implementation API supports both state values, CLI only exposes disable.

**Classification:** lifecycle product defect.

### F. "Self-improvement" wording

Current strategy evolution is real, but runtime Brain cannot promote E3/E4 or rewrite code.

**Classification:** product wording should remain precise, not a code defect.

---

## 27. Evidence limitations

1. No Brain-independent web research was needed because the repository preserves the research sources itself.
2. External projects are documented as research/inspiration, not runtime dependencies.
3. Current CI definitions were inspected, but this audit does not claim the latest workflow runs are green unless a current run is separately verified.
4. Other AI-Verse repos were not used as primary truth during the standalone reconstruction.
5. The absence of a generic cross-component write dispatcher is based on current protocol/interface/code-path review; future hidden/private systems are outside this repo's evidence.
6. The beta tag comparison uses repository file presence/current CLI content and is therefore directly evidenced.
7. Release status after the reviewed head may change and should trigger a living-spec update.
