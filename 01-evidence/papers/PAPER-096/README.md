+++
id = "PAPER-096"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
decision_use = "GENERIC_TRAINING_ALGORITHM_SYSTEM_BASELINE"
independence_assessment = "PREPRINT_ANDROID_PROTOTYPE"
title = "ZeroLock: Concurrent Memory-Efficient LLM Training via Modular Update Decoupling"
primary_url = "https://arxiv.org/abs/2608.07974"
priority = "P1"
evidence_role = "generic training baseline showing that update coupling and activation retention can be reduced algorithmically with an Android prototype"
authors = ["Wentao Dai", "Xuanran Li", "Yuxiang Zhang", "Ming Tang", "Chao Huang"]
venue = "arXiv preprint 2026"
+++

# PAPER-096 — ZeroLock

## 30-second read
- **Why it matters:** attacks training update-locking at algorithm level rather than treating it as fixed hardware behavior.
- **Mechanism:** local-objective modular updates decouple model chunks, reducing pipeline waiting and activation lifetime.
- **Android prototype:** TinyLlama fine-tuning reports peak PSS below 4 GB, battery temperature around 37°C and 1644.1 s wall time.
- **Server prototype result:** 26.5% memory reduction and 4.9% throughput improvement vs BP pipeline baseline.
- **H-CAL meaning:** further weakens generic “training concurrency requires new hardware” claims; it does not evaluate live Agent serving.

See [deep.md](deep.md) for full Paper Insight 10Q.
