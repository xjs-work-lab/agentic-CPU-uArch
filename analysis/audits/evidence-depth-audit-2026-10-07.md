# Evidence Depth Audit — Current Portfolio

Date: 2026-10-07
Audit mode: EDP v1 rescue

## Baseline at Rescue start
The five primary active/platform lanes A / PT-A / C / CG-06 / CG-07 were grounded by **33 unique paper Sources**.

At audit start:
- 19 / 33 carried FULL_10Q-class metadata;
- 14 / 33 lacked `review_depth`;
- 13 / 14 were P0.

## Rescue progress

### Rescue-0 complete
PAPER-009 / 041 / 051 / 052 revalidated.

### Rescue-1A complete — PT-A
PAPER-037 / 038 / 039 / 040 / 042 revalidated under EDP v1.

Two new decision-critical FULL_10Q sources were added:
- PAPER-101 — Action Rebinding / CCS 2026
- PAPER-102 — VeriGUI / ACL 2026

These additions expand the current five-lane paper set from 33 to **35**, but create no new depth debt because both enter as EDP v1 FULL_10Q.

## Current primary-lane debt
Only **5 papers** remain:
- PAPER-013 — A
- PAPER-015 — A
- PAPER-043 — A
- PAPER-044 — A
- PAPER-050 — A

PT-A now has **zero current paper-depth warnings**.

## Whole current-ROADMAP debt
Reserve-lane paper debt remains:
- PAPER-008 — R2
- PAPER-028 / 029 / 030 / 031 / 032 / 033 / 034 / 035 — B-residual
- PAPER-047 / 048 — R1
- PAPER-049 — R2

Expected warning state after Rescue-1A:
- primary lanes: **5**
- reserve lanes: **12**
- whole current ROADMAP: **17**

R3 remains patent-heavy and must be audited through the patent direct-claim gate separately.

## Rescue-1A findings that materially change interpretation

### PAPER-037
Real Pixel 9 runtime, but **remote model inference**. Do not treat as local-LLM compute/energy evidence.

### PAPER-038
CLI/ADB strongly changes task reachability and steps, but benchmark/rooted-emulator/backend access can exceed retail-phone authority.

### PAPER-039
More action surfaces are not automatically beneficial.
Untrained GUI+CLI drops OSWorld accuracy from 38.8% to 18.4%; selective SFT/RL is required.

### PAPER-040
Mixed-action/trace-verifier harness is valuable, but headline 75.0% pass rate combines capabilities, routing, controller quality and verifier stack. Verification is not isolated causally.

### PAPER-042
UIAnchor is strong peer-reviewed mobile system evidence, but current audited primary material does not support attributing its 75.5% latency / 52.4% energy improvements specifically to verification/recovery.

### PAPER-101
Adds decisive negative evidence: observation and action recipient can diverge. Recovery/confirmation alone can be insufficient.

### PAPER-102
Adds causal evidence that action-effect verification training improves recovery, while raising the software baseline.

## Current risk by lane

| Lane | Current paper-depth risk |
|---|---|
| A | HIGH — five early sources remain |
| PT-A | LOW for paper depth — Rescue-1A complete |
| C | LOW |
| CG-06 | MEDIUM for final target-phone residual, but paper-depth debt cleared |
| CG-07 | LOW for papers; vendor audit pending |
| B-residual | HIGH |
| R1 | MEDIUM-HIGH |
| R2 | MEDIUM-HIGH |
| R3 | patent audit required |

## Next
1. Rescue-1B: PAPER-013 / 015 / 043 / 044 / 050.
2. Rerun five-lane decision backtrace.
3. Then Rescue-2 reserves and patent evidence.
4. Frontier Round 14 only after the five primary lanes are depth-clean.
