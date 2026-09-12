# AI-Verse Brain Component Specification

**Component:** AI-Verse Brain  
**Repository reviewed:** `aiverse-filmmakers/AI-Verse-Brain`  
**Reviewed branch:** `main`  
**Reviewed head:** `bef8261ad35d126d29aeff5d496f46904125b7b6`  
**Fresh standalone review:** 2026-09-13  
**Evidence rule:** this specification was reconstructed from the Brain repository itself using the canonical AI-Verse forensic audit methodology.

---

## 1. Executive identity

**CURRENT:** AI-Verse Brain is a portable deterministic intelligence-control layer for long-horizon AI agents.

Its job is not merely to "think harder." It gives an agent durable, inspectable machinery for:

- explicit user-authorized intent;
- desired states and definitions of success;
- gap detection;
- opportunity discovery;
- initiative selection;
- bounded objectives;
- progress and stall detection;
- evidence-backed verification;
- derived beliefs with provenance and freshness;
- learning;
- strategy evolution;
- proactive attention;
- controlled external action requests.

The Brain repository expresses its product role as:

```text
Brain  = why / where / what next / how to verify / how to improve
OS     = structure / scope / routing / capabilities / connections / execution boundaries
Memory = historical recall / provenance / supersession
Host   = model and tool execution
```

The central governing principle is:

> The model may reason about what should happen, but deterministic policy decides what may happen and the host proves what did happen.

**LAW:** Brain must not become a second OS, general Memory store, scheduler, connection registry, capability implementation layer, tool runtime, or hidden source of user authority.

**INTENDED:** Brain should become the reusable intelligence layer an existing agent can adopt at any point, whether it runs inside AI-Verse OS, Hermes, Claude Code, Codex, or another compatible host.

---

## 2. What problem Brain solves

A normal agent can answer prompts well but still lacks durable answers to questions such as:

- What does the user actually want over time?
- Which goals are explicit versus inferred?
- What gap exists between current state and desired state?
- Which opportunity is worth attention next?
- How many initiatives can be active safely?
- Is work actually progressing or merely consuming attempts?
- What evidence proves an objective is complete?
- What should be learned from failure?
- Which operating strategies are becoming more reliable?
- When should the agent proactively surface something?
- When should it remain silent?
- What may the model propose but not authorize?
- What happens if a side effect may have occurred but no confirmation returned?

Brain turns those concerns into persistent typed objects, deterministic state machines, policies, evidence gates and host contracts.

---

## 3. Architectural thesis

Brain is built around the architecture:

```text
intent
  ↓
current-state comparison
  ↓
gap
  ↓
opportunity
  ↓
initiative
  ↓
objective
  ↓
action / observation
  ↓
progress or stall
  ↓
verification
  ↓
learning
  ↓
strategy evolution
```

But this is not one monolithic loop.

The repository deliberately separates three timescales.

### Direction Loop

```text
current state
→ desired state
→ gap
→ opportunity
→ initiative
→ priority
```

### Action Loop

```text
objective
→ completion contract
→ plan
→ act
→ observe
→ progress / stall
→ verify
→ close / replan / block
```

### Learning / Evolution Loop

```text
experience
→ evidence
→ reflection
→ candidate learning
→ evaluation
→ strategy candidate
→ promote / reject
→ monitor / rollback
```

**LAW:** these loops must not collapse into one giant prompt.

---

## 4. Five Brain functions

The research phase identified five distinct intelligence functions hidden behind the word "brain":

1. **Intent** - what ultimately matters.
2. **Cognition** - how much and what kind of reasoning is warranted.
3. **Initiative** - what useful work should be noticed or proposed without waiting for a direct user command.
4. **Learning** - what worked, failed, or should change.
5. **Evolution** - which strategies or methods should improve over time.

The implementation preserves these distinctions through separate object types and deterministic services.

---

## 5. Brain-owned canonical state

Brain canonically owns the following object families when authorized for the relevant scope:

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
- Brain policy.

These are not generic OS data. They are Brain's own intelligence/control objects.

### Native AI-Verse mode

```text
operator/brain/
workspaces/<id>/brain/
```

### Standalone mode

```text
.ai-verse-brain/
```

Brain runtime state is separate and disposable.

---

## 6. Explicit non-ownership

Brain must route or read rather than duplicate:

- workspace identity;
- OS current context;
- the operator profile as a whole;
- general historical memory;
- reusable domain knowledge;
- connections;
- credentials;
- capability implementation;
- scheduler implementation;
- external side-effect execution;
- vendor model/runtime state.

The write-classification vocabulary explicitly routes these concepts:

```text
stable identity / preference -> OS profile
current state                -> OS context
settled decision             -> OS decisions
historical event             -> Memory history
reusable knowledge           -> OS knowledge
repeatable execution         -> capability candidate
Brain intelligence state     -> Brain
transient thought            -> no durable write
```

**LAW:** classification does not transfer canonical ownership to Brain.

---

## 7. Critical write-routing limitation

The Brain repository contains a symbolic write router and a host interface operation named `write_route`.

However, in the current reviewed implementation, the cognition/learning pipeline does **not** provide a general end-to-end dispatcher that takes arbitrary routed classifications and causes OS/Memory/capability-owned canonical writes.

Therefore:

```text
Brain can identify the correct canonical destination
!=
Brain currently performs every cross-component canonical write
```

This is important because the Phase 3 research specification expected OS write routing and Memory write integration as part of the day-one functional slice.

**GAP:** the complete cross-component durable-write path remains unfinished at system level.

The future path should use owner-controlled host/component write boundaries rather than giving Brain direct access to sibling canonical files or databases.

---

## 8. Scope model

Current canonical scopes are:

```text
operator
workspace:<workspace-id>
```

Brain's workspace ID grammar is aligned with current AI-Verse OS workspace IDs.

### Standalone scope

Standalone core v0.1 supports operator scope directly.

Richer standalone/project scope mapping belongs in adapters rather than hardcoding a second workspace architecture into Brain.

**LAW:** Brain does not invent competing host scope semantics.

---

## 9. Storage and revision model

Brain stores each canonical object as inspectable JSON.

Every object includes:

- ID;
- kind;
- scope;
- lifecycle status;
- revision;
- timestamps;
- creator/updater;
- source references;
- evidence references;
- supersession fields;
- typed payload.

Writes use:

- path-safe IDs;
- atomic temporary-file replacement;
- optimistic revision checks;
- per-object runtime locks;
- scope/kind immutability.

This gives Brain inspectable local state without relying on an opaque database.

---

## 10. Runtime state

Disposable runtime state includes:

- object locks;
- direction coordination locks;
- trigger receipts;
- attention delivery/cooldown state;
- temporary coordination ledgers.

Runtime state must never become the only copy of:

- confirmed intent;
- initiative acceptance;
- objective completion;
- dismissal/rejection;
- learning;
- policy;
- durable side-effect reconciliation references.

**LAW:** deleting runtime may reduce convenience, but must not erase canonical intelligence state.

---

## 11. Authority hierarchy

The Brain protocol describes an operational authority hierarchy roughly as:

```text
host hard constraint
explicit user intent
canonical scoped state
verified evidence
confirmed derived model
validated strategy
temporary hypothesis
external data
```

This hierarchy is enforced in multiple places.

### User intent

Model output cannot silently create confirmed user goals, boundaries or success definitions.

### External data

External content cannot directly drive privileged Brain lifecycle transitions.

### Derived beliefs

A hypothesis about the user remains a derived belief, not an automatic user goal.

### Strategy

A learned strategy may improve method but cannot grant itself new user authority.

---

## 12. Intent and practices

Brain distinguishes finite direction from ongoing standards.

### Intent subtypes

Current intent includes:

- desired state;
- goal;
- boundary;
- constraint;
- success definition.

### Practice

Practices represent ongoing desired conditions, not one-time outcomes.

Examples:

- review initiatives weekly;
- preserve a standard;
- maintain a recurring habit/process.

This distinction came directly from research into systems that incorrectly collapse recurring standards into terminal goals.

---

## 13. Explicit onboarding

Brain onboarding is adaptive and dry-run-first.

Current command:

```bash
ai-verse-brain onboard <root>
```

Required minimum Brain-owned direction when Brain is the strategic owner:

- desired state;
- definition of success.

Optional:

- goals;
- boundaries;
- constraints;
- practices.

Apply explicitly:

```bash
ai-verse-brain onboard <root> --answers answers.json --apply
```

### Native ownership behavior

When AI-Verse OS owns strategic direction for a scope, Brain onboarding refuses to create a parallel strategic store.

It instead tells the operator to use explicit direction handover.

This is a strong ownership property.

---

## 14. Direction ownership with AI-Verse OS

Brain uses a per-scope one-owner model.

A native scope is owned by:

```text
os
or
brain
```

Brain installation does not steal strategic ownership.

### Handover to Brain

Current command:

```bash
ai-verse-brain direction-owner <root>   --scope <scope>   --handover-to-brain
```

Apply requires explicit confirmation:

```bash
ai-verse-brain direction-owner <root>   --scope <scope>   --handover-to-brain   --apply   --confirm-import
```

The handover can import supported OS strategic material with:

- source path;
- SHA-256 provenance;
- explicit import confirmation.

### Handback to OS

Brain can return strategic authority:

```bash
ai-verse-brain direction-owner <root>   --scope <scope>   --handover-to-os
```

Apply:

```bash
ai-verse-brain direction-owner <root>   --scope <scope>   --handover-to-os   --apply   --confirm-export
```

Active Brain direction is exported into the bounded OS strategic section, operational current-state sections are preserved, then the ownership marker flips.

### Crash safety

The ownership registry has:

- per-scope handover locks;
- a shared registry-wide lock;
- atomic updates;
- interrupted-handover recovery.

**LAW:** ownership flips only after the appropriate state/export transaction has reached the safe boundary.

---

## 15. Frozen strategy read boundary

When Brain owns strategy in native OS mode, the built-in read-only host delegates current-context retrieval to the OS ownership-aware resolver.

It does not read raw `CURRENT.md` as fallback.

If the resolver is:

- missing;
- malformed;
- returns wrong scope;
- times out;

Brain fails closed.

A user-supplied `--context-file` cannot bypass the OS resolver in native mode.

Standalone mode keeps explicit local context-file support.

**LAW:** read paths must honor strategic ownership just as write paths do.

---

## 16. Direction: gaps, opportunities and initiatives

### Gap

A gap is a Brain-owned interpretation linking:

- desired-state references;
- current-state references.

It is not current-state truth.

### Opportunity

An opportunity is a hypothesis about how a gap might be reduced.

Before qualification Brain checks:

- desired-state linkage;
- scope;
- permission compatibility;
- duplicate state;
- evidence freshness;
- minimum confidence;
- cooldown;
- hard boundaries.

### Initiative

An initiative must descend from a qualified opportunity.

Its ranking inputs cannot silently inflate during promotion.

### Dedupe and cooldown

Brain uses deterministic fingerprints and runtime locks to prevent duplicate opportunity/initiative promotion.

Dismissed/rejected items create cooldowns so rephrasing does not immediately resurrect stale work.

---

## 17. Attention economy

Brain treats user attention as a finite resource.

Current notification classes:

- INTERRUPT;
- SURFACE;
- BATCH;
- STORE;
- DROP.

Proactivity levels:

- P0 reactive;
- P1 observant;
- P2 advisory;
- P3 assistive;
- P4 delegated.

Current policy includes limits for:

- active initiatives;
- proactive items per session;
- interruptions per day;
- cooldown windows.

**LAW:** higher proactivity never grants new side-effect authority.

**LAW:** silence can be the correct intelligent action.

---

## 18. Objectives and progress

Objectives are bounded outcomes with explicit completion criteria.

Brain distinguishes:

- lifecycle status;
- progress interpretation.

Progress states include:

- progressing;
- waiting;
- blocked;
- stalled;
- wrong_strategy;
- invalidated;
- complete_unverified;
- verified_complete.

### Attempt semantics

- first observation establishes baseline;
- repeated same state is not progress;
- changed state without evidence is not meaningful progress;
- changed state plus evidence may reset non-progress count;
- blockers change state;
- attempt budget exhaustion blocks instead of self-expanding;
- repeated non-progress produces stalled state.

**LAW:** unfinished is not the same as progressing.

---

## 19. Verification

Brain implements V0-V3 verification.

### V0

Trivial/low-consequence work.

### V1

Normal material work with evidence.

### V2

Important work requiring stronger evidence and fresh-context evaluation.

### V3

High-impact work requiring independent model/evaluator or authoritative external verification.

Material criteria start `unverified`.

Model inference alone cannot pass V1+ criteria.

V2/V3 require stronger evidence.

A successful action is not sufficient to close an objective.

---

## 20. Skills receipt verification

Brain has a dedicated consumer for AI-Verse Skills execution receipt v2.

It requires exact binding to:

- Brain request fingerprint;
- scope;
- action class;
- operation;
- Skills provider identity;
- capability ID;
- immutable generation ID;
- package digest.

It treats `trace_id` only as correlation metadata.

A Skills runtime cannot self-label its observation as authoritative proof.

For successful external effects, Brain requires trusted OS effect provenance.

Objective completion remains Brain-owned through its evaluator.

**LAW:** execution success and objective verification are separate decisions.

---

## 21. Evidence and provenance

Brain evidence references support:

- evidence class;
- claim;
- observed time;
- expiry;
- scope;
- integrity;
- source kind;
- source reference;
- evaluation independence.

Current evidence classes include:

- USER_CONFIRMATION;
- CANONICAL_STATE;
- DIRECT_MEASUREMENT;
- AUTHORITATIVE_EXTERNAL;
- INDEPENDENT_EVALUATION;
- CORROBORATED_HISTORY;
- SINGLE_OBSERVATION;
- MODEL_INFERENCE.

This allows verification quality to be derived from provenance rather than a model simply asserting that evidence is "strong."

---

## 22. Derived model beliefs

Brain supports derived beliefs about:

- user model;
- agent model;
- world model.

Beliefs contain:

- epistemic state;
- confidence;
- evidence;
- observation time;
- expiry/max-age;
- contradiction references.

A belief can become stale or contradicted.

Refreshing a contradicted belief requires verified evidence or stronger authority.

**LAW:** personalization must not silently mutate explicit user intent.

---

## 23. Learning

Learning has a staged lifecycle.

Typical progression:

```text
OBSERVATION
→ HYPOTHESIS
→ PATTERN
→ REFLECTION
→ VALIDATED_LEARNING
→ STRATEGY_CANDIDATE
→ PROMOTED / REJECTED
```

Promotion requires increasing evidence.

External data cannot directly drive learning lifecycle authority.

User confirmation and independent evaluation are distinguished.

---


## 24. Strategy evolution

Brain implements controlled strategy-rule evolution rather than unrestricted self-modifying software.

Evolution tiers:

### E0

Ephemeral tactic. Not canonical strategy promotion.

### E1

User-local strategy rule. Requires evaluation and regression evidence. Policy may allow bounded auto-promotion.

### E2

Broader durable strategy. Requires stronger evaluation and, by default, explicit user approval.

### E3

Shipped/core Brain behavior. Cannot be activated by runtime Brain state. Requires tested code/PR promotion.

### E4

Privileged authority/safety/permission policy. Cannot be self-promoted by runtime strategy machinery.

**LAW:** self-improvement may improve method, but cannot silently rewrite user sovereignty or core authority.

### Current rollback reality

**CURRENT:** the strategy state machine permits `ACTIVE -> RETIRED` and `ACTIVE -> ROLLED_BACK`, and active strategy rules can accumulate helpful/harmful outcome evidence.

**GAP:** this is not yet a true restoration mechanism.

Current code does not provide a strategy rollback service that restores a prior strategy revision, reconstructs the previous known-good rule, or switches an active pointer back to that prior rule. New strategy candidates initialize `previous_revision_ref` to `None`, and the reviewed learning service does not populate or consume a revision chain. There is also no dedicated rollback CLI.

Therefore:

```text
mark strategy as ROLLED_BACK
!=
restore the previous known-good strategy
```

This matters because the current Brain protocol requires promotion through a permitted rollback path, and the current learning/evolution protocol treats rollback as part of controlled self-improvement.

### Product-language clarification

The current implementation genuinely supports:

- learning;
- strategy candidates;
- evidence-backed strategy promotion;
- strategy outcome measurement;
- retirement;
- a terminal `ROLLED_BACK` state.

It does **not** yet implement version-restoring strategy rollback, nor does it autonomously rewrite Brain source code, vendor model weights, external skills, or privileged policy.

"Controlled self-improvement" should therefore be understood as controlled strategy evolution with a still-incomplete restoration path.

## 25. Cognition runtime pipeline

The runtime pipeline is:

```text
trigger
→ deterministic orientation
→ bounded ephemeral context
→ reasoner
→ strict proposal parser
→ deterministic proposal application
→ attention decision
→ surface item
```

External action execution is outside this automatic pipeline.

### ORIENT

Explicit orientation can remain deterministic and spend zero model calls.

### Model proposals

Models may return proposal kinds and bounded payloads.

They cannot define:

- authoritative scope;
- policy;
- permission;
- lifecycle status;
- privileged self-evolution fields;
- side effects.

The runtime binds control fields itself.

---

## 26. Reasoner adapters

Brain is model-vendor neutral.

The stable transport is:

```text
ai-verse-brain-bridge/1.0
```

Current built-in reasoner-only wrappers:

- Claude Code;
- Codex CLI;
- Hermes Agent.

These advertise only `reason`.

They do not become action hosts.

### Bridge security

The JSON subprocess bridge:

- uses argv with `shell=False`;
- bounds stdin/stdout/stderr;
- enforces timeout;
- kills over-budget processes;
- validates protocol and request IDs;
- rejects malformed/duplicate-key JSON;
- filters environment;
- stores environment variable names, not secret values;
- rejects credential-bearing command flags.

---

## 27. Vendor runtime portability

### Claude Code

Reasoner-only plan-mode invocation.

### Codex CLI

Ephemeral, read-only sandbox style invocation.

### Hermes Agent

One-shot, safe-mode, safe-toolset reasoning invocation.

These wrappers are treated as moving external dependencies.

Release documentation requires their CLI flags to be revalidated before tagging.

**LAW:** vendor wrappers may evolve without changing Brain canonical state or authority contracts.

---

## 28. Host adapters

A real execution host selected for `run-tick` must advertise:

- read_context;
- retrieve_history;
- list_capabilities;
- list_connections.

Optional host operations include:

- query_data;
- authorize_action;
- request_action;
- request_evaluation;
- schedule_trigger;
- cancel_trigger;
- notify_user;
- write_route.

Brain never infers missing host operations.

Requested real host failure does not silently downgrade to the read-only fallback.

---

## 29. Meaningful retrieval

Brain owns retrieval intent.

Hosts own access.

### History

Brain creates task-specific semantic history queries based on:

- cognition purpose;
- current host context;
- relevant Brain state.

It does not send internal enum labels such as `gap_analysis` as if they were meaningful recall queries.

### Capabilities

Brain asks the host for a bounded candidate set, validates it, ranks it for the current task, then applies the reasoning-context limit.

Provider order is not relevance.

An over-budget candidate set fails closed rather than silently truncating relevant tail entries.

---

## 30. Current-state / historical-state boundary

Brain treats host current context as ephemeral data.

Historical evidence comes from host/Memory retrieval when useful.

Brain does not copy current OS context or general Memory history into competing Brain canonical stores simply because a model consumed it.

This is one of the most important anti-duplication laws.

---

## 31. Action boundary

Brain maintains a strict separation:

```text
"I should do X"
!=
"X is authorized"
!=
"X was dispatched"
!=
"X happened"
!=
"X satisfied the objective"
```

An `ActionRequest` binds:

- action class;
- scope;
- operation;
- immutable parameters;
- idempotency key;
- budget/scope/reversibility facts;
- reason;
- request fingerprint.

A model proposal cannot implicitly become an ActionRequest.

---

## 32. Approval binding

Explicit approval is bound to the exact immutable action.

The implementation protects against:

- changed recipient;
- changed amount;
- changed body;
- changed target;
- changed operation;
- expired grants;
- unrelated grants;
- nested parameter mutation;
- time-of-check/time-of-use mutation.

Legacy/unbound approvals fail closed.

**LAW:** user approval is not a vague reusable permission token.

---

## 33. Brain + host permission intersection

Brain policy alone is not sufficient authority for an external host effect.

The host must provide an exact bound permission decision.

Rules:

```text
Brain deny + host allow                = deny
Brain allow + host deny                = deny
Brain allow + host approval_required   = approval required
Brain approval_required + host allow   = approval required
both allow                             = potentially allowed after all other gates
```

The host cannot manufacture Brain's user ApprovalGrant.

Host permission is rechecked immediately before external dispatch.

Late revocation results in no external effect.

---

## 34. Side-effect replay safety

Every action uses an idempotency key.

Reusing the same key for different contents is rejected.

External side effects produce durable minimal receipt references under Brain state.

Uncertain outcomes are not automatically retried.

A failed action becomes safely retryable only when evidence proves no effect occurred or the host supports safe idempotency.

This implements the repository's stated preference:

> duplicated thinking is better than duplicated side effects.

---

## 35. Trigger and cadence model

Brain owns when cognition would be useful.

It deliberately does **not** own a scheduler.

Current trigger semantics include:

- explicit;
- session start;
- session end;
- scheduled orientation;
- scheduled review;
- event;
- objective wake;
- blocker resolution;
- external change;
- manual recovery.

Brain can emit:

```bash
ai-verse-brain plan-cadence ...
ai-verse-brain cadence-hooks ...
```

A host scheduler decides how to install/execute those hooks.

**LAW:** model cognition must not own deterministic scheduler bookkeeping.

---

## 36. Trigger replay

Trigger claims are idempotent runtime coordination.

A tick claims the trigger before the bounded cognition/application pass and marks it complete afterward.

A process crash leaves a claimed state.

Stale claim recovery is explicit.

Brain does not guess that a partially executed cognition pass is safe to replay.

---

## 37. Installation modes

### Standalone

Brain state:

```text
.ai-verse-brain/
```

### Native AI-Verse OS v2

Brain state:

```text
operator/brain/
workspaces/<id>/brain/
runtime/ai-verse-brain/
```

If `AI-VERSE.yaml` exists but is incompatible, Brain refuses standalone fallback.

**LAW:** an incompatible host must not cause a hidden parallel Brain store.

---

## 38. Package installation

Python 3.9+.

Current README recommends:

```bash
python -m pip install   "git+https://github.com/aiverse-filmmakers/AI-Verse-Brain.git@v0.1.0-beta.1"
```

or pipx.

The package defines:

- `ai-verse-brain`
- `ai-verse-brain-vendor-bridge`

---

## 39. Critical release-tag mismatch

This fresh audit compared current `main` with the README's recommended `v0.1.0-beta.1` tag.

The recommended beta tag does **not** contain the current hardening now described by the main README.

At `v0.1.0-beta.1`:

- `extension_registry.py` is absent;
- no `attach` CLI;
- no `disable` CLI;
- no `detach` CLI;
- no `direction-owner` CLI;
- native integration still reflects the older tracked-manifest generation.

Current `main` contains the later September 10-12 safety and lifecycle hardening.

Yet current package/version metadata still reports `0.1.0-beta.1`.

**GAP:** the documented immutable install artifact does not represent the current hardened product described by main.

This is one of the most important current release defects.

The next member release should cut a new immutable version/tag containing the current lifecycle/direction/permission/receipt hardening and update the install documentation accordingly.

---

## 40. Brain initialization

`init` is dry-run-first.

Plan:

```bash
ai-verse-brain init <root>
```

Apply:

```bash
ai-verse-brain init <root> --apply
```

### Native current behavior

On a clean compatible OS v2 host, current main can:

1. attach Brain in the local extension registry if absent;
2. create Brain-owned state;
3. create installation marker;
4. preserve tracked OS files.

This is newer than some stale protocol/CI material.

Initialization is idempotent.

---

## 41. Local attachment lifecycle

Current native commands:

```bash
ai-verse-brain attach <root>
ai-verse-brain attach <root> --apply

ai-verse-brain disable <root>
ai-verse-brain disable <root> --apply

ai-verse-brain detach <root>
ai-verse-brain detach <root> --apply
```

Attachment uses:

```text
.aiverse/extensions/registry.json
```

Brain mutates only its own entry.

Registry changes use:

- exclusive lock;
- atomic write;
- compare against expected original bytes;
- sibling/unknown field preservation.

Disable/detach preserve canonical Brain state.

Both are blocked while Brain owns strategic direction for any scope.

---

## 42. Missing enable command

The lifecycle is currently asymmetric.

There is a supported CLI command to disable Brain, but there is **no CLI `enable` command**.

An internal API exists:

```python
set_brain_enabled(root, True)
```

but the public CLI does not expose it.

Rerunning `attach --apply` does not solve this because attachment preserves the existing `enabled` field when an entry already exists.

Therefore:

```text
attach -> disable -> re-enable
```

cannot currently be completed through the documented Brain CLI.

**GAP:** add an explicit idempotent `enable <root> --apply` lifecycle path or equivalent supported operation.

This is a concrete present-stage product defect.

---


## 43. Detach, reinstall and cross-mode adoption

### Native detach

Detach removes local OS registration but preserves Brain canonical state.

When Brain owns strategic direction, detach is blocked until explicit handback to OS completes. After handback, detach is safe and state remains available for later reattachment.

### Same-mode reinstall / reattach

Initialization is idempotent and preserves the existing installation ID and canonical state.

After a real detach, reattachment can recreate the local registry entry.

### Disabled-state limitation

If Brain is disabled rather than detached, the missing public `enable` command blocks clean CLI recovery. Re-running `attach --apply` preserves the existing `enabled: false` value.

### Standalone-first, OS-later limitation

**GAP:** install-order independence is not complete across storage modes.

If Brain was initialized standalone under `.ai-verse-brain/` and that same root later becomes a compatible AI-Verse OS host, native initialization deliberately blocks because the standalone store exists:

```text
parallel standalone .ai-verse-brain store exists inside native AI-Verse host
```

That fail-closed behavior correctly prevents competing truth, but there is no supported migration/adoption transaction that moves or imports the standalone Brain canonical state into native Brain state.

So:

```text
OS first -> Brain later
```

is supported well, while:

```text
Brain first -> OS later
```

requires a missing cross-mode state adoption path.

### Package uninstall

Package removal remains owned by pip/pipx or the environment package manager. Brain has no package-uninstall orchestrator. Canonical state is not intentionally deleted by detach.


## 44. Migration

Current command:

```bash
ai-verse-brain migrate <root>
ai-verse-brain migrate <root> --apply
```

The implementation is conservative.

It can currently:

- inspect installation/state schema;
- block newer incompatible state;
- block unknown older state;
- refresh package-version metadata when state schema is unchanged.

### State-schema limitation

There is no registered state-schema conversion path in the current implementation.

If Brain state schema is older than current, migration reports that no registered migration path exists and fails closed.

That is safer than guessing, but it means the migration framework is present while historical state transformation is not yet implemented.

### Cross-mode limitation

The migration command does not migrate a standalone `.ai-verse-brain/` installation into native AI-Verse Brain state.

This is the missing half of the Brain-first -> OS-later lifecycle described above.

### Old-agent/history migration

Brain also does not provide a general importer for an existing agent's entire historical memory.

That is correct ownership-wise because general history belongs to Memory/host.

What Brain may need is deliberate import of:

- explicit strategic goals;
- desired states;
- constraints;
- practices;
- selected strategy state.

Native OS direction handover already provides one narrow strategic import path with provenance.

**GAP:** define both an ownership-safe strategic-intent import path for existing agents and a canonical cross-mode adoption path for standalone Brain state when a compatible host is introduced later.


## 45. Doctor

Current command:

```bash
ai-verse-brain doctor <root>
```

Doctor is read-only.

It checks structural Brain concerns including:

- host mode/compatibility;
- local attachment state;
- parallel-store risk;
- installation marker;
- state schema;
- scoped Brain object integrity;
- cross-scope leakage;
- minimum onboarding readiness.

### Health depth

Under the system health-depth vocabulary, current Brain doctor is primarily:

```text
STRUCTURAL
+ partial ATTACHMENT
```

It is not a RUNTIME, DEPENDENCY, OPERATIONAL or SYSTEM health proof.

This distinction is important because `DoctorReport.ok` means no check reached `FAIL`. A clean compatible native host with no Brain attachment can still return `ok=true` with a `WARN` for attachment.

Doctor does not prove:

- vendor CLI works;
- real host adapter works;
- real Memory retrieval works;
- optional Data is reachable or used;
- scheduler hooks are installed;
- external action path works;
- a representative cognition tick succeeds;
- full AI-Verse composition is healthy.

Vendor and adapter doctors cover some dependency checks separately.

**LAW:** Brain doctor PASS/OK must never be presented as full operational or system readiness.

## 46. Adapter doctor and vendor doctor

```bash
ai-verse-brain adapter-doctor <config>
ai-verse-brain vendor-doctor claude <root>
ai-verse-brain vendor-doctor codex <root>
ai-verse-brain vendor-doctor hermes <root>
```

These provide explicit dependency/transport checks.

A successful vendor handshake proves reachability and bridge compatibility.

It does not grant action authority.

---

## 47. Running Brain

Example current tick:

```bash
ai-verse-brain run-tick <root>   --vendor claude   --host-adapter <host-config>   --trigger explicit
```

or explicitly limited:

```bash
ai-verse-brain run-tick <root>   --vendor claude   --read-only-context   --trigger explicit
```

The host selection must be explicit.

Brain never silently replaces a requested real host with read-only mode.

---

## 48. Agent adoption limitation

Brain can already run Claude, Codex and Hermes as **reasoners inside Brain ticks**.

That is not the same as installing Brain into those agents' normal lifecycle.

There is currently no universal command equivalent to:

```text
activate brain in this existing Hermes agent
activate brain in this existing Codex agent
make this Claude runtime use Brain as its durable intelligence layer
```

without the operator manually understanding:

- host adapter;
- invocation;
- cadence hooks;
- strategic ownership;
- onboarding.

**GAP:** Brain needs a productized agent-adoption/setup sequence if the system target is "install Brain at any time and the existing agent takes it on board."

That activation flow must remain separate from strategic ownership transfer. Attaching Brain does not automatically mean handing it user direction.

---

## 49. Host selection

Current `run-tick` intentionally refuses implicit host selection.

A real host adapter is checked before reasoning begins.

Required host read operations:

- current context;
- history;
- capabilities;
- connections.

This prevents an agent from appearing integrated while silently running against a weaker fallback.

---

## 50. AI-Verse OS native integration

Current main supports:

- local extension registry;
- Brain-native state paths;
- OS ownership-aware current context;
- explicit direction handover/handback;
- OS permission intersection;
- dynamic OS host adapter;
- optional Memory;
- external Skills capabilities;
- Connections metadata;
- optional read-only Data query.

Brain does not need the Skills source repository at runtime.

Brain does not open Data storage directly.

---

## 51. Memory relationship

Brain owns **why/what next**, not long-term historical storage.

Brain asks the selected host for semantic history retrieval.

An AI-Verse Memory-backed host can satisfy that query.

Brain uses history as evidence/context.

It does not copy the result into a competing Brain Memory store.

### Current missing write integration

Brain classifies historical events as Memory-owned but does not provide a general automatic Memory write dispatcher in the current reviewed pipeline.

This should be solved through a supported owner-controlled write boundary rather than direct Memory storage access.

---

## 52. Skills relationship

Brain may reason over capability metadata returned by the host.

When execution is performed via Skills:

- immutable capability generation is bound;
- package digest is bound;
- action outcome is translated conservatively;
- objective verification remains separate.

Brain does not own Skills installation or package implementation.

---


## 53. Data relationship

The host protocol and bridge expose an optional `query_data` operation.

That is a useful integration boundary because it lets a host keep Data ownership outside Brain.

### Current operational reality

**GAP:** normal Brain cognition does not currently consume that operation.

The reviewed `ContextAssembler` builds cognition context from:

- `read_context`;
- `retrieve_history`;
- `list_capabilities`;
- `list_connections`;
- Brain-owned canonical state.

It does not call `query_data`, and `ContextBundle` has no Data result field.

Likewise, real host selection currently requires the four read operations above, not `query_data`.

Therefore:

```text
Data bridge operation exists = CURRENT contract surface
normal tick automatically queries Data = not implemented
```

README wording that attached Data can expose read-only structured queries should be interpreted as host capability exposure, not proof that current cognition automatically uses those queries.

**INTENDED:** if Data is meant to influence normal Brain reasoning, add an explicit, bounded, purpose-aware Data retrieval path and acceptance tests. Brain must continue treating Data output as evidence/data, not canonical Brain truth.

## 54. Scheduler relationship

Brain deliberately does not install cron jobs, daemons or scheduler state.

It emits scheduler requests/hooks.

The host/runtime owns actual scheduling.

This means "proactive Brain" depends on a cadence owner outside Brain for persistent background operation.

**SYSTEM GAP:** the overall AI-Verse family still needs an explicit final answer for which component/runtime owns universal cadence execution.

---


## 55. Release and cross-platform behavior

### Current-main CI

At reviewed head `bef8261ad35d126d29aeff5d496f46904125b7b6`, all three current workflows were verified green:

- `CI`, run `34710865210`;
- `OS Direction Ownership Contract`, run `34710865217`;
- `Skills Receipt Contract`, run `34710865215`.

The main CI run contains seven successful jobs:

- Ubuntu Python 3.9;
- Ubuntu Python 3.12;
- macOS Python 3.9;
- macOS Python 3.12;
- Windows Python 3.9;
- Windows Python 3.12;
- package-smoke.

The repository contains 20 unittest modules with 198 discovered `test_*` methods in the reviewed tree.

### Package smoke

Package smoke:

- builds a wheel;
- installs into a clean venv;
- invokes the installed CLI;
- initializes fresh standalone state;
- runs doctor/migration;
- verifies the installation marker.

This is strong source-head packaging evidence.

### Limits of that evidence

- package smoke runs on one CI platform, not all three;
- CI builds and installs from the current source head, not from the documented immutable beta tag;
- live Claude/Codex/Hermes installations are not exercised by this matrix;
- there is no GitHub Release object for the reviewed repository;
- the documented tag remains older than current hardening.

So current-main code is well tested cross-platform, while current immutable member distribution is not equivalent to current main.

## 56. Cross-repository acceptance

Brain contains separate workflows for:

- OS direction ownership;
- Skills receipt contract.

These prove important architecture boundaries with real sibling repositories.

### Current acceptance drift

The OS direction workflow still contains a test-only step that patches tracked `AI-VERSE.yaml` to add an old `extensions.brain` manifest registration before initialization.

Current Brain main no longer requires that pattern and explicitly treats tracked manifest registration as legacy.

Therefore the direction workflow does not currently prove the **exact current clean member path**.

**GAP:** update the workflow to use stock current OS + Brain's local registry attachment/init path with no tracked manifest patch.

---


## 57. Documentation drift

Fresh review found several current contradictions.

### Stale installation protocol

`protocol/INSTALLATION-ONBOARDING.md` still says native initialization requires an existing `extensions.brain` registration slot and fails when absent.

Current main auto-attaches through the local extension registry.

### Invalid current run-tick examples

`docs/INSTALLATION.md` shows `run-tick` examples without either `--host-adapter` or `--read-only-context`.

`docs/VENDOR-REASONERS.md` does the same for Claude, Codex and Hermes examples.

Current CLI parsing requires exactly one explicit host mode. Those documented commands therefore do not represent the current executable interface.

The README is newer and shows the explicit host-selection model correctly.

### Security installation wording

`SECURITY.md` still says native initialization requires the host's existing Brain extension contract. Current clean OS initialization can create the local Brain attachment itself.

The rule that tracked OS configuration must not be patched remains correct, but the registration wording is stale.

### Stale research status

`research/README.md` still says that no production Brain engine has been implemented.

That was true before Phase 4 and should now be marked historical or rewritten.

### Release-history drift

`CHANGELOG.md` and the beta release material describe the beta.1 generation but do not capture the substantial post-beta hardening now present on main.

### Acceptance drift

The OS direction workflow still injects the old tracked-manifest Brain slot in its test checkout before running current Brain initialization.

That setup is historical scaffolding, not the supported member path.


## 58. Security posture

Current security strengths include:

- model and retrieved content treated as untrusted data;
- exact approval binding to immutable action fingerprints;
- restrictive Brain + host permission intersection;
- permission recheck at the dispatch edge;
- durable side-effect receipts and fail-closed uncertainty;
- shell-free subprocess execution;
- bounded bridge input/output and timeouts;
- environment allowlisting;
- credential-bearing command-flag rejection;
- path-safe IDs and resolved containment checks;
- local extension-registry symlink rejection;
- scope isolation;
- fail-closed malformed/incompatible host state.

### Secret-material persistence limitation

**LAW in prose:** current security/protocol documents say Brain must not store secret or credential material.

**CURRENT implementation:** the bridge and adapter configuration paths contain real controls against accidentally embedding credential material in commands/configuration.

**GAP:** there is no generic secret-value detector at the canonical Brain object write boundary.

Brain object validation controls kinds, statuses, authority, IDs and typed payload structure, but arbitrary text fields are not generically screened for secret-like material before persistence.

Therefore the no-secrets rule is currently partly an operator/protocol obligation rather than a universal executable guarantee.

The mature contract should either add a deterministic rejection/redaction boundary appropriate to Brain-owned payloads, or narrow the documentation claim so it precisely matches the enforcement that exists.

## 59. Concurrency

Current concurrency mechanisms include:

- object revision checks;
- per-object locks;
- direction proposal locks;
- shared direction ownership registry lock;
- trigger claim receipts;
- local extension registry lock.

The September 10 repair specifically fixed cross-scope ownership handover races.

**LAW:** shared registries require serialization at the registry level, not only per-scope locks.

---

## 60. Failure semantics

The repository consistently prefers explicit failure over silent fallback.

Examples:

- incompatible OS -> no standalone Brain;
- requested real host fails -> no read-only downgrade;
- stale/malformed permission -> deny;
- unsupported migration -> stop;
- capability overflow -> stop;
- unknown external effect -> no blind retry;
- wrong scope -> reject;
- stale generation receipt -> reject;
- missing strong verification -> objective remains unverified.

This consistency is a major architectural strength.

---

## 61. Research lineage and curation

Brain is explicitly a curated synthesis.

### LifeOS

Adopted:

- Current State -> Ideal State;
- durable directional model;
- explicit success/verification;
- persistent goal orientation.

Rejected/modified:

- rigid universal fixed algorithm;
- duplicate canonical goal stores;
- domain-specific root ontology.

### Hermes Agent

Adopted:

- bounded persistent execution goals;
- completion contracts;
- separate evaluation;
- background reflection;
- candidate persistence.

Modified:

- execution goals are separated from long-horizon intent.

### AIS-OS / Three Ms / Four Cs

Adopted as:

- gap/intervention design;
- execution-readiness lenses.

Rejected as:

- the complete Brain architecture.

### Letta

Adopted:

- persistent agent state;
- mutable strategy distinct from historical experience;
- inspectable evolution.

Constraint added:

- evolving agent identity/strategy never outranks user intent.

### OpenClaw

Adopted:

- scheduler bookkeeping outside LLM;
- heartbeat/ambient-awareness distinction;
- stale-task resurrection prevention;
- explicit proactivity architecture.

### ACE

Adopted:

- incremental strategy/playbook evolution;
- stable strategy identities;
- evidence for helpful/harmful rules;
- avoid monolithic prompt rewrite.

### Hermes Self-Evolution

Adopted:

- candidate improvement;
- evaluation;
- regression;
- review/promotion;
- rollback.

Safety restriction:

- no privileged intent optimization.

### GEPA

Adopted:

- trajectory-based textual feedback;
- multi-objective improvement concept.

Restricted:

- cannot optimize user goals/permissions/privacy.

### Voyager

Adopted:

- curriculum-like initiative discovery;
- competence/opportunity frontier.

Restricted:

- must serve approved direction.

### Generative Agents and Reflexion

Adopted:

- reflection from experience;
- reflection informs future action.

Restricted:

- reflection remains inference until evidence/validation.

### PersonalOS

Adopted:

- capacity-aware portfolio management;
- limits/WIP;
- current action connected to long-term goals.

### Pascal Jarvis

Adopted:

- proactive intent state machine;
- attention scarcity;
- notification != completion;
- receipts and bounded retries.

### DeerFlow

Adopted:

- classify before persistence;
- scope/durability/authority before writeback.

### Honcho

Adopted:

- derived user model as perspective/hypothesis.

Critical safety modification:

- inferred preference cannot silently become canonical user intent.

### LangMem

Adopted:

- behavioral adaptation and historical memory are separate products.

### Agent Zero

Adopted:

- modular project/skill/schedule architecture;
- runtime independence.

### Magentic-One / AutoGen

Adopted:

- progress state distinct from task incompleteness.

### Anthropic long-running agent harness

Adopted:

- criteria begin unverified;
- fresh/independent evaluation;
- evaluator independence;
- long-running handoff state.

This research lineage is one of the strongest documented curation processes in the AI-Verse family.

---

## 62. Historical repair sequence

### Deterministic core

Phase 4 implemented object model, state machines, ranking, progress, verification, learning, cadence contracts and action safety.

**Lesson:** model reasoning belongs behind deterministic control.

### Public shipment

Phase 5 added install/init/onboarding, bridge, vendor wrappers, migration planning, package CI.

**Lesson:** a strong engine is not a product until it can be installed and exercised independently.

### Persisted policy repair

Brain originally risked caller/runtime policy bypass after restart.

Effective persisted policy loading was centralized.

**Lesson:** canonical policy must be reloaded from durable state at execution time.

### Approval fingerprint repair

Approval was bound to immutable action content.

**Lesson:** approval must authorize one exact effect, not a mutable request object.

### Native write-readiness repair

All native writes now require compatible host, live attachment and installation marker, except explicit bootstrap.

**Lesson:** presence of Brain files is not authorization to write.

### Single direction owner

Brain and OS strategy were made mutually exclusive per scope.

**Lesson:** installation must never imply authority transfer.

### Explicit host selection

Implicit runtime fallback was removed.

**Lesson:** degraded execution mode must be explicitly chosen, not silently substituted.

### Meaningful retrieval

Literal internal task labels were replaced by semantic queries, and capability ranking moved before reasoning limits.

**Lesson:** bounded context must still be relevant, not merely first-N.

### Permission intersection

Brain and host authority became restrictive-by-intersection.

**Lesson:** independent safety boundaries should compose by restriction.

### Skills receipt verification

Execution result and objective proof were separated and generation/provenance bound.

**Lesson:** "tool succeeded" is not "goal achieved."

### Useful explicit ticks

Orientation became bounded and useful without unnecessary model calls.

**Lesson:** intelligence includes deterministic orientation, not constant model invocation.

### Frozen strategy read repair

Brain now respects OS ownership-aware context reads.

**Lesson:** ownership rules must govern reads as well as writes.

### Direction registry concurrency repair

Shared direction registry got registry-wide locking.

**Lesson:** per-object locks do not protect shared read-modify-write registries.

### Local attachment and handback hardening

Tracked manifest registration was replaced with local extension registry; safe disable/detach and Brain->OS handback added.

**Lesson:** optional component lifecycle must preserve upstream tracked files and provide a safe exit from transferred authority.

### Workspace ID alignment

Brain scope grammar was narrowed to OS canonical IDs.

**Lesson:** shared identifiers need one exact cross-component grammar.

---


## 63. Current intended milestone

The present Brain milestone, based on current main, current protocol law and release documentation, is a hardened public-beta intelligence layer that:

- installs cleanly;
- runs standalone;
- integrates natively with current AI-Verse OS;
- initializes safely;
- captures explicit intent;
- supports Claude/Codex/Hermes reasoner wrappers;
- runs bounded cognition ticks;
- supports strategic handover/handback;
- enforces persisted policy;
- performs restrictive host permission intersection;
- safely handles side effects and receipts;
- verifies objectives;
- supports staged learning and strategy promotion;
- provides a real rollback/recovery path for promoted strategy;
- generates cadence requests without scheduler ownership;
- supports safe native lifecycle;
- exposes truthful doctor/migration surfaces;
- passes cross-platform/package acceptance;
- can be installed by a member from an immutable release artifact whose behavior matches the docs.

The stronger AI-Verse-System goal additionally requires an existing agent to adopt Brain seamlessly at any point, including Brain-first -> host-later scenarios, without duplicate truth or repository-level manual wiring.


## 64. Current-target readiness verdict

**Verdict: FUNCTIONALLY STRONG, BUT THE CURRENT PUBLIC-BETA TARGET IS NOT YET COMPLETE**

The deterministic core, current-main native integration, permission model, verification machinery and cross-platform source-head tests are strong.

### Current public-beta blockers

1. the recommended `v0.1.0-beta.1` tag does not contain current main hardening while current package metadata still identifies as beta.1;
2. no public CLI `enable` exists after `disable`;
3. current strategy "rollback" can mark a rule `ROLLED_BACK` but cannot restore a prior known-good revision;
4. the OS direction acceptance workflow still patches the obsolete tracked manifest slot instead of proving the current clean product path;
5. current installation/vendor docs contain `run-tick` examples that fail the current explicit-host-selection parser;
6. installation/security/research/release-history docs retain older generation claims.

### Stronger seamless-system blockers

7. standalone Brain state cannot be adopted automatically if the same root later becomes native AI-Verse OS;
8. no one-step existing-agent activation/adoption flow exists;
9. cross-component write routing is symbolic/contractual rather than end-to-end;
10. optional Data query transport is exposed but not consumed by normal cognition;
11. the documented no-secrets invariant is not generically enforced at Brain canonical-object persistence;
12. actual older-state schema conversion remains unimplemented until a migration path is registered.

These distinctions matter: Brain is not missing its intelligence core. It is missing several lifecycle, restoration, integration and release guarantees required before "works perfectly together like a glove" is true.


## 65. Completeness by dimension

| Dimension | Verdict |
|---|---|
| Brain object/state model | **COMPLETE** |
| Deterministic cognition/control core | **COMPLETE** |
| Intent / Direction Loop | **COMPLETE WITH HOST CURRENT-STATE DEPENDENCY** |
| Attention/proactivity core | **COMPLETE** |
| Public proactivity/kill-switch UX | **PARTIAL** |
| Objective/progress/stall | **COMPLETE** |
| V0-V3 verification | **COMPLETE** |
| Learning + strategy promotion | **COMPLETE** |
| Strategy outcome monitoring | **COMPLETE** |
| Version-restoring strategy rollback | **MISSING** |
| Privileged self-modification safety | **COMPLETE / FAIL-CLOSED** |
| Action/approval/idempotency | **COMPLETE / STRONG** |
| Host permission intersection | **COMPLETE** |
| Vendor reasoner bridge | **COMPLETE WITH MOVING-CLI DEPENDENCY** |
| Standalone mode | **COMPLETE FOR OPERATOR SCOPE** |
| Native OS attachment | **COMPLETE ON MAIN** |
| Native init | **COMPLETE ON MAIN** |
| Strategic handover/handback | **COMPLETE ON MAIN** |
| Disable | **COMPLETE ON MAIN** |
| Re-enable | **MISSING PUBLIC CLI** |
| Detach preserving state | **COMPLETE ON MAIN** |
| Same-mode reinstall/init idempotency | **COMPLETE** |
| Standalone -> native state adoption | **MISSING** |
| Generic agent adoption | **PARTIAL / MANUAL ORCHESTRATION** |
| Migration planning | **COMPLETE** |
| Actual older-state schema conversion | **MISSING** |
| Old-agent history migration | **NOT BRAIN-OWNED GENERALLY; STRATEGIC IMPORT PARTIAL** |
| Doctor | **COMPLETE FOR STRUCTURAL + PARTIAL ATTACHMENT HEALTH ONLY** |
| Composite runtime/dependency/system readiness | **MISSING** |
| Cadence planning/hooks | **COMPLETE** |
| Scheduler execution | **NOT BRAIN-OWNED** |
| Memory semantic reads | **COMPLETE THROUGH HOST CONTRACT WHEN HOST IMPLEMENTS IT** |
| Cross-component canonical write routing | **PARTIAL / SYMBOLIC + HOST INTERFACE ONLY** |
| Skills receipt verification | **COMPLETE** |
| Data host query transport | **COMPLETE AS OPTIONAL BRIDGE OPERATION** |
| Data use in normal cognition | **MISSING** |
| Generic secret-material rejection in Brain state | **MISSING; PROTOCOL RULE + BRIDGE-SPECIFIC GUARDS ONLY** |
| Cross-platform source-head CI | **COMPLETE / GREEN AT REVIEWED HEAD** |
| Wheel clean-install smoke | **COMPLETE FOR CURRENT MAIN CI DESIGN** |
| Exact current immutable member release | **MISSING / STALE TAG** |
| Documentation consistency | **PARTIAL / MATERIAL DRIFT** |


## 66. Lifecycle command matrix

| Lifecycle stage | Required? | Current path | End-to-end status | Gap |
|---|---:|---|---|---|
| package install | Yes | pip/pipx Git tag | Works, but documented tag is stale vs current hardening | New immutable release required |
| inspect integration | Yes | `plan-integration` | Read-only, but clean native host reports missing attachment as blocker even though `init` can auto-attach | Clarify plan vs bootstrap semantics |
| attach | Native only | `attach [--apply]` | Yes on main | Not in documented beta tag |
| enable | Native only | internal API only | **No public CLI** | Add `enable` |
| initialize | Yes | `init [--apply]` | Yes | None on main |
| onboard | Brain-owned strategy | `onboard [--apply]` | Yes | Existing-agent UX can be simpler |
| strategic activate/handover | Native optional | `direction-owner --handover-to-brain` | Yes | Must remain separate from generic activation |
| run cognition | Yes | `run-tick` | Yes | Host/vendor must be explicit; some docs omit required host mode |
| cadence plan | Optional | `plan-cadence` | Yes | Scheduler belongs elsewhere |
| scheduler hooks | Optional | `cadence-hooks` | Yes | Host must install them |
| doctor | Yes | `doctor` | Structural + partial attachment only | Does not prove runtime/dependencies/system |
| migrate | Yes | `migrate [--apply]` | Package metadata refresh for same schema only | No historical schema conversion |
| standalone -> native adopt | Required for install-order independence | none | **No** | Native init blocks parallel standalone store; migration path missing |
| disable | Native | `disable [--apply]` | Yes | No corresponding enable |
| strategic handback | Native | `direction-owner --handover-to-os` | Yes | None |
| detach | Native | `detach [--apply]` | Yes | None after handback |
| uninstall package | Operational | pip/pipx | External package manager | No Brain-specific uninstall orchestration |
| reinstall/reattach | Yes | reinstall + attach/init | Mostly | Disabled state cannot be re-enabled through CLI |
| update | Operational | pip/pipx reinstall/upgrade | Package-manager based | No Brain update-channel UX |
| rollback package | Useful | package-manager version selection | External/manual | No Brain package rollback command |
| rollback strategy | Required by current Brain protocol | generic state transition can mark `ROLLED_BACK` | **No actual prior-revision restoration** | Implement versioned restore/recovery path |
| reconcile uncertain action | Runtime safety | action reconciliation API | Yes | Distinct from component lifecycle reconcile |


## 67. Exact blockers to "works like a glove"

### 67.1 Cut a new hardened release

The immutable install path must contain the same lifecycle/security architecture described by current main.

### 67.2 Add lifecycle symmetry

A component that can be disabled must be re-enableable through the supported CLI.

### 67.3 Prove the exact current member path

Remove the tracked `AI-VERSE.yaml` Brain registration patch from the OS direction workflow. Acceptance must prove stock compatible OS + current Brain local attachment/init.

### 67.4 Fix stale executable documentation

Update the installation protocol, current `run-tick` examples, stale security installation wording, research status and release-history documentation.

### 67.5 Implement real strategy rollback

A `ROLLED_BACK` status is not sufficient.

The strategy subsystem needs an inspectable prior-version relationship plus a deterministic operation that can restore or reactivate the known-good prior strategy, with regression-triggered and user-triggered recovery tests.

### 67.6 Productize agent adoption

A supported setup sequence should verify the runtime, choose the host adapter, initialize/attach, detect existing strategic state, plan import, keep authority transfer explicit, configure cadence where requested, verify the reasoner, run health checks and execute a bounded first orientation.

### 67.7 Support Brain-first -> host-later adoption

If standalone canonical Brain state exists and a compatible AI-Verse host appears later, the system needs a dry-run-first cross-mode migration/adoption transaction.

It must detect competing stores, refuse silent merging, map scope explicitly, preserve provenance, resolve conflicts, verify the destination and retire old authority only after successful adoption.

### 67.8 Complete owner-routed durable writes

When Brain learns something that belongs to OS/Memory/Knowledge/Skills, it should submit a bounded candidate through the canonical owner-controlled write mechanism. Brain must not gain direct sibling storage access.

### 67.9 Wire Data into cognition only if it is a real Brain input

If attached Data is supposed to inform Brain ticks, add purpose-aware bounded `query_data` use and acceptance tests. Until then, document it as an exposed host operation rather than completed cognition integration.

### 67.10 Make the no-secrets rule executable or narrower

Either enforce the rule at the appropriate canonical boundary or document the narrower bridge-level guarantee that exists today.

### 67.11 Preserve scheduler separation while making proactivity easy

Brain should not become the scheduler, but activation should make it easy for the actual scheduler owner to install/enable appropriate cadence hooks.

### 67.12 Add truthful composite readiness

Keep Brain, reasoner, host and scheduler health layers distinct, but provide a composed readiness result capable of proving a representative Brain tick and optional dependencies.

## 68. Definition of done

Brain reaches the intended mature state when:

1. current hardened code is shipped under an immutable version;
2. install docs and installed artifact match;
3. Brain can attach, enable, disable, detach and reattach symmetrically;
4. a compatible existing agent can adopt Brain without repository-level manual wiring;
5. native installation never modifies tracked OS contracts;
6. strategic authority transfer remains explicit and reversible;
7. standalone and native scope semantics remain unambiguous;
8. old strategic state can be imported safely with provenance;
9. general history continues to route to Memory rather than duplicating it;
10. cross-component durable writes use owner-controlled boundaries;
11. vendor reasoners remain replaceable, bounded and non-authoritative;
12. real host selection remains explicit;
13. proactivity remains independent from permission;
14. side-effect uncertainty never creates blind retries;
15. objective completion remains evidence-backed;
16. runtime strategy evolution cannot modify E3/E4 privileged behavior;
17. cadence planning integrates cleanly with the chosen host scheduler;
18. doctor/readiness surfaces accurately distinguish Brain health from host/vendor/scheduler health;
19. release acceptance uses the exact documented member path;
20. current docs no longer describe superseded integration generations.

---

## 69. Contribution to the supreme AI-Verse vision

Brain supplies the missing durable intelligence layer above infrastructure.

AI-Verse OS answers:

- where work belongs;
- what scope is active;
- what source is authoritative;
- what capabilities/connections exist;
- what execution boundaries apply.

Memory answers:

- what happened before;
- what is relevant now;
- what superseded what;
- where historical evidence came from.

Brain answers:

- where are we trying to go;
- what gap matters;
- what should receive attention;
- is this initiative worth pursuing;
- are we actually progressing;
- what evidence proves success;
- what should we learn;
- which strategies are improving.

The architecture is successful when the user experiences one coherent intelligent system, while Brain remains independently portable and never steals OS, Memory, scheduler, tool or user authority.

---

## 70. Open decisions

1. What should the supported `enable` CLI look like?
2. Should Brain expose one higher-level `activate` command, or should AI-Verse OS orchestrate activation?
3. What version should contain the September 10-12 hardening after beta.1?
4. What strategic-intent import format should existing non-AI-Verse agents use?
5. What common system write contract should consume Brain's symbolic write classifications?
6. How should an existing Hermes/Codex/Claude agent persistently invoke Brain without manual host/cadence setup?
7. Which host owns cadence installation in each environment?
8. Should Brain provide a composite readiness command covering Brain + reasoner + host while preserving separate health layers?
9. When is an actual state-schema migration first required, and how will migration registrations be versioned?
10. How should external strategy/prompt/skill optimization candidates be represented without turning Brain into their canonical owner?
11. Should `research/README.md` be frozen as historical research or updated so its "current status" cannot mislead agents?
12. Which old protocol documents should be explicitly marked historical versus rewritten to current local-registry behavior?
