+++
id = "PAPER-105"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
deep_review_protocol = "EDP_V1"
deep_review_date = "2026-10-07"
decision_critical = true
decision_use = "T3_VERIFIED_ACTUATION_PRODUCT_SIGNAL_AND_T7_FINAL_OWNERSHIP"
independence_assessment = "INDEPENDENT_AAAI_2026_MOBILE_AGENT_LINEAGE"
title = "EcoAgent: An Efficient Device-Cloud Collaborative Multi-Agent Framework for Mobile Automation"
primary_url = "https://ojs.aaai.org/index.php/AAAI/article/view/40230"
priority = "P0"
evidence_role = "peer-reviewed mobile multi-agent architecture with device-side execution/verification, closed-loop feedback and communication compression"
authors = ["Biao Yi", "Xueyu Hu", "Yurun Chen", "Shengyu Zhang", "Hongxia Yang", "Fan Wu"]
venue = "AAAI 2026, Proceedings of the AAAI Conference on Artificial Intelligence, 40(35), 29838-29846"
artifact_urls = ["https://github.com/Yi-Biao/EcoAgent"]
+++

# PAPER-105 — EcoAgent

## 30-second read
- **Peer reviewed:** AAAI 2026.
- **Architecture:** cloud Planning Agent + device-side Execution Agent + device-side Observation Agent.
- **Closed loop:** each action is checked against an expected effect; failure triggers cloud reflection/replanning.
- **Ablation:** ShowUI 7.0% SR → +Planner 15.5% → +Observer 25.6%; OS-Atlas 4.3% → 19.0% → 27.6%.
- **Cloud-cost reduction:** EcoAgent(OS-Atlas) averages 1.53 cloud MLLM calls / 3240 tokens per task versus M3A 13.39 / 87469.
- **Latency:** EcoAgent(ShowUI) 3.9 s/step vs M3A 15.3 s in the reported comparison.
- **Communication:** 120 kB uplink/task vs AppAgent 2098 kB and M3A 5831 kB.
- **Important boundary:** the “device-side” 2B–4B models were deployed on an RTX 3090 24 GB local server to simulate mobile inference; AndroidWorld used a Pixel 6 / Android 13 emulator.
- **T3 impact:** strengthens verified/closed-loop actuation as a product pattern.
- **T7 impact:** multi-Agent benefit is role decomposition + feedback + communication placement; no local shared-resource CPU/NPU residual is isolated.
- **Counter-evidence:** EcoAgent SR 25.6–27.6% is near M3A 28.4%, but trails Agent S2 54.3% and V-Droid 59.5%; it is not a best-success-rate system.

See [deep.md](deep.md) for the FULL_10Q decision card.
