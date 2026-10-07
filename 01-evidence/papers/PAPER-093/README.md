+++
id = "PAPER-093"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
decision_use = "STRONG_MEMORY_BASELINE"
independence_assessment = "PEER_REVIEWED_ON_DEVICE_TRAINING"
title = "Memory-Efficient Structured Backpropagation for On-Device LLM Fine-Tuning"
primary_url = "https://aclanthology.org/2026.acl-industry.62/"
priority = "P1"
evidence_role = "Peer-reviewed algorithm/runtime baseline showing exact LoRA gradients with substantially lower activation memory through structured recomputation"
authors = ["JuneYoung Park", "Yuri Hong", "Seongwan Kim", "Jaeho Lee"]
venue = "ACL 2026 Industry Track"
+++

# PAPER-093 — Memory-Efficient Structured Backpropagation for On-Device LLM Fine-Tuning

## 30-second read
- **Why it matters:** attacks training-memory pressure without weakening gradient correctness.
- **Mechanism:** manually derived backward passes recompute LoRA’s small intermediate projection instead of retaining it.
- **Reported result:** 49% average memory reduction vs MeBP; 361 MB → 136 MB for Qwen2.5-0.5B with exact gradients.
- **Boundary:** evaluated in Apple-Silicon/MLX-style environment; not an Agent runtime and not a phone-wide energy study.
- **Portfolio meaning:** further reduces the generic memory residual available to any H-CAL hardware thesis.

See [deep.md](deep.md) for full Paper Insight 10Q.
