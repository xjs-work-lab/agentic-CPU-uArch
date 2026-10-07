+++
id = "PAPER-091"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
decision_use = "DIRECT_PHONE_TRAINING_SYSTEM_VALUE"
independence_assessment = "PREPRINT_DIRECT_SMARTPHONE_SYSTEM_MEASUREMENT"
title = "Fine-Tuning a 3B-Parameter LLM on a Smartphone: Characterizing Sustained Training"
primary_url = "https://arxiv.org/abs/2610.06325"
priority = "P0"
evidence_role = "Direct real-smartphone evidence for sustained multi-billion-parameter fine-tuning, energy, thermal throttling and backward-pass runtime gaps"
authors = ["Andrew Geyko", "Marius Mosbach", "André Brinkmann"]
venue = "arXiv preprint 2026"
+++

# PAPER-091 — Fine-Tuning a 3B-Parameter LLM on a Smartphone: Characterizing Sustained Training

## 30-second read
- **Why it matters:** supplies the missing real-phone sustained-training evidence rather than single-step or desktop proxies.
- **Platform:** iPhone 17 Pro; 3B model at 4-bit precision; complete per-user adapter runs.
- **Key finding:** training throughput drops to roughly half under sustained thermal throttling; tested pause/burst schedules do not recover it.
- **Efficiency finding:** repaired backward kernel gives 1.47× faster training on roughly one-third less energy.
- **Portfolio meaning:** mobile training is physically feasible and system-relevant, but the bottleneck is still largely generic training/runtime rather than Agent-specific.

See [deep.md](deep.md) for full Paper Insight 10Q.
