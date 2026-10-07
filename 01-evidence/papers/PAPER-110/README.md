+++
id = "PAPER-110"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
deep_review_protocol = "EDP_V1"
deep_review_date = "2026-10-07"
decision_critical = true
decision_use = "T8_CROSS_DEVICE_ORCHESTRATION_STRONGEST_SYSTEM_BASELINE"
independence_assessment = "MICROSOFT_LED_RESEARCH_SYSTEM"
title = "UFO3: Weaving the Digital Agent Galaxy"
primary_url = "https://arxiv.org/abs/2511.11332"
priority = "P0"
evidence_role = "engineered distributed Agent DAG/protocol/recovery baseline"
authors = ["Chaoyun Zhang", "Liqun Li", "He Huang", "Chiming Ni", "Bo Qiao", "Si Qin", "Yu Kang", "Minghua Ma", "Qingwei Lin", "Saravan Rajmohan", "Dongmei Zhang"]
venue = "arXiv preprint, current 2026 revision"
artifact_urls = ["https://github.com/microsoft/UFO"]
+++

# PAPER-110 — UFO³

## 30-second read
- Mutable distributed DAG called TaskConstellation.
- Persistent Agent Interaction Protocol channels support dispatch and result streaming.
- NebulaBench: 55 tasks, 5 machines, 10 categories.
- Reports 83.3% subtask completion, 70.9% task success and 31% lower latency than sequential execution.
- Main evaluation is Windows/Linux/A100 rather than Android.
- Persistent shared cross-device Agent memory remains future work.
- Strong C-class baseline; no phone CPU residual.

See [deep.md](deep.md).
