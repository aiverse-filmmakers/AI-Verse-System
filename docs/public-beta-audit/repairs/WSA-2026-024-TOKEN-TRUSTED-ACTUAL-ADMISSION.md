# WSA-2026-024 Closure — Token Trusted ACTUAL Admission

**Finding:** `WSA-2026-024`  
**Severity / confidence:** HIGH / PROVEN  
**Owner:** `ai-verse-token`  
**Repair wave:** R1.5  
**Closure date:** 2026-09-18  
**State:** **CLOSED**

## 1. Finding

Token's canonical monetary truth law required ACTUAL cost to come from a trusted provider/runtime charge source, but the generic protocol/storage path accepted any structurally valid `actual_charge`.

Before repair:

- `validateUsageEvent` accepted a syntactically valid `actual_charge`;
- `CollectorRunner` validated collector identity/version/runtime but did not prove ACTUAL source authority;
- `TokenLedger.ingestUsageEvent` persisted the normalized event directly;
- the cost engine correctly preferred an attached `actual_charge` as ACTUAL, which meant an untrusted upstream assertion could become the strongest canonical money truth.

The proven contradiction was `C-A1.8-001`, supported by `E-A1.8-004`, `E-A1.8-006`, `E-A1.8-007`, `E-A1.8-008` and `E-A1.8-010`.

Required closure law:

1. canonical ACTUAL admission requires verifiable trusted-source evidence;
2. generic collector/storage input cannot self-assert ACTUAL;
3. trusted OpenRouter, Hermes and Command Code provider/runtime paths remain functional;
4. structural copies, mutations and arbitrary collectors fail closed before canonical monetary persistence;
5. permanent negative regressions cover the authority boundary.

## 2. Baseline and repair identity

**Audited/live pre-repair Token ref:** `23b7b8ecbc9d9ef267f5e10449f785eb11107dd4`  
**Open Token PRs before repair:** 0

**Repair branch:** `repair/wsa-2026-024-trusted-actual-admission`  
**Repair PR:** `ai-verse-token#1`  
**Final reviewed/tested PR head:** `2656bc110b21cbf89ff10a866c8ddf7c45244eab`  
**Merged Token ref:** `1a85d0da0e529b659b62d3c9a3e2d40c853d67d3`  
**Final tested/merged tree:** `486cc2da61648e02179e2dbeb0b0c9d448ec6d1f`

The final tested PR tree and merged `main` tree are byte-identical.

Open Token PRs after merge: **0**.

## 3. Final implementation contract

### 3.1 Canonical ledger admission is now the authority gate

`TokenLedger.ingestUsageEvent` still performs normal protocol validation, but a non-null `actual_charge` is now rejected unless the input carries a valid internal trusted ACTUAL admission.

The new fail-closed error is:

`ACTUAL_CHARGE_UNTRUSTED`

The check runs before canonical event persistence, correlations or checkpoint advancement.

This means a caller cannot obtain ACTUAL truth merely by constructing a valid-looking `actual_charge`.

### 3.2 Trusted admission is nominal, internal and exact-event bound

A new internal module, `src/cost/trusted-actual-admission.ts`, owns the runtime proof.

The proof is:

- represented by a module-private Symbol;
- non-enumerable;
- non-serializable;
- non-configurable and non-writable;
- bound to the registered source ID;
- bound to the exact canonical JSON of the event;
- revalidated against the fixed first-release trusted ACTUAL source definitions.

The module is **not** exposed through Token's package public `exports`.

Therefore ordinary package callers, generic collectors and public storage clients cannot create authority merely from visible fields.

### 3.3 Public ACTUAL registry validation is not canonical authority

`ActualCostSourceRegistry` remains public for source semantics and normalization.

However, calling its public `attach` method alone does **not** grant ledger admission.

This preserves a useful public normalization API while separating:

- “this charge structurally matches a known source contract”
from
- “this event was produced by the trusted source implementation that is allowed to establish canonical ACTUAL truth.”

### 3.4 Concrete trusted source implementations issue admission

The existing trusted first-release paths now explicitly seal their exact normalized ACTUAL events:

- OpenRouter generation API → `openrouter-generation-api`;
- Hermes state DB → `hermes-state-db`;
- Command Code usage API → `commandcode-usage-api`.

Each seal is checked against the source definition's charge source and route scope.

No generic collector receives a blanket ACTUAL capability.

### 3.5 Collector normalization preserves proof without manufacturing it

`CollectorRunner` still canonicalizes collector emissions.

Its normalization step now preserves an existing trusted admission only when:

- the original input actually carries the private proof;
- the canonical normalized event is byte-for-byte equivalent in canonical JSON;
- the trusted source definition still matches the event.

A plain structural substitute receives no proof.

### 3.6 Clones and post-seal mutations lose authority

The admission is attached to the specific runtime object and records the exact canonical event JSON.

Therefore:

- JSON serialization/deserialization drops the proof;
- object copying does not recreate it;
- changing monetary or route fields after sealing invalidates the exact-event check.

This prevents provenance-by-shape.

### 3.7 Correlation remains downstream of admitted source truth

Existing exact cross-source correlation behavior is unchanged.

Canonical correlation can propagate an ACTUAL charge only from source observations that were already accepted by the ledger's admission boundary. The correlation engine itself does not become a new generic ACTUAL authority source.

## 4. Permanent adversarial regressions

Dedicated `test/actual-cost-authority.test.mjs` coverage proves:

1. a plain direct ledger caller cannot self-assert ACTUAL;
2. a result produced only by the public ACTUAL registry cannot enter canonical storage as ACTUAL;
3. an arbitrary CollectorRunner collector cannot emit ACTUAL or advance its checkpoint;
4. trusted OpenRouter and Command Code adapter events retain canonical ACTUAL admission;
5. JSON-cloning a trusted event removes authority;
6. post-seal event mutation invalidates authority;
7. CollectorRunner normalization preserves only an exact trusted adapter admission.

The existing Hermes integration suite additionally proves the trusted runtime-reported ACTUAL path remains operational.

## 5. CI caught stale fixture assumptions before merge

The first PR implementation was **not** merged immediately.

**Initial PR CI run:** `35329251285`  
**Result:** FAIL in `npm run ci`.

The failures were legacy tests that directly inserted synthetic `actual_charge` objects through the generic ledger API. That was precisely the path WSA-2026-024 intentionally closes.

The production authority check was **not weakened**.

Instead, only tests that intentionally require canonical ACTUAL were migrated to a repository-test-only helper that invokes the internal trusted source seal. Tests that exercise unrelated storage, dedupe, read/export and correlation behavior continue exercising those same behaviors after obtaining ACTUAL through the correct authority path.

The dedicated WSA-2026-024 negative tests remained fail-closed.

## 6. Exact acceptance evidence

### Final PR-head CI

**Run:** `35329691387`  
**Head:** `2656bc110b21cbf89ff10a866c8ddf7c45244eab`  
**Conclusion:** **SUCCESS**

All **6 / 6** matrix jobs succeeded:

- Ubuntu / Node 22;
- Ubuntu / Node 24;
- macOS / Node 22;
- macOS / Node 24;
- Windows / Node 22;
- Windows / Node 24.

Every matrix job passed:

- `npm run ci`;
- `npm pack --dry-run`;
- `node bin/ai-verse-token.mjs --help`.

Representative full-suite evidence:

- primary tests: **262 / 262 PASS**;
- release acceptance: **3 / 3 PASS**.

### Merged-main CI

**Run:** `35329970704`  
**Merged ref:** `1a85d0da0e529b659b62d3c9a3e2d40c853d67d3`  
**Conclusion:** **SUCCESS**

All **6 / 6** Ubuntu/macOS/Windows × Node 22/24 jobs succeeded.

Every matrix job again passed:

- `npm run ci`;
- `npm pack --dry-run`;
- CLI help smoke.

Representative merged-main suite:

- primary tests: **262 / 262 PASS**;
- release acceptance: **3 / 3 PASS**.

## 7. Finding-specific recheck

### C-A1.8-001

**RESOLVED for WSA-2026-024.**

A valid-looking `actual_charge` no longer constitutes ACTUAL authority by itself.

### Direct storage seam

**PASS.**

Generic direct ledger ingestion of forged ACTUAL fails before canonical persistence.

### Collector seam

**PASS.**

An arbitrary collector cannot manufacture ACTUAL, and rejected emission does not advance its checkpoint.

### Public registry seam

**PASS.**

Public source-registry attachment alone does not grant canonical monetary authority.

### Trusted provider/runtime seam

**PASS.**

OpenRouter, Hermes and Command Code trusted source implementations continue producing accepted ACTUAL observations.

### Structural-forgery adversarial recheck

**PASS.**

Plain objects, JSON clones and post-seal mutations cannot retain or manufacture admission.

### Package API boundary

**PASS.**

The trusted admission implementation is absent from package public exports.

## 8. Adjacent findings

This closure is limited to `WSA-2026-024`.

`WSA-2026-025` and all later Token findings remain **OPEN** and were not repaired, reclassified or implicitly closed here.

The next dependency-safe repair in the ordered program is `R1.6 / WSA-2026-030` owned by `AI-Verse-Connections`.

## 9. Closure verdict

All required WSA-2026-024 closure evidence is satisfied:

- owner repair merged;
- tested and merged trees match exactly;
- generic storage/collector input cannot self-assert ACTUAL;
- canonical admission requires nominal internal trusted-source evidence;
- trusted OpenRouter/Hermes/Command Code paths remain functional;
- clones and mutations fail closed;
- rejected arbitrary collector ACTUAL cannot advance canonical checkpoint state;
- permanent regressions exist;
- full six-leg PR and merged-main CI are green;
- package/API review confirms the admission module is not publicly exported;
- adjacent findings remain untouched.

**WSA-2026-024: CLOSED.**
