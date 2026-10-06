> V1 semantic source copied/repacked from frozen baseline `960abb4ef50f050da3c6784d30826053d42e5c5d`.

# PAPER-031 — CacheScout: Learning Agent Execution for KV-Cache Management in Agentic Serving

## Source
- Paper: https://arxiv.org/abs/2608.14624
- Authors: Rui Zhang, Chaeeun Kim, Shaoting Feng, Kuntai Du, Yuhan Liu, Yi Zhong, Cheng-Wei Ching, Junchen Jiang, Liting Hu
- Venue/status: arXiv preprint, 2026
- Target: server multi-Agent LLM serving
- Project relevance: Candidate B strongest history-only baseline
- Priority: P0

## Q1 — Problem + target mapping
Agent KV anchors are often evicted between dynamic Agent invocations because generic recency policies do not predict future Agent reuse.

## Q2 — Novelty / new-regime relevance
CacheScout learns Agent execution online using a first-order transition model rather than requiring explicit workflow DAGs or semantic annotations.

## Q3 — Falsifiable hypothesis
A lightweight history-only execution model is sufficient to predict enough near-term Agent reuse to outperform reactive cache policies.

## Q4 — Competing route
This is a direct competitor to Candidate B's explicit semantic StateAffinity/ReuseHint story and pressures richer PBKV-style predictors.

## Q5 — Mechanism
- identify current Agent from prompt-prefix fingerprint;
- update first-order transition counts online;
- derive survival probability;
- combine with recency/reconstruction cost;
- predictive eviction + background prefetch.

No explicit Agent semantic state contract is required.

## Q6 — Experiment
The paper reports across representative real-world multi-Agent workloads:
- +10–18 percentage points KV hit rate;
- 18–45% lower mean TTFT;
- 29–38% lower mean per-turn latency;
- up to 57% higher peak throughput.

Mechanism ablation reports predictive eviction as the dominant source of gain.

## Q7 — Artifact
Public paper; artifact status should be verified before reproduction.

## Q8 — Evidence vs hypothesis
**[FACT]** History-only online transition learning captures substantial Agent state-reuse value.

**[INFERENCE]** Explicit S0/S1 semantic reuse hints face a high B4 bar. They need to beat CacheScout-like learned execution structure, not LRU.

## Q9 — Project contribution
This materially weakens Candidate B's previous StateAffinity / ReuseHorizon thesis.

Future-reuse prediction alone is not a strong differentiated control point.

## Q10 — Next action
- Promote to P0 baseline.
- Put CacheScout-like online predictor into B4.
- Kill explicit ReuseHint if it cannot add >=~5% meaningful value above this baseline.

## Decision footer
- Evidence maturity: SYSTEM_VALUE for server Agent KV management; STRUCTURAL_SIGNAL for mobile transfer
- Decision impact: DOWNGRADE reuse-prediction part of B
- Open questions: smartphone transfer; artifact
- Primary source: https://arxiv.org/abs/2608.14624
