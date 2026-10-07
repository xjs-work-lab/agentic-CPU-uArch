+++
id = "CLM-CAL-001"
type = "CLAIM"
record_state = "CURRENT"
claim_kind = "SOURCE_CLAIM"
status = "SUPPORTED"
scope = "Agent contiguous local-learning structural coupling"
supersedes = []
+++

# CLM-CAL-001

## Proposition
Contiguous on-device Agent learning can couple foreground inference, feedback/judge work, adapter training/publication and KV-cache validity because model-state updates invalidate cached hidden state produced under older adapter versions.

## Current interpretation
PAPER-089 establishes this as an Agent-native runtime problem rather than ordinary static fine-tuning.

## Boundary
The evidence is from a single 24 GB consumer GPU, not a smartphone SoC, and PAPER-089 also demonstrates substantial software-runtime capture.
