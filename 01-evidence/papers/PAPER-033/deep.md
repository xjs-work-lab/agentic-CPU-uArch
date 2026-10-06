> V1 semantic source copied/repacked from frozen baseline `960abb4ef50f050da3c6784d30826053d42e5c5d`.

# PAPER-033 — LOCAL: Enabling Learning On-device Contiguously for Agent LLMs

## Source
- Paper: https://arxiv.org/abs/2608.15241
- Authors: Xinxin Liu, Jiaxin Li, Zibo Wang, Yun Ji, Zhangqi Zhu, Qing Hu, Zhibin Wang, Rong Gu, Sheng Zhong, Chen Tian
- Venue/status: arXiv preprint, 2026
- Evaluation platform: single 24 GB GPU; not smartphone despite on-device/local framing
- Project relevance: Candidate B version-aware KV state; C/A shared-resource control
- Priority: P0

## Q1 — Problem
Continual local adaptation changes adapter versions while foreground Agent inference and KV reuse continue on the same device.

## Q2 — New-regime relevance
Adapter updates make previously valid KV state stale even when token prefixes match.

The paper treats adapter version, task priority and KV-cache validity as one coupled runtime problem.

## Q3 — Falsifiable hypothesis
Version-aware KV management plus cooperative scheduling can maintain foreground responsiveness and background learning while avoiding stale KV reuse.

## Q4 — Competing route
Direct pressure on Candidate B's version-aware state-management residual.

## Q5 — Mechanism
- version-aware KV manager;
- agent-scoped KV identity;
- stale-coverage prefill;
- cross-Agent pre-prefill;
- memory-pressure offload;
- cooperative scheduler.

## Q6 — Experiment
Reported:
- 3.1x lower foreground queue-wait p95 vs FIFO;
- 1.55x lower p95 TTFT vs non-preemptible training;
- 25.6% lower post-publish first-hit prefill p99;
- 21.9% lower cross-Agent TTFT p99.

## Q7 — Artifact
Public arXiv paper; artifact status not yet verified.

## Q8 — Evidence boundary
Despite the on-device framing, the evaluated platform is a 24 GB single-GPU system, not a smartphone NPU.

Therefore it is direct Agent runtime evidence but only indirect smartphone evidence.

## Q9 — Project contribution
Version-aware Agent KV validity and multi-Agent state preparation are already active research directions.

This further narrows B:
the residual cannot simply be version-aware KV management.

## Q10 — Next action
- KEEP as P0 B-boundary source.
- Require a smartphone-specific S0/S1→S2/S3 coherence residual.
- Do not cite LOCAL as smartphone SYSTEM_VALUE.

## Decision footer
- Evidence maturity: SYSTEM_VALUE for evaluated local single-GPU runtime; STRUCTURAL_SIGNAL for phone transfer
- Decision impact: NARROW Candidate B
- Open questions: smartphone transfer; artifact
- Primary source: https://arxiv.org/abs/2608.15241
