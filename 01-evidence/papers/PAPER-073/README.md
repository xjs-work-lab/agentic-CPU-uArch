+++
id = "PAPER-073"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
decision_use = "DECISION_GRADE_WITH_SCOPE_BOUNDARY"
independence_assessment = "PREPRINT_AGENT_NATIVE"
title = "Beyond Training: Enabling Self-Evolution of Agents with MobiMem"
primary_url = "https://arxiv.org/abs/2512.15784"
priority = "P0"
evidence_role = "direct mobile-Agent memory primitive and OS-integration evidence; Profile/Experience/Action memory lifecycle with scheduling, record-replay and exception recovery on Android workloads"
authors = ["Zibin Liu", "Cheng Zhang", "Xi Zhao", "Yunfei Feng", "Bingyu Bai", "Dahu Feng", "Erhu Feng", "Yubin Xia", "Haibo Chen"]
venue = "arXiv preprint 2025"
+++

# PAPER-073 — MobiMem

## 30-second read
- **Why it matters:** First reviewed source that directly combines specialized Agent memory types with mobile execution services in one system.
- **What it establishes:** Profile, Experience and Action memory are not interchangeable storage buckets; they drive different execution mechanisms including profile retrieval, template instantiation, action replay, step-level scheduling and exception recovery.
- **Phone evidence:** Snapdragon 8 Elite on-device evaluation is used for Action Memory; Experience Memory and AgentRR are source-reported as already deployed on a flagship smartphone.
- **Reported anchors:** 83.1% profile alignment with 23.83 ms retrieval; up to 50.3% task-success improvement from Experience Memory; 77.3% average action reuse with human-crafted templates; 1.6×–9× Action-Memory speedup on Snapdragon 8 Elite; up to 1.98× fine-grained scheduling speedup.
- **Portfolio meaning:** strengthens H-PAM's Agent-memory lifecycle premise, but also shows that much value is already capturable through application/runtime/OS software.
- **Boundary:** preprint; on-device inference path is CPU-only llama.cpp in the reported Snapdragon setup; no direct CPU/NPU/memory-hierarchy residual or uArch need is established.
- **Primary source:** https://arxiv.org/abs/2512.15784

See [deep.md](deep.md) for full Paper Insight 10Q.