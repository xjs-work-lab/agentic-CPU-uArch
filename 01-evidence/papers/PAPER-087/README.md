+++
id = "PAPER-087"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
decision_use = "AGENT_NATIVE_WORKLOAD_EVIDENCE"
independence_assessment = "PEER_REVIEWED_MOBILE_AGENT_BENCHMARK"
title = "ProactiveMobile: A Comprehensive Benchmark for Boosting Proactive Intelligence On Mobile Devices"
primary_url = "https://openaccess.thecvf.com/content/CVPR2026/html/Kong_ProactiveMobile_A_Comprehensive_Benchmark_for_Boosting_Proactive_Intelligence_On_Mobile_CVPR_2026_paper.html"
priority = "P0"
evidence_role = "direct workload evidence that proactive mobile Agents must infer latent intent from continuous contextual state and explicitly decide when not to act before generating executable functions"
authors = ["Dezhi Kong", "Zhengzhao Feng", "Qiliang Liang", "Hao Wang", "Haofei Sun", "Changpeng Yang", "Yang Li", "Peng Zhou", "Shuai Nie", "Hongzhen Wang", "Linfeng Zhou", "Hao Jia", "Jiaming Xu", "Runyu Shi", "Ying Huang"]
venue = "CVPR 2026"
+++

# PAPER-087 — ProactiveMobile

## 30-second read
- **Why it matters:** Establishes proactive mobile assistance as a distinct Agent workload: infer latent user need from ongoing context, decide whether to intervene, then emit executable function calls without an explicit user request.
- **Context:** user profile, device status, world information, and behavioral trajectories (text or GUI screenshots).
- **Benchmark:** 3,660+ instances across 14 scenarios; executable function pool; one-to-many valid proactive actions; explicit Success Rate and False Trigger Rate.
- **CVPR result:** fine-tuned Qwen2.5-VL-7B reaches 20.82% success rate in the peer-reviewed version, outperforming o1 (17.02%) and GPT-5 (11.37%) in that evaluation.
- **Portfolio meaning:** provides a concrete recurring workload premise for CG-07 always-on/proactive Agent activity.
- **Boundary:** benchmark/model-capability evidence, not direct phone power/latency/duty-cycle evidence.
- **Primary source:** CVPR 2026 Open Access page.

See [deep.md](deep.md) for full Paper Insight 10Q.