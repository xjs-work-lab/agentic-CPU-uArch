# Research Authority Status

Updated: 2026-10-06

```yaml
migration_phase: CUTOVER_COMPLETE
research_authority: V2_2
authority_repository: xjs-work-lab/agentic-CPU-uArch
historical_source_authority: V1_FROZEN
historical_source_repository: xiejinsen/agentic-CPU-uArch
historical_source_commit: 960abb4ef50f050da3c6784d30826053d42e5c5d
migration_id: MIG-20261006-02
human_gate: APPROVED
human_gate_date: 2026-10-06
cutover_state: COMPLETE
cutover_pr: 11
cutover_merge_commit: 68698fd4b4bc6767c480d200fd3483bdc32eaf1b
post_cutover_verification: PASS
cutover_branch_cleanup: PASS
research_content_migrated: true
completed_slices:
  - A + CG-06
  - PT-A
  - C
  - CG-07
  - CG-01
  - B-residual
  - R1
  - R2
  - R3
```

## Authority

**V2.2 is the active Research SSOT.**

Repository:
`xjs-work-lab/agentic-CPU-uArch`

Frozen historical source:
`xiejinsen/agentic-CPU-uArch@960abb4ef50f050da3c6784d30826053d42e5c5d`

## Human Gate

Explicit approval:
**APPROVED — 2026-10-06**

## Cutover transaction

- PR: `#11`
- merge commit: `68698fd4b4bc6767c480d200fd3483bdc32eaf1b`
- final QA run: `37479121798`
- final QA job: `112322303675`
- branch cleanup run: `37479223624`
- post-cutover verification: **PASS**

## Current graph
- 226 canonical nodes
- 381 canonical semantic edges
- 381 generated reverse edges
- hard graph errors at final cutover QA: 0

## Portfolio invariant
- A — only differentiated Primary Bet
- PT-A — Platform Track
- C — Strategic Enabler / second-Bet watch
- CG-06 — INVEST
- CG-07 — EXPLORE
- CG-01 — BENCHMARK
- B-residual — Conditional Reserve
- R1 — Conditional Reserve
- R2 — Conditional Reserve
- R3 — BLOCKED
- second differentiated Primary Bet — intentionally unfilled
- uArch Primary Bet — none

## Hardware gate

Still mandatory:

`STRUCTURAL_SIGNAL → SYSTEM_VALUE → SOFTWARE_INSUFFICIENCY → hardware-specific cause → UARCH_CANDIDATE`

## Operating rule

Future research resumes from this repository.

V1 remains frozen for provenance and historical reference.

See:
[Authority Cutover Closeout](CUTOVER-CLOSEOUT.md)
