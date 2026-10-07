+++
id = "PAPER-040"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
independence_assessment = "INDEPENDENT_GROUP"
title = "PhoneHarness: Harnessing Phone-Use Agents through Mixed GUI, CLI, and Tool Actions"
primary_url = "https://arxiv.org/abs/2606.14832"
priority = "P0"
evidence_role = "mixed phone-action harness + trace/verifier platform evidence"
review_depth = "FULL_10Q"
deep_review_protocol = "EDP_V1"
deep_review_date = "2026-10-07"
decision_critical = true
authors = ["Chenxin Li", "Zhengyao Fang", "Zhengyang Tang", "Pengyuan Lyu", "Xingran Zhou", "Xin Lai", "Fei Tang", "Liang Wu", "Yiduo Guo", "Weinong Wang", "Junyi Li", "Yi Zhang", "Yang Ding", "Huawen Shen", "Sunqi Fan", "Shangpin Peng", "Zheng Ruan", "Anran Zhang", "Benyou Wang", "Chengquan Zhang", "Han Hu"]
venue = "arXiv preprint · 2026"
+++

# PAPER-040 — PhoneHarness

## 30-second read
- A phone-agent harness combining device-side CLI, delegated GUI control and host-side MCP-style tools, with trace-backed task verification.
- 124-task scored split: 75.0% overall vs 62.1% Seed2.0-Pro and 62.1% MobileClaw; strongest gains are device/system and tool-assisted tasks, not single-app GUI.
- Current reproducible reference uses Android emulator + Termux/ADB and remote/host proxies; some capabilities are not purely on-device.
- The paper supports mixed-action orchestration and verifiable outcomes, but does **not isolate verification as the sole cause** of the gain.
- Primary source: https://arxiv.org/abs/2606.14832

See [deep.md](deep.md) for EDP v1 FULL_10Q.
