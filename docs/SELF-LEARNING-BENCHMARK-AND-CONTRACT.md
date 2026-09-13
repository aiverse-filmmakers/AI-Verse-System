# AI-Verse Self-Learning Benchmark and Contract

**Status:** Canonical intended public-beta contract  
**Research date:** 2026-09-13  
**Feature:** Self-learning / self-improving Skills  
**Implementation status:** INTENDED, not implemented by this document  
**Canonical reusable-capability owner:** AI-Verse Skills

## 1. Decision

AI-Verse should learn from real work, but it must not silently rewrite privileged production behavior.

The strongest synthesis is:

observe evidence -> Brain evaluates improvement opportunity -> Skills creates a target-bound proposal -> scan/evaluate -> approve by risk/mode -> promote as a new immutable Skills generation -> monitor -> rollback by owner-controlled generation change.

Ownership is intentionally split:

| Responsibility | Owner |
|---|---|
| Improvement opportunity, strategic evaluation and whether a durable procedure is worth proposing | AI-Verse Brain |
| Historical corrections, outcomes and durable evidence | AI-Verse Memory |
| Reusable Skill package bytes, proposals, ownership policy, immutable generations, promotion, pin/protection, archive and rollback | AI-Verse Skills |
| Foreground review execution and post-run review trigger | AI-Verse Gateway / compatible host |
| Scheduled/idle curation trigger and retry timing | AI-Verse Automations |
| Workspace/scope and outer permission floor | AI-Verse OS |
| Usage/cost telemetry when enabled | AI-Verse Token |
| Delegated work evidence | AI-Verse Multiple Bots |

**LAW:** learning evidence is not permission to modify production state.

**LAW:** no background reviewer may directly mutate active Skill bytes, base system prompts, component code, permissions, credentials, Connections, Data schemas or other owner state merely because it noticed an improvement.

## 2. Research method

This contract was produced from current real implementations:

1. Hermes Agent self-improvement, /refine, /learn and Curator.
2. OpenClaw Self-learning and Skill Workshop.
3. Letta continual learning, MemFS, dreaming and learned Skills.
4. Prime Agent continual harness refinement as an additional serious comparison for race handling, scope and rollback.

The benchmark emphasizes concrete state/lifecycle and failure behavior, not marketing descriptions.

## 3. Benchmark: Hermes Agent

Primary documentation:

- https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
- https://hermes-agent.nousresearch.com/docs/user-guide/features/memory
- https://hermes-agent.nousresearch.com/docs/user-guide/features/curator
- https://hermes-agent.nousresearch.com/docs/reference/slash-commands

Current public failure evidence used as negative tests:

- https://github.com/NousResearch/hermes-agent/issues/80932
- https://github.com/NousResearch/hermes-agent/issues/105921
- https://github.com/NousResearch/hermes-agent/issues/93872
- https://github.com/NousResearch/hermes-agent/issues/84250

### Strong behavior

Hermes distinguishes short durable memory from longer procedural Skills. /learn turns sources or recent work into a Skill. /refine explicitly runs the memory/Skill self-improvement review.

The strongest patterns are:

- foreground learning can turn a correction or nontrivial workflow into a Skill;
- Skill writes can be staged for approval and survive restart;
- background review can be disabled independently while manual /refine remains;
- background review uses a restricted tool surface;
- the Curator maintains lifecycle state and usage evidence;
- Curator supports dry-run, backup, rollback, pin/unpin, adopt, restore, archive, ledger and explicit purge;
- automatic pruning and optional LLM consolidation are separated;
- only declared curator-owned content is eligible for autonomous curation;
- manually/user-directed Skills are not silently adopted;
- archives are recoverable;
- backups precede mutating Curator passes;
- mutation ledger records actor, action, evidence and before/after hashes;
- cheaper auxiliary models can be selected for review.

### Failure lessons

Hermes issue history provides valuable concrete warnings:

1. Prompt instructions to "update existing before create" did not prevent duplicate Skills. Deduplication cannot be prompt-only.
2. A background-review whitelist at tool granularity allowed a skill review to perform destructive memory operations. Background authority must be owner- and operation-scoped.
3. A read-before-write concurrency guard lost state across worker threads and triggered repeated model calls with extreme token burn. Review state and write preconditions need durable/transactional checks, not thread-local assumptions.
4. Background skill creation has had paths where active publication could occur before a fail-closed security decision. Admission must precede promotion.

### What not to copy

Do not copy free direct background writes as the default.

Do not infer autonomous ownership from usage telemetry.

Do not let one generic memory/skill tool grant every mutation verb to an unattended reviewer.

Do not rely on an audit ledger as a gate if mutation can succeed when the ledger fails.

## 4. Benchmark: OpenClaw Self-learning and Skill Workshop

Primary documentation:

- https://docs.openclaw.ai/tools/self-learning
- https://docs.openclaw.ai/tools/skill-workshop
- https://docs.openclaw.ai/tools/skill-workshop/configuration

### Strong behavior

OpenClaw treats Skills as the durable reusable unit and Skill Workshop as the governed authoring path.

It exposes three modes:

- off;
- propose;
- auto.

The strongest patterns are:

- immediate repair targets a Skill actually used in the foreground run;
- runtime usage receipts prevent unrelated Skill rewrites;
- proposals are bound to target hashes/state;
- proposal flow includes scanner state and rollback metadata;
- existing matching proposals/live Skills are revised before creating a new one;
- /learn never auto-applies;
- background review runs only after eligible substantial work;
- later messages are excluded from the captured evidence boundary;
- if saved source evidence is rewritten/removed, review fails rather than silently switching evidence;
- background work does not block foreground completion;
- propose mode narrows the reviewer to the Workshop tool;
- runtime facts must prove Workshop/model availability or delayed review fails closed;
- review exposes privacy/cost implications;
- scanner-critical outcomes quarantine rather than retry in a loop.

### Weaknesses to avoid

OpenClaw's auto mode directly maintains Workshop files with normal file tools. Its own documentation states those direct edits do not create proposals, do not run a post-turn scanner, and do not create automatic rollback snapshots.

That is too weak for AI-Verse because Skills already has immutable generations and a stronger owner-controlled promotion model.

AI-Verse should adopt OpenClaw's proposal, hash-binding, receipt, evidence-boundary and mode concepts, but not the direct-production auto write path.

## 5. Benchmark: Letta continual learning and learned Skills

Primary documentation:

- https://docs.letta.com/configuration/memory
- https://docs.letta.com/configuration/skills

### Strong behavior

Letta uses a git-backed MemFS for durable agent memory. Dreaming uses background subagents to review recent conversations and consolidate useful lessons without interrupting active work.

Letta Skills provide explicit scopes:

- agent-scoped;
- project-scoped;
- computer-scoped;
- bundled.

Agent-scoped Skills can move with the agent. Letta also warns that Skills may contain executable scripts, malicious prompts or data-exfiltration behavior and should come from trusted sources.

Useful patterns for AI-Verse are:

- explicit scope is part of Skill semantics;
- durable versioned state makes review and rollback inspectable;
- background consolidation is separate from foreground interaction;
- larger reorganization takes a backup before merge/split/restructure;
- executable Skill content remains subject to ordinary permissions/secrets rules.

### What not to copy

Letta places agent-scoped Skills inside the agent's git-backed memory filesystem. AI-Verse must not copy that ownership because Memory and Skills are separate canonical components.

Letta's optional second background reviewer still does not ask the human for approval. AI-Verse should not treat "another model reviewed it" as equivalent to promotion authority.

## 6. Additional benchmark: Prime Agent continual harness

Current primary source:

- https://github.com/PrimeIntellect-ai/prime-agent/blob/main/packages/coding-agent/src/core/refinement/refinement.ts

Prime Agent's refinement subsystem contributes three strong patterns:

- the base system prompt is immutable while refinements affect a separate editable harness;
- refinement planning is separated from apply;
- shared state is re-read before apply because another session may have changed it while the model was planning.

Its proposal records rationale, edits and expected outcome, and rollback can restore prior state. It also distinguishes local/session learning from explicit global cross-session learning.

AI-Verse should adopt the plan-then-compare-and-set race discipline, but keep reusable Skill bytes in Skills rather than a generic mixed harness store.

## 7. Cross-benchmark extraction

| Dimension | Strongest observed pattern | AI-Verse decision |
|---|---|---|
| Canonical reusable state | Skills/Workshop packages | Skills only |
| Evidence | real corrections, successful procedures, usage receipts | Memory + run/effect receipts, referenced by Brain |
| Foreground repair | target only a Skill proven used | adopt |
| Background review | detached, bounded, non-blocking | Gateway or Automations trigger Brain review |
| Modes | off/propose/auto | adopt, default propose |
| Ownership | agent/user/provider distinctions | explicit Skills ownership/protection policy |
| Target binding | base hash/generation before patch | mandatory |
| Dedup | revise existing first, similarity/ownership checks | enforce in Skills, not prompt-only |
| Security | scanner/quarantine + permission preservation | admission before any promotion |
| Rollback | snapshots/version history | immutable generation rollback |
| Persistence | proposals and learned Skills survive restart | Skills-owned |
| Race handling | plan then re-read baseline before apply | compare-and-set generation |
| Curation | active/stale/archive, pin, restore, explicit purge | agent-learned only by default |
| Privacy/cost | disclose extra model runs/provider | explicit provider/data scope and budgets |
| Failure handling | record failure, avoid retry loops | one attempt per trigger, bounded re-review |
| Provenance | actor/evidence/hash/diff/history | mandatory promotion receipt |

## 8. Canonical objects and ownership

### Brain: Improvement Opportunity

Brain may persist an improvement opportunity containing:

- opportunity_id;
- workspace/system scope;
- trigger type;
- evidence references;
- target Skill identity/generation if known;
- rationale;
- expected reusable benefit;
- confidence/risk classification;
- recommendation: abstain, revise existing, create proposal, consolidate, archive candidate;
- evaluation status.

Brain must not persist the Skill package bytes as a second canonical copy.

### Memory: evidence

Memory owns historical evidence such as:

- user correction;
- failed approach and verified recovery;
- repeated workflow observation;
- durable lesson/provenance;
- source session/run references.

Memory does not own Skill proposal state.

### Skills: proposal and package lifecycle

Skills owns:

- proposal_id;
- target package/Skill ID;
- base immutable generation/hash;
- candidate bytes/diff;
- ownership class;
- scope;
- requested capability/permission footprint;
- scanner results;
- dedup/consolidation analysis;
- eval definitions/results;
- approval state;
- immutable promoted generation;
- active routing/promotion pointer;
- pin/protection state;
- quarantine/archive state;
- rollback/promotion receipts.

## 9. Self-learning modes

AI-Verse should expose per-system/workspace policy:

### off

- no automatic post-run improvement review;
- no scheduled learning review;
- explicit /learn and explicit manual improvement remain available;
- no existing proposal is deleted merely because mode changes.

### propose - public-beta default

- eligible foreground corrections and background reviews may create/revise Skills proposals;
- proposals may be scanned/evaluated automatically;
- no proposal becomes active without required approval;
- foreground answer never waits for detached review;
- user sees a visible proposal/abstain/failure receipt.

### auto

Auto is deliberately narrower than OpenClaw's direct-edit mode.

Auto may automatically promote only low-risk changes to **agent-learned, unprotected Skills** when every mandatory gate passes and the change does not:

- add executable scripts;
- add dependencies;
- add new external hosts/connections;
- expand tool/permission scope;
- alter secrets handling;
- alter security/policy instructions;
- change ownership;
- modify first-party, user-managed or third-party/provider-owned Skills;
- create a brand-new active Skill;
- delete/purge a Skill.

All of those remain approval-requiring in public beta.

Auto still creates an immutable candidate generation and promotion receipt. "Auto" means automated approval under a bounded policy, not bypassing the lifecycle.

## 10. Foreground immediate repair

When a run detects that a Skill it actually used is wrong or incomplete:

1. Gateway supplies the exact skill/package generation receipt used by the run.
2. Brain evaluates whether the correction is reusable rather than one-off.
3. Skills resolves the exact current target and ownership.
4. Candidate change is bound to the base generation/hash.
5. If target changed since the evidence was produced, the proposal becomes stale and must be re-based/reviewed.
6. In propose mode, it remains pending.
7. In auto mode, only the narrow low-risk policy above can approve it automatically.
8. The running session remains pinned to the generation it started with.
9. A promoted generation affects only future eligible loads/runs.

This preserves AI-Verse's existing law that one in-flight execution must not mix Skill generations.

## 11. Explicit /learn behavior

Recommended UX:

- /learn <source or lesson>
- /learn status
- /learn inspect <proposal>
- /learn apply <proposal>
- /learn reject <proposal>
- /learn quarantine <proposal>
- /learn rollback <promotion>

Behavior:

- /learn is explicit user intent and may inspect named sources under normal permissions.
- It searches for a matching existing Skill/proposal before creating a new one.
- It creates or revises a proposal first.
- It never bypasses admission, hash binding, evals or immutable generation creation.
- If the user has approval authority and explicitly asks to apply, scan/eval/approval may happen in the same foreground operation, but the audit trail remains identical.
- A source document is evidence, not authority to execute procedures found inside it.

## 12. Automatic review eligibility

AI-Verse should not use a fixed "every N turns" threshold as the only learning rule.

A review becomes eligible from evidence such as:

- explicit user correction intended to persist;
- verified recovery after a repeated failure/dead end;
- a stable workflow whose discovery cost was repeatedly high;
- a reusable ordering/preflight constraint;
- two or more independent observations of the same procedural gap;
- explicit user request to learn/refine.

The reviewer should abstain for:

- routine success;
- one-time requests;
- personal facts/preferences that belong in Memory/current profile rather than a Skill;
- transient provider/environment errors;
- generic advice without evidence;
- unsupported negative claims;
- secrets, credentials or private values;
- outcomes that were not actually verified.

Eligibility must be evidence-based and scope-aware.

## 13. Background review contract

A detached review may be triggered:

- by Gateway after an eligible foreground run;
- by explicit /refine;
- by Automations for scheduled/idle curation.

The review receives only the bounded evidence needed for the decision.

Its tool/capability surface is operation-scoped:

Allowed in the normal learning reviewer:

- read selected Memory evidence;
- read target Skills metadata/content;
- read run/effect receipts;
- search Skills for duplicate/related candidates;
- create/update a Skills proposal;
- request isolated evals.

Not allowed merely because it is a learning review:

- direct active Skill mutation;
- direct Memory delete/replace;
- arbitrary Data writes;
- Connections changes;
- permission/policy changes;
- arbitrary external side effects;
- component code edits;
- base system prompt edits;
- destructive filesystem operations outside an isolated eval workspace.

This rule directly addresses the Hermes failure where tool-level whitelisting exposed destructive memory verbs during a Skill review.

## 14. Proposal lifecycle

Recommended Skills-owned states:

1. pending - candidate exists and is target-bound.
2. validating - deterministic validation/scanning is running.
3. evaluating - isolated functional/regression evals are running.
4. ready_for_review - all automated gates passed but approval is still required.
5. approved - authorized for promotion.
6. promoted - immutable generation created and made eligible for future selection.
7. rejected - operator/policy declined it.
8. quarantined - security/admission concern.
9. stale - base generation/evidence changed before apply.
10. superseded - replaced by a newer proposal.

A proposal can fail validation/evaluation without mutating active Skills.

No partial candidate write becomes production state.

## 15. Mandatory admission and evaluation

Before promotion, Skills should require the applicable subset of:

- manifest/schema validation;
- path/containment validation;
- provenance/source validation;
- secret/PII scan;
- dangerous instruction/prompt-injection scan;
- script/static analysis;
- dependency/license policy;
- requested tool/connection/permission footprint diff;
- semantic duplicate/overlap check;
- deterministic tests/smoke tests;
- isolated execution where executable behavior exists;
- replay against source evidence;
- regression against prior Skill evals;
- holdout task(s) where practical;
- baseline versus candidate comparison;
- approval policy decision.

A candidate that requires broader authority cannot grant it to itself. Promotion and execution permission remain separate.

## 16. Duplicate and consolidation handling

Prompt wording is not sufficient for deduplication.

Before creating a new Skill proposal, Skills must search:

- exact normalized identity/name;
- aliases;
- same target/namespace;
- pending proposals;
- semantic overlap against existing descriptions/procedures.

If a strong match exists, default to revising the existing owner-approved Skill rather than creating a parallel one.

Consolidation is its own proposal type and must:

- identify all source Skills/generations;
- preserve provenance;
- preserve redirects/aliases where needed;
- prove that distinct procedures are not accidentally merged;
- never hard-delete source Skills as part of automatic promotion;
- leave a reversible archive/supersession trail.

## 17. Ownership, protection and pinning

Skills must explicitly distinguish content the autonomous learner may control from content it may only propose against.

At minimum, policy needs to distinguish:

- AI-Verse/first-party managed;
- third-party/provider managed;
- user-managed;
- agent-learned.

Public-beta automatic promotion applies only to agent-learned content.

Existing generation pinning remains a runtime/distribution guarantee and must not be silently reinterpreted.

Skills also needs an owner-controlled learning protection flag or equivalent so an operator can make a Skill ineligible for automatic promotion/archive even when it is agent-learned.

References from Automations/Bots or other declared durable consumers should protect a Skill from automatic archival until those references are deliberately migrated.

Ownership/protection is declared, never inferred from usage telemetry.

## 18. Curation lifecycle

Curation belongs to Skills; Automations only triggers it.

Recommended public-beta behavior for agent-learned Skills:

- active;
- stale candidate after a configurable inactivity period;
- archived only through reversible owner-controlled transition;
- restore supported;
- automatic hard purge disabled.

Conservative initial defaults may be 30 days to stale and 90 days to archive, but release configuration should remain policy-driven and usage evidence must be trustworthy before any automatic transition.

Pinned/protected/referenced Skills skip automatic stale/archive transitions.

Consolidation should be propose-first unless auto policy proves it is low-risk and reversible.

## 19. Concurrency and idempotency

Learning is highly race-sensitive because model planning may take seconds or minutes.

Required rule:

1. plan against immutable base generation/hash;
2. immediately before promotion, re-read current target state;
3. compare expected generation/hash/version;
4. reject or mark stale on mismatch;
5. never apply a fuzzy patch to a different base;
6. make promotion atomic;
7. make promotion operation_id idempotent.

Review-local thread state is not an acceptable source of truth for write preconditions.

A failed or cancelled detached review gets one bounded attempt. Do not build immediate retry loops that can multiply token spend.

## 20. Security

Self-learning is an input-to-code/instructions supply-chain boundary.

Required controls:

- source/evidence is untrusted data;
- candidate instructions cannot expand their own permissions;
- executable Skill content is sandboxed/evaluated before promotion;
- secrets are referenced through approved secret mechanisms, never learned into Skill bytes;
- third-party Skill content cannot become agent-owned through inference;
- background reviewer authority is operation-scoped;
- scanner unavailable/error fails closed for auto promotion;
- critical scan result quarantines;
- remote approval requires authenticated principal mapping;
- package integrity does not equal trust;
- a promoted Skill still requires runtime readiness, permission and approval at execution time.

## 21. Rollback and recovery

AI-Verse should exploit Skills' existing immutable-generation architecture rather than invent mutable file backups as the primary recovery model.

Promotion:

- creates a new immutable generation;
- records prior active generation;
- atomically changes eligible routing;
- never rewrites the old generation.

Rollback:

- atomically restores the previous approved generation/routing;
- preserves the bad generation for audit/quarantine;
- records actor, reason and receipt;
- does not erase proposal/eval history.

If a review crashes before promotion, active Skills remain unchanged.

If a promotion succeeds but downstream verification fails, policy can quarantine/rollback the promoted generation without reconstructing bytes from chat history.

## 22. Audit and provenance

Every learning proposal/promotion should record:

- trigger and actor;
- workspace/system scope;
- source run/session IDs;
- Memory evidence IDs;
- Skill generation(s) actually used;
- base generation/hash;
- candidate diff/content digest;
- model/provider/config used for evaluation;
- scanner versions/results;
- eval definitions/results;
- duplicate/consolidation findings;
- requested authority footprint delta;
- approval actor or auto-policy version;
- promotion operation ID;
- new immutable generation ID;
- rollback/quarantine events.

Token may record raw model/cost usage, but Skills/Brain must retain enough references to explain why a change happened even when Token is disabled.

## 23. Privacy and cost

Background learning can expose conversation/tool content to a model provider and can become a major hidden cost.

Public-beta rules:

- setup must disclose whether automatic review is enabled and which provider/model it uses;
- propose is the default mode;
- review input should be minimized to selected evidence rather than blindly sending the entire transcript where possible;
- users can disable review per system/workspace;
- provider fallback must not silently send review evidence to a provider with a different privacy contract;
- review has token/time/cost ceilings;
- one trigger gets one bounded attempt;
- foreground completion never waits for detached learning;
- visible receipts show proposal, abstain, failure and cost/usage summary where available;
- cheaper/local auxiliary models may be selected explicitly;
- sensitive evidence can be marked non-exportable to external review providers.

## 24. Background versus foreground behavior

Foreground:

- explicit /learn;
- immediate repair after a Skill actually used fails or is corrected;
- visible proposal/apply decisions.

Background:

- eligible post-run review;
- scheduled curation;
- duplicate/consolidation analysis;
- stale/archive proposal.

Background review may create proposals. It does not gain additional production authority merely because it runs unattended.

No post-final hidden direct production modification is allowed.

## 25. What AI-Verse should not copy

Do not copy:

- OpenClaw auto mode's direct Workshop file edits without proposal/scanner/rollback;
- Hermes default free Skill writes as the AI-Verse default;
- prompt-only deduplication;
- tool-level whitelisting when a tool contains destructive verbs;
- learned Skills stored inside Memory as the canonical package store;
- "a second model reviewed it" as approval;
- mutation that proceeds when admission/scanner state is unavailable;
- auto adoption of user/third-party Skills inferred from telemetry;
- automatic hard deletion based only on inactivity;
- hidden transcript export to a review provider;
- unbounded background retries;
- direct modification of base system prompts, component code, permissions or credentials through the Skill-learning loop.

## 26. Public-beta acceptance tests

Before self-learning is public-beta ready, acceptance must prove:

1. propose is the default after clean setup.
2. off disables automatic review without disabling explicit /learn.
3. a background reviewer cannot directly mutate active Skill bytes.
4. a background Skill review cannot delete/replace Memory merely because Memory is readable.
5. immediate repair requires a receipt proving the target Skill generation was actually used.
6. running sessions remain pinned to their original Skill generation.
7. stale target hash/version makes a proposal stale instead of patching a new base.
8. duplicate Skill creation is prevented by executable checks, not prompt advice.
9. first-party/user/third-party Skills cannot be auto-promoted over.
10. agent-learned low-risk auto promotion still creates an immutable generation and full receipt.
11. scanner/eval failure leaves active generation unchanged.
12. scanner unavailable fails closed for auto promotion.
13. executable/permission-expanding changes require human approval.
14. rollback restores the previous approved generation atomically.
15. concurrent proposals cannot overwrite one another silently.
16. a detached review crash does not alter production state.
17. one failed review does not enter an immediate retry/token loop.
18. privacy/provider configuration is visible before automatic review.
19. evidence marked non-exportable is not sent to an external reviewer.
20. archive is reversible and automatic purge is disabled.
21. Automations can trigger curation without owning Skill proposal/package state.
22. Brain can abstain or create an opportunity without storing duplicate Skill bytes.

## 27. Implementation order

1. Skills: implement/finish the proposal/workshop data model on top of existing immutable generations.
2. Skills: add ownership/protection, base-generation binding, CAS promotion and proposal idempotency.
3. Skills: complete admission scanner, semantic duplicate checks and isolated eval pipeline required for learned content.
4. Brain: add Improvement Opportunity evaluation referencing Memory/run evidence and Skills targets, without package bytes.
5. Gateway: add foreground usage receipts, explicit /learn, immediate repair trigger and eligible detached-review execution.
6. Memory: expose bounded historical evidence/provenance reads needed by Brain, without becoming Skill storage.
7. Gateway + Skills: implement propose mode end to end and make it the public-beta default.
8. Skills: add reversible curation states and consolidation proposals.
9. Automations: add scheduled/idle curation triggers that reference owner APIs only.
10. Token: attribute review/eval/promotion cost where enabled.
11. Implement restricted auto mode only after admission/evals/rollback/provenance acceptance is green.
12. Distribution/System: freeze end-to-end public-beta acceptance and privacy/security tests.

## 28. Compatibility with current AI-Verse architecture

No new Learning repository is required.

The contract aligns with existing ownership:

- Brain already owns learning/evaluation and strategic evolution.
- Memory already owns historical evidence.
- Skills already owns reusable packages and immutable generations.
- Gateway and Automations are already planned as execution/trigger owners.
- OS remains the authority floor.

The important current implementation dependency is Skills' known admission/evaluation gap. Public beta may ship governed propose mode once proposals and safe admission are real, but should not enable automatic promotion until package admission, eval, ownership protection and atomic rollback are proven.

A second tension is generation granularity. Current Skills already guarantees immutable generations. Self-learning must build on that owner-controlled model, whether the implementation promotes a package-level generation or a new whole-provider generation. It must not solve the problem by mutating the active generation in place.
