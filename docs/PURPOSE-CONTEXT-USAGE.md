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
