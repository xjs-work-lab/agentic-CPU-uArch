+++
id = "CLM-AGENT-002"
type = "CLAIM"
record_state = "CURRENT"
claim_kind = "OBSERVATION"
status = "SUPPORTED"
scope = "generic demand-prediction baseline"
supersedes = []
+++

# CLM-AGENT-002

## Proposition
Behavioral history provides a strong generic predictor baseline for assistance demand/help-seeking timing.

## Current interpretation
- PAPER-043 / ICLR 2025 shows human activity is learnable for proactive intervention, but false-alarm remains high.
- PAPER-044 / ProAgentBench shows real longitudinal user history and real-world training materially improve When-to-Assist prediction; time-based per-user history is therefore part of the strongest baseline.

B4-TX may include long history, personalization and learned timing prediction where legally/product-wise available.

## Boundary
These labels are proxies for useful/help-seeking intervention, not direct observation of internal Agent RequiredProgress.

PAPER-044 is largely workstation/desktop data and its timing ground truth is anchored to observed assistance/LLM-use triggers.
PAPER-043's large training set is synthetic/generated while its test split is real.

Neither source establishes phone CPU/NPU cost or that history fully reconstructs DemandState.

## Evidence-depth audit
EDP v1 revalidated 2026-10-07.
