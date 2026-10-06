# Agentic CPU-uArch — V2.2 Candidate

> **CANDIDATE / NOT RESEARCH AUTHORITY**
>
> Authoritative research SSOT: `xiejinsen/agentic-CPU-uArch@960abb4ef50f050da3c6784d30826053d42e5c5d`
>
> Migration baseline: `MIG-20261006-02`

## Current migration state

Six dependency-closed V2.2 slices are **CLOSED / GO** and merged into `main`:

1. A + CG-06
2. PT-A
3. C
4. CG-07
5. CG-01
6. B-residual

The active next slice is **R1 — Post-ready Continuation Timing**.

Queued after R1:
- R2 — CPU Continuation Locality
- R3 — uArch Semantic Hints / blocked lineage

Nothing in this repository is research authority before explicit cutover. V1 remains authoritative until the separate Human Gate is passed.

## Start here
1. [00-project/AUTHORITY.md](00-project/AUTHORITY.md)
2. [00-project/STATUS.md](00-project/STATUS.md)
3. [00-project/REMAINING-MIGRATION-PLAN.md](00-project/REMAINING-MIGRATION-PLAN.md)
4. [00-project/MIGRATION-BASELINE.md](00-project/MIGRATION-BASELINE.md)
5. [views/graph/current.json](views/graph/current.json)

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

Automatic cleanup is enforced by `.github/workflows/delete-merged-work-branch.yml`; it does not depend on GitHub's repository-level `delete_branch_on_merge` setting.

Repository history is preserved through commits, PRs, Migration Receipts and review records—not by retaining merged branches.
