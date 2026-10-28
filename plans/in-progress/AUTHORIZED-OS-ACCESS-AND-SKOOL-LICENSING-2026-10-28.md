# Authorized OS Access: Skool Membership and Revocable App Licensing

**Date:** 2026-10-28  
**Status:** RESEARCHED PLAN, NOT IMPLEMENTED. Slice 1 ready for evidence refresh; architecture and implementation gated on verified provider/owner evidence. **0/7 fixed slices complete (0%).**  
**Canonical planning method:** [Adaptive Implementation Planning Skill](../../docs/ADAPTIVE-IMPLEMENTATION-PLANNING-SKILL.md) and [Implementation Plan Template](../../docs/IMPLEMENTATION-PLAN-TEMPLATE.md).  
**Product direction:** Preserve Skool as the current community and billing experience where feasible, make the member sign in once, automatically allow legitimately entitled users, and revoke use of the *software itself* after paid access ends, not merely updates. Do not add monthly codes, repeated logins or manual work for ordinary members.

## 1. Executive decision and feasibility warning

**Do not build a simple update-key scheme.** Subscription expiry must affect runtime authorization, not only the installer, updater, Dashboard display, model selection or downloaded releases.

**Two separate problems must be solved:**

1. **Subscription truth:** obtain trustworthy, current evidence that a given person remains eligible for OS access, including renewals, nonpayment, cancellation effective dates, bans, refunds, trials, gifts and lifetime grants.
2. **Application enforcement:** require a valid entitlement at *each supported premium execution entry point*, including Dashboard, Gateway, direct CLI/agent routes, background runs, remote clients and any other installed binary capable of performing the licensed work.

**Critical limitation:** As checked on 2026-10-28, Skool's documented Pro-only Zapier app has a polling **New Paid Member** trigger but **no supported cancellation trigger, live membership lookup, or subscription renewal-status search**. Skool itself says cancellation normally removes the member at the end of the paid billing period. Therefore Skool + Zapier alone cannot guarantee automatic timely revocation. A new-member notification is **not** evidence of every future paid renewal. Do not promise hands-off cancellation sync while this remains unverified.

**Second critical limitation:** An unrestricted local source distribution can be copied, patched and run independently by someone who controls their machine. Existing public GitHub source and local OS/Gateway/Distribution commands mean a cosmetic Dashboard gate is insufficient. No general-purpose client-only license can guarantee absolute post-cancellation non-use. The strict product goal requires either (a) critical functionality and premium effects enforced by an online trusted service, or (b) a hosted execution model, with an explicit decision on which local capabilities remain accessible. This plan does not claim to make already disclosed source or the user's own data uncopyable.

**Recommended direction, conditional on provider proof:** Keep Skool billing and affiliate mechanics initially; reuse the existing AI-Verse trusted runtime edges and existing VPS when appropriate; add the smallest distinct **commercial entitlement authority** necessary; make licensed operations require online verification; integrate a human-verifiable Skool reconciliation until Skool provides a supported reliable membership-state feed. **If zero-touch end-of-term revocation is a hard launch condition, block commercial release until an authoritative cancellation/renewal feed exists or billing ownership is deliberately changed.**

## 2. Research and source evidence (checked 2026-10-28)

| Evidence | What it establishes | What it does NOT establish |
| --- | --- | --- |
| [Skool Zapier documentation](https://help.skool.com/article/56-zapier-integration) and [Zapier Skool integration](https://help.zapier.com/hc/en-us/articles/10458381459341-How-to-get-started-with-Skool-on-Zapier) | Skool Pro, group key, new paid member polling, membership questions, invite, course unlock; no membership search/cancel trigger listed | Reliable renewal, cancellation or paid-through date for an existing member |
| [Skool cancellation instructions](https://help.skool.com/article/99-how-to-cancel-my-subscription-to-a-community) and [admin refunds/removal](https://help.skool.com/article/84-how-to-refund-a-members-payment) | Cancellation normally takes effect at billing-period end; removal/ban can end membership differently; refund alone does not cancel | Precise paid-through timestamp in an exported member row |
| [Skool export/help](https://help.skool.com/article/148-where-can-i-find-members-answers-to-membership-questions) and [paid group email export announcement](https://www.skool.com/educate/you-can-now-export-your-members-email-addresses-in-paid-groups) | Admin member exports exist, and paid groups may expose member emails | Export is guaranteed to contain member ID, renewal time or status unless first verified against real owner exports |
| [2026 third-party export observation](https://movetowhop.com/how-to/export-members-from-skool) | Indicates members/exports may separate active versus cancelling lists, and CSV lacks renewal dates; useful investigation lead only | Official supported schema or a reliable subscription clock |
| [Skool platform policy](https://help.skool.com/article/179/platform-policy) | Warns against scraping and automated requests | Permission to run browser bots, undocumented member endpoints or third-party reverse-engineered sync |
| [Skool payouts](https://help.skool.com/article/78-how-to-setup-skool-subscriptions), [payments FAQ](https://help.skool.com/article/86-subscriptions-faq), [Skool affiliate mechanics](https://help.skool.com/article/187-how-to-setup-affiliate) | Skool manages payments/payouts and has Skool-specific affiliate attribution | Merchant-level Stripe Billing webhooks are available to the creator for Skool membership payments |
| [Supabase Auth](https://supabase.com/docs/guides/auth), [RLS](https://supabase.com/docs/guides/database/postgres/row-level-security), [Edge Functions](https://supabase.com/docs/guides/functions/auth) | Managed login and server authorization are viable OPTIONAL tools if existing AI-Verse services are insufficient | Supabase is required, already present, or superior to reusing the existing VPS |
| [Stripe subscription events](https://docs.stripe.com/billing/subscriptions/webhooks) | A directly owned Stripe Billing subscription can provide renewal/cancellation event evidence | Those events appear on Skool's Stripe Express payout connection |

**Re-check all external integrations before implementation.** Prove actual Skool plan eligibility and owner dashboard/export shapes. Do not assume every member's email is available, that a Zapier event means a settled recurring renewal, that cancelling means immediately unpaid, or that a trial is paid.

## 3. Product brief and permanent laws

**Target journey:** Owner enables OS entitlement for qualifying paid Skool members. New member joins Skool, receives a simple app install/open link, signs in once with verified email or a verified binding flow, and uses the same local-first AI-Verse interface. Subsequent checks happen invisibly. When access legitimately expires or is revoked, premium execution stops; existing member projects/footage/exports remain intact. A renewed member recovers use without reinstall. Owner can revoke, grant, investigate and audit from a small admin interface.

**Scope:** Individual AI-Verse OS usage entitlement, launch and operation gates, Skool join/reconciliation evidence, lifetime/admin exceptions, expiry/re-entry, device/session management, member/admin UX, release qualification. This is **commercial app access**, not per-workspace ACL, Bot permission, Connections provider authentication, Token accounting or GitHub repo access.

**Non-goals:** DRM that claims unbreakable control of a user's computer; encrypting or deleting user content on cancellation; replacing existing OS action permissions; a broad multi-tenant SaaS/RBAC program; second update/installer service; forced Skool billing migration; bot scraping; new public APIs or databases before reuse is audited.

**Permanent laws:**

1. **Authorization is not authentication.** An email login identifies a person; server-sourced entitlement separately decides whether they may use licensed features. Email similarity or a self-reported Skool username is insufficient proof of membership.
2. **Entitlement is not host authority.** A valid subscription never grants broader workspace access, tool approval, external provider permissions, secret access or Bot authority. Effective authority is the restrictive intersection of entitlement, authenticated actor, system/workspace scope and existing OS/owner policies.
3. **Every real execution path must enforce.** Dashboard-only locks, updater-only keys, static AGENTS.md instructions or editable local flags do not protect direct Gateway/CLI/API/agent calls. Unknown or out-of-policy routes fail closed for licensed actions.
4. **No lifetime app by paying once.** Local packages/release hashes are never offline permanent premium licences. Offline-only premium operation conflicts with strict online revocation and must not be promised.
5. **Membership evidence has freshness and provenance.** Every grant records source, observed time, effective period, issuer, immutable evidence reference or digest and authorization revision. A new-join event cannot silently renew access forever. Stale/missing data is explicit, never converted to active automatically.
6. **Cancellation policy follows actually paid time.** Cancelling on Skool is not necessarily immediate loss of access; normal policy is through verified paid-through end. Immediate admin revocation/ban is a separate decision. Never synthesize a billing timestamp from join day or plan interval.
7. **User-owned state survives every licence change.** No deletion, corruption, hidden encryption hostage, project lockout or forced reinstallation. If storage access itself is licensed, provide a documented export/read-only route.
8. **No duplicate authority.** Reuse Gateway's real principal and OS permission system, Distribution's safe install/update, and existing secret storage. Dashboard only presents state/actions. This commercial entitlement source is separate from canonical member workspace Data and from Token usage evidence.
9. **No unapproved vendor or credential expansion.** Skool credentials, service secrets, admin proof and member personal data stay in trusted server storage; never expose them to client bundles, agents, chat context, logs or public CI.
10. **Keep launch truth honest.** No mark of secure/completely revocable before bypass, expiry, offline and provider-freshness tests pass against the actual distributed member package.

## 4. Options, tradeoffs and provisional selection

| Route | Joining | Cancellation/renewal truth | Member friction | Tradeoff / recommendation |
| --- | --- | --- | --- | --- |
| A. Skool + Zapier + owner verified reconciliation | New paid member can provision automatically on supported Pro plan | Verified active/cancelling/churned admin evidence must be periodically imported/reviewed; no proven push cancel API | Low | **Preferred initial pilot** only if owner accepts reconciliation and freshness/denial policy; do not call it fully automatic |
| B. Skool + third-party unofficial sync | May provision and query member states | Depends on undocumented Skool endpoints, account token, vendor resilience and Skool policy | Low until sync breaks | **Do not make security-critical default**; requires legality/policy, privacy, reliability and outage review |
| C. Own billing with Stripe Billing or equivalent + Skool invitation | App subscription events are accessible and testable | First-party billing webhooks and reconciliation possible | Usually low | **Best automation for app entitlement** if owner approves payment/affiliate changes; may not reproduce Skool native 40% recurring affiliate system, Skool membership removal or Discovery benefits |
| D. Fully hosted app/runtime | Provider-agnostic sign-in | Depends on A/B/C upstream billing truth | Low | Strongest enforcement on proprietary server functionality, but may compromise local-first video workflows and raise hosting costs |
| E. Download/update code only | Simple key | No real runtime revocation | Low | **Rejected** for requested goal |

**Default plan:** Prototype A with strict time-limited evidence and online runtime enforcement; design a billing-provider-neutral entitlement adapter so C can replace A without rebuilding app authorization. Require an explicit **GO/NO-GO** before declaring Skool billing suitable for unattended paid release.

## 5. Current system evidence and owner map

**Inspected moving main docs on 2026-10-28 (not a fresh code/test audit, not acceptance):**

- [System README](../../README.md), [Repository Network Governance](../../docs/REPOSITORY-NETWORK-GOVERNANCE-CONTRACT.md), [architecture tombstones](../../docs/ARCHITECTURE-TOMBSTONES.md) and [owner intent](../../docs/OWNER-PRODUCT-INTENT.md): System governs cross-owner contract, not implementation. Existing roadmap is single-user first; commercial member licensing is a new gated distribution milestone, not permission to reprioritize core Dashboard work.
- [Gateway README](https://github.com/aiverse-filmmakers/AI-Verse-Gateway/blob/main/README.md): Gateway already authenticates bearer credentials, derives an effective principal, offers run/chat HTTP operations and owns runtime execution. **REUSE / EXTEND**, subject to precise verification. A bearer token alone does not establish paid membership.
- [OS README](https://github.com/aiverse-filmmakers/AI-Verse-OS/blob/main/README.md): OS enforces workspace/permission and has local CLI and owner-routed commands. **REUSE / EXTEND**, audit alternate direct paths.
- [Dashboard README](https://github.com/aiverse-filmmakers/AI-Verse-Dashboard/blob/main/README.md): Dashboard is UI/control surface and currently developing; **EXTEND UI only**, never store entitlement as Dashboard truth. Coordinate with local Dashboard work; do not edit concurrently without source ownership agreement.
- [Distribution README](https://github.com/aiverse-filmmakers/ai-verse-distribution/blob/main/README.md): existing canonical safe install/update/restore and member payload boundaries. **EXTEND packaging only if necessary**, do not create a competing updater or erase user state.
- **Public-source exposure:** repo visibility/public installer availability must be verified for every materialized member payload. An exported local executor or public source cannot be retroactively revoked. **BLOCK strict security claims** until the hosted/licensed critical capability boundary is defined.
- **Unknown pending proof:** any existing shared account/auth layer, VPS database, entitlement service or Skool integration. **AUDIT/REUSE first**; no separate Auth+Supabase+VPS stack by default.

**Provisional ownership:**

- System: common entitlement requirements, security contract, release qualification intent.
- Trusted entitlement service (existing VPS/host service if suitable): subscription evidence, commercial grants, expiry, revocation, devices, signed server assertions, audit trail.
- Gateway / supported runtime host: verify access and enforce at execution edge, including running/background tasks and remote transports.
- OS and component owners: preserve existing owner permission checks and guard supported direct licensed routes.
- Dashboard: first-run sign-in, billing/access status, protected actions, admin list/revoke/grant UX only.
- Distribution: package and update policy, safe member install, channel qualification, preservation.
- Connections: only if an approved external billing/Skool adapter genuinely belongs in its existing external-provider capability boundary; do not turn it into a second entitlement database.
- Token: cost/usage evidence only, not commercial billing authority.

## 6. Proposed minimal contract, subject to Slice 1-3

**Authenticated session:** verified user ID from a trusted login mechanism (prefer extend existing), linked to a Skool member via verified claim/event or explicit admin-confirmed mapping. Login and membership linkage are independently auditable.

**Entitlement record:** internal subject ID, product/plan/features, provider and external member/subscription reference when available, status (pending, trial-eligible, active, cancelling, suspended, expired, revoked, lifetime/manual exception), observed_at, current_period_end **only if verified**, evidence_updated_at, evidence_source, effective_until, entitlement revision, admin reason and audit timestamp. No raw payment card data.

**Decision response:** allow/deny, machine-readable reason (login_required, membership_unverified, expired, revoked, evidence_stale, offline, device_limit, service_unavailable), user-safe message, authorized feature set, expires_at and evidence freshness metadata. Server signs any reusable short-lived assertion; client must not mint or prolong it.

**Revocation rule:** online premium operation consults the authoritative decision service at admission and at bounded checkpoints, and all hosted effects independently check at the server. Evaluate active jobs on revocation with a safe pause/cancel policy; do not abandon mutations mid-transaction. Never let a Dashboard cache or stale signed token override a central deny. For required near-immediate revocation, use per-operation server verification or an enforceable short revocation window, not an unconditional 24-hour offline token.

**Practical target for evaluation, not a promised guarantee:** visible revocation of protected server actions at next operation; otherwise define and measure a bounded maximum token/session lifetime, initially target 5-15 minutes. UI heartbeat can be 15-30 minutes for display but **must not** be treated as enforcement. Strict offline = premium execution blocked without valid live verification. Network-outage UX must explain retry/support and preserve work. Estimate server load before locking timing.

**Reconciliation rule:** A Skool New Paid Member event can create a pending/provisioned identity. Actual commercial entitlement activation/renewal needs proof policy agreed in S2. Owner-authenticated imports compare authoritative active/cancelling/churned/admin evidence, detect missing members and stale runs, and produce a dry-run impact report before mass revocation. No single missed CSV row silently deletes paid user access; no indefinite entitlement extension on missing evidence. Human review is required for mismatches until a supported authoritative feed exists. Verify export tabs and exact columns on the actual group first.

**Identity and device protections:** rate-limit login; secure magic links/one-time codes or existing managed auth; device count only if needed and communicated; no hardware fingerprinting as a default; allow account recovery and explicitly revoke lost devices. Email changes must not create a free entitlement transfer. Test signed/unsigned data, replay, wrong account, swapped member IDs and cross-system scope.

## 7. Requirements with acceptance

| ID | Required success and failure behavior | Owning slice / proof |
| --- | --- | --- |
| A01 | Paid eligible member signs in once and can use supported licensed OS features; unknown user cannot self-grant via client or email mismatch | S3-S5, real host integration |
| A02 | Skool join is detected where Zapier Pro applies; cancellation/renewal are NOT inferred from join; missing verification is explicit | S1-S2 and S6, provider fixture/evidence |
| A03 | Cancellation respects verified paid-through date; banned/revoked member denied on confirmed effective event; renewal restores without reinstall | S4-S7, date/time + state-transition tests |
| A04 | Direct CLI, Gateway API, unattended jobs, browser and native shell cannot use licensed execution by bypassing a Dashboard overlay | S1 and S5-S7, real member package bypass matrix |
| A05 | Offline, stale evidence, manipulated local clock, token replay, cached session, process restart and service outage cannot create permanent premium access | S4-S7, adversarial tests |
| A06 | Project files, memory, Data and previous rendered exports survive expiry, uninstall, recovery and successful reactivation | S5-S7, preservation fixtures |
| A07 | Owner can review member status, proof age, grant/revoke reason, false positive and support recovery; controls are authenticated, scoped and logged | S6-S7, admin negative tests |
| A08 | Lifetime/manual exceptions are deliberate owner grants with provenance, never an automatic inference from no charge or Skool level | S4-S7, exception tests |
| A09 | No competing updater, OS permission store, provider vault or Token billing store; secrets never leak to logs/UI/member package | S1-S7, ownership and secret-leak checks |
| A10 | Launch copy states actual verification frequency, offline limitation, cancellation effective-date policy and unsupported local-source guarantees | S2 and S7, UX/legal/product review |

## 8. Dependency-safe fixed slices

### S1. Audit real distribution and enforcement bypasses
**Status:** READY FOR RESEARCH. **Owner:** System coordinates; Gateway/OS/Dashboard/Distribution owners inspect own exact code and current member build.
- Refresh immutable heads, current owner acceptance, installed public routes, CLI/agent entry points, local file availability, repo visibility, credential/session mechanisms, existing VPS/Skool integration, tests and lifecycle. Map every path that can still run after Dashboard closes.
- Classify each required element as REUSE, EXTEND, CREATE, RETIRE or BLOCK/UNKNOWN. Identify the minimal protectable critical feature set.
- **Acceptance/evidence:** exact repo/ref table, public member execution/bypass matrix, existing auth/reuse map, source-only vs proven status, first viable protected operation and next S2 decision inputs. **No implementation just to satisfy the plan.**
- **First task at start:** Refresh exact current state and derive bounded execution tasks.
- **Next:** S2.

### S2. Prove Skool eligibility source and choose commercial access policy
**Status:** NOT STARTED. **Dependency:** S1.
- Confirm Skool plan (Pro requirement), owner-visible Active/Cancelling/Churned exports and fields, legitimate member identity binding, missing emails, free/grandfathered members, trials, refunds, annual plans, lifetime rewards, timestamp availability, Zapier events and costs. Request documented integration support from Skool if necessary.
- Benchmark operator workload for daily versus weekly reconciliation and revocation lag. Write the precise definition of *paid through*, allowable evidence age, support fallback, ban policy and offline policy. Compare Skool-only approach with directly owned billing, including impact on existing 40% Skool affiliates and Skool-only benefits.
- **Hard GO/NO-GO:** If owner requires automatic cancellation enforcement and no authoritative supported source is available, explicitly BLOCK unattended Skool launch. Do not ship a guessed expiry calculation or a scrape-based sync.
- **Acceptance/evidence:** sample data with redacted fields, proof of event semantics, documented owner decision and launch constraints, next S3 inputs.
- **Next:** S3 only if policy is accepted.

### S3. Freeze minimum commercial entitlement architecture and contracts
**Status:** NOT STARTED. **Dependency:** S1-S2 GO.
- Choose existing host/VPS auth and store if suitable, otherwise justify one bounded server dependency. Define trusted actor binding, provider adapter, entitlement schema, device/recovery policy, revision, status, response and minimal Gateway/OS/Distribution interfaces.
- Verify user project ownership, member privacy and local-first boundary. Choose which valuable functions must move server-side rather than pretending local editable scripts can be locked.
- **Acceptance/evidence:** named owner for every read/write, threat model, no-duplicate review, schema and error fixtures, compatibility and rollback contract, hosted vs local licensed operation map.
- **Next:** S4.

### S4. Implement and verify authoritative entitlement decisions
**Status:** NOT STARTED. **Dependency:** S3.
- Build only the missing commercial authority at its accepted owner. Authenticate trusted server inputs, issue/rotate/revoke short-lived decisions, store minimal audit and state; ensure repeated or reordered events and concurrent admin operations are idempotent.
- **Acceptance/evidence:** authenticated happy path, expired/stale/revoked/default-deny tests, race/replay/mismatched identity tests, restart/recovery, privacy and storage validation, exact owner acceptance.
- **Next:** S5.

### S5. Enforce at every supported execution and packaging edge
**Status:** NOT STARTED. **Dependency:** S4 and S1 path inventory.
- Gateway and OS owners add entitlement checks *before and during* supported premium operations without weakening existing tool/workspace permissions; handle abandoned jobs and transport reconnect. Distribution gates new admitted licensed build without recreating updater; Dashboard offers simple sign-in and state display only.
- **Acceptance/evidence:** browser/native/CLI/Gateway/agent/background bypass tests; protection remains when Dashboard is killed; offline and cached-token negative proof; local file preservation; no regression in legitimate owner-only development mode.
- **Next:** S6.

### S6. Connect verified Skool evidence and small admin operations
**Status:** NOT STARTED. **Dependency:** S2-S5.
- Add Zapier onboarding only after group eligibility is confirmed. Integrate verified membership/admin reconciliation, dry-run missing/downgraded member report, stale-proof alert, manual explicit grant/revoke, lifetime exception and support recovery, without a scraper.
- **Acceptance/evidence:** new paid member, cancelled-at-period-end, expired, annual renewal, failed payment, free/grandfathered, owner gift, level-reward exception, duplicate event, absent CSV row, email mismatch and outage test fixtures; transparent operator workload.
- **Next:** S7.

### S7. End-to-end commercial qualification and honest rollout
**Status:** NOT STARTED. **Dependency:** S1-S6 accepted.
- Owner-accepted revisions only; Distribution qualifies exact composition across supported platforms and release profiles. Run red-team bypass + offline + revoked-running-job + reinstall/update/restore + data-export tests. Stage a small opt-in member pilot, measure revocation lag, legitimate lockouts, login friction, cost and admin effort. Do not silently change current Core releases.
- **Acceptance/evidence:** actual member package cannot invoke the selected **protected** operations outside the verified licensed path; publish the list of inherently unprotectable local artifacts; complete support/rollback instructions, operational monitoring and truthful feature/release claims.
- **Next:** move to completed only after owner and whole-release acceptance evidence, otherwise record blocker and exact test failure.

## 9. Required reviews, risks and recovery

- **Security:** public source bypass, compromised client, stolen session, device sharing, admin impersonation, fail-open cache, direct CLI, time rollback, replay, cross-system ID confusion, offline use, bypassable third-party APIs. Protect hosted operations server-side.
- **Billing accuracy:** Skool event lag, absent renewals, early refund or ban, cancellation scheduled for period end, inconsistent CSV status and no precise end date. Confirm from Skool admin, do not guess.
- **Member experience:** legitimate active customer locked out after missing manual import, bad network or device change. Provide visible explanation, read/export of their local work, safe resumption and owner support path. Select reconciliation SLA before launch.
- **Legal/privacy/policy:** document consent, storage limitation, retention/access controls, Skool terms, member notices and consumer cancellation expectations. No silent scraping.
- **Cost and operational load:** measure number of checks per daily active user, uptime/security monitoring, magic-link delivery, backup/restore and support before buying an additional SaaS.
- **Preservation:** no forced wipe, no orphaned state, no destructive software removal, no mutation of owner data when an entitlement expires. Canonical update/restore remains Distribution-owned.
- **Review cadence:** product/architecture before S3, code/adversarial at S4-S6, composed real-member qualification at S7.
- **Plan amendments:** changing billing provider, access/expiry laws, source ownership, offline rights or local-vs-hosted protected feature set requires documented protected amendment before implementing new direction.

## 10. Progress and current next action

- **Program:** 0/7 fixed slices (0%); no app security, Skool automations, licence service, releases or member entitlements were implemented by writing this plan.
- **Current slice:** S1 READY FOR RESEARCH; detailed tasks derived only when exact owner heads and implementation evidence are refreshed.
- **Key blocker for automatic commercial launch:** no currently verified authoritative Skool cancellation/renewal feed; a once-only New Paid Member event is inadequate.
- **Owner product tradeoff to decide at S2:** retain Skool native payments/affiliates with verified reconciliation, or adopt directly controlled billing to automate precise revocation; also choose whether premium features must always be online.
- **Scope isolation:** do not interrupt local Dashboard development, move release pins, create a new repository, promote branch head by date or add a second installer merely to start the plan.
