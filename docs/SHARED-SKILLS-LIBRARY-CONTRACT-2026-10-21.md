# Shared skills library — structure and behavior contract

Date: 2026-10-21. Step 1 design baseline complete locally.
Status: implementation specification; not a merged contract or released feature.
Program: [implementation plan](SHARED-SKILLS-LIBRARY-IMPLEMENTATION-PLAN-2026-10-21.md).

## 1. Outcome and boundaries

A member can create a reusable skill while working in workspace A and use it
from workspace B without copying its procedure or exposing A's private context.
One searchable catalog covers authorized providers. It is a view, not a new
owner of every package. A skill becoming available never grants execution,
connection access, credentials, approval or strategic authority.

Fresh installations start with the correct structure. Members bringing skills
use an explicit import workflow. Updates preserve existing skills in place.
Do not build a broad automatic legacy-folder reorganization framework.
Bogdan's existing local skills move is a separate manual operation after shared
delivery, with inventory, retained originals, verification and a move log.
Skills-repository consolidation/deletion is another subsequent effort.

## 2. Current source characterization

Evidence is repository source at the plan's starting refs, not a claim that this
new design is installed:

| Observed source | Existing behavior / design consequence |
| --- | --- |
| OS `AI-VERSE.yaml`, `AGENTS.md` | OS built-ins have canonical sources under `system/capabilities`; runtime skill directories are generated peers; workspace isolation remains mandatory |
| OS `scripts/capability-placement.mjs` | Practical this-workspace/related-work/everywhere placement already exists; default portable placement needs an additive versioned route |
| OS `scripts/capability-promotion.mjs`, resolver wrapper | Existing explicit workspace-to-local promotion preserves originals and records nonidentity compatibility; reuse rather than replace |
| OS `scripts/capability-resolver-core.mjs` at baseline | Four providers; exact bare collisions use precedence; provider roots can default independently |
| OS `scripts/ai_verse_host_adapter.py` | Host forwards its provider roots; every entrypoint needs the same installation binding |
| OS `SKILL-AUTHORING.md` | Stale guidance calls `.claude/skills` an authoring source; correct in the OS implementation step |
| Skills `installer/provider_contract_v1.py` | Managed manifests/generations are immutable; producer and verifier currently require shared visibility |
| Skills learning owner | Learning has admission/proposal rules; this work must not silently activate proposals or relabel private historical packages |
| System Safe Infrastructure slices 3.3 and 3.4 | Provider/scope is part of identity; promotion is not identity continuity; no generic reference database may be invented |

Current qualified-ID consumers include the OS resolver, CLI, Python host,
Brain learning/host calls, optional desktop bridge, and execution receipts.
Durable references must retain qualified identity and revision/digest evidence;
there is no authority to batch rewrite unrelated historical records.

## 3. Ownership and physical structure

| Material | Canonical owner and home | Writable by ordinary skill creation? |
| --- | --- | --- |
| OS operating capabilities | OS `system/capabilities/` | No |
| Published library packages | Skills-managed immutable generation under the installation's configured Skills root | No; use publisher lifecycle |
| Reusable member-created/imported skills | Skills-owned package lifecycle at configured personal-library root; member owns content | Yes, through import/create/revision operations |
| Strictly workspace-only legacy skills | Owning workspace's existing skills location | Only within that authorized workspace |
| New restricted personal-library packages | Same personal-library lifecycle, explicit `workspace:<id>` visibility | Only from the owning scope; not advertised elsewhere |
| Workspace-specific inputs/preferences | OS-owned workflow, user-owned workspace context | Yes, bounded binding operation |
| External runtime/plugin packages | Their existing publisher/runtime location | No relocation; supported read-only registration only |
| Runtime catalogs/adapters | Derived indexes and generated adapters | Generated, never independent authoring truth |

The personal root is explicitly bound to an installation/profile; a home-directory
default is only bootstrap compatibility when no binding exists. Two isolated
installations/tests must not silently share writable libraries.

Personal package layout (versioned contract `aiverse-member-skill-library-v1`):

```text
<configured-personal-root>/.aiverse/member-library/
  index.json
  packages/<stable-id>/<content-digest>/
    SKILL.md
    references/ ... scripts/ ... assets/ ...
```

The index is owner-managed identity, revision, scope and transaction metadata;
its search projection is derived. Do not treat it as disposable or reconstruct
lost provenance by guessing from directory names. A saved revision is immutable.
Legacy direct packages remain supported in place; no automatic adoption/move.

OS installation binding: `.aiverse/capability-providers.json`, schema version 1,
contains the managed Skills root and personal-library root. Distribution supplies
actual owner-established paths through the OS contract. Node, Python, Brain and
native adapters converge on it. A conflicting caller root is refused; a missing
configured source is reported without searching another installation.

External providers need an explicit supported read-only registration contract
with identity, ownership, visibility, bounded locator and integrity evidence.
Arbitrary paths and unsupported plugin caches are not automatically crawled.
Their final transport schema is an implementation-step detail, not permission.

## 4. Identity, revisions and name selection

- New personal package identity: `local:skill-<UUID hex>`. Friendly name, origin
  workspace, category and filesystem path are not identity.
- Same friendly names may coexist; importing another package does not update an
  existing one merely because names match. An update names the exact existing ID.
- Existing `os:<name>`, `aiverse-skills:<name>`, `local:<name>` and
  `workspace:<workspace-id>:<name>` remain valid. Do not rewrite legacy identity
  into a UUID without an explicit relationship and reference compatibility.
- Personal revisions use deterministic portable package content digests; changes
  append a revision. Rollback selects a retained verified revision. Managed
  packages continue using their owner's generation and digest contract.
- Exact qualified choice wins subject to scope/integrity/readiness checks.
- Protected bare OS operations continue resolving to OS as required by AGENTS;
  show same-named alternatives and allow their explicit qualified selection.
- Otherwise, an exact short-name collision returns alternatives. A saved
  scope-specific choice can resolve it; then an operator preference can apply.
  If that choice is missing/unhealthy, report it rather than replace it silently.
- Natural-language search may rank candidates, but ranking is not execution
  approval. A material identity ambiguity must be resolved before execution.
- Existing promotion receipts continue exposing the real target identity and
  `qualified_identity_preserved: false`. Never advertise an old alias as a second
  canonical package or use compatibility to bypass a scope restriction.

This intentionally changes silent bare-name precedence. It requires explicit
consumer handling and regression coverage; it is not a Provider-v1 wire-format
change. Do not silently expand Provider-v1 shared visibility semantics: scope
metadata for new learned packages needs an additive/versioned owner contract,
while existing immutable published generations remain unchanged.

## 5. Creation, import and learning

1. Determine whether the material is a repeatable skill rather than knowledge,
   current context, history or a one-off prompt.
2. Separate reusable method from workspace facts and private resources.
3. After admission, portable method defaults to shared member availability even
   if created in a workspace. Explicit workspace-only intent overrides that.
4. If portability/privacy is uncertain, keep the draft restricted and ask only a
   meaningful real-world question; do not ask the member to choose a provider.
5. Ordinary creation and learned candidates use the same placement law. Existing
   learning proposal/approval modes remain in force; no automatic activation.
6. Import preview inventories the exact package, source provenance, license,
   dependencies, requested capabilities, identity choice and target visibility.
   Admission includes secret/resource/symlink checks and compatibility diagnostics.
7. Apply binds source bytes, target identity and current library state. Drift or
   collision refuses before overwrite. Preserve the source; do not install
   dependencies, enable hooks, grant credentials or execute package code on import.
8. New identity by default; revision of an existing identity only by explicit
   selection. Exact replay is idempotent. Use a recorded transaction and atomic
   activation; interrupted writes remain inactive or require bounded recovery.

Portable shared admission explicitly confirms reusable method, no embedded
workspace data, no credentials, and no undeclared workspace dependency. Textual
checks alone do not establish that semantic claim. Untrusted skill instructions
never grant themselves authority. High-risk or unsupported imports stay inactive
with a practical explanation; preserve originals rather than deleting them.

## 6. Workspace bindings and execution

OS binding contract: `aiverse-skill-bindings-v1`.
Operator choices live at `operator/context/skill-bindings.json`; workspace choices
and inputs live at `workspaces/<id>/context/skill-bindings.json`.
Bindings reference qualified identity and optional retained revision, plus bounded
non-secret inputs. Member-specific input values never enter the shared package.

Workspace-specific inputs never inherit from another workspace or operator
bindings silently. Operator identity preferences may apply across workspaces;
private inputs may not. A binding cannot grant permissions or authorize reading
its source workspace. Connection references are resolved through current scope
permissions at execution. No credentials in bindings.

Missing required or incompatible inputs block execution with a useful next step.
Pinned unavailable revisions report unavailable; do not silently select latest.
Binding preview/apply verifies candidate identity, revision and scope and rejects
stale state. Protected OS aliases cannot be redirected by a saved preference.

## 7. Preservation, lifecycle and errors

- Preserve personal packages, originals, licenses, unknown files, workspace state,
  native hook trust and publisher ownership during install/update/rollback.
- No automatic recursive scan or promotion of all workspaces. Enumerate only
  authorized shared providers and the explicitly bound workspace.
- Reject traversal, escaping symlinks/special entries and malformed metadata.
  Bound catalog/package input sizes. Do not load every SKILL.md into model context.
- Catalog unavailable/degraded, ambiguous selection, admission-required, stale
  preview and recovery-required are distinct actionable results; no fake success.
- A successful import is not proof the skill runs successfully. Execution and
  supported-runtime readiness are separate evidence.
- No package deletion feature is required for this first layer. Future curation
  must assess real content, references, provenance and licensing before retirement.

## 8. Requirement coverage and later proof

This is design acceptance, not a claim that these cases already pass in Core.

| Requirement | Contract sections | Required implementation proof |
| --- | --- | --- |
| R01 cross-workspace reuse | 3, 5, 6 | Real owner create/import in A; select same ID/revision in B; no A-private reads |
| R02 scoped settings | 4, 6 | Different A/B inputs; unchanged shared bytes; invalid/pinned input failures |
| R03 one authorized catalog | 2, 3, 7 | Same installed roots through CLI/host/native/Brain; supported external source; missing-root diagnostic |
| R04 name collisions | 4 | Same-name alternatives; explicit choice; saved choice unavailable; protected OS behavior |
| R05 creation and learning | 5 | Portable method shared after admission; uncertain/private candidate restricted; proposal mode preserved |
| R06 existing references | 4, 7 | Legacy IDs/receipts still resolve within permissions; unchanged originals and custom content |
| R07 lifecycle/recovery | 3, 5, 7 | Immutable update, retained rollback, stale preview, interruption/retry and publisher/member separation |
| R08 privacy/permissions | 3, 5, 6, 7 | Wrong scope, secrets, resource dependencies, traversal, symlinks, binding privilege refusal |
| R09 fresh/populated installs | 1, 3, 7 | Official fresh install, explicit import, populated update preservation and owner doctors |
| R10 consistent guidance | 2, 5 | Correct authoring docs and generated peers; ordinary creation routes without asking for folders/providers |

## 9. Step 1 completion and handoff

Completed locally: source/caller characterization, ownership/storage decision,
identity and compatibility rules, portable/private placement, import boundary,
selection precedence, binding privacy, lifecycle preservation and requirement
matrix. No unresolved product-structure choice blocks the next step.

Owner implementation steps must finalize exact machine schemas/API error shapes,
external registration transport and cross-platform transaction mechanics before
publishing those APIs. These details must obey this contract; they do not reopen
the agreed outcomes. Repository review/merge and release acceptance remain future
work. Existing prototypes are unaccepted experiments and must be reconciled with
this specification before reuse.

At step 1 closeout, execution stopped at the operator's request. Subsequent
explicit step authorizations and the living plan determine the current execution
pointer. This design baseline itself grants no permission to move personal skills,
update an installation, publish a release or curate repository content.
