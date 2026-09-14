# AI-Verse Component Release Descriptor Contract

**Status:** Canonical machine-readable release metadata contract  
**Version:** `ai-verse.component-release/v1`  
**Schema:** `contracts/component-release-descriptor.schema.json`  
**Safety law:** `docs/SAFE-UPDATE-AND-STATE-PRESERVATION-CONTRACT.md`

## Purpose

Every releasable AI-Verse component may publish one small descriptor that lets Distribution reason about a specific immutable component release candidate without importing the component engine or inventing its lifecycle semantics.

The descriptor is release metadata only.

It is not canonical health, readiness, authority, installation state, workspace state, or user-state truth. Live `status` and `doctor` remain with the component owner.

## Required identity

A descriptor identifies:

- `component_id`;
- `version`;
- exact 40-character Git `revision`;
- `release_status` of `candidate` or `accepted`;
- package repository/source type.

Floating `main`, branch names, tags without resolved immutable revision, and implicit `latest` are invalid descriptor revisions.

### Descriptor publication commit is not the release revision

A descriptor committed inside a component repository normally cannot describe the same commit that contains the descriptor because that would require a self-referential Git SHA.

Therefore the canonical publication pattern is:

1. finish and accept the component source/runtime revision;
2. record that exact immutable revision in the descriptor;
3. publish or update the descriptor in a later metadata-only commit or release-metadata surface.

Distribution consumes the descriptor's `revision` as the component release target. It must not substitute the commit that happens to contain the descriptor.

A metadata-only descriptor publication commit does not create a new component engine release by itself.

## Platform and runtime claims

The descriptor declares supported operating systems and required runtime families. These are release claims and must be supported by evidence.

## Lifecycle support

The descriptor declares whether the release exposes:

- install;
- setup;
- status;
- doctor;
- enable;
- disable;
- update;
- uninstall.

A `false` value is allowed when the lifecycle action is not meaningful for that owner. Distribution must not invent a missing owner lifecycle operation.

## State claims

The descriptor declares whether the component owns canonical state and must affirm the release-safety floor:

- preserve state on update;
- preserve state on normal uninstall;
- preserve unknown/user files.

A component that cannot make these preservation claims is not valid for the normal safe-update train without first changing the contract/version and explicit release policy.

## Migration claims

Migration metadata declares:

- compatibility class;
- explicitly supported source versions;
- whether explicit migration is required;
- that migration remains owner-controlled;
- checkpoint/recovery policy.

`blocked` is a valid truthful compatibility class. It means Distribution must refuse the transition.

The descriptor does not authorize Distribution to edit owner state.

## Authority-negative facts

The v1 descriptor is intentionally strict for the normal update train. It requires that applying the component release does not itself:

- grant permissions;
- change Brain direction owner;
- widen scope;
- enable a disabled component;
- expose a remote listener.

A future intentionally authority-changing product operation would require a separate explicit user action and must not be smuggled through release metadata.

## Evidence

Both CI and release-acceptance evidence are required.

Each evidence item is tied to an exact immutable revision. The semantic validator also requires every evidence revision to equal the descriptor revision.

Evidence `status` in a publishable descriptor is `pass`.

## Semantic guardrails beyond JSON shape

The repository validator additionally enforces:

- evidence revision equals descriptor revision;
- explicit-migration compatibility implies `requires_explicit_migration=true`;
- non-explicit compatibility requires `requires_explicit_migration=false`;
- `none-required` cannot claim source versions;
- `blocked` cannot be published as `accepted`;
- release metadata semantics stay `release_metadata_only=true` and `live_health_truth=false`.

## Validation

Run:

```bash
python scripts/validate_component_release_descriptor.py contracts/examples/component-release-descriptor.valid.json
python -m unittest discover -s tests -p "test_*.py"
```

The dedicated contract-validation workflow runs these tests on pull requests and `main`.

## Distribution rule

Passing descriptor validation means only that the component has well-formed, self-consistent release metadata.

It does not mean a Distribution release set is safe.

Distribution must still evaluate explicit release-set transition compatibility, migration requirements, owner evidence, whole-product preservation acceptance, and promotion policy.
