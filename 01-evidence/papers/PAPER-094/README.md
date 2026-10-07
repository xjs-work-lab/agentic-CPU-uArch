+++
id = "PAPER-094"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
decision_use = "ADAPTER_LIFECYCLE_SOFTWARE_BASELINE"
independence_assessment = "PEER_REVIEWED_ACL_LONG"
title = "K-Merge: Online Continual Merging of Adapters for On-device Large Language Models"
primary_url = "https://aclanthology.org/2026.acl-long.137/"
priority = "P1"
evidence_role = "software baseline for continually evolving on-device LoRA collections under storage and compute constraints"
authors = ["Donald Shenaj", "Ondrej Bohdal", "Taha Ceritli", "Mete Ozay", "Pietro Zanuttigh", "Umberto Michieli"]
venue = "ACL 2026 Long Papers"
+++

# PAPER-094 — K-Merge

## 30-second read
- **Why it matters:** demonstrates that an evolving on-device adapter set can be managed as a lightweight software lifecycle problem rather than requiring new lower-layer state.
- **Mechanism:** data-free similarity-based adapter assignment plus history-aware online merging under a fixed adapter-slot budget.
- **Use case:** new single-task LoRAs arrive incrementally; device must preserve prior capabilities without keeping every adapter.
- **Boundary:** incoming adapters are already trained; this is not live on-device learning from Agent interactions and does not evaluate serving/training interference.
- **H-CAL meaning:** raises the software baseline for adapter lifecycle/version population management.

See [deep.md](deep.md) for full Paper Insight 10Q.
