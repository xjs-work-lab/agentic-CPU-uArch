# TXN-20261007-EVIDENCE-RESCUE-R1-01

Date: 2026-10-07
Question: Are current portfolio conclusions vulnerable to shallow understanding of decision-critical evidence?

## Scope
Primary audit: A / PT-A / C / CG-06 / CG-07 paper evidence.
QA warning scope: every Direction scheduled by the current ROADMAP.

## Audit result
Primary five lanes:
- 33 unique paper Sources;
- 14 lacked review_depth metadata at audit start;
- 13 were P0.

After Round-1 rescue:
- 10 primary-lane paper warnings remain.

Whole current ROADMAP:
- Graph QA reports 22 decision-critical paper warnings after Round 1;
- 12 are additional current reserve-lane papers in B-residual / R1 / R2.

## Sources re-read under EDP v1
- PAPER-009
- PAPER-041
- PAPER-051
- PAPER-052

## Corrections
- PAPER-009: CPU-over-NPU Prefill result narrowed to evaluated stack; backend maturity/operator coverage are causal alternatives.
- PAPER-041: Effect/Commit legality is conditionally runtime-constructible/enforceable, not universally derivable.
- PAPER-051: generic UMA execution, HAL allocation and suspend/yield effects separated.
- PAPER-052: CPU-matrix viability retained; no claim of phone CPU>NPU superiority; energy/GPU comparisons scoped to M4 Pro.

## Decision change
No lane, score or maturity change.

## Research-process change
- EDP v1 policy created.
- evidence-depth registry created.
- Graph QA gains warning-only decision-critical paper-depth checks during rescue mode.
- Graph QA run 37609526876 passes and exposes the broader 22-paper current-roadmap backlog.

## Next
1. Rescue PT-A PAPER-037/038/039/040/042.
2. Rescue A PAPER-013/015/043/044/050.
3. Rerun active-lane backtrace before Frontier Round 14.
4. Then rescue B-residual / R1 / R2 and audit patent-heavy lanes before final portfolio convergence.
