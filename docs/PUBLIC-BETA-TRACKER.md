# AI-Verse Public Beta Tracker

**Status:** Agent Distribution release complete; Invisible Intelligence candidate qualified; independent whole-system public-beta audit is now the active pre-dogfood gate  
**Updated:** 2026-10-05
**Target:** First complete **Agent public beta** unless explicitly widened.

This file tracks execution state only. Architectural law remains in the Final Blueprint and public-beta contracts.

## Independent whole-system audit gate

Before real Mission Control MC1.4 integration proof or broader owner dogfood, execute the canonical audit program:

- `docs/public-beta-audit/PROGRAM-2026-09-15.md`
- `docs/public-beta-audit/EXECUTION-TRACKER-2026-09-15.md`
- `docs/public-beta-audit/EVIDENCE-FINDING-PROTOCOL.md`
- `docs/public-beta-audit/RELATIONSHIP-MATRIX-PROTOCOL.md`

The audit begins at A0.1 and is intentionally read-only against product repositories until the whole-system synthesis and repair program are complete. Existing accepted Agent release evidence remains historical/release evidence to be independently revalidated, not automatically trusted as audit proof.


## Target profile

The released Agent Distribution profile is:

- AI-Verse OS
- AI-Verse Brain
- AI-Verse Memory
- AI-Verse Skills
- AI-Verse Data
- AI-Verse Gateway
- AI-Verse Automations
- AI-Verse Multiple Bots
- AI-Verse Token
- ai-verse-distribution

Connections is not an Agent-profile blocker. Dashboard and Apps are not Agent-profile blockers. Full-profile work is not part of this release.

## Current execution board

| Area | Current evidence | State | Next action |
|---|---|---|---|
| System contracts | Goals, Self-Learning, Install/Setup and Public Beta contracts exist | READY | Keep tracker/blueprint current |
| OS | Context Ladder candidate ref `924a21a3dc1094d0fb6cc422f55fdfc714634e4d`; accepted release-set evidence | CURRENT CANDIDATE ACCEPTED | Preserve exact release-set identity |
| Brain | Context Ladder candidate ref `6f986e8d06c7f9c069fbf05aa92ae7b7a1af9bf4` | CURRENT CANDIDATE ACCEPTED | Preserve exact release-set identity |
| Memory | Context Ladder candidate ref `406b14fb4398eb1b16dd5f30e50520e8c3540972` | CURRENT CANDIDATE ACCEPTED | Preserve exact release-set identity |
| Skills | Context Ladder candidate ref `71264af6b2b9a575812fe18858d75a54ea2ff545` | CURRENT CANDIDATE ACCEPTED | Preserve exact release-set identity |
| Data | Context Ladder candidate ref `8edde7dca5afa34e300130cc6b8ee2b4170ad40f` with companion dependency lock | CURRENT CANDIDATE ACCEPTED | Preserve exact release-set identity |
| Gateway | Context Ladder candidate ref `46c15ee58b028dd7fb8b310327ea705ef618805e`; composed owner path accepted | CURRENT CANDIDATE ACCEPTED | Preserve exact release-set identity |
| Automations | Context Ladder candidate ref `caaed83b98026dd955640fc015d181529b91a1c6` | CURRENT CANDIDATE ACCEPTED | Preserve exact release-set identity |
| Multiple Bots | Context Ladder candidate ref `c600e2bc014351a61e1c0e2673fc63f5d5fa54ec` | CURRENT CANDIDATE ACCEPTED | Preserve exact release-set identity |
| Token | `23b7b8ecbc9d9ef267f5e10449f785eb11107dd4` (`0.1.0-beta.3`); collection/projection accepted | CURRENT CANDIDATE ACCEPTED | Preserve Token as canonical normalized telemetry/pricing/cost truth |
| Distribution | PR #2 immutable Agent release remains default; PR #7 `a215c8777da55b299247ec9e564cca020cfe2020` freezes the explicit-only Invisible Intelligence candidate | AGENT RELEASE + NEXT CANDIDATE ACCEPTED | Keep cross-release transition closed until Safe Update admits it |
| Connections | Separate implementation track; not an Agent Distribution blocker | OUTSIDE THIS RELEASE | Handle independently |
| Dashboard | Separate UI track | POST-AGENT-DISTRIBUTION | Do not use as retroactive release blocker |
| Apps | Separate app/runtime track | POST-AGENT-DISTRIBUTION | Do not use as retroactive release blocker |

## Accepted Agent Distribution evidence

Canonical release set:

`agent-public-beta-2026-09-14`

Exact immutable component refs for the accepted Context Ladder candidate `agent-context-ladder-rc1-2026-09-15`:

- OS: `924a21a3dc1094d0fb6cc422f55fdfc714634e4d`
- Brain: `6f986e8d06c7f9c069fbf05aa92ae7b7a1af9bf4`
- Memory: `406b14fb4398eb1b16dd5f30e50520e8c3540972`
- Skills: `71264af6b2b9a575812fe18858d75a54ea2ff545`
- Data: `8edde7dca5afa34e300130cc6b8ee2b4170ad40f`
- Gateway: `46c15ee58b028dd7fb8b310327ea705ef618805e`
- Automations: `caaed83b98026dd955640fc015d181529b91a1c6`
- Multiple Bots: `c600e2bc014351a61e1c0e2673fc63f5d5fa54ec`
- Token: `23b7b8ecbc9d9ef267f5e10449f785eb11107dd4`

Qualification evidence frozen in the Distribution manifest:

- qualification head: `a4f9ee17b65cddef8d7547115cca34738a41b3fe`
- Distribution CI: run `34852469436`
- Core clean-machine regression: run `34852470941`
- Agent clean-machine acceptance: run `34852469415`
  - Ubuntu: job `104004060260`
  - macOS: job `104004060743`
  - Windows: job `104004060677`

Final evidence-only exact-head rerun before merge:

- head: `775a5a49c6a861dd8ff8aad525b69c33ee02dd06`
- Distribution CI: run `34853174986`, 6/6 green
- Core clean-machine regression: run `34853174887`
  - Ubuntu: job `104006455753` green
  - macOS: job `104006455798` green
  - Windows: job `104006455747` green
- Agent clean-machine acceptance: run `34853174857`
  - Ubuntu: job `104006432884` green
  - macOS: job `104006432362` green
  - Windows: job `104006432569` green

Merge and post-merge evidence:

- Distribution PR #2 merge: `19150267b28fc41ee012495cabf7b5148e7a81f4`
- post-merge Distribution CI: run `34854358450`, 6/6 green
  - Ubuntu Python 3.9: job `104009939643`
  - Ubuntu Python 3.12: job `104009939690`
  - macOS Python 3.9: job `104009939525`
  - macOS Python 3.12: job `104009939431`
  - Windows Python 3.9: job `104009939129`
  - Windows Python 3.12: job `104009939539`

## What the Agent gate proved

The clean-machine release gate proved the complete Distribution-owned composition path without stealing component ownership:

- clean immutable Agent install and setup;
- onboarding, status and doctor;
- loopback-only Gateway bounded run;
- canonical Brain Goal ownership and evaluation;
- Gateway restart/recovery;
- Memory recall;
- immutable Skills invocation;
- structured Data create/read;
- two durable Multiple Bots collaborating and surviving restart;
- Automations delivering a bounded wake into Multiple Bots owner ingress;
- Token collection and projection;
- supported disable/enable and Agent component uninstall/reinstall;
- canonical state preservation;
- owner update lifecycle and same-release rollback behavior;
- exact source verification and no hidden tracked-source edits.

## Authority boundaries preserved

The accepted Agent Distribution release does not grant permissions, transfer Brain strategy ownership, initialize unspecified workspaces, or expose Gateway remotely.

Brain remains canonical for goals/strategy/evaluation. Automations remains canonical for cadence/schedules/triggers. Token remains canonical for normalized telemetry evidence, immutable usage accounting, pricing evidence and ACTUAL/CALCULATED/UNKNOWN cost truth. Multiple Bots owns operational coordination budgets/counters only and treats usage/cost as projection/execution evidence rather than a second canonical Token ledger.

## Post-release CURRENT Invisible Intelligence evidence

The immutable `agent-public-beta-2026-09-14` release above remains unchanged. The following evidence is later same-day implementation and acceptance intended for a **new** future Agent candidate, not a retroactive mutation of the frozen release.

Accepted post-release Distribution merges:

- product-level one-action bootstrap, PR #3: `68d08a432739deeaff3fe3f7915b7fe9abf7e686`
- bounded deterministic self-heal, PR #4: `52a86075a36df9c541d750f021d21cad3311f8c7`
- scenarios A-F gate, PR #5: `7ff5e58fa03e80e541c87bd3f3f319149ccb3fe6`
- scenarios G-M gate, PR #6: `f89bcae9429ef40128c3c0496993a2d502215d19`

Current accepted owner evidence used by the cross-repo scenario gates:

- Gateway: `7627df658b2071ecb4ea242572343edfb7abf768`
- OS: `156f15f162c6d63159b54d3ad87e0342ec7cf9aa`
- Skills: `71264af6b2b9a575812fe18858d75a54ea2ff545`
- Data: `8edde7dca5afa34e300130cc6b8ee2b4170ad40f`
- Automations: `caaed83b98026dd955640fc015d181529b91a1c6`
- Multiple Bots: `c600e2bc014351a61e1c0e2673fc63f5d5fa54ec`

Accepted product behavior now includes:

- `aiverse start` as the ordinary Agent first-run path over exact released components;
- progressive first value without a mandatory deep subsystem questionnaire;
- bounded deterministic self-heal only for the exact released OS/Brain owner repair that passes a strict plan allowlist;
- automatic safe workspace organization and owner-routed Memory/Skills/Data organization;
- low-risk Skills learning through immutable candidate/eval/promotion gates;
- dangerous/secret Skill quarantine and explicit destructive Data migration boundaries;
- recurring-responsibility recommendation without silent Automation creation;
- direct recurring requests routed through the canonical Automations owner;
- durable Bot creation only from explicit/direct consent;
- bounded automatic temporary Workers without durable promotion;
- ordinary outcome language without subsystem-choice jargon;
- restart-safe idempotent replay and no silent authority expansion.

Cross-repo acceptance evidence:

- A-F: run `34890195270`, 2/2 scenario jobs green;
- G-M: run `34890857872`, 2/2 scenario jobs green;
- associated Distribution/Core/Agent regressions remained green across Ubuntu, macOS and Windows.

This CURRENT implementation evidence is now frozen into a separate qualified candidate:

`agent-invisible-intelligence-rc1-2026-09-14`

Distribution PR #7 merged at `a215c8777da55b299247ec9e564cca020cfe2020` from exact qualification head `d2f47297bace2a3afe4d13fac928025dee982246`.

Exact candidate refs:

- OS: `156f15f162c6d63159b54d3ad87e0342ec7cf9aa`
- Brain: `16c0b7ea32fcb4759cfb8368876b6985016eab68`
- Memory: `1c6acf036d42937e57d94dfe48ac501727861653`
- Skills: `71264af6b2b9a575812fe18858d75a54ea2ff545`
- Data: `8edde7dca5afa34e300130cc6b8ee2b4170ad40f`
- Gateway: `7627df658b2071ecb4ea242572343edfb7abf768`
- Automations: `caaed83b98026dd955640fc015d181529b91a1c6`
- Multiple Bots: `c600e2bc014351a61e1c0e2673fc63f5d5fa54ec`
- Token: `23b7b8ecbc9d9ef267f5e10449f785eb11107dd4`

Final candidate qualification:

- Distribution CI: `34900045849`, 6/6 green;
- Core clean-machine: `34900045847`, Ubuntu/macOS/Windows green;
- original Agent regression: `34900045982`, Ubuntu/macOS/Windows green;
- candidate clean-machine: `34900045944`, Ubuntu/macOS/Windows green;
- scenarios A-F: `34900045856`, green;
- scenarios G-M: `34900045862`, green.

The candidate is deliberately not the default Agent channel. `agent-public-beta-2026-09-14` remains unchanged and default. Old -> candidate update and candidate -> old rollback are not admitted; candidate acceptance proves both fail closed. Same-candidate update/rollback remains a safe no-op. This is intentionally compatible with, but does not complete, the separate Safe Update / Release Train project.

## Release boundary

**Agent Distribution is released and accepted.**

This tracker does **not** claim that the separate independent final whole-system PUBLIC-BETA audit has been run. That audit is now the active pre-dogfood gate and is governed by `docs/public-beta-audit/PROGRAM-2026-09-15.md`. It does not retroactively invalidate the completed Agent Distribution release; it independently challenges the current whole system before further dogfood.

## Stop rule

Do not reopen this accepted release for hypothetical improvements. New work belongs to the next release unless it exposes a real security, data-loss/corruption, authority/isolation, install/setup, current-generation compatibility or acceptance regression.
