# AI-Verse Brain Multi-Lens QC

**Component:** AI-Verse Brain  
**Repository source:** `aiverse-filmmakers/AI-Verse-Brain` only for the standalone baseline  
**Reviewed head:** `bef8261ad35d126d29aeff5d496f46904125b7b6`  
**QC date:** 2026-09-13  
**Overall verdict:** **PASS WITH MATERIAL RELEASE, LIFECYCLE AND CROSS-COMPONENT WRITE GAPS**

Brain's deterministic intelligence architecture is unusually mature for a beta. The main weaknesses are no longer the core cognition model. They are the gap between current-main hardening and the artifact users are told to install, lifecycle asymmetry, existing-agent adoption UX, stale integration documentation/CI, and incomplete owner-routed writeback outside Brain-owned state.

---

## 1. Product identity QC

**Verdict: PASS WITH WORDING CAUTION**

Brain genuinely implements persistent intent, initiative, planning, verification, learning and controlled strategy evolution.

The phrase "controlled self-improvement" is defensible only when understood precisely.

Current runtime self-improvement means:

- evidence-gated learning;
- strategy-rule candidates;
- E1/E2 promotion under policy;
- strategy outcome measurement;
- rollback state.

It does **not** mean:

- autonomous source-code rewrite;
- autonomous vendor-model modification;
- unrestricted prompt rewrite;
- privileged policy self-modification.

That distinction should remain visible in public product language.

---

## 2. Architecture QC

**Verdict: PASS**

The architecture is coherent.

Major responsibilities are separated into:

- intent;
- cognition;
- initiative;
- objectives/progress;
- verification;
- learning/evolution;
- policy;
- host integration.

The three-loop design avoids one giant reasoning prompt.

The deterministic core owns lifecycle/bookkeeping while the model supplies bounded proposals.

This separation is one of Brain's strongest design decisions.

---

## 3. Ownership QC

**Verdict: PASS - STRONG**

Brain explicitly owns:

- intent;
- practices;
- gaps;
- opportunities;
- initiatives;
- objectives;
- derived beliefs;
- evaluations;
- learning;
- strategies;
- Brain policy.

Brain explicitly does not own:

- OS current state;
- workspace identity;
- general Memory history;
- connections;
- capabilities;
- scheduler;
- secrets;
- external side-effect execution.

The write router reinforces this separation.

### Risk

A future convenience layer must not start persisting retrieved OS/Memory data inside Brain simply because it is useful for reasoning.

---

## 4. Source-of-truth QC

**Verdict: PASS**

Explicit user intent outranks inference.

Canonical current state stays in the host.

Historical memory stays in Memory/host.

Derived beliefs stay marked as derived.

Strategic ownership is singular in native mode.

The system has a clear rule for current truth vs historical evidence.

This is materially better than systems where one vector store gradually becomes the answer to every question.

---

## 5. Provenance QC

**Verdict: PASS - STRONG**

Brain objects can preserve:

- source refs;
- evidence refs;
- source kind/ref;
- timestamps;
- integrity;
- independence;
- OS source path/hash during direction import.

Historical OS strategy can survive as provenance without remaining active authority.

Skills evidence preserves execution provenance rather than trusting arbitrary strength labels.

---

## 6. Scope QC

**Verdict: PASS**

Current native scopes:

- operator;
- workspace:<canonical-id>.

PR #17 aligned workspace IDs with the OS schema.

Standalone core intentionally supports operator scope only rather than inventing another independent project/workspace model.

This is good scope discipline.

---

## 7. Isolation QC

**Verdict: PASS**

Evidence includes:

- exact scope grammar;
- native path contract;
- cross-scope doctor checks;
- storage containment;
- current-context scope verification;
- direction ownership by scope.

Cross-workspace leakage is treated as failure rather than warning.

---

## 8. Privacy/local-first QC

**Verdict: PASS**

Brain state is inspectable local JSON.

Credentials are not stored.

Adapter configs contain environment variable names, not secret values.

Host/retrieved content is ephemeral unless a Brain-owned derived object is deliberately created.

The model does not automatically persist everything it sees.

---

## 9. Installation QC

**Verdict: PASS ON MAIN, FAILS CURRENT RELEASE-PATH CONSISTENCY**

Current main has a sound install/init architecture.

Standalone init is dry-run-first and idempotent.

Native init auto-attaches through the local extension registry without tracked OS edits.

Incompatible hosts fail closed.

### Material problem

The README tells users to install `v0.1.0-beta.1`.

That tag predates local attachment, attach/disable/detach and direction-owner hardening.

Therefore:

> the current documented immutable install artifact does not equal the current documented product.

This fails the clean member-path release bar even though main is strong.

---

## 10. Attachment/registration QC

**Verdict: PASS ON MAIN**

Brain mutates only its local registry entry.

Shared registry writes use:

- exclusive lock;
- atomic replacement;
- expected-original comparison.

Unknown/sibling fields are preserved.

Tracked OS files are not normal attachment state.

This is the correct optional-component pattern.

---

## 11. Enable/disable lifecycle QC

**Verdict: FAIL / REQUIRES CORRECTION**

Public CLI has:

- disable.

It does not have:

- enable.

Internal Python API supports `set_brain_enabled(..., True)`.

Re-running attach preserves a previously false `enabled` value.

So a normal CLI user can disable Brain but cannot re-enable it using the documented lifecycle.

This is a real lifecycle completeness defect.

Recommended fix:

```text
ai-verse-brain enable <root>
ai-verse-brain enable <root> --apply
```

with the same dry-run/idempotent style as disable.

---

## 12. Initialization QC

**Verdict: PASS**

Current main:

- plans first;
- auto-attaches clean native OS when needed;
- validates registration;
- creates only Brain-owned/runtime state;
- writes a versioned marker;
- verifies marker after write;
- preserves installation identity on repeat.

Initialization is the sole native bootstrap exception to the normal "marker must already exist" write gate.

That exception is narrow and justified.

---

## 13. Activation/adoption QC

**Verdict: PARTIAL**

Brain has a strong **strategic activation** mechanism:

- direction handover to Brain.

But package installation and strategic ownership are deliberately separate.

This is correct.

### Missing product layer

There is no one flow that makes an already-running Claude/Codex/Hermes agent adopt Brain as its persistent control layer.

Current user must still understand:

- Brain package;
- host adapter or read-only mode;
- vendor reasoner;
- init/onboarding;
- strategic ownership;
- cadence hooks.

This is functional but not yet "works like a glove."

---

## 14. Strategic handover QC

**Verdict: PASS - STRONG**

The OS <-> Brain direction ownership transaction is one of the strongest areas.

Properties:

- install does not imply ownership;
- explicit plan;
- explicit confirmation;
- provenance-preserving import;
- crash-safe ownership flip;
- shared registry serialization;
- generated direction view;
- no outage fallback;
- explicit export/handback;
- detach blocked while Brain owns direction.

This should serve as a model for any future component activation that can change authority.

---

## 15. Migration QC

**Verdict: PARTIAL**

Current migration planner is honest and safe.

It:

- detects schema mismatch;
- refuses downgrade/newer state;
- refuses unknown older conversion;
- can refresh package metadata.

### Missing

No state-schema conversion is registered.

No generic old-agent strategic import format exists beyond native OS direction handover.

General historical memory migration should remain Memory-owned.

### Recommendation

Brain migration should focus on strategic/control state:

- explicit goals;
- desired states;
- boundaries;
- practices;
- strategy/evaluation state where meaningful.

---

## 16. Update/upgrade QC

**Verdict: PARTIAL**

There is no Brain-specific update command.

Package update is delegated to pip/pipx/Git version selection.

That can be acceptable.

But a mature UX should still specify:

- release channel;
- version compatibility;
- state migration;
- rollback guidance;
- post-update doctor.

Current main/version/tag mismatch makes this more urgent.

---

## 17. Detach/uninstall/reinstall QC

**Verdict: PASS WITH ENABLE GAP**

Detach:

- removes registration;
- preserves canonical Brain state;
- requires strategic handback first.

Reattach + init can rediscover preserved state.

### Problem

Disabled state is harder to recover than detached state because CLI has no enable.

### Package uninstall

Package uninstall is external package-manager responsibility.

Brain should document the correct order:

1. handback if needed;
2. detach;
3. uninstall package;
4. preserve/remove canonical Brain data only by explicit user choice.

---

## 18. Install-order independence QC

**Verdict: PASS ARCHITECTURALLY, PARTIAL IN PRODUCT UX**

Brain supports:

- standalone installation;
- OS-first then Brain;
- Brain package existing before attachment;
- late native attachment.

Native incompatible host never falls back to parallel standalone state.

This is correct.

### Missing

A higher-level host/agent reconciliation path is still needed to turn late installation into automatic adoption.

---

## 19. Discovery QC

**Verdict: PASS FOR BRAIN'S OWN HOST DETECTION**

Brain can detect:

- standalone root;
- compatible OS v2;
- incompatible AI-Verse.

Native attachment state is explicit.

Host adapter selection is explicit rather than guessed.

No major discovery defect found.

---

## 20. Readiness-state QC

**Verdict: PASS**

Brain distinguishes:

- package installed;
- native attached;
- attached enabled;
- initialized;
- onboarded enough to orient;
- strategic owner;
- vendor reachable;
- host reachable;
- action authorized.

These states are not collapsed.

This is a strong model.

### Missing lifecycle state surface

Because enable is not exposed in CLI, the lifecycle state model is stronger than the user-facing lifecycle implementation.

---

## 21. Doctor/health QC

**Verdict: PASS WITH HEALTH-DEPTH LIMIT**

Brain doctor checks Brain structural/native readiness.

Vendor and adapter doctors check separate dependencies.

This is appropriate.

### Gap

There is no one composite command that says:

- Brain state good;
- vendor good;
- host adapter good;
- scheduler hooks installed;
- Memory/capabilities live;
- representative tick successful.

This is a system-level unified health opportunity, not necessarily something Brain must own alone.

---

## 22. Permissions QC

**Verdict: PASS - EXCELLENT**

Brain permission architecture is one of the strongest reviewed areas.

- durable policy;
- operator/workspace tightening only;
- caller overrides tightening only;
- exact action classes;
- conservative defaults;
- exact approval binding;
- independent host permission;
- restrictive intersection;
- permission recheck at dispatch edge.

This is implementation-enforced, not prose-only.

---

## 23. Security/path QC

**Verdict: PASS**

Security patterns include:

- scope/path validation;
- no incompatible-host fallback;
- bounded subprocesses;
- no shell execution;
- bounded adapter I/O;
- exact protocol/request IDs;
- safe extension registry;
- path-safe object IDs;
- no credentials in configs/state;
- frozen strategy resolver delegation.

No architectural reason was found to weaken these controls for UX convenience.

---

## 24. Idempotency/replay QC

**Verdict: PASS - STRONG**

Brain uses idempotency for:

- action requests;
- trigger claims;
- direction handover recovery;
- onboarding dedupe;
- initialization;
- external effects.

Uncertain side effects block automatic replay.

This is an important difference between safe long-running autonomy and "just retry."

---

## 25. Concurrency/locking QC

**Verdict: PASS AFTER HISTORICAL REPAIR**

Object-level locking plus revisions protects canonical objects.

Runtime semantic locks protect opportunity promotion.

Registry-wide direction locking repaired the multi-scope race.

Extension registry mutation is serialized.

The repair history is strong evidence that concurrency is treated as architecture, not an afterthought.

---

## 26. Failure semantics QC

**Verdict: PASS - STRONG**

Brain repeatedly fails closed:

- incompatible AI-Verse host;
- missing real host operations;
- invalid bridge;
- malformed policy;
- weaker policy override;
- stale approval;
- stale Skills generation;
- unsupported migration;
- uncertain external side effect;
- wrong current-context scope;
- capability overflow.

A major strength is that fallback paths are explicit rather than silent.

---

## 27. Capability taxonomy QC

**Verdict: PASS**

Brain does not implement capabilities itself.

It reads/ranks capability metadata and can bind execution identity/receipts.

This preserves Skills/OS capability ownership.

Brain's learned strategies are not misrepresented as executable Skills.

---

## 28. Runtime/agent portability QC

**Verdict: PASS WITH ADOPTION UX GAP**

The bridge is genuinely portable.

Claude/Codex/Hermes wrappers stay small and reasoner-only.

The deterministic Brain core is vendor neutral.

This is exactly the correct architecture for portability.

### Gap

Runtime portability at the protocol level is ahead of productized runtime adoption.

"Can integrate" is true.

"Install once and the existing agent automatically uses Brain" is not yet true.

---

## 29. Integration-boundary QC

**Verdict: PASS**

Strong boundaries:

- OS current context through host/resolver;
- Memory history through host;
- Skills through metadata/receipt contract;
- Data through optional host query;
- actions through host permission + request boundary.

Brain does not directly open sibling databases.

This is clean component design.

---

## 30. Cross-component write QC

**Verdict: PARTIAL / MATERIAL GAP**

Brain knows where different durable facts belong.

It has symbolic write routing.

The bridge defines a `write_route` host operation.

But the reviewed automatic cognition/learning path does not complete a generic cross-component owner-routed write transaction.

This means:

- learning can remain Brain-owned;
- external OS/Memory/Knowledge promotion requires additional orchestration.

This aligns with the OS audit's missing canonical handlers.

### System implication

The two repos are converging on the same missing layer:

```text
Brain classifies owner
→ host/OS accepts bounded write candidate
→ canonical owner validates
→ owner rechecks permissions/authority/idempotency
→ canonical effect
→ receipt
```

That should become a shared system contract.

---

## 31. Read-path QC

**Verdict: PASS - STRONG**

Brain does not treat provider order as relevance.

History query is semantic.

Capability ranking precedes context limit.

Native context respects OS ownership.

Host data remains ephemeral.

No significant read-boundary defect found.

---

## 32. Schema/data-model QC

**Verdict: PASS**

The object model is explicit and typed.

Lifecycle transitions are deterministic.

Common envelope carries revisions/provenance.

Migration is fail-closed.

### Future issue

Once state schema changes from 1.0, real conversion registration must exist before release.

The current migration code is prepared structurally, but no historical schema path is implemented because there is not yet one to migrate from.

---

## 33. Performance/scalability QC

**Verdict: PASS FOR BETA WITH KNOWN FILE-STORE LIMITS**

The file-per-object design is transparent and simple.

Brain bounds:

- context;
- capability candidates;
- attention;
- active initiatives;
- parallel objectives;
- background ticks;
- evaluations.

### Future scaling concern

Object listing currently scans JSON files in kind directories.

This is appropriate for the current local-first beta scale but may eventually need derived indexes for very large Brain state.

Any index must remain rebuildable and non-canonical.

No immediate correctness blocker.

---

## 34. Product/UX QC

**Verdict: PARTIAL**

Strong UX:

- dry-run-first mutation;
- human-readable CLI;
- explicit apply;
- plan-integration;
- doctor;
- vendor-doctor;
- handover plans.

Weak UX:

- no enable;
- package/tag mismatch;
- no one-step adoption;
- host/cadence configuration still technical;
- multiple commands needed to reach "Brain is part of my agent."

This is the main area where Brain feels like a high-quality developer system more than a seamless member product.

---

## 35. Cadence QC

**Verdict: PASS FOR BRAIN OWNERSHIP**

Brain correctly refuses scheduler ownership.

It generates cadence policy and argv hooks.

This is not a missing Brain feature.

### System dependency

Someone else must actually install/run the cadence.

The OS audit independently found no universal OS scheduler.

Therefore the overall ecosystem still has a cadence-execution ownership decision to make.

---

## 36. Agent/orchestration QC

**Verdict: PASS**

Brain is itself the intelligence/control layer.

It does not duplicate a generic multi-agent fleet.

Vendor models are reasoners behind Brain, not autonomous authority sources.

This should remain distinct from Multiple Bots.

---

## 37. App/UI QC

**Verdict: NOT APPLICABLE AS A BRAIN-OWNED UI**

Brain does not ship a main UI/dashboard.

Its output is structured state/CLI/tick summaries.

A future Dashboard may visualize Brain, but must remain a projection or write through Brain-owned APIs.

---

## 38. Release/distribution QC

**Verdict: FAILS CURRENT IMMUTABLE-ARTIFACT BAR**

This is Brain's most material current release issue.

The current README recommends beta.1 tag.

The tag lacks major current hardening.

Main still reports beta.1.

That means version identity no longer uniquely describes product behavior.

### Required correction

Cut a new beta/RC version from current hardened main after:

- enable lifecycle fix;
- stale docs/CI correction;
- full current acceptance.

Then update install command to that immutable version.

---

## 39. Cross-platform QC

**Verdict: PASS**

Core CI covers:

- Linux;
- macOS;
- Windows;
- Python 3.9;
- Python 3.12.

Package smoke is Linux 3.12.

Vendor CLI functionality remains a moving external dependency and must be rechecked at release.

---

## 40. Documentation consistency QC

**Verdict: FAILS CLEANLINESS BAR**

Material drift:

1. beta tag vs current README features;
2. stale installation protocol;
3. stale research README status;
4. OS direction CI still patches tracked manifest;
5. historical docs not always clearly marked historical.

Because agents will read these docs to operate Brain, this is not cosmetic.

---

## 41. Historical-learning QC

**Verdict: PASS - EXCELLENT**

Brain has a dense repair history that repeatedly strengthened general laws:

- persisted policy repair -> durable policy must govern runtime;
- approval binding -> approval authorizes exact effect;
- write readiness -> files present != authorized write;
- direction ownership -> install != authority;
- explicit host -> no silent degraded fallback;
- meaningful retrieval -> relevance before truncation;
- permission intersection -> safety boundaries compose restrictively;
- Skills receipts -> execution != verification;
- frozen strategy read -> ownership applies to reads;
- registry race -> shared registries need shared locking;
- local lifecycle -> optional components do not mutate tracked host files.

This repair-to-law behavior should continue.

---

## 42. Inspiration/curation QC

**Verdict: PASS - EXCEPTIONALLY WELL DOCUMENTED**

Brain's research lineage is explicit and nuanced.

The repository does not merely list competitors. It records:

- why each system mattered;
- strong ideas;
- what Brain should learn;
- what not to copy.

This directly implements the user's "curate the best systems into a stronger one" philosophy.

Among the 10 components, Brain currently has one of the strongest documented inspiration chains.

---

## 43. Negative-space QC

**Verdict: MATERIAL FINDINGS**

Expected from product/research claims but not fully present:

### Expected: symmetric native lifecycle
Missing: public enable.

### Expected: current beta artifact contains beta behavior
Missing: current hardening is post-tag.

### Expected: migration command means migration paths exist
Current reality: package metadata refresh only; older state conversion fails closed.

### Expected: OS/Memory write routing from Phase 3
Current reality: classification/host contract exists, general dispatcher not wired.

### Expected: "works with Hermes/Codex/Claude"
Current reality: yes as reasoners through Brain CLI, but not persistent plug-in adoption into their normal agent lifecycle.

### Expected: proactive background Brain
Current reality: cadence requests/hooks exist; scheduler is deliberately external.

These are exactly the distinctions the final system blueprint must preserve.

---

## 44. Architecture-vs-operation QC

| Subsystem | Classification |
|---|---|
| object model | implementation + tests |
| lifecycle state machines | implementation + tests |
| intent onboarding | implementation + tests |
| gap/opportunity/initiative | implementation + tests |
| objective progress/stall | implementation + tests |
| verification | implementation + tests |
| policy | implementation + tests |
| attention | implementation + tests |
| learning/strategy | implementation + tests |
| core source-code self-modification | prohibited / not implemented |
| cadence policy | implementation |
| scheduler | external/not Brain-owned |
| bridge | implementation + tests |
| vendor wrappers | implementation, external CLI dependency |
| host selection | implementation + tests |
| native attach/init | implementation + tests on main |
| native enable | API only, CLI missing |
| direction handover/handback | implementation + acceptance |
| cross-component read | implementation via host |
| cross-component generic write | contract/classification, incomplete dispatch |
| migration framework | implementation |
| actual old schema conversion | absent |
| package beta artifact | exists but stale vs main |
| agent adoption | manual/composed, not seamless |

---

## 45. Current-target readiness QC

**Verdict: FUNCTIONALLY STRONG, CURRENT RELEASE PRODUCT NOT YET COMPLETE**

For the actual core intelligence milestone, Brain is highly complete.

For the public-beta/member milestone described by current docs, it is not yet fully complete because the recommended install artifact does not contain the current integration generation.

### Current-target blockers

1. new hardened version/tag;
2. enable CLI;
3. current member-path cross-repo CI;
4. stale docs corrected;
5. lifecycle/adoption instructions made coherent.

The cross-component write/adoption/migration improvements may continue beyond the immediate beta, but they are required for the stronger system-wide seamless target.

---

## 46. Scope-creep QC

**Verdict: PASS**

The repository has repeatedly resisted becoming:

- an OS;
- Memory;
- scheduler;
- capability host;
- connection system;
- tool executor;
- generic UI.

That restraint should continue.

The correct next work is not "put everything inside Brain."

It is to improve contracts and orchestration with owners.

---

## 47. "Works like a glove" acceptance scenario

The mature Brain should pass:

1. Agent already exists.
2. User installs Brain package.
3. System detects standalone/native host.
4. Brain attaches if appropriate.
5. Existing strategic state is discovered.
6. User is shown what strategic ownership would change.
7. User confirms import/handover if desired.
8. Brain initializes.
9. Existing goals/practices are imported with provenance where appropriate.
10. Runtime host adapter is selected/configured.
11. Vendor reasoner is verified.
12. Cadence hooks are offered to the actual scheduler owner.
13. Brain doctor passes.
14. First bounded orientation succeeds.
15. Existing agent now uses Brain as its durable intelligence layer.
16. Brain can be disabled.
17. Brain can be re-enabled.
18. Strategic ownership can be handed back.
19. Brain can be detached without data loss.
20. Reinstall can reattach preserved state.
21. No OS/Memory/capability ownership is duplicated.
22. User never needs to manually patch tracked files.

**CURRENT:** most low-level pieces exist on main, but the entire scenario is not yet one supported productized flow.

---

## 48. Exact corrective work recommended before new Brain feature expansion

Priority order:

### P1. Fix release identity

Cut a new version from current hardened architecture.

### P2. Add enable CLI

Restore lifecycle symmetry.

### P3. Fix current cross-repo CI

Remove legacy tracked manifest patch.

### P4. Correct stale docs

Especially installation protocol and research status.

### P5. Verify full current release matrix

Use the exact new immutable artifact/member path.

### P6. Productize activation/adoption

Build the setup sequence around existing primitives rather than adding new core cognition features.

### P7. Complete shared canonical write routing with the system owner

Do not implement direct OS/Memory writes inside Brain.

---

## 49. Final documentation verdict

**PASS WITH MATERIAL RELEASE, LIFECYCLE AND CROSS-COMPONENT WRITE GAPS**

Brain's architecture is not the problem.

The deterministic engine is sophisticated, safety-conscious and well tested.

The largest risk is documentation/release generation drift: current main is ahead of the immutable artifact users are told to install.

The best next Brain work is release/lifecycle convergence, not another intelligence-model redesign.

---

## 50. Readiness for supreme-system synthesis

**READY AS COMPONENT 2 BASELINE AFTER THIS QC**

Brain can now be treated as a documented system component.

Later audits of Memory, Skills, Data, Multiple Bots and other components may refine the cross-component contracts, especially:

- owner-routed writes;
- existing-agent migration;
- cadence runtime ownership;
- component activation/adoption;
- unified system health.

Any such refinement must update this living Brain spec.
