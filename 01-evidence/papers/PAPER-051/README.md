+++
id = "PAPER-051"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
independence_assessment = "UNKNOWN"
title = "EdgeAgent: Orchestrating On-Device LLM inference for End-User Multi-Agent Systems on CPU-GPU Unified Memory Architectures"
primary_url = "https://arxiv.org/abs/2610.03394"
priority = "P0"
evidence_role = "C system-control evidence: generic UMA/SME optimization plus incremental Agent-aware scheduling"
review_depth = "FULL_10Q"
deep_review_protocol = "EDP_V1"
deep_review_date = "2026-10-07"
decision_critical = true
origin_paths = ["03-academic/paper-10q/PAPER-051.md", "analysis/stage16a/public_evidence/README.md", "analysis/stage16a/results/pass2-public-evidence-summary.md"]
origin_blobs = ["4fae7a001ce8c3aaeceabc85205eadf2950afc6d", "21c60cd65c7148b97792a62e7570100ff5657f1e", "0e505a7589f0f6469836d1a9f0cfa6add8d69b43"]
authors = ["Yuhai Long", "Yuanxin Wei", "Kai Wu", "Jinhui Wei", "Dan Huang", "Jiangsu Du"]
venue = "ASPLOS 2027 / arXiv 2026-10-02"
+++

# PAPER-051 — EdgeAgent

## 30-second read
- EdgeAgent combines a generic UMA-aware execution layer with Agent-workload scheduling on Apple M4/M4 Pro-class hardware.
- UMA-aware SME kernels + zero-copy tensor parallelism contribute up to 1.29× over Batch-SD in the reported ablation.
- HAL-based draft-budget scheduling adds about 1.05–1.17× over the corresponding UMA-aware configuration.
- Under synthetic log-uniform tool stalls up to [1,100] s, suspend-and-yield contributes to a headline 1.77× makespan improvement in the extreme reported case.
- Boundary: Apple CPU-GPU UMA, synthetic stall injection, no smartphone/NPU transfer proof.
- Primary source: https://arxiv.org/abs/2610.03394

See [deep.md](deep.md) for EDP v1 FULL_10Q.
