+++
id = "T8"
type = "TREND"
record_state = "CURRENT"
title = "Cross-device Agent fabric & continuation"
time_horizon = "2027-2029"
scope = "SMARTPHONE_AGENTIC_CPU_SYSTEM_UARCH"
trend_maturity = "EMERGING_PRODUCT_TREND"
product_posture = "BENCHMARK_AND_PREPARE"
coverage_state = "OWNED_BY_EXISTING_DIRECTIONS_AND_PLATFORM"
related_claims = ["CLM-T8-001", "CLM-T8-002", "CLM-T8-003", "CLM-T8-004"]
related_capabilities = []
direction_links = [{ direction_id = "C", differentiation_posture = "RESIDUAL_RESEARCH" }, { direction_id = "B-residual", differentiation_posture = "RESIDUAL_RESEARCH" }, { direction_id = "PT-A", differentiation_posture = "RESIDUAL_RESEARCH" }]
+++

# T8 — Cross-device Agent fabric & continuation

## Product thesis
T8 asks whether phone↔PC↔watch↔edge Agent continuation introduces execution-state handoff, consistency or recovery costs materially different from ordinary distributed task orchestration. It is a frontier signal, not yet a Direction.

## Interpretation invariant
A paper or product may strengthen this Trend while simultaneously narrowing the novelty of one or more linked Directions.

> **Prior art constrains novelty, not product relevance.**


## Round 14-C final
Evidence:
- PAPER-109 DevicesWorld;
- PAPER-110 UFO³;
- PAPER-111 explicit Agent state migration;
- PAPER-112 EdgeFlow generic KV migration;
- VENDOR-021 Windows Resume continuity.

Final:
- **EMERGING_PRODUCT_TREND**
- **BENCHMARK_AND_PREPARE**
- standalone T8-specific candidate = **KILL_DIFFERENTIATED_BET**
- ownership = **C + B-residual/T5 + PT-A**
- no T8-specific Direction
- no second Primary Bet
- no uArch candidate

## Reopen condition
Require physical-phone evidence that cross-device continuation must migrate in-flight Agent inference/runtime state with a material cost beyond ordinary task/RPC/checkpoint/KV/context transfer and existing C/T5/PT-A controls.
