# AI-Verse System

This repository is the canonical big-picture specification for the AI-Verse operating-system family.

It does **not** duplicate implementation code from the component repositories. Instead, it records:

- what each component is and why it exists;
- what each component owns and must never own;
- how the components compose without creating competing sources of truth;
- the design rules that apply across the ecosystem;
- what is implemented today versus what is intended next;
- installation, attachment, activation, migration, disable, detach, reinstall, and upgrade expectations;
- important architectural repairs and the lessons they established;
- inspirations and reference systems used when they are evidenced in the component repositories or research history;
- unresolved gaps and future-state requirements;
- the long-term vision for the complete AI-Verse system.

## Documentation rule

Every component is researched independently and documented one repository at a time. A component is not marked complete until its source repository, architecture documents, release/status documents, important historical fixes, integration contracts, relevant commit history, implementation enforcement, lifecycle surfaces, tests/CI, contradictions, negative-space findings, documentation drift, and current-target readiness have been reviewed.

The canonical review procedure is `docs/AUDIT-METHODOLOGY.md`. It defines the evidence hierarchy, fresh standalone-repository rule, 46 mandatory audit lenses, lifecycle/completeness matrices, contradiction scan, historical repair analysis, write/read-path tracing, health-depth classification, and the completion checklist used for every component.

Implementation facts and future intent are kept separate. A desired feature is never described as shipped merely because it belongs in the long-term architecture.

## Living specification rule

AI-Verse-System is continuously maintained.

Whenever a meaningful new idea, planned feature, integration, lifecycle change, migration requirement, repair, architectural decision, readiness finding or release-state change affects AI-Verse, this repository should be updated as part of the same body of work.

Use:

- `docs/OWNER-PRODUCT-INTENT.md` as the canonical living record of the owner's product direction, UX/autonomy preferences, "grandma/Jarvis" experience, automatic-vs-ask boundaries, and known intent-versus-implementation gaps;
- `docs/IDEA-INBOX.md` to capture ideas before their final architectural home is clear;
- `docs/LIVING-SPEC-PROTOCOL.md` for update/propagation rules;
- `docs/SYSTEM-CHANGELOG.md` for the chronological record of meaningful changes;
- the relevant component spec/QC/source map once the change has a clear owner.

A future agent should be able to reconstruct the current system intent from this repository without needing the original chat where the idea appeared.

For product/UX/autonomy decisions, read `docs/OWNER-PRODUCT-INTENT.md` before changing behavior. It records the owner's recurring direction separately from implementation evidence, so a desired behavior is not mistaken for something already shipped.

## Planned component set

The initial system inventory is:

1. AI-Verse OS
2. AI-Verse Brain
3. AI-Verse Memory
4. AI-Verse Skills
5. AI-Verse Data
6. AI-Verse Multiple Bots
7. AI-Verse Connections
8. AI-Verse Apps
9. AI-Verse Dashboard
10. AI-Verse Token

Additional repositories are added only if the audit shows they are genuine OS-family components rather than distribution, community, demo, or deployment repositories.

## Final system blueprint

All ten initial AI-Verse component repositories have now been independently audited and synthesized into the canonical cross-component blueprint:

- `docs/FINAL-AI-VERSE-BLUEPRINT.md`

The blueprint defines:

- the complete system topology and product philosophy;
- canonical ownership and source-of-truth boundaries;
- the common lifecycle, adoption and migration model;
- cross-component read/write and authority laws;
- current readiness of all ten components;
- release horizons and exact system-level blockers;
- the implementation order from the current state to the complete "works like a glove" system;
- the system-wide definition of done.

The detailed component specs remain authoritative for component-local evidence. The Final AI-Verse Blueprint is the canonical system-level synthesis.

For the practical answer to what can be used now, what interface to use, progressive onboarding, security/MCP/runtime-loop coverage and the staged product gates, see `docs/DOGFOOD-UX-AND-PLATFORM-COMPLETENESS.md`.

See `docs/MASTER-PLAN.md` for the audit methodology and synthesis process.

This repository remains canonical after the blueprint baseline. The blueprint and component specs must evolve whenever the system evolves.
