+++
id = "PAPER-092"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
decision_use = "GENERIC_MOBILE_TRAINING_RUNTIME_BASELINE"
independence_assessment = "PREPRINT_REAL_PHONE_TRAINING_FRAMEWORK"
title = "MobileFineTuner: A Mobile-Native Framework for On-Device LLM Fine-Tuning in Real-World Embedded AI Applications"
primary_url = "https://arxiv.org/abs/2512.08211"
priority = "P1"
evidence_role = "Mobile-native C++ framework baseline for real-phone Full-FT/LoRA with memory and energy controls plus a private personalized health-Agent case study"
authors = ["Jiaxiang Geng", "Lunyu Zhao", "Yiyi Lu", "Bing Luo"]
venue = "arXiv preprint 2025/2026 revision"
+++

# PAPER-092 — MobileFineTuner: A Mobile-Native Framework for On-Device LLM Fine-Tuning in Real-World Embedded AI Applications

## 30-second read
- **Why it matters:** shows that real-phone training can be packaged as reusable mobile-native runtime infrastructure, not only research scripts.
- **Mechanisms:** parameter sharding, gradient accumulation, activation checkpointing, memory-efficient attention and energy-aware scheduling.
- **Agent relevance:** includes a private campus health-Agent case study using local wearable/user history.
- **Boundary:** broad training framework; Agent-specific runtime semantics are not its main mechanism.
- **Portfolio meaning:** further raises the generic software baseline for H-CAL.

See [deep.md](deep.md) for full Paper Insight 10Q.
