# WSA-2026-053 Closure - Data Natural-Key Uniqueness

**Finding:** `WSA-2026-053`  
**Severity / confidence:** HIGH / PROVEN  
**Primary owner:** `AI-Verse-Data`  
**Adopting seam:** `AI-Verse-OS` automatic structured Data routing  
**Repair wave:** R3.4  
**Closure date:** 2026-10-03  
**State:** **CLOSED**

## 1. Finding

Automatic structured truth expected one canonical Data record for one semantic natural key, but uniqueness was enforced by an OS query-before-create sequence rather than by Data at the owner mutation boundary.

At the audited baseline:

- Brain could admit different candidate IDs for the same natural key;
- OS queried Data for the natural key and created only when that query returned zero;
- Data create idempotency was candidate-specific;
- canonical storage uniqueness was by generated record ID rather than semantic natural key.

Two concurrent admitted candidates could therefore both observe zero matches and commit separate canonical rows for one logical key.

**Contradiction:** `C-A4.2-008`.

Primary historical evidence: `E-A4.2-018` through `E-A4.2-024`.

## 2. Repair identity

### Data owner

**Pre-repair Data ref:** `491e22084418f34b849c7d9e700a40973888dcf6`  
**Repair PR:** `AI-Verse-Data#18`  
**Final tested Data head:** `cc2dfd66daba27f3ce7df4949bd243bc0fffcf0b`  
**Merged Data ref:** `5cbf9908440ca7e11506991ba1dd7d3344f2b1fd`  
**Tested/merged Data tree:** `05e46bb4034cfe4b010bdb8b6f5d1c77dc71221e`

### OS adoption

**Pre-repair OS ref:** `924a21a3dc1094d0fb6cc422f55fdfc714634e4d`  
**Adoption PR:** `AI-Verse-OS#45`  
**Final tested OS head:** `9e2e592624e3d64847cf061cb044a6ac005670dd`  
**Merged OS ref:** `53c6806bf4c8205062096ab7d6247c732823df41`  
**Tested/merged OS tree:** `3710b9e747c265429b31f3d006d99b82bce683b9`

The exact tested and merged product trees are identical in both repositories.

## 3. Final owner contract

### 3.1 Natural-key admission is owned by Data

Data now exposes a trusted host-only `naturalKey` extension on `data.record.create`.

The natural-key lookup and possible record creation execute inside one Data `BEGIN IMMEDIATE` transaction. The uniqueness decision therefore occurs at the canonical owner mutation boundary rather than in a caller-side query/create window.

Ordinary Data CRUD behavior remains unchanged when `naturalKey` is absent.

### 3.2 Proposed record and natural key must agree

The natural-key field/value must exactly match the proposed record payload.

A caller cannot claim uniqueness for one semantic key while writing different record data.

### 3.3 Existing canonical state is resolved under the same transaction

Inside the owner transaction:

- zero matching rows permits one create;
- exactly one matching row is handled as existing canonical truth;
- more than one matching row fails closed as ambiguous historical state.

Data does not silently choose one row when pre-existing canonical state is already contradictory.

### 3.4 Candidate-specific idempotency can no longer create duplicate natural-key rows

The owner path preserves durable idempotency receipts while binding them to the natural-key admission result.

Once one candidate/idempotency identity creates the canonical row:

- replay of that winning durable identity resolves consistently;
- a different candidate/idempotency identity for the same natural key cannot create another row.

This removes the audited gap where different Brain candidate IDs bypassed one another through separate Data idempotency keys.

### 3.5 The privileged extension is host-bound

The `naturalKey` extension is available only through trusted host-bound actor/authorization context.

Legacy/untrusted direct host usage cannot acquire this semantic uniqueness authority merely by supplying the extra payload field.

## 4. OS automatic-routing adoption

The existing OS structured-truth sequence remains intentionally recognizable:

1. Brain admits the candidate and provides the canonical match field/value;
2. OS ensures the Data structure;
3. OS performs its advisory duplicate query;
4. one existing match retains the established exact-record update path;
5. more than one match remains ambiguous/fail-closed;
6. when the advisory query sees zero rows, OS sends Brain's admitted `{field,value}` to `data.record.create` as `naturalKey`.

The advisory query is no longer the final uniqueness authority. Data rechecks the same semantic key atomically at create time.

The existing trusted Data actor remains `{kind: "system", id: "ai-verse-gateway"}`.

## 5. Permanent concurrency regressions

Data now includes a real multi-process natural-key race test in `test/natural-key-concurrency.test.ts`.

It proves that competing host-bound create attempts with different candidate/idempotency identities but the same natural key result in exactly one canonical row.

Additional owner regressions prove:

- winning durable replay remains stable;
- a different identity for the committed key is rejected rather than duplicated;
- natural-key/payload mismatch fails closed;
- untrusted/legacy host usage cannot invoke the privileged extension.

The OS adopter includes `scripts/test-data-natural-key-routing.py`, which proves the real automatic structured-truth create payload carries Brain's admitted natural key and that its field/value exactly match the record data.

The adopter regression runs permanently on Ubuntu, macOS and Windows via `Data Natural-Key Routing`.

## 6. Data validation evidence

### Exact PR head

Final Data head: `cc2dfd66daba27f3ce7df4949bd243bc0fffcf0b`

- CI `37067680122`: **PASS**, Ubuntu/macOS/Windows Node 22/24, **6 / 6 jobs PASS**;
- canonical Data suite: **369 / 369 tests PASS**;
- Release Smoke `37067680146`: **PASS**;
- Five-Component Release Acceptance `37067680205`: **PASS**, **3 / 3 jobs PASS**.

### Merged main

Merged Data ref: `5cbf9908440ca7e11506991ba1dd7d3344f2b1fd`

- merged-main CI `37068103906`: **PASS**, **6 / 6 jobs PASS**;
- canonical Data suite: **369 / 369 tests PASS**;
- exact tested and merged Data trees: **identical**.

## 7. OS validation evidence

### Exact PR head

Final OS head: `9e2e592624e3d64847cf061cb044a6ac005670dd`

All ten exact-head workflow groups passed:

- Data Natural-Key Routing `37071822264`: **PASS**, Ubuntu/macOS/Windows **3 / 3 jobs**;
- Four Repo Acceptance `37071822273`: **PASS**;
- Repository QC `37071822356`: **PASS**;
- Direction Ownership `37071822232`: **PASS**;
- Five-Component Public Beta `37071822284`: **PASS**;
- OS Write Command Boundary `37071822321`: **PASS**;
- OS Brain Permission Contract `37071822162`: **PASS**;
- Invisible Intelligence Automation Consent `37071822172`: **PASS**;
- Invisible Intelligence Temporary Worker `37071822320`: **PASS**;
- Invisible Intelligence Permanent Bot Consent `37071822147`: **PASS**.

### Merged main

Merged OS ref: `53c6806bf4c8205062096ab7d6247c732823df41`

All seven push-to-main workflow groups passed:

- Data Natural-Key Routing `37072044292`: **PASS**, Ubuntu/macOS/Windows **3 / 3 jobs**;
- Repository QC `37072044212`: **PASS**;
- Four Repo Acceptance `37072044295`: **PASS**;
- Five-Component Public Beta `37072044301`: **PASS**;
- Direction Ownership `37072044288`: **PASS**;
- OS Write Command Boundary `37072044192`: **PASS**;
- OS Brain Permission Contract `37072044299`: **PASS**.

Exact tested and merged OS trees are **identical**.

## 8. Finding-specific recheck

### C-A4.2-008

**RESOLVED for WSA-2026-053.**

The semantic uniqueness decision is now performed by Data within the same owner transaction that may create the record.

### Competing candidate IDs

**PASS.**

Different Brain candidate/idempotency identities racing on one natural key cannot create multiple canonical rows.

### Query-then-create seam

**RESOLVED.**

OS may still query for routing/update behavior, but zero observed matches no longer grants unconditional create authority. The owner atomically rechecks the admitted natural key before insert.

### Existing ambiguous canonical state

**PASS / fail-closed.**

More than one pre-existing row for the semantic key is surfaced as ambiguity instead of silently normalized by choosing one.

### Trusted host boundary

**PASS.**

The owner-only semantic uniqueness extension requires trusted host-bound authority.

## 9. Adjacent findings remain open

This closure is limited to `WSA-2026-053`.

The next dependency-safe finding is:

`R3.5 / WSA-2026-052 - OS semantic migration source concurrency`.

The repair does not claim to close migration source-identity concurrency, Data release identity, broader schema migration, or unrelated OS/Data lifecycle findings.

The whole-system verdict remains **NO-GO**.

## 10. Closure verdict

Required WSA-2026-053 behavior is present on merged Data and OS `main`:

- natural-key admission is owner-atomic in Data;
- different candidate IDs cannot create duplicate canonical rows for one semantic key;
- winning replay and conflicting identity behavior are durable and deterministic;
- ambiguous pre-existing state fails closed;
- natural-key authority is trusted-host-only;
- the real OS automatic structured-data path passes Brain's admitted key into Data owner admission;
- Data exact-head CI is 6 / 6 PASS with 369 / 369 tests;
- Data merged-main CI is 6 / 6 PASS with 369 / 369 tests;
- OS exact-head workflow groups are 10 / 10 PASS;
- OS merged-main workflow groups are 7 / 7 PASS;
- focused OS natural-key routing is 3 / 3 PASS on exact head and merged main;
- tested and merged product trees are identical in both repositories.

**WSA-2026-053: CLOSED.**
