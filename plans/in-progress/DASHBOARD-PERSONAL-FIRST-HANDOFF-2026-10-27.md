# Dashboard — Personal-first delivery and guided connections

**Date:** 27 October 2026
**Status:** proposed cross-repo amendment; detailed Dashboard plan is in draft PR #41. No runtime, release or acceptance promotion.
**Detailed implementation owner:** AI-Verse-Dashboard. System owns this coordination summary, not a competing task ledger.

## 1. Problem and boundary

The operator wants a clean, beginner-friendly Personal OS first, with chat always present across app navigation. Filmmaking builds on the same conversations, capabilities, app actions and usage presentation. General chat does not require a workspace or a workflow container. Workspaces may be created manually or automatically when a substantial scope is clear, without expanding permissions.

Mission Control remains a proven integration reference and reusable source of operational features. Selective reuse/custom presentation is the proposed replacement for full visible-shell adoption. Preserve the accepted MC0/MC1 proof, provenance and feature inventory. Earlier System product-intent/full-shell text remains the accepted historical baseline until this amendment and Dashboard gate reconciliation are reviewed; this summary does not silently override it.

## 2. Existing path and smallest change

- [Detailed Dashboard plan, exact published revision](https://github.com/aiverse-filmmakers/AI-Verse-Dashboard/blob/c28b2ec06a8699a61ba2f2961369ddff217a19a9/docs/CANONICAL-MISSION-CONTROL-ADOPTION-PLAN-2026-09-15.md)
- [Dashboard review PR #41](https://github.com/aiverse-filmmakers/AI-Verse-Dashboard/pull/41)
- [Provider UX / Connections handoff](https://github.com/aiverse-filmmakers/AI-Verse-Dashboard/blob/c28b2ec06a8699a61ba2f2961369ddff217a19a9/docs/CONNECTIONS-UX-HANDOFF-2026-10-27.md)
- [MC2.1 transport contract and explicit amendment gaps](https://github.com/aiverse-filmmakers/AI-Verse-Dashboard/blob/c28b2ec06a8699a61ba2f2961369ddff217a19a9/docs/MC2.1-AIVERSE-GATEWAY-CLIENT-CONTRACT-2026-10-26.md)

Reuse existing Dashboard client/protocol/registry/live packages and canonical Gateway. Do not rebuild Gateway or add another session/credential/domain store. Bounded app awareness describes the open app, scope and selection; it is not unrestricted screen capture. Manual and agent canvas edits use the same typed, permission-checked actions with revision/idempotency, undo and cancellation.

### Beginner connection experience

One Connections area with AI assistants, creative tools and apps/tools. Entry is also available directly from chat or a relevant creation tool. Explain each provider before asking for setup:
- **ChatGPT:** connect an eligible ChatGPT account to chat and work with AI; models/usage depend on the admitted route and plan.
- **OpenRouter:** models such as GPT, Claude and Gemini through one account; credits/pay for usage, not a promise of every model.
- **KIE.ai:** images, videos and music through one account and credit balance.
- **Higgsfield API:** image/video creation through its supported API account.
- **Apps & tools:** connect existing apps, plugins and MCP-backed capabilities without requiring users to learn the protocol name.

Where supported, browser sign-in returns directly to AI-Verse. For API keys, the operator requests familiar provider entry wording, then a small masked key field, official account/key links, short steps and a connect/check action. Explain the actual method honestly inside the dialog; saved key does not mean verified identity/readiness. Handle invalid/revoked/expired/cancelled/unavailable/insufficient-funds states, replace and disconnect. No terminal or environment-variable setup in the ordinary journey. No paid generation simply to test a key.

ChatGPT/OpenRouter browser authorization and ChatGPT eligibility are explicit dependencies. KIE/Higgsfield key guidance is not invented OAuth. Provider documentation, billing differences and links are in the detailed handoff; never promise universal subscription replacement.

## 3. Acceptance and planned verification

First working milestone: open Personal, chat through a real admitted Gateway runtime, see streaming/status/errors and supported stop/control, and retain chat while navigating. Then add supported provider/model/reasoning selection, attachments, commands/skills, durable conversations and canvas actions. Real image jobs follow their own provider/asset gate.

Preserve system/workspace isolation through navigation and delayed events; never transfer private conversation content on a tab switch. Browser/model input cannot supply trusted scope, grants or raw provider authority. Usage/cost comes from Token; unknown is not zero. Validate provider callbacks, token identity and scopes, protected credential storage, owner-backed readiness, revocation and negative permission paths before enabling integrations. Documentation is not executed product evidence.

## 4. Execution and owners

| Owner | Responsibility / current boundary |
| --- | --- |
| Dashboard | Presentation, guides, authenticated host integration, chat/app context and UI controls. Detailed plan and acceptance ledger remain here. |
| Connections | Reuse credential isolation, verification, capability admission, revocation and external-effect receipts. Inspect current public contract before adding adapters. |
| Gateway/runtime | Canonical authenticated execution, run/event/control routing and admitted runtime behavior. Inspect runtime credential ownership instead of assuming all auth belongs to Connections. |
| Token | Existing canonical usage/cost evidence and bounded projections; no duplicate accounting engine. |
| System | This linked scope/dependency summary; reconcile protected scope and future gates explicitly. |
| Distribution | Separate member release/compatible set admission. No promotion by this plan. |

System main inspected at `21bf92a3ca5bf767cbffaab9a7f7701f8943d783` already records [Token stop-check complete](../completed/TOKEN-COMPLETION-STOP-CHECK-2026-10-27.md) and [Connections V1 qualification complete](../completed/CONNECTIONS-V1-QUALIFICATION-AND-HANDOFF-2026-10-27.md). Do not reopen those scopes or invent extra work. Reuse the [Connections consumption handoff](https://github.com/aiverse-filmmakers/AI-Verse-Connections/blob/d326e39f4f07fb163250d671b8960a1fc00e8e03/docs/DASHBOARD-CONSUMPTION-HANDOFF-2026-10-27.md); an existing browser/Gateway provider execution bridge was not qualified by that closeout. New provider UX/integration is a separately bounded follow-up after contract inspection.

Proposed order: reconcile amended gates → real Personal chat and minimum shell → actual shared chat tools → persistent workspace/canvas → agent canvas actions → real creative jobs → advanced operational views → specialist Filmmaking → desktop/composed acceptance. No new denominator or engineering completion percentage is asserted until scope estimates are reviewed.

## 5. Checkpoint and next action

- Accepted history remains **15 baseline Dashboard points** for MC0/MC1; new scope does not fit a claimed unchanged “85 remaining.”
- Dashboard PR #41 publishes the plan, contract gaps and Connections UX handoff as documentation only.
- A local preparatory AUTH-1 transaction helper has build/test evidence (102 pass, one skip); its source is not in this documentation PR and is not accepted/published runtime behavior. Token exchange, verified account identity, refresh/storage, visible routes/UI and real chat remain pending.
- Next: review/reconcile the Dashboard PRD/tracker and authentication/credential ownership, separately review the first code slice, then continue the detailed Dashboard plan. Keep the browser agent's completed Token/Connections work intact.
- No new provider account, credentials, paid request, private-Core trial or member release was performed by publication.


## Published source checkpoint — 27 October 2026

The prototype, full inspiration gallery and AUTH-1 source/tests are now published in [Dashboard PR #42](https://github.com/aiverse-filmmakers/AI-Verse-Dashboard/pull/42), branch `codex/dashboard-source-checkpoint`, initially at `e152acf474290acf856f2d86852dad99d7b59dfe`. That branch contains the plan and code together; it is stacked on plan PR #41. Earlier “local only” statements describe the previous checkpoint and are superseded for source availability, not feature acceptance. The [remote handoff](https://github.com/aiverse-filmmakers/AI-Verse-Dashboard/blob/codex/dashboard-source-checkpoint/docs/REMOTE-DEVELOPMENT-CHECKPOINT-2026-10-27.md) has run instructions, known gaps and next work. No sign-in or AI runtime is wired into the preview yet. Operator requires meaningful local Dashboard work/checkpoints to be synced to GitHub for browser continuation; inspect remote changes before updating branches and never publish secrets or browser state. This does not authorize automatic merges/releases.
