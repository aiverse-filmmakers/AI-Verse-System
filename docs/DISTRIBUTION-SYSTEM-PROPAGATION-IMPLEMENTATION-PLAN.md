# Distribution -> System Propagation, Canonical Owner Routing and Member Isolation Implementation Plan

**Status:** ACTIVE  
**Canonical planning repo:** `aiverse-filmmakers/AI-Verse-System`  
**Primary implementation repo:** `aiverse-filmmakers/ai-verse-distribution`  
**Started:** 2026-10-12  
**Program size:** 14 slices  
**Completed:** 1  
**Remaining:** 13  
**Progress:** 7.1%  
**Rule:** Update this file before and after every implementation slice. A slice is COMPLETE only when its acceptance criteria are satisfied and exact implementation/test evidence is recorded here.

## 0. Mission

Make meaningful evolution in `aiverse-filmmakers/ai-verse-distribution` reliably propagate into the canonical `aiverse-filmmakers/AI-Verse-System` record, preserve the canonical implementation ownership of every AI-Verse component repository, and keep all maintainer/development governance completely outside the member-facing AI-Verse installation.

The finished behavior must achieve all three goals at once:

1. **System stays current.** Meaningful Distribution features, improvements, fixes, lifecycle changes, release changes, preservation changes, compatibility changes, member-experience changes and architectural changes are evaluated and reflected appropriately in AI-Verse-System.
2. **Canonical component owners stay current.** If Distribution work discovers or requires a change canonically owned by Skills, Brain, Memory, Data, OS, Gateway, Automations, Multiple Bots, Connections, Apps, Dashboard, Token or another sibling component, the actual fix/improvement must land in that owning repository. Distribution must not become a substitute implementation layer for the component.
3. **Members receive only product-relevant files.** Maintainer rules, internal propagation instructions, roadmaps, qualification records, developer-only governance and System synchronization machinery are not copied, generated or exposed as part of the member project/runtime installation.

This program is not a request to mirror every Distribution commit into System or to make Distribution edit sibling implementation files directly. It is a requirement that meaningful product truth cannot evolve in Distribution while System or the canonical component owner silently becomes stale.

---

## 0A. Non-negotiable separation rule

There are three different surfaces and they must not be confused.

### A. Canonical maintainer/source repositories

These may contain development governance, architecture plans, release qualification, tests, internal agent instructions and propagation rules.

Examples:

- `aiverse-filmmakers/AI-Verse-System`
- `aiverse-filmmakers/ai-verse-distribution`
- canonical sibling implementation repositories such as `AI-Verse-Skills`, `AI-Verse-Brain`, `AI-Verse-Memory`, `AI-Verse-Data` and `AI-Verse-OS`

### B. Distribution packaging/runtime machinery

This is the code that resolves releases, installs AI-Verse, updates it, validates health, preserves user state and performs release/lifecycle work.

It may internally know about maintainer-only rules when operating as source/development infrastructure, but those rules must not become member project instructions.

### C. Member AI-Verse installation

This is the user's actual OS/project/runtime surface.

It may contain member-facing/generated files such as:

- `AGENTS.md`
- `CLAUDE.md`
- `AI-VERSE.yaml`
- capability adapters
- runtime configuration
- component/runtime files required by the installed release

It must not receive maintainer-only governance merely because those files exist in the source repository.

**A member installation must never inherit source-repository governance by broad repository copying.**

Where practical, the installation boundary should be expressed as an explicit allowlist or deterministic generated payload rather than a blacklist of files to remove afterward.

---

## 0B. Canonical System propagation rule to implement

The implementation produced by this program must establish the following policy:

> Any meaningful change to `aiverse-filmmakers/ai-verse-distribution`, including new features, improvements, fixes, lifecycle behavior, installation, updates, rollback, compatibility, preservation, release behavior, member experience, or architectural changes, must be evaluated and reflected appropriately in `aiverse-filmmakers/AI-Verse-System`.
>
> Update whichever System records are relevant to the change, such as the canonical specification, blueprint, component documentation, QC/readiness, source maps, implementation plans, or `docs/SYSTEM-CHANGELOG.md`. Not every change requires every System document to change, but meaningful Distribution progress must not leave AI-Verse-System describing an outdated version of the product.
>
> Purely internal changes with no meaningful effect on capability, behavior, architecture, safety, lifecycle, release state, compatibility, preservation, readiness, or product truth may be recorded as having no System impact.
>
> These are maintainer/development rules only and must never be included in member installations or generated member project instructions.

This rule is semantic, not commit-count based.

---

## 0C. Meaningful-change decision model

A Distribution change is presumed to require System evaluation when it changes or materially improves any of the following:

- install behavior;
- update behavior;
- rollback behavior;
- repair/reconcile behavior;
- release selection or admission;
- compatibility resolution;
- preservation/user-state safety;
- lifecycle ownership;
- health/readiness/doctor semantics;
- member-facing behavior or generated project behavior;
- component composition;
- source-of-truth boundaries;
- security/trust assumptions;
- packaging/distribution topology;
- supported environments;
- failure semantics;
- migration behavior;
- release state/readiness;
- a previously missing capability becoming implemented;
- a meaningful defect being repaired;
- a meaningful improvement that makes System documentation materially incomplete or misleading if omitted.

A change may be classified `NO SYSTEM IMPACT` only when it truly does not alter meaningful product truth. Examples may include:

- formatting only;
- comments only;
- non-semantic renames;
- mechanical test cleanup with no change in covered contract;
- equivalent internal refactoring with no behavior, ownership, safety or readiness consequence.

The implementation must make this classification explicit enough that an agent cannot silently skip the decision.

---

## 0D. Canonical owner routing law

Distribution is the packaging, release, compatibility, installation, update, rollback, qualification and lifecycle-orchestration owner. It is not a second implementation home for sibling component behavior.

Whenever Distribution work discovers a defect, missing capability, required improvement or behavior change, the work must first determine the canonical owner.

Examples of canonical ownership include:

- `AI-Verse-Skills` owns Skills engine behavior, Skill packages, registry/provider behavior, generations, provenance, trust/admission and Skills-specific lifecycle semantics;
- `AI-Verse-Brain` owns Brain implementation and Brain-specific domain behavior;
- `AI-Verse-Memory` owns Memory implementation and Memory-specific domain behavior;
- `AI-Verse-Data` owns Data implementation and Data-specific domain behavior;
- `AI-Verse-OS` owns OS/host implementation and OS-specific domain behavior;
- other AI-Verse component repositories retain their documented canonical responsibilities;
- `ai-verse-distribution` owns cross-component packaging, release-set selection, compatibility resolution, immutable acquisition, install/update/rollback orchestration, Distribution receipts/locks, release-level qualification and Distribution-specific member delivery behavior.

The required routing sequence is:

```text
Distribution work discovers or requires a change
        |
        v
Determine canonical owner
        |
        +--> DISTRIBUTION
        |       |
        |       v
        |   Fix in Distribution
        |
        +--> SIBLING COMPONENT
                |
                v
        Fix in owning repository
                |
                v
        Test/accept owner change
                |
                v
        Record immutable owner commit/ref
                |
                v
        Distribution pins/adopts that ref
                |
                v
        Distribution qualifies the composed release
                |
                v
        Propagate meaningful product truth to System
```

### Non-negotiable consequences

1. **Do not patch a genuine sibling-owned defect only inside Distribution.** A Distribution workaround must not become the permanent substitute for repairing the canonical owner.
2. **Do not duplicate sibling domain logic into Distribution merely to make a release pass.**
3. **Do not claim a sibling-owned problem is fixed until the owner repository contains the accepted fix/improvement and exact evidence exists.**
4. **Distribution may contain adapters only for concerns canonically owned by Distribution**, such as bounded orchestration, compatibility translation, packaging, release transitions or invocation of owner lifecycle surfaces. An adapter must not silently become a second copy of the sibling engine.
5. **After a sibling-owned change lands, Distribution must adopt an immutable accepted revision before claiming that the composed product includes the change.**
6. **System propagation happens after ownership truth is resolved.** AI-Verse-System must describe both the meaningful product change and the correct owner rather than documenting a Distribution workaround as canonical sibling behavior.
7. If ownership is ambiguous, classify the work as `BLOCKED - OWNER UNRESOLVED` until System ownership evidence resolves it. Do not choose Distribution merely because the issue was discovered there.

Every meaningful Distribution task/release covered by this program must be able to record:

```text
Canonical owner: <repo/component>
Owner change required: YES | NO
Owner reason: <why this owner is authoritative>
Owner evidence: <commit/PR/ref when required>
Distribution adaptation required: YES | NO
Distribution evidence: <commit/PR/ref when applicable>
System impact: YES | NO
System evidence: <commit/PR/ref when YES>
```

This rule prevents implementation drift between Distribution and the actual component repositories.

---

## 0E. No blind cross-repo mirroring

Do not implement a mechanism that automatically copies every Distribution commit or changelog line into AI-Verse-System or automatically edits every sibling repository.

AI-Verse-System owns the evolving architectural/product truth. Component repositories own their implementations. Distribution owns composition and delivery.

The desired loop is evidence-driven and ownership-aware, not repository mirroring.

If automation is introduced, prefer validation, evidence and pull-request creation over direct unattended writes to another repository's default branch.

---

## 0F. Member-isolation law

A Distribution maintainer instruction is not a member instruction.

The implementation must prove that:

- source `AGENTS.md`/`CLAUDE.md` maintainer rules are not reused blindly as generated member instructions;
- internal System-propagation or owner-routing text is absent from member-facing generated `AGENTS.md` and `CLAUDE.md`;
- internal roadmap/qualification/maintainer documents are absent from the member project payload;
- internal propagation/owner-routing records are absent from normal runtime configuration unless a runtime field is genuinely needed for product behavior;
- install/update qualification includes regression coverage for governance leakage;
- future additions to maintainer-only paths cannot silently enter the member payload.

If the user deliberately clones a source repository for development, source-only files naturally exist in that source checkout. That is distinct from the member AI-Verse installation produced by Distribution. This program protects the installed product surface.

---

## 0G. Preservation law

Nothing in this program may weaken the existing zero-loss update direction.

No member-owned state may be deleted, reset, overwritten, replaced or silently discarded to enforce packaging separation, canonical-owner routing or System propagation.

Preserve canonical ownership of:

- memories;
- goals;
- preferences;
- profile;
- Brain direction;
- workspaces;
- decisions;
- Data databases;
- connections;
- custom files;
- user-created Skills;
- automations;
- extensions;
- project history;
- other user-owned state recognized by the current Distribution preservation contract.

If a packaging, routing or propagation mechanism conflicts with user ownership, fail safely rather than rewriting user state.

---

## 0H. Status vocabulary and required slice evidence

- `NOT STARTED`
- `IN PROGRESS`
- `BLOCKED`
- `COMPLETE`

Every slice must record, where applicable:

- affected repo(s);
- exact starting refs inspected;
- canonical owner(s);
- owner change required: `YES | NO`;
- owner evidence/ref when required;
- implementation decision;
- member-isolation decision;
- System-propagation decision;
- acceptance criteria;
- focused tests/validation;
- exact commit/PR/workflow evidence;
- explicit NEXT slice.

Do not mark a slice COMPLETE merely because code was written.

---

## 0I. Program accounting rule

This plan begins and remains at 14 slices unless implementation genuinely requires a denominator change.

Do not silently change the denominator. If implementation reveals that a slice must be split, added, merged or removed:

1. update `Program size`, `Completed`, `Remaining` and `Progress`;
2. explain the change in this document's Program Change Log;
3. preserve completed-slice history;
4. do not use denominator changes to inflate progress.

---

# Phase 0 - Persistent canonical program

## Slice 0.1 - Create persistent implementation plan

**Status:** COMPLETE  
**Repos:** AI-Verse-System  
**Dependencies:** none

### Acceptance criteria

- canonical plan exists in AI-Verse-System;
- mission covers Distribution -> System propagation, canonical component ownership and member-install isolation;
- meaningful improvements, not only architecture changes, trigger System evaluation;
- pure internal/no-impact changes are explicitly distinguished;
- member-facing and maintainer-facing surfaces are explicitly separated;
- broad repository copying is rejected as the member payload model;
- sibling-owned fixes are prohibited from becoming Distribution-only permanent fixes;
- phased implementation work is represented as resumable slices;
- every future slice has evidence-gated completion;
- future agents can resume from this file without the original conversation.

### Evidence

- canonical path: `docs/DISTRIBUTION-SYSTEM-PROPAGATION-IMPLEMENTATION-PLAN.md`
- created: 2026-10-12
- owner-routing requirement added to the persistent plan on 2026-10-12 without changing the 14-slice denominator

### NEXT

**Slice 1.1 - Audit the current Distribution source-to-member and Distribution-to-owner boundaries.**

---

# Phase 1 - Prove the current boundaries before changing them

## Slice 1.1 - Audit current Distribution source-to-member and owner boundaries

**Status:** NOT STARTED  
**Repos:** ai-verse-distribution, AI-Verse-System, relevant sibling owner repositories as evidence requires  
**Dependencies:** 0.1

Read current Distribution source rather than relying on historical assumptions.

Trace at minimum:

- `AGENTS.md`;
- `CLAUDE.md`;
- `INSTALL.md`;
- package/build configuration;
- install/bootstrap orchestration;
- project bootstrap/generation code;
- generated project `AGENTS.md`;
- generated project `CLAUDE.md`;
- generated `AI-VERSE.yaml`;
- runtime/package manifests;
- release-set materialization;
- private tool/cache/source-checkout locations;
- member project root outputs;
- update and rollback materialization paths;
- tests that assert installed file trees;
- all component-specific adapters and lifecycle handlers in Distribution;
- any Distribution code that patches, rewrites, vendors, substitutes for or compensates for sibling-owned behavior;
- current exact component refs used by admitted release sets;
- current System ownership records for the affected components.

### Acceptance criteria

- exact current member project payload path is documented from source evidence;
- exact current generated-member-instruction path is documented;
- exact current source-only/developer paths are documented;
- any source checkout retained on a member machine is distinguished from the installed project/runtime payload;
- all routes by which maintainer files could leak into member surfaces are identified;
- all current Distribution-to-component adapters are classified by canonical owner;
- any suspected case where Distribution contains a permanent workaround for a sibling-owned defect is identified for resolution rather than normalized;
- exact current release refs show which owner revision Distribution actually ships;
- no implementation change is made before both boundaries are understood.

### Evidence

To be recorded on completion.

### NEXT

**Slice 1.2 - Build the canonical file/surface and owner classification inventory.**

---

## Slice 1.2 - Classify relevant Distribution surfaces and ownership

**Status:** NOT STARTED  
**Repos:** ai-verse-distribution, AI-Verse-System, relevant sibling owner repositories  
**Dependencies:** 1.1

Create a classification of relevant Distribution files/outputs using at least these surface classes:

- `MAINTAINER-SOURCE-ONLY`
- `BUILD/QUALIFICATION-ONLY`
- `PACKAGING-INTERNAL`
- `MEMBER-RUNTIME`
- `MEMBER-GENERATED-INSTRUCTION`
- `USER-OWNED/PRESERVED`
- `AMBIGUOUS - MUST RESOLVE BEFORE SHIPPING`

For component-related behavior, also classify canonical ownership:

- `DISTRIBUTION-OWNED`
- `SIBLING-OWNER-IMPLEMENTATION`
- `DISTRIBUTION-ADAPTER-TO-OWNER`
- `AMBIGUOUS-OWNER - BLOCKED UNTIL RESOLVED`

### Acceptance criteria

- every current source-to-install route from 1.1 has a surface classification;
- every component-specific Distribution behavior from 1.1 has an owner classification;
- ambiguous paths are not silently treated as member-safe;
- ambiguous ownership is not silently assigned to Distribution;
- user-owned paths remain explicitly protected;
- the inventory identifies the authoritative code/config that decides what becomes member-facing;
- the inventory identifies the authoritative repository for every meaningful implementation concern encountered;
- a future maintainer file has a safe default of exclusion rather than accidental inclusion;
- a future sibling-owned defect has a safe default of routing to the owner rather than patching Distribution.

### Evidence

To be recorded on completion.

### NEXT

**Slice 1.3 - Define enforceable member payload and canonical-owner contracts.**

---

## Slice 1.3 - Define member payload, owner-routing and leak threat contracts

**Status:** NOT STARTED  
**Repos:** AI-Verse-System, ai-verse-distribution  
**Dependencies:** 1.2

Define the exact contract for what Distribution is allowed to place into a member installation and what Distribution is allowed to own when interacting with sibling components.

Prefer an allowlist or deterministic generation model where technically practical.

Document member-payload threats including:

- recursive copy of repository root;
- package-data wildcard expansion;
- docs accidentally included in a wheel/archive;
- root `AGENTS.md` reused as member `AGENTS.md`;
- root `CLAUDE.md` reused as member `CLAUDE.md`;
- update code copying newly added source files into existing projects;
- rollback restoring internal governance into project root;
- release-set packaging admitting unexpected developer files;
- test fixtures or qualification assets entering production payloads.

Document ownership threats including:

- fixing a Skills/Brain/Memory/Data/OS defect only in Distribution;
- copying sibling engine/domain logic into a Distribution adapter;
- leaving the owner repo broken while Distribution hides the defect;
- pinning an old owner revision after claiming a newer owner fix is part of the product;
- documenting a Distribution workaround in System as if it were canonical owner behavior;
- allowing release qualification to pass when an owner-required change lacks exact owner evidence.

### Acceptance criteria

- explicit member payload contract exists;
- explicit canonical-owner routing contract exists;
- the safe default for unknown maintainer files is exclusion;
- the safe default for ambiguous implementation ownership is fail/block until resolved;
- generated member instructions are treated as distinct artifacts from source maintainer instructions;
- update and rollback obey the same payload boundary as fresh install;
- preservation rules take precedence over cleanup/removal of anything user-owned;
- Distribution adapters cannot become untracked substitutes for sibling fixes;
- contracts are ready to be enforced by tests in Phase 3.

### Evidence

To be recorded on completion.

### NEXT

**Slice 2.1 - Create canonical System-side propagation and owner-routing contract.**

---

# Phase 2 - Establish canonical propagation and ownership governance

## Slice 2.1 - Create System-side Distribution propagation and owner-routing contract

**Status:** NOT STARTED  
**Repos:** AI-Verse-System  
**Dependencies:** 1.3

Create the canonical System document that defines how meaningful Distribution evolution propagates into AI-Verse-System and how Distribution-discovered implementation work routes to canonical component owners.

The contract must include:

- meaningful-change triggers;
- `SYSTEM IMPACT` versus `NO SYSTEM IMPACT` classification;
- canonical owner classification;
- `OWNER CHANGE REQUIRED` versus `NO OWNER CHANGE REQUIRED` classification;
- examples for Distribution-owned work, sibling-owned work, improvements, fixes and internal-only work;
- required sequence for owner fix -> immutable ref -> Distribution adoption -> qualification -> System propagation;
- System destinations that may require updates;
- owner and System evidence requirements;
- completion semantics;
- member-isolation requirement;
- rule against blind commit mirroring;
- rule against Distribution becoming a second sibling implementation layer;
- rule against unattended direct writes to another repo's main branch unless separately approved and safely designed.

### Acceptance criteria

- contract is canonical and self-contained;
- it covers meaningful improvements even when architecture does not change;
- it is compatible with `docs/LIVING-SPEC-PROTOCOL.md`;
- it preserves component repository implementation ownership;
- it makes clear that discovery location does not determine canonical ownership;
- it does not claim every change must touch every System document;
- it cannot be interpreted as a runtime/member requirement.

### Evidence

To be recorded on completion.

### NEXT

**Slice 2.2 - Integrate propagation and owner-routing rules into System living governance.**

---

## Slice 2.2 - Integrate propagation and owner routing into System living governance

**Status:** NOT STARTED  
**Repos:** AI-Verse-System  
**Dependencies:** 2.1

Update the appropriate canonical System governance so future agents discover both rules naturally.

Evaluate and update where appropriate:

- `docs/LIVING-SPEC-PROTOCOL.md`;
- `docs/OWNER-PRODUCT-INTENT.md`;
- `docs/FINAL-AI-VERSE-BLUEPRINT.md` if ownership/topology requires clarification;
- component ownership/specification records;
- Distribution-related System records;
- `docs/SYSTEM-CHANGELOG.md`.

Do not add text to files merely for repetition. Each update must have a clear canonical purpose.

### Acceptance criteria

- future System agents discover the Distribution propagation requirement without needing this conversation;
- future System agents discover the rule that sibling implementation fixes must land in the sibling owner repo;
- owner intent records the requirement that maintainer governance stay outside member installations when this is the correct canonical destination;
- System changelog records the adopted governance;
- blueprint/spec changes are made only where they clarify real topology/ownership/lifecycle truth;
- no claim of Distribution implementation is made before Phase 3 lands.

### Evidence

To be recorded on completion.

### NEXT

**Slice 2.3 - Define the owner/propagation decision and evidence schema used by Distribution work.**

---

## Slice 2.3 - Define owner-routing and propagation evidence schema

**Status:** NOT STARTED  
**Repos:** AI-Verse-System, ai-verse-distribution  
**Dependencies:** 2.2

Define a lightweight, durable decision format that can be used by meaningful Distribution tasks/releases.

Minimum semantic fields:

```text
Canonical owner: <component/repository>
Owner change required: YES | NO
Owner reason: <concise rationale>
Owner evidence: <commit/PR/ref when required>
Distribution adaptation required: YES | NO
Distribution evidence: <commit/PR/ref when applicable>
System impact: YES | NO
System reason: <concise rationale>
System destinations evaluated: <paths/categories>
System evidence: <commit/PR/ref when YES>
Member payload impact: YES | NO
Member-isolation check: PASS | NOT APPLICABLE | BLOCKED
```

The exact storage location must be chosen after the Phase 1 audit. Do not create a second general release database merely for this rule.

### Acceptance criteria

- schema is small enough to use routinely;
- meaningful Distribution work cannot be closed without an owner decision and System-impact decision;
- `Owner change required: YES` requires exact accepted owner evidence before the fix is represented as complete;
- when owner change is required, Distribution adoption/pinning of the accepted immutable owner revision is evidence-gated;
- `Owner change required: NO` requires enough rationale to show the concern is genuinely Distribution-owned or no implementation change is needed;
- `System impact: NO` requires a reason rather than silent omission;
- `System impact: YES` can point to exact System evidence;
- schema does not expose maintainer governance into member runtime files;
- schema composes with existing Distribution release/program records rather than duplicating them unnecessarily.

### Evidence

To be recorded on completion.

### NEXT

**Slice 3.1 - Add source-only maintainer instructions to Distribution.**

---

# Phase 3 - Enforce the rules in Distribution without leaking them to members

## Slice 3.1 - Add source-only Distribution maintainer instructions

**Status:** NOT STARTED  
**Repos:** ai-verse-distribution  
**Dependencies:** 2.3

Update Distribution's source-repository maintainer instructions so an AI or contributor working on Distribution knows it must both route implementation work to the canonical owner and propagate meaningful product truth into System.

Expected surfaces include current source `AGENTS.md` and `CLAUDE.md` where appropriate, but exact edits must follow the Phase 1 audit.

### Acceptance criteria

- meaningful Distribution evolution explicitly triggers System evaluation;
- improvements and important fixes are included, not only architecture changes;
- every meaningful component-related issue requires a canonical-owner decision;
- sibling-owned defects/improvements explicitly route to the sibling repo first;
- Distribution-only permanent patches for sibling-owned behavior are prohibited;
- owner acceptance and exact immutable owner evidence are required before Distribution claims the sibling fix is included;
- pure internal/no-impact work may be classified `NO SYSTEM IMPACT` with reason;
- instruction points to canonical System governance where practical;
- instruction explicitly states it is maintainer-only;
- no member-generated `AGENTS.md`/`CLAUDE.md` inherits the maintainer rule;
- focused tests prove member instruction templates remain clean.

### Evidence

To be recorded on completion.

### NEXT

**Slice 3.2 - Add canonical-owner and System-propagation completion gates to Distribution work/release flow.**

---

## Slice 3.2 - Add Distribution owner-routing and propagation completion gates

**Status:** NOT STARTED  
**Repos:** ai-verse-distribution  
**Dependencies:** 3.1

Integrate the decision schema from 2.3 into the most authoritative existing Distribution development/release lifecycle surface.

Do not invent a parallel lifecycle system if the existing Core/Agent release, roadmap, qualification or release-record machinery can carry the decisions.

### Acceptance criteria

- meaningful task/release completion requires an explicit canonical-owner decision;
- `OWNER CHANGE REQUIRED: YES` requires exact owner evidence;
- sibling-owned changes cannot be represented as fixed solely by a Distribution commit;
- when a sibling change is required, the composed release must point to/adopt the accepted immutable owner revision before qualification can claim inclusion;
- `OWNER CHANGE REQUIRED: NO` requires rationale;
- meaningful task/release completion requires an explicit System-impact decision;
- `SYSTEM IMPACT: YES` requires exact System evidence before architectural/documentation completion is claimed;
- `SYSTEM IMPACT: NO` requires rationale;
- implementation may remain technically merged while owner/System completeness is visibly blocked if required evidence is missing;
- no runtime/member file is used as canonical storage for maintainer decisions;
- existing release/preservation contracts remain intact.

### Evidence

To be recorded on completion.

### NEXT

**Slice 3.3 - Enforce member payload isolation and prevent sibling implementation shadowing.**

---

## Slice 3.3 - Enforce member payload isolation and component ownership boundaries

**Status:** NOT STARTED  
**Repos:** ai-verse-distribution  
**Dependencies:** 3.2

Implement the member payload contract from 1.3 in the actual packaging/install/update paths and ensure Distribution materializes admitted owner revisions rather than carrying shadow copies of sibling implementations.

Where technically practical, prefer explicit inclusion of intended member artifacts over copying a broad source tree and deleting unwanted files afterward.

### Acceptance criteria

- fresh install excludes maintainer-only governance;
- update excludes maintainer-only governance;
- rollback excludes maintainer-only governance;
- generated member instructions come from their intended member templates/generation path, not source maintainer files;
- unexpected new files under maintainer-only paths do not become member payload by default;
- no user-owned file is deleted merely because its filename collides with an internal convention;
- ambiguity fails safely rather than overwriting user content;
- component bytes/behavior shipped by Distribution trace to the admitted canonical owner revision or an explicitly documented Distribution-owned adapter;
- no new mechanism silently vendors a patched sibling implementation into Distribution as a substitute for the owner repository.

### Evidence

To be recorded on completion.

### NEXT

**Slice 3.4 - Add automated isolation, owner-routing and propagation regression tests.**

---

## Slice 3.4 - Add regression coverage

**Status:** NOT STARTED  
**Repos:** ai-verse-distribution  
**Dependencies:** 3.3

Add focused automated tests for member isolation, canonical-owner routing and System propagation.

Required scenarios include:

- fresh member install contains expected generated member files;
- fresh install does not contain maintainer propagation/owner-routing text or files;
- update does not introduce maintainer files;
- rollback does not introduce maintainer files;
- newly added fake maintainer document remains excluded;
- source maintainer `AGENTS.md` is distinguishable from generated member `AGENTS.md`;
- source maintainer `CLAUDE.md` is distinguishable from generated member `CLAUDE.md`;
- canonical-owner decision is required where the governance gate says it is required;
- a simulated sibling-owned defect, such as a Skills-engine defect, cannot be closed with only Distribution evidence;
- `OWNER CHANGE REQUIRED: YES` with missing owner evidence fails the gate;
- accepted owner evidence plus Distribution adoption of the immutable owner ref can pass the owner gate;
- a genuinely Distribution-owned orchestration change does not falsely require a sibling implementation commit;
- propagation decision is required where the chosen governance gate says it is required;
- explicit `NO SYSTEM IMPACT` path requires rationale;
- missing System evidence blocks documented completion when impact is `YES`;
- preservation fixtures prove user-owned state is unchanged.

### Acceptance criteria

- tests fail on deliberate governance leakage;
- tests fail when sibling-owned work is falsely represented as a Distribution-only fix;
- tests fail when required owner evidence or required owner revision adoption is missing;
- tests pass for legitimate Distribution-owned adapters/orchestration;
- tests fail on missing required System propagation evidence;
- tests pass on legitimate no-impact changes/fixtures;
- tests protect update and rollback, not only first install;
- tests do not weaken existing Core update preservation qualification.

### Evidence

To be recorded on completion.

### NEXT

**Slice 4.1 - Add cross-repo owner and System evidence validation at the strongest safe boundary.**

---

# Phase 4 - Close and qualify the loop

## Slice 4.1 - Add cross-repo owner and System evidence validation

**Status:** NOT STARTED  
**Repos:** ai-verse-distribution, AI-Verse-System, relevant sibling owner repositories  
**Dependencies:** 3.4

Implement the strongest safe verification available without creating unsafe cross-repo write authority.

Preferred behavior:

- Distribution records an exact owner commit/PR/reference when owner change is required;
- qualification verifies that the release actually adopts the accepted immutable owner revision or a descendant where the explicit release contract permits that lineage;
- Distribution records an exact System commit/PR/reference when System impact is `YES`;
- qualification validates evidence formats and, when repository permissions safely permit it, verifies that referenced evidence exists;
- automation may create or request an owner/System PR only if separately justified and least-privilege credentials are available;
- do not silently grant Distribution CI broad write access to System or sibling repositories;
- do not directly auto-write to another repo's main branch merely for convenience.

### Acceptance criteria

- stale/missing owner evidence is detectable at the chosen completion/release boundary;
- a claimed sibling fix cannot qualify if the release still pins a revision that does not contain the accepted fix;
- stale/missing System evidence is detectable at the chosen completion/release boundary;
- validation fails closed where evidence is mandatory;
- inability to access a cross-repo ref is reported distinctly from evidence being absent;
- no secret is placed into member artifacts;
- no new broad repository credential is introduced without explicit need and documented scope;
- semantic propagation and canonical ownership remain the rules, not commit mirroring.

### Evidence

To be recorded on completion.

### NEXT

**Slice 4.2 - Run end-to-end owner-to-Distribution-to-System-to-member qualification.**

---

## Slice 4.2 - End-to-end qualification

**Status:** NOT STARTED  
**Repos:** ai-verse-distribution, AI-Verse-System, at least one representative sibling owner repo  
**Dependencies:** 4.1

Run representative end-to-end scenarios covering both ownership paths.

### Scenario A - Distribution-owned meaningful improvement

1. make or simulate a meaningful Distribution-owned improvement;
2. classify canonical owner as Distribution;
3. classify System impact;
4. update relevant System truth;
5. record exact Distribution/System evidence;
6. build/qualify Distribution;
7. install into a clean member project;
8. verify no maintainer governance leaks.

### Scenario B - sibling-owned problem discovered during Distribution work

1. discover or simulate a meaningful sibling-owned defect/improvement, preferably using Skills as one representative owner;
2. classify the canonical owner correctly;
3. implement or use an accepted owner-repo fix;
4. record exact owner evidence;
5. update Distribution to adopt the accepted immutable owner revision;
6. qualify the composed release;
7. update relevant System truth and record exact System evidence;
8. install into a clean member project;
9. inspect the complete member-facing file tree;
10. inspect generated `AGENTS.md`, `CLAUDE.md` and `AI-VERSE.yaml`;
11. perform an update over representative user-owned state;
12. perform rollback where supported;
13. verify no maintainer governance leaks at any member-facing stage;
14. verify all protected member state survives unchanged;
15. verify the canonical owner repository, Distribution release ref and System truth all agree about the shipped change.

### Acceptance criteria

- Distribution-owned work stays in Distribution without unnecessary sibling edits;
- sibling-owned work is actually repaired in the canonical owner repository;
- Distribution ships the accepted owner revision rather than a local substitute patch;
- propagation loop works from meaningful change to current System evidence;
- member project contains no maintainer propagation/owner-routing instructions or files;
- install/update/rollback all respect the same boundary;
- user-owned state preservation passes;
- qualification output clearly distinguishes owner implementation evidence, Distribution evidence, System evidence and member payload;
- any discovered ambiguity is fixed before completion.

### Evidence

To be recorded on completion.

### NEXT

**Slice 4.3 - Synchronize canonical System truth and close program v1.**

---

## Slice 4.3 - Canonical closeout

**Status:** NOT STARTED  
**Repos:** AI-Verse-System, ai-verse-distribution, affected sibling owner repositories  
**Dependencies:** 4.2

Close the implementation only after end-to-end behavior is proven.

Update all canonical records that actually need to change, including where relevant:

- this implementation plan;
- `docs/LIVING-SPEC-PROTOCOL.md`;
- `docs/OWNER-PRODUCT-INTENT.md`;
- `docs/FINAL-AI-VERSE-BLUEPRINT.md`;
- component ownership/specification records;
- Distribution-related System documentation/QC/source maps;
- `docs/SYSTEM-CHANGELOG.md`;
- Distribution maintainer documentation;
- qualification/release evidence.

### Acceptance criteria

- all 14 slices are COMPLETE with exact evidence;
- AI-Verse-System accurately describes the finished propagation and owner-routing behavior;
- Distribution source instructions enforce both policies for future work;
- member payload isolation is automated and regression-tested;
- meaningful Distribution evolution cannot silently leave System stale under the supported maintainer workflow;
- a sibling-owned defect/improvement discovered during Distribution work cannot be permanently fixed only in Distribution under the supported workflow;
- released component behavior traces to the accepted canonical owner revision;
- Distribution cannot claim a sibling fix is shipped while still pinning an owner revision that lacks it;
- no maintainer governance is present in the member installation;
- zero-loss update/preservation contracts remain satisfied;
- program status is changed from ACTIVE to COMPLETE only after all acceptance criteria pass.

### Evidence

To be recorded on completion.

### NEXT

None. Program v1 complete.

---

# Program Change Log

## 2026-10-12 - Canonical owner routing added

- Added the owner's requirement that Distribution must not become a substitute implementation repo for Skills, Brain, Memory, Data, OS or other sibling components.
- Added the canonical routing sequence: determine owner -> fix owner repo when required -> test/accept owner change -> record immutable owner ref -> Distribution adopts/pins ref -> qualify composed release -> propagate meaningful truth to System.
- Added mandatory owner decision/evidence fields to the program.
- Extended Phase 1 to audit current Distribution-to-owner boundaries and detect existing workaround/shadow-implementation risks.
- Extended Phase 2 to make owner routing part of canonical System governance.
- Extended Phase 3 gates and regression coverage so a sibling-owned fix cannot be closed with only Distribution evidence.
- Extended Phase 4 cross-repo validation and end-to-end qualification to prove both Distribution-owned and sibling-owned change paths.
- Kept the program at 14 slices. No denominator change was required.
- Kept Slice 0.1 as the only completed slice. This plan update defines the requirement but does not falsely claim the enforcement implementation already exists.

## 2026-10-12 - Program created

- Created the canonical 14-slice implementation program.
- Recorded the owner's requirement that meaningful Distribution improvements, not only architectural changes, propagate into System.
- Recorded the owner's requirement that this governance remain separate from the member-installed OS.
- Chose semantic propagation rather than blind commit mirroring.
- Chose an audit-first approach so member/source boundaries are proven from current Distribution code before implementation.
- Marked only Slice 0.1 complete.

---

# Current execution pointer

**Completed:** Slice 0.1  
**Next:** Slice 1.1 - Audit current Distribution source-to-member and owner boundaries  
**Do not skip directly to maintainer-rule edits before Slice 1.1 establishes the current packaging/generation boundary and identifies where component-specific behavior is canonically owned.**