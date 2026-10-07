+++
id = "PAPER-095"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
decision_use = "MOBILE_LORA_KV_SOFTWARE_BASELINE"
independence_assessment = "PEER_REVIEWED_ACL_LONG_INDUSTRY_COAUTHOR"
title = "MobiLoRA: Accelerating LoRA-based LLM Inference on Mobile Devices via Context-aware KV Cache Optimization"
primary_url = "https://aclanthology.org/2025.acl-long.1140/"
priority = "P0"
evidence_role = "direct mobile LoRA-serving baseline for cross-adapter KV reuse, cache compression and application-lifecycle-aware retention/eviction"
authors = ["Borui Li", "Yitao Wang", "Haoran Ma", "Ligeng Chen", "Jun Xiao", "Shuai Wang"]
venue = "ACL 2025 Long Papers"
+++

# PAPER-095 — MobiLoRA

## 30-second read
- **Why it matters:** directly attacks LoRA-specific KV-cache pressure on mobile devices.
- **Mechanism:** CtxAttention + cross-adapter similarity-aware delta encoding + application-state-aware cache management.
- **Mobile context:** cache policy uses foreground/background/killed application state, not only LRU.
- **Reported result:** 18.1%–81.3% TTFT acceleration across evaluated mobile workloads/traces.
- **H-CAL meaning:** strongly narrows any claim that adapter identity + KV retention/locality needs a new hardware control point.

See [deep.md](deep.md) for full Paper Insight 10Q.
