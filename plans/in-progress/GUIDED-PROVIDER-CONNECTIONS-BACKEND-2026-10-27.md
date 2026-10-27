# Guided provider connections: bounded backend follow-up

**Date:** 2026-10-27
**Status:** S1 IN PROGRESS, S2 BLOCKED on authenticated host/API and deployment decisions. **0/2 fixed outcome slices accepted** at plan creation.
**Planning rule:** [Adaptive Implementation Planning Skill](../../docs/ADAPTIVE-IMPLEMENTATION-PLANNING-SKILL.md) and [Implementation Plan Template](../../docs/IMPLEMENTATION-PLAN-TEMPLATE.md). This is new provider UX scope, not a reopening of completed Connections V1 or Token.

## Product and evidence
People should be able to connect supported AI services with a browser login where actually permitted, or a single API-key field and clear account/key links. A saved key must not be described as authenticated, usable or funded without a meaningful check.

Read actual source and checkpoint in [System PR #294](https://github.com/aiverse-filmmakers/AI-Verse-System/pull/294), [Dashboard plan PR #41](https://github.com/aiverse-filmmakers/AI-Verse-Dashboard/pull/41), [Dashboard source PR #42](https://github.com/aiverse-filmmakers/AI-Verse-Dashboard/pull/42), [Dashboard Connections UX handoff](https://github.com/aiverse-filmmakers/AI-Verse-Dashboard/blob/codex/dashboard-source-checkpoint/docs/CONNECTIONS-UX-HANDOFF-2026-10-27.md), and [Dashboard remote checkpoint](https://github.com/aiverse-filmmakers/AI-Verse-Dashboard/blob/codex/dashboard-source-checkpoint/docs/REMOTE-DEVELOPMENT-CHECKPOINT-2026-10-27.md). PR #42 is **published and stacked on #41**, not an unpublished local-only source. Dashboard AUTH-1 is a host-only one-use PKCE transaction helper, **not** an exchange, account connection, vault or inference route.

Connections `main@d326e39f4f07fb163250d671b8960a1fc00e8e03` already provides `ConnectionsService`, encrypted local vault handles, `addGeneric/verify/reauth/revoke`, capability admission, final-edge permission enforcement and receipts. Existing [V1 closeout](../completed/CONNECTIONS-V1-QUALIFICATION-AND-HANDOFF-2026-10-27.md) stays closed. Gateway runtime currently reads `runtime.api_key_env` for its OpenAI-compatible provider; no approved browser-to-Gateway provider-management API exists. Token remains canonical cost owner.

## Permanent laws
- Trusted local host authenticates the user and derives system/workspace/grants. Browser/chat cannot supply trusted identity, raw vault paths, arbitrary provider origins or approval authority.
- Reuse **Connections credential vault** for external provider API keys; never add a Dashboard vault. Gateway's configured model-runtime secret path is not silently migrated. Do not conflate model inference authorization with external-effect grants.
- Never put keys, OAuth codes/verifiers/tokens or signed URLs into browser persistence, chat context, diagnostics, PRs or receipts; no real secrets/paid requests.
- Keep configured, verified, approved, funded, plan-eligible and model-ready distinct. No blind retries, automatic authority grants or unknown-outcome optimism.
- Preserve owner-local completed qualification, existing method response shapes, registry/workspace isolation and release gates. No Dashboard code changes in this plan.

## Fixed outcomes and requirements
| ID | Success / failure | Owner / slice | Evidence |
| --- | --- | --- | --- |
| P-R01 | Higgsfield raw copied key can be transported as `Authorization: Key <key>` to an approved fixed origin, not via a user-supplied extra prefix. Existing Bearer/header remain unchanged. | Connections / S1 | Synthetic loopback mock checks header; private key absent from registry/receipts. |
| P-R02 | KIE non-generating GET credit check accepts documented `code: 200` and rejects HTTP 200 with JSON `code: 401/429`, invalid JSON and wrong shape without claiming verified success. | Connections / S1 | Positive and negative mock responses, no generation request. |
| P-R03 | Failed verification invalidates verified/authorized/approved UI-facing flags; replacement/revocation still require owner-authorized actions. | Connections / S1 | Negative regression and existing full tests. |
| P-R04 | Host can later present scoped list/setup/check/replace/disconnect without a new store or allowing browser/model-derived authority. | Dashboard host + Connections / S2 | Contract and integration tests via authenticated host (not assumed complete now). |
| P-R05 | ChatGPT/OpenRouter browser callback exchange and eligibility are admitted only for supported deployment routes, with state/PKCE/identity/scopes, protected token lifecycle and negative tests. | Dashboard host/runtime / S2 | Real owner contract review + synthetic auth tests; no live credentials now. |

## Flow, ownership and classification
Existing: trusted Connections local service → registration with credential handle → generic adapter credential resolution → bounded provider probe → status flags → separate capability admission/approval → final-edge execution/receipt. **REUSE** vault, registry, scope/admission and security policy. **EXTEND** the existing generic adapter only for a documented Higgsfield key header and KIE response semantics; **do not CREATE** a parallel credential store, standalone service, Gateway provider adapter or broad OAuth system. **BLOCK** a browser API until an authenticated host route is designed and tested.

Official source checks (27 Oct 2026): [OpenRouter PKCE](https://openrouter.ai/docs/guides/overview/auth/oauth), [OpenRouter key check](https://openrouter.ai/docs/api/api-reference/api-keys/get-current-key), [KIE getting started](https://docs.kie.ai/getting-started), [KIE credits](https://docs.kie.ai/common-api/get-account-credits), [Higgsfield quick start](https://open.higgsfield.ai/quick-start), [OpenAI sign-in eligibility](https://developers.openai.com/siwc/quickstart). ChatGPT local OSS plan usage and commercial/hosted partner paths are **different admission routes**. No Higgsfield free authenticated readiness endpoint is verified: saved key is **configured, unverified**, until documented non-billable validation exists. OpenRouter OAuth returns a user-bound key; it is not a blanket ChatGPT OAuth equivalent.

## Slices
### S1: Owner-local key transport and honest check (Connections only)
**Status:** IN PROGRESS; depends on actual adapter, existing fake-provider harness and documentation verified above.
**Current tasks:** S1.1 characterize/record concrete false-positive and Key-header gaps; S1.2 add narrow Key header + opt-in KIE credit response validation, without altering defaults; S1.3 add mock tests for success/denial/malformed response, secret redaction, status invalidation and regression of existing Bearer behavior; S1.4 run `npm run check` / CI, update exact revision and owner handoff.
**Acceptance:** synthetically demonstrated key-only happy path, failed check cannot remain approved; no provider generation, no raw key in persisted state, no changed v1 default behavior. Existing public library/CLI stays backward compatible. Full test suite green. **Next:** S2 only after host/eligibility gate; stop on complete S1.

### S2: Authenticated host connection and OAuth admission handoff
**Status:** BLOCKED / not authorized to edit Dashboard code in parallel with local Codex. Ownership: Dashboard authenticated host and canonical Gateway runtime for model execution; Connections owner for locally supported provider credentials.
**Scope:** no code in this task unless Dashboard Mac agent coordinates source ownership and exact interfaces. Define response shapes, errors, permissions and synthetic host integration tests. Reuse `ProviderAuthorization` from Dashboard PR #42; add exchange, JWT identity, refresh, secure host credential storage only after deployment eligibility + canonical ownership is reviewed.
**Acceptance:** authenticated host denies wrong session/system/workspace and never serializes key; faithful list/check/replace/disconnect flows; distinct configured/verified/authorized/approved/funded; explicit unsupported ChatGPT route; fake-run and callback tests, plus later local Mac acceptance. No release promotion.

## Risks, reviews and next step
- KIE uses HTTP 200 even for API error payloads; inspect body only for opt-in KIE probe, never trust status alone.
- Higgsfield `Key` scheme is not a verified key check; do not generate media to validate.
- OpenRouter PKCE yields a provider key; no unapproved client-side token storage.
- Vault credential deletion may affect shared handles: require reference checks and explicit operator scope before physical deletion in any future host route.
- Recheck branch heads before writes; ship System plan and Connections code in separate **draft** PRs. Keep the Dashboard PR branch untouched.
- **Progress:** S1 0/4 derived tasks initially, overall 0/2 slices; no new whole-program Dashboard points. Advance only with tests and owner review.
