+++
id = "PAPER-034"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
deep_review_protocol = "EDP_V1"
deep_review_date = "2026-10-07"
decision_critical = true
decision_use = "B_RESIDUAL_SEMANTIC_PROVENANCE_VALIDITY_CONTROL_PLANE_BASELINE"
independence_assessment = "EARLY_SINGLE_AUTHOR_PREPRINT_EXECUTABLE_PROTOTYPE_NO_PHONE"
title = "PLACEMEM: Toward a Compute-Aware Memory Plane for Lifelong Agents"
primary_url = "https://arxiv.org/abs/2607.04089"
priority = "P1"
evidence_role = "semantic provenance/validity bound to reusable runtime artifacts"
authors = ["Sukanta Ganguly"]
venue = "arXiv preprint · 2026"
+++

# PAPER-034 — PLACEMEM

## 30-second read
- Proposes versioned capsules that unify semantics, provenance, validity and reusable runtime state under one correction-aware identity.
- Executable vLLM-first control-plane prototype with persistent capsule state, concurrency-safe invalidation, routing sidecar and typed metadata.
- Capsules drive text retrieval, KV-aware routing and cascading invalidation over live backends.
- Deeper layer-frontier replay is explicitly future work, not a claimed implemented feature.
- Strong evidence that cross-layer semantic validity/provenance can be represented in software.
- Early prototype, single-author preprint, no phone evidence.

See [deep.md](deep.md).
