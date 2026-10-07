# TXN-20261007-EVIDENCE-RESCUE-R1-01

Date: 2026-10-07
Question: Are current portfolio conclusions vulnerable to shallow understanding of decision-critical evidence?

## Scope
Current A / PT-A / C / CG-06 / CG-07 paper evidence.

## Audit result
33 unique paper Sources directly ground the five lanes.
14 lacked review_depth metadata at audit start; 13 were P0.

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
- active-lane evidence-depth registry created.
- Graph QA gains decision-critical paper depth warnings during rescue mode.

## Next
Rescue PT-A PAPER-037/038/039/040/042, then remaining early A sources.
Frontier Round 14 remains paused until active-lane evidence-depth debt is cleared.
