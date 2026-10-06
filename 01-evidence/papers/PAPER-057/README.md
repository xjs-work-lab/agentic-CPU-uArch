+++
id = "PAPER-057"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
independence_assessment = "UNKNOWN"
title = "ShadowNPU: System and Algorithm Co-design for NPU-Centric On-Device LLM Inference"
primary_url = "https://doi.org/10.1145/3745756.3809205"
priority = "P0"
evidence_role = "direct mobile heterogeneous NPU-CPU/GPU operator partition and pipeline evidence for CG-06/C"
authors = ["Wangsong Yin", "Daliang Xu", "Mengwei Xu", "Gang Huang", "Xuanzhe Liu"]
venue = "ACM MobiSys 2026"
+++

# PAPER-057 — ShadowNPU

## 30-second read
- **Why it matters:** Demonstrates a concrete mobile path where NPU and CPU/GPU cooperate at finer granularity because attention components have different precision/economic properties.
- **What it establishes:** The evaluated system moves low-precision dense estimation to the NPU and retains sparse high-precision work on CPU/GPU, with graph bucketing and pipelining used to control cross-engine overhead.
- **Reported anchors:** up to 4.5x end-to-end speedup and up to 7.7x energy reduction with 0.4 percentage-point accuracy loss in the reported evaluation.
- **Portfolio pressure:** Strongly reinforces CG-06's stage/operator-placement framing and argues against a simple NPU-first policy.
- **Boundary:** Evaluated on Qualcomm Hexagon NPUs; generality across other NPU families and real Agent workloads remains open.
- **Primary source:** https://doi.org/10.1145/3745756.3809205
