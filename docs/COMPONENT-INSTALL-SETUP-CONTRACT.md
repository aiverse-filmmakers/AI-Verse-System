# AI-Verse Component Install and Setup Contract

**Status:** Canonical intended public-beta UX contract  
**Date:** 2026-09-13  
**Applies to:** all current and future AI-Verse components

## 1. Purpose

AI-Verse may remain modular internally, but installation and first use must feel like one product.

Normal users should not need to know whether a component is Python, Node, shell, an external provider, or a local extension.

The public vocabulary is:

```text
install
setup
status
doctor
enable
disable
update
uninstall
```

Internally, `setup` may perform the component-specific subset of attachment, adoption, migration, initialization and readiness checks.

Setup must never silently transfer canonical authority or broaden permissions.

## 2. Product-level command family

The target unified CLI is:

```bash
aiverse install
aiverse setup
aiverse status
aiverse doctor

aiverse component install <component>
aiverse component setup <component>
aiverse component status <component>
aiverse component doctor <component>
aiverse component enable <component>
aiverse component disable <component>
aiverse component update <component>
aiverse component uninstall <component>
```

Optional expert commands may expose `attach`, `detach`, `migrate`, `reconcile`, `rollback`, `handover` and component-specific operations.

## 3. Required lifecycle semantics

### install

Makes the package/runtime available.

It must not by itself imply:

- attachment;
- scope initialization;
- authority transfer;
- permission grant;
- external account authorization.

### setup

Makes an installed component usable in the selected AI-Verse system/scope through the safest owner-defined sequence.

Examples:

- Brain: attach + initialize, but do not hand strategic direction to Brain unless separately requested.
- Memory: attach + initialize/rebuild derived index and detect migration needs.
- Skills: verify the immutable provider generation and dynamic discoverability; no fake attachment record.
- Data: attach runtime and explicitly initialize only selected workspaces.
- Multiple Bots: select standalone or AI-Verse OS mode and initialize canonical coordination state.
- Gateway: configure system endpoint/runtime and local auth policy without acquiring domain ownership.
- Automations: initialize scheduler/event runtime and declared trigger stores without moving Brain ownership.

### status

Fast, non-destructive state summary.

Must distinguish at least:

```text
absent
installed
setup-required
disabled
unhealthy
migration-required
ready
```

where meaningful.

### doctor

Deeper read-only verification.

Must state what depth was checked:

- structural;
- attachment/discovery;
- runtime;
- dependency;
- operational;
- system/composed.

### enable / disable

Only where the component has an enabled state.

A disabled component must have a supported route back to enabled unless disable is explicitly terminal.

### update

Updates software/runtime separately from canonical user-state migration.

An update must not silently reactivate a disabled component, broaden authority, destroy state, overwrite unknown user files, or infer compatibility from a floating branch/version alone.

Product-level update orchestration must obey `docs/SAFE-UPDATE-AND-STATE-PRESERVATION-CONTRACT.md`: exact immutable release sets, explicit source-to-target compatibility, owner-controlled migration, fail-closed unknown migration, explicit preview/apply consent, and truthful interrupted-update recovery.

### uninstall

Removes product/runtime integration while preserving canonical user-owned state by default.

Destructive purge is a different explicit action. It must never be invoked implicitly by update or normal uninstall.

Reinstall must discover/adopt preserved state according to the owner lifecycle rather than silently creating a competing canonical store.

## 4. Machine-readable contract

Every public-beta component must expose an orchestration-friendly machine-readable descriptor or command output sufficient for the Distribution layer to determine:

- component id;
- version;
- compatibility;
- package/install source;
- setup requirements;
- supported lifecycle commands;
- current state;
- health/readiness;
- required host version;
- migration requirement;
- requested scopes/capabilities;
- whether authority transfer is separate;
- whether uninstall preserves canonical state.

Every lifecycle command should support structured output, preferably `--json`, and stable exit codes.

Release-candidate metadata is standardized separately by `docs/COMPONENT-RELEASE-DESCRIPTOR-CONTRACT.md` and `contracts/component-release-descriptor.schema.json`. That descriptor is release metadata only and must not replace the component's live `status` or `doctor` truth.

## 5. First-use rule

Every repository README must contain the same top-level structure:

1. **Install**
2. **Setup**
3. **Verify**
4. **Use**
5. **Update / disable / uninstall**
6. **What setup does and does not grant**

The first-use path must be copy/pasteable and must not require the user to infer the next command from architecture docs.

## 6. One-product distribution

The existing `aiverse-filmmakers/ai-verse-distribution` repository is the intended distribution/meta-installer owner.

It should evolve from its legacy profile/package form into the canonical AI-Verse distribution layer that:

1. selects a release channel/profile;
2. resolves an exact compatible component set;
3. installs component packages;
4. invokes each component's owner-controlled setup flow;
5. initializes selected scopes;
6. runs system doctor/readiness;
7. records the installed manifest/lock without becoming a new domain source of truth;
8. supports update and rollback to known compatible component sets.

Suggested profiles:

```text
Core
  OS + Brain + Memory + Skills + Data

Agent
  Core + Multiple Bots + Gateway + Automations + Token

Full
  Agent + Connections + Dashboard + Apps when released

Custom
  explicit component selection
```

Profiles are packaging convenience, not authority bundles.

## 7. Backward compatibility

Existing native commands remain valid until deliberately deprecated.

The unified `aiverse ...` UX wraps them first.

Do not rewrite mature component engines merely to make the CLI aesthetically identical.

## 8. Acceptance

A component is public-beta install/setup ready only when a clean-machine test proves:

```text
install
-> setup
-> doctor
-> representative use
-> disable/enable where applicable
-> update
-> uninstall/reinstall with claimed state preservation
```

through the documented public path, without hidden repository surgery.
