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
| OS | main `9600929...`; PR #25 public-beta closure merged, PR #26 Windows Data-host fix merged; current post-merge workflows green | PUBLIC-BETA REPO TARGET DONE | Use latest accepted ref in Distribution/final manifest |
| Brain | main `80019be...`; PR #18 merged; post-merge workflows green | PUBLIC-BETA REPO TARGET DONE | Freeze exact ref for final manifest |
| Memory | PR #9 merged; public-beta acceptance 12/12 jobs passed across Linux/macOS/Windows | PUBLIC-BETA IMPLEMENTATION READY | Freeze/reference exact release artifact in final manifest |
| Skills | PR #8 merged; Runtime Readiness, Validate Skills, Full E2E all green | PUBLIC-BETA IMPLEMENTATION READY | Freeze/reference exact release artifact in final manifest |
| Data | `189b132...`; canonical five-component release hardening frozen | READY FOR CURRENT TARGET | Do not reopen absent a real regression |
| Multiple Bots | Phase 5.9 merged as `6033efd...`; CI green; Phase 5.10 is next | IN PROGRESS | Finish 5.10 channel bridges, 5.11 approvals UX, 5.12 observability, 5.13 release docs, 5.14 final acceptance |
| Gateway | public repo main `b20d56e...`; hosted CI green | PUBLIC-BETA REPO TARGET DONE | Final composed Goal/runtime acceptance only |
| Automations | public repo main `494469a...`; hosted CI green | PUBLIC-BETA REPO TARGET DONE | Final composed wake/delivery acceptance only |
| Token | beta.3 main `23b7b8e...`; hosted CI green | PUBLIC-BETA REPO TARGET DONE | Freeze exact beta.3 ref/tag for Agent manifest |
| Connections | PR #1 merged as `baaac641...`; v1 implementation exists; private-repo CI jobs fail before step 1 | IMPLEMENTED, REMOTE CI UNPROVEN | Fix Actions runner availability or run equivalent release proof; not Agent blocker |
| Distribution | PR #1 merged as `116aa2d...`; Core release `core-public-beta-2026-09-13`; final-head CI `34782949282` green 6/6; Core clean-machine `34782949287` green on Ubuntu/macOS/Windows | CORE DISTRIBUTION ACCEPTED | Keep Agent blocked until Multiple Bots remaining Phase 5 slices finish and the complete immutable Agent set passes composed acceptance |
| Dashboard | Phase 2 Task 5 current | POST-AGENT-BETA | Do not use as current release blocker |
| Apps | architecture seed only | POST-AGENT-BETA | Do not use as current release blocker |

## Accepted Core Distribution evidence

The canonical Core Distribution/meta-installer is accepted.

- Distribution merge: `116aa2d74bb55c4ee00bf6139e98bb345b516b8a`
- accepted release set: `core-public-beta-2026-09-13`
- OS: `9600929b946746c25c64e48471fcc83031fddda9`
- Brain: `80019be5e6df29aee70371544bd96cedbf0329b9`
- Memory: `031e1e77c97ed3c9012235c7ffe0a4ece05e3695`
- Skills: `042fda1ea2ddd8b79b74f1db9d3f65212953b64a`
- Data: `189b13264ab86115d2f21fee3ba8cd5a8dac6581`
- Distribution final-head CI: run `34782949282`, 6/6 green across Ubuntu/macOS/Windows and Python 3.9/3.12
- Core clean-machine acceptance: run `34782949287`
  - Ubuntu: job `103793852607` green
  - macOS: job `103793852290` green
  - Windows: job `103793852407` green

This accepts the Core one-product install/setup/onboard/status/doctor/use lifecycle, immutable source verification, deterministic Data companion-lock packaging, state-preserving component lifecycle, and cross-platform clean-machine behavior. It does not release the Agent profile.

## Immediate critical path

1. Finish Multiple Bots Phase 5.10 through 5.14 sequentially.
2. Freeze the final accepted Multiple Bots ref alongside the already accepted OS, Brain, Memory, Skills, Data, Gateway, Automations and Token refs.
3. Promote the complete Agent release set in Distribution only when every required ref is accepted.
4. Run the canonical final public-beta acceptance matrix across the composed Agent profile.
5. Fix only genuine PUBLIC-BETA BLOCKER findings in their owning repositories.
6. Freeze the final Agent manifest and declare PUBLIC BETA READY only if the matrix passes.

## Known CI infrastructure issue

The remaining recorded runner-availability issue applies to `AI-Verse-Connections`, whose earlier private-repository jobs terminated before executing step 1. Distribution is public and its required hosted matrices now execute and pass.

By contrast, public repositories including Brain, Memory, Skills, Multiple Bots and Token are receiving hosted runners.

## Stop rule

Do not reopen already-passed components for hypothetical improvements.

After the Agent acceptance gate passes on immutable refs, new ideas belong to the next release unless they expose a real security, data-loss, authority/isolation, install, compatibility or acceptance regression.
