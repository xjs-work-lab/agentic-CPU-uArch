+++
id = "PAPER-089"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
decision_use = "AGENT_CONTIGUOUS_LEARNING_SEED"
independence_assessment = "PREPRINT_AGENT_RUNTIME"
title = "LOCAL: Enabling Learning On-device Contiguously for Agent LLMs"
primary_url = "https://arxiv.org/abs/2608.15241"
priority = "P0"
evidence_role = "Agent-native systems seed showing that continual local adaptation couples foreground inference, background learning, adapter-version publication, KV-cache validity and memory pressure"
authors = ["Xinxin Liu", "Jiaxin Li", "Zibo Wang", "Yun Ji", "Zhangqi Zhu", "Qing Hu", "Zhibin Wang", "Rong Gu", "Sheng Zhong", "Chen Tian"]
venue = "arXiv preprint 2026"
+++

# PAPER-089 — LOCAL: Enabling Learning On-device Contiguously for Agent LLMs

## 30-second read
- **Why it matters:** breaks the stable-weight inference assumption for local Agents; inference and learning share one device and model instance.
- **Mechanism:** cooperative GPU scheduling + version-aware KV cache + multi-agent runtime over shared adapter-version/task-priority/cache-validity state.
- **Reported result:** queue-wait p95 3.1× lower than FIFO, TTFT p95 1.55× lower than non-preemptible training, and lower post-publish/cross-agent tail latency.
- **Boundary:** evaluated on a single 24 GB consumer GPU with 7B-class models, not a smartphone SoC.
- **Portfolio meaning:** strong Agent-native structural signal, but also a strong software-runtime baseline against any new hardware thesis.

See [deep.md](deep.md) for full Paper Insight 10Q.
