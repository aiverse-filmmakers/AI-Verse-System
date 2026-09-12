# Canonical AI-Verse Component Research Prompt

Use this prompt separately for each AI-Verse component repository.

---

You are documenting one component of the AI-Verse system family for the canonical `AI-Verse-System` architecture repository.

Your job is **not** to summarize files or reproduce code. Your job is to reverse-engineer the component's product philosophy, architectural role, ownership laws, current implementation, historical evolution, important fixes, interoperability contracts and intended end state.

Treat the repository itself as evidence, not as automatically perfect truth. README files, runtime behavior, tests, CI, status documents, repair handoffs and commit history may disagree. Resolve those disagreements explicitly.

## Primary objective

Produce a document that explains:

1. **What this component is today.**
2. **Why it exists.**
3. **What responsibility it canonically owns.**
4. **What it must never own or duplicate.**
5. **How it works inside AI-Verse OS.**
6. **How portable it should be outside AI-Verse OS, including compatible agents/hosts such as Hermes, Codex, Claude Code and other systems.**
7. **How it installs, attaches, activates, disables, detaches, upgrades and uninstalls today.**
8. **How those lifecycle operations should work in the intended end state.**
9. **How it behaves when installed before or after the OS or sibling components.**
10. **How an already-running agent can discover/adopt it later without reinstalling everything.**
11. **How legacy or pre-existing state should migrate into it.**
12. **Which external systems/projects/frameworks inspired it, when evidence exists.**
13. **Which ideas were adopted, changed or rejected from those inspirations.**
14. **Which important bugs/audits/fixes shaped the current architecture.**
15. **What permanent system law each important repair teaches.**
16. **What remains unfinished or contradictory.**
17. **What the component is intended to become.**
18. **How it contributes to the larger AI-Verse vision.**
19. **What this component is supposed to achieve at the current project stage, not only in the distant future.**
20. **Whether it currently achieves that present-stage target completely, partially, or not yet.**
21. **Exactly what is still missing before it can be called complete for the current intended milestone.**
22. **Whether the missing work is architecture, implementation, lifecycle wiring, commands/UX, migration, tests/acceptance, distribution/release, documentation, or external verification.**
23. **Whether a real implementation/activation command exists for the component, and whether that command actually makes an already-running host/agent adopt the component correctly.**

## System-wide product philosophy

Preserve these intentions unless direct evidence shows a deliberate change:

- AI-Verse uses a curating approach: study strong systems in each category, extract the best compatible ideas, learn from their weaknesses, then build a cleaner and more integrated version.
- Components should be excellent standalone modules where their responsibility permits.
- They should integrate especially deeply with AI-Verse OS.
- Components should avoid hidden assumptions about install order.
- Package availability and attachment to a particular OS root are separate concepts.
- Installation should not silently modify sibling-owned canonical state.
- A component installed later must be discoverable and adoptable by an existing host/agent.
- The long-term UX should include explicit setup/activation/reconciliation sequences so an agent can be told to use the new component as its canonical infrastructure for that responsibility.
- Stateful components need deliberate migration/import paths for older agents and existing state.
- User-owned canonical state should survive disable, detach, reinstall and normal uninstall.
- Derived indexes, caches, projections and dashboards must not become hidden sources of truth.
- Missing optional components should degrade gracefully.
- Registration, installation, enablement, health, initialization and authorization are different states.
- Cross-component integrations must preserve ownership instead of duplicating data to make integration look easier.

## Evidence collection

Before writing:

1. Inspect the full repository tree.
2. Read the top-level README, manifests and runtime contracts.
3. Read architecture, PRD, build-map, status, integration, release and migration documents.
4. Inspect installers, CLI commands, lifecycle code and doctor/status behavior.
5. Inspect relevant tests and CI.
6. Inspect important commit history.
7. Search commit/docs history for terms such as:
   - audit
   - repair
   - fix
   - migration
   - legacy
   - install
   - lifecycle
   - attach
   - detach
   - reconcile
   - ownership
   - authority
   - compatibility
   - isolation
   - security
   - release
8. Search for inspiration/reference/research documents and external project names.
9. Identify known incidents where a previous architecture failed.
10. Identify current contradictions and incomplete lifecycle behavior.

## Current target readiness audit

Do not compare the repository only against a hypothetical far-future vision.

For every component, identify the **current intended milestone** from its build map, PRD, release plan, status documents, recent fixes and the wider AI-Verse integration goal.

Then produce a hard readiness verdict:

- **READY FOR CURRENT TARGET** - everything required for the present intended milestone is implemented, wired, tested and usable through supported commands.
- **FUNCTIONALLY READY, IMPLEMENTATION UX MISSING** - the core engine works, but install/attach/activate/migrate/reconcile commands or host adoption are incomplete.
- **PARTIALLY READY** - meaningful functionality exists, but one or more required runtime/integration/lifecycle behaviors are missing.
- **NOT READY FOR CURRENT TARGET** - the component cannot yet perform the role it is presently supposed to perform.
- **BLOCKED BY EXTERNAL VERIFICATION** - implementation is complete enough, but release proof is blocked by CI, distribution, access, credentials, platform testing or another external gate.

The audit must explicitly answer:

1. What is this component supposed to do **right now**, based on the current project/release phase?
2. Which parts are already 100% implemented?
3. Which parts only exist as architecture/docs/contracts but are not implemented?
4. Which parts work internally but are not wired into the real OS/host/member path?
5. Which parts work only in tests or special integration fixtures?
6. Which parts lack a public/member command?
7. Does a simple implementation command exist?
8. Does an attach command exist?
9. Does an activation/adoption command exist?
10. Can an agent that existed before installation adopt the component without reinstalling the system?
11. Is migration/import for old state implemented or only planned?
12. Does doctor/status prove health after activation?
13. Can disable/detach/uninstall/reinstall preserve canonical state?
14. Has the exact real user path been acceptance-tested?
15. What exact missing tasks separate today's state from "works perfectly together like a glove"?

### Command matrix

For every component, record a command/status matrix:

| Capability | Required now? | Current command | Works end-to-end? | Missing |
|---|---|---|---|---|
| Install/package availability | | | | |
| Attach/register | | | | |
| Activate/adopt | | | | |
| Initialize scope | | | | |
| Migrate/import legacy state | | | | |
| Doctor/status | | | | |
| Update | | | | |
| Disable | | | | |
| Detach/uninstall | | | | |
| Reinstall/reconcile preserved state | | | | |

If a row has no command, say so explicitly.

A component must not be called "100% complete" for the current target merely because the engine code is complete. If the intended current product requires installation, attachment, activation, migration or host adoption and those paths are missing, that is unfinished implementation.

## Required distinction

Every major claim must conceptually fall into one of these categories:

- **CURRENT:** implemented/supported now.
- **LAW:** architectural invariant that should remain true.
- **INTENDED:** desired future behavior.
- **GAP:** missing behavior between current and intended.
- **HISTORICAL:** old behavior retained only for migration/provenance.
- **INSPIRATION:** external/reference idea that materially influenced the design.

Never describe INTENDED behavior as CURRENT.

## Required output structure

Write `COMPONENT-SPEC.md` with:

1. Executive identity
2. Role in the whole system
3. Problem it solves
4. Current architecture
5. Canonical ownership
6. Explicit non-ownership
7. Sources of truth
8. Runtime model
9. Scope and isolation model
10. Installation today
11. Attachment/registration today
12. Activation/adoption today
13. Upgrade behavior
14. Disable/detach/uninstall behavior
15. Legacy/history migration today
16. Intended lifecycle end state
17. Install-order independence target
18. Agent/runtime portability
19. Integration with every relevant sibling component
20. Permission/security boundaries
21. Failure/degradation behavior
22. Important historical repairs
23. Permanent laws learned from those repairs
24. Inspirations/references
25. What was adopted/rejected from inspirations
26. Current known gaps
27. Desired future state
28. Definition of done
29. Big-picture contribution to AI-Verse
30. Open questions/decisions still required
31. Current target readiness verdict
32. Present-stage missing implementation
33. Command/lifecycle implementation matrix
34. Exact blockers to "works perfectly together like a glove"

Write `SOURCE-MAP.md` containing the evidence used.

Write `QC.md` containing independent architecture, lifecycle, migration, integration, security, portability, UX, historical-learning and future-state reviews.

## Final quality bar

The reader should be able to understand the component without reading its source code and should also understand:

- what is real today;
- what is only intended;
- why the architecture has its current shape;
- which past failures it is designed never to repeat;
- how the component should behave in a mature AI-Verse installation;
- how it can participate in other compatible agent systems;
- what must still be built before calling the component complete;
- whether it is actually complete for the current intended milestone;
- whether the remaining gap is engine capability or simply missing implementation/wiring/commands;
- which exact command or lifecycle path still needs to exist before the component works seamlessly with the rest of AI-Verse.

Do not move to another repository until this component passes all QC perspectives.
