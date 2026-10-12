# AI-Verse Architecture Tombstones

**Status:** Canonical cross-system architecture history  
**Canonical owner:** `aiverse-filmmakers/AI-Verse-System`  
**Governance:** `docs/REPOSITORY-NETWORK-GOVERNANCE-CONTRACT.md`  
**Initial evidence:** `docs/REPOSITORY-NETWORK-REUSE-OWNERSHIP-INVENTORY-2026-10-12.md`, `docs/REPOSITORY-NETWORK-IMPLEMENTATION-ARCHITECTURE-2026-10-12.md`

## Purpose

This ledger records architecture that has been retired, replaced, or explicitly prohibited from silent resurrection.

A tombstone is not a deletion request. Historical files, commits, audits and plans may continue to describe old architecture. The tombstone tells future maintainers and agents that those historical descriptions are not permission to recreate the old structure.

Default rule:

> If an old source conflicts with an active tombstone, do not resurrect the old architecture automatically.

If resurrection appears necessary, treat it as an explicit protected architecture change and resolve it through current governance with fresh evidence.

## Entry format

Each cross-system tombstone records:

- tombstone ID;
- date;
- status: `retired`, `replaced` or `prohibited-resurrection`;
- affected architecture/surface;
- superseded refs/paths;
- replacement architecture/ref;
- reason/evidence;
- compatibility/migration impact;
- cleanup obligations, if any;
- canonical owner;
- relevant release/qualification refs;
- resurrection condition, default `none` unless explicitly approved.

Component-local API/schema/migration tombstones belong at the component owner when needed. They do not replace this cross-system ledger.

---

## ARCH-TOMB-001 - Second component compatibility fingerprint format

**Date:** 2026-10-12  
**Status:** `prohibited-resurrection`  
**Affected architecture/surface:** component release and compatibility metadata

**Superseded refs/paths:** any proposal for a parallel `compatibility-fingerprint.json`, second component fingerprint schema, or independent Distribution-owned component compatibility fingerprint.

**Replacement architecture/ref:**

- `docs/COMPONENT-RELEASE-DESCRIPTOR-CONTRACT.md`
- `contracts/component-release-descriptor.schema.json`
- later evidence-backed version/extension of that one descriptor contract only

**Reason/evidence:** Phase 1 proved the existing Component Release Descriptor is already the canonical home for component release metadata and can be extended for missing compatibility generations/ranges/migration declarations. A second format would create duplicate component compatibility truth.

**Compatibility/migration impact:** future compatibility fields must be added through the canonical descriptor contract when evidence requires them. Existing historical descriptors remain historical evidence.

**Cleanup obligations:** do not create or consume a second fingerprint as release authority.

**Canonical owner:** AI-Verse-System defines descriptor semantics; component owners publish their descriptor; Distribution consumes it.

**Relevant release/qualification refs:** current Distribution release-set/qualification evidence remains separate whole-product evidence.

**Resurrection condition:** none. A second format requires an explicit governed replacement of the current descriptor architecture and a new tombstone for the superseded design.

---

## ARCH-TOMB-002 - Second safe-update or state-preservation subsystem

**Date:** 2026-10-12  
**Status:** `prohibited-resurrection`  
**Affected architecture/surface:** install/update/migration/rollback/user-state preservation

**Superseded refs/paths:** any new repository-network updater or preservation engine created in parallel with the existing safe-update contracts and Distribution lifecycle machinery.

**Replacement architecture/ref:**

- `docs/SAFE-UPDATE-AND-STATE-PRESERVATION-CONTRACT.md`
- existing Distribution install/update/rollback, preservation, lifecycle transaction and recovery machinery
- canonical owner-controlled migrations/recovery semantics

**Reason/evidence:** Phase 1 found substantial working update and preservation machinery, including the completed Core Update Program. Rebuilding it would split ownership and risk lowering the proven state-safety floor.

**Compatibility/migration impact:** future improvements extend existing owner/Distribution mechanisms. They must not duplicate canonical owner state or invent sibling migration semantics.

**Cleanup obligations:** none for historical code/evidence. Reject new parallel safe-update control planes.

**Canonical owner:** System owns safety law; component owners own state/migration semantics; Distribution owns transition orchestration.

**Relevant release/qualification refs:** `qualification/core-update-program-u35/qualification.json`, `qualification/core-update-program-u36/release-evidence.json` in Distribution.

**Resurrection condition:** none without an explicit governed architecture replacement that preserves or strengthens every existing safety guarantee.

---

## ARCH-TOMB-003 - Separate whole-release acceptance database

**Date:** 2026-10-12  
**Status:** `prohibited-resurrection`  
**Affected architecture/surface:** whole-product release acceptance and qualification evidence

**Superseded refs/paths:** any independent database or canonical store that duplicates Distribution release sets, qualification evidence, preservation results and release receipts.

**Replacement architecture/ref:**

- Distribution `release-sets/` for exact composition
- Distribution `qualification/` for durable qualification evidence
- `docs/WHOLE-RELEASE-PRESERVATION-RESULT-CONTRACT.md`
- future `qualification/<release-id>/release-receipt.json` as compact reconstruction binding

**Reason/evidence:** current Distribution already owns exact composition and qualification. Another acceptance database would create competing release truth.

**Compatibility/migration impact:** none. Future durable receipts reference existing authorities rather than replacing them.

**Cleanup obligations:** do not promote task-specific evidence stores into independent release authorities.

**Canonical owner:** ai-verse-distribution for release composition/qualification; AI-Verse-System for shared acceptance semantics.

**Relevant release/qualification refs:** `release-sets/core-first-run-rc1-2026-10-12.json`, U35/U36 qualification evidence.

**Resurrection condition:** none unless the existing Distribution release authority itself is explicitly replaced through governed architecture change.

---

## ARCH-TOMB-004 - Hand-maintained canonical Markdown Repository State ledger

**Date:** 2026-10-12  
**Status:** `prohibited-resurrection`  
**Affected architecture/surface:** repository-network current state and human status reporting

**Superseded refs/paths:** any design where `docs/REPOSITORY-STATE-LEDGER.md` or equivalent hand-edited Markdown is the canonical machine state source.

**Replacement architecture/ref:**

```text
governance/repository-registry.json
        ↓
governance/repository-state.json
        ↓
generated docs/REPOSITORY-STATE-LEDGER.md
```

The Registry and State schemas/implementations are created in later planned slices.

**Reason/evidence:** static identity/role truth and dynamic observed state must be machine-readable and distinct. A hand-maintained Markdown ledger would drift and become a third source of truth.

**Compatibility/migration impact:** when Repository State implementation lands, human ledger content is generated/projected only.

**Cleanup obligations:** never treat manual edits to the generated ledger as canonical state changes.

**Canonical owner:** AI-Verse-System.

**Relevant release/qualification refs:** not applicable.

**Resurrection condition:** none while the System Repository Registry/State architecture remains active.

---

## ARCH-TOMB-005 - Distribution-owned sibling component acceptance truth

**Date:** 2026-10-12  
**Status:** `prohibited-resurrection`  
**Affected architecture/surface:** component acceptance and canonical ownership

**Superseded refs/paths:** any design where Distribution independently declares a sibling component revision accepted without canonical owner evidence, or where hard-coded adapter revision knowledge becomes the sole acceptance authority.

**Replacement architecture/ref:**

```text
component owner native acceptance
-> exact owner revision/evidence
-> Distribution adoption of that exact accepted revision
-> Distribution whole-product qualification
```

**Reason/evidence:** owner acceptance and composition qualification are intentionally separate validation layers. Distribution cannot manufacture sibling acceptance without becoming a shadow owner.

**Compatibility/migration impact:** existing Distribution adapter command/revision knowledge may remain bounded routing/packaging support but must not substitute for owner acceptance or owner-defined compatibility contracts.

**Cleanup obligations:** later governance gates must bind Distribution adoption to owner evidence rather than duplicating acceptance.

**Canonical owner:** component owner for component acceptance; Distribution for composition qualification.

**Relevant release/qualification refs:** future candidate evidence snapshot and owner-adoption gates.

**Resurrection condition:** none unless canonical component ownership is explicitly changed through governed architecture amendment.

---

## ARCH-TOMB-006 - Broad member payload copy followed by governance-file deletion

**Date:** 2026-10-12  
**Status:** `prohibited-resurrection`  
**Affected architecture/surface:** member install/update/rollback payload construction

**Superseded refs/paths:** designs that copy broad source trees into member installs and then try to remove maintainer/governance files by filename or cleanup rules.

**Replacement architecture/ref:** deterministic member payload inclusion using explicit package/generated-file ownership and receipt evidence.

**Reason/evidence:** broad copy-then-delete risks leaking internal governance and deleting user/local files whose names resemble internal files. Member isolation and state preservation require positive ownership/inclusion rules.

**Compatibility/migration impact:** legitimate product-facing generated files such as member `AGENTS.md`, `CLAUDE.md` or `AI-VERSE.yaml` remain allowed when they are explicitly owned product surfaces. Similar names never authorize deletion of user files.

**Cleanup obligations:** future payload work must extend deterministic inclusion and fail closed on ambiguous ownership.

**Canonical owner:** ai-verse-distribution for member payload boundary, subject to System safety law and component runtime ownership.

**Relevant release/qualification refs:** existing Distribution member/bootstrap preservation evidence; future Slice 5.2 qualification.

**Resurrection condition:** none while deterministic member payload isolation is active.

---

## ARCH-TOMB-007 - Watchdog-owned second Repository State database

**Date:** 2026-10-12  
**Status:** `prohibited-resurrection`  
**Affected architecture/surface:** drift watchdog, repository refresh and heartbeat state

**Superseded refs/paths:** any watchdog-specific database or second repository comparison engine that independently stores canonical dynamic repository state.

**Replacement architecture/ref:**

- future `scripts/refresh_repository_state.py` as the single scoped/full refresh implementation;
- future `governance/repository-state.json` as dynamic state authority;
- future `.github/workflows/repository-drift-watchdog.yml` calling that same refresh implementation;
- watchdog heartbeat recorded inside Repository State.

**Reason/evidence:** a second watchdog state engine would create conflicting dynamic truth and make silence/drift harder to diagnose.

**Compatibility/migration impact:** event-triggered or scheduled automation may evolve, but must reuse the same State/refresh semantics.

**Cleanup obligations:** watchdog implementation must not create an independent state database.

**Canonical owner:** AI-Verse-System.

**Relevant release/qualification refs:** not applicable.

**Resurrection condition:** none unless the canonical Repository State architecture is explicitly replaced and tombstoned.

---

## ARCH-TOMB-008 - Parallel promotion/ring database unsupported by Distribution reality

**Date:** 2026-10-12  
**Status:** `prohibited-resurrection`  
**Affected architecture/surface:** release promotion, channels and candidate lifecycle

**Superseded refs/paths:** a new independent promotion database or mandatory ceremonial ring taxonomy created in parallel with Distribution's real candidate, qualification, lineage/promotion and channel mechanisms.

**Replacement architecture/ref:** existing Distribution release catalog mechanics:

```text
owner accepted exact ref
-> explicit Distribution candidate
-> supported qualification evidence, including dogfood/canary/limited evidence when real
-> admitted/released release set
-> current/default channel when policy allows
```

**Reason/evidence:** Phase 1 found an existing promotion skeleton. A parallel ring system would duplicate release authority without operational need.

**Compatibility/migration impact:** new operational states may be added later only when real product/release behavior requires them. Qualification evidence may record dogfood/canary/limited testing without creating a new canonical release status.

**Cleanup obligations:** extend existing Distribution promotion/catalog surfaces rather than creating an independent promotion authority.

**Canonical owner:** AI-Verse-System defines shared release policy; ai-verse-distribution implements promotion/channels.

**Relevant release/qualification refs:** current Core candidate/promotion/lineage/catalog evidence in Distribution.

**Resurrection condition:** none unless the existing Distribution promotion architecture is explicitly replaced through governed architecture change.

---

## Adding future tombstones

Add a new cross-system tombstone whenever architecture is deliberately retired, replaced, or made unsafe to resurrect and stale historical sources could reasonably cause it to return.

Do not use tombstones to hide unresolved disagreement. If the correct architecture is still uncertain, classify the issue as drift/open decision instead.

A tombstone does not erase history. It preserves the fact that history moved on.
