# Purpose Context Usage

**Status:** Core admitted  
**Core release:** `core-purpose-context-public-beta-2026-10-09`  
**Purpose Context schema:** `1.0`  
**Admitted OS contract:** `4f03849444b1d01ad81317bf0fece082d5a30e79`  
**Qualified Purpose-aware Gateway runtime:** `1772b75e2add73a524715f746e87b3a6b5561bf6`

Purpose Context is a read-only, scope-bound projection. It is not a database, cache, or new strategic owner. The admitted v1 public surface is the AI-Verse OS CLI and library API; Gateway consumes the same owner-backed capability through runtime/context-ladder integration.

## 1. CLI and library API

### CLI commands

The shipped CLI is `scripts/purpose-context.mjs` in AI-Verse OS and emits JSON.

Read operator Purpose Context:

```bash
node scripts/purpose-context.mjs read --scope operator
```

Read a workspace with automatic profile selection:

```bash
node scripts/purpose-context.mjs read --scope workspace:ai-verse --profile auto
```

Request rich workspace eligibility for a relevant KPI domain:

```bash
node scripts/purpose-context.mjs read \
  --scope workspace:ai-verse \
  --profile rich \
  --relevant-domain kpis
```

Read against a non-current OS root:

```bash
node scripts/purpose-context.mjs read \
  --root /path/to/AI-Verse \
  --scope workspace:ai-verse
```

The CLI supports:

- `read` - compose the current Purpose projection;
- `explain` - explain an exact semantic ref; `--ref` is required. Explain/trajectory semantics are documented separately in Slice 13.1 Task 5;
- `--root` or `--dir` - AI-Verse OS root, default current working directory;
- `--scope` - `operator` or `workspace:<id>`, default `operator`;
- `--profile` - `auto`, `basic`, or `rich`, default `auto`; `basic` and `rich` are workspace-only;
- `--relevant-domain <name>` - repeatable relevance input used by profile resolution;
- `--max-bytes <integer>` - serialized Purpose budget. The admitted contract accepts 4,096 through 65,536 bytes and defaults to 16,384;
- `--ref <semantic-ref>` - exact semantic ref for `explain`, for example `initiative:<id>`.

Unknown commands/options and invalid arguments fail closed rather than silently changing the projection contract.

### Library API

The admitted OS architecture declares these public library surfaces:

```js
composePurposeContext(root, scope, options)
composeProfiledPurposeContext(root, scope, options)
```

Direct base projection:

```js
import { composePurposeContext } from './scripts/purpose-context-core.mjs';

const purpose = composePurposeContext(root, 'operator', {
  maxBytes: 16384,
});
```

Profiled projection, including Data current-state composition and final budget enforcement:

```js
import { composeProfiledPurposeContext } from './scripts/purpose-context-profile.mjs';

const purpose = composeProfiledPurposeContext(root, 'workspace:ai-verse', {
  profile: 'auto',
  relevantDomains: ['kpis'],
  maxBytes: 16384,
});
```

Owner integrations may supply the public owner readers required by the active scope, including `readBrainPurposeSnapshot` when Brain owns strategic direction and `readPurposeDataCurrentState` for Data-owned current values. Those readers do not transfer ownership to Purpose Context.

### Output and failure contract

- Output is schema `1.0` JSON with scope, owner-backed semantic sections, and provenance.
- Purpose creates no durable Purpose state or Purpose cache.
- Every read is rebuildable from current owner state.
- If Brain is the declared strategic owner but its public Purpose reader is unavailable, strategic direction is reported unavailable. OS must not parse Brain private storage or reactivate frozen OS strategy.
- Data-owned measured values remain transient projections with exact owner evidence; Purpose does not become the KPI/current-state source of truth.
- Budget pruning is deterministic and reported in provenance.

This document describes the admitted v1 interfaces. It does not create a new API authority or a second Purpose storage surface.

## 2. Operator vs workspace behavior

Purpose Context supports exactly two scope forms in v1:

```text
operator
workspace:<id>
```

Both scopes use the same ownership law: the projection reads current canonical owners and never becomes an independent source of truth.

### Operator scope

`operator` is the person's/global trajectory scope. It is appropriate for questions such as what the operator is trying to achieve overall, which priorities matter now, and how current work connects to broader direction.

Operator behavior:

- the requested profile must be `auto`;
- the resolved profile is `operator_default`;
- workspace-only `basic` or `rich` profile requests are rejected rather than silently reinterpreted;
- owner-backed strategic sections may include mission/purpose, problems, goals, challenges, strategies, initiatives, current state, metrics, and material changes when those sections are available from their declared owners;
- strategic direction still follows the OS/Brain direction-owner contract;
- unavailable owner state is represented as unavailable/partial rather than filled from stale projection data.

Example:

```bash
node scripts/purpose-context.mjs read --scope operator
```

### Workspace scope

`workspace:<id>` is the trajectory of one specific project, product, client, team, business, or custom workspace.

Workspace behavior:

- accepted caller profiles are `auto`, `basic`, and `rich`;
- `auto` starts at `workspace_basic`;
- `auto` promotes to `workspace_rich` only when a rich-only domain is both relevant/requested and actually backed by owner evidence;
- `basic` keeps the compact workspace trajectory and required truth/provenance diagnostics while suppressing rich-only narratives, KPIs, and optional rich domains;
- `rich` broadens the eligible read set but does not create fields that have no owner-backed data;
- workspace name, type, age, free-text purpose, file count, perceived importance, or unused byte budget cannot force rich mode;
- v1 does not add or read a `purpose_context` configuration block in `WORKSPACE.yaml`.

Typical compact workspace flow:

```text
Purpose -> Goals -> Challenges -> Strategies -> Initiatives -> Current Work
```

Example:

```bash
node scripts/purpose-context.mjs read \
  --scope workspace:client-campaign \
  --profile auto
```

### Isolation and cross-scope behavior

Workspace isolation is fail-closed:

- reading `workspace:A` does not scan or inherit Purpose state from `workspace:B`;
- optional owner-backed data is retained only when exact source evidence belongs to the requested scope;
- malformed scope or ownership records fail closed;
- explicit cross-scope trajectory relationships may remain explicit provenance-bearing refs, but they do not authorize implicit foreign-scope resolution, enumeration, or ingestion;
- deleting or rebuilding the projection cannot alter any workspace's canonical state.

The practical rule is simple: use `operator` for global personal direction and `workspace:<id>` for one bounded workspace. Purpose Context never blends scopes merely because their content appears related.

## 3. Optional rich workspace fields

A rich workspace is still the same Purpose Context schema and ownership model. Rich mode only makes additional owner-backed context eligible for projection when it is useful. It does not require a company-style template and does not populate empty fields for small projects.

### Rich-profile strategic/context sections

Compared with `workspace_basic`, rich projection may retain these existing contextual sections when owner-backed:

- `narratives`;
- `kpis`.

`workspace_basic` suppresses these sections to keep small workspaces compact.

### Optional owner-backed rich domains

The admitted OS contract defines exactly these optional rich domain names:

- `risks` - relevant risks with exact owner/source evidence;
- `team_resources` - relevant team or resource context;
- `customers` - relevant customer context;
- `infrastructure` - relevant infrastructure context;
- `budget_cost` - relevant budget or cost context.

Each item must carry exact evidence for the requested scope. If a domain is absent, malformed, foreign-scope, or unsupported by owner evidence, Purpose omits it rather than fabricating an empty or inferred corporate field.

### Current state and material changes

`current_state` and `recent_material_changes` can also be relevance signals for automatic rich resolution when useful owner-backed content exists. They are not a license to invent a separate rich-state database. Current operational truth remains with its declared owner, and recent material changes remain derived from owner-backed evidence.

Unlike `narratives`, `kpis`, and the five optional domains above, basic-profile filtering does not automatically delete valid required current-state/material-change context needed for truth/freshness diagnostics.

### Initiative/project operational status

Purpose v1 does not create a separate `initiative_operational_status` or `project_operational_status` store. When Brain owns strategic direction, the canonical initiative object already owns its lifecycle status. The Brain Purpose snapshot projects that same owner-backed initiative/status object under `initiatives`.

If a distinct project/initiative operational owner is introduced later, it must enter through a new explicit owner contract. Purpose must not infer such status from generic Data rows or free-text workspace metadata.

### Requesting rich context

Explicit rich eligibility:

```bash
node scripts/purpose-context.mjs read \
  --scope workspace:ai-verse \
  --profile rich \
  --relevant-domain kpis \
  --relevant-domain risks
```

Automatic enrichment:

```bash
node scripts/purpose-context.mjs read \
  --scope workspace:ai-verse \
  --profile auto \
  --relevant-domain risks
```

With `auto`, a requested/relevant rich domain only promotes the workspace when matching owner-backed content actually exists. Merely naming `risks`, `customers`, or another rich domain does not fabricate content.

### What rich mode does not do

Rich mode does not:

- change the workspace type or manifest;
- grant new permissions or strategic authority;
- copy Data rows into a Purpose database;
- turn Memory history into current truth;
- infer cross-workspace data;
- require every workspace to have KPIs, risks, customers, infrastructure, budget, or team structure;
- allow arbitrary `WORKSPACE.yaml` metadata to force enrichment.

The design goal is progressive disclosure: simple workspaces stay simple, while larger workspaces can expose additional verified context without changing the core engine or owner contracts.
