+++
id = "PAPER-090"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
decision_use = "STRONG_GENERIC_MOBILE_TRAINING_BASELINE"
independence_assessment = "PEER_REVIEWED_REAL_MOBILE_TRAINING"
title = "FBLayout: Optimizing Memory Layout for Efficient LLM Finetuning on Mobile GPUs"
primary_url = "https://arxiv.org/abs/2607.21624"
priority = "P0"
evidence_role = "Peer-reviewed mobile-systems strongest baseline showing that forward/backward layout conflict and data movement in mobile-GPU fine-tuning are heavily software-capturable"
authors = ["Kahou Tam", "Wei Niu", "Yu Bao", "Xiaomin Ouyang", "ChengZhong Xu", "Li Li"]
venue = "MobiSys 2026"
+++

# PAPER-090 — FBLayout: Optimizing Memory Layout for Efficient LLM Finetuning on Mobile GPUs

## 30-second read
- **Why it matters:** on-device training has different memory/layout behavior from inference, but strong software/HW-aware layout co-design already captures much of it.
- **Mechanism:** R-Tile unified layout, index transformation instead of physical movement, global activation-guided layout propagation.
- **Reported result:** 2.2–5.7× speedup over MNN/TFLite/TVM across seven transformer models and ARM Mali / Qualcomm Adreno phones.
- **Boundary:** generic transformer fine-tuning; not Agent-specific concurrency or continual-learning semantics.
- **Portfolio meaning:** any H-CAL hardware thesis must beat this kind of mobile-GPU software/layout optimization first.

See [deep.md](deep.md) for full Paper Insight 10Q.
