# AI-Verse Purpose Context v1 Contract

**Status:** IN PROGRESS — Slice 2.1 contract freeze  
**Parent plan:** `docs/PURPOSE-CONTEXT-IMPLEMENTATION-PLAN.md`  
**Scope:** derived/read-only Purpose Context projection only  
**Canonical owner of this contract:** `AI-Verse-System`  
**Implementation owner:** `AI-Verse-OS` after the contract is frozen

Purpose Context is a disposable, rebuildable projection over canonical owner state. Nothing in this document creates a second strategic, Data, Memory, or runtime authority.

---

## Task 1 — `schema_version` — FROZEN

The v1 serialized envelope MUST emit:

```yaml
schema_version: "1.0"
```

Contract rules:

- `schema_version` is a required UTF-8 string in `MAJOR.MINOR` decimal form.
- The initial Purpose Context contract version is exactly `"1.0"`.
- Producers MUST emit the version explicitly; consumers MUST NOT infer it from file names, repository refs, runtime version, or transport metadata.
- An unsupported major version MUST fail closed as an unsupported Purpose Context contract. It must not be interpreted as v1 by best effort.
- A minor-version increase within major `1` may add backward-compatible optional fields or enum values only when the owning contract explicitly permits them. It may not change the meaning of an existing field, make an optional field required, weaken scope/isolation rules, or change owner authority.
- Any incompatible semantic change requires a new major version.
- Repository/component release versions and `schema_version` are independent. A newer OS/Brain/Data/Memory/Gateway build may still emit Purpose Context `"1.0"`.
- The version applies to the complete Purpose Context envelope, including its provenance/freshness/reference substructures unless a later contract explicitly versions one of those substructures separately.

### Compatibility law

A consumer may accept a Purpose Context envelope only when it understands the declared major version and all required fields for that version. Unknown fields must never grant authority or silently override known owner-backed fields.

---

## Slice 2.1 freeze progress

1. [x] `schema_version`
2. [ ] supported scope kinds
3. [ ] required vs optional fields
4. [ ] provenance format
5. [ ] freshness format
6. [ ] canonical ref format
7. [ ] deterministic ordering rules
8. [ ] unknown/unavailable field behavior
9. [ ] bounded size/budget rules
10. [ ] rebuildability contract
