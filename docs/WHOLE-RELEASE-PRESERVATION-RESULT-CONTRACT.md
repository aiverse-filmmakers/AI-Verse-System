# AI-Verse Whole-Release Preservation Result Contract

**Status:** Canonical machine-readable release acceptance contract  
**Version:** `ai-verse.release-preservation/v1`  
**Schema:** `contracts/release-preservation-result.schema.json`  
**Safety law:** `docs/SAFE-UPDATE-AND-STATE-PRESERVATION-CONTRACT.md`

## Purpose

This result records executable evidence for a specific Distribution release-set transition.

It answers a narrow question:

> Is this exact target Distribution revision proven safe to install and, when a source release set is present, proven safe to update from that exact source under the declared acceptance policy?

It is acceptance evidence only.

It is not a replacement for component canonical state, live health, permissions, migration journals, backups, or Distribution's installed manifest.

## Identity

Every result names:

- source release set, or `null` only when recording clean-install-only evidence;
- target release set;
- exact target Distribution 40-character Git revision;
- supported platforms covered by the result.

## `safe_for_update`

`safe_for_update=true` is a strong claim.

The semantic validator requires:

- non-null source release set;
- clean install = `pass`;
- real upgrade = `pass`;
- restart/recovery = `pass`;
- authority preservation = `pass`;
- every declared state-preservation domain = `pass` or explicitly `not-applicable`;
- all required destructive-transition negative tests = `pass`;
- migration status is not `blocked` or `not-tested`;
- executable evidence is present and bound to the exact target Distribution revision.

A failing, blocked, or untested required dimension makes `safe_for_update=true` invalid.

This prevents Distribution from representing a candidate as update-safe merely because clean installation succeeds.

## State preservation

The v1 result records outcomes for:

- Brain;
- Memory;
- Data;
- Skills;
- Multiple Bots;
- Token;
- OS/workspace configuration;
- user-created files.

`not-applicable` is allowed only for a domain genuinely absent from the source/target profile. The result must not use `not-applicable` to hide an included owner that was not tested.

Profile-aware release tooling is responsible for enforcing that mapping.

## Authority preservation

Authority preservation is separate from state preservation.

A passing result means the tested transition did not silently widen scope/permissions, change Brain direction ownership, re-enable disabled components, or create other forbidden authority changes covered by the acceptance harness.

## Migration evidence

Migration status is one of:

- `none`;
- `required-complete`;
- `blocked`;
- `not-tested`.

When `required-complete` is claimed, owner migration/checkpoint/recovery evidence must be attached.

The result does not contain or copy canonical owner state.

## Negative tests

The v1 result explicitly tracks:

- unsupported migration refusal;
- user-file collision protection;
- disabled-component preservation;
- permission-floor preservation;
- Brain-ownership preservation;
- partial-failure recovery;
- wrong release SHA/source-drift refusal.

A candidate with any failed or untested required destructive-transition test cannot be marked update-safe.

## Rollback

The result records software rollback acceptance separately.

A passing software rollback result does not imply canonical user-state rewind.

A blocked rollback may still be the correct safe answer when old software cannot safely consume current state.

## Evidence binding

Every evidence item is tied to the exact target Distribution revision.

Evidence may include workflow run IDs, job IDs, and URLs. The semantic validator rejects revision mismatches.

## Validation

Run:

```bash
python scripts/validate_release_preservation_result.py contracts/examples/release-preservation-result.valid.json
python -m unittest discover -s tests -p "test_*.py"
```

The System Contract Validation workflow executes all contract tests when hosted runner infrastructure is available.

## Promotion rule

This result is necessary evidence, not the promotion decision itself.

Distribution remains the canonical release owner. Promotion policy must consume this result plus the relevant release-set compatibility and channel rules.

No result with `safe_for_update=false` may be used to advertise that source-to-target transition as a normal safe update.
