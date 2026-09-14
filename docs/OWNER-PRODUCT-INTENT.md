# AI-Verse Owner Product Intent and Operating Principles

**Status:** Canonical living owner-product-intent record  
**Updated:** 2026-09-14  
**Authority:** Product direction, UX intent, autonomy philosophy and owner preference. This document does not override implementation evidence, component ownership, security policy, migration safety or permission enforcement.

## Purpose

This document records the recurring product direction behind AI-Verse so future agents and contributors do not have to reconstruct the owner's intent from old chats.

It answers:

- what kind of product AI-Verse is trying to become;
- how invisible or visible the internal architecture should be to normal users;
- which optimizations should happen automatically;
- which actions should still require explicit user consent;
- how first-run/onboarding should feel;
- how the system should improve itself from ordinary daily use;
- what product behaviors the owner repeatedly rejects;
- how future product decisions should be checked against that direction.

This is a **living document**. When the owner materially clarifies or corrects product intent, update this file and propagate the change into the relevant canonical System/component contracts.

Implementation status must remain truthful. A behavior described here as the desired product experience is not considered shipped until the owning implementation and acceptance evidence prove it.

---

## 1. North-star experience

AI-Verse should feel like **one intelligent, persistent personal operating system with capable employees**, not like a collection of repositories, databases, agent frameworks or configuration screens.

The architecture may remain modular and strict internally, but the user should experience:

> install AI-Verse -> start talking/working -> AI-Verse learns how the user operates -> the backend quietly organizes and improves itself -> the user is asked only when a meaningful new commitment, permission, external effect or durable autonomous actor requires consent.

Normal users should not need to understand component names such as Brain, Memory, Data, Skills, Bots, Token, Connections, capability leases or canonical ownership before receiving value.

The system should explain those concepts only when the user asks, when troubleshooting requires it, or when an advanced user deliberately opens technical controls.

---

## 2. Invisible intelligence is preferred over configuration burden

When AI-Verse can safely infer and perform an **internal, reversible, bounded organizational improvement** from sufficient evidence, it should normally do so without asking the user to make a technical architecture decision.

The user should not be asked:

- whether something should be a workspace;
- whether repeated internal knowledge should become a Skill;
- whether recurring structured facts should live in Data;
- which canonical subsystem should own a datum;
- how internal context should be indexed;
- how safe internal backend organization should be optimized.

The user's job is to describe goals, work, preferences, constraints and desired outcomes.

The system's job is to choose the correct internal structure.

---

## 3. Current autonomy decisions

These are explicit owner decisions and should be treated as product-direction requirements.

| Detected situation | Desired default behavior |
|---|---|
| A substantial client/project/area repeatedly needs isolated context | **Create or evolve the appropriate workspace automatically** when the boundary is clear and doing so does not broaden authority |
| A workflow is repeated and is reusable | **Create/evaluate/use a reusable Skill automatically** when it is safe, internal, reversible, scoped and does not expand permissions/connections |
| Repeated information is clearly structured operational truth | **Create/evolve the appropriate Data structure automatically** when the change is additive/safe and owner rules allow it |
| A stable useful historical fact/preference/lesson should be remembered | Route it to the correct Memory/profile owner automatically when evidence and ownership rules allow |
| A complex one-off task benefits from parallel/specialist help | Temporary Workers may be created automatically within existing bounded authority |
| A responsibility should run on a future/recurring schedule | **Ask the user before creating/enabling the Automation** |
| A durable specialist/employee Bot would be useful repeatedly | **Ask the user before creating the permanent Bot** |
| New permission, credential, connection, external account or broader scope is required | Ask / follow explicit authorization flow |
| Destructive, irreversible, high-risk or materially costly action is required | Ask / follow the relevant approval boundary |
| Strategic authority would change | Require explicit owner-approved handover; never infer it from convenience |

The distinction is intentional:

> **internal organization and safe learning should be proactive; new ongoing autonomy, durable employees, external authority and consequential actions should be explicit.**

---

## 4. Do not confuse backend optimization with doing unrequested work

AI-Verse may proactively optimize its own internal organization from daily user interaction when the operation:

- stays inside already-authorized scope;
- does not create a new external side effect;
- does not create a future recurring obligation;
- does not create a durable autonomous employee;
- does not expand permissions or credentials;
- does not change strategic authority;
- is reversible or recoverable;
- preserves provenance and canonical-owner rules.

This does **not** authorize the system to invent user tasks or perform consequential work the user never requested.

For example:

- creating an internal workspace to keep a user's already-requested client work organized is backend optimization;
- creating an internal Skill from a repeatedly successful workflow is backend optimization;
- creating an additive Data schema for repeatedly tracked records is backend optimization;
- deciding to send emails every Monday is a new recurring responsibility and requires consent;
- creating a permanent specialist Bot is a new durable autonomous actor and requires consent.

---

## 5. The Brain/LLM should be used for intelligent adaptation, not security enforcement

The active capable model/runtime should be allowed to reason from ordinary daily input and identify useful internal improvements.

Examples:

- detect that multiple conversations belong to the same client;
- detect a repeated procedure;
- detect that information is naturally tabular/relational;
- detect duplicated or inefficient backend organization;
- detect when a temporary specialist is useful;
- detect when a recurring responsibility or permanent role would be valuable and propose it to the user.

However, model intelligence does not replace deterministic safety boundaries.

The model may **decide what optimization is useful**. Owner components and host policy must still enforce:

- scope;
- permissions;
- migration safety;
- protected ownership;
- approval requirements;
- external-action boundaries;
- destructive-operation guards;
- rollback/recovery;
- canonical ownership.

---

## 6. Grandma/Jarvis first-use target

The normal user should not have to learn the technical lifecycle vocabulary.

The technical system may internally retain:

`install -> setup -> onboard -> doctor -> open/use`

because those stages are valuable for reliability, testing, recovery and support.

The ordinary product experience should collapse them behind a simple first-run path where possible:

```text
Install AI-Verse
    -> install exact released components
    -> perform safe owner-controlled setup
    -> run health/doctor verification
    -> launch the conversational product
    -> ask only the minimum questions required to begin safely
    -> start helping
```

A normal user should not be told to manually run `setup` or `doctor` after installation unless:

- automatic setup cannot safely continue;
- migration/authorization is required;
- troubleshooting/advanced usage is requested.

Onboarding should be progressive and conversational, not a mandatory architecture questionnaire.

A preferred first interaction is closer to:

> What would you like help with?

Then learn missing information when it becomes relevant.

Deeper onboarding remains available for advanced users, migration, support or deliberate configuration.

---

## 7. Minimize questions

Before asking the user a question, ask:

1. Can the answer be inferred reliably from existing context/evidence?
2. Is this merely an internal technical choice AI-Verse should make itself?
3. Is the operation reversible and inside current authority?
4. Does the answer materially affect safety, external effects, permissions, costs, future recurring work or durable autonomous actors?

If 1-3 support automatic action and 4 is false, prefer acting and recording the decision rather than asking.

Ask when the answer is genuinely necessary for:

- authorization;
- external side effects;
- new recurring automation;
- durable Bot creation;
- strategic handover;
- destructive/irreversible operations;
- materially ambiguous workspace/privacy boundaries;
- meaningful cost/risk;
- credential/account access;
- user preference that cannot be safely inferred.

---

## 8. Progressive backend evolution

AI-Verse should become better organized as it is used.

A healthy long-term loop is:

```text
user works normally
    -> Brain/runtime observes bounded evidence
    -> classify useful persistent improvement
    -> route to canonical owner
    -> perform safe internal/reversible improvement automatically
       OR ask when the change crosses an approval boundary
    -> verify
    -> preserve provenance
    -> continue working
```

Examples of owner routing:

- workspace/current context -> OS;
- strategic goal/evaluation -> Brain;
- history/lesson -> Memory;
- structured current records -> Data;
- reusable procedure -> Skills;
- temporary collaboration -> Multiple Bots Workers;
- durable Bot -> Multiple Bots after user approval;
- recurring schedule -> Automations after user approval;
- connection/credential authority -> Connections/host authorization;
- usage/cost evidence -> Token.

The user should experience the result as increased usefulness, not as repeated subsystem configuration.

---

## 9. Product defaults should be smart but bounded

The desired product is not "ask before everything."

It is also not "silently do everything."

The target is **maximum useful autonomy inside already-granted, reversible, internal boundaries** and explicit consent at meaningful commitment/authority boundaries.

This principle should guide future default-mode decisions.

Where existing public-beta contracts are more conservative than this owner direction, record the difference as an implementation/product gap rather than silently rewriting safety policy.

Example: if Skills currently defaults to proposal-only creation of a new Skill, the implementation should not be described as satisfying the automatic-learning target until a safe auto-create/evaluate/promote path is implemented and accepted.

---

## 10. What the owner does not want

Avoid product drift toward:

- forcing users to understand the internal component architecture;
- asking permission for harmless internal organization;
- repeated setup/configuration questions that the system can answer itself;
- creating a workspace, Skill or Data structure as a visible ceremony when it can happen safely in the background;
- a giant monolithic repo that destroys modular component development;
- duplicate canonical owners;
- silent permission/authority expansion;
- silent recurring automations;
- silent creation of permanent Bots;
- destructive "self-improvement";
- upgrades that risk user state;
- technical correctness without a simple end-user path;
- documentation that describes an aspiration as if it is already implemented.

---

## 11. Modularity remains an implementation advantage

The owner wants AI-Verse components to remain independently improvable over time.

That modularity should not leak into ordinary UX.

The intended structure remains:

```text
independent component repositories
        -> exact accepted immutable releases
        -> AI-Verse Distribution
        -> one installable/updatable AI-Verse product
```

A user should not have to manually coordinate repositories.

Distribution and release automation should assemble compatible component versions and preserve user state across updates.

---

## 12. How to use this document in future work

Before a significant product, UX, onboarding, autonomy, learning, workspace, Data, Skills, Bot, Automation or Distribution decision:

1. read this document;
2. inspect current implementation evidence;
3. distinguish owner intent from what is actually shipped;
4. identify the canonical owning component;
5. preserve safety/authority laws;
6. implement the smallest owner-correct change;
7. add acceptance evidence;
8. update this document if the owner has materially refined the direction;
9. propagate the change into the relevant canonical contract/blueprint;
10. record the meaningful change in `docs/SYSTEM-CHANGELOG.md`.

If a future request from the owner conflicts with an older statement here, the newer explicit clarification wins after checking that it does not require violating non-negotiable security, data-integrity or authority laws. Update this file rather than leaving contradictory product intent scattered across chat history.

---

## 13. Current known intent-versus-implementation gaps

As of this document's creation, the following product-intent areas require continued implementation/acceptance rather than documentation-only claims:

- one-action first-run that hides normal `setup` and `doctor` from ordinary users;
- progressive conversational onboarding instead of requiring all deep intake questions before first value;
- runtime detection of recurring scopes and automatic workspace creation/evolution;
- safe automatic creation/evaluation/promotion of new internal Skills under bounded policy;
- runtime detection of recurring structured truth and automatic safe Data organization;
- proposal/confirmation UX for new recurring Automations;
- proposal/confirmation UX for durable permanent Bots;
- final whole-product acceptance proving these behaviors through the real Distribution/Gateway product path.

These are product gaps, not reasons to collapse component ownership or bypass permission/migration rules.
