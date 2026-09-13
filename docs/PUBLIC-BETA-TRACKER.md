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
| OS | PR #25 `653f2c3...`; all 8 hosted workflows green | PUBLIC-BETA CANDIDATE READY TO MERGE | Review/merge PR #25, then freeze exact ref |
| Brain | PR #18 `b4cf39b...`; 3/3 workflows green; draft/open | IMPLEMENTED, RELEASE CLOSURE IN PROGRESS | Finish acceptance/release docs/artifact pinning, merge |
| Memory | PR #9 merged; public-beta acceptance 12/12 jobs passed across Linux/macOS/Windows | PUBLIC-BETA IMPLEMENTATION READY | Freeze/reference exact release artifact in final manifest |
| Skills | PR #8 merged; Runtime Readiness, Validate Skills, Full E2E all green | PUBLIC-BETA IMPLEMENTATION READY | Freeze/reference exact release artifact in final manifest |
| Data | `189b132...`; canonical five-component release hardening frozen | READY FOR CURRENT TARGET | Do not reopen absent a real regression |
| Multiple Bots | Phase 5.5 merged; CI green; Phase 5 ~25%, overall directional ~95% | IN PROGRESS | Phase 5.6 production doctor, then 5.7-5.14 |
| Gateway | canonical public repo exists; main `b20d56e...`; hosted CI run #1 green | PUBLIC-BETA IMPLEMENTATION CANDIDATE READY | After Brain merge, run composed Goal-continuation acceptance and freeze exact ref |
| Automations | canonical public repo exists; main `494469a...`; hosted CI green | PUBLIC-BETA IMPLEMENTATION CANDIDATE READY | Run final composed wake/delivery acceptance with OS/Gateway/Bots and freeze exact ref |
| Token | beta.3 main `193a9ae...`; hosted CI reaches all six legs but fails one stale CLI-help version assertion expecting beta.2 | NEARLY READY | Update stale test to beta.3, rerun six-leg CI, then freeze/tag release |
| Connections | PR #1 merged as `baaac641...`; v1 implementation exists; private-repo CI jobs fail before step 1 | IMPLEMENTED, REMOTE CI UNPROVEN | Fix Actions runner availability or run equivalent release proof; not Agent blocker |
| Distribution | PR #1 open at current head; implementation exists; current Unit/Core jobs terminate before step 1 on private-repo hosted runners | IMPLEMENTED, ACCEPTANCE INFRA BLOCKED | Restore runner availability or make repo public if intended; get Core clean-machine gate green, then admit exact Agent refs |
| Dashboard | Phase 2 Task 5 current | POST-AGENT-BETA | Do not use as current release blocker |
| Apps | architecture seed only | POST-AGENT-BETA | Do not use as current release blocker |

## Immediate critical path

1. Review/merge OS PR #25; all eight current hosted workflows are green.
2. Finish Brain PR #18 release closure and merge it.
3. Finish Multiple Bots Phase 5.6 through 5.14 sequentially.
4. Fix Token beta.3's stale CLI-help version assertion and rerun the six-leg matrix.
5. Run composed Brain Goal continuation through the now-published Gateway and freeze Gateway's exact ref.
6. Run composed Automations wake/delivery acceptance with current owner boundaries and freeze its exact ref.
7. Get Distribution Core CI/clean-machine acceptance actually running and green.
8. Add exact Agent component refs to Distribution and run Agent clean-machine acceptance.
9. Run the canonical final public-beta acceptance matrix.
10. Freeze immutable refs and declare PUBLIC BETA READY only if the matrix passes.

## Known CI infrastructure issue

Current private repositories `AI-Verse-Connections` and `ai-verse-distribution` have GitHub Actions matrix jobs that terminate before executing step 1. This is not evidence that their tests failed in code; remote runner availability must be resolved or equivalent release evidence supplied.

By contrast, public repositories including Brain, Memory, Skills, Multiple Bots and Token are receiving hosted runners.

## Stop rule

Do not reopen already-passed components for hypothetical improvements.

After the Agent acceptance gate passes on immutable refs, new ideas belong to the next release unless they expose a real security, data-loss, authority/isolation, install, compatibility or acceptance regression.
