# WSA-2026-031 Closure — Connections MCP Credential-Origin Binding

**Finding:** `WSA-2026-031`  
**Severity / confidence:** HIGH / PROVEN  
**Owner:** `AI-Verse-Connections`  
**Repair wave:** R1.7  
**Closure date:** 2026-10-02  
**State:** **CLOSED**

## 1. Finding

Connections already prevented one MCP bearer credential handle from being registered against two different server origins during initial `addMcp`.

The same rule was not enforced by `reauth`.

Before repair, an existing MCP connection for origin B could be reauthenticated with a handle already assigned to origin A. The next `verify` would resolve that handle and send it to origin B before connection approval could be restored.

Canonical contradiction: `C-A1.10-003`.

Required closure evidence:

1. centralize MCP credential-origin binding validation;
2. apply the same rule to add, reauth and verification;
3. make verification reject a conflicting binding before credential resolution or provider transmission;
4. prove cross-origin add rejection;
5. prove cross-origin reauth rejection;
6. preserve same-origin credential rotation.

## 2. Baseline and repair identity

**Pre-repair Connections ref:** `ac8e34cffeaaa0417aaf5011a2379af1b044bf96`  
**Open Connections PRs before repair:** 0

**Repair branch:** `repair/wsa-2026-031-credential-origin-binding`  
**Repair PR:** `AI-Verse-Connections#4`  
**Final tested head:** `bcd7c8617ec96e36dd6652c969c1dae8d015d928`  
**Merged Connections ref:** `78a9843e338f2e301e7a8c7c3153d5b43cb69ea4`  
**Tested/merged product tree:** `56f6e4e674876e1fe5b38d905800612548bbe838`

The final PR head and merged `main` commit have the same product tree.

Open Connections PRs after merge: **0**.

## 3. Final implementation contract

### 3.1 One shared credential-origin guard

A new internal helper, `assertMcpCredentialOriginBinding`, now owns the MCP credential-handle/origin invariant.

The security origin is derived from the registered MCP `config.url`, not server self-reporting.

For a non-`none` MCP credential handle, the guard rejects another MCP connection using the same handle when its registered origin differs.

The existing error remains:

`MCP_CREDENTIAL_REUSE_FORBIDDEN`

### 3.2 Registration uses the shared guard

`addMcp` no longer contains a separate one-off reuse check.

It invokes the centralized guard while holding the canonical registry mutation lock and before the new connection is persisted.

Initial cross-origin reuse therefore remains fail-closed.

### 3.3 Reauthentication now preserves origin binding

`reauth` now invokes the same centralized guard before changing `credentialHandle`.

A failed cross-origin reauth leaves the previous credential handle unchanged.

Same-origin rotation remains allowed, including rotation to a handle already used by another MCP connection on the same registered origin.

### 3.4 Verification checks before credential resolution or network use

`verify` now reads lifecycle and registry state under the Connections state lock, rechecks installation-system binding, then applies the MCP credential-origin guard before invoking the provider adapter.

Therefore a legacy, corrupted or externally introduced cross-origin handle conflict fails before:

- `CredentialManager.resolve`;
- Authorization-header construction;
- MCP discovery;
- any HTTP request to the conflicting origin.

This closes the audited disclosure path.

## 4. Permanent regression

A dedicated regression was added:

`test/connections-credential-origin.integration.test.js`

It proves:

1. origin A can register `env:A_TOKEN`;
2. origin B cannot initially register the same handle;
3. origin B can register its own independent handle;
4. origin B cannot reauth to origin A's handle;
5. failed reauth does not mutate the previous handle;
6. origin A can rotate to another handle already used on origin A;
7. a deliberately corrupted legacy registry can be given a cross-origin handle whose secret is unavailable;
8. `verify` rejects with `MCP_CREDENTIAL_REUSE_FORBIDDEN`, not `CREDENTIAL_UNAVAILABLE`;
9. the conflicting origin receives **zero** requests.

The unavailable-secret case demonstrates the binding check happens before credential resolution as required.

## 5. Validation evidence

### PR-head exact product tests

Final PR-head Actions run:

`36994384660`

On the exact final head `bcd7c8617ec96e36dd6652c969c1dae8d015d928`:

- Ubuntu / Node 20: **PASS**
- Ubuntu / Node 22: **PASS**
- macOS / Node 20: **PASS**
- macOS / Node 22: **PASS**
- Windows / Node 20: validation harness failure before tests
- Windows / Node 22: validation harness failure before tests

The successful matrix jobs ran `npm run check`. A representative exact-head Ubuntu job executed the full Node test suite:

- tests: **26**
- passed: **26**
- failed: **0**

The WSA-2026-031 regression passed.

### Post-merge acceptance

Post-merge Actions run:

`36994536871`

On merged `main` ref `78a9843e338f2e301e7a8c7c3153d5b43cb69ea4`:

- Ubuntu / Node 20: **PASS**
- Ubuntu / Node 22: **PASS**
- macOS / Node 20: **PASS**
- macOS / Node 22: **PASS**
- Windows / Node 20: validation harness failure before tests
- Windows / Node 22: validation harness failure before tests

### Windows CI limitation

Both Windows jobs fail before `npm test` because the existing package script is:

`node --check src/*.js && node --check src/providers/*.js && node --check bin/*.js && npm test`

PowerShell does not expand those globs, so Node attempts to load a literal path such as `src/*.js` and exits with `MODULE_NOT_FOUND`.

The same failure occurred on the pre-final PR attempt and again on the final exact head and post-merge `main`. It is not caused by WSA-2026-031 product logic, and no Windows product-test failure is claimed.

This closure does not modify the CI harness because that would exceed the bounded WSA-2026-031 repair scope.

## 6. Finding-specific recheck

### C-A1.10-003

**RESOLVED for WSA-2026-031.**

The initial-registration law and reauthentication law now use one shared credential-origin invariant.

### Add seam

**PASS.**

Cross-origin credential-handle reuse is rejected before persistence.

### Reauth seam

**PASS.**

Cross-origin reuse is rejected before credential mutation; same-origin rotation remains supported.

### Verify seam

**PASS.**

A conflicting stored binding is rejected before secret resolution or network transmission.

### A4.1 secret-boundary branch

**RESOLVED for WSA-2026-031.**

The supported reauth-to-foreign-origin bearer disclosure path is closed.

## 7. Adjacent findings remain open

This closure is limited to `WSA-2026-031`.

The following Connections findings remain **OPEN** and were intentionally not repaired here:

- `WSA-2026-033` — Generic API normalized path authorization;
- `WSA-2026-051` — DNS/private-network rebinding containment;
- `WSA-2026-032` — complete final-edge lifecycle and budget authority;
- later Connections findings in the ordered program.

No Generic API path normalization, DNS resolution/pinning, provider networking, rate-budget logic or final-edge lifecycle logic was changed.

## 8. Closure verdict

Required WSA-2026-031 closure behavior is present on merged Connections `main`:

- one centralized MCP credential-origin validator;
- add is guarded;
- reauth is guarded;
- verify is guarded before secret resolution/network use;
- cross-origin add and reauth fail closed;
- failed reauth preserves the old handle;
- same-origin rotation remains allowed;
- corrupted legacy conflict is rejected before any provider request;
- permanent regression coverage is present;
- Linux/macOS Node 20/22 exact-head and post-merge checks pass;
- final tested and merged product trees are identical.

The pre-existing Windows glob-expansion validation-harness defect remains outside this repair.

**WSA-2026-031: CLOSED.**
