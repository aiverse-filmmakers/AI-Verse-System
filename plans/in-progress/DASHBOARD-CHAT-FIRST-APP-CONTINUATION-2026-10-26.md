# Chat-first AI-Verse App — Continuation from Step 2

**Date:** 26 October 2026 · **Owner:** AI-Verse-System · **Implementation:** Dashboard, Gateway, Distribution and existing domain owners.
**Status:** PLANNED; preparation may start, live proof requires the separate qualification handoff. **Progress:** 0/9 continuation slices accepted; existing accepted work is preserved.
**Method:** [Plan Maker](../../docs/PLAN-MAKER.md). Extended depth is justified by provider credentials, persistent sessions, multiple repositories and desktop/remote access. This is the single continuation plan, not a new backend program.

## 1. Problem and boundary

The backend already does substantial work, but members cannot yet use it through a finished general-purpose AI-Verse interface. Deliver one coherent app: select a system/workspace, connect a supported model account, chat with retained context/history, control active work and continue from desktop or phone. Keep room for useful future panels. Do not restrict the product to one filmmaking workflow or result.

This plan starts at the operator's **step 2**. **Step 1 — remaining Gateway security/integration qualification — is excluded and owned by the operator's separate workstream.** Its living source is the [Gateway completion plan](GATEWAY-COMPLETION-AND-DASHBOARD-READINESS-2026-10-23.md); the current in-progress handoff is [System PR #280](https://github.com/aiverse-filmmakers/AI-Verse-System/pull/280). That PR is a checkpoint, not acceptance. Do not take it over, duplicate its tasks or assume it has passed.

Before the real step-2 proof, consume its accepted exact-source receipt and reconcile Dashboard MC1.4's written audit/repair gate. Merely merging a plan, passing an older SHA or receiving permission to plan does not release that gate. Until then, bounded source inspection, fixture/lab preparation and documentation can proceed; live owner acceptance waits. If later feature code changes an accepted boundary, qualify that changed feature normally without reopening unrelated completed programs.

**Preserve:** existing owner APIs, sessions/history, context/Purpose/Memory behavior, authorization, system/workspace separation, user files and lifecycle recovery. Dashboard owns presentation and connection metadata, Gateway owns runtime ingress/runs/events, and domain truth stays with its existing owners. Distribution retains installation, compatibility and release authority.

**Outside this release:** a new agent engine, second memory/session database, framework rewrite, complete Control Room, broad provider marketplace, native phone app or public multi-tenant SaaS. Future tabs can be added without becoming prerequisites for usable chat. No blanket promise that local MIT-licensed code becomes uncopyable or remotely revocable.

## 2. Existing path and smallest change

Current route: pinned Mission Control task dispatch -> authenticated canonical Gateway -> selected system/workspace -> owner/host -> configured runtime -> canonical run/events -> client projection.

| Surface | Reuse / bounded extension |
| --- | --- |
| Mission Control shell | Reuse Dashboard's canonical adoption plan, upstream pin and `scripts/mc1/` lab. Do not restart the historical scratch-built frontend or migrate its framework/build tools merely to follow an older Vite example. |
| Actual chat | Extend the adopted main chat page through the first-class AI-Verse adapter. Generic local-provider task dispatch alone does not wire that page. |
| Runtime and history | Reuse Gateway `src/server.mjs`, `src/run-engine.mjs`, `src/store.mjs`, `src/runtime.mjs` and existing owner/context adapters. Dashboard caches remain reconstructable. |
| Scope and panels | Preserve Dashboard `packages/protocol`, `packages/registry`, `packages/client`, `packages/live` and `apps/web` contracts where compatible. Existing render models are not a finished app. |
| Provider connections | Extend the existing HTTP/runtime seam; generic OpenAI-compatible calls already exist. OpenRouter authorization, a model/account UI and a real Codex login adapter are not established by inspected source. |
| Streaming | Gateway exposes SSE, but its generic HTTP adapter currently sends upstream `stream: false`. Extend delivery rather than introducing another broker or run store. |

The approved shell adoption, pre-strip feature-disposition rules and existing Dashboard tracker remain in force. This plan defines the requested bounded delivery milestones inside that program; it neither resets its 11/100 historical acceptance nor claims the whole roadmap must ship first. Record accepted work in the existing component tracker and reference it here rather than maintaining competing task histories.

**Product/technical choices:** OpenRouter is the first bring-your-own-account connection; members use their own credits. Codex is an agent runtime integration, not just another chat endpoint. Reuse official managed authentication and existing secure credential facilities where sufficient; Dashboard should receive status and safe handles rather than own raw provider tokens. No new credential service/store is justified until the existing owner seam is inspected and shown insufficient. Switching providers must make the selected context destination clear and must not silently switch billing routes.

## 3. Acceptance and planned verification

These are requirements to prove, not results already obtained. Add focused regressions where existing coverage is insufficient; do not create a separate test framework or require redundant checks for every row.

| ID | Observable behavior and meaningful failure | Planned verification / expected result |
| --- | --- | --- |
| A1 | Stock pinned Mission Control dispatches one real read-only request through the intended authenticated Gateway and receives the actual result; wrong binding/token fails safely. | After the external handoff, Dashboard `npm run mc1:preflight`, then its existing `npm run mc1:local` on a disposable system with hidden-token input. Retain sanitized result and exact refs; cleanup preserves AI-Verse state. |
| A2 | The actual chat page visibly binds one system/workspace, sends to its Gateway and shows its response. | Supported UI journey: select scope, send a message, inspect canonical run/session identity. Invalid or unavailable system shows an error, never a fallback into another system. |
| A3 | History survives reload/restart; switching A→B→A restores the correct session. Stop and other advertised controls affect the real run. | Browser reload/reconnect and two-system/two-workspace journey; exercise existing run-control API and relevant Gateway/Dashboard regressions. Unsupported controls are hidden/disabled; uncertain restart continuation stays explicit. |
| A4 | A member can authorize OpenRouter, choose supported models and send requests billed to their own account; disconnect/revocation is clear. | Official PKCE connection with a test account; at least two available model families, depleted-credit/invalid-auth cases, disconnect and reconnect. No secret in browser bundles/logs/exports; app access and provider access remain distinct. |
| A5 | Provider text arrives incrementally, cancellation reaches upstream, and interrupted/tool responses do not corrupt history or duplicate effects. | Focused adapter stream/error/abort fixtures plus one real UI/provider request; inspect persisted final history and incomplete-run state. Do not claim token streaming from an SSE wrapper around a completed response. |
| A6 | Codex managed account login, session execution and relevant approvals work through a replaceable Gateway adapter. | Supported official app-server login -> real turn -> disconnect/relogin, expired auth, cancellation, scoped approval and restart cases. Credentials remain with the runtime/secure owner; a ChatGPT subscription is not an unrestricted general API key. |
| A7 | A macOS desktop artifact launches the shared web UI, attaches/starts the correct isolated Gateway and preserves an existing installation. | Install/open/quit/reopen/update smoke on the supported Mac path; no orphan process or lost session. An explicit new-system install uses Distribution. Native host is thin; no second installer/runtime. |
| A8 | A phone can securely reach the same selected system and resume chat with an understandable connection state. | Real phone over the chosen authenticated private remote path: sign in, send/resume, background/reconnect and unavailable-host case. Local host must be awake/reachable; independent cloud execution is not implied. No unauthenticated public listener. |
| A9 | Verified member entitlement controls the defined paid product boundary; expired/revoked access cannot bypass it through a direct protected request. | Test grant, paid-through expiry, revocation/refund handling and rejoin against the legitimate membership source. Preserve user work/export. Document any staffed reconciliation delay; do not equate Skool new-member automation with cancellation sync or claim copy protection for permissive local code. |

Use the component's existing native checks plus the relevant exact-source composed acceptance when publishing changed code. Verify the real browser/desktop/phone path where specified. Native tests, owner acceptance and Distribution release are separate evidence. Measure actual responsiveness/cost only enough to set justified limits; do not invent performance budgets.

## 4. Execution — original steps 2–6

### Step 2 — Complete the existing Mission Control → Gateway proof

**Slice 2.1 — Existing proof accepted.** Owner: Dashboard/Gateway; acceptance A1. Reuse MC1.1–MC1.3 and close MC1.4/MC1.5 with actual evidence. This also satisfies the equivalent proof requirement in Gateway G4.1 when its owning plan accepts the same evidence; do not perform a duplicate proof simply for another tracker.

Immediate tasks, refined only from observed facts:
1. Refresh the relevant heads, current MC1 gate and step-1 receipt; record exact eligible component refs and any incompatible inputs.
2. Reuse the pinned lab/preflight/proof scripts. Prepare only the smallest fixture/runbook correction needed; no real personal data or token in documentation.
3. Once the explicit prerequisite gate is discharged, run the existing read-only proof on a disposable system. Use the normal secure local input path; ask for human action only if it cannot be performed through an already authorized secure route.
4. Record sanitized acceptance and cleanup evidence in the component tracker and this checkpoint. Move to step 3 only after A1 passes. If the prerequisite remains open, record that dependency without turning its repair into this plan's scope.

### Step 3 — Build the actual chat interface

**Slice 3.1 — Scoped main chat works.** Owner: Dashboard with the existing Gateway contract; acceptance A2. Extend MC2's first-class adapter, adopted chat page, composer and system/workspace selection. Use selected-system metadata, preserve per-system Gateway binding and make errors visible. Apply feature-disposition decisions before replacing/stripping an upstream authority. Dependency: 2.1.

**Slice 3.2 — Continue and control real work.** Owner: Dashboard/Gateway; acceptance A3. Wire canonical history, streamed activity, reconnect/reload and advertised stop/pause/resume/approval controls. Reuse existing capabilities; do not simulate controls in UI state or persist provider continuation only in Dashboard memory. Dependency: 3.1. First usable internal browser milestone ends here, using a supported existing runtime; it does not require every later tab.

### Step 4 — Add OpenRouter connection, model selection and provider streaming

**Slice 4.1 — Bring your own OpenRouter account.** Owner: Gateway/runtime or existing secure connection owner for credentials, Dashboard for UI; acceptance A4. Reuse generic HTTP transport and official PKCE; expose connection/model state through a bounded owner API. Do not accept arbitrary untrusted endpoint/secret configuration as request authority. Record billing and context-transfer behavior. Dependency: 3.2.

**Slice 4.2 — Genuine provider streaming.** Owner: Gateway runtime, Dashboard renders existing events; acceptance A5. Extend the current invocation seam incrementally while preserving nonstreaming/subprocess compatibility, tool-call assembly, aborts and final usage/history semantics. No second event broker. Dependency: 4.1.

### Step 5 — Add Codex authentication through a runtime adapter

**Slice 5.1 — Managed Codex runtime connection.** Owner: Gateway adapter and managed Codex runtime; Dashboard displays status and controls; acceptance A6. Inspect the official app-server contract at implementation time. Prefer managed browser/device login over copied auth files or another client's OAuth identity. Keep authentication/session lifecycle, tool approvals and model/provider capabilities explicit. Preserve ordinary chat access while unconfigured Codex is unavailable. Dependency: 4.2; the provider-neutral UI can be prepared earlier without bypassing acceptance.

Claude models remain usable through supported provider APIs such as OpenRouter. Generic Claude subscription sign-in is not a requirement or assumed entitlement in this plan.

### Step 6 — Package desktop, then establish phone access and member entitlements

**Slice 6.1 — Shared desktop delivery.** Owner: Dashboard thin host + Gateway lifecycle + Distribution; acceptance A7. Use the existing Tauri direction if compatible with the adopted shell, retain one frontend, system selection and isolated Gateway instances. Keep signing/packaging credentials in their approved owner. An unsigned internal build is not a signed public release. Dependency: 5.1.

**Slice 6.2 — Phone access to the same system.** Owner: Dashboard/client host and Gateway's existing remote policy; acceptance A8. Start with a trusted private authenticated route to the user's running host, reusing supported mechanisms. Choose the smallest supported transport after inspecting deployment constraints; preserve TLS/auth/origin policy. A separate hosted-runtime option needs its own explicit infrastructure/cost decision rather than silently converting this product into SaaS. Dependency: 6.1.

**Slice 6.3 — Member access and bounded release.** Owner: product entitlement authority to be identified within existing Gateway/Distribution/connection boundaries, Dashboard for account UX; acceptance A9 plus the combined A1–A8 journey. Identify the authoritative membership source and exact enforceable paid feature boundary before code; record that bounded owner decision if no existing contract suffices. Reuse official lifecycle events where verified; a small pilot may use administrator-verified, time-bounded access with explicit reconciliation. Ordinary cancellation follows verified paid-through terms; refund/chargeback handling is a separate policy. Reuse existing user-data retention/export and licensing obligations. Dependency: 6.2. Distribution qualifies exact accepted artifacts before member release; do not rewrite admitted pins from this plan.

Detailed tasks for later slices are deliberately deferred to their start. Keep the nine outcomes fixed; change implementation techniques from evidence. A different outcome, weakened gate or new product obligation follows the existing Plan Maker amendment process. Do not add new architecture, platforms or features merely to improve a progress metric.

## 5. Checkpoint, evidence and next action

**Confirmed source snapshot:** System main `a6ea488b42bb19f106ddcccbe03594c7dd1fe7c7`; Dashboard main `ec5d40aea7fa3111357c086660a2630cef20f51a`; Gateway main `fa131c146690f4c02893d2849b7f4a21489b30c7`. Heads were refreshed during plan creation. System PR #280 independently tracks pending qualification. These observations do not claim acceptance of later code, a safe personal rollout or a member release.

**Current status:** planning/documentation only; 0/9 continuation outcomes accepted. No feature implementation, real provider login, live MC1 proof or release promotion has been performed under this plan. The earlier local proposal to build a single filmmaking workflow is superseded by the operator's general-purpose app requirement; hosted-first implementation is not this plan's default.

**Next action:** start 2.1's bounded source/receipt reconciliation. Consume step 1's accepted handoff before live proof. Preparation can proceed independently; do not represent the entire app as blocked solely because live acceptance is pending. Owner/runtime/token availability may require one secure local acceptance step; never request secrets in chat.

**Later decisions, at their relevant slice:** actual secure provider-custody seam, Codex process supervision compatibility, desktop distribution/signing and private-phone transport, legitimate membership lifecycle events and entitlement authority. These are bounded implementation decisions, not permission to invent a new platform. No calendar promise is made before the existing proof and app adapter establish real scope.

**Completion evidence format:** per slice, record accepted outcome/requirement IDs, exact owner PR/SHA, commands or real journey and result, remaining limitation and next step. Keep detailed logs at their owner; link them here. Preserve the separate Gateway and Dashboard program counters.

### Source routes

- [Dashboard canonical adoption](../../docs/DASHBOARD-CANONICAL-MISSION-CONTROL-ADOPTION-PLAN-2026-09-15.md); [owner product intent](../../docs/OWNER-PRODUCT-INTENT.md).
- [Dashboard tracker at inspected ref](https://github.com/aiverse-filmmakers/AI-Verse-Dashboard/blob/ec5d40aea7fa3111357c086660a2630cef20f51a/docs/MISSION-CONTROL-EXECUTION-TRACKER-2026-09-15.md); [existing MC1 runbook](https://github.com/aiverse-filmmakers/AI-Verse-Dashboard/blob/ec5d40aea7fa3111357c086660a2630cef20f51a/docs/MC1-MISSION-CONTROL-AIVERSE-RUNTIME-PROOF.md).
- [Gateway runtime at inspected ref](https://github.com/aiverse-filmmakers/AI-Verse-Gateway/blob/fa131c146690f4c02893d2849b7f4a21489b30c7/src/runtime.mjs).
- Official provider contracts: [OpenRouter authorization](https://openrouter.ai/docs/guides/overview/auth/oauth), [Codex app-server](https://learn.chatgpt.com/docs/app-server). Re-read the specific contract at implementation time; do not infer a new provider's support from interface names.
