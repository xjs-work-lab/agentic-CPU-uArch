> V1 semantic source copied/repacked from frozen baseline `960abb4ef50a8f5b0bd357c067f08346025d`.
> Do not reinterpret this page as V2.2 metadata authority; the compact README owns the Source object.

# PAPER-044 — ProAgentBench: Evaluating LLM Agents for Proactive Assistance with Real-World Data

## Source
- Paper: https://arxiv.org/abs/2602.04482
- Authors: Yuanbo Tang, Huaze Tang, Tingyu Cao, Lam Nguyen, Anping Zhang, Xinwen Cao, Chunkang Liu, Wenbo Ding, Yang Li
- Venue/status: arXiv preprint, 2026
- Public dataset: https://huggingface.co/datasets/qv9n2xk7m1z8pt4/ProAgentBench
- Project relevance: A / strong B4 learned-history baseline / real workload timing prior
- Priority: P0

## Q1 — What problem is the paper solving, and how does it map to smartphones?
Proactive Agents need two abilities:
1. decide **when** the user needs assistance;
2. infer **how** to assist.

Prior proactive benchmarks rely heavily on synthetic/isolated tasks and often miss the behavioral history preceding a need.

ProAgentBench uses continuous real-world workflows, making it highly relevant to our question of whether demand can be inferred from generic history.

It is primarily desktop/workstation data, so the transfer to smartphone CPU/system behavior remains unproven.

## Q2 — Is the problem/new mechanism actually new?
Real continuous pre-assistance history is a major advance over synthetic isolated proactive examples.

For our project this is not an A mechanism.
It is a **strong competing baseline source**:
generic behavioral history can encode much of the information A might otherwise claim as privileged.

## Q3 — What falsifiable hypothesis is being tested?
Author hypothesis:
long real behavioral history and real-world training improve proactive timing/content prediction more than short/synthetic context.

Project hypothesis:
if B4 can infer assistance demand accurately from ordinary history, explicit Agent DemandState may have less incremental value.

The falsifier for A is not high classifier accuracy alone; it is B4 capturing nearly all B5-to-B4 end-outcome headroom.

## Q4 — What is the research lineage / competing route?
- synthetic proactive benchmarks;
- THUNLP ProactiveAgent/ProactiveBench;
- LLM/VLM prompt-based triggering;
- RAG/KG/memory approaches;
- real-world SFT/LoRA.

## Q5 — What is the key technical mechanism / control point?
The benchmark decomposes:
- **When to Assist** — binary timing prediction from historical observations/user context;
- **How to Assist** — intent/content generation after the trigger.

For our project, When-to-Assist is the relevant B4 proxy.

The control point is an Agent-side learned trigger, not CPU/uArch.

## Q6 — How is the experiment designed?
Reported dataset:
- **28,000+ events**;
- **500+ hours** of real user sessions;
- burstiness **B=0.787**;
- 17 participants in the released study.

Context-window ablation tests:
- 10 s;
- 30 s;
- 1 min;
- 2 min;
- 5 min;
- 10 min.

Longer history generally improves proactive prediction; benefits become small beyond roughly 5 minutes.

Real-world vs synthetic training is compared at equal data scale.

Key reported When-to-Assist results:

### LLaMA-3.1-8B-Instruct
- zero-shot accuracy: 57.3%, F1 66.7%;
- SFT synthetic: 62.1%, F1 70.2%;
- **SFT real-world: 74.0%, F1 78.5%**.

### Qwen3-VL-8B-Instruct
- zero-shot accuracy: 51.7%, F1 66.1%;
- SFT synthetic: 54.8%, F1 67.8%;
- **SFT real-world: 63.5%, F1 72.4%**.

## Q7 — What data/artifact/reproducibility support exists?
Strong for workload characterization.

Public participant JSON includes:
- event identity;
- start/end timestamp;
- LLM-event label;
- application/window;
- event summary;
- screenshot reference/timestamp.

Stage 15 directly parsed a small non-random set of public participants and confirmed:
- large user/session variation in LLM-event fraction;
- contiguous LLM-event bursts;
- timestamped workflow structure.

Data caveats:
- event summaries are model-generated and may contain noise;
- event durations can include long inactivity/session gaps;
- wall-clock duration is not CPU/NPU active cost.

## Q8 — Do the results actually support the hypothesis?
Yes, for generic proactive prediction.

**[FACT]** Real-world training materially improves When-to-Assist accuracy relative to zero-shot and synthetic training.

**[FACT]** Longer history improves prediction.

**[INFERENCE]** Our previous B4 can no longer be represented by a shallow recent-history predictor only.

**Boundary:** When-to-Assist is not the same as REQUIRED/OPTIONAL/SPECULATIVE continuation demand and says nothing about Effect/Commit legality.

## Q9 — What is the real contribution / technology control point for us?
This paper materially **hardens Candidate A's competitor**.

New requirement:
B4 must permit:
- long behavioral history;
- real-world training;
- learned timing prediction;
- ordinary user/workload personalization where legal.

A's surviving residual becomes narrower:

> Does explicit Agent runtime knowledge of active goal closure, speculative branch status and effect/commit legality provide >=~5% useful-progress/end-outcome gain after a strong long-history generic predictor?

This is a better and more defensible research question.

## Q10 — What should we do next?
- UPGRADE to P0 because it changes A's promotion gate.
- Define B4-L2/L3 with ~5-minute history and real-world training.
- Use public event timing only after sessionization/outlier handling.
- Build participant/session holdouts.
- Measure calibration and cost-weighted errors, not accuracy only.
- Do not use LLM-event labels as DemandState.
- Require real phone trace for CPU/NPU/energy and in-flight cancelability.

## Decision footer
- **Evidence maturity:** STRUCTURAL_SIGNAL / real-workload evidence for B4; not mobile SYSTEM_VALUE
- **Decision impact:** HARDEN B4; KEEP A but raise proof bar
- **Open questions:** smartphone transfer; cost weighting; DemandState residual after B4-L3
- **Primary source:** https://arxiv.org/abs/2602.04482
- **Dataset:** https://huggingface.co/datasets/qv9n2xk7m1z8pt4/ProAgentBench
