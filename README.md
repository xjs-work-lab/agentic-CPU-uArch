# Agentic CPU-uArch — V2.2 Candidate

> **CANDIDATE / NOT RESEARCH AUTHORITY**
>
> Authoritative research SSOT: `xiejinsen/agentic-CPU-uArch@960abb4ef50a8f5b0bd357c067f08346025d`
>
> Migration baseline: `MIG-20261006-02`

This public repository is the isolated V2.2 migration target.

## Current phase

**WAVE 0 — TARGET BOOTSTRAP**

Wave 0 contains infrastructure only. No A / CG-06 research content has been migrated.

## V2.2 model

Canonical node classes:
- SOURCE
- DISCOVERY_RUN
- CLAIM
- EVIDENCE_CASE
- ACTOR
- CAPABILITY
- DIRECTION
- EXPERIMENT
- DECISION_EVENT
- ROADMAP
- STATUS

Core rules:
- premises inside one Evidence Case are AND;
- multiple Evidence Cases may provide alternative routes;
- missing nodes/edges never prove absence;
- source independence is never inferred from missing provenance;
- graph metrics do not own truth, confidence or strategy;
- generated reverse/transitive edges are navigation only.

## Start here

1. [00-project/AUTHORITY.md](00-project/AUTHORITY.md)
2. [00-project/STATUS.md](00-project/STATUS.md)
3. [00-project/MIGRATION-BASELINE.md](00-project/MIGRATION-BASELINE.md)
4. [analysis/graph/README.md](analysis/graph/README.md)
