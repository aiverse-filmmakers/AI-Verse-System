# AI-Verse Automations Component Specification

**Status:** CURRENT canonical implementation for local single-user public beta  
**Evidence date:** 2026-09-13  
**Canonical repository:** `aiverse-filmmakers/AI-Verse-Automations`  
**Current evidence head:** `494469a496d479cfec618bcd9511033c0cd3e815`  
**Implementation publication head:** `447310570aba837c1df61b9f87013f7cb7ec062b`  
**Exact implementation tree before evidence-only documentation update:** `0749fdb4259b1d7e28715eb8e367f1642d43db4e`

## 1. Canonical role

AI-Verse Automations is the canonical scheduler, trigger and wake-delivery runtime owner.

It closes the ownership gap left intentionally by OS, Brain and Multiple Bots:

- OS defines scope and the outer permission floor but does not own a universal scheduler;
- Brain decides when cognition is useful but does not own scheduler bookkeeping;
- Multiple Bots accepts automation wakes but does not parse or execute schedules;
- Dashboard is a client/projection layer and does not own automation truth.

The execution shape is:

```text
schedule / normalized event / verified webhook
  -> Automations durable occurrence claim
  -> current definition/version fence
  -> current OS scope + permission evaluation
  -> Brain cognition OR Bot/Team Run OR Gateway owner boundary
  -> bounded owner acknowledgement
  -> Automations run/wake receipt
```

## 2. CURRENT owned state and behavior

Automations currently owns:

- durable automation definitions;
- one-time, interval and timezone-aware five-field cron triggers;
- normalized event and authenticated webhook triggers;
- trigger next-fire state and occurrence identity;
- automation and trigger pause/resume lifecycle;
- run-now;
- definition/version execution fences;
- transactional due-run claims;
- retry/backoff state;
- dead-letter state;
- event replay/idempotency receipts;
- process-owner claim metadata;
- restart recovery state;
- wake invocation identity and bounded acknowledgement receipts;
- component lifecycle state and read-only automation/run projections.

Its canonical scheduler store is component-owned SQLite using WAL and transactional claims.

## 3. Explicit non-ownership

Automations does not own:

- strategic goals, intent, strategy or completion judgment;
- general Memory;
- Skills or capability packages;
- Bot Tasks, Team Runs, Workers or downstream coordination attempts;
- external credentials or connection authorization;
- canonical business Data;
- Gateway session/run truth after wake acceptance;
- OS workspace policy.

A successful wake is a delivery acknowledgement, not an authority transfer.

## 4. Scheduling and occurrence semantics

Supported time triggers are:

- one-time UTC/offset timestamp;
- fixed interval from 60 seconds to one year;
- five-field cron with IANA timezone.

Cron evaluation tests UTC instants in the requested local timezone, avoiding nonexistent spring-forward local times and distinguishing repeated fall-back instants.

Missed recurring schedules coalesce instead of replaying an unbounded outage backlog.

Scheduled occurrence identity is deterministic over automation, trigger and exact scheduled instant. Event/webhook occurrence identity is deterministic over automation, trigger and stable source event ID.

## 5. Authority and revocation

Stored scope/action class is a request, not permission.

Before every delivery attempt, including retry, Automations calls the current OS `scripts/action-permission.mjs` boundary with the exact:

- action class;
- operator/workspace scope;
- immutable request fingerprint.

The permission response must bind back to those values. Missing, malformed or unavailable permission evaluation fails closed.

A workspace pause, policy change or other revocation therefore stops a pending delivery rather than relying on a cached historical allow.

An `approval_required` result is not treated as approval.

## 6. Restart and uncertain effects

Live claims carry a process owner identity.

If a process disappears during downstream delivery, a new scheduler process marks the abandoned delivery `unknown`. It does not automatically replay the wake because the downstream effect may already have happened before acknowledgement was persisted.

Explicit retry preserves the original immutable invocation ID. Retrying an `unknown` run requires operator confirmation that the downstream owner honors that invocation ID idempotently.

This is stronger than timeout-only stale-claim recovery.

## 7. Event and webhook security

Webhook triggers use:

- HMAC-SHA256 signatures;
- bounded timestamp skew;
- stable source event IDs;
- persistent replay receipts;
- payload/source/type binding.

Reusing an event ID with changed semantics is rejected.

Raw bearer credentials are rejected from ordinary target configuration. Secret references use bounded `env:` or `file:` handles.

The built-in public-beta HTTP service is loopback-only. Remote exposure requires an external TLS/authenticated boundary.

## 8. Owner integrations

### Brain

The current Brain adapter invokes `ai-verse-brain run-tick` with the exact scope, trigger type and Automations invocation ID as Brain's idempotency key.

Brain retains cognition/goal/strategy ownership.

### Multiple Bots

The current adapter targets the Phase 3.6 `POST /v1/automations/invoke` receive-side contract.

Because current Multiple Bots still revalidates an OS automation source path/digest, Automations creates an invocation-specific compatibility projection under the allowed OS automation roots. It contains bounded IDs/digests and an explicit projection-only marker, not the recurring prompt, credentials or a second canonical automation definition.

Multiple Bots remains the owner of downstream coordination state.

### Gateway

Automations has a replaceable generic owner wake envelope. It deliberately does not invent Gateway session internals before the canonical Gateway receive-side contract is published.

### Dashboard

Automations exposes read-only status/automation/run projections. Schedule mutation remains local operator CLI in the public-beta threat model.

## 9. Lifecycle contract

The repository implements:

```text
install
setup
status
doctor
enable
disable
update
uninstall
```

Lifecycle commands support structured JSON output.

Setup binds to a real OS permission boundary and detects pre-existing legacy OS automation definitions. If competing legacy definitions are present, execution remains disabled and status becomes `migration-required` rather than silently creating split scheduler authority.

Uninstall preserves canonical scheduler state by default.

## 10. CURRENT acceptance evidence

Local implementation evidence:

- implementation commit: `f38f525769c9ad976e5dd016f8d577fa8a4e8035`;
- exact tested implementation tree: `0749fdb4259b1d7e28715eb8e367f1642d43db4e`;
- **27/27 local tests passed**;
- editable package install and CLI smoke passed.

Hosted publication evidence:

- canonical repository exists and is populated;
- GitHub publication commit `447310570aba837c1df61b9f87013f7cb7ec062b` had the exact tested tree `0749fdb4259b1d7e28715eb8e367f1642d43db4e`;
- GitHub Actions CI run **34777167602** passed **9/9 matrix jobs** across Ubuntu, macOS and Windows on Python 3.11, 3.12 and 3.13;
- current head `494469a496d479cfec618bcd9511033c0cd3e815` is an evidence-only documentation update over that implementation and has its own CI rerun.

## 11. Remaining release/composition work

These are not reasons to move scheduler ownership elsewhere:

- finish the current-head hosted CI rerun after the evidence-only documentation update;
- optionally publish/tag an immutable release artifact when the Distribution version set is frozen;
- replace the generic Gateway target with the canonical versioned Gateway receive-side contract when that repository is published;
- retire the Multiple Bots OS-source compatibility projection when Multiple Bots exposes a direct canonical Automations-owner source contract;
- prove full Agent-profile clean-install/composed acceptance through Distribution.

CURRENT implementation is real and canonical. Immutable release/version-set acceptance remains a separate release gate.
