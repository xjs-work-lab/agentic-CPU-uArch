+++
id = "PAPER-059"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
decision_use = "DECISION_GRADE_WITH_SCOPE_BOUNDARY"
independence_assessment = "GROUP_OVERLAP_WITH_PAPER_057"
title = "Fast On-device LLM Inference with NPUs"
primary_url = "https://doi.org/10.1145/3669940.3707239"
priority = "P0"
evidence_role = "direct commercial-phone optimized NPU offload baseline; predecessor lineage for ShadowNPU and CG-06 strongest comparator"
authors = ["Daliang Xu", "Hao Zhang", "Liming Yang", "Ruiqi Liu", "Gang Huang", "Mengwei Xu", "Xuanzhe Liu"]
venue = "ACM ASPLOS 2025"
+++

# PAPER-059 — Fast On-device LLM Inference with NPUs (llm.npu)

## 30-second read
- **Why it matters:** Establishes that mobile NPU shortcomings for LLMs can be substantially overcome in software by reconstructing prompt/model execution across prompt, tensor and block levels.
- **What it establishes:** On evaluated Xiaomi/Redmi Snapdragon phones, NPU-centric prefill with selective CPU/GPU residual work can strongly outperform CPU/GPU and prior NPU baselines while preserving accuracy.
- **Reported anchors:** 22.4x average faster prefill and 30.7x average energy savings in the paper headline; up to 32.8x end-to-end application speedup; >1000 tokens/s prefill for billion-scale models.
- **Portfolio meaning:** Strong precursor to ShadowNPU; reinforces that optimized NPU software is a fast-moving frontier that CG-06 must beat.
- **Boundary:** Primarily generic mobile-LLM prefill; not Agent-semantic placement and not Huawei transfer.
- **Primary source:** https://doi.org/10.1145/3669940.3707239
- **Artifact:** https://doi.org/10.5281/zenodo.14392760

See [deep.md](deep.md) for the full Paper Insight 10Q.
