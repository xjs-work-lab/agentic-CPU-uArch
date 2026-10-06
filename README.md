# Agentic CPU-uArch — V2.2 Candidate

> **CANDIDATE / NOT RESEARCH AUTHORITY**
>
> Authoritative research SSOT: `xiejinsen/agentic-CPU-uArch@960abb4ef50f050da3c6784d30826053d42e5c5d`
>
> Migration baseline: `MIG-20261006-02`

## Current branch state
The first dependency-closed **A + CG-06** migration slice has been objectized on the Pilot branch and is **QA PENDING**.

Nothing in this repository is research authority before explicit cutover.

## Start here
1. [00-project/AUTHORITY.md](00-project/AUTHORITY.md)
2. [00-project/STATUS.md](00-project/STATUS.md)
3. [00-project/MIGRATION-BASELINE.md](00-project/MIGRATION-BASELINE.md)
4. [views/graph/current.json](views/graph/current.json)

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
