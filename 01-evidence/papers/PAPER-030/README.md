+++
id = "PAPER-030"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
deep_review_protocol = "EDP_V1"
deep_review_date = "2026-10-07"
decision_critical = true
decision_use = "B_RESIDUAL_MOBILE_SEMANTIC_STATE_VALUE_AND_D0_SOFTWARE_SUFFICIENCY"
independence_assessment = "PEER_REVIEWED_MOBISYS_2026"
title = "AgentProg: Empowering Long-Horizon GUI Agents with Program-Guided Context Management"
primary_url = "https://arxiv.org/abs/2512.10371"
arxiv_id = "2512.10371"
doi = "10.1145/3745756.3809245"
priority = "P0"
evidence_role = "direct mobile semantic-state value + D0 software-sufficiency baseline"
authors = ["Shizuo Tian", "Hao Wen", "Yuxuan Chen", "Jiacheng Liu", "Shanhui Zhao", "Guohong Liu", "Ju Ren", "Yunxin Liu", "Yuanchun Li"]
venue = "MobiSys 2026"
artifact_urls = ["https://github.com/MobileLLM/AgentProg"]
+++

# PAPER-030 — AgentProg

## 30-second read
- Peer-reviewed MobiSys 2026 with public code.
- Uses a Semantic Task Program with variables/control flow plus a Global Belief State.
- Reports 78.0% AndroidWorld and 68.4% AW-Extend success.
- MobiSys review notes high latency/inference cost as a deployment concern.
- Strong proof that semantic/program state has direct mobile Agent value.
- Boundary: the value is realized at S0/S1 Agent runtime/context construction; no S2/S3 physical-state necessity is shown.
- B-residual impact: positive workload signal, negative cross-tier necessity signal.

See [deep.md](deep.md).
