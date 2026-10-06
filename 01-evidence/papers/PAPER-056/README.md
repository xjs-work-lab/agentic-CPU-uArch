+++
id = "PAPER-056"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
independence_assessment = "UNKNOWN"
title = "AgentProg: Empowering Long-Horizon GUI Agents with Program-Guided Context Management"
primary_url = "https://doi.org/10.1145/3745756.3809245"
priority = "P0"
evidence_role = "direct long-horizon mobile GUI Agent workload and explicit semantic execution-state/context-management evidence"
authors = ["Shizuo Tian", "Hao Wen", "Yuxuan Chen", "Jiacheng Liu", "Shanhui Zhao", "Guohong Liu", "Ju Ren", "Yunxin Liu", "Yuanchun Li"]
venue = "ACM MobiSys 2026"
+++

# PAPER-056 — AgentProg

## 30-second read
- **Why it matters:** Long-horizon mobile GUI Agents expose context/state-management behavior that ordinary chat-style LLM workloads do not.
- **What it establishes:** Program-like control/data-flow structure, explicit variables and an execution tree can improve long-horizon mobile Agent task completion in the evaluated benchmarks.
- **Reported anchors:** 78.0% success on AndroidWorld and 68.4% on AW-Extend; removal of the execution tree was reported to reduce AW-Extend performance to 39.5%.
- **Portfolio pressure:** Strengthens the thesis that Agent execution carries useful semantic state, while also showing that much of the value can live in software/runtime representations.
- **Boundary:** High inference cost remains a practical concern; does not establish CPU/uArch residual.
- **Primary source:** https://doi.org/10.1145/3745756.3809245
