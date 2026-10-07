# Research Authority Status

Updated: 2026-10-07

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
evidence_rescue: ACTIVE
evidence_depth_protocol: EDP_V1
```

## Authority
**V2.2 is the active Research SSOT.**

Repository: `xjs-work-lab/agentic-CPU-uArch`

Frozen historical source: `xiejinsen/agentic-CPU-uArch@960abb4ef50f050da3c6784d30826053d42e5c5d`

## Current graph
- 374 canonical nodes
- 587 canonical semantic edges
- 587 generated reverse edges
- projection refreshed after Frontier Round 13 Agent-flow heterogeneous SoC orchestration
- last full cutover QA hard errors: 0
- Round 12 Graph QA: **PASS** — run `37599649724`, job `112720612564`
- Round 12 QA squash merge: `7fa99ba2ae56a997e6d35bd68b508623dd2d577a`
- Round 13 Graph QA: **PASS** — run `37607500340`, job `112746473467`
- Round 13 squash merge: `4e1515e8f09a8e288a343d220ba3c0ea17cd8e53`
- Round 13 work-branch cleanup: **PASS** — run `37607556023`
- Evidence Rescue Round 1 Graph QA: **PASS** — run `37609685036`, job `112753634718`
- Evidence Rescue Round 1 squash merge: `192e3fc816fd96d3112b1a0f94da916f8f869e33`
- Evidence Rescue Round 1 work-branch cleanup: **PASS** — run `37609721034`

## Portfolio invariant
- A — only differentiated Primary Bet
- PT-A — Platform Track
- C — Strategic Enabler / SYSTEM_VALUE
- CG-06 — INVEST
- CG-07 — EXPLORE; proactive workload strengthened, PRPF-class strongest baseline added
- CG-01 — BENCHMARK
- B-residual — Conditional Reserve
- R1 — Conditional Reserve
- R2 — Conditional Reserve
- R3 — BLOCKED
- second differentiated Primary Bet — intentionally unfilled
- system-control second-Bet search — converged / no standalone Bet found
- H-PAM — CLOSED / killed as standalone candidate
- security / confidential execution — platform requirement + research radar
- proactive / always-on intervention gating — covered inside CG-07; not standalone
- H-CAL — CLOSED / killed as standalone candidate; contiguous learning retained as workload/evaluation scenario
- current second-Bet frontier — NONE / UNASSIGNED after Round 13
- uArch Primary Bet — none

## Hardware gate
`STRUCTURAL_SIGNAL → SYSTEM_VALUE → SOFTWARE_INSUFFICIENCY → hardware-specific cause → UARCH_CANDIDATE`

## Evidence Rescue state
Frontier Round 14 is **PAUSED** while current portfolio evidence is revalidated under EDP v1.

Five primary-lane paper audit:
- 33 unique paper Sources directly ground A / PT-A / C / CG-06 / CG-07;
- 14 lacked review_depth metadata at audit start;
- 13/14 were P0;
- Rescue Round 1 re-reads PAPER-009 / 041 / 051 / 052;
- no lane/score/maturity reversal from Round 1;
- remaining primary-lane paper debt after Round 1: **10**.

Whole current-ROADMAP warning audit:
- Graph QA follows all scheduled Directions, including B-residual / R1 / R2 / R3;
- remaining decision-critical paper warnings after Round 1: **22**;
- therefore **12 additional reserve-lane papers** require later rescue beyond the primary-lane 10.

Method authority:
- `00-project/evidence-depth-policy.md`
- `analysis/audits/evidence-depth-audit-2026-10-07.md`
- `analysis/audits/decision-backtrace-audit-2026-10-07.md`

## Operating rule
Do not resume frontier expansion until the 10 primary-lane decision-critical paper warnings are cleared and active-lane backtrace is rerun.

Before final portfolio convergence, also clear current reserve-lane paper debt and audit decision-critical patent evidence.

Historical Kill lanes are audited after current-roadmap evidence is clean.
