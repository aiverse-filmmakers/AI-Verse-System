# AI-Verse Automations Source Map

**Status:** CURRENT evidence map  
**Date:** 2026-09-13

## Canonical implementation repository

Repository: `aiverse-filmmakers/AI-Verse-Automations`

Current accepted evidence head: `caaed83b98026dd955640fc015d181529b91a1c6`

Implementation publication head: `447310570aba837c1df61b9f87013f7cb7ec062b`

Exact implementation tree: `0749fdb4259b1d7e28715eb8e367f1642d43db4e`

## Ownership and product contract

- `AUTOMATIONS.yaml`
  - component identity/version;
  - canonical scheduler/trigger/runtime role;
  - explicit owned and non-owned domains;
  - lifecycle command declaration;
  - state-preserving uninstall and separate authority transfer.

- `README.md`
  - public Install -> Setup -> Verify -> Use -> Update/disable/uninstall path;
  - Brain, Multiple Bots and Gateway target configuration;
  - webhook/event usage;
  - recovery UX;
  - explicit setup/non-authority statement.

- `docs/ARCHITECTURE.md`
  - durable occurrence and invocation identity;
  - SQLite/WAL canonical scheduler state;
  - misfire coalescing;
  - transactional claims;
  - process-owner restart recovery;
  - OS permission re-check;
  - Multiple Bots compatibility projection;
  - loopback HTTP threat model.

- `docs/OWNER-CONTRACT.md`
  - stable wake envelope;
  - Brain adapter boundary;
  - Multiple Bots Phase 3.6 translation;
  - Gateway replaceable owner boundary;
  - Dashboard projection relationship.

- `SECURITY.md`
  - scheduler authority/revocation rules;
  - webhook/event replay defenses;
  - secret-reference policy;
  - local HTTP exposure boundary.

## Runtime implementation

- `src/aiverse_automations/db.py`
  - SQLite connection/schema and transaction foundation.

- `src/aiverse_automations/store.py`
  - automation/trigger/run/event persistence;
  - durable claims and state transitions.

- `src/aiverse_automations/schedule.py`
  - one-time, interval and timezone-aware cron evaluation.

- `src/aiverse_automations/engine.py`
  - scheduler tick/claim/delivery/retry/dead-letter/recovery flow;
  - definition/version fences;
  - bounded wake delivery.

- `src/aiverse_automations/authority.py`
  - OS permission-boundary invocation and response binding.

- `src/aiverse_automations/adapters.py`
  - Brain, Multiple Bots and Gateway owner adapters;
  - stable invocation identity propagation.

- `src/aiverse_automations/security.py`
  - secret-reference and transport safety helpers.

- `src/aiverse_automations/webhook.py`
  - HMAC/timestamp/replay validation.

- `src/aiverse_automations/service.py`
  - local scheduler service;
  - loopback webhook ingress;
  - read-only HTTP projections.

- `src/aiverse_automations/lifecycle.py`
  - setup/readiness/state-preserving lifecycle behavior;
  - legacy automation migration-required detection.

- `src/aiverse_automations/cli.py`
  - lifecycle and operator command surface;
  - structured output.

## Acceptance tests

- `tests/test_engine.py`
  - due dispatch, concurrency, retry/dead-letter and execution fences.

- `tests/test_schedule.py`
  - schedule/cron behavior and time semantics.

- `tests/test_events.py`
  - event source/type binding and replay behavior.

- `tests/test_webhook_security.py`
  - webhook HMAC/timestamp/replay protection.

- `tests/test_recovery.py`
  - process-owner recovery and explicit uncertain retry.

- `tests/test_authority_integration.py`
  - real OS permission subprocess boundary and re-check.

- `tests/test_lifecycle.py`
  - shared lifecycle, preservation and migration-required behavior.

- `tests/test_public_beta.py`
  - public-beta owner adapter/contract cases.

- `tests/test_http_safety.py`
  - loopback exposure restrictions.

- `.github/workflows/ci.yml`
  - Ubuntu/macOS/Windows;
  - Python 3.11/3.12/3.13;
  - install, compile, pytest and CLI smoke.

## Sibling evidence that constrained implementation

### AI-Verse OS

- `automations/README.md`
- `automations/jobs/README.md`
- `automations/triggers/README.md`
- `automations/policies/README.md`
- `scripts/action-permission.mjs`
- `system/architecture/action-permissions.md`

These establish Cadence architecture and OS authority while explicitly not proving a universal scheduler runtime.

### AI-Verse Brain

- `engine/aiverse_brain/cadence.py`
- `engine/aiverse_brain/cadence_plan.py`
- `engine/aiverse_brain/cadence_hooks.py`
- `protocol/INTEGRATION-CADENCE.md`
- `engine/aiverse_brain/cli.py`

These establish that Brain requests cadence but does not own scheduling and supports idempotent `run-tick` invocation.

### AI-Verse Multiple Bots

- `src/automation-wake-ingress.ts`
- `test/automation-wake-ingress.test.ts`
- `docs/AI-VERSE-AUTOMATION-WAKE-SCHEDULE.md`

These establish the current Phase 3.6 receive-side wake contract, source binding, idempotency and non-scheduler ownership.

### AI-Verse Dashboard

- `packages/protocol/src/methods.ts`

This records future `cron.*` query/command names while the Dashboard remains a non-canonical client.

## Benchmark provenance

Repository record:

- `docs/RESEARCH.md`

The implementation synthesized mature patterns from Hermes cron/heartbeat, OpenClaw schedules/hooks, Letta scheduled continuation and durable execution systems. The adopted laws are deterministic scheduler bookkeeping outside model cognition, durable claims, stable idempotency identity, explicit uncertainty handling and no cached authority.

---

## 2026-09-14 Invisible Intelligence superseding evidence

Current owner evidence after the original implementation audit:

- `53ab6a79a07f99f7e0e357a9c78337926823d96d` - atomic consented Automation definition creation;
- `caaed83b98026dd955640fc015d181529b91a1c6` - safe Automations OS extension-owner bridge;
- registry locks are never stolen and explicit disabled state is preserved on reattach;
- Distribution frozen Agent acceptance proves whole-profile Automations composition;
- Invisible Intelligence G/H run `34890857872` proves recommendation leaves canonical recurring state empty and direct recurring consent reaches the Automations owner.

The frozen Agent release ref remains historical release truth; this newer head is CURRENT post-release evidence for a future candidate.
