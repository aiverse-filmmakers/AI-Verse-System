# AI-Verse Brain Component Specification

**Component:** AI-Verse Brain  
**Repository audited:** `aiverse-filmmakers/AI-Verse-Brain`  
**Reviewed branch:** `main`  
**Reviewed head:** `bef8261ad35d126d29aeff5d496f46904125b7b6`  
**Audit date:** 2026-09-13  
**Method:** `docs/AUDIT-METHODOLOGY.md`, evidence-first, repo-local baseline, contradiction and negative-space passes included.

---

## 1. Executive verdict

AI-Verse Brain is a real implementation, not a design-only repository.

Its deterministic intelligence and safety core is mature for a beta candidate. The reviewed head has strong enforcement for explicit user authority, scoped Brain state, policy tightening, bounded cognition, strategic ownership, exact action approvals, host permission intersection, replay safety, receipt-backed side effects, evidence-backed objective closure, learning/evolution limits and standalone/native operation.

It is **not yet complete under the AI-Verse “works perfectly like a glove” criterion**.

The main remaining problems are lifecycle and product-path completeness rather than missing cognition machinery:

1. `disable` has no symmetric public `enable` command. The internal API can enable Brain, but the supported CLI cannot.
2. A standalone Brain that later becomes part of a native AI-Verse root has no supported standalone-to-native adoption/migration transaction. Native doctor treats the surviving `.ai-verse-brain` store as a parallel-store failure.
3. There is no one-shot implementation/adoption command that proves installed Brain is attached, initialized, host-integrated, onboarding-ready and, where chosen, strategically adopted. Strategic authority transfer correctly remains separate, but the availability path is still multi-step.
4. `doctor` is primarily structural. It can report `ok=true` while Brain is unattached or uninitialized because those conditions are warnings, so `ok` must not be interpreted as runtime readiness.
5. `docs/INSTALLATION.md` contains a current `run-tick` example that omits the now-required host choice. Current code requires exactly one of `--host-adapter` or `--read-only-context`.
6. Current `main` is 20 commits ahead of immutable tag `v0.1.0-beta.1`. The post-tag hardening includes core lifecycle, ownership, permission, retrieval and receipt work. No GitHub Release object exists even though `docs/RELEASE.md` says the beta shipment should create one.
7. The local extension-registry lock has no stale-lock recovery. A process crash while holding `.aiverse/extensions/registry.json.lock` can leave later lifecycle mutations blocked until manual repair.
8. CI passes strongly, but bridge tests currently emit unclosed-file `ResourceWarning`s.
9. The OS direction cross-repo workflow is valuable compatibility evidence but still contains a legacy tracked-manifest fixture and tracks current OS `main`, so it is not a fully pinned exact end-user product-path proof.
10. The general cross-component owner-routed durable-write path remains a system-level gap. Brain can classify canonical write ownership and exposes host routing concepts, but the cognition/learning pipeline does not itself complete every OS/Memory/Knowledge/Capability canonical write transaction.

**Current-target verdict:** strong beta engine and strong native safety model, with specific lifecycle/distribution/readiness gaps before seamless member-facing completion.

---

## 2. CURRENT identity

AI-Verse Brain is a portable deterministic intelligence-control layer for long-horizon agents.

It owns Brain-specific intelligence state and control semantics such as:

- explicit intent;
- desired state and success definition;
- practices;
- gaps;
- opportunities;
- initiatives;
- objectives;
- progress/stall interpretation;
- model beliefs;
- evaluations;
- learnings;
- strategy rules;
- Brain policy;
- attention decisions;
- verification state;
- durable side-effect receipt references required for Brain replay safety.

Its implemented responsibility split is:

```text
Brain  = why / where / what next / how to verify / how to improve
OS     = structure / scope / routing / capabilities / connections / execution boundaries
Memory = historical recall / provenance / supersession
Host   = model and tool execution
```

The repository is Python, requires Python 3.9+, declares no required third-party runtime Python dependencies, and exposes the `ai-verse-brain` CLI.

---

## 3. LAW

The following laws are enforced by code/tests and should be treated as architectural invariants.

### 3.1 Model reasoning is not authority

Model output is advisory. It cannot silently redefine user goals, policy, permissions, privacy boundaries, risk posture or success meaning.

### 3.2 Proactivity is not permission

P0-P4 affects cognition/surfacing behavior, not external side-effect authority.

### 3.3 One canonical owner per state class

Brain owns Brain intelligence state. OS owns OS current state and system structure. Memory owns historical recall state. Skills/capability providers own capability implementation. Host/runtime owns actual execution.

### 3.4 One strategic owner per native scope

A native scope has one active strategic owner, `os` or `brain`. Installation does not silently steal direction ownership.

### 3.5 Read boundaries must honor ownership too

When Brain owns direction, native current-context reads use the OS ownership-aware resolver and do not reactivate frozen OS strategy by raw-file fallback.

### 3.6 Native writes fail closed

Normal native writes require:

- compatible AI-Verse OS v2 host;
- supported, installed and enabled local Brain attachment;
- valid Brain installation marker.

Initialization is the only bootstrap exception to the marker requirement.

### 3.7 External effects require restrictive permission intersection

Brain permission and host permission intersect. Either layer may deny or require additional approval. Host `allow` cannot weaken Brain policy.

### 3.8 Approval is exact-action authority

Approval is bound to exact request identity and fingerprint, including scope, action class, operation, parameters and idempotency key.

### 3.9 Uncertain side effects are not automatically replayed

If effect outcome cannot be proven, Brain records uncertainty and requires reconciliation.

### 3.10 Action success is not objective success

Objective completion remains evidence/criterion governed. A successful external action alone does not close the objective.

### 3.11 Higher-scope policy may only be tightened

Workspace/caller policy cannot weaken operator restrictions.

### 3.12 Brain does not own the scheduler

Brain owns cadence intent and emits plans/hooks. Host/runtime owns scheduling execution.

### 3.13 Runtime state is disposable coordination, not canonical intelligence

Locks/cooldowns/trigger coordination may be runtime state, while confirmed intent, evaluations, learning, policy and durable action proof live in canonical Brain state.

---

## 4. INTENDED identity

The repository’s intended end state is a universal intelligence layer usable:

- standalone;
- inside AI-Verse OS;
- through capable non-AI-Verse agents/runtimes;
- with optional Memory, Skills, Connections and Data through host/component contracts rather than direct ownership leakage.

The desired user experience is that Brain can be installed at any point, safely adopted, discovered, health-checked and used without duplicating host truth or requiring manual internal file wiring.

The current beta target is narrower than a final 1.0 ecosystem target, but it still implies a real installable package with safe lifecycle, host integration and external testing readiness.

---

## 5. Canonical state and source of truth

### Native mode

```text
operator/brain/
workspaces/<id>/brain/
runtime/ai-verse-brain/
```

### Standalone mode

```text
.ai-verse-brain/
.ai-verse-brain/runtime/
```

Current canonical object families:

- `intent`
- `practice`
- `gap`
- `opportunity`
- `initiative`
- `objective`
- `model_belief`
- `evaluation`
- `learning`
- `strategy_rule`
- `policy`

Every Brain object carries typed envelope information including ID, kind, scope, status, revision, timestamps, provenance/evidence references and payload.

Writes use atomic replacement and optimistic revision checks. Per-object runtime locks provide local concurrency coordination.

---

## 6. Explicit non-ownership

Brain must not become canonical owner of:

- workspace identity;
- general OS current state;
- operator profile as a whole;
- generic historical memory;
- generic reusable knowledge;
- connections or credentials;
- capability implementation/packages;
- scheduler implementation;
- vendor model/runtime state;
- sibling component canonical databases;
- arbitrary external execution state.

Brain may reason over and reference these domains through bounded host/component contracts.

---

## 7. Architecture

The implemented conceptual flow is:

```text
explicit intent
  -> current-state comparison
  -> gap
  -> opportunity
  -> initiative
  -> objective
  -> action/observation
  -> progress or stall
  -> verification
  -> learning
  -> controlled strategy evolution
```

The architecture deliberately separates:

### Direction loop

```text
current state -> desired state -> gap -> opportunity -> initiative -> priority
```

### Action loop

```text
objective -> completion contract -> act/observe -> progress/stall -> verify -> close/replan/block
```

### Learning/evolution loop

```text
experience -> evidence -> reflection -> learning -> strategy candidate -> promote/reject -> monitor
```

This separation prevents one unbounded prompt from becoming both reasoner and authority.

---

## 8. Scope and isolation

Current scopes are:

```text
operator
workspace:<workspace-id>
```

At reviewed head, workspace IDs are aligned with the OS-style canonical grammar:

```text
[a-z0-9][a-z0-9-]{0,127}
```

Standalone core v0.1 directly supports operator scope. Native workspace state is physically mapped inside the corresponding workspace and scope paths are checked for containment.

Cross-workspace access is not inferred simply because a model asks for it.

---

## 9. Intent, onboarding and strategic ownership

### Onboarding

Onboarding is explicit and dry-run-first. Brain requires at minimum:

- desired state;
- definition of success.

Optional explicit answers include goals, boundaries, constraints and practices.

Identical answers are deduplicated.

### Native strategic ownership

Native scopes default to OS strategic ownership unless explicitly handed to Brain.

Handover to Brain:

```bash
ai-verse-brain direction-owner <root> --scope operator --handover-to-brain
ai-verse-brain direction-owner <root> --scope operator --handover-to-brain --apply --confirm-import
```

Supported OS strategic statements are imported with path and SHA-256 provenance before active ownership completes.

Handback to OS:

```bash
ai-verse-brain direction-owner <root> --scope operator --handover-to-os
ai-verse-brain direction-owner <root> --scope operator --handover-to-os --apply --confirm-export
```

Brain exports current strategic intent, updates only the bounded OS strategic section, preserves operational context, then flips the durable ownership marker. Brain objects remain as provenance.

Concurrent scope handovers use per-scope coordination plus a shared registry lock. Interrupted activation is resumable.

---

## 10. Cognition and runtime

`BrainRuntime` keeps model reasoning outside deterministic authority.

Runtime sequence:

```text
write readiness
-> effective policy refresh
-> trigger claim
-> deterministic tick plan
-> bounded context assembly
-> reasoner call where proposal kinds exist
-> strict proposal parsing
-> deterministic proposal application
-> attention decision
-> trigger completion
```

Reasoner/application errors are captured as structured tick errors. One bad proposal does not become an automatic replay path.

Explicit orientation can be useful without a reasoner call.

The runtime does not automatically convert surfaced items into host notifications and does not let cognition call external action execution implicitly.

---

## 11. Host and adapter boundary

Current real-host selection is explicit.

A `run-tick` invocation must choose exactly one of:

```text
--host-adapter <config>
--read-only-context
```

A requested real host is live-handshaken and must expose:

- `read_context`
- `retrieve_history`
- `list_capabilities`
- `list_connections`

Missing/incomplete/unstartable real hosts fail closed. There is no silent downgrade to the limited read-only host.

The built-in read-only host is intentionally limited and has no external action authority.

The JSON subprocess bridge uses argv execution rather than shell execution, bounded I/O/timeouts, filtered environment forwarding and credential-bearing command checks.

---

## 12. Vendor reasoners

Built-in wrappers exist for:

- Claude Code;
- Codex CLI;
- Hermes Agent.

They advertise reasoner behavior, not Brain action authority.

The wrapper posture is deliberately restrictive and still depends on external vendor CLI behavior, so the release checklist correctly requires current flag verification before immutable release.

---

## 13. Retrieval

Brain builds semantic history/capability queries from the real cognition task and current canonical context rather than literal internal purpose labels.

Capability selection validates and ranks the full bounded candidate set before applying the final reasoning-context limit.

Provider order is only a tie-breaker. Candidate overflow fails closed rather than silently hiding candidates after an arbitrary cutoff.

This is CURRENT implementation, not merely design intent.

---

## 14. Policy and attention

Brain persists effective policy and reloads it for runtime use.

Workspace policy and caller overrides may only tighten the operator baseline.

Attention includes:

- WIP caps;
- proactive item limits;
- interruption limits;
- notification thresholds;
- cooldowns.

Notification classes include interrupt, surface, batch, store and drop semantics.

Silence can be a valid result.

---

## 15. Progress, verification and learning

Brain distinguishes lifecycle status from evidence-backed progress.

Important current rules include:

- repeated unchanged state is not progress;
- changed state without evidence is not sufficient progress;
- attempt budgets do not self-expand;
- repeated non-progress may become stalled;
- objective pass requires explicit criteria;
- passed criteria require evidence;
- high-impact work requires stronger verification independence;
- learning requires staged evidence;
- strategy evolution cannot escalate itself into new user authority;
- high evolution tiers cannot silently runtime-promote privileged changes.

---

## 16. External action boundary

External side effects are a separate explicit runtime path.

Current controls include:

- immutable/deep-frozen action parameters;
- exact request fingerprint;
- exact explicit-user approval grant;
- Brain policy gate;
- host permission check before dispatch claim;
- host permission recheck at the actual dispatch edge;
- idempotency coordination;
- durable side-effect receipt references;
- no automatic replay of uncertain effects;
- verified reconciliation.

A late host permission revocation is recorded as zero effect rather than uncertain effect because dispatch has not occurred.

---

## 17. Skills receipt integration

Brain contains an independent consumer for `aiverse-execution-receipt-v2`.

It validates exact binding to:

- Brain action fingerprint;
- scope;
- action class;
- operation;
- provider ID;
- capability ID;
- immutable generation ID;
- package digest.

`trace_id` is correlation only, not durable proof.

External effect proof and objective criterion proof remain separate.

The Brain workflow pins the tested Skills commit for this contract, which is stronger reproducibility evidence than a moving sibling branch.

---

## 18. Lifecycle matrix

| Stage | CURRENT | Verdict |
|---|---|---|
| package install | pip/pipx or editable checkout | IMPLEMENTED |
| detect compatible host | standalone / OS v2 / incompatible | IMPLEMENTED |
| plan install | `init` dry run | IMPLEMENTED |
| initialize | `init --apply` | IMPLEMENTED |
| attach | local extension-registry `attach --apply`; native init auto-attaches | IMPLEMENTED |
| enable | internal `set_brain_enabled(..., True)` only, no CLI command | **GAP** |
| disable | `disable --apply`, blocked while Brain owns strategic direction | IMPLEMENTED |
| strategic adoption | explicit OS-to-Brain handover with confirmed import | IMPLEMENTED |
| strategic handback | explicit Brain-to-OS export then ownership flip | IMPLEMENTED |
| host activation | explicit host adapter/read-only choice per tick; no one-shot adoption command | PARTIAL |
| onboarding | dry-run-first explicit intent ingestion | IMPLEMENTED |
| cadence | plan/hooks only; host installs/runs scheduler | IMPLEMENTED BY DESIGN |
| doctor | structural state/install/attachment/onboarding checks | PARTIAL READINESS |
| migrate same schema | package metadata refresh | IMPLEMENTED |
| migrate older schema | fails closed, no registered conversion path yet | **GAP for future upgrades** |
| update package | external package-manager operation + migration | PARTIAL UX |
| detach | removes local attachment, preserves Brain state; blocked while Brain owns direction | IMPLEMENTED |
| reinstall after detach | state preserved and can be reattached/reinitialized | MOSTLY IMPLEMENTED |
| standalone -> later native OS adoption | no supported canonical state relocation/handoff | **GAP** |
| reconcile lifecycle | no general component reconcile command | **GAP / SYSTEM UX** |
| rollback package/state | fail-closed compatibility checks, no explicit rollback workflow | PARTIAL |
| uninstall | package manager can remove code; no Brain CLI uninstall contract | PARTIAL |

### Key lifecycle defect: missing enable

`extension_registry.py` has a valid internal setter for `enabled=True/False`, but `cli.py` exposes only `disable`.

`attach` intentionally preserves an existing `enabled` field. Therefore:

```text
disable
-> attach again
-> still disabled
```

The only supported-looking workaround is detach then attach, which is not lifecycle symmetry and is dangerous UX around a state-preserving component.

This should be repaired with an explicit `enable` command and tests for `disable -> enable -> write-ready`.

---

## 19. Install-order analysis

### OS first, Brain later

**CURRENT: good.**

On a compatible clean OS root, Brain `init --apply` can create its local attachment and Brain-owned state without editing tracked OS configuration.

### Brain standalone first, OS later

**GAP.**

Standalone state lives in `.ai-verse-brain/`. Once the same root becomes native AI-Verse, storage detection switches to native paths and doctor treats `.ai-verse-brain` inside native mode as a parallel store.

No current lifecycle command imports/relocates that standalone canonical state into native `operator/brain/` while preserving provenance and guaranteeing one writable owner.

Therefore Brain does not yet satisfy full install-order independence.

### Brain detached and later reattached

**Mostly good.**

Detach preserves state. A later attach/init can restore availability, provided strategic ownership has already been safely returned where required.

---

## 20. Doctor and readiness semantics

Current doctor checks:

- host compatibility;
- parallel standalone store in native mode;
- local attachment state;
- installation marker;
- Brain JSON kind/scope integrity;
- onboarding minimums;
- workspace state scanning;
- optional Memory detection information.

However, doctor currently treats some unavailable states as warnings:

- unattached native Brain;
- uninitialized Brain.

This can leave `report.ok == true` while Brain cannot perform normal native writes.

Therefore:

```text
doctor ok
!=
runtime ready
!=
fully integrated
!=
operationally verified
```

The mature interface should expose explicit readiness dimensions or states rather than overload one boolean.

Doctor is currently best classified as **structural/attachment health with limited readiness hints**, not dependency, runtime, operational or whole-system proof.

---

## 21. Migration and upgrades

Current migration is deliberately conservative.

It can:

- validate marker schema;
- reject newer unsupported state;
- reject unknown older state without a registered migration;
- refresh package version metadata when state schema is unchanged.

It currently has no real historical state-schema conversion path because the active state schema remains `1.0`.

This is acceptable for the first schema generation, but not sufficient evidence for future upgrade maturity.

Before the first state schema bump, the repository needs an actual migration implementation and acceptance path.

---

## 22. CI and acceptance evidence

At the final workspace-scope hardening PR head, all three workflows were green:

- `CI`
- `OS Direction Ownership Contract`
- `Skills Receipt Contract`

Core CI includes:

- Ubuntu, Python 3.9 and 3.12;
- macOS, Python 3.9 and 3.12;
- Windows, Python 3.9 and 3.12;
- wheel build and clean virtual-environment install smoke.

The reviewed final PR merge gate ran **198 tests successfully per matrix runner**.

This is strong evidence for current code behavior.

### CI caveats

1. Bridge tests emit unclosed-file `ResourceWarning`s around subprocess pipes. Not a functional failure, but cleanup debt.
2. The OS direction contract clones current OS `main`, so it is a compatibility canary rather than a fully reproducible pinned pair.
3. That workflow still contains a legacy tracked `AI-VERSE.yaml` Brain-registration fixture before initialization, even though current local attachment authority is `.aiverse/extensions/registry.json`. The workflow proves important direction behavior but should be cleaned so the fixture matches the exact current product path.
4. The package smoke tests standalone installation. Native clean-install/adoption proof is spread across unit/cross-repo workflows rather than one member-style end-to-end shipment test.

---

## 23. Release state

`v0.1.0-beta.1` exists as a tag.

Current `main` is **20 commits ahead** of that tag.

Those 20 commits contain major hardening, including:

- persisted effective policy enforcement;
- exact immutable action approvals;
- native write readiness;
- strategic direction ownership;
- explicit host selection;
- meaningful retrieval;
- host permission intersection;
- Skills receipt verification;
- useful explicit tick output;
- frozen strategy read boundaries;
- direction-registry concurrency repair;
- local extension attachment lifecycle;
- workspace scope grammar hardening.

Therefore the immutable beta tag is not equivalent to current hardened Brain behavior.

The GitHub releases endpoint returned no Release objects. `docs/RELEASE.md` says beta shipment should create a GitHub prerelease from the exact tag, so the current repository is also incomplete against its own release checklist.

**GAP:** create a new immutable beta/release candidate from current hardened code, update version/changelog/docs accordingly, and verify that exact artifact.

---

## 24. Documentation drift

### Current broken installation example

`docs/INSTALLATION.md` currently shows a `run-tick` example without either required host-mode argument.

Current CLI parser requires one of:

```text
--host-adapter
--read-only-context
```

A second standalone example uses `--context-file` but likewise omits `--read-only-context`, even though code restricts context files to that mode.

These commands are not executable as written.

### Historical research wording

`research/README.md` correctly says the directory preserves pre-implementation research, but its “Current status” section still says no production Brain engine has been implemented. That statement is HISTORICAL, not current repository truth.

The section should be relabeled to prevent agents/readers from misclassifying it.

### Release docs/version drift

Current public docs describe post-tag behavior while the immutable beta tag predates it. Development and released behavior must be clearly separated.

---

## 25. Concurrency and crash recovery

Strong current controls:

- optimistic object revisions;
- per-object stale-lock recovery;
- trigger/action idempotency;
- direction per-scope locks;
- shared direction registry lock;
- atomic state/registry writes;
- uncertain side-effect replay blocking.

Remaining issue:

`extension_registry.py` creates `.aiverse/extensions/registry.json.lock` with `O_EXCL` and always deletes it in normal/finally paths, but there is no timestamp/token/TTL stale-lock recovery.

A hard process termination can leave the lock file behind and future attachment/enable/disable/detach mutations fail as “registry busy.”

**GAP:** use a shared OS-owned registry mutation primitive or add bounded stale-lock recovery with ownership-safe semantics.

---

## 26. Performance and scale

For beta/local use, the file-per-object design is understandable and inspectable.

Current scale limits include:

- object listing scans JSON directories;
- doctor scans Brain JSON across workspaces;
- no index/pagination layer for large canonical state collections;
- capability candidate validation/ranking is bounded explicitly rather than unbounded;
- context output is deliberately bounded.

No current evidence shows a production-scale benchmark target. This is not a beta blocker, but should remain visible before very large operator/workspace histories are expected.

---

## 27. Portability

Strong portability properties:

- Python 3.9+;
- tested on Linux/macOS/Windows;
- no mandatory third-party runtime package dependencies;
- JSON subprocess adapter contract;
- standalone mode;
- host/runtime separation;
- reasoner wrappers do not own action permission;
- cadence hooks do not assume scheduler ownership.

Portability limitation:

Standalone-to-native canonical state adoption is not yet implemented, so “can run standalone” does not yet imply “can later become native without migration work.”

---

## 28. Cross-component write path

Brain contains a write-classification concept and host routing boundary, but there is no complete generic automatic pipeline by which arbitrary cognition/learning durable candidates become canonical OS/Memory/Knowledge/Capability writes.

The correct future system path is:

```text
Brain/agent identifies durable candidate
-> classify canonical owner
-> immutable bounded write request
-> host/OS rechecks scope, permission and authority
-> owner component validates current state/idempotency
-> canonical effect
-> receipt/provenance
-> Brain references result without duplicating owner truth
```

Brain should not solve this by directly writing sibling internal storage.

---

## 29. HISTORICAL evolution

The repository history shows a coherent progression:

- PR #1: deterministic Brain core;
- PR #2: shipment/installability foundation;
- PR #3: `v0.1.0-beta.1` release candidate;
- PR #4: persisted effective policy repair;
- PR #5: exact action approval binding;
- PR #6: native write readiness;
- PR #7: single strategic direction owner;
- PR #8: explicit real host selection;
- PR #9: meaningful Memory/capability retrieval;
- PR #10: Brain/host permission intersection;
- PR #11: Skills receipt verification;
- PR #12: useful explicit tick output;
- PR #13: frozen strategy read boundary;
- PR #14: shared direction registry concurrency repair;
- PR #15: host adapter documentation repair;
- PR #16: local attachment and safe lifecycle hardening;
- PR #17: workspace ID contract hardening.

Important history lesson: several crucial safety properties were repairs after the original beta candidate. Those repairs should be promoted into permanent LAW, not treated as incidental patch history.

---

## 30. INSPIRATION lineage

The repository’s preserved research explicitly studies or references systems including:

- LifeOS;
- Hermes;
- AIS-OS;
- Letta;
- OpenClaw;
- ACE;
- Hermes Self-Evolution;
- GEPA;
- Voyager;
- Generative Agents;
- Reflexion;
- PersonalOS;
- Pascal Jarvis;
- DeerFlow;
- Honcho;
- LangMem;
- Agent Zero;
- Magentic-One;
- Anthropic long-running-agent work.

These are INSPIRATION/HISTORICAL evidence, not proof that current Brain implements every source mechanism.

The central design result of the research is that the missing layer is not another filesystem or another Memory database. It is explicit intent plus bounded cognition, initiative, verification, learning and controlled evolution.

---

## 31. Completeness matrix

| Dimension | Current status | Notes |
|---|---|---|
| core state model | COMPLETE for current beta | real typed canonical objects and state machines |
| authority model | COMPLETE for current beta | model/external data do not become authority |
| strategic ownership | COMPLETE for current beta | explicit reversible OS/Brain ownership transaction |
| storage isolation | STRONG | native/standalone scope and path checks |
| policy enforcement | STRONG | persisted and tightening-only overrides |
| cognition pipeline | STRONG | bounded reasoner proposals, deterministic apply |
| action safety | STRONG | permission intersection, exact approvals, idempotency, receipts |
| verification | STRONG | criterion/evidence gates and Skills receipt bridge |
| learning/evolution | STRONG | staged, authority bounded |
| host portability | STRONG | bridge + explicit host selection |
| native install after OS | COMPLETE | clean OS can auto-attach/init |
| standalone mode | COMPLETE for operator scope | real usable self-contained state |
| Brain-before-OS adoption | **INCOMPLETE** | no standalone-to-native migration |
| enable/disable lifecycle | **INCOMPLETE** | disable exists, public enable missing |
| detach/handback safety | STRONG | state preserved, ownership protected |
| lifecycle reconcile | INCOMPLETE | no generic reconciliation/adoption command |
| doctor/readiness | PARTIAL | structural `ok` is not runtime-ready proof |
| migrations | PARTIAL | fail-closed, only same-schema metadata refresh today |
| distribution | **DRIFTED** | hardened main is 20 commits beyond beta tag |
| GitHub release process | INCOMPLETE | no Release object found |
| docs consistency | PARTIAL | broken install run-tick examples, historical drift |
| cross-component write routing | SYSTEM GAP | classification exists, generic canonical handler chain incomplete |
| CI | STRONG | 198 tests per runner + package smoke + two contract workflows |
| CI cleanliness | MINOR DEBT | bridge ResourceWarnings |
| scale/indexing | FUTURE/UNPROVEN | file scans acceptable beta, not benchmarked large-scale |

---

## 32. Exact remaining work before “works perfectly like a glove”

### P0 lifecycle correctness

1. Add public `enable` CLI with dry-run/apply semantics.
2. Add acceptance test: initialize -> disable -> verify writes blocked -> enable -> verify same state resumes safely.
3. Add stale-lock recovery or OS-owned mutation API for extension registry operations.

### P0 install-order/adoption

4. Design explicit standalone-to-native migration/adoption.
5. Snapshot and verify standalone source before migration.
6. Import/relocate canonical Brain objects without creating two writable Brain stores.
7. Record provenance/handoff and retire the standalone writable route only after native verification.
8. Add acceptance test for Brain-first then OS-later install order.

### P0 release truth

9. Cut a new immutable prerelease from hardened main or equivalent reviewed successor.
10. Update version/changelog/release docs.
11. Create the GitHub prerelease required by the repository’s own checklist.
12. Test exact immutable installation artifact, not only source `main`.

### P1 readiness and product path

13. Make doctor/readiness output explicitly distinguish installed, attached, enabled, initialized, host-ready, onboarding-ready and operationally verified.
14. Add one member-style native acceptance flow starting from stock compatible OS without legacy tracked-registration fixture.
15. Pin the sibling revision for reproducible acceptance, or explicitly label a second moving-main workflow as a compatibility canary.
16. Add an implementation/adoption UX that can reconcile available Brain into a host without transferring strategic ownership implicitly.

### P1 docs/quality

17. Fix `docs/INSTALLATION.md` host-mode examples.
18. Relabel stale pre-implementation research “Current status” as historical.
19. Separate released-tag documentation from development-main documentation.
20. Close subprocess pipes cleanly so CI no longer emits ResourceWarnings.

### P1/P2 system integration

21. Complete the owner-routed canonical write pipeline at system level without direct sibling-storage writes.
22. Before state schema 1.0 changes, implement and test a real registered migration path.
23. Decide/document update, uninstall, rollback and reconcile UX for stable member lifecycle.

---

## 33. Definition of done for current seamless target

Brain can be called seamless for the present AI-Verse milestone when all of the following are true:

- a compatible OS can exist before Brain and Brain adopts cleanly;
- Brain can exist standalone before OS and later migrate/adopt cleanly;
- attach, enable, disable and detach are all supported symmetrically where relevant;
- strategic ownership transfer remains explicit and separate from component activation;
- disable/detach never strand or silently reactivate stale strategy;
- one canonical Brain store exists after any supported adoption path;
- doctor/readiness truthfully distinguishes discovered, attached, initialized, runtime-ready and operational states;
- the documented native install/tick path works exactly as written;
- the immutable distributed version contains the architecture the docs claim;
- a stock-user acceptance test proves install -> attach -> init -> host integration -> onboarding -> optional direction handover -> tick -> disable/enable -> safe handback/detach;
- cross-component writes occur through owner-controlled contracts, not direct Brain access to sibling storage;
- CI is green and free of known lifecycle-fixture contradictions.

---

## 34. Supreme-system contribution

Brain contributes the system’s **direction, initiative, verification and controlled-learning layer**.

Its most important system contribution is not “more autonomous AI.” It is the opposite: it creates durable machinery that lets an agent reason proactively while keeping user intent, policy, ownership, execution authority and evidence outside the model’s unilateral control.

That architecture is already substantially real.

The remaining work is to make the lifecycle and distribution experience as rigorous as the core intelligence/safety engine.