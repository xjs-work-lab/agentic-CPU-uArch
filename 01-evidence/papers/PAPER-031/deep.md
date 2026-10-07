# PAPER-031 — CacheScout — FULL_10Q

## Q1 — Problem
Reactive recency policies evict reusable fixed Agent prefixes between dynamic Agent invocations.

## Q2 — New-regime relevance
Agent execution has repeated transition structure that can be learned online.

## Q3 — Hypothesis
A lightweight online execution model can predict enough reuse to beat reactive cache policies without a predefined DAG or semantic contract.

## Q4 — Baseline
Standard prefix caching with recency-based replacement and other reactive Agent-serving cache policies.

## Q5 — Mechanism
- identify current Agent from prompt-prefix fingerprint;
- update first-order Agent transition counts online;
- derive reuse/survival probability;
- combine prediction with recency/reconstruction cost;
- predictive eviction;
- asynchronous/background prefetch.

No semantic ABI or offline workflow graph is required.

## Q6 — Experiment
Implemented on vLLM across representative real-world multi-Agent workloads.

Reported:
- KV hit rate +10–18 percentage points;
- mean TTFT -18–45%;
- mean per-turn latency -29–38%;
- peak throughput up to +57%;
- larger-model experiments report TTFT reduction up to 54% with 37% higher throughput.

Mechanism ablation identifies predictive eviction as a major contributor.

## Q7 — Artifact / limitations
Public paper; no official code artifact was verified in this review.
Server/vLLM setting; no phone energy/thermal/QoE or mobile memory-tier measurement.

## Q8 — Evidence
FACT: history-only online transition learning captures substantial Agent reuse value.
INFERENCE: semantic ReuseHint must show incremental value above a learned history baseline.
NOT ESTABLISHED: learned transitions capture correctness/validity after semantic revision.

## Q9 — Project decision
This materially weakens the reuse-prediction portion of B-residual.

The remaining B residual shifts toward correctness/validity information not inferable from reuse history.

## Q10 — Next
Pair this baseline with explicit version/provenance/invalidation systems before testing phone residual.

## Decision footer
- SYSTEM_VALUE for server Agent KV management
- no target-phone SYSTEM_VALUE
- no B-residual promotion
