+++
id = "PAPER-074"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
decision_use = "DECISION_GRADE_WITH_SCOPE_BOUNDARY"
independence_assessment = "INDEPENDENT_PEER_REVIEWED_AGENT_NATIVE"
title = "Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents"
primary_url = "https://aclanthology.org/2026.acl-long.981/"
priority = "P0"
evidence_role = "independent recurrence evidence for explicit Agent memory lifecycle operations learned as policy actions: add/update/delete/retrieve/summary/filter"
authors = ["Yi Yu", "Liuyi Yao", "Yuexiang Xie", "Qingquan Tan", "Jiaqi Feng", "Yaliang Li", "Libing Wu"]
venue = "ACL 2026 Long Paper"
+++

# PAPER-074 — AgeMem

## 30-second read
- **Why it matters:** Independently confirms that memory operations are recurring Agent actions rather than a MobiMem-specific software decomposition.
- **What it establishes:** AgeMem exposes LTM `ADD/UPDATE/DELETE` and STM `RETRIEVE/SUMMARY/FILTER` as tool actions inside the Agent policy and trains the Agent to decide when to invoke them.
- **Reported anchors:** average scores 41.96 and 54.31 on five benchmarks with Qwen2.5-7B/Qwen3-4B; +4.82 and +8.57 percentage points over best compared memory baselines; Memory Quality 0.533/0.605; STM tools reduce prompt tokens by ~3.1%/5.1% vs its RAG variants.
- **Operation evidence:** RL increases `ADD`/`UPDATE` use, introduces non-zero `DELETE`, and makes retrieval more selective, showing the lifecycle policy is adaptive rather than a fixed API sequence.
- **Portfolio meaning:** passes H-PAM's cross-framework recurrence test for lifecycle semantics, but provides no phone/system-cost evidence.
- **Boundary:** Agent reasoning/memory-management paper; no CPU/NPU/DRAM/thermal or mobile systems evaluation.
- **Primary source:** https://aclanthology.org/2026.acl-long.981/
- **Artifact:** https://github.com/y1y5/AgeMem

See [deep.md](deep.md) for full Paper Insight 10Q.