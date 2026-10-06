# PAPER-059 — Fast On-device LLM Inference with NPUs (llm.npu)

## Source
- ASPLOS 2025
- DOI: https://doi.org/10.1145/3669940.3707239
- arXiv: https://arxiv.org/abs/2407.05858
- Artifact: https://doi.org/10.5281/zenodo.14392760
- Code lineage: https://github.com/UbiquitousLearning/mllm
- Devices: Xiaomi 14 / Redmi K60 Pro/K70-class Snapdragon platforms in the paper/artifact
- Models: Qwen1.5-1.8B, Gemma-2B, Phi-2-2.7B, Llama-2-7B, Mistral-7B
- Real workloads: DroidTask UI automation, LongBench context-aware email reply, Persona-Chat summary
- Priority: P0

## Q1 — Problem + target mapping
Mobile LLM prefill is often the dominant latency for Agent-relevant workloads because prompts are long and outputs are short.

The paper reports prefill shares of:
- 88.3%–98.8% on CPU for representative UI/context tasks;
- 54.2%–91.7% on GPU.

Naively offloading to mobile NPU fails because:
- prompt shapes are dynamic while NPU graphs are static;
- per-group quantization maps poorly to NPU execution;
- FP attention/norm operations remain necessary.

This is directly relevant to CG-06 because it changes the realistic NPU comparator for Agent-relevant AI stages.

## Q2 — Novelty / new-regime relevance
The paper introduces three levels of reconstruction:

1. **Prompt level — chunk-sharing graphs**
   - variable prompt → fixed chunks;
   - reuse prebuilt static graphs;
   - share prompt-size-independent operators to reduce memory.

2. **Tensor level — shadow outlier execution**
   - NPU keeps fast per-tensor INT8 MatMul;
   - sparse activation outliers are extracted to CPU/GPU in parallel.

3. **Block level — out-of-order subgraph execution**
   - CPU/GPU and NPU subgraphs are scheduled by affinity/accuracy sensitivity;
   - online scheduler prioritizes reducing NPU stalls.

Classification: **generic enabling / mobile-LLM amplified**, not Agent-native.

## Q3 — Falsifiable hypothesis
If mobile NPU constraints are treated as a graph/quantization/scheduling problem rather than a fixed hardware limitation, then software can recover high NPU utilization while retaining accuracy.

Falsifiers:
- graph preparation dominates;
- outlier residual work is too large;
- CPU/GPU/NPU synchronization erases gains;
- INT8 accuracy cannot be recovered;
- energy advantage disappears end-to-end.

The evaluated results support the hypothesis in the Qualcomm/QNN scope.

## Q4 — Research lineage / competing route
This is the direct predecessor line to PAPER-057 ShadowNPU:
- llm.npu (ASPLOS 2025): prompt/tensor/block decomposition for NPU-centric prefill;
- ShadowNPU (MobiSys 2026): further reclaims attention via low-precision importance estimation + sparse high-precision residual.

Shared authors/groups include Daliang Xu, Gang Huang, Mengwei Xu and Xuanzhe Liu ecosystem.

Therefore PAPER-059 and PAPER-057 are **lineage evidence, not independent corroboration**.

Competing routes:
- llama.cpp CPU;
- MNN CPU;
- MLC-LLM GPU;
- TFLite GPU;
- PowerInfer-V2 NPU;
- later HeteroLLM;
- CPU matrix/SME2 fast paths.

## Q5 — Key mechanism / control point
The important abstraction is:
> transform model/prompt representation so each sub-computation matches the strengths/constraints of the available engine.

This includes:
- static-shape specialization;
- quantization-role decomposition;
- selective CPU/GPU float residuals;
- out-of-order scheduling to hide accelerator bubbles.

The control point is therefore already **compiler/runtime/system graph transformation**, not simple engine selection.

## Q6 — Experiment design
Evaluated:
- five model families from 1.8B to 7B;
- four benchmark families;
- two commercial mobile devices;
- CPU, GPU and NPU baselines.

Strong baselines:
- llama.cpp;
- TFLite;
- MNN;
- MLC-LLM;
- PowerInfer-V2.

Headline:
- average prefill speedup: **22.4x**;
- average energy saving: **30.7x**;
- >1000 tokens/s prefill for billion-scale model;
- end-to-end application speedup up to **32.8x**.

For 1024-token prompts, reported gains over various CPU/GPU baselines can exceed 30x, while even PowerInfer-V2-NPU is beaten by roughly 3–5x in the reported device settings.

## Q7 — Data / artifact / reproducibility
Strengths:
- ASPLOS peer review;
- public artifact appendix;
- archived Zenodo artifact;
- public mllm code lineage;
- binary + source support;
- explicit hardware/software requirements;
- artifact evaluation instructions.

Artifact reference configuration:
- Redmi K70 Pro 24GB;
- Qwen1.5-1.8B demonstration model;
- accuracy + prefill-performance workflows;
- MIT license;
- archived artifact DOI.

This project did not independently rerun the artifact.

## Q8 — Evidence vs hypothesis
### [FACT]
On evaluated Snapdragon phones, software reconstruction makes NPU prefill materially faster and more energy efficient than multiple CPU/GPU/NPU baselines.

### [FACT]
The paper retains CPU/GPU for FP-sensitive/outlier work; it is not "all NPU".

### [OBSERVATION]
Many apparent accelerator limitations are mutable software boundaries when graph shape, quantization and execution order are redesigned.

### [INFERENCE — project]
The CPU-resident opportunity must be assessed against a **moving optimized-NPU frontier**, not against vendor-default offload.

### Not established
- Agent-semantic-aware placement;
- universal NPU dominance;
- Huawei transfer;
- decode-phase superiority;
- CPU/uArch insufficiency.

## Q9 — Real contribution to project decision
### CG-06
**Strong baseline/lineage strengthening; no score/action change.**

PAPER-059 reinforces CLM-CPU-004 and shows ShadowNPU is part of a sustained trajectory:
> optimize NPU constraints in software → progressively reclaim CPU/GPU fallback regions.

CG-06 therefore must survive:
- llm.npu-style prompt/tensor/block optimization;
- ShadowNPU-style attention decomposition;
- later HeteroLLM-style concurrent heterogeneous execution where applicable.

### C
Only contextual support. The scheduler is model/runtime-specific, not Agent-aware OS control.

### A
No direct impact.

### R3
Remain BLOCKED. Existing software/runtime techniques capture major value on existing hardware.

## Q10 — Next action
1. KEEP as P0.
2. Add as a second, group-overlapping premise for CLM-CPU-004.
3. Add PAPER-059 to EXP-CG06-001 input sources.
4. Treat llm.npu + ShadowNPU as a **research lineage** defining NPU-OPT, not as independent evidence count.
5. Deep-review HeteroLLM next only if it adds a genuinely distinct concurrent CPU/GPU/NPU mechanism or stronger matched baseline.
6. Do not change CG-06 score/action from this paper alone.

## Decision footer
- **New-regime relevance:** generic enabling / mobile-LLM amplified
- **Evidence maturity:** SYSTEM_VALUE on evaluated commercial-phone mobile-LLM workloads
- **Decision impact:** strengthen NPU-OPT baseline and lineage; no Bet promotion
- **CG-06 impact:** INVEST / 86.5 unchanged, harder comparator
- **C/A impact:** no direct promotion
- **R3 impact:** remain BLOCKED
- **Open questions:** newer NPU families, decode, matched CPU-MATRIX comparison, Huawei transfer, foreground QoE externalities
- **Primary source:** https://doi.org/10.1145/3669940.3707239
- **Artifact:** https://doi.org/10.5281/zenodo.14392760
