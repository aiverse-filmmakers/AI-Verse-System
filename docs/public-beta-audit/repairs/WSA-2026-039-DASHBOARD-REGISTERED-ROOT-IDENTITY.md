# WSA-2026-039 Closure - Dashboard Registered-Root Identity Binding

**Finding:** `WSA-2026-039`  
**Severity / confidence:** HIGH / PROVEN  
**Owner:** `AI-Verse-Dashboard`  
**Repair wave:** R1.12  
**Closure date:** 2026-10-02  
**State:** **CLOSED**

## 1. Finding

Dashboard registration canonicalized an approved OS root once and then stored only the pathname behind a stable `systemId`.

Later reads called `resolveRoot()`, which returned that stored pathname without proving it still named the filesystem object that had actually been approved.

Therefore an approved root path could be removed, renamed, replaced, or redirected to a different compatible tree while the same `systemId` continued to represent it.

Canonical contradiction: `C-A1.13-002`.

Required closure evidence:

- bind registration to durable filesystem identity beyond pathname alone;
- verify that binding before reads;
- detect root removal/replacement/redirection;
- mark the registered system unauthorized on identity drift;
- prevent ordinary revalidation from silently approving a replacement;
- require an explicit reapproval/rebind path;
- add rename, symlink/redirection and same-path replacement regressions.

## 2. Baseline and repair identity

**Pre-repair Dashboard ref:** `fe0119235df5227560b3a0ef9be8cf85d8aa1d4c`  
**Open Dashboard PRs before repair:** 0

**Repair branch:** `repair/wsa-2026-039-registered-root-identity`  
**Repair PR:** `AI-Verse-Dashboard#12`  
**Final tested PR head:** `facdbfcf58cc36ad92ea28a82410e467d348ccf0`  
**Merged Dashboard ref:** `c9e29ab660c7f56bea83dd00050a1342286734dc`  
**Tested/merged product tree:** `bd150bacf338597cfa72678496fa82d23db46257`

The exact tested PR head and merged `main` commit have the same product tree.

Open Dashboard PRs after merge: **0**.

## 3. Final implementation contract

### 3.1 Explicitly approved root identity

At registration time Dashboard now records server-side root identity consisting of:

- canonical realpath;
- filesystem device identity;
- inode/file identity;
- birth-time nanosecond value.

The identity is captured only after the candidate passes compatible-OS validation.

Approval performs a second compatibility/identity probe before committing the binding, so a root that changes during approval fails closed.

### 3.2 Root identity remains privileged

The stored root pathname, root identity and sticky drift flag remain server-side registry state.

`toPublic()` does not expose:

- `root`;
- `rootIdentity`;
- `identityDrifted`.

The browser continues to operate through `systemId`, not raw path or filesystem identity authority.

### 3.3 Every root resolution rechecks identity

`resolveRoot(systemId)` now:

1. verifies the system exists;
2. verifies it is currently authorized;
3. captures the current filesystem identity at the approved pathname;
4. compares it to the identity recorded at explicit approval time;
5. returns the root only if the identity still matches.

This check runs before workspace resolution and therefore before workspace/content reads.

### 3.4 Drift fails closed and becomes sticky

If the root:

- disappears;
- is renamed away;
- is replaced by another directory at the same pathname;
- becomes a symlink/junction to another compatible tree;
- otherwise changes filesystem identity,

Dashboard:

- marks the system `authorized: false`;
- sets `identityDrifted: true`;
- records a new validation timestamp;
- rejects the first detection with `SYSTEM_IDENTITY_DRIFT`.

Subsequent ordinary resolutions reject the system as unauthorized.

### 3.5 Ordinary revalidation cannot bless a replacement

Once `identityDrifted` is true, `revalidate()` returns incompatible state with an explicit "rebind required" reason.

It does not:

- clear the drift flag;
- restore authorization;
- adopt the current filesystem object.

This prevents a normal compatibility probe from silently changing the meaning of an already approved `systemId`.

### 3.6 Explicit rebind is the approval boundary

A new explicit `rebind(systemId, candidateRoot)` operation is the only supported path that clears sticky identity drift.

Rebind:

- validates the candidate as a compatible OS;
- captures and confirms its filesystem identity;
- preserves the existing stable `systemId`;
- re-applies duplicate/overlap protections against other registered systems;
- replaces the privileged root binding;
- resets `identityDrifted` to false;
- restores authorization.

This makes filesystem identity changes deliberate rather than implicit.

## 4. Permanent regressions

Dedicated coverage was added in:

`test/registered-root-identity.test.ts`

The suite proves:

1. registration stores durable server-side root identity;
2. public connection views do not expose root or identity metadata;
3. same-path replacement is detected;
4. the replaced system becomes unauthorized;
5. ordinary `revalidate()` cannot authorize that replacement;
6. explicit `rebind()` can deliberately approve it;
7. the stable `systemId` is preserved through explicit rebind;
8. a renamed-away approved root is detected before workspace reads;
9. symlink/junction redirection to another compatible tree is detected;
10. replacement workspace content cannot be resolved before explicit rebind;
11. after explicit rebind, the approved replacement becomes readable.

The symlink test uses a Windows junction on Windows and a directory symlink on Unix-like systems.

## 5. Validation evidence

### PR-head acceptance

Final PR-head Dashboard Actions run:

`37018365465`

On exact final head `facdbfcf58cc36ad92ea28a82410e467d348ccf0`:

- Ubuntu / Node 22: **PASS**
- macOS / Node 22: **PASS**
- Windows / Node 22: **PASS**

Representative exact-head suite:

- tests: **73**
- suites: **16**
- passed: **72**
- failed: **0**
- skipped: **1**

The WSA-2026-039 registered-root identity suite passed.

Two earlier intermediate PR-head runs exposed only test-fixture issues:

- one TypeScript assertion cast;
- one macOS logical-path versus canonical-realpath assertion.

Neither was a product-security failure. Both fixtures were corrected before the final exact head above.

### Post-merge acceptance

Post-merge Dashboard Actions run:

`37018487192`

On merged `main` ref `c9e29ab660c7f56bea83dd00050a1342286734dc`:

- Ubuntu / Node 22: **PASS**
- macOS / Node 22: **PASS**
- Windows / Node 22: **PASS**

Representative merged-main suite:

- tests: **73**
- suites: **16**
- passed: **72**
- failed: **0**
- skipped: **1**

The WSA-2026-039 suite passed after merge.

## 6. Finding-specific recheck

### C-A1.13-002

**RESOLVED for WSA-2026-039.**

A stable `systemId` is no longer authorized solely by pathname continuity.

### Same-path replacement seam

**PASS.**

Replacing the approved directory with another compatible tree at the same pathname produces identity drift and authorization loss.

### Rename seam

**PASS.**

Renaming the approved root away is detected before workspace resolution can read from it.

### Symlink/junction redirect seam

**PASS.**

Redirecting the registered pathname to another compatible filesystem tree does not transfer the existing `systemId` authority.

### Sticky unauthorized seam

**PASS.**

Once identity drift is observed, ordinary revalidation does not silently restore authority.

### Explicit rebind seam

**PASS.**

Only an explicit rebind can approve the replacement identity while preserving the stable `systemId`.

### Read-fence seam

**PASS.**

Replacement workspace content is unreachable through the old authority until the explicit rebind succeeds.

## 7. Adjacent findings remain open

This closure is limited to `WSA-2026-039`.

The following Dashboard findings remain **OPEN** and were intentionally not repaired here:

- `WSA-2026-040` - local Dashboard Gateway read authentication;
- `WSA-2026-041` - loopback browser Origin handling with explicit ports;
- `WSA-2026-042` - synthetic owner-domain projection semantics.

MC1.4 remains paused behind the whole-system audit/repair gate.

No authentication model, Origin policy, synthetic read-model semantics, Mission Control release gate or unrelated Dashboard behavior was changed.

## 8. Closure verdict

Required WSA-2026-039 closure behavior is present on merged Dashboard `main`:

- registration binds `systemId` to durable server-side filesystem identity;
- root identity is rechecked before workspace/content reads;
- missing, renamed, replaced and redirected roots fail closed;
- identity drift marks the system unauthorized;
- identity drift remains sticky across ordinary revalidation;
- only explicit `rebind()` can approve a changed filesystem identity;
- public Dashboard views do not expose privileged root identity;
- rename, replacement, symlink/junction and read-fence regressions pass on supported platforms;
- exact-head Ubuntu/macOS/Windows Node 22 CI passes;
- post-merge Ubuntu/macOS/Windows Node 22 CI passes;
- representative suites report 73 tests, 72 pass, 0 fail, 1 existing skip;
- tested and merged product trees are identical;
- open Dashboard PRs are zero.

**WSA-2026-039: CLOSED.**
