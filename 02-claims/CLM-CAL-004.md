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
PAPER-094 shows a software lifecycle for continually evolving adapter collections; PAPER-095 exposes LoRA identity and mobile application lifecycle to KV-cache software; PAPER-104 extends the baseline to **live foreground Agent inference plus local adapter training/publication** on one 24 GB consumer GPU with explicit adapter-version/KV validity.

This materially strengthens the software-capture interpretation.

## Boundary
PAPER-104 is not a commercial-phone experiment. The remaining unresolved boundary is target-phone battery/thermal/foreground-QoE behavior and any residual after the LOCAL-class software runtime, not whether versioned adapter/KV state can be represented in software.
