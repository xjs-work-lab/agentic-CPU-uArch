+++
id = "PAPER-079"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
decision_use = "PRIOR_ART_BASELINE"
independence_assessment = "PEER_REVIEWED_EDGE_SYSTEMS"
title = "MMEdge: Accelerating On-device Multimodal Inference via Pipelined Sensing and Encoding"
primary_url = "https://doi.org/10.1145/3774906.3800485"
priority = "P0"
evidence_role = "current on-device systems prior art for fine-grained sensing/encoding pipelining, modality-aware configuration, cross-modal skipping and runtime adaptation under resource/thermal dynamics"
authors = ["Runxi Huang", "Mingxuan Yu", "Mingyu Tsoi", "Xiaomin Ouyang"]
venue = "SenSys 2026"
+++

# PAPER-079 — MMEdge

## 30-second read
- **Why it matters:** Directly pressures H-PAM's last cross-stage/cross-representation systems residual.
- **Mechanism:** fine-grained sensing+encoding pipeline, adaptive modality/model configuration, temporal aggregation, cross-modal speculative skipping.
- **Reported anchor:** up to 75.83% end-to-end latency reduction on a real multimodal UAV testbed while preserving task performance; additional evaluation on NVIDIA edge devices.
- **Systems relevance:** profiling explicitly includes end-to-end sensing/inference behavior, CPU scheduling and thermal throttling effects.
- **Portfolio meaning:** sensing→encoding coupling, modality-aware runtime configuration and cross-modal skipping are generic on-device multimodal-systems prior art, not memory-specific differentiation.
- **Boundary:** not a smartphone-Agent-memory workload; UAV/edge systems and inference task.
- **Primary source:** https://doi.org/10.1145/3774906.3800485
- **Artifact:** https://github.com/HKUST-MINSys-Lab/MMEdge

See [deep.md](deep.md) for full Paper Insight 10Q.