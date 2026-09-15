# A1.3 — Independent Repository Audit: AI-Verse-Brain

**Audit program:** Independent Whole-System Public-Beta Audit  
**Phase:** A1 Independent repository audits  
**Task:** A1.3 AI-Verse-Brain  
**Audit date:** 2026-09-15  
**Frozen repository ref:** `6f986e8d06c7f9c069fbf05aa92ae7b7a1af9bf4`  
**System control baseline:** `d491eb5c852f4a57c4189652c399940895927d8a`  
**Repository role reconstructed from itself:** canonical persistent intent / Goal / strategic reasoning and verification owner  
**Audit status:** **COMPLETE**  
**Standalone product verdict:** **DOGFOOD BLOCKED**  
**R-a Reconstruction:** COMPLETE / PASS  
**R-b Enforcement:** COMPLETE / MATERIAL FAILURES FOUND  
**R-c Verdict:** COMPLETE / BLOCKED  
**Findings opened:** `WSA-2026-009`, `WSA-2026-010`, `WSA-2026-011`  
**Next task:** A1.4 AI-Verse-Memory

> Audit-completion points measure completed forensic work, not product acceptance. Brain remains behind the dogfood gate because A1.3 found one HIGH and one MEDIUM product defect.

## 1. Independence statement

This packet reconstructs AI-Verse-Brain from the frozen Brain repository itself.

Substantive evidence came only from:

- files tracked in `aiverse-filmmakers/AI-Verse-Brain` at the frozen SHA;
- Brain-owned GitHub repository metadata, commit/PR history and Actions;
- tests, fixtures, research and cross-owner workflows defined by Brain.

No sibling repository source was opened to fill a standalone Brain gap.

Brain workflows that clone OS or Skills are evidence only of what Brain tests against those revisions. They do not independently prove the sibling implementation. Cross-validation is deferred to A2.

No existing AI-Verse-System Brain component spec was used as Brain evidence.

## 2. Pre-task and pre-write drift control

At A1.3 start and immediately before writing:

- Brain `main` = `6f986e8d06c7f9c069fbf05aa92ae7b7a1af9bf4`;
- this exactly matches the frozen A0 snapshot;
- System `main` = `d491eb5c852f4a57c4189652c399940895927d8a`;
- open PRs in Brain and System: **0**;
- no Brain product file was modified;
- Dashboard MC1.4 remains paused.

No drift invalidated the standalone target.

---

# R-a — Reconstruction

## 3. Repository inventory and canonical roots

The frozen recursive tree is complete and not truncated:

- tracked entries: **152**
- canonical engine files: **59**
- tests: **26**
- schemas: **20**
- protocol documents: **11**
- current docs: **6**
- research/provenance documents: **6**
- GitHub workflows: **4**

Primary regions:

| Region | Role |
|---|---|
| `engine/aiverse_brain/` | canonical Brain implementation |
| `schemas/` | machine-readable object/action/cognition contracts |
| `protocol/` | authority, action, verification, direction, learning and runtime laws |
| `tests/` | behavioral, security and release acceptance |
| `.github/workflows/` | cross-platform CI and cross-owner contracts |
| `release/component-release.json` | immutable accepted release metadata |
| `research/` | architecture research and source provenance |

No external Python runtime dependency is declared. Brain is implemented with Python standard-library primitives plus external tools only through explicit subprocess/host boundaries.

## 4. Product identity and version

Current package metadata:

- package: `ai-verse-brain`
- Python: `>=3.9`
- version source: `engine/aiverse_brain/_version.py`
- current version string: `0.1.0b2` / `0.1.0-beta.2`
- license: MIT
- repository visibility: public

The repository frames Brain as a universal durable intelligence/control layer rather than an execution host.

Central law:

> model reasoning is advisory; deterministic policy decides what may happen and the host proves what happened.

## 5. Canonical ownership

Brain canonically owns scoped strategic/intelligence state including:

- confirmed intent;
- practices;
- gaps;
- opportunities;
- initiatives;
- objectives;
- persistent Goals;
- derived beliefs;
- evaluations;
- learning objects/candidates;
- strategy rules;
- Brain policy state;
- minimal durable side-effect receipt references;
- installation/adoption metadata required for Brain-owned state.

Brain explicitly does **not** own:

- workspace identity;
- OS current-context truth;
- operator profile as a whole;
- general historical Memory;
- reusable capability implementation;
- Connections/secrets;
- scheduler implementation;
- external side-effect execution;
- vendor model runtime.

Runtime locks, cadence receipts, attention delivery state and transient coordination are explicitly disposable.

## 6. Scope and storage model

Scopes are constrained by a deterministic regex to:

- `operator`;
- `workspace:<lowercase-id>`.

Standalone mode supports operator Brain state under:

`.ai-verse-brain/`

Native mode uses:

- `operator/brain/`;
- `workspaces/<id>/brain/`;
- `runtime/ai-verse-brain/`.

Object IDs reject slash/backslash traversal forms.

Object writes:

- validate object kind/status/payload;
- use per-object lock files;
- use optimistic `expected_revision`;
- write through temp file + fsync + `os.replace`;
- preserve immutable scope/kind and creation provenance.

Core parent-directory containment has one material gap recorded as `WSA-2026-009`.

## 7. Direction ownership

Brain contains an explicit single-owner direction protocol.

Default native direction owner remains OS.

Brain setup/onboarding does not silently take strategic ownership.

Explicit OS -> Brain handover:

- inspects existing OS strategic sources;
- imports with source path/hash provenance;
- requires explicit confirmation;
- updates an OS-local durable ownership registry;
- uses a registry-wide lock;
- preserves Brain ownership across Brain runtime/state loss.

Brain -> OS handback:

- exports current Brain strategy;
- writes only the bounded OS strategic section;
- preserves operational/current-state sections;
- verifies the export/write before flipping ownership back to OS.

Direction-registry and strategic-file helpers explicitly reject unsafe symlinks.

## 8. Persistent Goal owner

Brain is the canonical persistent Goal owner.

Goal service supports:

- create;
- get/list;
- edit;
- pause/resume/block/complete;
- criteria add/remove/clear;
- progress recording;
- deterministic evaluation;
- continuation contract.

Goal safety includes:

- user-authority requirements for mutating strategic state;
- optimistic version checks;
- operation receipts;
- deterministic Goal IDs for create;
- evidence-bound criteria;
- model inference alone cannot pass completion criteria;
- no-progress and budget exhaustion block rather than self-expand;
- continuation contract grants no tools/scheduling/Connections/permission expansion.

Concurrent cross-Goal operation-ID admission has one defect recorded as `WSA-2026-010`.

## 9. Direction, action and learning loops

### Direction

Current state + desired state -> gap -> opportunity -> initiative.

Hard gates, cooldown, WIP limits and inspectable ranking precede surfacing.

Proactivity level does not grant side-effect permission.

### Action

Objectives have explicit completion criteria and attempt/stall budgets.

Material completion requires evidence and the configured independence floor.

V2 requires fresh-context evaluation.

V3 requires independent model or authoritative external verification.

### Learning

Learning is staged.

Runtime cannot promote high-tier strategy merely by model assertion.

Policy/permission/identity/privacy/scope/risk semantics cannot self-expand through learning.

## 10. Effective policy and permission intersection

Canonical operator policy is the outer Brain policy.

Workspace policy may only tighten it.

Caller/cadence overrides may not weaken persisted canonical policy.

External actions pass two independent gates:

1. Brain effective policy;
2. host/OS permission decision.

Host decisions are bound to exact request fingerprint, scope and action class.

Host denial always wins.

Host `approval_required` adds an approval requirement.

Permission is rechecked immediately before the real dispatch.

## 11. External action replay/receipt safety

Brain action requests bind:

- action class;
- exact scope;
- operation;
- immutable parameters;
- idempotency key;
- budget/scope/reversibility facts;
- request fingerprint.

Approvals bind exact request ID, idempotency key, scope, action class and request fingerprint.

For side effects:

- autonomous execution requires host idempotency support or explicit approval;
- Brain writes a durable claimed receipt before dispatch;
- host exceptions/invalid responses/uncertain results become durable uncertainty;
- uncertain side effects do not auto-retry;
- successful side effects require a stable host receipt ID;
- completed duplicate requests return prior status without redispatch;
- reconciliation requires stronger evidence.

The public subprocess adapter timeout is capped at 600 seconds, while the action idempotency lock uses a much longer 3600-second TTL, so normal adapter execution does not outlive that lock lease.

## 12. Owner-routed writes and self-learning

Brain classifies durable writes by owner.

Brain-owned state must use Brain APIs.

Non-Brain durable writes require an explicit host `write_route` and a stable owner receipt/reference.

Current automatic candidate gates include:

- substantial reusable-procedure candidates -> Skills owner route;
- repeated bounded structured current truth -> Data owner route.

Runtime-supplied authority/scope/provenance fields are rejected.

Brain does not directly write Skill package bytes, Data canonical state or general Memory state.

## 13. Host/runtime portability

The JSON subprocess bridge:

- requires array commands, not shell strings;
- uses `shell=False`;
- rejects common credential-bearing command flags;
- filters the environment;
- bounds stdin/stdout/stderr;
- caps timeout at 600 seconds;
- binds request/response IDs;
- rejects duplicate JSON keys;
- requires advertised operations.

Built-in wrappers for Claude Code, Codex CLI and Hermes are reasoner-only.

Vendor wrappers are not action hosts and do not inherit Brain authority.

## 14. Lifecycle

Public lifecycle:

- install;
- setup;
- status;
- doctor;
- enable;
- disable;
- update;
- uninstall.

Setup is dry-run-first.

Native setup:

- attaches only the local Brain registry entry;
- initializes/adopts Brain-owned state;
- does not silently transfer direction authority;
- does not patch tracked OS canonical files.

Disable/uninstall:

- preserve canonical Brain state;
- are blocked while Brain owns direction;
- require explicit handback first.

Standalone-to-native adoption:

- validates standalone objects;
- rejects unsafe source object symlinks;
- retires the old writable source;
- stages a copied native state;
- activates the native destination transactionally;
- retains retired source as provenance.

Native destination-parent path safety remains incomplete under `WSA-2026-009`.

## 15. Doctor/readiness

Brain distinguishes:

- compatible host detection;
- local attachment;
- initialization marker;
- migration requirement;
- enabled/disabled state;
- structural health;
- operational live-host checks;
- whole-system composed readiness.

Doctor explicitly says operational model/tool execution and whole-system readiness are not proven unless those layers are actually exercised.

That is appropriately conservative.

---

# R-b — Enforcement

## 16. Security and isolation strengths

Verified enforcement includes:

- strict scope grammar;
- path-safe object IDs;
- native writes require compatible host registration + installation marker;
- incompatible AI-Verse host refuses standalone fallback;
- extension registry rejects symlinks;
- direction registry rejects symlinks;
- adoption source rejects symlinked state objects/directories;
- vendor adapter config rejects shell strings/credential flags;
- secret values are not stored by adapter config;
- model output cannot directly execute actions;
- model output cannot create policy/permission authority;
- exact approval/request binding;
- permission recheck immediately before dispatch;
- uncertain side effects never auto-retry.

Core native state path parents remain vulnerable to a parent-symlink escape, documented below.

## 17. Concurrency and replay strengths

Verified:

- Brain object writes use per-object cross-process lock + expected revision;
- direction ownership registry uses a registry-wide lock;
- Goal create locks on scope + operation ID;
- normal same-Goal mutations lock on scope + Goal ID;
- action side effects lock on idempotency key for the whole dispatch;
- runtime/cadence receipts are deterministic and replay-aware;
- no-progress/budget states do not silently widen themselves.

The cross-Goal Goal-operation namespace mismatch remains a concurrent first-use gap.

## 18. Exact-head CI

Frozen Brain head:

`6f986e8d06c7f9c069fbf05aa92ae7b7a1af9bf4`

Current exact-head push runs:

- CI `34969997987`: SUCCESS
- Skills Receipt Contract `34969998014`: SUCCESS
- OS Direction Ownership Contract `34969997970`: SUCCESS

CI actually executed:

- Ubuntu Python 3.9: SUCCESS
- Ubuntu Python 3.12: SUCCESS
- macOS Python 3.9: SUCCESS
- macOS Python 3.12: SUCCESS
- Windows Python 3.9: SUCCESS
- Windows Python 3.12: SUCCESS
- wheel build + clean venv install/lifecycle smoke: SUCCESS

The full unit suite contains 26 test modules covering authority, cognition/action boundaries, Goals, direction ownership, policy intersection, integration, migration, native readiness, vendor bridge, Skills receipts and runtime hardening.

## 19. Cross-owner workflow evidence

### Skills

The Skills Receipt Contract pins an exact Skills commit:

`558bbcb05ce9f42bb5be30730ea205a7e791bf86`

and proves exact capability/generation/package binding plus conservative effect verification.

### OS direction

The OS Direction Ownership Contract passed and proves Brain's side of direction handover/read semantics.

However, the workflow clones **current OS main** rather than an immutable SHA.

A1.3 therefore treats run `34969997970` as valid historical evidence for the exact environment exercised at that run time, but not as permanently reproducible immutable composition evidence.

This is recorded as an evidence limitation, not a standalone product finding. A2 must revalidate the seam with exact refs.

## 20. Release identity

The immutable accepted release descriptor correctly pins beta.2 to:

`80019be5e6df29aee70371544bd96cedbf0329b9`

Frozen current main is 13 commits ahead:

`6f986e8d06c7f9c069fbf05aa92ae7b7a1af9bf4`

Those later commits include production behavior in `learning.py` and `local_host.py`, not documentation only.

Current main still builds as exactly:

`0.1.0b2`

and README still describes the repository as `0.1.0-beta.2`.

The accepted immutable descriptor remains truthful for its older revision, but the same package version now identifies materially different source trees. See `WSA-2026-011`.

---

# R-c — Contradictions and findings

## 21. C-A1.3-001 — scope/path-safety claim is stronger than native parent containment

**Source A:** `SECURITY.md` says Brain state paths and object IDs are validated for scope/path safety.

**Source B:** executable host/storage/installation code accepts symlinked native `operator/` or `workspaces/` parents because:

- host compatibility uses `Path.is_dir()`, which follows directory symlinks;
- operator state containment checks `operator/brain` relative to `operator` after both are resolved;
- workspace containment checks workspace relative to resolved `workspaces/`;
- initialization/runtime paths then create/write below those resolved symlink parents.

**Higher authority:** executable storage/integration/installation implementation.

**Classification:** implementation defect / filesystem containment.

**Finding:** `WSA-2026-009`.

## 22. C-A1.3-002 — Goal operation-ID replay law is not globally serialized across Goals

**Source A:** README/BRAIN manifest say persistent Goal operations are version checked and idempotent; reused operation IDs with different mutation payload are rejected.

**Source B:** executable Goal code stores receipts by scope + operation ID, but edit/transition/criteria/progress acquire locks by scope + Goal ID. Concurrent first-use operations on different Goals can therefore share one operation ID without sharing one lock.

**Higher authority:** executable Goal implementation.

**Classification:** implementation defect / concurrency-idempotency gap.

**Finding:** `WSA-2026-010`.

## 23. C-A1.3-003 — current main and accepted beta artifact share one package version

**Source A:** release descriptor pins accepted beta.2 to `80019be…`.

**Source B:** current frozen main is 13 commits later, includes production changes, and still reports/builds `0.1.0-beta.2`.

**Higher authority:** current executable version source + immutable release descriptor + commit comparison.

**Classification:** release/version identity drift.

**Finding:** `WSA-2026-011`.

## 24. WSA-2026-009 — native Brain state can escape the selected host root through symlinked parent directories

**Severity:** HIGH  
**Confidence:** PROVEN  
**State:** OPEN  
**Root area:** filesystem containment / scope isolation  
**Affected repo:** `AI-Verse-Brain`  
**Affected journeys:** native setup, initialization, Brain object writes, runtime locks, standalone-to-native adoption

### Expected law

All native Brain-owned state/runtime writes must remain physically inside the selected AI-Verse host root and declared operator/workspace boundary, including when parent paths are symlinks.

### Observed behavior

Host compatibility accepts:

- `<root>/operator` when `is_dir()` is true;
- `<root>/workspaces` when `is_dir()` is true.

Those checks follow symlinks.

For operator state, storage then validates:

`<root>/operator/brain` is inside `<root>/operator`

after resolving both paths.

If `operator` itself points outside `<root>`, both resolve under the same outside target and the check succeeds.

The same structural issue exists for a symlinked `workspaces/` parent.

Installation writes `operator/brain/installation.json`, runtime state and normal canonical objects beneath those paths without rejecting the parent symlink.

The direction and extension registry code demonstrates the intended safer pattern by explicitly rejecting symlink directories/files, but the core state path does not apply that rule.

### Impact

A malformed or adversarial host layout can cause Brain setup and later canonical writes to leave the selected host root and write into external filesystem locations.

This violates the stated isolation/path-safety law and can create canonical state in an unintended authority boundary.

### Required closure evidence

After A6 authorizes repair:

1. reject symlinked native `operator`, `workspaces`, workspace directories and `runtime` parents;
2. verify every final state/runtime/adoption destination realpath remains inside the selected root and intended scope root;
3. apply equivalent checks to installation marker paths;
4. add Linux/macOS/Windows-compatible tests where possible for parent symlink/junction escape;
5. re-audit native setup, normal writes and adoption on the repaired exact ref.

## 25. WSA-2026-010 — Goal operation-ID idempotency can race across different Goals

**Severity:** MEDIUM  
**Confidence:** PROVEN  
**State:** OPEN  
**Root area:** Goal concurrency / replay safety  
**Affected repo:** `AI-Verse-Brain`  
**Affected journeys:** Goal edit/transition/criteria/progress APIs

### Expected law

Within one scope, an `operation_id` is one durable mutation identity. Reusing it for a changed Goal mutation must be rejected even during concurrent first use.

### Observed behavior

Goal receipts are stored under:

`<scope-state>/goal-operations/<sha256(operation_id)>.json`

`create` correctly locks:

`scope|operation_id`

before the second receipt check.

But:

- `edit`;
- `transition`;
- criteria add/remove/clear;
- `record_progress`;

lock:

`scope|goal_id`

before the second receipt check.

Therefore two concurrent mutations using the same `operation_id` against different Goals acquire different locks, can both see no receipt, both commit canonical Goal mutations, then race to replace the single operation receipt.

Sequential reuse is correctly rejected; this is specifically a concurrent first-use gap.

### Impact

A client retry/collision bug can create two canonical Goal mutations while Brain later retains only one operation receipt, weakening replay/audit truth.

Because the effect is confined to Brain-owned Goal state and requires concurrent conflicting operation-ID use, severity is MEDIUM rather than HIGH.

### Required closure evidence

After A6 authorizes repair:

- serialize Goal mutation admission on scope + operation ID as well as object revision;
- preserve per-Goal optimistic concurrency;
- add deterministic concurrent tests using one operation ID across two Goals with different payloads;
- prove exactly one mutation commits and the other receives a changed-payload/idempotency conflict.

## 26. WSA-2026-011 — materially different Brain source trees build with the same beta.2 package version

**Severity:** LOW  
**Confidence:** PROVEN  
**State:** OPEN  
**Root area:** release/version identity  
**Affected repo:** `AI-Verse-Brain`  
**Affected journeys:** source installs, artifact identification, support/debugging, update/release evidence

### Expected law

A public-beta package version should identify one materially defined product state, or a development head should carry a distinct development/pre-release identity so diagnostics do not conflate it with the accepted immutable artifact.

### Observed behavior

Accepted release descriptor:

- version `0.1.0-beta.2`;
- revision `80019be5e6df29aee70371544bd96cedbf0329b9`.

Frozen current main:

- `6f986e8d06c7f9c069fbf05aa92ae7b7a1af9bf4`;
- 13 commits ahead;
- production changes in learning/current-context behavior;
- still builds as `0.1.0b2`.

Release install documentation correctly instructs users to use the immutable beta.2 SHA, which bounds the risk.

### Impact

Version-only diagnostics, installation markers or manually built source artifacts cannot distinguish the accepted beta.2 code from newer development code carrying the same version.

### Required closure evidence

After A6 authorizes repair:

- bump post-release development main to a distinct version identity, or formally accept/reissue the new immutable beta revision;
- ensure README/changelog/version source/release descriptor semantics clearly distinguish accepted artifact from later development head;
- add a release QC rule preventing production-code commits after an accepted release ref from retaining the exact accepted artifact version unintentionally.

---

# R-c — Completeness and verdict

## 27. Lifecycle matrix

| Lifecycle area | State | Conclusion |
|---|---|---|
| package install | VERIFIED | standard Python package, clean wheel smoke passes |
| setup plan | VERIFIED | dry-run-first |
| setup apply | VERIFIED/PARTIAL | bounded attachment/state init; symlink-parent gap WSA-009 |
| initialization | VERIFIED/PARTIAL | marker/state guarded; same path gap |
| status | VERIFIED | layered readiness |
| doctor | VERIFIED | conservative operational/system claims |
| enable | VERIFIED | native attachment state |
| disable | VERIFIED | blocked while Brain owns direction |
| update | VERIFIED/PARTIAL | explicit metadata/state migration; release identity drift WSA-011 |
| uninstall | VERIFIED | detach only, state preserved, direction-owner gate |
| reinstall | VERIFIED | preserved state/attachment model |
| standalone-to-native adoption | VERIFIED/PARTIAL | transactional source retirement; destination path gap WSA-009 |
| direction handover | VERIFIED | explicit, provenance-preserving, registry-wide lock |
| Goal create | VERIFIED | version/idempotency safe |
| Goal non-create mutations | PARTIAL | cross-Goal operation-ID race WSA-010 |
| action dispatch | VERIFIED | exact approval + host permission + durable uncertainty |
| migration | VERIFIED | explicit/fail-closed |
| cross-platform | VERIFIED | 6/6 matrix + artifact smoke |

## 28. 46-lens completeness matrix

| # | Lens | A1.3 state | Conclusion |
|---:|---|---|---|
| 1 | Product identity | VERIFIED | durable intelligence/control layer |
| 2 | Architecture | VERIFIED | direction/action/learning + host boundaries coherent |
| 3 | Ownership | VERIFIED | clear Brain/non-Brain split |
| 4 | Source of truth | VERIFIED | scoped Brain objects + explicit external owners |
| 5 | Provenance | VERIFIED | source/evidence refs, direction import hashes, receipts |
| 6 | Scope | VERIFIED/PARTIAL | strict scope grammar; parent symlink path escape |
| 7 | Isolation | CONTRADICTED | WSA-009 |
| 8 | Privacy/local-first | VERIFIED | no credential value storage; local canonical state |
| 9 | Installation | VERIFIED/PARTIAL | real path, clean smoke; WSA-009 |
| 10 | Attachment/registration | VERIFIED | local extension registry |
| 11 | Activation/adoption | VERIFIED/PARTIAL | safe semantics; destination path gap |
| 12 | Initialization | VERIFIED/PARTIAL | fail closed except symlink parent |
| 13 | Migration/legacy | VERIFIED | explicit migration/adoption |
| 14 | Update/upgrade | PARTIAL | safe state update; version identity drift |
| 15 | Disable/detach/uninstall | VERIFIED | state preserved, direction guard |
| 16 | Install-order independence | VERIFIED/PARTIAL | standalone/native supported; full graph A2/A3 |
| 17 | Discovery | VERIFIED | host/registry/adapters explicit |
| 18 | Readiness | VERIFIED | layered state, no false composed readiness |
| 19 | Health/doctor | VERIFIED | structural vs operational/system separation |
| 20 | Permissions/approvals | VERIFIED | restrictive intersection + late recheck |
| 21 | Security/path safety | CONTRADICTED | WSA-009 |
| 22 | Idempotency/replay | PARTIAL | strong action/create paths; WSA-010 |
| 23 | Concurrency/locking | PARTIAL | object/direction/action locks strong; Goal namespace race |
| 24 | Failure/recovery | VERIFIED | uncertain effects fail closed; adoption resumable |
| 25 | Capability taxonomy | VERIFIED | Brain does not become Skills/Automations/host |
| 26 | Runtime portability | VERIFIED | generic bridge + vendor reasoners |
| 27 | Integration boundaries | VERIFIED AS BRAIN CLAIMS | sibling side deferred A2 |
| 28 | Cross-component writes | VERIFIED AS BRAIN CLAIM | owner-routed receipt required |
| 29 | Read path/retrieval | VERIFIED | current context + meaningful bounded retrieval |
| 30 | Data/schema evolution | VERIFIED | Brain schema + explicit migration |
| 31 | Performance/bounds | VERIFIED | adapter/context/attention/budget bounds |
| 32 | Product/UX | VERIFIED | dry-run-first CLI and explicit handovers |
| 33 | Automation/cadence | VERIFIED | cadence planning without scheduler ownership |
| 34 | Agent behavior | VERIFIED | model advisory, deterministic application |
| 35 | Apps/UI projections | NOT-APPLICABLE | Brain surfaces structured outputs, no UI ownership |
| 36 | Release/distribution | PARTIAL | immutable descriptor valid; current-main version drift |
| 37 | Cross-platform | VERIFIED | Python 3.9/3.12 on Linux/macOS/Windows |
| 38 | Documentation consistency | PARTIAL | path/idempotency/release claims exceed edge behavior |
| 39 | Historical-learning | VERIFIED | repair PR sequence/provenance strong |
| 40 | Inspiration/reference | VERIFIED | research/source map retained |
| 41 | Negative-space | VERIFIED | no scheduler/secret/Skills/Data canonical takeover found |
| 42 | Architecture-vs-operation | PARTIAL | strong overall, three concrete gaps |
| 43 | Current-target readiness | **BLOCKED** | HIGH WSA-009 + MEDIUM WSA-010 |
| 44 | Final seamless-system gap | UNVERIFIED BY DESIGN | A2-A5 |
| 45 | Scope-creep | VERIFIED | H1 retrieval envelope explicitly rejected when unjustified |
| 46 | Definition of done | VERIFIED | complete standalone packet + closure evidence |

## 29. Negative-space checks

Within frozen canonical Brain roots, A1.3 found no evidence that Brain:

- stores plaintext API keys/credential values;
- owns scheduler execution;
- directly writes Skills package bytes;
- directly writes canonical Data or general Memory state;
- treats retrieved content/model output as authority;
- allows workspace policy to weaken operator policy;
- treats proactivity as permission;
- treats budget exhaustion as Goal completion;
- allows model inference alone to pass material Goal criteria;
- silently transfers direction ownership during setup;
- silently reactivates OS strategy when Brain owns direction;
- allows disabled/unregistered native Brain to perform normal writes;
- treats vendor reasoners as action hosts;
- auto-retries uncertain external effects;
- accepts trace IDs as stable effect receipts;
- lets a lower-authority self-evolution tier grant itself broader permissions.

Negative claims are limited to the frozen tracked repository.

## 30. Evidence limitations

- A1.3 does not independently validate OS, Skills, Data, Memory, Gateway or other sibling behavior.
- OS direction workflow uses moving OS main, not immutable OS SHA; A2 must revalidate that seam against frozen exact refs.
- Symlink-parent escape was established from unambiguous path-resolution code and was not executed against real external user data.
- Goal cross-Goal operation-ID race was not patched or test-added because A0-A6 product repos are read-only.
- No production external vendor CLI/network SLO is claimed.
- Release descriptor validates an older immutable accepted beta.2 artifact, not current development main.
- Whole-system release composition remains A5 work.

## 31. Evidence inventory

- `E-A1.3-001`: frozen recursive tree/repository metadata.
- `E-A1.3-002`: README/BRAIN.yaml/pyproject/version/license identity.
- `E-A1.3-003`: protocol and security ownership/authority laws.
- `E-A1.3-004`: storage/scope/object-write implementation.
- `E-A1.3-005`: integration/native path contract and write readiness.
- `E-A1.3-006`: installation/lifecycle/adoption implementation.
- `E-A1.3-007`: direction ownership implementation and tests.
- `E-A1.3-008`: Goal owner implementation.
- `E-A1.3-009`: effective policy and permission intersection.
- `E-A1.3-010`: action replay/receipt implementation.
- `E-A1.3-011`: owner-write routing and learning/Data candidate gates.
- `E-A1.3-012`: bridge/vendor subprocess hardening.
- `E-A1.3-013`: full 26-module test inventory.
- `E-A1.3-014`: exact-head CI run `34969997987`.
- `E-A1.3-015`: exact-head Skills Receipt run `34969998014`.
- `E-A1.3-016`: exact-head OS Direction run `34969997970`.
- `E-A1.3-017`: accepted release descriptor revision `80019be…`.
- `E-A1.3-018`: compare accepted beta.2 ref -> frozen main, 13 commits ahead.
- `E-A1.3-019`: recent PR/repair history.
- `E-A1.3-020`: pre-write live ref/open-PR recheck.

## 32. Standalone verdict

**AI-Verse-Brain at `6f986e8d06c7f9c069fbf05aa92ae7b7a1af9bf4`: AUDIT COMPLETE, DOGFOOD BLOCKED.**

Strong areas:

- unusually explicit canonical ownership;
- deterministic authority hierarchy;
- strong direction handover semantics;
- versioned/idempotent Goal model;
- evidence-gated verification;
- effective-policy tightening;
- independent host permission intersection;
- exact approval binding and late permission recheck;
- durable uncertainty/receipt handling;
- owner-routed sibling writes;
- reasoner-only vendor wrappers;
- strong cross-platform CI and clean artifact smoke.

Current blockers to standalone dogfood acceptance:

1. `WSA-2026-009` HIGH native filesystem containment;
2. `WSA-2026-010` MEDIUM cross-Goal operation-ID concurrency;
3. `WSA-2026-011` LOW package-version identity drift.

No Brain product repair is made during A1.3.

## 33. Progress after audit acceptance

- weighted audit progress: **11 / 100 = 11%**
- weighted remaining: **89%**
- A1 repository audits complete: **3 / 14**
- A1 repository audits remaining: **11 / 14**
- A1 weighted progress: **6 / 28**
- next task: **A1.4 AI-Verse-Memory**

## 34. Task completion record

**Task:** A1.3 AI-Verse-Brain  
**Reviewed repository ref:** `6f986e8d06c7f9c069fbf05aa92ae7b7a1af9bf4`  
**R-a:** COMPLETE / PASS  
**R-b:** COMPLETE / MATERIAL FAILURES FOUND  
**R-c:** COMPLETE / DOGFOOD BLOCKED  
**Contradictions:** `C-A1.3-001`, `C-A1.3-002`, `C-A1.3-003`  
**Findings opened:** `WSA-2026-009`, `WSA-2026-010`, `WSA-2026-011`  
**Inherited findings:** unchanged  
**Standalone verdict:** COMPLETE / DOGFOOD BLOCKED  
**Tracker change:** A1.3 COMPLETE; accepted progress 11/100; A1.4 NEXT  
**Next task:** A1.4 AI-Verse-Memory
