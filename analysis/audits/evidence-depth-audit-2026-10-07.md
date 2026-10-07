# Evidence Depth Audit — Current Portfolio

Date: 2026-10-07
Audit mode: EDP v1 rescue

## Baseline
At rescue start, A / PT-A / C / CG-06 / CG-07 were grounded by 33 unique paper Sources; 14 lacked current FULL_10Q depth metadata.

Rescue-1A added two new FULL_10Q sources, bringing the current five-lane set to **35**.

## Rescue progress
- Rescue-0: PAPER-009 / 041 / 051 / 052 — complete.
- Rescue-1A PT-A: PAPER-037 / 038 / 039 / 040 / 042 — complete.
- Rescue-1B A: PAPER-013 / 015 / 043 / 044 / 050 — complete.

## Primary-lane paper-depth state
After Rescue-1B source updates, **all current decision-critical paper Sources for A / PT-A / C / CG-06 / CG-07 carry EDP v1 FULL_10Q-class review metadata.**

Expected primary-lane warning count after Graph QA: **0**.

## Reserve-lane paper debt
Still pending:
- PAPER-008 — R2
- PAPER-028 / 029 / 030 / 031 / 032 / 033 / 034 / 035 — B-residual
- PAPER-047 / 048 — R1
- PAPER-049 — R2

Expected current-ROADMAP paper-depth warnings after Rescue-1B: **12**.

R3 is patent-heavy and requires the separate patent direct-claim gate.

## Rescue-1B corrections

### PAPER-013 — Speculative Interaction Agents
Speculative work and ready≠required semantics are real, but safe/unsafe, cancellation, dependency and commit state are explicitly runtime-managed.
Naturalistic Human Instructions also show a negative transfer case where speculative streaming becomes slower and less accurate.

### PAPER-015 — PARE
Observe / Awaiting Confirmation / Execute provide direct proactive demand/authorization semantics.
Effectful execution starts only after user acceptance; PARE does not prove pre-authorization effect speculation or phone system value.

### PAPER-043 — Proactive Agent
Metadata corrected to **ICLR 2025**.
The large 6,790-event Agent training set is generated/synthetic; the 233-event test set is real.
The 66.47% F1 result coexists with substantial false-alarm pressure.

### PAPER-044 — ProAgentBench
Real longitudinal history materially strengthens When-to-Assist prediction.
The protocol isolates each user's history and uses time-based splits, so legal personalization belongs in B4-TX.
Observed assistance/LLM-use triggers are still proxy ground truth, not intrinsic Agent RequiredProgress.

### PAPER-050 — TomasuLLM
COW sandboxing + dependency/effect tracing + commit validation derive substantial legality at runtime.
Irreversible or untraceable effects become speculation barriers, preventing an invalid universal-derivability conclusion.

## A decision consequence
A survives only as the hypothesis that **explicit Agent-internal DemandState / RequiredProgress contains decision-relevant information that is not reconstructible from long history, workflow/program state, SLO/utility, topology, verification/legality and reuse proxies.**

No source directly proves that residual.

## Next
1. Validate Rescue-1B with Graph QA.
2. Rerun/lock the five-lane decision backtrace.
3. If clean, resume Frontier Round 14.
4. Continue Rescue-2 reserve lanes and patent audit before final portfolio convergence.
