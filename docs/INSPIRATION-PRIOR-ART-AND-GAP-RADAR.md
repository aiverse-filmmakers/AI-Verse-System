# AI-Verse Inspiration, Prior-Art, and Competitive Gap Radar

**Status:** Canonical living research index  
**Date:** 2026-09-15  
**System baseline:** `aiverse-filmmakers/AI-Verse-System@303b8ed1e24a61304e74ca398ce12b815feb6bef`  
**Purpose:** keep every meaningful AI-Verse inspiration in one place, expose capabilities that other systems currently do better or more completely, and maintain a ranked radar of ideas worth evaluating without copying another architecture wholesale.

## 1. Why this document exists

AI-Verse has already been designed with a large number of capabilities and unusually strict ownership boundaries. That creates a useful but dangerous blind spot:

> A system can be strong at everything its designer has already thought about and still miss an entire category of capability that another project treats as obvious.

This document exists to apply the rule:

> **We do not know what we do not know.**

The goal is therefore not to prove AI-Verse is better than other systems. The goal is to keep looking for things other systems have already solved, identify the parts AI-Verse genuinely does not have, and decide which ideas deserve future implementation.

This is an inspiration and gap radar, not an implementation mandate.

A feature belongs here when one or more of these are true:

- another project has a useful capability AI-Verse does not currently implement;
- another project has a materially better product experience for a capability AI-Verse already has architecturally;
- another project has a stronger security, runtime, distribution, evaluation, or interoperability primitive;
- an external design reveals a category AI-Verse has not considered;
- an older AI-Verse document already used the project as research or inspiration and that provenance should not be lost.

## 2. Research method and truth rules

This comparison was made against current System evidence, not against memory of what AI-Verse is supposed to become.

The AI-Verse baseline included:

- `docs/FINAL-AI-VERSE-BLUEPRINT.md`
- `docs/OWNER-PRODUCT-INTENT.md`
- `docs/DOGFOOD-UX-AND-PLATFORM-COMPLETENESS.md`
- `docs/IDEA-INBOX.md`
- `docs/GOALS-BENCHMARK-AND-CONTRACT.md`
- `docs/SELF-LEARNING-BENCHMARK-AND-CONTRACT.md`
- `docs/CONTEXT-LADDER-AND-LOSSLESS-MEMORY-IMPLEMENTATION-PLAN.md`
- `docs/DASHBOARD-CANONICAL-MISSION-CONTROL-ADOPTION-PLAN-2026-09-15.md`
- all ten current `components/*/COMPONENT-SPEC.md` files;
- existing Interface Designer and Video Editor upstream-pin research.

External repositories were reviewed from their current public repository documentation on 2026-09-15. For the most important claimed gaps, implementation-oriented architecture/security/runtime documents were also checked where available.

### Confidence labels

- **VERIFIED-DOCS:** supported by current project documentation that points to concrete implementation surfaces.
- **README-CLAIM:** claimed by the external project README, but not independently accepted as production-grade by AI-Verse.
- **SYSTEM-PRIOR-ART:** already documented as an AI-Verse inspiration in System.
- **AI-VERSE-CURRENT:** implemented and evidenced in AI-Verse.
- **AI-VERSE-GAP:** explicitly missing or plan-only in current AI-Verse evidence.
- **AI-VERSE-INTENDED:** designed or planned, but not yet current implementation.

### Non-copy rule

AI-Verse should continue to follow its existing principle:

> **Borrow ideas, not architectures.**

No external project earns canonical ownership inside AI-Verse merely because it has a useful feature.

Every adopted idea must still obey:

- one canonical owner per responsibility;
- no hidden duplicate truth;
- installation is not authority;
- scope and permission are rechecked at the effect boundary;
- stateful migration moves authority, not just bytes;
- Dashboard and Apps do not silently become databases;
- Memory, Data, Brain, Skills, Bots, Automations, Connections, Token and OS keep their declared boundaries;
- benchmark before importing a mature behavior when measurable evidence is possible.

---

# 3. Executive finding

The biggest opportunities are **not** another memory system, another cron engine, another swarm framework, or another generic vector database.

AI-Verse is already unusually strong in:

- canonical ownership and source-of-truth separation;
- workspace isolation and scope;
- Brain goal/strategy boundaries;
- historical Memory versus current Data separation;
- immutable Skill generations and governed self-learning;
- durable Bot/Worker/Task/Room coordination;
- restart-safe Automations;
- truthful Token/cost accounting;
- migration/state-preservation laws;
- exact-source context recovery and the progressive context ladder;
- release and acceptance discipline.

The strongest external advantages are concentrated elsewhere:

1. **Agent computers and sandboxed execution**
2. **A real Apps product, not only Apps architecture**
3. **A real Connections product with broad integrations**
4. **Integrated runtime security at the tool/computer boundary**
5. **One unified whole-system readiness and security audit**
6. **Multi-channel reachability and voice**
7. **Better visual goal-to-plan execution surfaces**
8. **Source-backed knowledge/wiki experiences and multimodal memory ingestion**
9. **Portable execution backends and hibernating agent environments**
10. **Recipe/app/agent marketplaces and one-click reproducible setups**
11. **Cross-machine agent federation and enterprise collaboration, later**
12. **Longitudinal self-evolution evaluation and trajectory research tooling**

These are the areas where other systems most clearly expose things AI-Verse either does not yet implement or does not yet productize.

---

# 4. Priority ranking: what AI-Verse should evaluate next

The ranking below respects current owner direction. The Mission Control Dashboard adoption path remains the immediate active product track and should not be derailed by a new architecture project.

| Rank | Missing advantage | Best references | Current AI-Verse state | Recommendation |
|---|---|---|---|---|
| **1** | **Universal Agent Computer / Sandbox execution contract** | Celesto/SmolVM, Osaurus, ZeroClaw, Hermes | AI-Verse explicitly says terminal/computer/browser execution is external-runtime responsibility today and there is no universal sandbox contract | **HIGH. Evaluate immediately after the current Dashboard proof reaches a safe stopping point.** Add a provider contract, not a new canonical truth owner. |
| **2** | **Connections v1 that actually executes real external capabilities** | HolaOS, Gawkbot, ZeroClaw, Hermes, Pipedream, Nango, Composio | Connections is currently architecture/research only | **HIGH. Already one of the clearest system gaps.** Ship one deep provider path, then broaden through managed OAuth/MCP adapters. |
| **3** | **Apps v1 with live, agent-operable, user-takeover surfaces** | HolaOS, Gawkbot, Mission Control | Apps implementation has not started | **HIGH.** Build on canonical Data/Connections/Skills/Gateway rather than app-local truth. |
| **4** | **Execution security floor for tools, browsers and sandboxes** | ZeroClaw tool receipts, Ruflo AI Defence, Celesto network isolation | AI-Verse has strong approval/authority laws but fragmented receipts and no universal sandbox/tool policy | **HIGH.** Treat prompt injection, PII, tool-result authenticity, network policy and untrusted code as runtime security contracts. |
| **5** | **One whole-system MetaHarness-style doctor and drift audit** | Ruflo MetaHarness | AI-Verse has excellent component doctors/audits but explicitly lacks one end-to-end command proving all layers | **HIGH-MEDIUM.** Compose existing owner evidence into one read-only system readiness/security report rather than inventing new truth. |
| **6** | **Multi-channel Gateway and voice front doors** | Hermes, ZeroClaw, HolaOS | channels/notifications are future product work; current owner priority is desktop/browser first | **MEDIUM.** Add after Dashboard core is usable. Telegram is likely the highest-value first non-UI channel. |
| **7** | **Visual goal-to-plan execution graph with adaptive replanning** | Ruflo GOAP, LifeOS Current State -> Ideal State | Brain owns goals/gaps/initiatives and durable continuation, but no comparable visual action-state planner/product surface is established | **MEDIUM.** Prototype as a derived Brain/Dashboard plan view. Never expose private chain-of-thought. |
| **8** | **Source-backed Knowledge Wiki / research surface** | Gawkbot, EverOS, LifeOS | AI-Verse has canonical knowledge/memory/data and provenance but no equivalent polished wiki experience | **MEDIUM.** A rebuildable Dashboard/App projection could make existing evidence dramatically easier to use. |
| **9** | **Multimodal durable ingestion into Memory/Knowledge** | EverOS | current AI-Verse memory/context work is strong, but no equally clear first-class image/PDF/audio/office ingestion pipeline is documented | **MEDIUM.** Evaluate after context-ladder completion. Keep original files/source refs authoritative. |
| **10** | **Portable execution backends and hibernating environments** | Hermes terminal backends, Celesto snapshots | Multiple Bots supports external runtimes, but AI-Verse does not own a normalized computer lifecycle with snapshot/hibernate semantics | **MEDIUM.** Likely part of Rank 1 rather than a separate component. |
| **11** | **Full foreign-agent migration adapters** | Hermes OpenClaw migration | AI-Verse now has strong semantic user-context migration, but not a complete importer for foreign skills, allowlists, credentials, runtime settings and assets | **MEDIUM.** Build format-specific adapters on top of the semantic migration contract, never import foreign authority blindly. |
| **12** | **One-click recipes / Combos / reproducible workspace setups** | HolaHub, HolaOS Combos, Ruflo plugins | Skills exist; Apps/Connections are not yet productized enough to compose full recipes | **MEDIUM-LOW until Apps + Connections exist.** Later this could become a major ecosystem advantage. |
| **13** | **Trajectory export and longitudinal self-evolution evaluation** | Hermes, EverMind research stack, Ruflo | AI-Verse has strong acceptance/evaluation contracts but less explicit trajectory-training/evolution benchmarking as a user-facing research surface | **MEDIUM-LOW.** Useful for improving AI-Verse itself, not a first user feature. |
| **14** | **Zero-trust cross-machine agent federation** | Ruflo Federation | remote and A2A support exist in bounded forms; human/team/federated product scope is deliberately later | **LOW near-term, potentially HIGH later.** Keep on radar without distracting from single-user excellence. |
| **15** | **Enterprise accounts, RBAC/SSO/SCIM and public multi-tenancy** | HolaOS enterprise, Gawkbot sharing, Ruflo federation | explicitly deferred by current owner intent | **LOW now.** Do not spend current product cycles here. |

## Priority dependency view

A sensible future sequence is:

```text
Current Mission Control / Dashboard proof
        |
        v
Connections v1
        |
        +--> Agent Computer / Sandbox provider contract
        |
        v
Apps v1 + live surfaces
        |
        +--> source-backed Knowledge / Data views
        +--> recipe / Combo packaging
        |
        v
multi-channel + voice
        |
        v
advanced planning / federation / enterprise
```

Security and whole-system readiness auditing should be improved continuously alongside these stages rather than postponed to the end.

---

# 5. User-supplied inspiration repositories

## 5.1 Gawkbot

**Repository:** https://github.com/najmuzzaman-mohammad/gawkbot  
**License note:** Sustainable Use License. Treat as product/UX inspiration unless licensing is reviewed for a specific reuse case. The current Dashboard adoption plan already records this restriction.

### What it does particularly well

Current project documentation describes a job-oriented system where the user describes a workflow and Gawkbot creates a Bot around that workflow with:

- a live build feed;
- a real product surface rather than only chat;
- routines with versioned prompts, run history and transcripts;
- Bot-authored tools;
- source-cited knowledge pages;
- per-Bot typed data surfaces;
- approval gates for mutating external actions;
- visible cost/tokens/runs;
- broad integration coverage;
- multiple workspaces and sharing.

Its architecture also makes several useful implementation choices:

- isolated git worktrees per Bot;
- fresh runtime session per turn with explicit continuity packets;
- role-shaped/scoped MCP tool surfaces;
- unfinished-work replay after restart;
- broker-driven wakeups rather than naive polling.

### What AI-Verse already has

AI-Verse already has stronger or comparable foundations for:

- permanent Bots versus temporary Workers;
- Tasks, Rooms, Threads, Team Runs and handoffs;
- restart-safe coordination;
- approval boundaries;
- recurring Automations;
- Token usage/cost truth;
- workspace isolation;
- canonical Data ownership;
- stronger one-owner-per-responsibility laws.

### What Gawkbot currently has that AI-Verse does not

**AI-VERSE-GAP:**

1. **A shipped workflow -> Bot -> live microapp/product path.** AI-Verse Apps is still architecture only.
2. **A polished job-first UI where each Bot visibly owns an outcome surface.**
3. **Source-cited Bot knowledge pages as a first-class product experience.**
4. **Broad ready-to-use integration UX in the same product flow.**
5. **Per-Bot data and routine views already wired into the product.**
6. **One simple build experience that turns a natural-language workflow into a visible operational Bot.**

### Important correction

Gawkbot should **not** be credited with a shipped per-Bot VM computer architecture. Its own comparison currently says Bot computers are not yet implemented and describes per-Bot directories/tool allowlists instead.

### Best idea to borrow

Borrow the **job-first product metaphor**:

> “Describe the job, watch the Bot get built, then manage the outcome through a real surface.”

Implement it through AI-Verse Apps, Data, Bots, Connections, Automations and Token rather than duplicating Gawkbot's backend ownership.

**Priority:** HIGH for product UX, after core Dashboard/Apps/Connections wiring.

---

## 5.2 ZeroClaw

**Repository:** https://github.com/zeroclaw-labs/zeroclaw  
**License:** MIT OR Apache-2.0 according to current repository metadata.

### What it does particularly well

ZeroClaw is a concrete local agent runtime with:

- 20+ model/provider options;
- 30+ communication channels;
- shell/browser/HTTP/hardware/MCP tools;
- OS-level sandbox options such as Landlock, Bubblewrap, Seatbelt and Docker;
- default supervised autonomy;
- provider fallback/routing;
- Gateway + Dashboard;
- an SOP engine with deterministic procedures, trigger matching, approval gates and auditable/resumable run state;
- ACP editor/IDE integration;
- cryptographic tool receipts.

Its Tool Receipts design is especially notable. Successful tool results can receive HMAC-SHA256 receipts using an ephemeral runtime key, making fabricated “I ran this tool” claims detectable inside the active receipt scope.

### What AI-Verse already has

AI-Verse already has:

- stronger canonical owner separation;
- robust Automations with restart/retry/dead-letter semantics;
- explicit approval/authority intersections;
- Gateway;
- Bot/Worker coordination;
- MCP as a first-class intended interoperability target;
- strong receipt/provenance concepts.

### What ZeroClaw has that AI-Verse does not

1. **One concrete universal runtime sandbox layer** with multiple host isolation mechanisms.
2. **Cryptographic per-tool result receipts** as a standard runtime primitive.
3. **A very broad first-class channel layer** already integrated into one agent runtime.
4. **A concrete SOP execution engine** for deterministic multi-step event-triggered procedures. AI-Verse Automations owns cadence/triggers but is not a general SOP/workflow engine.
5. **ACP as a concrete editor/client interoperability surface.**
6. **Provider fallback chains/routing** as an explicit runtime feature.

### Best ideas to borrow

- tool-result authenticity receipts;
- one normalized sandbox/tool policy contract;
- resumable deterministic SOPs where a reusable Skill is too model-guided and an Automation alone is too small;
- ACP compatibility if it materially improves editor/client portability.

Do **not** create a second scheduler. Any SOP trigger cadence should still compose with AI-Verse Automations.

**Priority:** HIGH for sandbox/security; MEDIUM for SOP/ACP.

---

## 5.3 EverOS

**Repository:** https://github.com/EverMind-AI/EverOS

### What it does particularly well

EverOS is primarily a local-first memory runtime rather than a complete OS.

Current documentation describes:

- canonical readable Markdown memory;
- local SQLite and LanceDB indexes;
- conversations, files and agent trajectories;
- separate user `episodes/profile` and agent `cases/skills` tracks;
- granular search by user, agent, app, project and session;
- an editable source-backed Knowledge Wiki;
- offline memory evolution that clusters episodes and refines profiles/skills;
- optional hybrid/vector/reranked retrieval;
- multimodal file ingestion for images, PDFs, audio and office documents;
- a wider EverMind research stack around hierarchical memory, sparse attention, longitudinal memory evaluation and agent self-evolution benchmarks.

### What AI-Verse already has

AI-Verse already has strong advantages in:

- current truth versus history separation;
- Memory provenance/supersession;
- Data as structured current truth instead of overloading Memory;
- self-learning routed into Skills;
- context-ladder progressive retrieval;
- exact-source escalation;
- bounded neighbor expansion backed by benchmark evidence;
- no indiscriminate “remember everything” design.

### What EverOS has that AI-Verse does not clearly have

1. **First-class multimodal durable ingestion** across image/PDF/audio/office formats.
2. **A polished editable source-backed Knowledge Wiki.**
3. **A simple Markdown-native user editing experience** for memory/knowledge.
4. **A clearly packaged longitudinal memory/evolution benchmark ecosystem.**
5. **Portable user/agent/app/project/session memory APIs** already positioned as a standalone memory product.

### Best ideas to borrow

- multimodal ingest with exact original-file provenance;
- a Knowledge Wiki projection over AI-Verse Memory/Knowledge/Data;
- longitudinal memory quality benchmarks, especially “does this system become more useful without becoming noisier?”

Do not replace AI-Verse Memory with a second Markdown/vector store.

**Priority:** MEDIUM.

---

## 5.4 LifeOS

**Repository:** https://github.com/danielmiessler/LifeOS

### What it does particularly well

LifeOS has one of the clearest user-facing mental models:

> **Current State -> Ideal State**

Its documented system includes:

- TELOS/personal context;
- goal/ideal-state artifacts;
- an Observe -> Think -> Plan -> Build -> Execute -> Verify -> Learn loop;
- complexity/tier selection;
- Cortex memory;
- Atlas asset graph;
- Ledger change tracking;
- Pulse daemon for voice, hooks, observability, cron, dashboard/wiki APIs and optional message bridges;
- Skills;
- intelligent routing;
- self-improvement;
- a Hermes sidecar as another front door;
- AI-driven installation.

### What AI-Verse already has

AI-Verse Brain directly adopted important LifeOS ideas already:

- Current State -> Ideal State;
- durable direction;
- success/verification;
- persistent goals.

AI-Verse deliberately rejected or changed:

- one rigid universal algorithm;
- duplicate goal stores;
- domain-specific root ontology.

AI-Verse also already has richer component ownership separation than a single-harness design.

### What LifeOS still does better or differently

1. **A clearer user-facing life/goal narrative** around Current State -> Ideal State.
2. **Voice as an integrated first-class product surface.**
3. **A unified asset graph concept** that makes active artifacts visible as a live system.
4. **A concrete complexity-tier routing idea** for deciding when a task needs minimal/native/full reasoning machinery.
5. **A highly integrated “one DA” product identity** even though the implementation is composed from many subsystems.

### Best ideas to borrow

- expose Brain goals/gaps in a simpler Current -> Ideal product view;
- evaluate a derived live asset map for important workspace artifacts;
- benchmark whether explicit complexity tiers improve cost/latency without adding brittle prompt choreography.

Do not import the Pulse monolith or a rigid Algorithm if AI-Verse's existing owners can compose the same user experience.

**Priority:** MEDIUM for goal UX; LOW-MEDIUM for the rest.

---

## 5.5 HolaOS

**Repository:** https://github.com/holaboss-ai/holaOS  
**License note:** Modified Apache-2.0. Review its modification before direct code reuse.

### What it does particularly well

HolaOS exposes a compelling “apps and agent side by side” workspace:

- real interactive app surfaces beside the agent;
- the user can operate the app manually and the agent sees the updated context;
- the agent can operate the app and the user can watch/take over;
- one-click app marketplace;
- arbitrary URL + MCP-backed app surfaces;
- 50+ OAuth integrations;
- Slack/Feishu/DingTalk/WeChat context;
- Skills and MCP;
- “Combos” that package Skills + Integrations together;
- multiple agent runtimes over the same workspace/memory/tools;
- local-first memory;
- browser operation;
- generation models;
- schedule/trigger automation;
- HolaHub recipes that expose not only output but the ingredients/session used to create it.

### What AI-Verse already has

AI-Verse already has the stronger ownership model that would prevent a workspace shell from becoming the hidden source of truth.

It already has:

- Apps architecture;
- Connections architecture;
- Skills;
- Data;
- Bots;
- Gateway;
- Automations;
- Dashboard plan;
- local-first direction;
- multiple runtime compatibility.

### What HolaOS has that AI-Verse does not

1. **A real Apps implementation with live interactive surfaces.**
2. **Bidirectional UI-context sync between user interaction and agent context.**
3. **A mature in-workspace app marketplace.**
4. **One-click Combos that compose capability + connection setup.**
5. **Broad OAuth integration UX already productized.**
6. **Direct IM context integration as a normal user feature.**
7. **A community recipe platform where setups are reproducible and inspectable.**
8. **A first-class browser inside the workspace.**

### Best ideas to borrow

This is one of the highest-value product references for AI-Verse Apps + Dashboard.

The strongest candidate is:

> **An app surface is not merely output. It is a live shared workspace between the human and the agent.**

AI-Verse can improve on this by keeping all business truth with Data/Connections/other canonical owners and treating app UI state as a projection.

**Priority:** VERY HIGH for Apps product design.

---

## 5.6 Osaurus

**Repository:** https://github.com/osaurus-ai/osaurus  
**License:** MIT.

### What it does particularly well

Osaurus is a native macOS harness with concrete local execution machinery.

Current project docs describe:

- agents with their own prompts/memory/theme;
- automatic tool/Skill selection;
- agent working folders;
- file/search/git tools;
- a model-driven task/todo execution loop with verification;
- an isolated Linux VM sandbox using Apple virtualization/container technology;
- a full development environment inside the sandbox;
- per-agent persistent `SOUL.md`;
- per-agent plugins;
- host bridge over vsock;
- path/network/rate-limit security;
- private per-agent SQLite databases;
- a constrained single “next run” self-scheduling slot;
- opt-in SQLCipher storage;
- native Swift/SwiftUI desktop experience;
- plugin ABI and MCP surfaces.

### What AI-Verse already has

AI-Verse already has stronger:

- semantic ownership boundaries;
- Data versus Memory separation;
- Automations ownership;
- Bot/Worker coordination;
- Skill packages;
- workspace scoping.

### What Osaurus has that AI-Verse does not

1. **A productized per-agent isolated Linux development environment on macOS.**
2. **A normalized agent sandbox toolset and lifecycle.**
3. **A visible sandbox management/diagnostics UI.**
4. **A constrained agent “schedule my next run” primitive.**
5. **Per-agent structured private DB tooling already surfaced in-product.**
6. **A native cryptographic identity/storage layer tied to the desktop harness.**

### Best ideas to borrow

- the sandbox lifecycle and management UX;
- safe host-to-sandbox bridges;
- read-only/default constrained mounting;
- explicit tool exposure based on granted agent capability.

Do not let per-agent databases become a second Data owner. If AI-Verse exposes agent-local scratch/state, it must remain coordination/runtime state or be routed into Data when it becomes canonical operational truth.

**Priority:** HIGH as an Agent Computer reference.

---

## 5.7 Celesto / SmolVM

**Repository:** https://github.com/CelestoAI/celesto  
**License:** Apache-2.0.

### What it does particularly well

Celesto's SmolVM is not a full agent OS. It is a focused execution primitive, and that is precisely why it is valuable.

Current docs describe:

- secure persistent microVMs for agents;
- roughly sub-second VM startup targets;
- hardware isolation;
- Firecracker on Linux and QEMU/macOS support;
- configurable outbound network restrictions;
- browser sandboxes;
- visible browser viewers and VNC/CDP interfaces;
- Linux “computer” environments with desktop apps;
- macOS desktop sandboxes in preview;
- Windows guests;
- read-only host directory mounts by default;
- explicit writable-mount opt-in;
- snapshot/pause/resume;
- persistent files/state/processes across sessions;
- coding-agent presets for Claude Code/Codex/Pi;
- benchmark tooling for startup, interactivity, pause/resume and snapshots.

### What AI-Verse already has

AI-Verse knows how to delegate work safely at the coordination/authority level, but it currently leaves terminal/computer/browser execution to external runtimes and does not define a universal sandbox execution substrate.

### What Celesto has that AI-Verse does not

1. **Hardware-isolated persistent agent computers as a reusable primitive.**
2. **Snapshot and resume of a full execution environment.**
3. **Explicit network policy at the sandbox boundary.**
4. **Live user-visible browser/computer observation and takeover interfaces.**
5. **Read-only host mounts by default.**
6. **A concrete cross-platform VM abstraction.**
7. **Execution-environment performance benchmarks.**

### Best idea to borrow

This is the strongest candidate reference for an **AI-Verse Agent Computer provider contract**.

A future architecture could look like:

```text
Multiple Bots / Gateway
        |
        | bounded execution lease
        v
Agent Computer Provider Contract
        |
        +-- local process backend
        +-- Celesto/SmolVM backend
        +-- Docker backend
        +-- SSH/VPS backend
        +-- future cloud sandbox backend
```

The computer provider owns execution environment mechanics, not AI-Verse business truth.

**Priority:** VERY HIGH.

---

## 5.8 Hermes Agent

**Repository:** https://github.com/NousResearch/hermes-agent  
**License:** MIT.

### What it does particularly well

Hermes is already a major AI-Verse benchmark source.

Current documentation includes:

- TUI;
- Telegram, Discord, Slack, WhatsApp, Signal and email via one Gateway;
- voice memo transcription;
- model/provider flexibility;
- persistent memory;
- self-improving Skills;
- Curator;
- persistent Goals;
- cron;
- subagents;
- MCP;
- local/Docker/SSH/Singularity/Modal/Daytona/Vercel Sandbox execution backends;
- serverless persistent/hibernating environments;
- batch trajectory generation and trajectory compression;
- OpenClaw migration including settings, memories, Skills, allowlists, API keys, TTS assets and AGENTS instructions.

### What AI-Verse already borrowed or exceeds

AI-Verse has already deeply benchmarked Hermes for:

- Persistent Goals;
- completion contracts;
- self-learning;
- Skill improvement;
- background review;
- durable Bot inspiration;
- runtime portability.

AI-Verse now adds stricter canonical owner and authority boundaries around many of these concepts.

### What Hermes still has that AI-Verse does not

1. **Much broader messaging/channel reachability.**
2. **One normalized set of terminal backends including serverless persistent sandboxes.**
3. **Voice memo input already integrated into messaging.**
4. **Batch trajectory generation/compression for training/research.**
5. **A complete format-aware OpenClaw migration flow covering more than semantic user context.**
6. **A highly polished “agent from anywhere” experience today.**

### Best ideas to borrow

- runtime backend adapter breadth;
- hibernate/wake execution environments;
- migration adapters built on top of AI-Verse's new semantic migration law;
- channels/voice when the Dashboard product shell is stable.

**Priority:** MEDIUM-HIGH.

---

## 5.9 Ruflo

**Repository:** https://github.com/ruvnet/ruflo  
**License:** MIT.

### What it does particularly well

Ruflo is broad and should be mined selectively rather than copied.

Notable current surfaces include:

- large agent/plugin catalog;
- swarm coordination;
- background workers;
- self-learning;
- vector/graph memory;
- local model routing;
- browser automation;
- security/audit plugins;
- cost tracking;
- GOAP planning;
- agent federation;
- MetaHarness;
- plugin marketplace.

Four ideas are especially relevant.

#### A. MetaHarness

Ruflo integrates a harness-auditing layer that can:

- score readiness;
- classify the harness “genome”;
- scan MCP surfaces;
- threat-model;
- create composite audits;
- persist snapshots;
- detect drift;
- compare systems;
- gate CI.

This maps directly to a known AI-Verse gap: there is no single command that proves the OS, components, dependencies and system path end to end.

#### B. AI Defence

Current docs describe:

- prompt-injection scanning;
- jailbreak/adversarial-content detection;
- PII detection;
- security pattern learning;
- runtime hardening checks;
- a three-gate pattern around storage/context/tool exposure.

AI-Verse's current system plan explicitly identifies prompt-injection/tool-poisoning defenses as a gap.

#### C. GOAP planning

Ruflo Goals documents:

- precondition-based action planning;
- cost optimization;
- A* planning;
- persistent horizons;
- milestone checkpoints;
- adaptive replanning;
- evidence-graded research;
- live plan/agent visualization.

AI-Verse Brain has goals, gaps, initiatives, evaluation and continuation, but no equivalent visual action-state planning product has been established.

#### D. Agent federation

Ruflo documents:

- cross-machine agent discovery;
- mTLS + Ed25519 identity;
- trust levels;
- PII stripping;
- audit trails;
- lower privilege for untrusted peers;
- optional WireGuard mesh integration.

This is powerful but not a near-term AI-Verse priority because AI-Verse is deliberately single-user first.

### What AI-Verse already has

Do not copy Ruflo's:

- generic swarm architecture;
- giant preset agent catalog;
- graph/vector memory as a second memory owner;
- duplicate cron/background-worker ownership;
- cost tracker as a second Token owner.

AI-Verse already has cleaner canonical owners for those concerns.

### Best ideas to borrow

1. MetaHarness-style **whole-system audit + drift snapshots**.
2. Runtime **prompt injection / PII / tool poisoning defenses**.
3. A derived **goal-plan graph and adaptive replanning UX**.
4. Later, zero-trust **cross-machine federation**.

**Priority:** HIGH for MetaHarness/security, MEDIUM for GOAP, LOW near-term for federation.

---

## 5.10 Telos

**Repository:** https://github.com/danielmiessler/telos  
**License:** MIT.  
**Verified:** 2026-10-02 from the public repository and its `corporate_telos.md` example.

### What it does particularly well

Telos makes the **deep context around purpose** explicit.

Its example structure captures:

- mission;
- goals;
- KPIs;
- risks/problems;
- strategies;
- projects;
- team/operational context;
- current-state/activity updates that can change how earlier goals should be interpreted.

The strongest idea is not the Markdown file itself. It is giving an AI one coherent answer to:

> What are we trying to achieve, what matters most, what is true now, and what recent change should alter our decisions?

### What AI-Verse already has

AI-Verse already has stronger separated canonical owners:

- OS for scope/current operating context;
- Brain for goals/strategy/evaluation;
- Data for current structured operational truth;
- Memory for history/provenance;
- Gateway/runtime for live session state.

Therefore AI-Verse should **not** copy Telos as one new canonical file/database that duplicates these owners.

### Best ideas to borrow

1. A first-class **Purpose Context** envelope.
2. Explicit mission -> goals -> priorities/strategies -> KPIs -> current-state orientation.
3. A compact material-change/activity projection that can change current planning.
4. A product surface that makes purpose and progress legible without exposing internal component plumbing.

### Correct AI-Verse form

The Purpose Context object should be derived/rebuildable and owner-backed.

High-impact mission/goal/priority/value changes must route to the canonical owner and require appropriate user confirmation.

**Priority:** **EARLY P1**, first eligible new cross-owner capability after the active whole-system repair/requalification program establishes a safe baseline.

Canonical adoption note:

- `docs/PURPOSE-CONTEXT-TELOS-ADOPTION-PLAN.md`

---

## 5.11 TheAlgorithm

**Repository:** https://github.com/danielmiessler/TheAlgorithm  
**Status:** experimental research project.  
**Verified:** 2026-10-02 from the public repository README and version inventory. The standalone repository exposes `versions/TheAlgorithm_Latest.md` / v6.3.0, while its README notes that the shipping version now lives in LifeOS.

### What it does particularly well

TheAlgorithm treats problem-solving as a disciplined transition from **current state -> ideal state**, with explicit verification before completion.

Its strongest current ideas include:

- a staged work loop: Observe -> Think -> Plan -> Build -> Execute -> Verify -> Learn;
- reverse-engineering vague user intent into explicit, testable definition-of-done criteria;
- Ideal State Criteria (ISC) covering functional, structural, behavioral, negative and edge conditions;
- evidence-gated completion, where a criterion should not be marked complete merely because it "should work";
- a final re-read against the user's original request;
- independent/second-opinion review at durable commitment boundaries;
- durable task/spec artifacts that survive long work and session compaction;
- deliberate attention to negative criteria and regressions, not only happy-path output.

### What AI-Verse already has

AI-Verse already contains substantial overlap:

- Brain owns Goals, desired states, completion contracts, evaluation and strategic reasoning;
- Gateway/runtime owns execution and bounded continuation;
- Multiple Bots owns delegated task coordination;
- Skills owns reusable capability packages;
- the audit/repair methodology already requires evidence, negative-space checks and exact acceptance;
- self-learning contracts already provide governed learn/evaluate/promote loops.

Therefore AI-Verse should **not** import TheAlgorithm wholesale or create a second Brain, Goal store, task database or universal PRD authority.

### Best ideas to evaluate later

1. **Definition-of-done compiler**: turn vague task intent into concise, verifiable acceptance criteria before expensive work begins.
2. **Evidence-gated completion**: important criteria close only from current tool/runtime evidence where verification is possible.
3. **Negative/edge criteria by default** for substantial tasks so regressions and failure modes are explicit.
4. **Original-request re-read gate** before declaring substantial work complete.
5. **Commitment-boundary review** for durable/high-impact outputs, using an independent reviewer/model where justified.
6. **Task learning closure** that feeds useful lessons into AI-Verse's existing Memory/Skills learning paths without creating another learning owner.
7. **Hard-to-vary specification checks** as a quality heuristic for ambiguous plans/specs, evaluated rather than adopted as universal doctrine.

### Correct AI-Verse form

The likely fit is **inside the existing Brain + Gateway task/Goal execution contract**, with verification evidence coming from the owning runtime/tools and learning routed through existing Memory/Skills owners.

Any task-spec/criteria artifact should either be Brain-owned or derived from Brain-owned Goal/task state. It must not become a parallel canonical PRD/ISA database.

### Implementation posture

This is a **future research/upgrade candidate only**.

Do not change the active public-beta repair order, release gates, Purpose Context sequencing or current runtime behavior because of this entry.

Before implementation:

1. compare TheAlgorithm against current Brain Goals, completion contracts, self-learning and audit verification;
2. identify only genuinely missing behaviors;
3. benchmark whether the added ceremony improves real task quality enough to justify its cost;
4. implement the smallest owner-correct pieces rather than copying the framework wholesale.

**Priority:** P1/P2 research candidate after the active repair/requalification program; exact implementation priority remains uncommitted until overlap/benefit benchmarking.

---

# 6. Prior inspirations already inside AI-Verse-System

This section consolidates previous System research so future work does not have to rediscover it.

## 6.1 Core agent, goal, learning and runtime references

| Reference | Canonical repo/reference | Where AI-Verse already uses it |
|---|---|---|
| **OpenAI Codex** | https://github.com/openai/codex | Persistent Goals benchmark, runtime compatibility, portable Skill conventions |
| **Hermes Agent** | https://github.com/NousResearch/hermes-agent | Goals, self-learning, Skills, Bot mode, runtime portability |
| **OpenClaw** | https://github.com/openclaw/openclaw | Goals, self-learning, scheduler separation, proactivity, isolation, Dashboard/Gateway patterns |
| **Letta** | https://github.com/letta-ai/letta | persistent agent state, mutable strategy, continual learning and Skills |
| **Prime Agent** | https://github.com/PrimeIntellect-ai/prime-agent | continual harness / goal and self-evolution benchmark research |
| **LifeOS** | https://github.com/danielmiessler/LifeOS | Brain Current State -> Ideal State; Skills judgment/authoring; Dashboard/Pulse ideas |
| **Agent Zero** | https://github.com/agent0ai/agent-zero | Brain modular project/skill/schedule architecture and runtime-independence research |
| **Magentic-One / AutoGen** | https://github.com/microsoft/autogen | Brain progress-state distinctions; multi-agent coordination research |
| **LangGraph** | https://github.com/langchain-ai/langgraph | checkpointing, workflow and durable-agent-loop comparisons |
| **CrewAI** | https://github.com/crewAIInc/crewAI | multi-agent workflow/failure research |
| **A2A** | protocol/reference standard | current Multiple Bots external runtime adapter standard |
| **OpenAI Agents SDK** | https://github.com/openai/openai-agents-python | manager delegation versus handoff semantics |
| **Microsoft Agent Framework** | https://github.com/microsoft/agent-framework | explicit orchestration topologies |
| **AgentScope, PydanticAI, Google ADK, Agno, CAMEL, MetaGPT** | https://github.com/agentscope-ai/agentscope ; https://github.com/pydantic/pydantic-ai ; https://github.com/google/adk-python ; https://github.com/agno-agi/agno ; https://github.com/camel-ai/camel ; https://github.com/FoundationAgents/MetaGPT | multi-agent message hubs, typed delegation, transfer/workflow/failure research |

### Brain research lineage also records

The current Brain component spec explicitly records research influence from:

- AIS-OS / Three Ms / Four Cs;
- ACE;
- Hermes Self-Evolution;
- GEPA;
- Voyager;
- Generative Agents;
- Reflexion;
- PersonalOS;
- Pascal Jarvis;
- DeerFlow;
- Honcho;
- LangMem;
- Anthropic long-running agent harness.

Not all of these references currently have an exact canonical repository pinned in System. That is a documentation hygiene opportunity: future research updates should add immutable source URLs/commits when practical.

---

## 6.2 Context and memory references

| Reference | Link | What AI-Verse took from it |
|---|---|---|
| **Kylon** | No canonical public repository is pinned in current System evidence | hierarchical/reversible folding concepts; first-class structured data/apps/connectivity ideas in older research |
| **Graft** | https://github.com/trailhq/Graft | compact orientation maps, source fingerprints, bounded relationships, summary-to-source escalation |
| **Kilo Code / Kilo Memory** | https://github.com/Kilo-Org/kilocode | session digests, selective consolidation/promotion, budgeted recall |
| **EverOS** | https://github.com/EverMind-AI/EverOS | new radar entry for multimodal ingest, wiki, portable memory benchmarking |

AI-Verse has already rejected generic/unbounded graph traversal and shipped only the benchmark-proven bounded one-hop path where it materially improved recall.

---

## 6.3 Dashboard and product-shell references

| Reference | Link | Existing AI-Verse use |
|---|---|---|
| **Builderz Labs Mission Control** | https://github.com/builderz-labs/mission-control | **Current canonical Dashboard shell direction** |
| **Gawkbot** | https://github.com/najmuzzaman-mohammad/gawkbot | job-first Bot/product UX reference; idea-only/code-reuse restricted by license |
| **Open WebUI** | https://github.com/open-webui/open-webui | acceptable temporary dogfood shell, not final AI-Verse UX |
| **OpenHands** | https://github.com/All-Hands-AI/OpenHands | runtime/client separation and ACP/session ideas |
| **OpenFang** | https://github.com/RightNow-AI/openfang | autonomous-worker information architecture |
| **TenacitOS** | https://github.com/carlosazaustre/tenacitOS | Mission Control visual concepts |
| **Langfuse** | https://github.com/langfuse/langfuse | trace/span/token/cost observability inspiration |
| **Phoenix** | https://github.com/Arize-ai/phoenix | observability/tracing inspiration |
| **Hermes Desktop** | Hermes ecosystem | native React UI over separate headless backend |
| **Dockview** | https://github.com/mathuo/dockview | docking/popout interaction patterns |
| **Tauri 2** | https://github.com/tauri-apps/tauri | preferred desktop wrapper direction |

The current canonical product decision is **Mission Control as shell, AI-Verse as authority**. This radar does not supersede that decision.

---

## 6.4 Connections references

The Connections component already records:

| Reference | Link | Lesson |
|---|---|---|
| **Pipedream** | https://github.com/PipedreamHQ/pipedream | broad managed authentication/integration coverage |
| **Nango** | https://github.com/NangoHQ/nango | managed OAuth/integration infrastructure |
| **Composio** | https://github.com/composiohq/composio | broad agent-tool integration infrastructure |
| **MCP/tool gateways** | protocol ecosystem | normalized external capability class |
| **Kylon** | no canonical public repo pinned | broad connectivity as a core agent-platform capability |

These remain references. Connections is still plan-only, so they are more relevant now than when the architecture was first written.

---

## 6.5 Apps references

The Apps component already records:

| Reference | Link | Lesson |
|---|---|---|
| **Kylon** | no canonical public repo pinned | durable agent-created applications inside a workspace |
| **Lovable** | https://github.com/lovable-dev/lovable | natural-language request -> working app |
| **Replit** | https://github.com/replit | integrated application generation/iteration product reference |
| **Retool** | https://github.com/tryretool | durable operational/internal tools close to data/workflows |
| **HolaOS** | https://github.com/holaboss-ai/holaOS | new high-value reference for live app + agent shared surfaces |
| **Gawkbot** | https://github.com/najmuzzaman-mohammad/gawkbot | new high-value reference for workflow -> Bot -> microapp UX |

The exact Replit/Retool product source used by the original Apps research is not pinned to one repository in current System documentation, so those organization links are reference anchors rather than immutable implementation pins.

---

## 6.6 Multiple Bots references

Current Multiple Bots research records:

- xAI Grok Bot;
- xAI Grok Multi-Agent;
- Hermes Bot Mode;
- Microsoft Agent Framework: https://github.com/microsoft/agent-framework
- A2A 1.0: protocol/reference standard
- OpenAI Agents SDK: https://github.com/openai/openai-agents-python
- OpenClaw: https://github.com/openclaw/openclaw
- AgentScope: https://github.com/agentscope-ai/agentscope
- Pydantic AI: https://github.com/pydantic/pydantic-ai
- Google ADK: https://github.com/google/adk-python
- LangGraph: https://github.com/langchain-ai/langgraph
- CrewAI: https://github.com/crewAIInc/crewAI
- Agno: https://github.com/agno-agi/agno
- CAMEL: https://github.com/camel-ai/camel
- MetaGPT: https://github.com/FoundationAgents/MetaGPT

AI-Verse has already curated these into a deliberate distinction between:

- durable Bots;
- temporary Workers;
- Tasks;
- Rooms/Threads;
- Team Runs;
- handoffs;
- leases;
- approvals;
- external runtime adapters.

**Recommendation:** do not start another swarm/orchestration subsystem merely because a new project advertises more agents or more topologies. New inspiration should only be adopted if it closes a measurable coordination gap.

---

## 6.7 Skills references

Current Skills research records:

- Hermes;
- LifeOS;
- OpenClaw;
- Agent Skills;
- Anthropic;
- OpenAI/Codex;
- PydanticAI;
- Gemini CLI;
- Copilot CLI;
- NVIDIA SkillSpector / SkillEvaluator.

The important remaining external-catalog gap is not “more Skills.” It is **stronger admission/scanning/evaluation of external Skills**, especially against supply-chain and prompt/tool abuse risk.

---

## 6.8 Token / cost-observability references

Token explicitly records primary references:

1. Tokscale
2. CodeBurn
3. ccusage
4. Pydantic genai-prices
5. Portkey Models
6. LiteLLM
7. OpenLIT
8. Langfuse
9. OpenMeter
10. Bifrost

Secondary references:

- OpenLLMetry;
- Helicone;
- Hermes Agent.

AI-Verse Token has already curated these into a stricter model of immutable evidence and **ACTUAL / CALCULATED / UNKNOWN** cost truth. Future work should not add another cost ledger merely because another product has prettier usage charts.

---

## 6.9 OS conceptual ancestry

The OS component records explicit provenance from **Nate Herk** for:

- Three Ms of AI;
- Four Cs of an AI OS.

It also records implementation dependencies for the 3D Brain visualization, including:

- 3d-force-graph;
- three.js;
- three-forcegraph;
- Preact;
- D3-related packages;
- ngraph packages;
- Marked.

These are conceptual/implementation lineage, not competing OS architectures.

---

# 7. Existing domain-level upstream inspirations

These are narrower than the OS itself but are part of the complete AI-Verse inspiration inventory.

## 7.1 Interface Designer

The current Interface Designer upstream research pins:

- Anthropic Skills: https://github.com/anthropics/skills
- UI/UX Pro Max: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
- Vercel Agent Skills: https://github.com/vercel-labs/agent-skills
- Vercel Web Interface Guidelines: https://github.com/vercel-labs/web-interface-guidelines
- shadcn/ui: https://github.com/shadcn-ui/ui
- Google `design.md`: https://github.com/google-labs-code/design.md
- Meng To Skills: https://github.com/MengTo/Skills
- Emil Kowalski Skills: https://github.com/emilkowalski/skills
- Scroll Craft: https://github.com/nateherkai/scroll-craft
- Google Stitch Skills: https://github.com/google-labs-code/stitch-skills

These are specialist craft providers. They should stay composable instead of being merged into one giant prompt.

## 7.2 Video Editor

Current Video Editor research pins:

- HyperFrames: https://github.com/heygen-com/hyperframes
- Nate baseline: https://github.com/nateherkai/hyperframes-student-kit

AI-Verse preserves Nate's deterministic/editorial logic and uses a compatibility gate rather than silently replacing it with a newer HyperFrames generation.

---

# 8. Things AI-Verse should explicitly NOT copy

The purpose of competitive research is not feature accumulation.

## Do not add another generic Memory system

EverOS, Ruflo and other projects have valuable memory ideas, but AI-Verse already has a deliberate Memory/Data/OS split and benchmarked context ladder.

Adopt missing ingestion, wiki, evaluation or retrieval ideas into the correct owners.

## Do not add another scheduler

Hermes, ZeroClaw, Gawkbot, Osaurus and Ruflo all have scheduling concepts.

AI-Verse Automations is already the canonical cadence owner.

New scheduling UX or SOP behavior must compose with Automations.

## Do not add another swarm engine

Ruflo's huge swarm surface is interesting, but AI-Verse Multiple Bots already owns coordination.

New topologies belong only if they prove better outcomes for a real missing case.

## Do not add another cost ledger

Token is canonical.

External usage systems are references for collectors, pricing, UX and telemetry, not competing authority.

## Do not add an app-local business database by convenience

HolaOS/Gawkbot style app surfaces are worth copying as UX concepts.

Their AI-Verse adaptation must keep canonical records in Data or another declared owner.

## Do not turn a sandbox into a new OS owner

Celesto/Osaurus-style computers should be execution providers.

They do not own goals, permissions, Memory, Data, Bots or workspace truth.

## Do not import 100 preset agents because a project has them

A larger agent catalog is not automatically more intelligent.

AI-Verse should prefer dynamic role/task specialization where it measurably improves work.

## Do not prioritize enterprise multi-user scope now

Federation, RBAC, SSO, SCIM and tenancy remain useful future directions.

Current owner intent explicitly prioritizes the single-user product.

---

# 9. Recommended future implementation cards

These are research cards, not accepted implementation plans.

## Card A: AI-Verse Agent Computer provider contract

**Priority:** P0/P1 research

**Inspired by:** Celesto, Osaurus, ZeroClaw, Hermes.

### Target experience

A Bot/Worker can be granted a bounded computer with:

- explicit system/workspace identity;
- read-only mounts by default;
- optional bounded writable mounts;
- network off/allowlist/full modes;
- CPU/RAM/disk/time budgets;
- browser or desktop visibility;
- snapshot/pause/resume;
- deterministic teardown;
- secret handles instead of raw secrets;
- execution receipts;
- operator takeover.

### Correct owners

- Multiple Bots: execution identity, lease/task coordination
- Gateway/runtime: live run/session orchestration
- OS: outer permission/scope floor
- Connections: external credential/capability handles
- Token: usage evidence
- external computer provider: VM/container mechanics

### Reject if

- it requires a second workspace authority;
- the sandbox stores business truth as canonical state;
- network/tool access is wider than the effective lease;
- snapshots silently preserve revoked credentials/authority.

---

## Card B: Connections v1 product path

**Priority:** P0/P1

**Inspired by:** HolaOS, Gawkbot, ZeroClaw, Hermes, Pipedream, Nango, Composio.

### Minimum valuable slice

- one high-value OAuth provider;
- one MCP provider;
- exact connection identity;
- opaque credential handle;
- live verification;
- workspace grant;
- approval-required write;
- provider-edge revocation recheck;
- idempotent execution;
- structured receipt;
- clean uninstall/re-auth;
- Dashboard projection.

### User experience

The user should be able to say:

> “Use my Gmail for this workspace.”

AI-Verse should handle the internal component routing and only ask the real authorization question.

---

## Card B2: Purpose Context / Telos projection

**Priority:** EARLY P1 / first post-repair cross-owner capability

**Inspired by:** Telos.

### Target experience

AI-Verse can answer, in a scope-correct way:

- what are we trying to achieve?
- what matters most right now?
- what are the active goals and constraints?
- how do we measure progress?
- what is the current state?
- what recently changed enough to alter the plan?

### Correct owners

- OS: identity, scope and OS-owned current context
- Brain/current direction owner: mission, goals, priorities, strategy
- Data: current structured KPI/operational truth
- Memory: historical evidence/provenance
- Gateway/runtime: bounded context assembly

### Reject if

- it creates a second editable Goal/Memory/Data/profile store;
- the projection can overrule current owner state;
- mission/priority changes happen silently;
- Dashboard becomes the hidden owner;
- the feature interrupts the active repair/requalification program.

Detailed plan: `docs/PURPOSE-CONTEXT-TELOS-ADOPTION-PLAN.md`

---

## Card B3: Verifiable task-completion loop

**Priority:** P1/P2 research candidate

**Inspired by:** TheAlgorithm.

### Evaluate

A bounded task-quality layer that can:

- turn vague intent into verifiable definition-of-done criteria;
- include negative and edge criteria for substantial work;
- track criteria against actual execution evidence;
- re-read the original request before completion;
- request independent review at durable/high-impact commitment boundaries when worthwhile;
- route post-task lessons into existing Memory/Skills learning owners.

### Correct owners

- Brain: task/Goal intent, completion contract and evaluation semantics
- Gateway/runtime: execution, live probes and evidence collection
- Multiple Bots: delegated task execution where used
- Memory/Skills: existing governed learning paths

### Reject if

- it creates a second Goal/task/PRD canonical store;
- every trivial task gains heavy ceremony;
- an LLM assertion counts as verification where deterministic evidence is available;
- it duplicates the existing audit/repair machinery;
- it changes current repair/release sequencing before benchmark evidence exists.

---

## Card C: Apps v1 shared human-agent surface

**Priority:** P1

**Inspired by:** HolaOS, Gawkbot, Mission Control.

### Target

A generated/installed App can:

- open beside Chat;
- project owner-backed Data/Memory/Connection state;
- expose scoped commands;
- let the user interact directly;
- let the agent observe only approved app-state/context changes;
- show live agent activity;
- support takeover;
- survive the conversation that created it;
- update/rollback safely;
- be deleted without deleting sibling-owned canonical truth.

### First reference App

Build one real useful app around an existing AI-Verse owner, not a toy.

---

## Card D: Runtime security receipts and untrusted-content defenses

**Priority:** P1

**Inspired by:** ZeroClaw, Ruflo, Celesto.

Evaluate:

- tool-result HMAC receipts;
- durable effect receipts where cross-session audit is required;
- prompt-injection scanning on untrusted external content;
- PII/secret detection before durable persistence or external transmission;
- MCP server identity and tool-list drift detection;
- sandbox network policy;
- environment-variable denylist for process launch;
- read-only mounts by default;
- supply-chain admission for external Skills/Apps/plugins.

This should extend current AI-Verse approval/authority laws rather than replace them.

---

## Card E: Whole-System Doctor / Harness Audit

**Priority:** P1/P2

**Inspired by:** Ruflo MetaHarness.

A single read-only command should answer:

- what exact AI-Verse release set is installed?
- what is structurally healthy?
- what is attached/enabled/initialized?
- what is runtime-ready?
- which owner dependencies are unavailable?
- which Connections are live?
- are pricing/cost truth and telemetry ready?
- is the Gateway authenticated and correctly scoped?
- are there unsupported MCP/tool surfaces?
- has the system drifted from the last known-good audit?
- are there security findings?
- what blocks “ready for daily use”?

The report must aggregate owner evidence, not invent health semantics.

---

## Card F: Channel and Voice adapters

**Priority:** P2

**Inspired by:** Hermes, ZeroClaw, HolaOS, LifeOS.

Suggested sequence:

1. Telegram
2. voice memo/transcription
3. Discord
4. Slack
5. email
6. WhatsApp/Signal where integration/security quality is acceptable

Every channel must preserve the same system/workspace/actor/approval boundaries as the Dashboard.

---

## Card G: Goal Plan projection

**Priority:** P2

**Inspired by:** Ruflo GOAP and LifeOS.

Evaluate a derived Brain view containing:

- target state;
- current gap;
- prerequisites;
- candidate action graph;
- blocked nodes;
- cost/risk estimates;
- completion criteria;
- current execution state;
- replanning events;
- verification evidence.

Do not expose private chain-of-thought. This is a structured plan/state artifact, not hidden reasoning.

---

## Card H: Knowledge Wiki + multimodal ingest

**Priority:** P2

**Inspired by:** EverOS, Gawkbot, LifeOS.

Evaluate:

- source-backed editable topic pages;
- exact citations/provenance;
- image/PDF/audio/office ingest;
- session/project/topic browsing;
- AI-assisted consolidation;
- direct descent to original source;
- rebuildable indexes.

Memory remains historical authority where appropriate. Data remains structured current truth.

---

## Card I: Foreign-system migration adapters

**Priority:** P2

**Inspired by:** Hermes OpenClaw migration.

Build on the semantic migration contract.

Potential import adapters:

- Hermes
- OpenClaw
- LifeOS
- Claude/Codex project context
- generic USER.md / MEMORY.md / SOUL.md trees

Importers may preserve useful preferences/history/Skills only after classification.

They must never import foreign:

- system-prompt authority;
- permission grants;
- tool authority;
- credentials into model-visible files;
- durable Bots/Automations without normal AI-Verse consent.

---

## Card J: Recipe / Workspace Pack ecosystem

**Priority:** P3

**Inspired by:** HolaHub, HolaOS Combos, Ruflo plugins.

A future AI-Verse Pack could declaratively request:

- Skills;
- Apps;
- Connections;
- Bot roles;
- Data schema;
- Dashboard layout;
- optional Automations.

Installation must remain a proposal until each requested permission/connection/recurring behavior is approved under its canonical owner.

---

# 10. What AI-Verse currently beats many references on

This section matters because the correct outcome of research is sometimes “keep our existing design.”

## Canonical ownership

Many agent systems colocate memory, app state, task state, credentials and operational records inside one harness.

AI-Verse's one-owner-per-responsibility model is stronger for long-lived evolution.

## Truthful lifecycle

AI-Verse distinguishes installed, supported, attached, enabled, initialized, healthy, authorized and operationally ready.

Many projects compress these into “installed.”

## Authority handoff during migration

AI-Verse explicitly says copying bytes is not a completed migration.

Canonical write authority must move safely.

## State-preserving release law

AI-Verse has explicit update/state-preservation contracts and whole-release preservation evidence requirements.

## Memory versus current truth

AI-Verse does not let old memory silently override current structured/context truth.

## Governed self-learning

Skills can learn and evolve, but promotion remains bounded by risk and immutable generation/evaluation rules.

## Bot coordination versus intelligence

Multiple Bots coordinates. Brain reasons. OS governs. Automations schedules.

These do not collapse into one “super-agent” database.

## Token cost truth

AI-Verse distinguishes actual, calculated and unknown cost instead of presenting inferred cost as fact.

## Progressive context with exact-source recovery

The context ladder treats summaries as orientation and source as evidence.

## Benchmark-driven rejection

AI-Verse has already rejected a generic relationship-graph expansion after measuring the tradeoffs and shipped only a bounded path that improved representative recall.

This “reject useful-looking complexity unless it proves value” principle should remain a competitive advantage.

---

# 11. Research watchlist

The following categories deserve periodic scouting because new projects can expose unknown unknowns quickly.

## Agent computers

Watch for:

- microVM startup improvements;
- macOS/Windows desktop automation;
- snapshot/hibernate;
- GPU isolation;
- network egress policy;
- safe host mounts;
- secret injection;
- live takeover;
- deterministic replay.

Current references: Celesto, Osaurus, ZeroClaw, Hermes.

## Agent-native applications

Watch for:

- human/agent co-use of the same UI;
- app state -> agent context sync;
- app generation from conversation;
- safe user takeover;
- durable app lifecycle;
- component/recipe marketplaces.

Current references: HolaOS, Gawkbot, Mission Control, Lovable, Replit, Retool.

## External connectivity

Watch for:

- managed OAuth;
- least-privilege capability grants;
- MCP trust/admission;
- webhook authenticity;
- event replay;
- provider idempotency;
- secret brokerage;
- connector marketplaces.

Current references: Pipedream, Nango, Composio, HolaOS, ZeroClaw, Hermes.

## Agent security

Watch for:

- prompt injection;
- tool poisoning;
- MCP server/tool drift;
- secret/PII leakage;
- sandbox escape;
- tool-result authenticity;
- supply-chain attacks against Skills/plugins/Apps;
- remote actor identity.

Current references: ZeroClaw, Ruflo, Celesto.

## Long-term agent quality

Watch for:

- longitudinal memory benchmarks;
- skill-evolution regressions;
- trajectory evaluation;
- transfer learning;
- stale-memory noise;
- user-model calibration;
- “gets better over months” evidence rather than demo quality.

Current references: EverMind research stack, Hermes, Ruflo, Letta, Prime Agent.

---

# 12. Maintenance rule

This file is now the **central inspiration index** for AI-Verse-System.

When a new external reference materially influences AI-Verse:

1. add it here;
2. state exactly what it has that AI-Verse does not;
3. state what AI-Verse already covers so we do not duplicate architecture;
4. identify the correct AI-Verse owner;
5. assign a priority;
6. include the canonical repository/reference URL;
7. mark whether the external capability is verified or only claimed;
8. record licensing constraints before copying code;
9. link any deeper benchmark/implementation plan;
10. update this document when the gap is closed so it does not remain falsely listed as missing.

The central question should always remain:

> **What does this project know, expose, or make easy that AI-Verse still does not?**

And the second question must always be:

> **Can AI-Verse gain that advantage through its existing owners without creating duplicate truth or unnecessary architecture?**
