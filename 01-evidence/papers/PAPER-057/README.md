+++
id = "PAPER-057"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
decision_use = "DECISION_GRADE_WITH_SCOPE_BOUNDARY"
independence_assessment = "UNKNOWN"
title = "ShadowNPU: System and Algorithm Co-design for NPU-Centric On-Device LLM Inference"
primary_url = "https://doi.org/10.1145/3745756.3809205"
priority = "P0"
evidence_role = "direct commercial-phone NPU-centric attention + CPU/GPU residual evidence; strong optimized-NPU baseline and pressure test for CG-06"
authors = ["Wangsong Yin", "Daliang Xu", "Mengwei Xu", "Gang Huang", "Xuanzhe Liu"]
venue = "ACM MobiSys 2026"
+++

# PAPER-057 — ShadowNPU

## 30-second read
- **Why it matters:** Direct smartphone evidence that a strong NPU-centric system can reclaim work that mainstream frameworks usually leave on CPU/GPU by decomposing the operator according to precision and hardware affinity.
- **What it establishes:** On evaluated Snapdragon phones, low-precision NPU estimation + small high-precision CPU/GPU sparse attention + graph bucketing + cross-engine pipelining can sharply reduce CPU/GPU dependence while preserving near-full-attention accuracy.
- **Reported anchors:** up to 4.5x and 2.9x average end-to-end speedup vs one-core C/G-Full under the paper's constrained-resource setup; up to 7.66x lower single-attention-kernel energy on the evaluated Redmi K60; average accuracy 36.4 vs 36.8 lossless C/G-Full across four models/three datasets.
- **Portfolio meaning:** strengthens heterogeneous-placement evidence but **challenges the size of the CPU-resident region**. CG-06 must beat an optimized NPU-centric path, not a naive NPU baseline.
- **Boundary:** Generic mobile-LLM/operator evidence with Agent-relevant datasets; not Agent-native scheduling and not Huawei transfer.
- **Primary source:** https://doi.org/10.1145/3745756.3809205

## Decision-use gate
**FULL 10Q COMPLETE — decision-grade within the evaluated Qualcomm/mobile-LLM scope.**

Use as:
- direct commercial-phone evidence for fine-grained CPU/NPU role decomposition;
- strong optimized-NPU baseline for CG-06;
- evidence that numerical semantics (relative-ranking tolerance vs exact-value sensitivity) can determine hardware placement.

Do **not** use as:
- proof that Agent semantics themselves require heterogeneous placement;
- proof of Huawei NPU behavior;
- proof of CPU superiority over NPU;
- proof of new ISA/uArch need.

See [deep.md](deep.md) for the full Paper Insight 10Q.
