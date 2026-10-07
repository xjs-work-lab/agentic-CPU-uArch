# PAPER-114 — MARS — FULL_10Q

## Q1 — Problem + target mapping
MARS studies multi-round Agent sessions where GPU inference repeatedly hands off to CPU tools.

The core problem is coupled pressure across:
- GPU compute;
- KV cache capacity;
- CPU tool service;
- repeated suspend/resume boundaries.

Target mapping:
AO-1 Execution Fabric and AO-3 State/Context Fabric.

## Q2 — New-regime relevance
Agent-native / Agent-amplified.

The temporal shift is from one continuous inference to multiple short inference rounds separated by tools.
The spatial shift is from GPU-centric service to coupled CPU-GPU execution.

## Q3 — Falsifiable hypothesis
If token throughput and an Agent-aware GPU scheduler are sufficient, a cross-plane control stream and joint CPU/KV admission control should add little.

MARS reports substantial gains over FCFS, Autellix, InferCept and Continuum-family baselines.

## Q4 — Strongest baseline
Compared against:
- vLLM FCFS;
- Autellix program-level scheduling;
- InferCept cache management;
- Continuum and Continuum-Dynamic phase-aware KV management.

This is a strong software baseline family.

## Q5 — Mechanism / control point
Unified Information Stream:
- gpu_submit / projected KV;
- gpu_first_token / launch delay;
- gpu_end / freed blocks;
- tool count;
- tool start/end and duration;
- stable per-session identifiers.

External control plane:
- pressure-aware queue packing;
- CPU and KV-aware admission limits;
- AIMD adaptation;
- decoupled ordering and admission.

Internal Agent-centric scheduler:
- multi-level feedback priority;
- priority-aligned KV eviction;
- fine-grained prefill chunk shrinking;
- bounded KV pinning for warm tool returns;
- progress-oriented scheduling.

## Q6 — Experiment design + results
Hardware:
- H200 NVL with dual AMD EPYC 9355 and 1.5 TB memory;
- H100 NVL node;
- one GPU per run.

Models:
- Qwen3-Coder-30B-A3B-Instruct;
- GPT-OSS-120B.

Workloads:
- SWE-bench;
- GitTaskBench;
- Terminal-Bench;
- RepoBench;
- InfinityBench;
- OpenHands full deployment.

Reported:
- controlled H100/Qwen mean latency: 1.44–5.80x better than strongest baseline across tested points;
- paper headline up to 5.94x mean E2E reduction across workloads;
- OpenHands end-to-end task completion: 1.20–1.87x faster than strongest baseline;
- OpenHands P90 up to 1.34x and P95 up to 1.28x.

Ablations:
- remove priority coordinator: roughly 2–5x mean-latency inflation;
- remove external control plane: roughly 1.5–3x slowdown under high contention;
- remove opportunistic co-scheduler: roughly 1.5–2x slowdown in memory-constrained heavy regimes;
- one low-load regime shows opportunistic-management overhead can outweigh benefit.

## Q7 — Artifact / limitations
Source code is publicly linked by the paper.

Limits:
- datacenter GPU/CPU;
- coding-agent workloads;
- one-GPU node-local control;
- CPU and GPU tool/inference cores are deliberately separated;
- no phone energy/thermal/foreground-QoE;
- fairness is not the main objective;
- multi-GPU migration remains future work.

## Q8 — Evidence vs hypothesis
FACT:
phase-boundary visibility plus coordinated admission/scheduling/KV policy matters.

FACT:
software alone can exploit a small set of cross-layer events to recover large system value.

FACT:
warm-state retention is valuable only when resumption benefit exceeds residency opportunity cost.

NOT ESTABLISHED:
mobile transfer or hardware necessity.

## Q9 — Decision contribution
MARS is a strong UNDERCUT against broad claims that Agentic heterogeneity automatically requires new hardware.

At the same time, it supports AO-1 because it shows the control problem spans CPU tools, accelerator execution and state residency.

The architectural question shifts to whether mobile hardware/software interfaces expose these states cheaply enough.

## Q10 — Next action
Use as AO-1 strongest software baseline.
Search for:
- mobile equivalents;
- cross-xPU queue/state visibility cost;
- hardware events unavailable to software at useful timescales;
- shared-memory contention and state handoff.

## Decision footer
- Evidence maturity: SYSTEM_VALUE on server
- Decision impact: strengthen AO-1 problem while strongly narrowing hardware claims
- Open questions: mobile transfer, observability overhead, hardware-visible state
- Primary source: https://arxiv.org/abs/2604.26963
