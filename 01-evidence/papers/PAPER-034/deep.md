# PAPER-034 — PLACEMEM — FULL_10Q

## Q1 — Problem
Long-lived Agent memories may be corrected while serving systems continue to reuse runtime artifacts derived from old state.

## Q2 — Agent-specific relevance
The core issue is not merely retrieval; it is linking semantic correction to derived reusable compute state.

## Q3 — Hypothesis
A correction-aware identity that binds semantics, provenance, validity and runtime state can prevent stale reuse while preserving valid reuse.

## Q4 — Baselines
Ordinary text memory/retrieval plus serving caches that lack explicit correction/provenance linkage.

## Q5 — Mechanism
Versioned capsules include typed metadata for:
- semantic content/identity;
- provenance;
- validity/version;
- dependencies;
- reusable runtime artifacts.

The current prototype uses capsules for:
- prompt-level retrieval;
- KV-aware routing;
- cascading invalidation;
- concurrency-safe control through a vLLM-first sidecar.

## Q6 — Evaluation
The paper describes an executable prototype and benchmark harness measuring live first-token latency, reuse and post-correction behavior on streamed backends.

Important boundary:
prospective deeper layer-frontier replay is explicitly positioned as future integration, not an implemented engine feature.

## Q7 — Artifact / limitations
ArXiv v1, single author, six-page systems position/prototype.
No smartphone hardware, phone battery/thermal/QoE, or demonstrated NPU/DRAM/UFS artifact lineage.
No official GitHub artifact was verified from the paper surface during this review.

## Q8 — Evidence
FACT: semantic/provenance/validity/runtime-artifact identity can be represented in a software control plane.
INFERENCE: broad “semantic lineage contract” is no longer whitespace.
NOT ESTABLISHED: the software capsule reaches or solves phone S2/S3 physical artifacts.

## Q9 — Project decision
PLACEMEM crowds the correctness half of broad B.
B-residual must prove target-phone incremental value beyond a typed correction-aware software control plane.

## Q10 — Next
Use EXP-BR-001 to test whether phone artifacts require information that cannot be expressed in such capsule/version/provenance state.

## Decision footer
- executable software-control-plane evidence
- no target-phone SYSTEM_VALUE
- narrow B-residual
