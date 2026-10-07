+++
id = "CLM-CAL-004"
type = "CLAIM"
record_state = "CURRENT"
claim_kind = "INFERENCE"
status = "SUPPORTED"
scope = "on-device adapter lifecycle and LoRA KV software capture"
supersedes = []
+++

# CLM-CAL-004

## Proposition
On-device adapter evolution, adapter identity and LoRA-specific KV retention/reuse are explicitly representable and substantially optimizable in software under mobile resource constraints.

## Current interpretation
PAPER-094 shows a software lifecycle for continually evolving adapter collections, while PAPER-095 directly exposes LoRA identity and mobile application lifecycle to KV-cache software and reports substantial TTFT improvement.

## Boundary
Neither source evaluates live local gradient publication during a user-facing Agent session. They narrow, but do not individually eliminate, the adapter-version update residual.
