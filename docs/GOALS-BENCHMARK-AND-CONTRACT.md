# AI-Verse Goals Benchmark and Contract

**Status:** Canonical intended public-beta contract  
**Research date:** 2026-09-13  
**Feature:** Persistent Goals / autonomous continuation  
**Implementation status:** INTENDED, not implemented by this document  
**Canonical owner:** AI-Verse Brain for goal and verification state

## 1. Decision

AI-Verse should implement Persistent Goals as one Brain-owned durable objective contract plus a separate host continuation mechanism.

The feature must not become another scheduler, task database, Bot database or session-only Goal store.

The final ownership rule is:

| Responsibility | Owner |
|---|---|
| Goal objective, completion contract, criteria, status, verification state, blocker state, policy intent | AI-Verse Brain |
| Workspace identity, outer scope and permission floor | AI-Verse OS |
| Foreground execution, autonomous continuation admission, pause/resume/cancel transport, streaming, continuation leases | AI-Verse Gateway / compatible host |
| Durable time/event wake registrations and wake delivery | AI-Verse Automations |
| Delegated Bot/Worker coordination, Tasks and Handoffs | AI-Verse Multiple Bots |
| Historical evidence recalled later | AI-Verse Memory |
| Structured operational facts used as evidence | AI-Verse Data |
| Raw usage/cost telemetry when enabled | AI-Verse Token |

**LAW:** there is one canonical Goal state, in Brain. Gateway sessions, Automations jobs and Multiple Bots Tasks may reference a Brain goal_id but may not maintain a competing editable Goal object.

## 2. Research method

This contract was produced benchmark-first from current real implementations and current primary documentation/source where available.

Primary benchmark set:

1. Hermes Agent Persistent Goals.
2. OpenClaw Goal.
3. OpenAI Codex Goal source and current public issue evidence.
4. Prime Agent bounded autonomous mode and quality-gate pattern where it materially improves the comparison.

The comparison focuses on state, lifecycle, continuation, verification, budgets, race behavior, recovery, authority and UX rather than command-name imitation.

## 3. Benchmark: Hermes Persistent Goals

Primary source:

- https://hermes-agent.nousresearch.com/docs/user-guide/features/goals
- https://hermes-agent.nousresearch.com/docs/user-guide/configuration
- https://hermes-agent.nousresearch.com/docs/reference/slash-commands

### Strong behavior

Hermes gives one session a standing Goal that survives turns and resume. After each turn an auxiliary judge returns a small verdict such as done, blocked, continue or wait. Continue feeds an ordinary user-role continuation back into the same session.

Important controls include Goal set/show/status, draft, pause, resume, clear, wait/unwait, quality gates and subgoals.

The strongest patterns are:

- a structured completion contract can be drafted from plain language;
- deterministic quality gates run before semantic judging;
- a failed unchanged gate can reuse the prior failure instead of burning wall time;
- gate retries and timeouts are bounded;
- waiting on a real process or timer consumes no Goal turns while parked;
- user input preempts queued autonomous continuation;
- setting a replacement Goal during an active run is rejected to avoid races;
- Goal state persists separately from the conversational turn;
- the default 20-turn continuation budget auto-pauses instead of continuing forever;
- judge reasons are visible to the operator.

### Weaknesses to avoid

Hermes' semantic judge primarily sees the Goal plus the assistant's final response, with deterministic gates supplying stronger evidence where configured. That is weaker than requiring current authoritative evidence for every completion claim.

Judge failure is fail-open to continue. The turn budget is the backstop. AI-Verse should not let repeated verifier infrastructure failures become an expensive hidden loop.

A session-keyed Goal store is appropriate for Hermes but would conflict with AI-Verse because Brain already owns durable goals and intent.

## 4. Benchmark: OpenClaw Goal

Primary source:

- https://docs.openclaw.ai/tools/goal

### Strong behavior

OpenClaw models a Goal as one durable objective attached to a session. It explicitly says a Goal is not a background task, reminder, cron job or standing order.

It exposes operator commands for start, edit, pause, resume, block, complete and clear, while model tools are narrower. The model can read the Goal and report complete or blocked, but it cannot silently pause, resume, clear or replace it.

The strongest patterns are:

- one Goal per session binding;
- explicit statuses for active, paused, blocked, budget-limited and complete;
- token budgets stop pursuit without erasing the objective;
- resume creates a fresh budget window while keeping the same Goal;
- active Goal context is injected only while active;
- start is atomic with run admission in the Control UI;
- failed admission leaves the user's draft and does not create a ghost active Goal;
- structured controls target goalId, so a stale UI control cannot mutate a replacement Goal;
- update/clear calls carry operationId, issuedAtMs and goalId;
- retry receipts are durable for a bounded period;
- reusing an operation ID with a different request is rejected;
- operator.write and session participation are required;
- concurrent Goal control operations are rejected.

### Weaknesses to avoid

OpenClaw lets the model's own complete/blocked report drive terminal status. AI-Verse should require Brain-owned verification before terminal completion.

The Goal is session state in OpenClaw. AI-Verse should keep the UI/session binding in Gateway but canonical objective state in Brain.

## 5. Benchmark: OpenAI Codex Goal

Current primary source:

- https://github.com/openai/codex/blob/main/codex-rs/ext/goal/templates/goals/continuation.md
- https://github.com/openai/codex/blob/main/codex-rs/ext/goal/src/spec.rs
- https://github.com/openai/codex/blob/main/codex-rs/ext/goal/src/tool.rs

Current public failure evidence, useful as negative tests:

- https://github.com/openai/codex/issues/37869
- https://github.com/openai/codex/issues/40929
- https://github.com/openai/codex/issues/24531
- https://github.com/openai/codex/issues/38148

### Strong behavior

Codex's current continuation instructions contain the strongest completion discipline in the benchmark:

- keep the original objective intact across turns;
- do not redefine success around an easier subset;
- treat current worktree and external state as authoritative;
- classify progress, verified wait and no progress;
- verify completion requirement by requirement;
- use evidence whose scope matches the requirement;
- weak, indirect or missing evidence means incomplete;
- a token limit is not success;
- blocked requires a repeated real blocker, not ordinary difficulty;
- the model should not infer a Goal from an ordinary task;
- token budgeting is persisted with the Goal.

This is the right completion philosophy for AI-Verse.

### Failure lessons

Current issue reports show why Goal control cannot rely on model compliance or a stale prompt:

- a Goal whose persisted status was paused has still received automatic continuation turns;
- resumed Goals have entered rapid no-progress continuation loops;
- a conversational stop can leave canonical Goal state active and burn tokens;
- stale/in-flight continuations can outlive Goal control changes.

These reports are not the normative contract, but they are valuable race and no-progress acceptance cases.

**AI-Verse rule derived from them:** before every autonomous continuation, Gateway must re-read Brain's canonical Goal status/version and validate a revocable continuation lease. Pause, cancel, edit that invalidates execution assumptions, or replacement must revoke the old lease immediately. An old queued continuation may never act merely because it was admitted earlier.

## 6. Additional benchmark: Prime Agent

Relevant current source:

- https://github.com/PrimeIntellect-ai/prime-agent

Prime Agent separates a persistent Goal from bounded autonomous execution and supports user-defined quality gates. That separation is useful for AI-Verse:

- Goal answers what outcome remains true.
- Autonomous continuation answers how long the host may keep trying now.
- A quality gate proves only what that gate actually covers.
- Exhausting a limit is a stop condition, not evidence of completion.

AI-Verse should preserve this separation.

## 7. Cross-benchmark extraction

| Dimension | Strongest observed pattern | AI-Verse decision |
|---|---|---|
| Canonical state | Durable Goal object separate from turns | Brain owns it |
| One vs many | One execution Goal per active session binding, broader systems may contain many objectives | Brain may hold many Goals; one Gateway session binds to at most one active execution Goal |
| Lifecycle | active plus explicit pause/block/complete and recoverable budget stop | Brain state machine below |
| User controls | status, edit, pause, resume, clear/cancel, verification/gates | Adopt with AI-Verse ownership |
| Persistence | durable state survives restart/resume | Brain persistence, not Gateway Goal copy |
| Continuation | host injects ordinary continuation after each turn | Gateway continuation driver |
| Completion | deterministic gates plus conservative evidence audit | Brain verifier over current authoritative evidence |
| Budgets | bounded turns/tokens; stop does not equal success | mandatory turn ceiling plus optional token/time/cost ceilings |
| Wait | park without model turns until real event/process/time | waiting state plus optional Automations wake |
| Blocking | repeated genuine blocker, not difficulty | validated blocker or repeated same no-progress condition |
| Idempotency | goalId + operationId + stale-control rejection | required on every durable mutation |
| Race control | reject conflicting operations; session idle admission | compare-and-set version + revocable continuation lease |
| Permissions | Goal never expands tool authority | OS/host permission floor rechecked at every effect |
| Recovery | objective survives stops; resume opens new execution window | Brain state survives; Gateway reconstructs only execution binding |
| Audit | status reason, usage, operation receipts | immutable state-transition and verification receipts |
| Background | Goal is not automatically cron/standing order | explicit wake policy only |
| Cost | bounded auxiliary/continuation work | visible budget windows and Token integration when enabled |

## 8. Canonical Brain Goal object

Brain should persist at minimum:

- goal_id;
- system_id and workspace_id;
- creator principal and creation provenance;
- objective;
- completion contract;
- status;
- status_reason;
- monotonically increasing version;
- execution policy;
- budget policy;
- current activation/budget epoch;
- wait condition when applicable;
- blocker fingerprint/history;
- evidence references;
- verification result and verifier version;
- created, updated and terminal timestamps;
- terminal receipt when complete/cancelled/superseded.

The completion contract should support:

- outcome;
- explicit acceptance criteria;
- verification requirements;
- constraints;
- boundaries;
- stop_when conditions.

Brain owns the contract and verdict. It does not execute shell commands itself.

## 9. Goal lifecycle

Recommended canonical states:

1. **draft** - objective/contract exists but is not executing.
2. **active** - eligible for bounded Gateway continuation.
3. **waiting** - progress depends on a validated future process/event/time condition.
4. **paused** - autonomous pursuit is stopped by operator, policy, budget, usage, verification infrastructure or runtime protection.
5. **blocked** - a genuine stable blocker requires user/external change and no valid automatic wake is registered.
6. **complete** - Brain verification proves the full contract.
7. **cancelled** - operator intentionally ends pursuit without success.
8. **superseded** - explicitly replaced by another Brain Goal.

Terminal states are complete, cancelled and superseded.

Paused is reversible. Waiting may return to active only from a validated wake. Blocked returns to active only through explicit resume or a specifically authorized external-state transition.

A visible "budget_limited" UX should be represented as paused with status_reason=budget rather than a second independent canonical state.

## 10. Exact public Goal UX

Recommended public commands:

- /goal <objective> or /goal start <objective>
- /goal draft <objective>
- /goal status
- /goal show
- /goal edit <objective>
- /goal pause [reason]
- /goal resume [reason]
- /goal cancel [reason]
- /goal clear
- /goal verify
- /goal gate add|list|remove|clear
- /subgoal add|list|remove|clear

Semantics:

- start creates or activates only from explicit user/system intent. The model must never infer a persistent Goal from an ordinary task.
- start is acknowledged only after Brain persistence and Gateway run admission form one recoverable transaction. If execution admission fails, the Goal remains draft rather than pretending to be active.
- clear removes the session binding/UI focus. It does not silently erase Brain history. Clearing an unfinished active Goal requires cancel or explicit clear-with-cancel semantics.
- edit changes the objective/contract, increments version and revokes the current continuation lease.
- pause revokes continuation immediately.
- resume creates a new activation epoch and fresh bounded budget window.
- complete from the operator is an override request. Brain records it as an operator override with reason/evidence, never as an agent self-certified success.

Model-facing operations should be narrower:

- get_goal;
- report_goal_progress;
- propose_goal_wait;
- propose_goal_blocked;
- propose_goal_complete.

The model must not silently edit, pause, resume, cancel, clear, replace or broaden the Goal.

## 11. Continuation contract

Gateway/host owns execution continuation, not Goal truth.

After a foreground Goal turn finishes, Gateway may schedule another continuation only if all are true:

1. Brain still reports the same goal_id.
2. Brain status is active.
3. Brain version equals the version bound to the continuation lease.
4. the activation epoch is unchanged;
5. the session/run is idle and recoverable;
6. cancellation/pause has not been observed;
7. current OS scope and permission floor still allow the next operation class;
8. budget remains;
9. no no-progress or verification circuit breaker has fired.

Every continuation lease is bound to:

- goal_id;
- Brain goal version;
- activation epoch;
- run/session binding;
- authorization/scope snapshot identifier;
- expiry;
- unique continuation operation ID.

Before every autonomous turn Gateway revalidates the lease against current Brain and OS state. This check is executable control-plane logic, not prompt text.

User input always preempts a not-yet-started continuation.

## 12. Verification and completion

AI-Verse should not copy a "judge the last answer" completion model.

Completion is a Brain-owned verification transaction:

1. derive the full requirement set from the Goal contract;
2. gather current authoritative evidence from the appropriate owners/providers;
3. run declared deterministic gates through Gateway/host under normal permissions;
4. bind each gate result to the exact state/version it checked;
5. run a conservative semantic verifier only over the Goal contract plus current evidence;
6. require every criterion to be proved at the correct scope;
7. persist the verification record;
8. transition to complete only if the verification transaction succeeds.

A passing test proves only the scope that test covers.

A model statement, plan update, prior transcript or plausible final answer is not proof.

If the semantic verifier is unavailable or malformed, AI-Verse must not mark the Goal complete. Gateway may continue actionable work within the remaining budget. Repeated verifier infrastructure failures must trip a bounded pause instead of fail-open looping forever.

## 13. Quality gates

Quality gates are useful but security-sensitive.

A gate:

- is part of the Brain completion contract;
- is executed by Gateway/host, never Brain;
- runs under the same or narrower current permission envelope;
- has a timeout and retry ceiling;
- records command/tool identity, relevant state fingerprint, exit/result and output digest;
- cannot grant new permissions;
- is not re-run against unchanged authoritative state merely to burn time;
- cannot prove requirements outside its declared coverage.

Adding an executable gate from a remote/untrusted source may itself require approval.

## 14. Waiting, blocking and no-progress protection

### Waiting

Use waiting when a specific validated condition can wake work, such as:

- a known process/session handle;
- a CI/deploy job;
- a rate-limit deadline;
- an Automation event;
- a specific time.

While waiting:

- no model continuation turns run;
- the Goal turn budget does not advance;
- the wait condition is visible;
- a stale/dead handle must resolve to re-evaluation, not an infinite park.

A short in-process wait may be handled by Gateway. A durable cross-restart time/event wake belongs to Automations and references goal_id only.

### Blocking

Blocked is for a true impasse that cannot be solved within current authority and has no valid automatic wake.

A deterministic blocker such as denied required permission, missing user secret or explicit external rejection may block immediately with evidence.

Otherwise, after the same no-progress/blocker condition is observed on three consecutive Goal attempts, no fourth autonomous turn may run. Brain must classify it as blocked, waiting or paused(no_progress).

This circuit breaker is host-enforced. It cannot rely only on the model remembering to call a status tool.

## 15. Budgets and stop conditions

Public-beta default:

- maximum 20 automatic continuation turns per activation epoch.

Additional optional limits:

- token budget;
- wall-clock budget;
- cost budget when cost evidence is available;
- provider/usage quota;
- deterministic gate retry/time limits.

Distribution/host policy may impose stricter hard ceilings.

Resume creates a new activation epoch and a fresh window but never erases cumulative audit/usage history.

Reaching any budget pauses pursuit. It never marks the Goal complete.

If Token is installed, Token remains canonical for raw usage/cost telemetry. Brain stores Goal control limits, budget status and evidence references, not a competing global usage ledger.

## 16. Idempotency and race law

Every durable Goal mutation must include:

- goal_id where a Goal already exists;
- expected Brain version;
- operation_id;
- actor/principal;
- issued_at;
- requested transition/payload.

Brain applies compare-and-set semantics.

Required outcomes:

- exact retry returns the original receipt;
- same operation_id with different payload fails;
- stale expected version fails;
- stale goal_id cannot mutate a replacement;
- pause/cancel/edit invalidates old continuation leases;
- queued continuation from an invalidated lease is discarded before model execution;
- terminal transition is idempotent;
- replacement requires explicit supersede/cancel behavior.

This is a correctness boundary, not merely a UI convenience.

## 17. Permissions and security

A Goal is intent, not authority.

Effective authority remains the intersection of:

- user intent;
- OS/host policy;
- workspace scope;
- component capability;
- delegated lease;
- connection grant;
- approval requirements;
- current revocation/expiry.

Goal continuation never bypasses normal tool, filesystem, connection, external-effect or approval checks.

Prompt injection cannot edit Brain Goal state unless an authenticated owner-routed command authorizes it.

Goal text is user data, not higher-priority instruction.

Remote Goal controls require authenticated principal mapping and appropriate operator scope at Gateway.

## 18. Recovery and restart

On restart:

- Brain Goal state is authoritative;
- Gateway reconstructs only a session/run binding and obtains a fresh continuation lease;
- no old in-memory continuation is trusted;
- active does not mean "blindly start work immediately after daemon restart";
- foreground continuation resumes when an eligible session is re-admitted;
- durable background wake occurs only through an explicit Automations wake policy.

A crash after an external side effect but before a local response must use owner/execution receipts and idempotency before retrying the effect.

## 19. Background versus foreground

Starting a Goal authorizes bounded autonomous continuation for that Goal under the current execution policy. It does not create a cron job or standing order.

Default public-beta behavior:

- foreground Goal continuation occurs in the bound Gateway session;
- process/event parking can resume inside the same live host;
- durable cross-restart/background wake requires an explicit registered wake policy;
- Automations stores the trigger/job and references goal_id, but never copies the Goal objective/status;
- destructive or authority-expanding work still requires normal approvals after wake.

## 20. Multiple Bots relationship

Multiple Bots may decompose Goal work into Tasks/Team Runs only when the Goal execution policy permits delegation.

Multiple Bots owns:

- delegated task assignment;
- Worker/Bot lifecycle;
- leases;
- handoffs;
- coordination state.

It does not own:

- Goal objective;
- completion criteria;
- final Goal status;
- Brain verification verdict.

A delegated Task may return evidence to Brain. It may not mark the Brain Goal complete.

## 21. What AI-Verse should not copy

Do not copy:

- a second session-local Goal database in Gateway;
- completion based only on the assistant's last response;
- fail-open verifier errors with no circuit breaker;
- model-only pause semantics;
- unlimited immediate no-progress continuation;
- Goal state as a scheduler/cron substitute;
- task-board state masquerading as Goal state;
- model authority to silently replace/pause/cancel Goals;
- budget exhaustion as success;
- stale queued continuations that survive Goal version changes;
- direct external side-effect retries without receipt/idempotency checks.

## 22. Public-beta acceptance tests

Before Goal mode is public-beta ready, acceptance must prove at least:

1. Goal survives process restart because Brain persisted it.
2. Gateway has no second editable Goal truth.
3. pause prevents every not-yet-started continuation, including an already queued one.
4. stale Goal UI/control requests cannot mutate a replacement.
5. exact control retries are idempotent.
6. editing a Goal invalidates the previous continuation lease.
7. one active session binding cannot accidentally start a second Goal.
8. a budget stop pauses without completing.
9. three identical no-progress attempts cannot produce a fourth automatic turn.
10. wait does not consume model turns while the validated condition is pending.
11. durable wake references the Brain goal_id rather than copying Goal state.
12. deterministic gates cannot expand permission.
13. semantic verifier failure never marks complete.
14. completion requires current evidence for every criterion.
15. delegated Bots can contribute evidence but cannot own/complete the Goal.
16. crash/retry around side effects does not duplicate a verified effect.
17. Goal controls work under the remote authenticated-principal model before remote public exposure.

## 23. Implementation order

1. Brain: add/confirm canonical Goal object, lifecycle, versioning, completion contract and verification record.
2. Brain: expose owner-routed Goal command/query interface with compare-and-set idempotency.
3. Gateway: implement one-session-to-one-goal binding and revocable continuation lease.
4. Gateway: implement bounded continuation, user preemption, pause/cancel race handling and no-progress circuit breaker.
5. Gateway + Brain: implement deterministic gate evidence and Brain semantic verification.
6. Automations: add durable goal_id wake registrations and idempotent wake delivery.
7. Multiple Bots: pass goal_id/evidence references through delegation without copying Brain state.
8. Token: attribute Goal usage/cost where enabled without becoming Goal authority.
9. Distribution/System acceptance: freeze cross-component tests for the failure cases above.
10. Dashboard: project Brain/Gateway state and route controls, never maintain Goal truth.

## 24. Compatibility with current AI-Verse architecture

This contract does not require a new Goals repository.

It strengthens existing intent rather than changing canonical ownership.

The implementation dependencies that do not exist yet are Gateway and Automations. Until those repositories exist, Brain may implement Goal state/verification primitives but AI-Verse cannot claim the full autonomous-continuation contract.

The main architectural caution is that Brain may contain many strategic objectives, while the user-facing Gateway session should bind to at most one active execution Goal at a time. That is a binding rule, not a limitation on Brain's broader strategy model.
