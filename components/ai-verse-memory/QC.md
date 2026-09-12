# AI-Verse Memory QC

## Audit identity

- **Repository:** `aiverse-filmmakers/AI-Verse-Memory`
- **Reviewed branch:** `main`
- **Reviewed revision:** `f5b417f9e7ce1b3f05bc80d10a483d10f6ad10ee`
- **Audit date:** 2026-09-13
- **Current repository version:** `0.2.0`
- **Latest reviewed main CI:** `34709185500`, success

## Final QC verdict

**CURRENT TARGET: NOT YET COMPLETE**

AI-Verse Memory has a strong engine and strong native read/integration architecture. It is substantially closer to release-ready than a prototype. The audit still found current-target defects at exactly the boundaries most likely to matter during real adoption:

- canonical write containment;
- external legacy migration;
- canonical authority handoff;
- mutation concurrency;
- detach/uninstall semantics;
- health-depth clarity;
- immutable distribution;
- documentation consistency.

This is not an engine failure verdict. It is a lifecycle/readiness verdict.

---

# 1. Gate summary

| QC gate | Verdict |
|---|---|
| Architecture | PASS WITH LIMITATIONS |
| Canonical ownership | PASS |
| Native source-of-truth separation | PASS |
| Read/index workspace isolation | PASS |
| Write-path workspace containment | FAIL |
| Current-source freshness | PASS |
| Historical supersession | PASS WITH LIMITATIONS |
| Install/package | PASS WITH LIMITATIONS |
| Host compatibility | PASS |
| Attach/register | PASS |
| Enable/disable | PASS |
| Detach | PASS WITH LIMITATIONS |
| Uninstall | FAIL / MISSING |
| Reconcile | FAIL / MISSING |
| Migration local legacy store | PASS WITH LIMITATIONS |
| Migration external old store | FAIL FOR ONE VALID INPUT CLASS |
| Legacy canonical authority retirement | FAIL / MISSING |
| Doctor/status | PASS WITH LIMITATIONS |
| Security/privacy claims | PASS WITH LIMITATIONS |
| Canonical mutation concurrency | FAIL FOR FINAL TARGET |
| Cross-platform | PASS |
| OS update coexistence | PASS |
| Documentation consistency | FAIL |
| Immutable release/distribution | FAIL |
| Current-target seamless adoption | FAIL |
| Final-state architecture direction | PASS |

---

# 2. Current-target definition QC

The current milestone is not merely "can Memory store and recall text".

The repository's own v0.2/readme/PR history sets a stronger present target:

- native AI-Verse OS v2;
- one source of truth;
- scoped historical memory;
- local extension attachment;
- install-order independence;
- clean OS coexistence;
- explicit old-state migration;
- safe lifecycle.

Under that target, the following are blockers rather than optional future features:

1. native writes must stay physically inside the canonical scope;
2. advertised external migration must work for valid old memories with missing provenance;
3. migration must prevent old and new stores remaining active canonical writers;
4. the user/member release path must be deterministic if described as stable.

Therefore a green internal test suite is necessary but not sufficient for "complete".

---

# 3. Architecture QC

## PASS

The architecture cleanly distinguishes:

```text
current canonical OS truth
historical Memory truth
derived recall index
```

Memory does not duplicate native profile/context/decision/knowledge ownership.

SQLite is explicitly disposable.

Standalone ownership is preserved only when no compatible host is present.

## PASS

The architecture allows Memory to remain useful outside AI-Verse OS.

## PASS

Knowledge retrieval remains outside Memory rather than turning Memory into a second universal RAG system.

## LIMITATION

The repository carries stale v0.1 architecture prose that can mislead an implementer about the current native model.

---

# 4. Ownership QC

## PASS

Native responsibility boundaries are coherent.

## PASS

Brain direction handover is handled without Memory claiming direction ownership.

## PASS

Legacy profile/scenario summaries are not automatically promoted to current native truth.

## FAIL: legacy authority retirement

Copying old atomic history into the native canonical store does not itself revoke the old store's canonical role for the old agent.

There is no enforceable authority-handoff record that says:

```text
old standalone Memory: preserved archive, no longer active writer
new native Memory: active canonical writer
```

This is the main dual-canonical-system risk.

---

# 5. Isolation and path-security QC

## PASS: read/index side

The implementation and tests are unusually strong here.

Every indexed native source is checked against:

- lexical ownership;
- resolved physical ownership;
- repository containment;
- expected source kind;
- expected workspace scope.

Invalid cached rows are rejected and purged.

## FAIL: write side

The same containment law is not enforced before destination creation/write.

Attack shape:

```text
workspaces/alpha -> symlink outside root
        or
workspaces/alpha/memory -> symlink elsewhere
        or
.../memory/atomic -> symlink elsewhere
```

`workspace_ids()` can recognize a symlinked workspace directory because directory checks follow symlinks.

`atomic_dir_for_scope()` / `atomic_path()` can then create/write through that redirected parent.

Later indexing may reject the escaped result, but the unauthorized filesystem write has already occurred.

### Required repair

Before any native canonical write:

1. validate the expected lexical owner;
2. validate each owner boundary is a real non-symlink directory or safely created under a validated real parent;
3. resolve the final parent;
4. prove it remains under the expected canonical root;
5. write atomically;
6. revalidate before effect completion.

### Required negative tests

- symlinked `operator/memory`;
- symlinked workspace root;
- symlinked workspace `memory`;
- symlinked `atomic`;
- redirected migration destination;
- redirected supersede destination.

---

# 6. Migration QC

## 6.1 Local v0.1 store

**PASS WITH LIMITATIONS**

Good behavior:

- dry run default;
- explicit apply;
- no source deletion;
- safe scope mapping;
- unresolved scopes remain unresolved;
- IDs/chronology preserved;
- profile/scenario not blindly promoted.

Limitations:

- no transaction journal;
- no source snapshot binding;
- migration completion not validated.

## 6.2 External Memory-first/OS-later path

**FAIL FOR ONE VALID INPUT CLASS**

Concrete defect:

If the old memory has no `source`, apply constructs fallback provenance relative to the new OS root.

For a true external source this relation is invalid.

The existing external test does not expose the bug because its fixtures already contain a source value.

This must be fixed before the advertised external path is considered complete.

## 6.3 Arbitrary existing-agent history

**PARTIAL**

`discover` is useful and appropriately conservative.

It is a candidate-finding tool, not a deterministic import pipeline.

The connected agent must perform supervised distillation.

That is acceptable as an architectural choice, but current UX lacks:

- reviewed source snapshot identity;
- migration manifest;
- durable record-by-record receipts;
- canonical handoff/retirement step.

## 6.4 Split-brain prevention

**FAIL**

The current process preserves old evidence, which is correct, but does not distinguish preserved bytes from active authority strongly enough.

### Required law

> After adoption, old Memory may remain as evidence but must not remain an active writable canonical route.

### Required completion proof

Migration completion should require evidence such as:

- reviewed source digest;
- no unexpected source drift;
- zero blocking invalid/unresolved records or explicit signed exceptions;
- target verification;
- representative recalls;
- authority handoff receipt;
- old writer retired/disabled/read-only or otherwise removed from active routing.

---

# 7. Lifecycle QC

## Install

**PASS**

Real local and remote paths exist.

## Attach/register

**PASS**

The local registry implementation:

- preserves sibling entries;
- preserves unknown fields;
- validates schema;
- locks mutation;
- compare-checks before replace;
- atomically replaces the file.

## Enable/disable

**PASS**

Both transitions are public and state-preserving.

## Detach

**PASS WITH LIMITATIONS**

The local registry entry is removed without deleting canonical data.

However engine/adapters remain installed intentionally.

There is no acceptance evidence proving every runtime treats those adapters as inert after registry detach.

Therefore the exact semantics should be documented as "registry detach" unless the host contract guarantees that local registry state gates all discovery.

## Uninstall

**MISSING**

No public uninstall command.

## Reinstall

**PASS WITH LIMITATIONS**

Re-running install can restore attachment and preserves canonical state.

## Reconcile

**MISSING**

No explicit Memory reconcile command.

## Rollback

**MISSING**

No public rollback strategy.

## Stale registry lock

**GAP**

The lock is exclusive but has no lease/PID/timestamp recovery policy.

A crash can leave a stale lock that blocks later lifecycle operations.

---

# 8. Health/readiness QC

## Structural health

**PASS**

## Runtime/index health

**PASS**

## Isolation health

**PASS on reads**

## Attachment readiness

**PARTIAL**

Missing/disabled attachment is warning-level in doctor.

## Migration readiness

**PARTIAL**

Legacy presence and migration marker are warning-level.

## Operational/system readiness

**UNVERIFIED by Memory doctor alone**

### QC rule

Do not interpret:

```text
Doctor: PASS
```

as:

```text
installed + attached + enabled + migrated + authorized + adopted + system-ready
```

Those are distinct states.

---

# 9. Concurrency and idempotency QC

## Registry

**PASS WITH LIMITATIONS**

Registry mutation is serialized.

## Canonical Memory

**FAIL FOR FINAL TARGET**

No equivalent Memory-wide mutation lock exists.

### Supersede failure window

```text
write new active memory
rebuild
        <crash here>
mark old superseded
rebuild
```

A crash can leave both old and new active.

### Concurrent writer risks

Potential races include:

- two remembers;
- remember versus rebuild;
- two supersedes of the same memory;
- forget versus recall/rebuild;
- migration versus normal writes.

Exact text deduplication is not a durable idempotency protocol.

### Intended repair

Use a component-owned mutation protocol with:

- lock/serialization;
- atomic file replacement;
- effect IDs/idempotency keys where requests can be retried;
- journal/receipt for multi-step effects;
- safe rebuild coordination.

---

# 10. Retrieval QC

## PASS

Long-query FTS repair is real and tested.

## PASS

Workspace scoping is enforced before ranking.

## PASS

Current canonical authority is scored above historical memory.

## LIMITATION

Candidate caps can cause scale-related recall misses:

- FTS: 200 candidates;
- lexical fallback: 2000 candidates before post-filtering.

## LIMITATION

Every ordinary write triggers a full rebuild.

This is acceptable for current small local scale but should not be treated as proven for large installations.

---

# 11. Canonical Markdown QC

## PASS

Markdown can reconstruct the index.

## CONTRADICTION / LIMITATION

The phrase "Markdown is canonical" can imply that a human edit should become visible automatically.

Current historical atomics deliberately do not live-refresh on recall.

A direct edit may therefore leave SQLite serving the older indexed text until rebuild.

One of these contracts should be explicit:

### Option A

Atomic history is canonical but engine-managed. Manual edits require `rebuild`.

### Option B

Recall also fingerprints historical atomic files and refreshes changed ones.

The current implementation behaves like Option A, but the docs do not state the limitation strongly enough.

---

# 12. Permission/safety QC

## PASS

Memory does not pretend to be a general permission engine.

## PASS

Cross-workspace access requires explicit recall opt-in.

## PARTIAL

At direct CLI level, a caller with filesystem/process access can write Memory without an external host permission token.

For the final AI-Verse shared write path:

- host/OS should check caller permission/approval;
- Memory should revalidate scope/effect at its boundary;
- Memory should return durable effect provenance/receipt.

This is a cross-component integration requirement, not a reason for Memory to absorb OS authorization policy.

---

# 13. Cross-platform QC

## PASS

Configured matrix:

- Ubuntu;
- macOS;
- Windows;
- Python 3.9;
- Python 3.12.

Installer smoke adds shell/PowerShell coverage.

## LIMITATION

Bootstrap checks that a Python command exists but does not preflight the documented >=3.9 version before executing modules that require it.

This is a UX issue, not a core architecture defect.

---

# 14. Acceptance QC

## PASS

Latest main CI is green at the exact audited head.

The test matrix runs 44 tests per unit-test job.

## PASS

Real OS update interoperability is exercised from Memory's own CI.

## MISSING acceptance scenarios

Add acceptance for:

1. symlinked native write destination;
2. external old memory with blank/missing source;
3. dry-run/apply source drift;
4. interrupted migration and retry;
5. migration with invalid numeric metadata;
6. two concurrent supersedes;
7. stale registry lock recovery;
8. detach followed by actual runtime discovery attempt;
9. immutable release install;
10. large-history recall quality and write latency before scale release.

---

# 15. Release QC

## FAIL

Remote bootstrap tracks `main`.

No current immutable GitHub release/tag was evidenced.

The repository version field alone is not an immutable distribution artifact.

### Required release gate

A stable/member-ready Memory release should:

- have an immutable tag/version;
- contain the same architecture described by current docs;
- be the source used by install instructions;
- run the same acceptance suite against that exact ref;
- publish upgrade/compatibility expectations.

---

# 16. Documentation contradiction scan

| Topic | Current implementation/tests | Conflicting prose | QC |
|---|---|---|---|
| Native registration | `.aiverse/extensions/registry.json` | Claude integration says `skills/registry.yaml` | DRIFT |
| Native AGENTS edits | Current install leaves tracked AGENTS clean | Claude integration says it adds a Memory block | DRIFT |
| Architecture generation | Native v0.2 ownership | Architecture doc still framed as v0.1 profile/scenario core | DRIFT |
| Doctor meaning | Attachment/adapters can be warnings | High-level wording can imply complete integration health | AMBIGUOUS |
| Markdown canonical | Historical direct edits need rebuild | Canonical wording does not highlight this operational rule | AMBIGUOUS |
| Migration complete | Command writes marker unconditionally | Migration guide tells user to verify first but code does not enforce | INTENT > IMPLEMENTATION |
| External migration | Advertised and mostly tested | Empty-source fallback can abort | IMPLEMENTATION GAP |
| Detach | Registry entry removed, adapters preserved | "attachment removed" is true but may be read as full runtime removal | AMBIGUOUS |

---

# 17. Definition-of-done QC against 46-lens methodology

The following condensed lens results preserve the required distinctions.

## Architecture / ownership / truth

- identity: PASS;
- canonical owner: PASS;
- derived state: PASS;
- duplicate current truth: PASS in native architecture;
- legacy dual writable authority: FAIL until handoff exists.

## Scope / isolation / privacy / paths

- recall scope: PASS;
- indexed-source containment: PASS;
- cross-workspace source isolation: PASS;
- canonical write containment: FAIL;
- secrets boundary: PASS;
- multi-user isolation: NOT CLAIMED.

## Lifecycle / discovery / readiness

- install: PASS;
- attach: PASS;
- enable/disable: PASS;
- detach: LIMITATION;
- activate/adopt: PARTIAL;
- uninstall: MISSING;
- reconcile: MISSING;
- readiness state separation: PARTIAL.

## Migration / legacy

- local atomic migration: PASS WITH LIMITATIONS;
- external migration: FAIL for missing-source case;
- arbitrary history discovery: PARTIAL;
- provenance: PASS when present, BUG in external fallback;
- source snapshot/drift: MISSING;
- authority retirement: MISSING;
- resumability: PARTIAL by duplicate-ID retry, no journal.

## Health / operations

- structural doctor: PASS;
- runtime doctor: PASS;
- attachment doctor: warning-only;
- operational readiness: UNVERIFIED;
- system readiness: EXTERNAL/UNVERIFIED.

## Safety / concurrency / failure

- incompatible host fail-closed: PASS;
- registry concurrency: PASS WITH stale-lock limitation;
- canonical write concurrency: GAP;
- supersede crash consistency: GAP;
- migration partial-failure recovery: GAP.

## Integration / cross-component

- current-source read integration: PASS;
- direction ownership: PASS;
- OS update coexistence: PASS;
- authorized owner-routed durable write pipeline: PARTIAL / system dependency;
- missing optional infrastructure: generally graceful.

## Scalability / portability / UX

- small local operation: PASS;
- large history: UNVERIFIED;
- Claude/Codex portability: PASS;
- Hermes: PARTIAL / not acceptance-tested;
- clear commands: mostly PASS;
- complete lifecycle UX: PARTIAL.

## Documentation / history / inspiration

- repair history: PASS, strong PR lineage;
- repair-to-law extraction: PASS in this audit;
- documentation consistency: FAIL;
- explicit external inspiration lineage: NONE FOUND;
- negative-space analysis: COMPLETE.

## Distribution

- CI: PASS;
- current main: PASS;
- immutable stable release: MISSING.

---

# 18. Prioritized blocker list

## P0 / current-target correctness

### M1. Native write containment

Prevent symlink/cross-root destination writes.

### M2. External migration missing-source bug

Repair provenance fallback and test it.

### M3. Migration authority handoff

Prevent two active canonical Memory systems after adoption.

## P1 / lifecycle integrity

### M4. Canonical mutation serialization/idempotency

Protect multi-step writes and concurrency.

### M5. Migration preflight/journal/drift detection

Make migration resumable and review-bound.

### M6. Detach/uninstall/reconcile semantics

Close or precisely define every discovery surface.

### M7. Health/readiness depth

Do not let a structural PASS imply operational readiness.

## P2 / release and consistency

### M8. Immutable release

Tag and test the exact member artifact.

### M9. Documentation repair

Update stale architecture and integration docs.

### M10. Scale acceptance

Prove retrieval/write behavior at larger history sizes before large deployments.

---

# 19. System-wide laws promoted by this audit

## LAW: migration authority handoff

Preserving old data is not the same as preserving old authority.

After adoption, exactly one writable canonical route may remain active.

## LAW: symmetric physical containment

If a component validates resolved physical ownership on reads, it must apply equivalent containment before canonical writes.

A later read rejection cannot undo an already escaped write.

## LAW: detach semantics must match discovery reality

A lifecycle command named detach must either:

- make the component unavailable through every host discovery route it attached; or
- be explicitly named/scoped as a narrower detachment operation.

Preserved user data is correct. Preserved accidental runtime authority is not.

These laws are propagated into the System living docs by this audit.

---

# 20. Audit completion checklist

- [x] Read canonical audit methodology first.
- [x] Audited Memory independently before cross-repo context.
- [x] Recorded exact default-branch revision.
- [x] Inventoried tracked repository.
- [x] Read runtime implementation, not only README.
- [x] Read protocols, migration, security and integration docs.
- [x] Inspected lifecycle commands.
- [x] Inspected tests and current CI.
- [x] Inspected visible PR history #1-#8.
- [x] Tested prose against deterministic implementation.
- [x] Ran contradiction scan.
- [x] Ran negative-space analysis.
- [x] Classified CURRENT / INTENDED / GAP / LAW / HISTORICAL / INSPIRATION.
- [x] Built lifecycle matrix.
- [x] Built completeness matrix.
- [x] Separated health depth from readiness.
- [x] Assessed current target versus final target.
- [x] Focused specifically on old-agent/history migration and dual-canonical risk.
- [x] Captured repair-to-law history.
- [x] Identified documentation drift.
- [x] Identified exact "works like a glove" blockers.
- [x] Propagated new system-wide laws/ideas to living System docs.
- [x] Stopped after Memory.

## Final state

**Memory documentation baseline established. Memory itself remains current-target PARTIAL until the P0/P1 gaps above are repaired and verified.**
