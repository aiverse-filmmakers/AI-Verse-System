# Purpose Context Slice 12.4 Independent Review - Question 12

**Status:** COMPLETE / ACCEPTED  
**Date:** 2026-10-09  
**Question:** Are all final refs exact and immutable?

## Result

**YES.** The final frozen candidate and qualified runtime evidence use exact immutable commit SHAs only.

## Evidence

1. Distribution qualification PR #26 is still open/unmerged and explicitly qualification-only. Its exact head is `578fc400ade045855bbf9bfcab9e25daf651cd42`.
2. `qualification/purpose-context/candidate.json` at that exact head has `status: blocked` and `candidate_refs_frozen: true`.
3. Every Core component revision is a full 40-character commit SHA:
   - OS `4f03849444b1d01ad81317bf0fece082d5a30e79`
   - Brain `69f7912eeb35f0178f6952ff0554aec8d7f2c496`
   - Memory `f1327be48ba2ee0043959021365e6dbb9dcb1d3a`
   - Skills `afde5c06307fba7d074de2929c2eb6c3dc6bdab8`
   - Data `f8978f8f7a1bc94edecddc2662112233289159a3`
4. The candidate records `qualification_ref_policy: exact-commit-sha-only` and `qualification_uses_moving_branch_heads: false`.
5. Data's frozen dependency lock is bound to the exact Data source revision and hashed manifest/lock/dependency-tree evidence.
6. Final runtime qualification names Gateway by exact SHA `1772b75e2add73a524715f746e87b3a6b5561bf6`.
7. The conditional Agent candidate also used exact immutable refs for Gateway, Automations, Multiple Bots and Token rather than moving branches.
8. Slice 12.3 final qualification evidence was required to correspond to one frozen candidate set; separate green runs from different component combinations were not treated as release evidence.

## Finding

All refs that define the final Purpose Core candidate and its qualified runtime composition are exact immutable commits. Mutable branches were used only as development/PR containers and are not the candidate identity.

**Review Question 12: COMPLETE / ACCEPTED.**

## Slice 12.4 disposition

All twelve independent review questions are now COMPLETE / ACCEPTED. No unresolved independent-review blocker remains.

## NEXT

Formally close Slice 12.4 and begin Slice 12.5 Task 1 only: **create a new append-only Core release entry without modifying `core-repaired-public-beta-2026-10-06`.**
