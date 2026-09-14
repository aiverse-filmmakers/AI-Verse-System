# AI-Verse Self-Learning and Skill Evolution Benchmark and Contract

**Status:** Canonical benchmarked public-beta contract  
**Date:** 2026-09-13  
**Owner split:** Brain evaluates learning opportunity; Memory preserves historical evidence; Skills owns reusable learned procedures; Gateway/Automations trigger reviews.

## 1. Purpose

AI-Verse self-learning must not mean "the model rewrites itself every few minutes."

The target is a governed continual-improvement pipeline based on real existing systems.

This contract synthesizes:

- Hermes Agent self-improvement, `/learn`, `/refine` and Curator;
- OpenClaw Self-learning and Skill Workshop;
- Letta persistent-agent continual learning and learned Skills.

## 2. Benchmark findings

### Hermes Agent

Current Hermes explicitly presents itself as a self-improving agent.

Important mechanisms:

- `/learn <source/procedure>` distills reusable Skills from docs, workflows, notes or conversation experience;
- `/refine [focus]` triggers a memory/Skill self-improvement review;
- background review can create agent-owned Skills;
- background-origin Skill provenance distinguishes agent-created material from foreground/user-directed or external Skills;
- Curator tracks Skill views/uses/patches;
- Curator moves Skills through active -> stale -> archived;
- Curator proposes consolidation/patches;
- mutation is preceded by backup when enabled;
- every Skill mutation can be recorded in an append-only ledger;
- archived Skills remain recoverable;
- manually created/external/user-directed Skills can be excluded from autonomous curation.

Primary evidence:

- https://hermes-agent.nousresearch.com/docs/reference/slash-commands
- https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
- https://hermes-agent.nousresearch.com/docs/user-guide/features/curator

### OpenClaw

OpenClaw Self-learning treats Skills as the durable learned unit and Skill Workshop as the governed mutation surface.

Strong patterns:

- `off`, `propose`, `auto` autonomous modes;
- after substantial work, detached/background review can turn corrections and successful procedures into reusable Skills;
- immediate foreground repair when an actually used Skill is wrong/incomplete;
- proposals are separate from active Skills until applied;
- create/update proposals;
- inspect/revise/evaluate/apply/reject/quarantine lifecycle;
- agent-scoped proposal ownership;
- explicit evidence/goal fields;
- approval policy distinct from autonomous learning mode;
- caps on pending/quarantined proposals and proposal size;
- exact-target patch authorization for bounded Skill repair;
- Control UI support for learning from past conversations without enabling full autonomous learning.

Primary evidence:

- https://docs.openclaw.ai/tools/self-learning
- https://docs.openclaw.ai/tools/skills-config
- https://docs.openclaw.ai/tools/skill-workshop/configuration
- https://docs.openclaw.ai/tools/skill-workshop/authoring
- https://docs.openclaw.ai/cli/skills

### Letta

Letta's current platform describes agents as stateful agents that learn from experience and improve with use.

The current product separates:

- persistent Memory;
- reusable Skills, either learned or pre-made;
- subagents;
- schedules;
- persistent harness/runtime state.

Useful architectural lesson:

> Learning should update the correct durable layer rather than collapsing memory, Skill procedure and runtime behavior into one undifferentiated "self modification" store.

Primary evidence:

- https://docs.letta.com/
- https://docs.letta.com/quickstart/
- https://docs.letta.com/v1-sdk/

## 3. What AI-Verse should copy

From Hermes:

- explicit `/learn` and `/refine` concepts;
- evidence-based background review;
- provenance distinguishing agent-owned learned Skills from user/external Skills;
- usage tracking;
- active/stale/archived lifecycle;
- consolidation/deduplication;
- backups and mutation ledger;
- recoverable archive instead of silent deletion.

From OpenClaw:

- off/propose/auto modes;
- proposal objects separate from active Skills;
- inspect/revise/evaluate/apply/reject/quarantine;
- immediate repair of a Skill that just failed;
- bounded patch authorization;
- approval policy separate from learning mode;
- proposal caps and size limits;
- learning from past sessions as an explicit review operation.

From Letta:

- persistent learning is broader than Skills but should be separated by durable owner;
- Memory and Skills are different durable learning products;
- schedules/background work should remain separate from learned content.

## 4. What AI-Verse should not copy

Do not implement:

- periodic blind rewriting every 3-5 minutes;
- automatic edits to upstream/vendor/user-authored Skills;
- hidden production Skill overwrite with no version/rollback;
- learning that can expand permissions;
- learning from secret material into reusable Skills;
- a second general Memory system inside Skills;
- a self-learning scheduler inside Brain;
- promotion based only on the model saying the new Skill is better;
- permanent accumulation of narrow duplicate Skills;
- auto-deletion of learned Skills without recoverable archive;
- hidden modification of security/authority rules.

## 5. Canonical owner split

### Brain owns

- deciding whether observed work contains a potentially reusable lesson;
- classification of improvement type;
- strategic evaluation;
- candidate rationale/evidence references;
- comparison/evaluation signal;
- whether a finding belongs to Skill, Memory, Data, OS knowledge or another owner.

Brain does not own Skill package bytes.

### Memory owns

- historical corrections;
- experiences;
- lessons;
- provenance/evidence references;
- recall of previous failures/successes.

Memory does not own executable Skill procedure packages.

### Skills owns

- learned Skill proposals;
- proposal lifecycle;
- candidate package content;
- immutable candidate/final generations;
- Skill provenance/ownership;
- evaluation metadata;
- security/admission status;
- active/stale/archived status;
- backup/rollback;
- promotion;
- usage metrics specific to Skill lifecycle.

### Gateway owns

- post-turn/substantial-task review trigger;
- foreground immediate repair trigger;
- collecting bounded execution evidence;
- presenting approval UI/interrupt when required.

### Automations owns

- periodic/idle/weekly curation schedules;
- delayed review;
- retrospective learning jobs;
- maintenance wakeups.

## 6. Learning modes

Canonical modes:

```text
off
propose
auto
```

Recommended public-beta default:

```text
propose
```

Rationale:

- it demonstrates real continual learning;
- it keeps a human in the promotion loop by default;
- it is safer while evaluation/admission matures.

`auto` is opt-in and remains bounded by ownership, security, permissions, evaluation and rollback rules.

Mode is not permission. `auto` cannot bypass host/Skills admission policy.

### Owner product-direction note

The current public-beta safety default above is intentionally conservative. The canonical longer-term product intent in `docs/OWNER-PRODUCT-INTENT.md` is that safe internal reusable workflows should not burden ordinary users with a "create a Skill?" question. Once owner-specific evaluation/security/rollback gates support it, a newly detected internal Skill may be created/evaluated/promoted automatically when it is scoped, reversible, non-destructive and requires no permission, dependency, connection or authority expansion.

Until that path is implemented and accepted, proposal-only new-Skill creation remains an implementation gap relative to the target UX rather than evidence that the owner wants routine confirmation.

## 7. Trigger model

Learning should be event-driven first, not timer-driven first.

Eligible triggers:

### Foreground

- explicit `/learn`;
- explicit `/refine`;
- user correction;
- Skill failure discovered during actual use;
- successful novel procedure with clear reusable value;
- repeated manual procedure.

### Background

- substantial task completion;
- N-turn/session review;
- idle review;
- scheduled curator pass;
- review of selected past conversations;
- repeated failure pattern;
- duplicate/narrow Skill accumulation.

A configurable 3-5 minute timer MAY trigger a review in a long-running active session, but elapsed time alone must never authorize mutation or promotion.

## 8. Candidate classification

Before creating a Skill proposal, Brain/Gateway should classify the finding.

Possible owners:

```text
Memory        historical lesson / preference / event
Skills        reusable procedure
Data          current structured operational fact/schema
Brain         strategic belief/goal/evaluation rule within Brain's allowed evolution
OS            current profile/context/decision where OS owns it
Automation    recurring trigger/job
Bot           durable specialist role proposal
None          transient / not worth persisting
```

Self-learning must not turn every useful observation into a Skill.

## 9. Brain learning-candidate envelope

Brain may emit a bounded candidate equivalent to:

```json
{
  "candidate_id": "learn_...",
  "scope": {},
  "suggested_owner": "skills",
  "kind": "create|repair|consolidate|archive-review|memory",
  "summary": "...",
  "target_skill_id": null,
  "evidence_refs": [],
  "success_signal": [],
  "failure_signal": [],
  "risk": "low|medium|high",
  "confidence": 0.0,
  "created_at": "..."
}
```

This is not hidden chain-of-thought.

It is inspectable durable/provenance-oriented metadata.

## 10. Skills proposal lifecycle

Canonical lifecycle:

```text
candidate
-> proposal
-> evaluating
-> pending_approval | auto_eligible
-> applied
   OR rejected
   OR quarantined
```

Applied changes create a new immutable generation.

The previous active generation remains rollbackable according to retention policy.

A proposal should contain:

- proposal ID;
- target agent/system/workspace scope;
- create/update/consolidate type;
- target Skill if any;
- evidence references;
- candidate content/diff;
- source ownership;
- risk classification;
- requested capability/dependency changes;
- evaluation results;
- security/admission results;
- approval state;
- generation digest when applied.

## 11. Ownership/protection classes

Every Skill should be classifiable at least as:

```text
first_party
curated_upstream
user_authored
agent_learned
workspace_local
external
```

Autonomous mutation policy should be conservative.

Default:

- `agent_learned`: eligible for governed self-maintenance;
- `workspace_local`: eligible if explicitly configured;
- `user_authored`: proposal only unless user opts in;
- `first_party`: proposal only through development/release policy;
- `curated_upstream`: never silently rewrite; prefer upstream pin/update or local derived Skill;
- `external`: no autonomous mutation without explicit admission/ownership.

Pinned/protected Skills must never be auto-archived or consolidated away.

## 12. Evaluation before promotion

A learned Skill must not become active simply because it was generated.

Where applicable evaluate:

- package/schema validity;
- instruction size/format;
- security scanner;
- forbidden secret patterns;
- capability/request delta;
- permission expansion;
- dependency readiness;
- test fixtures/examples;
- replay on representative task;
- regression against current Skill;
- duplicate/overlap similarity;
- provenance completeness.

A proposal that expands permissions/capabilities is never silently auto-promoted.

## 13. Immediate repair

If a Skill actually used in the current run proves wrong or incomplete:

1. preserve the failing evidence;
2. read the exact current Skill generation;
3. create a bounded patch proposal against that exact generation/digest;
4. invalidate proposal if target changes before apply;
5. evaluate;
6. apply under current mode/policy;
7. retry only if safe and within task budget.

This avoids broad free-form rewrites of a Skill from stale context.

## 14. Curator / maintenance

Skills should have a Curator-equivalent maintenance loop.

Track at least:

- last selected;
- last successfully used;
- last failed;
- last patched;
- usage count;
- success/failure trend;
- duplicate/overlap signals;
- owner/protection class.

Lifecycle:

```text
active
-> stale
-> archived
```

No autonomous permanent purge in public beta.

Archive must be reversible.

Consolidation creates a proposal with references to source Skills. It must not erase evidence.

## 15. Backup, ledger and rollback

Before any automated mutating curation batch:

- create a recoverable snapshot/pointer when appropriate;
- record mutation intent;
- apply atomically;
- verify resulting generation;
- append immutable audit/provenance event.

Support:

- rollback current learned Skill to previous known-good generation;
- restore archived Skill;
- inspect who/what changed a Skill and why.

## 16. Privacy and secrets

Self-learning must assume conversation/tool output may contain secrets or private data.

Rules:

- no credential/token/private-key copying into Skills;
- prefer evidence references over raw transcript copying;
- redact or reject sensitive material according to executable policy;
- a learned Skill should encode procedure, not unnecessary user data;
- workspace-private Skill scope must remain private;
- past-session mining must obey current visibility/authorization.

## 17. Cost controls

Background learning has explicit budget.

Controls may include:

- minimum substantial-work threshold;
- max reviews per session/day;
- cheap auxiliary model for triage;
- full model only for accepted candidate;
- max pending proposals;
- max proposal bytes;
- skip review when no novel signal;
- Token attribution for review/curator cost.

## 18. Auto mode eligibility

Even in `auto`, direct promotion is allowed only when all are true:

- target is agent-learned or explicitly auto-maintainable;
- no capability/permission expansion;
- no new secret/connection requirement;
- evaluation passes;
- security/admission passes;
- rollback target exists;
- scope is valid;
- current user/system policy allows auto;
- operation is idempotent/current-generation bound.

Otherwise create a pending proposal.

## 19. Public UX

Recommended commands/surfaces:

```text
/learn <source or procedure>
/refine [focus]

aiverse skills learning status
aiverse skills learning mode off|propose|auto
aiverse skills proposals list
aiverse skills proposals inspect <id>
aiverse skills proposals evaluate <id>
aiverse skills proposals apply <id>
aiverse skills proposals reject <id>
aiverse skills proposals quarantine <id>
aiverse skills curator status
aiverse skills curator run
aiverse skills curator restore <skill/version>
```

Exact component CLI names may wrap these.

## 20. Cross-component APIs

### Brain -> Skills

- create learning candidate;
- evidence refs;
- recommended target/operation;
- risk/confidence;
- evaluation criteria.

Brain does not write Skill files.

### Memory -> Brain/Skills

- bounded evidence references/recall;
- correction/failure/success history;
- no automatic executable mutation.

### Skills -> Brain/Gateway

- proposal status;
- evaluation result;
- active generation;
- rollback result;
- usage/health projection.

### Gateway -> Skills

- foreground Skill failure evidence;
- explicit user `/learn` / `/refine`;
- approval response.

### Automations -> Skills

- curator/review wake;
- retrospective review trigger.

Automations does not mutate Skill state directly.

## 21. Public-beta acceptance

Must prove:

- off/propose/auto modes;
- propose is default;
- explicit `/learn`;
- explicit `/refine`;
- correction -> proposal;
- successful procedure -> proposal;
- used-Skill failure -> bounded repair proposal;
- evaluate/apply/reject/quarantine;
- immutable generation after apply;
- rollback;
- agent-learned ownership;
- user/upstream protected behavior;
- no permission-expanding auto promotion;
- no secret persistence in test cases;
- usage metrics;
- stale -> archived;
- restore archived;
- duplicate/consolidation proposal;
- background review budgets;
- restart persistence;
- audit/provenance;
- real end-to-end learned Skill used successfully on a later task.

## 22. Sources

- Hermes docs: https://hermes-agent.nousresearch.com/docs/
- Hermes Skills: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
- Hermes Curator: https://hermes-agent.nousresearch.com/docs/user-guide/features/curator
- Hermes slash commands: https://hermes-agent.nousresearch.com/docs/reference/slash-commands
- OpenClaw Self-learning: https://docs.openclaw.ai/tools/self-learning
- OpenClaw Skill Workshop config: https://docs.openclaw.ai/tools/skill-workshop/configuration
- OpenClaw Workshop authoring: https://docs.openclaw.ai/tools/skill-workshop/authoring
- OpenClaw Skills CLI: https://docs.openclaw.ai/cli/skills
- Letta docs: https://docs.letta.com/
- Letta quickstart: https://docs.letta.com/quickstart/
- Letta Agent SDK: https://docs.letta.com/v1-sdk/
