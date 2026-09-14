# Agent Distribution Release — 2026-09-14

**Status:** RELEASED AND ACCEPTED  
**Release set:** `agent-public-beta-2026-09-14`  
**Distribution merge:** `19150267b28fc41ee012495cabf7b5148e7a81f4`

This document is the canonical System evidence record for the completed Agent Distribution release. Any older execution-plan language saying that Agent Distribution is blocked, that Multiple Bots Phase 5.10-5.14 is incomplete, or that composed Agent acceptance is still outstanding is historical and superseded by this evidence and `PUBLIC-BETA-TRACKER.md`.

## Exact immutable release set

| Component | Accepted revision |
|---|---|
| AI-Verse OS | `d961ef8e2422d6f713d6519cf5a48916c600d63a` |
| AI-Verse Brain | `619dd17daac9c1bd7eaf4381a5889e56ab05ec59` |
| AI-Verse Memory | `031e1e77c97ed3c9012235c7ffe0a4ece05e3695` |
| AI-Verse Skills | `042fda1ea2ddd8b79b74f1db9d3f65212953b64a` |
| AI-Verse Data | `189b13264ab86115d2f21fee3ba8cd5a8dac6581` |
| AI-Verse Gateway | `240c2b1b71abc7a8dbdc4d573da7fd85a110ca8f` |
| AI-Verse Automations | `494469a496d479cfec618bcd9511033c0cd3e815` |
| AI-Verse Multiple Bots | `9bffdffd07fb8abcea848213642936a23ecf4ecf` |
| AI-Verse Token | `23b7b8ecbc9d9ef267f5e10449f785eb11107dd4` |

## Qualification evidence

Frozen implementation qualification head:

`a4f9ee17b65cddef8d7547115cca34738a41b3fe`

- Distribution CI run `34852469436`
- Core clean-machine regression run `34852470941`
- Agent clean-machine acceptance run `34852469415`
  - Ubuntu `104004060260`
  - macOS `104004060743`
  - Windows `104004060677`

## Final exact-head pre-merge evidence

Final evidence-only PR head:

`775a5a49c6a861dd8ff8aad525b69c33ee02dd06`

All required matrices passed again on that exact head:

- Distribution CI `34853174986`: 6/6 green
- Core clean-machine `34853174887`: 3/3 green
  - Ubuntu `104006455753`
  - macOS `104006455798`
  - Windows `104006455747`
- Agent clean-machine `34853174857`: 3/3 green
  - Ubuntu `104006432884`
  - macOS `104006432362`
  - Windows `104006432569`

## Merge and post-merge evidence

Distribution PR #2 merged as:

`19150267b28fc41ee012495cabf7b5148e7a81f4`

Post-merge Distribution CI run `34854358450` passed 6/6:

- Ubuntu Python 3.9 `104009939643`
- Ubuntu Python 3.12 `104009939690`
- macOS Python 3.9 `104009939525`
- macOS Python 3.12 `104009939431`
- Windows Python 3.9 `104009939129`
- Windows Python 3.12 `104009939539`

## Acceptance scope

The clean-machine Agent gate proved:

- immutable install and setup;
- onboarding/status/doctor;
- bounded loopback Gateway run;
- canonical Brain Goal ownership/evaluation;
- Gateway restart/recovery;
- Memory recall;
- immutable Skills invocation;
- Data create/read;
- two durable Multiple Bots collaborating and surviving restart;
- Automations bounded wake delivery into Multiple Bots;
- Token collection/projection;
- supported lifecycle operations with state preservation;
- same-release update/rollback behavior;
- exact source verification and no hidden tracked-source edits.

## Ownership law preserved

Distribution grants no permissions and owns no component domain truth.

- Brain owns goals, strategy and evaluation.
- Automations owns schedules, triggers and cadence runtime.
- Token owns canonical normalized telemetry evidence, immutable usage accounting, pricing evidence and ACTUAL/CALCULATED/UNKNOWN cost truth.
- Multiple Bots owns coordination-local operational budgets/counters only; its usage/cost surfaces are projection/execution evidence, not a competing canonical Token ledger.
- Gateway remains loopback/default and was not remotely exposed by Distribution.
- No unspecified workspace initialization or silent Brain strategic handover is admitted.

## Boundary

This closes the **Agent Distribution release** only.

It does not claim completion of the separate independent final whole-system PUBLIC-BETA audit, and it does not start Full-profile work.
