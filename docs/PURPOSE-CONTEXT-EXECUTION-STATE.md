# Purpose Context - Task-Level Execution State

**Purpose:** durable continuation checkpoint for `docs/PURPOSE-CONTEXT-IMPLEMENTATION-PLAN.md`  
**Execution law:** read the implementation plan, then this file, then active contract/closure docs. Execute in exact task order. For a bounded user-requested batch, persist each task before beginning the next.  
**Current admitted Core baseline:** `core-repaired-public-beta-2026-10-06`  
**Last updated:** 2026-10-08

## Current execution pointer

- **Phase:** 6 - Memory-backed history and material changes
- **Current slice:** **6.2 - Material changes**
- **Slice state:** IN PROGRESS
- **Completed slices:** 0.1, 1.1, 1.2, 1.3, 2.1, 2.2, 2.3, 3.1, 3.2, 4.1, 4.2, 4.3, 5.1, 5.2, 6.1
- **Completed Slice 6.2 tasks:** 2 of 3
- **NEXT:** **Slice 6.2 / Task 3 - allow newer material facts to alter current relevance without rewriting historical evidence**
- Execute Slice 6.2 in exact task order. Do not begin Slice 7.1 until Task 3 is complete, tested, persisted, Slice 6.2 is closed, and Phase 6 is closed.

## Slice 6.2 task checklist

1. [x] classify bounded material changes and exclude raw event spam - added a deterministic structured `purpose.material-changes.v1` classifier in OS. It accepts only the frozen materiality dimensions (`goal_status`, `priority`, `feasibility`, `blocker_state`, `strategy_validity`, `risk`, `kpi_trend`, `kpi_threshold`, `initiative_status`, `scope`, `direction_ownership`), drops candidates with no materiality before they become Purpose history, fails closed on unsupported materiality dimensions or cross-scope input, strips raw candidate payloads, caps input at 64 candidates and output at the 20 newest material changes, and orders output deterministically. The classifier is deliberately not wired into normal Purpose composition yet, so Task 1 cannot introduce unprovenanced changes. PR #50 exact head `f2b03e2742dca28778a756f96dcc80fff7f5c1d3` merged to OS main as `62642a09d9e48e1b95202a60bb2c06310224477a`; focused Direction Ownership workflow `37771740798` PASS including `Test Purpose material-change classifier`.
2. [x] require exact owner-backed source refs for every admitted material change - every material item now requires 1-8 exact owner-backed refs before admission. OS, Brain, and Memory refs use the canonical `{owner, scope, kind, id, version?}` contract and remain bound to the exact Purpose scope; Memory additionally requires `kind=memory` and an exact source version. Data uses its existing exact field-ref contract `{owner:'ai-verse-data', spaceId, entity, recordId, field}` and must match the exact workspace scope; operator Data refs fail closed until an operator Data ownership contract exists. Refs are sanitized to canonical fields, deduplicated, deterministically ordered, and extra raw owner payload/provenance internals are stripped. Missing refs, unsupported owners, cross-scope refs, malformed Memory refs, wrong Data workspaces, and over-cap refs fail closed. PR #51 exact head `eadfdcd0c10ce1ca7779fc1960de70b9767d4969` merged to OS main as `f77a572c43a56ab3516268bcbef8e6ff982ea328`; focused Direction Ownership workflow `37772386576` PASS including both `Test Purpose material-change classifier` and `Test Purpose material-change provenance`.
3. [ ] allow newer material facts to alter current relevance without rewriting historical evidence

## Slice 6.1 task checklist

1. [x] expose bounded recent history relevant to Purpose - added `memory.purpose-history.v1` on the normal Memory owner surface, backed by the existing scoped `recall` path rather than a new history store. Requests require active-scope canonical Purpose refs plus a bounded Purpose-derived query. The reader caps Purpose refs, query size, result count, age window, candidate recall, excerpt size, and serialized bytes; admits only `kind=memory` historical rows from the exact requested scope; rejects cross-scope refs; excludes current-source records; and orders results deterministically by owner timestamp then ID. The adapter is shipped by the modern installer and exported through `scripts/memory.py`. Implementation `0e8363779b00f8e15658a8588201ab3fced157b0`; installer `c7ab25996b7210475e057d2bfbc35c0d79ac85c6`; public owner exposure `15c7ff463656d4f90a333fce5b9dde8a29074759`; focused/public regression exact Memory head `9c00460c252e3ef126cc771ea1fec1b3a7f409a8`; Test workflow `37672604116` PASS across the full matrix; Migration Handoff Atomicity `37672603859` PASS.
2. [x] preserve Memory provenance - bounded history now fails closed on missing Memory source-state provenance. Every admitted item carries an exact `ai-verse-memory` canonical source ref with scope, memory ID, and owner source version plus explicit Memory `source_identity`, `source_version`, and freshness metadata. Internal storage paths are not exposed. PR #34 exact head `f4906bfe4860772fe5989269f1a83eddf2973db5` merged to Memory main as `f1327be48ba2ee0043959021365e6dbb9dcb1d3a`; Test workflow `37686373044` PASS across the complete matrix; Migration Handoff Atomicity `37686373051` PASS on Ubuntu, macOS, and Windows.
3. [x] separate historical evidence from current authority - added an OS trust boundary for `memory.purpose-history.v1` that requires exact scope, exact `ai-verse-memory` refs, source-version continuity, and `freshness=historical`. It projects only bounded `historical_evidence` records marked `authoritative_for_current_state=false`; attempted Memory-supplied mission, goal, strategy, current-state, current-value, provenance internals, and other authority-shaped fields are stripped rather than admitted. Cross-scope, wrong-owner, non-historical, version-mismatched, and over-cap inputs fail closed. PR #48 exact head `f01e363c50c8b0848dd808fc965669cffe7bb525` merged to OS main as `98b969e78fc090f934a29596a6d420c566217177`; focused Direction Ownership workflow `37687320762` PASS.
4. [x] avoid dumping raw memory into every Purpose read - ordinary `composePurposeContext()` performs zero Memory history reads, even when a Memory reader is supplied in options. Historical Memory is available only through the separate explicit `readPurposeHistoricalEvidence()` gate, which requires exact scope, 1-32 canonical Purpose refs, a non-empty Purpose-derived query capped at 4096 characters, an explicit Memory owner reader, at most 8 history items, at most 8192 requested bytes, and at most 365 days of history. Memory output immediately crosses the historical-only trust boundary; raw Memory records, provenance internals, and authority-shaped fields do not enter the Purpose projection, and owner responses exceeding the explicitly requested item limit fail closed. PR #49 exact head `60df2c813281aa42d5cf28d4da38d147397e20dd` merged to OS main as `3077e393f688399a2336c60bf6d1115d301ff2bb`; focused Direction Ownership workflow `37687905948` PASS. Exact-head OS workflows all PASS: OS Brain Permission Contract `37687979002`, Migration Source Concurrency `37687979006`, Four Repo Acceptance `37687979062`, Five-Component Public Beta `37687978993`, Direction Ownership `37687978834`, Repository QC `37687979109`, OS Write Command Boundary `37687978998`.

## Slice 6.1 closure

**COMPLETE / ACCEPTED FOR CONTINUATION** at Memory head `f1327be48ba2ee0043959021365e6dbb9dcb1d3a` and OS head `3077e393f688399a2336c60bf6d1115d301ff2bb`.

Acceptance summary:

- Memory exposes bounded, Purpose-relevant historical evidence through its normal owner surface rather than a new history store;
- canonical Memory ownership, source identity/version, freshness, scope, and exact source refs survive the read path;
- Memory evidence is explicitly historical and non-authoritative for current Brain/Data/OS state;
- ordinary Purpose reads do not load Memory history at all;
- the explicit history path is scope-bound, query-bound, ref-bound, item/byte/age-bounded, and fails closed on malformed or over-limit owner output;
- workspace isolation is preserved and raw Memory records do not cross into Purpose Context;
- all seven exact-head OS workflows passed before closure.

Durable closure record: `docs/PURPOSE-CONTEXT-SLICE-6.1-CLOSURE.md`, created at System commit `aefc5a83c09955c484f1ddac956338c4d700792e`.

## Slice 5.2 closure

**COMPLETE / ACCEPTED FOR CONTINUATION** at OS head `c8d871e306fa896a7390e493c25c88a772db4e28` with Data canonical Purpose owner remaining at `f8978f8f7a1bc94edecddc2662112233289159a3`.

Acceptance summary:

- only Purpose-relevant, exact-ref Data current state is admitted;
- stale and missing values remain diagnostics rather than trusted current truth;
- explicit Data outage or missing reader is visible and cannot reuse a previously generated Data projection;
- exact Data field refs plus workspace provenance support precise source descent; fuzzy field/record variants do not resolve;
- falsy values remain legitimate current values;
- no Data row copy or second canonical store was introduced;
- all seven exact-head OS workflows passed before closure: OS Brain Permission Contract `37670850113`, Migration Source Concurrency `37670850220`, Four Repo Acceptance `37670850224`, Five-Component Public Beta `37670850380`, Direction Ownership `37670850421`, Repository QC `37670849948`, OS Write Command Boundary `37670850335`.

Slice 5.2 task evidence:

1. relevant current-state projection: exact OS head `f853044e2b40479a55c2ce197f0b847cf63b63cf`; Direction Ownership `37665122571` PASS.
2. stale/unavailable diagnostics: exact OS head `e5a0201b379ea3660ba5a95610d9b1278742fdee`; Direction Ownership `37665571952` PASS.
3. no stale generated fallback on outage: implementation `e7ab72694aca211f8f1483b20c3d5a0c9e929d92`; focused regression/exact OS head `0b74cd66c393dcec9d3218bb04b885bedb97639d`; Direction Ownership `37670375719` PASS.
4. exact-source descent: focused test `da179e1bb953273ee1f90a96d1d6ea00aa7de76d`; CI wiring/exact closure head `c8d871e306fa896a7390e493c25c88a772db4e28`; Direction Ownership `37670850421` PASS and all seven exact-head workflows PASS.

## Slice 5.1 closure

**COMPLETE / ACCEPTED FOR CONTINUATION** at Data head `f8978f8f7a1bc94edecddc2662112233289159a3` and OS head `cbc357d7fd509b911138d82ebf558565e1995b7c`.

Acceptance summary:

- Purpose-referenced current values use a bounded exact-ref Data read surface rather than raw list/query/aggregate access;
- exact workspace scope, actor, authorization, schema version, record version, and canonical Data field refs are preserved;
- freshness evidence is the canonical Data record `updatedAt`, never query execution time;
- `value`, `stale`, and `missing` are explicit states, while `0`, `false`, and `null` remain legitimate present values;
- raw Data rows and canonical row metadata do not cross the Purpose Data surface;
- OS accepts only bounded transient scalar/status projections that preserve `ai-verse-data` ownership and exact source refs;
- OS rejects raw `data`/`record`/row-shaped inputs and ownership relabeling to OS;
- neither OS nor Brain receives or persists copied Data rows as canonical Purpose/current-state truth.

Slice 5.1 task evidence:

1. bounded current-value reads: implementation `9ec6dc83d261d8d14b37c90cf6824086d2787f0f`; module export `5a362c43112f2e52fad1a1682754e5ac018fbd50`; package-root export `798845135dd209bcf5bd830ec4fb4fd8a9d29c72`; focused test/exact Data head `9a1cb1721fc4917dd7807fbf77282a5b31859f92`; CI `37633277840` PASS across Node 22/24 on Ubuntu, macOS, and Windows.
2. scope and provenance: implementation `bf593047222762bed57be3314813e76413173ca9`; exact Data head `b5929f3a6aefda0f20d62fb595c517d5ca890185`; CI `37642975869` PASS across Node 22/24 on Ubuntu, macOS, and Windows.
3. freshness/timestamp: implementation `5698c22fdab4373576dbd29c3a19e5bd7a327439`; focused test/exact Data head `5b085cadad5ffebce272b090b88395944e4a9d14`; CI `37643681845` PASS across Node 22/24 on Ubuntu, macOS, and Windows.
4. missing/stale/falsy distinction: implementation `cb4a1a53b5f8b0dfb63f357e2c4160f769e10b58`; export `41da7c02221e7c5c4b5bce83b979c643c7162f4b`; focused tests finalized at exact Data head `5eff082872a1144c32dba072e7593b5552247645`; CI `37644581021` PASS across Node 22/24 on Ubuntu, macOS, and Windows.
5. no canonical row copy: Data no-row-copy regression exact head `f8978f8f7a1bc94edecddc2662112233289159a3`, CI `37645269881` PASS across Node 22/24 on Ubuntu, macOS, and Windows. OS transient source-owner boundary implementation `7bd2838c8c0a183ba1cd9b40e8182c2d6baf125a`, focused regression `04194e3863f605661830443cb6da23ea7c0a5dc1`, Direction Ownership CI wiring `602a0ba8e4f200bc3b7c6feb37fb5c77586ef4ac`, ownership contract/final exact OS head `cbc357d7fd509b911138d82ebf558565e1995b7c`. Exact-head OS workflows all PASS: OS Write Command Boundary `37645507286`, Direction Ownership `37645507290`, Repository QC `37645507283`, OS Brain Permission Contract `37645507313`, Migration Source Concurrency `37645507268`, Four Repo Acceptance `37645507267`, Five-Component Public Beta `37645507310`.

## Slice 4.3 closure

**COMPLETE / ACCEPTED FOR CONTINUATION** at OS head `020b43509d5f76a69baf4942d85acdc5c30706cc`.

Acceptance summary:

- exact current-work and initiative selectors traverse only explicit canonical relationships;
- deterministic explain paths can rise toward strategy, goal, mission, and problem only where owner-backed edges exist;
- missing parents, scope boundaries, and true orphans remain visible instead of being repaired by inference;
- every hop preserves exact canonical owner/source refs;
- structural cycles are rejected before authoritative traversal using deterministic SCC detection, surfaced as `structural_cycle` / `cycle_rejected`, and remain bounded by a defense-in-depth traversal cap;
- focused Direction Ownership `37632219638` PASS;
- all exact-head OS workflows passed: Direction Ownership `37632219638`, OS Brain Permission Contract `37632219959`, OS Write Command Boundary `37632219756`, Migration Source Concurrency `37632220238`, Five-Component Public Beta `37632220052`, Four Repo Acceptance `37632219702`, Repository QC `37632219971`.

Slice 4.3 task evidence:

1. explicit/canonical traversal: implementation `a531a56dff353801cf8c282b16a2c725e293666c`, CLI integration `a5375d1aff1cc9164e712c175e47025adb7ef174`, focused test `824e6d61f777f01aa044980d69c26bd8dc1e580f`, exact CI head `33fd9253bfab44163c903cab70c549495ed16da9`, Direction Ownership `37598469727` PASS.
2. path from current work/initiative toward strategic roots: implementation `5ab91e5bf708c033f969cac520c6e9e71b5cd0c7`, exact task head `eeabc6c523a135713b64bb3dcd7189ffa8ec21d0`, Direction Ownership `37630898630` PASS.
3. visible missing links/orphans: implementation `93ef9e26b20f6cb76b4dca27b53995b19499dd74`, exact task head `854dd642c3dda318546c4eae91d50916607b4748`, Direction Ownership `37631216976` PASS.
4. owner/source refs per hop: implementation `9c1bb03560283f57c35cf70b27b792e135107373`, exact task head `73b8d441311b6668f9e1e3f939456867e45f39b0`, Direction Ownership `37631718278` PASS.
5. bounded cycle behavior: structural `serves | advances | executes | supersedes` SCCs are detected deterministically; all structural edges internal to a multi-node SCC are removed from authoritative traversal and returned with exact `structural_cycle` evidence. Causal explain branches that encounter rejected cycle edges terminate visibly with `cycle_rejected`; `supersedes` remains contextual rather than a normal causal parent. Implementation `79a839831bd4b005d295628db2cd816cba61097c`; exact task/closure head `020b43509d5f76a69baf4942d85acdc5c30706cc`; Direction Ownership `37632219638` PASS.

## Slice 4.2 closure

**COMPLETE / ACCEPTED FOR CONTINUATION** at OS head `e42261e5d8cfd9d9d7dec1b58199bb8356ca6b2a`.

## Slice 4.1 closure

**COMPLETE / ACCEPTED FOR CONTINUATION** at OS head `8619104eac5632188d64279e34c5b5a8978b635d`.

## Slice 3.2 closure

**COMPLETE / CONTRACT FROZEN / ACCEPTED FOR CONTINUATION** at Brain head `69f7912eeb35f0178f6952ff0554aec8d7f2c496`. Exact-head CI `37584271057` and Skills Receipt Contract `37584271047` succeeded.

## Slice 3.1 closure

**COMPLETE / ACCEPTED FOR CONTINUATION** at Brain head `684acbf03ad44a6526a8b95cd9e136dd5cbc0f19`.

## Phase 2 closure

Slices 2.1, 2.2 and 2.3 are COMPLETE / CONTRACT FROZEN. Phase 2 is complete. Slice 2.3 explicitly froze that v1 does not add a `purpose_context` configuration block to `WORKSPACE.yaml`; caller profile requests and deterministic auto-selection remain runtime read behavior.

## Carried repair register

1. Dashboard workspace-ID contract must align with canonical lowercase alnum/hyphen max 128 before Purpose Dashboard qualification.
2. OS workspace manifest schema max length should align with runtime max 128.
3. Data aggregate freshness must never be inferred from query execution time. **RESOLVED for the Purpose current-value path in Slice 5.1:** freshness is sourced from canonical Data record `updatedAt`; aggregate/query execution time is not used as freshness evidence.
4. Final qualification must pin exact component refs.

## Resume instructions

Continue only with **Slice 6.2 / Task 3 - allow newer material facts to alter current relevance without rewriting historical evidence**. Do not begin Slice 7.1 until Task 3 is complete, tested, persisted, Slice 6.2 is closed, and Phase 6 is closed.
