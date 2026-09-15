> **Dashboard owner decision, 2026-09-15:** Use Builderz Labs Mission Control as the initial AI-Verse Dashboard shell, preserve the existing AI-Verse Dashboard foundations, connect through the canonical AI-Verse Gateway first, audit every Mission Control feature before stripping it, and progressively replace Mission Control-owned domain state with AI-Verse owner-backed projections. Canonical plan: [DASHBOARD-CANONICAL-MISSION-CONTROL-ADOPTION-PLAN-2026-09-15.md](DASHBOARD-CANONICAL-MISSION-CONTROL-ADOPTION-PLAN-2026-09-15.md).

# AI-Verse Owner Product Intent and Operating Principles

**Status:** Canonical living owner-product-intent record  
**Updated:** 2026-09-15  
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

### Semantic migration clarification

When the user transfers accumulated context from another assistant, memory file, notes archive, USER.md/MEMORY.md/SOUL.md-style source, or raw pasted contents:

- filenames are optional hints; classify by the real-world meaning of the content;
- automatically route high-confidence facts through the existing canonical owners;
- do not copy foreign file structure or foreign assistant instructions into AI-Verse authority;
- if information matters but its real-world meaning is genuinely ambiguous, preserve bounded provenance-backed unresolved evidence and ask a targeted clarification instead of dropping it;
- clarification questions must ask about the user's world, such as whether something is a current client, past client, one-off project, ongoing project, contact, stable preference, historical fact or current truth;
- never ask the user whether AI-Verse should create a workspace, choose Memory vs Data, create a Skill, select an owner, or make another internal architecture decision;
- after the user clarifies meaning, AI-Verse chooses the correct internal structure and resumes the same owner-routed import;
- batch related questions and do not re-ask facts already explicit in the source;
- unresolved questions must remain resumable after interruption/restart without becoming a second canonical profile, Memory, Data or workspace store.

The product rule is:

> **Ask the user what the real thing means. Never ask the user how AI-Verse should store it.**

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


## 9A. Context and memory intelligence direction

AI-Verse should become better at deciding **how much context to load and how deeply to retrieve** without asking the user to manage memory, summaries, retrieval depth or graph structure.

The owner wants long-lived AI-Verse installations to remain fast and intelligent even after years of conversations, workspaces, memories, Skills, Data and Bots.

The preferred direction is a progressive context ladder:

```text
current task + current scope + recent raw context
        -> tiny orientation map/catalog
        -> relevant session/fold summaries
        -> exact targeted owner records
        -> bounded related-context expansion when useful
        -> exact original source/evidence when precision requires it
```

Most ordinary turns should stop at the shallowest layer that is sufficient.

Normal users should never be asked:

- what recall depth to use;
- whether to unfold context;
- whether to load a memory graph;
- whether to inspect a session digest;
- whether to use summaries versus source;
- which internal retrieval subsystem should answer.

The runtime should choose automatically.

### Lossless compression principle

Long conversation history may be compressed into hierarchical summaries for working context, but compression must not destroy access to the original source.

A summary is a navigation/orientation aid, not the final authority for exact-sensitive facts.

For exact prices, numbers, dates, commands, paths, IDs, configuration, quotations, permissions or contractual/state-transition facts, AI-Verse should be able to descend to original authoritative evidence before relying on the answer.

> **Summary is orientation. Source is evidence.**

### Derived context, not duplicate truth

Compact maps, catalogs, summary trees, relationship edges and retrieval indexes should remain derived/rebuildable wherever possible.

They must not become competing canonical owners.

The existing ownership model remains authoritative:

- Memory owns historical memory;
- Gateway owns live session/runtime context;
- OS owns workspace/scope/current operating context;
- Brain owns goals/strategy/evaluation;
- Data owns structured current truth;
- Skills owns executable capability packages;
- Multiple Bots owns coordination identities/state.

If a derived context artifact can be deleted and rebuilt from canonical owners, that is preferred.

### Borrow ideas, not architectures

External systems such as Kylon, Graft and Kilo may inspire improvements, but AI-Verse should adopt only ideas that measurably improve its existing design.

Current desired candidates include:

- Kylon-style hierarchical, reversible conversation folding and cheap branch/fork catalogs where they improve Gateway context scaling;
- Graft-style compact orientation maps, source fingerprints, bounded relationship traversal and summary-to-source escalation;
- Kilo-style session digests, selective consolidation/promotion and targeted recall before heavy historical retrieval.

Do not import an external subsystem wholesale.

Every borrowed mechanism must justify itself through lower context cost, better recall/accuracy, stronger continuity, safer recovery, better scalability or lower user-facing complexity.

If a feature adds architecture without measurable benefit, reject it.

### Long-term memory behavior

AI-Verse should not remember everything indiscriminately.

A healthy pattern is:

```text
normal conversation/work
    -> bounded session continuity
    -> concise session digest when useful
    -> evaluate durable value
    -> promote only useful historical facts/lessons/corrections/workflows
    -> retain provenance and exact-source references
```

Transient chatter should remain transient.

The system should become more useful over time without allowing memory volume to make retrieval progressively noisier or more expensive.



## 9B. Learn from user friction without making the user write bug reports

A future AI-Verse should be able to recognize explicit corrections, repeated repair attempts and clear dissatisfaction as useful product/learning evidence.

The desired experience is that a user can simply say things such as:

- "No, that's not what I meant."
- "Why did you remember that?"
- "That Skill did this wrong."
- "You put that in the wrong place."

and AI-Verse can preserve a compact local record of the relevant failure context automatically rather than requiring the user to reconstruct a technical bug report later.

This should remain **local-first and privacy-preserving**.

For member installations, any upstream contribution to improve AI-Verse must be opt-in and sanitized. Do not send raw conversations, private Memory, business Data, credentials, files or unrelated surrounding context by default.

The preferred future pattern is:

```text
friction/correction
    -> local structured evidence
    -> owner-correct repair/learning candidate when safe
    -> optional sanitized upstream product feedback with consent
```

The system should distinguish explicit user correction from merely inferred frustration. Model-detected frustration is evidence, not authority, and must never by itself justify destructive state changes, permission changes or silent global product updates.


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
- documentation that describes an aspiration as if it is already implemented;
- forcing users to understand retrieval depth, summary trees, fold cards, context maps or memory graphs;
- another canonical graph/vector store merely because an external project uses one;
- summarizing every trivial interaction or promoting every conversation into durable Memory;
- context systems that become larger or more expensive than the problem they solve.

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

## 11A. Owner operating style and decision preferences

When interpreting future product decisions, the recurring owner pattern is:

- prefer **invisible usefulness** over visible configuration;
- prefer extending/wiring existing canonical owners over creating new subsystems;
- benchmark strong external implementations, then take only the parts that improve AI-Verse;
- require implementation and acceptance evidence, not documentation-only claims;
- prefer one bounded implementation slice at a time with persistent GitHub plans rather than relying on chat/agent memory;
- allow intelligent internal optimization automatically when it is reversible and inside existing authority;
- ask only at meaningful commitment, permission, recurring-autonomy, durable-actor, destructive or external-effect boundaries;
- preserve modular repositories internally while presenting one coherent AI-Verse product externally;
- optimize for a system that gets smarter and better organized through ordinary daily use without making the user become its administrator.

A future agent should treat repeated corrections from the owner as product-direction evidence. When a newer explicit correction changes an older preference, update this file so stale chat history does not remain the de facto specification.



## 11B. Current product scope and interface priority

The current product target is deliberately **single-user first**.

Near-term AI-Verse should optimize for:

- one owner/operator;
- primarily local use;
- optional private VPS/VPN access;
- no requirement for public multi-user accounts, organization administration, human-team invitations or enterprise identity before the single-user product is excellent.

Multi-user collaboration, public SaaS account systems, human-team membership, enterprise RBAC/SSO and similar capabilities remain valid later-product directions, but they are deliberately low priority unless the owner explicitly promotes them.

The immediate product-layer priority is to make the existing intelligence **visible and usable through one coherent interface**, rather than continuing to add backend subsystems.

In particular, Multiple Bots must stop feeling like an invisible backend component.

The normal product should make the relationship clear:

```text
Main AI-Verse agent / chat
        +
visible AI team / Bots
        +
temporary Workers when needed
        +
current workspace / work status
```

The owner wants the primary chat to remain the main interaction surface while a nearby Bot/team surface makes permanent Bots, their roles, availability, activity, delegated work and relevant status easy to discover and use.

This does not require turning every backend object into a UI panel.

The first interface should expose only the concepts that materially help the owner work:

- primary chat;
- current workspace/scope;
- permanent AI employees/Bots;
- temporary Worker activity when relevant;
- active/delegated work and meaningful status;
- approvals/attention when required.

Deep engine details, canonical-owner internals, raw telemetry and low-level lifecycle machinery should remain behind advanced/debug views.

### Interface-before-expansion rule

After the currently active implementation tracks reach safe stopping points, prefer building the thin AI-Verse product shell over starting another broad capability expansion.

The shell should consume existing Gateway, Multiple Bots, OS and owner APIs rather than becoming a new canonical state owner.

Open WebUI or another borrowed chat shell may remain useful for temporary dogfood, but it is not the final product answer if it hides AI-Verse-specific concepts such as the visible AI team, Bot roles, work delegation and owner-backed status.

The near-term goal is not a giant Dashboard.

It is a focused single-user shell that makes the already-built system understandable and usable.

## 11C. Dashboard MVP and desktop-first shell priority

The owner has explicitly promoted the first usable AI-Verse interface ahead of the broader Dashboard roadmap.

The immediate target is the **smallest chat-first product shell**, not the complete Control Room.

The desired first product is:

- one shared browser/desktop frontend rather than separate UI implementations;
- a macOS DMG first, using the same frontend as the browser build;
- automatic start/attachment of the canonical local AI-Verse Gateway when the desktop app opens or a system is selected;
- native selection and registration of one or multiple compatible AI-Verse OS folders;
- recognition of an already-installed AI-Verse structure without rewriting it;
- an explicit Install AI-Verse path for a new folder, routed through canonical Distribution rather than a Dashboard-specific installer;
- primary Chat as the first working surface;
- visible current system/workspace scope;
- supported ChatGPT/runtime authentication without making Dashboard the credential owner;
- strict isolation when several AI-Verse OS installations are registered;
- a stack deliberately chosen so Bots, Work, Approvals, Automations, Brain, Token, Apps, detachable panels and other future Dashboard features can be added without replacing the shell.

The desktop host should remain thin. Native-only responsibilities such as folder selection, process supervision, secure local secret handling and install/bootstrap actions belong at the host edge. Canonical run/session/domain behavior remains in Gateway and the relevant owner components.

The current preferred stack direction is React 19 + TypeScript + Vite for the shared UI and Tauri 2 for the macOS desktop host.

The current AI-Verse Gateway binds one system root per Gateway configuration. The first multi-system Dashboard should preserve that boundary by supervising isolated Gateway instances per registered OS when needed, rather than turning Gateway into a multi-root canonical owner.

For the first supported ChatGPT login path, prefer an official managed runtime authentication surface such as Codex rich-client/App Server authentication behind a replaceable Gateway runtime adapter. Dashboard should not implement or persist raw ChatGPT OAuth credentials itself.

The older Dashboard sequencing idea that desktop packaging should wait until every Dashboard phase is complete is superseded by this newer explicit owner direction. A thin desktop wrapper is now part of the immediate dogfood path.

Canonical implementation plan:

- docs/DASHBOARD-MVP-WEB-DESKTOP-PLAN-2026-09-15.md

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
- final whole-product acceptance proving these behaviors through the real Distribution/Gateway product path;
- progressive context retrieval that starts with tiny orientation and descends only as needed;
- first-class session digests/selective durable promotion where useful;
- lossless hierarchical conversation folding with exact-source recovery in Gateway if benchmarks prove it beneficial;
- derived compact context maps/relationships only where they measurably improve retrieval without creating duplicate canonical truth;
- a focused single-user product shell that keeps chat primary while making Multiple Bots / AI employees visible and directly usable;
- clear runtime/product wiring showing when permanent Bots, temporary Workers, Rooms/Threads and delegated work are used instead of leaving Multiple Bots as an invisible backend capability.

These are product gaps, not reasons to collapse component ownership or bypass permission/migration rules.
