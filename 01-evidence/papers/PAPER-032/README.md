+++
id = "PAPER-032"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
deep_review_protocol = "EDP_V1"
deep_review_date = "2026-10-07"
decision_critical = true
decision_use = "B_RESIDUAL_VERSIONED_AUTHORITY_AND_COMPATIBLE_STATE_INHERITANCE_BASELINE"
independence_assessment = "PREPRINT_SERVER_VLLM_NO_TARGET_PHONE"
title = "Serving a Revisable World: Versioned Execution for Interruptible Agents"
primary_url = "https://arxiv.org/abs/2610.01160"
priority = "P0"
evidence_role = "versioned execution + certified compatible-state inheritance baseline"
authors = ["Yanxin Zhang", "Rahul Sharma", "Nitin Vegesna", "Zheyu Fu", "Chang Liu", "Trivikram Krishnamurthy"]
venue = "arXiv preprint · 2026-10-01"
+++

# PAPER-032 — Serving a Revisable World

## 30-second read
- Direct Agent revision/interrupt serving system built in vLLM.
- Separates request resource ownership from execution-version authority.
- Revokes obsolete work and certifies completed state that a successor may inherit.
- Covers output publication, GPU execution, KV handoff, tiered recovery and distributed/multi-tenant serving.
- Reports median 17.1% reduction in revision→successor TTFT versus abort/cold restart.
- Strong negative pressure on broad B-residual novelty.
- Server/GPU evidence only; target-phone cross-tier residual remains open.

See [deep.md](deep.md).
