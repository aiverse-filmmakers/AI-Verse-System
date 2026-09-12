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

Every component is researched independently and documented one repository at a time. A component is not marked complete until its source repository, architecture documents, release/status documents, important historical fixes, integration contracts, and relevant commit history have been reviewed.

Implementation facts and future intent are kept separate. A desired feature is never described as shipped merely because it belongs in the long-term architecture.

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

## Final synthesis

After every component is documented and independently QC'd, this repository will produce one supreme system blueprint describing:

- where AI-Verse started;
- what it has become;
- the architecture and product philosophy behind it;
- how every component fits together;
- the common lifecycle and interoperability contract;
- the failures and repairs that shaped the architecture;
- the missing pieces between the current system and the intended end state;
- the roadmap toward a portable, install-order-independent AI operating system that can work with AI-Verse OS, Hermes, coding agents, and other compatible hosts.

See `docs/MASTER-PLAN.md` for the research sequence and quality gates.
