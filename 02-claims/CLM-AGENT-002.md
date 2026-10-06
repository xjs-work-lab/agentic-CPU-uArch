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
Behavioral history provides a strong generic predictor baseline for assistance demand.

## Current interpretation
PAPER-043 and PAPER-044 independently show that observed behavioral history can train/improve proactive assistance prediction; PAPER-044 is the stronger long-history real-workflow baseline.

## Boundary
Primarily desktop/workstation workflow evidence; not phone CPU/NPU active-cost ground truth.

## Migration
- V1 baseline: `960abb4ef50f050da3c6784d30826053d42e5c5d`
- Transform: `STRUCTURAL_REPACK`
