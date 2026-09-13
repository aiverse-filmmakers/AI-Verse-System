# AI-Verse Public Beta Tracker

**Status:** Live execution tracker  
**Updated:** 2026-09-13  
**Target:** First complete **Agent public beta** unless explicitly widened.

This file tracks execution state only. Architectural law remains in the Final Blueprint and public-beta contracts.

## Target profile

The first Agent public beta is:

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

Connections is not currently an Agent-profile blocker. Dashboard and Apps are not Agent-profile blockers.

## Current execution board

| Area | Current evidence | State | Next action |
|---|---|---|---|
| System contracts | Goals, Self-Learning, Install/Setup, Public Beta plan exist | READY | Keep tracker/blueprint current |
| OS | main `a1e11b8...`; PR #25 merged; all 8 post-merge workflows green | PUBLIC-BETA REPO TARGET DONE | Freeze exact ref for final Agent manifest |
| Brain | main `80019be...`; PR #18 merged; post-merge CI + ownership/Skills contract workflows green | PUBLIC-BETA REPO TARGET DONE | Freeze exact ref and use in composed Goal continuation acceptance |
| Memory | PR #9 merged; public-beta acceptance 12/12 jobs passed across Linux/macOS/Windows | PUBLIC-BETA IMPLEMENTATION READY | Freeze/reference exact release artifact in final manifest |
| Skills | PR #8 merged; Runtime Readiness, Validate Skills, Full E2E all green | PUBLIC-BETA IMPLEMENTATION READY | Freeze/reference exact release artifact in final manifest |
| Data | `189b132...`; canonical five-component release hardening frozen | READY FOR CURRENT TARGET | Do not reopen absent a real regression |
| Multiple Bots | Phase 5.6 merged as `2db3fb4...`; CI green; Phase 5 ~30% | IN PROGRESS | Phase 5.7 upgrade/migration, then 5.8-5.14 sequentially |
| Gateway | public repo main `b20d56e...`; hosted CI green | PUBLIC-BETA REPO TARGET DONE | Final composed Goal/runtime acceptance only |
| Automations | public repo main `494469a...`; hosted CI green | PUBLIC-BETA REPO TARGET DONE | Final composed wake/delivery acceptance only |
| Token | beta.3 main `23b7b8e...`; stale beta.2 assertion fixed; hosted CI run #31 green | PUBLIC-BETA REPO TARGET DONE | Freeze exact beta.3 ref/tag for Agent manifest |
| Connections | PR #1 merged as `baaac641...`; v1 implementation exists; private-repo CI jobs fail before step 1 | IMPLEMENTED, REMOTE CI UNPROVEN | Fix Actions runner availability or run equivalent release proof; not Agent blocker |
| Distribution | PR #1 open at `d363c40...`; companion Data dependency lock is implemented; Unit/Core jobs still terminate before step 1 on private-repo runners | IMPLEMENTATION NEARLY DONE, ACCEPTANCE INFRA BLOCKED | Get real Core clean-machine execution green, refresh stale Agent blocker docs, merge PR #1 |
| Dashboard | Phase 2 Task 5 current | POST-AGENT-BETA | Do not use as current release blocker |
| Apps | architecture seed only | POST-AGENT-BETA | Do not use as current release blocker |

## Immediate critical path

1. Finish Multiple Bots Phase 5.7 through 5.14 sequentially.
2. Finish Distribution PR #1: execute real Core clean-machine acceptance, refresh stale Agent blocker evidence, and merge.
3. Freeze exact immutable refs for OS, Brain, Memory, Skills, Data, Gateway, Automations, Multiple Bots and Token.
4. Promote the complete Agent release set in Distribution only when every required ref is accepted.
5. Run the canonical final public-beta acceptance matrix across the composed Agent profile.
6. Fix only genuine PUBLIC-BETA BLOCKER findings in their owning repositories.
7. Freeze the final manifest and declare PUBLIC BETA READY only if the matrix passes.

## Known CI infrastructure issue

Current private repositories `AI-Verse-Connections` and `ai-verse-distribution` have GitHub Actions matrix jobs that terminate before executing step 1. This is not evidence that their tests failed in code; remote runner availability must be resolved or equivalent release evidence supplied.

By contrast, public repositories including Brain, Memory, Skills, Multiple Bots and Token are receiving hosted runners.

## Stop rule

Do not reopen already-passed components for hypothetical improvements.

After the Agent acceptance gate passes on immutable refs, new ideas belong to the next release unless they expose a real security, data-loss, authority/isolation, install, compatibility or acceptance regression.
