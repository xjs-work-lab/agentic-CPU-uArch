# Agentic CPU-uArch — V2.2 Candidate

> **CANDIDATE / NOT RESEARCH AUTHORITY**
>
> Authoritative research SSOT: `xiejinsen/agentic-CPU-uArch@960abb4ef50f050da3c6784d30826053d42e5c5d`
>
> Migration baseline: `MIG-20261006-02`

## Migration state

All nine planned V2.2 migration slices are **CLOSED / GO** and merged into `main`:

1. A + CG-06
2. PT-A
3. C
4. CG-07
5. CG-01
6. B-residual
7. R1
8. R2
9. R3

Current cumulative graph:
- **226 canonical nodes**
- **381 canonical semantic edges**
- **381 generated reverse edges**
- **0 hard graph errors**

## Current phase

**FINAL PRE-CUTOVER REVIEW**

Migration completion does not make this repository authoritative.

Before cutover:
- full-graph QA;
- cross-slice semantic review;
- frozen-V1 parity review;
- roadmap/view reconciliation;
- unresolved-ambiguity audit;
- separate Human Gate.

## Start here
1. [00-project/AUTHORITY.md](00-project/AUTHORITY.md)
2. [00-project/STATUS.md](00-project/STATUS.md)
3. [00-project/REMAINING-MIGRATION-PLAN.md](00-project/REMAINING-MIGRATION-PLAN.md)
4. [00-project/MIGRATION-BASELINE.md](00-project/MIGRATION-BASELINE.md)
5. [views/graph/current.json](views/graph/current.json)
6. [09-roadmap/current.md](09-roadmap/current.md)

## Reasoning model
```text
SOURCE / DISCOVERY_RUN / upstream CLAIM / EXPERIMENT
                         ↓
                    EVIDENCE_CASE
                         ↓
                       CLAIM
                   ↙           ↘
            CAPABILITY       DIRECTION
                ↑               ↓
              ACTOR         EXPERIMENT
                                ↓
                         DECISION_EVENT
```

Premises within one Evidence Case are conjunctive; alternative Evidence Cases remain separate routes.

## Branch policy

`main` is the only long-lived branch.

Migration/feature branches are temporary transaction workspaces:

PR → CI/review → merge → automatic branch deletion.

Repository history is preserved through commits, PRs, Migration Receipts and review records—not by retaining merged branches.
