# Audit Evidence and Finding Protocol

**Date:** 2026-09-15  
**Applies to:** Independent Whole-System Public-Beta Audit

## 1. Evidence IDs

Every important source cited in an audit packet should receive a local evidence label:

~~~text
E-<task>-001
E-<task>-002
...
~~~

Example:

~~~text
E-A1.2-004
Source: AI-Verse-Gateway/src/server.mjs
Ref: <exact SHA>
Claim supported: Gateway binds run.system_id from canonical configured system.id.
Evidence type: executable implementation
~~~

Evidence labels are local audit navigation aids. They do not replace exact GitHub refs/paths.

## 2. Evidence hierarchy

Use the canonical methodology hierarchy:

1. current executable implementation;
2. current acceptance tests/CI;
3. machine-readable contracts/schemas;
4. architecture docs;
5. README/member docs;
6. release/status docs;
7. history/PR evidence;
8. older compatibility docs;
9. inferred intent.

A lower source cannot silently override a higher one.

## 3. Claim states

Every material claim should be one of:

- VERIFIED
- CONTRADICTED
- PARTIAL
- PLAN-ONLY
- HISTORICAL
- UNVERIFIED
- NOT-APPLICABLE

## 4. Finding IDs

Stable global format:

~~~text
WSA-2026-<NNN>
~~~

Example:

~~~text
WSA-2026-017
Severity: HIGH
Confidence: PROVEN
State: OPEN
Root area: lifecycle/adoption
Affected repos: OS, Memory
Affected seam: OS -> Memory
Affected journeys: A3.2
Summary: ...
Evidence: E-A1.1-014, E-A1.4-008, E-A2.3-021
Expected law: ...
Observed behavior: ...
Impact: ...
Reproduction/trace: ...
Required closure evidence: ...
~~~

Never renumber findings after publication.

## 5. Severity

### BLOCKER
Use for:
- exploitable security boundary failure;
- data loss/corruption;
- authority/isolation breach;
- install/setup path that prevents supported public-beta use;
- release composition represented as supported but fundamentally invalid;
- systemic flaw that makes continued dogfood unsafe.

### HIGH
Major correctness, reliability, lifecycle or ownership failure with realistic user/system impact.

### MEDIUM
Meaningful defect/debt with bounded workaround or acceptable temporary limitation if explicitly acknowledged.

### LOW
Minor defect, stale docs, polish issue or narrow edge case.

### INFO
Verified limitation, observation or future recommendation.

Severity measures impact, not implementation effort.

## 6. Confidence

- PROVEN: directly reproduced or unambiguous implementation/test evidence.
- STRONG: multiple consistent evidence sources; no direct reproduction needed/available.
- POSSIBLE: credible risk requiring more evidence.
- UNVERIFIED: hypothesis only.

BLOCKER/HIGH should normally require PROVEN or STRONG confidence.

## 7. Contradiction IDs

Format:

~~~text
C-<phase/task>-<NNN>
~~~

Record:
- source A;
- source B;
- higher-authority source;
- classification;
- finding ID if material.

Contradiction classes:
- stale documentation;
- implementation defect;
- intentional compatibility;
- unresolved architecture ambiguity;
- historical-only wording.

## 8. Negative-space evidence

Negative claims are dangerous.

Prefer:
- "no implementation found under reviewed canonical roots";
- "no test found covering X";
- "repo claims no direct write; search across canonical roots found none";
- "unverified because generated/vendor region was excluded".

For architecturally sensitive forbidden relations, perform explicit searches for:
- repo/component names;
- canonical state paths;
- storage formats;
- imports/packages;
- endpoints;
- CLI invocations;
- environment variables;
- direct filesystem writes;
- direct DB access.

## 9. Audit packet minimum

Each task packet must contain:

1. task and exact refs;
2. scope and exclusions;
3. evidence inventory;
4. verified claims;
5. contradictions;
6. findings;
7. negative-space checks;
8. limitations/unverified areas;
9. verdict;
10. downstream claims/seams for later phases;
11. next task.

## 10. No repair contamination

During A0-A6:

- findings remain findings;
- do not patch product code;
- do not update product docs to remove contradictions;
- do not merge implementation fixes "while here".

If emergency containment is required, record:
- original snapshot;
- finding ID;
- reason audit paused;
- containment PR;
- exact re-audit scope required afterward.
