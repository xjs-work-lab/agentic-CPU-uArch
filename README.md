# Agentic CPU-uArch — V2.2 Candidate

> **CANDIDATE / NOT RESEARCH AUTHORITY**
>
> Authoritative research SSOT: `xiejinsen/agentic-CPU-uArch@960abb4ef50f050da3c6784d30826053d42e5c5d`
>
> Migration baseline: `MIG-20261006-02`

## Migration state

All nine planned V2.2 migration slices are **CLOSED / GO**.

Current graph:
- **226 canonical nodes**
- **381 canonical semantic edges**
- **381 generated reverse edges**

## Current phase

**FINAL PRE-CUTOVER REVIEW**

The semantic/portfolio parity audit is complete and currently supports:
**GO_TO_HUMAN_GATE**, subject to final PR graph QA.

This does **not** authorize cutover.

## Start here
1. [00-project/AUTHORITY.md](00-project/AUTHORITY.md)
2. [00-project/STATUS.md](00-project/STATUS.md)
3. [00-project/FINAL-PRE-CUTOVER-REVIEW.md](00-project/FINAL-PRE-CUTOVER-REVIEW.md)
4. [00-project/HUMAN-GATE-PACKAGE.md](00-project/HUMAN-GATE-PACKAGE.md)
5. [00-project/MIGRATION-BASELINE.md](00-project/MIGRATION-BASELINE.md)
6. [views/graph/current.json](views/graph/current.json)
7. [09-roadmap/current.md](09-roadmap/current.md)

## Portfolio invariant
- one differentiated Primary Bet: A
- second Primary Bet intentionally unfilled
- no uArch Primary Bet
- competitive-gap actions remain a separate axis

## Authority rule

Migration completion is not authority cutover.

Only explicit Human Gate approval may authorize a separate cutover transaction.

## Branch policy

`main` is the only long-lived branch.

Temporary work branches are deleted after reviewed merge.
