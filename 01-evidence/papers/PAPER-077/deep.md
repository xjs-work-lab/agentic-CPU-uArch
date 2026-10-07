# PAPER-077 — MemArena: An Ego-Centric Benchmark for On-Device Agentic Personal Memory Assistants at Scale

## Source
- arXiv:2608.02613, 2026 preprint
- Authors: Jiadong Zhang, Xiaosong Ma — MBZUAI
- Evaluation hardware for latency/power: NVIDIA Spark GB10, 128 GB unified memory, SGLang, concurrency=1
- Dataset: MemArena-L

## Q1 — Problem + target mapping
Personal Agents need dense, ego-centric, multi-session memory with provenance and privacy boundaries.

Most existing memory benchmarks under-test:
- realistic activity density;
- partial/ego-centric visibility;
- coherent multi-session worlds;
- permission-aware disclosure.

Project mapping:
MemArena is useful because it measures both **memory-backend quality** and **systems cost** under a long-horizon personal-memory workload.

## Q2 — Novelty / new-regime relevance
MemArena simulates one coherent social world with:
- 50 agents;
- 15 days;
- 10.3M dialog-text tokens;
- ~24.1K text-only ego-observed tokens per agent per day;
- 1,579 evaluation instances.

It evaluates five readers × five memory backends across recall, reasoning and trustworthiness.

New-regime classification:
**DIRECT_AGENTIC personal-memory workload benchmark**, but hardware evaluation is edge-node rather than phone.

## Q3 — Falsifiable hypothesis
Two relevant hypotheses:

1. Memory-backend design can matter more than reader scaling for long-horizon personal-memory accuracy.
2. Memory search itself may be a modest systems cost compared with reader inference, while structured-memory ingest may incur substantial background energy.

The reported results support both on the evaluated platform.

## Q4 — Research lineage / competing route
Backends:
- Vanilla context;
- BM25-RAG;
- Oracle retrieval (diagnostic only);
- Memobase;
- MemSearch (markdown + Milvus-Lite hybrid index).

Readers:
- Qwen3-0.6B;
- Qwen3-8B;
- Qwen3-32B-AWQ;
- Llama-3.2-3B;
- Mistral-7B-Instruct-v0.3.

Important project comparator:
MUSE measures phone-side retrieval/insertion/index maintenance.
MemArena measures dense personal-memory reader/backend behavior and ingest energy on edge hardware.

## Q5 — Key mechanism / control point
MemArena itself is a benchmark, not a new execution substrate.

Systems insight comes from separating phases:
- **ingest / structure extraction**;
- **search / retrieval**;
- **reader prefill/inference**.

That phase decomposition is highly relevant to H-PAM because it tests whether foreground recall or background memory construction is the expensive part.

## Q6 — Experiment design
Main grid:
- five readers × five backends;
- n=3 seeds for accuracy;
- 15-day MemArena-L history.

### Accuracy
At Qwen3-0.6B:
- Memobase → MemSearch: Recall +32.5 pp, Reasoning +19.2 pp.

Reader scaling under MemSearch from Qwen3-0.6B → Qwen3-32B-AWQ:
- Recall +10.6 pp;
- Reasoning +6.8 pp.

Thus backend architecture affects content performance materially.

### Query-time latency
Spark GB10:
- BM25-RAG search: ~87 ms;
- Memobase: ~7 ms;
- MemSearch: ~48 ms.

Only Qwen3-0.6B + slowest BM25 case makes search ~54% of a 161 ms TTFT.
For a much larger Qwen3-32B-AWQ reader, BM25 adds only ~3.4% TTFT.

### Ingest energy
Structured-memory backends run extractor-LLM calls during ingest.
For a 15-day Memobase cache, reported energy spans roughly:
- **52 kJ** with Qwen3-0.6B-scale extraction;
- up to **1,222 kJ** with Qwen3-32B-AWQ-scale extraction.

This is a crucial phase asymmetry: low query latency can hide high background ingest cost.

## Q7 — Data / artifact / reproducibility
Strengths:
- dense workload model;
- reader/backend factorial design;
- latency/power measurement on real edge AI hardware;
- explicit separation of ingest vs search vs inference;
- permission-aware evaluation.

Limitations:
- preprint;
- benchmark world is simulated, not months of real phone traces;
- GB10 is not a smartphone SoC;
- 128 GB unified memory changes capacity pressure;
- code/data promised upon acceptance, not necessarily fully released at review time;
- ingest-energy comparison depends on extractor model choice.

## Q8 — Evidence vs hypothesis
### [FACT]
On the evaluated edge platform, search overhead is fixed/moderate and usually small relative to reader inference except with very small readers.

### [FACT]
Structured-memory ingest can consume large cumulative energy due to extractor-LLM calls.

### [OBSERVATION]
Persistent-memory cost is phase-asymmetric: **ingest/maintenance may matter more than query search**.

### [INFERENCE — project]
If this asymmetry transfers to phones, the interesting systems question is background memory construction/maintenance coexistence with foreground QoE—not a generic recall fast path.

### Not established
- smartphone transfer;
- battery impact on target phone;
- CPU/NPU mapping;
- that Agent semantics beyond ordinary phase identity are needed for scheduling.

## Q9 — Real contribution to project decision
### H-PAM
Narrows the only plausible residual toward background ingest/maintenance.

But it also weakens broad H-PAM:
- query-time search is not generally dominant;
- ingest cost comes substantially from extractor model inference, a recognizable workload phase;
- MUSE already provides phone-side scheduling for insertion/index maintenance.

Thus H-PAM needs an Agent-specific fact beyond `foreground query` vs `background ingest` to remain distinct.

### CG-06 / C
Expensive extractor inference may interact with existing heterogeneous inference/control lanes rather than require a memory-specific Direction.

## Q10 — Next action
1. KEEP as P0 phase-cost evidence.
2. Add a Claim distinguishing query-light vs ingest-heavy memory phases.
3. Require smartphone transfer before any SYSTEM_VALUE promotion.
4. Compare background-ingest control against MUSE and generic mobile sensing/resource scheduling.

## Decision footer
- **Evidence maturity:** SYSTEM_VALUE on evaluated edge node; STRUCTURAL_SIGNAL for smartphone transfer
- **Decision impact:** strongly narrows H-PAM toward background ingest, not query fast path
- **Open questions:** phone energy transfer, ingest duty cycle, extractor placement, foreground interference
- **Primary source:** https://arxiv.org/abs/2608.02613