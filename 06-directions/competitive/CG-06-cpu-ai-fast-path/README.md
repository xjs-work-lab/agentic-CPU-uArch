+++
id = "CG-06"
type = "DIRECTION"
record_state = "CURRENT"
title = "CPU-Resident Latency-Critical Agent AI Fast Path"
direction_class = "COMPETITIVE_GAP"
competitive_action = "INVEST"
score_context = 86.5
evidence_maturity = "STRUCTURAL_SIGNAL"
maturity_scope = "public smartphone/engineering evidence supports the path; representative Agent crossover and Huawei target-system value remain unproven"
related_claims = ["CLM-CPU-001", "CLM-CPU-002", "CLM-CPU-003", "CLM-HUAWEI-001", "CLM-CG06-EXP-001"]
related_capabilities = ["CAP-ARM-C2-SME2-CPU-AI"]
+++

# CG-06 — CPU-Resident Latency-Critical Agent AI Fast Path

## 30-second decision
**INVEST / 86.5 / Adaptation + Differentiation**

Strategic control point:
stage/operator placement + dispatch/fallback/layout/state reuse across CPU and NPU paths.

## Evidence synthesis
- `CLM-CPU-001`: CPU↔NPU winner is workload-stage/operator dependent in direct phone evidence.
- `CLM-CPU-002`: CPU matrix acceleration materially expands the CPU-local region under evaluated settings.
- `CLM-CPU-003`: Arm publicly productizes CPU+SME2 for responsive Agentic/local AI.
- `CLM-HUAWEI-001`: equivalent Huawei smartphone CPU matrix-AI fast path is not publicly established in the reviewed V1 source set.

## Boundary
- Strategic gap / adaptation route, **not global novelty**.
- No inference of Huawei internal absence.
- No new ISA/uArch conclusion.
- Exhaust existing compiler/runtime/ISA paths first.

## Next discriminating gate
`EXP-CG06-001` tests whether a representative CPU-fast-path region remains after all launch/communication/fallback/layout costs are counted.
