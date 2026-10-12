# AI-Verse Component Release Descriptor Contract

**Status:** Canonical machine-readable release metadata contract  
**Version:** `ai-verse.component-release/v1`  
**Schema:** `contracts/component-release-descriptor.schema.json`  
**Safety law:** `docs/SAFE-UPDATE-AND-STATE-PRESERVATION-CONTRACT.md`

## Purpose

Every releasable AI-Verse component may publish one small descriptor that lets Distribution reason about a specific immutable component release candidate without importing the component engine or inventing its lifecycle semantics.

The descriptor is release metadata only.

It is not canonical health, readiness, authority, installation state, workspace state, or user-state truth. Live `status` and `doctor` remain with the component owner.

There is one component release/compatibility metadata format. Compatibility classification belongs inside this descriptor. A second compatibility fingerprint, sibling acceptance record, or health-derived release format is not permitted.

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

## Migration and compatibility claims

Migration metadata declares:

- compatibility class;
- explicit `change_classification` of `non-breaking` or `breaking`;
- explicitly supported source versions;
- whether explicit migration is required;
- that migration remains owner-controlled;
- checkpoint/recovery policy.

The classifications have deliberately different jobs:

- `change_classification=non-breaking` is the owner's release-time statement that the candidate does not introduce a known breaking compatibility boundary for the declared predecessor transitions. It does not make the release safe by itself and does not bypass Distribution qualification.
- `change_classification=breaking` means the owner knows the candidate crosses a compatibility boundary. A breaking transition must name at least one predecessor in `from_versions` and may only use `compatibility=explicit-migration` or `compatibility=blocked`.
- `compatibility=explicit-migration` means the breaking transition has an owner-controlled migration path that still requires normal evidence and Distribution qualification.
- `compatibility=blocked` is a truthful fail-closed state. Distribution must refuse the transition, and a blocked descriptor cannot be published as `accepted`.

A descriptor that declares a breaking change while claiming `compatible` or `none-required` is invalid. This prevents a known breaking transition from being represented as compatible inside the canonical metadata format.

The owner is responsible for truthfully classifying its own interface/state compatibility. False classification is an owner-contract failure, not something Distribution may repair by guessing sibling semantics. Owner acceptance in the next handoff stage must validate the classification against the component's own tests/contracts.

The descriptor does not authorize Distribution to edit owner state.

### Historical descriptor evidence

Previously published immutable descriptors and Distribution qualification snapshots remain historical evidence and are not rewritten to add new fields retroactively.

New candidate/adoption work validated against the current canonical v1 contract must include `change_classification`. Historical descriptors that do not satisfy the current admission surface cannot be silently promoted as new owner acceptance evidence; owner adoption is handled explicitly by the rollout slices.

The existing optional `migration.infrastructure` extension remains part of this same descriptor and is unaffected by the compatibility classification field. Infrastructure generation/recipe metadata is not a second release or compatibility format.

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
- `change_classification` is mandatory and is exactly `non-breaking` or `breaking`;
- breaking classification requires at least one explicit predecessor version;
- breaking classification may only use `explicit-migration` or `blocked` compatibility;
- explicit-migration compatibility implies `requires_explicit_migration=true`;
- non-explicit compatibility requires `requires_explicit_migration=false`;
- `none-required` cannot claim source versions;
- `blocked` cannot be published as `accepted`;
- release metadata semantics stay `release_metadata_only=true` and `live_health_truth=false`;
- infrastructure-upgrade recipe validation remains independently fail-closed when that optional block is present.

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

Distribution must consume this canonical descriptor and owner evidence rather than create a competing component acceptance or compatibility authority.