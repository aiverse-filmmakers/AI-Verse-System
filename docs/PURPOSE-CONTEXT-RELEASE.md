# Purpose Context Admitted Core Release

**Status:** RELEASED / ADMITTED  
**Release ID:** `core-purpose-context-public-beta-2026-10-09`  
**Profile:** `core`  
**Purpose Context schema:** `1.0`  
**Admission date:** 2026-10-09

This document records the final admitted Core release for Purpose Context and its exact immutable component refs.

## Final Core release

`core-purpose-context-public-beta-2026-10-09`

Exact Core components:

- OS: `4f03849444b1d01ad81317bf0fece082d5a30e79`
- Brain: `69f7912eeb35f0178f6952ff0554aec8d7f2c496`
- Memory: `f1327be48ba2ee0043959021365e6dbb9dcb1d3a`
- Skills: `afde5c06307fba7d074de2929c2eb6c3dc6bdab8`
- Data: `f8978f8f7a1bc94edecddc2662112233289159a3`

Qualified Purpose-aware runtime, recorded separately because Gateway is not a Core component:

- Gateway: `1772b75e2add73a524715f746e87b3a6b5561bf6`

## Distribution admission record

Canonical Distribution release-set path:

`release-sets/core-purpose-context-public-beta-2026-10-09.json`

Release-set blob SHA:

`6adb651359aa1697135bf2af5a3527628b99745c`

Distribution admission merge:

`b91fc3768fe8c007fc5f19ca9e9a80e92242450d`

Final admission qualification head:

`468164945e6118f1c9bcd144a6241d740403ab1b`

The release set is marked `released` in Distribution.

## Lineage

Parent release:

`core-repaired-public-beta-2026-10-06`

Lineage policy:

`same-or-descendant`

The prior repaired Core release was not modified in place. Purpose Context was admitted as a new descendant release after qualification.

## Distribution qualification evidence recorded on the release

- Distribution CI: `37911706836`
- Clean Machine Core: `37916866642`
- member/project bootstrap: `37918170553`
- OS/Brain owner contract: `37921740519`
- workspace isolation: `37922223517`
- Data/Memory integration: `37928193308`
- context-ladder/runtime: `37929899476`
- restart/rebuild: `37930360090`
- composed Core: `37931207537`
- conditional Agent/composed: `37933117320`
- conditional Agent lineage: `37933117450`

Independent final review accepted all 12 review questions before admission.

## Data dependency lock

The admitted Data ref uses the Distribution companion lock:

`ai-verse-data/f8978f8f7a1bc94edecddc2662112233289159a3/lock.json`

Recorded lock SHA-256:

`0af6c9763fa04170b0bc6226764bb1c78db5296b5586a91d9d2851e27da98ea3`

## Authority statement

Admission of this release does not grant new permissions, transfer Brain strategy authority, or initialize all workspaces. Purpose Context remains a read-only derived projection whose claims remain owned by their canonical source systems.

## Final release identity rule

Any operational or documentation reference to the admitted Purpose Context Core must use this exact release ID and these exact component refs. Moving branch heads are not substitutes for the admitted release set.
