+++
id = "PAPER-058"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
decision_use = "DECISION_GRADE_WITH_SCOPE_BOUNDARY"
independence_assessment = "GROUP_OVERLAP_WITH_PAPER_056"
title = "AutoDroid-V2: Boosting SLM-based GUI Agents via Code Generation"
primary_url = "https://doi.org/10.1145/3711875.3729134"
priority = "P0"
evidence_role = "direct smartphone on-device GUI-Agent software-baseline evidence; task-level script lowering, app-document reuse and local SLM execution"
authors = ["Hao Wen", "Shizuo Tian", "Borislav Pavlov", "Wenjie Du", "Yixuan Li", "Ge Chang", "Shanhui Zhao", "Jiacheng Liu", "Yunxin Liu", "Ya-Qin Zhang", "Yuanchun Li"]
venue = "ACM MobiSys 2025"
+++

# PAPER-058 — AutoDroid-V2

## 30-second read
- **Why it matters:** Directly attacks the cost of step-wise mobile GUI Agents by lowering a user task into one multi-step executable script.
- **What it establishes:** On the evaluated Snapdragon 8 Gen2 phone, task-level script generation plus app documentation/prefix reuse can dramatically reduce model-query, token and inference cost while improving task success.
- **Reported anchors:** 46.3 s/task vs 669.2 s/task for step-wise AutoDroid on Snapdragon 8 Gen2; 97.8% fewer uncached input tokens and 85.2% fewer output tokens; 47.1% success on the evaluated AitW subset vs 36.7% AutoDroid with the same Llama-3.1-8B-ft family.
- **Portfolio meaning:** Strong software-only semantic-lowering baseline. It narrows any broad H-SCL/A claim that program/task semantics must be consumed by lower layers.
- **Boundary:** Highly dynamic/unstructured UIs can force replanning and erode the efficiency advantage; no CPU/uArch necessity is established.
- **Primary source:** https://doi.org/10.1145/3711875.3729134
- **Artifact:** https://github.com/MobileLLM/AutoDroid-V2

See [deep.md](deep.md) for the full Paper Insight 10Q.
