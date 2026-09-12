# AI-Verse Apps Source Map

## Audit identity

- Repository: `aiverse-filmmakers/AI-Verse-Apps`
- Default branch: `main`
- Reviewed revision: `db5b0115bf59d6eae9149137a40e891968f3a637`
- Reviewed tree: `a4a0bfdebff7eeb9f1d3c12cb111971be9a3be90`
- Review date: 2026-09-13
- Method: `docs/AUDIT-METHODOLOGY.md`

The Apps repository was reconstructed independently before system synthesis. No sibling repository was audited.

## Repository inventory

The reviewed default branch contains exactly one tracked file:

| Path | Size | Classification |
|---|---:|---|
| `README.md` | 15,803 bytes | canonical founding architecture / research seed |

Observed repository state:

- one visible branch: `main`;
- one visible commit;
- root commit has no parent;
- no pull requests found;
- no issues found;
- no releases found;
- no required status checks on `main`;
- no implementation, generated, vendor, build, media, template, test, CI, compatibility or legacy regions exist on the default branch.

## Canonical source

### `README.md`

Blob SHA: `447522197be46aa2b22b3ac303b69d305aa89172`

The README is the only current evidence source in the component repository.

It explicitly states:

- status: founding architecture / research seed;
- implementation status: not started;
- exact app schemas are not fixed yet;
- no implementation is committed by the founding document.

Therefore architecture statements are INTENDED unless they describe repository identity or current absence.

## Architecture evidence

The README defines the intended split:

- OS: canonical operating-system structure, boundaries, policy and app registration;
- Apps: app definition, lifecycle, SDK, sandbox, versions, permissions and runtime contract;
- Dashboard: visual host/navigation;
- Data: canonical structured operational records;
- Connections: safe external-service access;
- Skills: reusable capabilities;
- Multiple Bots: builders/operators;
- Brain: intent/planning/evaluation;
- Memory: historical recall.

This is the primary evidence for the ownership map in `COMPONENT-SPEC.md`.

## Apps ownership evidence

The README says Apps should eventually own:

- manifest specification;
- package format;
- lifecycle state machine;
- create/install/update/disable/uninstall contracts;
- SDK;
- app-to-Dashboard extension protocol;
- sandbox/runtime contract;
- permission request model;
- health, compatibility and migration contracts;
- versioning and rollback;
- app registry format;
- import/export packaging;
- preview mode;
- signing/trust model if an ecosystem is created.

It explicitly says Apps must not become:

- OS;
- Memory;
- Data engine;
- Bot framework;
- Skills registry;
- token/credential vault;
- Dashboard;
- mandatory cloud hosting;
- unrestricted code execution.

## Source-of-truth evidence

The strongest rule appears in the Data relationship and invariant list:

```text
AI-Verse App
  -> AI-Verse Data API
  -> canonical structured records
```

The README states that Data owns structured truth while the App owns presentation and interaction.

It also states that structured operational data belongs to Data or another explicitly declared canonical source rather than hidden app state.

The Dashboard is described as host/presentation rather than the app source of truth.

This is the evidence for the permanent UI/app projection law.

## Lifecycle evidence

No executable lifecycle exists.

The README describes the intended flow:

```text
idea
 -> generated draft
 -> preview
 -> automated checks
 -> permission review
 -> user approval where required
 -> install
 -> operate
 -> update
 -> rollback if necessary
```

No command, API, installer or state machine implements it.

## Discovery and manifest evidence

The README contains an illustrative YAML manifest with:

- ID;
- name;
- version;
- entrypoint;
- scope;
- Data permissions;
- Connections permissions;
- capabilities;
- Dashboard surface.

It explicitly says the exact schema is not fixed.

Therefore the example is not a supported machine-readable contract.

## Security evidence

The README recommends future:

- sandboxed execution;
- explicit capabilities;
- least privilege;
- scoped Data and Connections access;
- no direct secret exposure;
- restricted host access;
- UI content security;
- controlled outbound networking where practical;
- package/dependency checks;
- review gates;
- auditability;
- version pinning;
- package trust/signing;
- explicit review of privilege-expanding updates.

Enforcement status: prose-only. No runtime code or tests exist.

## Scope/isolation evidence

The README explicitly requires separate installations of the same app in separate AI-Verse systems to remain isolated.

It says they must not implicitly share:

- data;
- provider sessions;
- permissions;
- app configuration;
- Connections.

It also says future multi-user identity should use the wider identity/access layer rather than an Apps-specific account system.

Enforcement status: prose-only.

## Local-first and portability evidence

The README says:

- local operation should be possible without mandatory hosted SaaS;
- cloud, remote, shared-team and public deployment may be adapters;
- app building should not depend on one specific coding agent/runtime.

No SDK, runtime or host adapter currently proves portability.

## Tests and CI

None exist on the reviewed default branch.

There is therefore no acceptance evidence for:

- manifest validation;
- install;
- registration;
- activation;
- scope isolation;
- permission enforcement;
- sandboxing;
- canonical read/write routing;
- update;
- rollback;
- uninstall/reinstall;
- supported operating systems.

## Release/distribution evidence

The GitHub releases collection is empty.

No package metadata, license file, release notes or immutable Apps platform artifact exists in the reviewed tree.

## Historical evidence

The only visible commit is:

`db5b0115bf59d6eae9149137a40e891968f3a637`

Message:

`docs: establish AI-Verse Apps founding architecture`

It is the root commit.

No PRs, issues or implementation repairs were found.

Therefore the audit records no HISTORICAL repair sequence.

## Inspiration evidence

The README explicitly cites:

- **Kylon**: durable apps inside an AI-native workspace;
- **Lovable**: natural-language app creation;
- **Replit**: full application generation/iteration;
- **Retool**: operational/internal tools;
- **AI-Verse's own architecture**: local-first modular ownership and source-of-truth discipline.

No third-party implementation code exists in the repository.

## Contradiction scan

### Implementation status

No contradiction. README says implementation has not started and the tree confirms it.

### Registry ownership

Potential ambiguity:

- OS owns app registration;
- Apps should own app registry format.

The audit records this as an unresolved contract split, not as permission for two canonical registries.

### App-local state

The README correctly prohibits hidden operational truth but does not fully classify preferences, configuration, drafts, logs, caches, sessions or generated assets.

### Background behavior

The manifest is expected to describe background behavior, but scheduler/execution ownership is not defined.

## Negative-space findings

Because the complete default-branch tree contains only `README.md`, the following expected platform surfaces are absent:

- package/build metadata;
- executable source;
- manifest schemas/validators;
- installer;
- registry implementation;
- SDK;
- runtime;
- sandbox;
- verifier;
- OS adapter;
- Dashboard adapter;
- CLI/API;
- tests;
- CI;
- release artifact.

The README independently confirms that this absence is intentional at the current seed stage.

## Evidence limitations

1. No executable behavior exists to inspect for security or correctness defects.
2. No CI exists to establish platform support.
3. No release exists to compare with main.
4. No PR/issue history exists for repair archaeology.
5. No machine-readable contract exists.
6. Sibling repositories were not audited.
7. Sibling integration statements are Apps-owned intent only.
8. External inspiration sites were not treated as implementation evidence.

## Evidence conclusion

AI-Verse Apps currently has a coherent founding architecture and strong source-of-truth intent.

It does not currently have a working framework, package lifecycle, OS discovery/registration, activation, sandbox, integration implementation, tests, CI or distribution.

Any claim beyond that would exceed the reviewed evidence.
