# Distribution -> System Propagation and Member Isolation Implementation Plan

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

Make meaningful evolution in `aiverse-filmmakers/ai-verse-distribution` reliably propagate into the canonical `aiverse-filmmakers/AI-Verse-System` record, while keeping all maintainer/development governance completely outside the member-facing AI-Verse installation.

The finished behavior must achieve both goals at once:

1. **System stays current.** Meaningful Distribution features, improvements, fixes, lifecycle changes, release changes, preservation changes, compatibility changes, member-experience changes and architectural changes are evaluated and reflected appropriately in AI-Verse-System.
2. **Members receive only product-relevant files.** Maintainer rules, internal propagation instructions, roadmaps, qualification records, developer-only governance and System synchronization machinery are not copied, generated or exposed as part of the member project/runtime installation.

This program is not a request to mirror every Distribution commit into System. It is a requirement that meaningful product truth cannot evolve in Distribution while System silently becomes stale.

---

## 0A. Non-negotiable separation rule

There are three different surfaces and they must not be confused:

### A. Canonical maintainer/source repositories

These may contain development governance, architecture plans, release qualification, tests, internal agent instructions and propagation rules.

Examples:

- `aiverse-filmmakers/AI-Verse-System`
- `aiverse-filmmakers/ai-verse-distribution`

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

## 0B. Canonical propagation rule to implement

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

## 0D. No blind cross-repo mirroring

Do not implement a mechanism that automatically copies every Distribution commit or changelog line into AI-Verse-System.

AI-Verse-System owns the evolving architectural/product truth, not a duplicate Git history.

The desired loop is:

```text
Meaningful Distribution work
        |
        v
System-impact decision
        |
        +--> NO IMPACT -> record reason where required
        |
        +--> IMPACT
              |
              v
       Update relevant System truth
              |
              v
       Record evidence/ref
              |
              v
       Distribution work can close
```

If automation is introduced, prefer validation, evidence and pull-request creation over direct unattended writes to the System default branch.

---

## 0E. Member-isolation law

A Distribution maintainer instruction is not a member instruction.

The implementation must prove that:

- source `AGENTS.md`/`CLAUDE.md` maintainer rules are not reused blindly as generated member instructions;
- internal System-propagation text is absent from member-facing generated `AGENTS.md` and `CLAUDE.md`;
- internal roadmap/qualification/maintainer documents are absent from the member project payload;
- internal propagation records are absent from normal runtime configuration unless a runtime field is genuinely needed for product behavior;
- install/update qualification includes regression coverage for governance leakage;
- future additions to maintainer-only paths cannot silently enter the member payload.

If the user deliberately clones a source repository for development, source-only files naturally exist in that source checkout. That is distinct from the member AI-Verse installation produced by Distribution. This program protects the installed product surface.

---

## 0F. Preservation law

Nothing in this program may weaken the existing zero-loss update direction.

No member-owned state may be deleted, reset, overwritten, replaced or silently discarded to enforce packaging separation or System propagation.

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

If a packaging or propagation mechanism conflicts with user ownership, fail safely rather than rewriting user state.

---

## 0G. Status vocabulary

- `NOT STARTED`
- `IN PROGRESS`
- `BLOCKED`
- `COMPLETE`

Every slice must record:

- affected repo(s);
- exact starting refs inspected;
- implementation decision;
- member-isolation decision;
- System-propagation decision;
- acceptance criteria;
- focused tests/validation;
- exact commit/PR/workflow evidence;
- explicit NEXT slice.

Do not mark a slice COMPLETE merely because code was written.

---

## 0H. Program accounting rule

This plan begins with 14 slices.

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
- mission covers both Distribution -> System propagation and member-install isolation;
- meaningful improvements, not only architecture changes, trigger System evaluation;
- pure internal/no-impact changes are explicitly distinguished;
- member-facing and maintainer-facing surfaces are explicitly separated;
- broad repository copying is rejected as the member payload model;
- phased implementation work is represented as resumable slices;
- every future slice has evidence-gated completion;
- future agents can resume from this file without the original conversation.

### Evidence

- canonical path: `docs/DISTRIBUTION-SYSTEM-PROPAGATION-IMPLEMENTATION-PLAN.md`
- created: 2026-10-12

### NEXT

**Slice 1.1 - Audit the current Distribution source-to-member installation boundary.**

---

# Phase 1 - Prove the current boundary before changing it

## Slice 1.1 - Audit current Distribution source-to-member installation boundary

**Status:** NOT STARTED  
**Repos:** ai-verse-distribution, AI-Verse-System  
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
- tests that assert installed file trees.

### Acceptance criteria

- exact current member project payload path is documented from source evidence;
- exact current generated-member-instruction path is documented;
- exact current source-only/developer paths are documented;
- any source checkout retained on a member machine is distinguished from the installed project/runtime payload;
- all routes by which maintainer files could leak into member surfaces are identified;
- no implementation change is made before the boundary is understood.

### Evidence

To be recorded on completion.

### NEXT

**Slice 1.2 - Build the canonical file/surface classification inventory.**

---

## Slice 1.2 - Classify every relevant Distribution surface

**Status:** NOT STARTED  
**Repos:** ai-verse-distribution, AI-Verse-System  
**Dependencies:** 1.1

Create a classification of relevant Distribution files/outputs using at least these classes:

- `MAINTAINER-SOURCE-ONLY`
- `BUILD/QUALIFICATION-ONLY`
- `PACKAGING-INTERNAL`
- `MEMBER-RUNTIME`
- `MEMBER-GENERATED-INSTRUCTION`
- `USER-OWNED/PRESERVED`
- `AMBIGUOUS - MUST RESOLVE BEFORE SHIPPING`

The inventory must cover current and foreseeable governance locations, including root maintainer instructions and `docs/` maintainer material.

### Acceptance criteria

- every current source-to-install route from 1.1 has a classification;
- ambiguous paths are not silently treated as member-safe;
- user-owned paths remain explicitly protected;
- the inventory identifies the authoritative code/config that decides what becomes member-facing;
- a future maintainer file has a safe default of exclusion rather than accidental inclusion.

### Evidence

To be recorded on completion.

### NEXT

**Slice 1.3 - Define the enforceable member payload contract.**

---

## Slice 1.3 - Define member payload contract and leak threat model

**Status:** NOT STARTED  
**Repos:** AI-Verse-System, ai-verse-distribution  
**Dependencies:** 1.2

Define the exact contract for what Distribution is allowed to place into a member installation.

Prefer an allowlist or deterministic generation model where technically practical.

Document threats including:

- recursive copy of repository root;
- package-data wildcard expansion;
- docs accidentally included in a wheel/archive;
- root `AGENTS.md` reused as member `AGENTS.md`;
- root `CLAUDE.md` reused as member `CLAUDE.md`;
- update code copying newly added source files into existing projects;
- rollback restoring internal governance into project root;
- release-set packaging admitting unexpected developer files;
- test fixtures or qualification assets entering production payloads.

### Acceptance criteria

- explicit member payload contract exists;
- the safe default for unknown maintainer files is exclusion;
- generated member instructions are treated as distinct artifacts from source maintainer instructions;
- update and rollback must obey the same payload boundary as fresh install;
- preservation rules take precedence over cleanup/removal of anything user-owned;
- contract is ready to be enforced by tests in Phase 3.

### Evidence

To be recorded on completion.

### NEXT

**Slice 2.1 - Create canonical System-side Distribution propagation contract.**

---

# Phase 2 - Establish canonical propagation governance

## Slice 2.1 - Create System-side Distribution propagation contract

**Status:** NOT STARTED  
**Repos:** AI-Verse-System  
**Dependencies:** 1.3

Create the canonical System document that defines how meaningful Distribution evolution must propagate into AI-Verse-System.

The contract must include:

- meaningful-change triggers;
- `SYSTEM IMPACT` versus `NO SYSTEM IMPACT` classification;
- examples for features, improvements, fixes and internal-only work;
- System destinations that may require updates;
- evidence requirements;
- completion semantics;
- member-isolation requirement;
- rule against blind commit mirroring;
- rule against unattended direct writes to System main unless separately approved and safely designed.

### Acceptance criteria

- contract is canonical and self-contained;
- it covers meaningful improvements even when architecture does not change;
- it is compatible with `docs/LIVING-SPEC-PROTOCOL.md`;
- it does not claim every change must touch every System document;
- it cannot be interpreted as a runtime/member requirement.

### Evidence

To be recorded on completion.

### NEXT

**Slice 2.2 - Integrate propagation rules into System living governance.**

---

## Slice 2.2 - Integrate propagation into System living governance

**Status:** NOT STARTED  
**Repos:** AI-Verse-System  
**Dependencies:** 2.1

Update the appropriate canonical System governance so future agents discover this rule naturally.

Evaluate and update where appropriate:

- `docs/LIVING-SPEC-PROTOCOL.md`;
- `docs/OWNER-PRODUCT-INTENT.md`;
- `docs/FINAL-AI-VERSE-BLUEPRINT.md` if ownership/topology requires clarification;
- Distribution-related System records;
- `docs/SYSTEM-CHANGELOG.md`.

Do not add text to files merely for repetition. Each update must have a clear canonical purpose.

### Acceptance criteria

- future System agents discover the Distribution propagation requirement without needing this conversation;
- owner intent records the requirement that maintainer governance stay outside member installations when this is the correct canonical destination;
- System changelog records the adopted rule;
- blueprint/spec changes are made only if the rule changes canonical topology/ownership/lifecycle truth;
- no claim of Distribution implementation is made before Phase 3 lands.

### Evidence

To be recorded on completion.

### NEXT

**Slice 2.3 - Define the propagation decision/evidence schema used by Distribution work.**

---

## Slice 2.3 - Define propagation decision and evidence schema

**Status:** NOT STARTED  
**Repos:** AI-Verse-System, ai-verse-distribution  
**Dependencies:** 2.2

Define a lightweight, durable decision format that can be used by meaningful Distribution tasks/releases.

Minimum semantic fields:

```text
System impact: YES | NO
Reason: <concise rationale>
System destinations evaluated: <paths/categories>
System evidence: <commit/PR/ref when YES>
Member payload impact: YES | NO
Member-isolation check: PASS | NOT APPLICABLE | BLOCKED
```

The exact storage location must be chosen after the Phase 1 audit. Do not create a second general release database merely for this rule.

### Acceptance criteria

- schema is small enough to use routinely;
- a meaningful Distribution change cannot be closed without an impact decision;
- `NO` requires a reason rather than silent omission;
- `YES` can point to exact System evidence;
- schema does not expose maintainer governance into member runtime files;
- schema composes with existing Distribution release/program records rather than duplicating them unnecessarily.

### Evidence

To be recorded on completion.

### NEXT

**Slice 3.1 - Add source-only maintainer instructions to Distribution.**

---

# Phase 3 - Enforce the rule in Distribution without leaking it to members

## Slice 3.1 - Add source-only Distribution maintainer instructions

**Status:** NOT STARTED  
**Repos:** ai-verse-distribution  
**Dependencies:** 2.3

Update Distribution's source-repository maintainer instructions so an AI or contributor working on Distribution knows it must evaluate and propagate meaningful change into System.

Expected surfaces include current source `AGENTS.md` and `CLAUDE.md` where appropriate, but exact edits must follow the Phase 1 audit.

### Acceptance criteria

- meaningful Distribution evolution explicitly triggers System evaluation;
- improvements and important fixes are included, not only architecture changes;
- pure internal/no-impact work may be classified `NO SYSTEM IMPACT` with reason;
- instruction points to canonical System governance where practical;
- instruction explicitly states it is maintainer-only;
- no member-generated `AGENTS.md`/`CLAUDE.md` inherits the maintainer rule;
- focused tests prove the member instruction templates remain clean.

### Evidence

To be recorded on completion.

### NEXT

**Slice 3.2 - Add propagation decision/evidence gate to Distribution work/release flow.**

---

## Slice 3.2 - Add Distribution propagation completion gate

**Status:** NOT STARTED  
**Repos:** ai-verse-distribution  
**Dependencies:** 3.1

Integrate the decision schema from 2.3 into the most authoritative existing Distribution development/release lifecycle surface.

Do not invent a parallel lifecycle system if the existing Core/Agent release, roadmap, qualification or release-record machinery can carry the decision.

### Acceptance criteria

- meaningful task/release completion requires an explicit System-impact decision;
- `SYSTEM IMPACT: YES` requires exact System evidence before architectural/documentation completion is claimed;
- `SYSTEM IMPACT: NO` requires rationale;
- implementation may remain technically merged while documentation completeness is visibly blocked if System propagation is missing;
- no runtime/member file is used as the canonical storage for this maintainer decision;
- existing release/preservation contracts remain intact.

### Evidence

To be recorded on completion.

### NEXT

**Slice 3.3 - Enforce member payload exclusion/allowlisting.**

---

## Slice 3.3 - Enforce member payload isolation

**Status:** NOT STARTED  
**Repos:** ai-verse-distribution  
**Dependencies:** 3.2

Implement the member payload contract from 1.3 in the actual packaging/install/update paths.

Where technically practical, prefer explicit inclusion of intended member artifacts over copying a broad source tree and deleting unwanted files afterward.

### Acceptance criteria

- fresh install excludes maintainer-only governance;
- update excludes maintainer-only governance;
- rollback excludes maintainer-only governance;
- generated member instructions come from their intended member templates/generation path, not source maintainer files;
- unexpected new files under maintainer-only paths do not become member payload by default;
- no user-owned file is deleted merely because its filename collides with an internal convention;
- ambiguity fails safely rather than overwriting user content.

### Evidence

To be recorded on completion.

### NEXT

**Slice 3.4 - Add automated isolation and propagation regression tests.**

---

## Slice 3.4 - Add regression coverage

**Status:** NOT STARTED  
**Repos:** ai-verse-distribution  
**Dependencies:** 3.3

Add focused automated tests for both sides of the contract.

Required scenarios include:

- fresh member install contains expected generated member files;
- fresh install does not contain maintainer propagation text/files;
- update does not introduce maintainer files;
- rollback does not introduce maintainer files;
- newly added fake maintainer document remains excluded;
- source maintainer `AGENTS.md` is distinguishable from generated member `AGENTS.md`;
- source maintainer `CLAUDE.md` is distinguishable from generated member `CLAUDE.md`;
- propagation decision is required where the chosen governance gate says it is required;
- explicit `NO SYSTEM IMPACT` path requires rationale;
- missing System evidence blocks documented completion when impact is `YES`;
- preservation fixtures prove user-owned state is unchanged.

### Acceptance criteria

- tests fail on deliberate governance leakage;
- tests fail on missing required propagation evidence;
- tests pass on legitimate no-impact changes/fixtures;
- tests protect update and rollback, not only first install;
- tests do not weaken existing Core update preservation qualification.

### Evidence

To be recorded on completion.

### NEXT

**Slice 4.1 - Add cross-repo evidence validation at the strongest safe boundary.**

---

# Phase 4 - Close and qualify the loop

## Slice 4.1 - Add cross-repo System evidence validation

**Status:** NOT STARTED  
**Repos:** ai-verse-distribution, AI-Verse-System  
**Dependencies:** 3.4

Implement the strongest safe verification available without creating unsafe cross-repo write authority.

Preferred behavior:

- Distribution records an exact System commit/PR/reference when System impact is `YES`;
- qualification validates the reference format and, when repository permissions safely permit it, verifies that the referenced System evidence exists;
- automation may create or request a System PR only if separately justified and least-privilege credentials are available;
- do not silently grant Distribution CI broad write access to System;
- do not directly auto-write to System main merely for convenience.

### Acceptance criteria

- stale/missing System evidence is detectable at the chosen completion/release boundary;
- validation fails closed where evidence is mandatory;
- inability to access a private cross-repo ref is reported distinctly from evidence being absent;
- no secret is placed into member artifacts;
- no new broad repository credential is introduced without explicit need and documented scope;
- semantic propagation remains the rule, not commit mirroring.

### Evidence

To be recorded on completion.

### NEXT

**Slice 4.2 - Run end-to-end maintainer-to-member qualification.**

---

## Slice 4.2 - End-to-end qualification

**Status:** NOT STARTED  
**Repos:** ai-verse-distribution, AI-Verse-System  
**Dependencies:** 4.1

Run a representative end-to-end scenario covering:

1. make or simulate a meaningful Distribution improvement;
2. classify System impact;
3. update relevant System truth;
4. record exact System evidence;
5. build/qualify Distribution;
6. install into a clean member project;
7. inspect the complete member-facing file tree;
8. inspect generated `AGENTS.md`, `CLAUDE.md` and `AI-VERSE.yaml`;
9. perform an update over representative user-owned state;
10. perform rollback where supported;
11. verify no maintainer governance leaks at any member-facing stage;
12. verify all protected member state survives unchanged.

### Acceptance criteria

- propagation loop works from meaningful Distribution change to current System evidence;
- member project contains no maintainer propagation instructions/files;
- install/update/rollback all respect the same boundary;
- user-owned state preservation passes;
- qualification output clearly distinguishes developer evidence from member payload;
- any discovered ambiguity is fixed before completion.

### Evidence

To be recorded on completion.

### NEXT

**Slice 4.3 - Synchronize canonical System truth and close program v1.**

---

## Slice 4.3 - Canonical closeout

**Status:** NOT STARTED  
**Repos:** AI-Verse-System, ai-verse-distribution  
**Dependencies:** 4.2

Close the implementation only after the end-to-end behavior is proven.

Update all canonical records that actually need to change, including where relevant:

- this implementation plan;
- `docs/LIVING-SPEC-PROTOCOL.md`;
- `docs/OWNER-PRODUCT-INTENT.md`;
- `docs/FINAL-AI-VERSE-BLUEPRINT.md`;
- Distribution-related System documentation/QC/source maps;
- `docs/SYSTEM-CHANGELOG.md`;
- Distribution maintainer documentation;
- qualification/release evidence.

### Acceptance criteria

- all 14 slices are COMPLETE with exact evidence;
- AI-Verse-System accurately describes the finished propagation behavior;
- Distribution source instructions enforce the policy for future work;
- member payload isolation is automated and regression-tested;
- meaningful Distribution evolution cannot silently leave System stale under the supported maintainer workflow;
- no maintainer governance is present in the member installation;
- zero-loss update/preservation contracts remain satisfied;
- program status is changed from ACTIVE to COMPLETE only after all acceptance criteria pass.

### Evidence

To be recorded on completion.

### NEXT

None. Program v1 complete.

---

# Program Change Log

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
**Next:** Slice 1.1 - Audit current Distribution source-to-member installation boundary  
**Do not skip directly to maintainer-rule edits before Slice 1.1 establishes the current packaging/generation boundary.**
