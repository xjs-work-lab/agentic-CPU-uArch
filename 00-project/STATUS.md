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
research_content_migrated: true
evidence_rescue: ACTIVE
evidence_depth_protocol: EDP_V1
```

## Authority
**V2.2 is the active Research SSOT.**

Repository: `xjs-work-lab/agentic-CPU-uArch`

Frozen historical source: `xiejinsen/agentic-CPU-uArch@960abb4ef50f050da3c6784d30826053d42e5c5d`

## Current graph
- 383 canonical nodes
- 610 canonical semantic edges
- 610 generated reverse edges
- projection prepared after Evidence Rescue 1A PT-A deep audit
- Round 13 Graph QA: **PASS** — run `37607500340`, job `112746473467`
- Evidence Rescue Round 1 Graph QA: **PASS** — run `37609685036`, job `112753634718`
- Evidence Rescue Round 1 squash merge: `192e3fc816fd96d3112b1a0f94da916f8f869e33`

## Portfolio invariant
- A — only differentiated Primary Bet
- PT-A — Platform Track / 80.0 / SYSTEM_VALUE; Rescue-1A reframes core contract around capability/authority + fresh context binding + OutcomeReceipt + verification/recovery
- C — Strategic Enabler / SYSTEM_VALUE
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
`STRUCTURAL_SIGNAL → SYSTEM_VALUE → SOFTWARE_INSUFFICIENCY → hardware-specific cause → UARCH_CANDIDATE`

## Evidence Rescue state
Frontier Round 14 remains **PAUSED**.

### Rescue Round 1
Re-read PAPER-009 / 041 / 051 / 052 and introduced EDP v1.

### Rescue-1A — PT-A
Re-read under EDP v1:
- PAPER-037 ClawMobile
- PAPER-038 Beyond GUI
- PAPER-039 HybridCUA
- PAPER-040 PhoneHarness
- PAPER-042 UIAnchor

Added decision-critical counter/baseline evidence:
- PAPER-101 Action Rebinding / CCS 2026
- PAPER-102 VeriGUI / ACL 2026

PT-A result:
- lane **PLATFORM_TRACK unchanged**
- score **80.0 unchanged**
- maturity **SYSTEM_VALUE unchanged**
- new residual: **observation→action context integrity**
- new validation: `EXP-PTA-002`
- no software-insufficiency pass
- no hardware/uArch candidate

### Evidence-depth debt
Original five-lane audit started with 33 unique papers and 14 missing depth metadata.
Two new FULL_10Q papers were added during Rescue-1A, so the current five-lane source set is 35.

After Rescue-1A:
- remaining primary-lane paper debt: **5** — PAPER-013 / 015 / 043 / 044 / 050, all in A;
- expected whole-current-ROADMAP paper-depth warnings: **17** — primary 5 + reserve-lane 12.

## Operating rule
Next: **Rescue-1B Candidate A deep audit**.

Do not resume Frontier Round 14 until PAPER-013 / 015 / 043 / 044 / 050 are deep-read and the five-lane decision backtrace is rerun.

Before final portfolio convergence, also clear reserve-lane paper debt and audit decision-critical patents.
