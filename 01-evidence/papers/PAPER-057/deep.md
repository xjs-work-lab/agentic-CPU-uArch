# PAPER-057 — ShadowNPU: System and Algorithm Co-design for NPU-Centric On-Device LLM Inference

## Source
- Paper: https://arxiv.org/abs/2508.16703
- ACM DOI: https://doi.org/10.1145/3745756.3809205
- Venue: ACM MobiSys 2026
- Authors: Wangsong Yin, Daliang Xu, Mengwei Xu, Gang Huang, Xuanzhe Liu
- Institutions: Peking University + Beijing University of Posts and Telecommunications
- Artifact record: https://zenodo.org/records/19555734
- ACM artifact status: Artifacts Available + Artifacts Evaluated & Functional
- Implementation: >10k LoC C++/Python
- Main devices: Xiaomi 14 / Snapdragon 8 Gen3; Redmi K60 Champion Edition / Snapdragon 8 Gen2
- Models: Qwen2-0.5B/1.5B; PhoneLM-0.5B/1.5B
- Datasets: ArxivSum; DroidCall; Octopus
- Priority: P0

## Q1 — Problem + target mapping

### Paper problem
Mobile NPUs are efficient low-precision accelerators, but mainstream on-device LLM frameworks often keep attention on CPU/GPU because attention activations (Q/K/V) are difficult to quantize accurately under static, coarse per-tensor NPU graphs.

The paper measures an average **18 percentage-point accuracy loss** when full attention is moved directly to NPU INT8 across the evaluated models/tasks.

Therefore current systems face a trade-off:
- leave attention on CPU/GPU → preserve accuracy but consume general-purpose resources and create contention;
- move it fully to NPU → improve resource isolation/efficiency but lose accuracy.

### Project mapping
This is highly relevant to CG-06 because it directly attacks the boundary that decides which engine should execute latency-critical AI work.

However, the optimization is driven by:
- operator structure;
- numerical precision tolerance;
- NPU static-graph constraints;
- sparsity;
- pipeline economics.

Those are **generic LLM/operator properties**, not Agent-native semantics.

DroidCall and Octopus make the evaluation Agent-relevant, but the mechanism would apply even if no Agent existed.

## Q2 — Novelty / new-regime relevance

### New-regime signal
On-device LLMs stress a heterogeneous SoC regime where:
- NPU INT throughput is high but float/dynamic behavior is limited;
- CPU/GPU remain flexible but compete with user-facing workloads;
- attention contains both quantization-sensitive value computation and quantization-tolerant ranking/selection work.

### Core novelty
ShadowNPU exploits a semantic asymmetry **inside the operator**:
- estimating *which tokens matter* needs relative ranking and tolerates low-precision error;
- computing the final attention value needs high numerical fidelity.

That enables role decomposition:
- NPU: dense INT8 importance estimation;
- CPU/GPU: top-k + sparse high-precision attention on a small subset.

Additional system techniques solve NPU constraints:
- scale/shape compute-graph bucketing;
- fused NPU head launch;
- head-wise NPU↔CPU/GPU overlap;
- greedy pipeline ordering;
- head-specific sparsity.

Classification: **generic enabling / mobile-LLM amplified**, not Agent-native.

## Q3 — Falsifiable hypothesis

Core hypothesis:
> If the low-precision NPU is used only for the relative-ranking portion of attention and high-precision CPU/GPU work is restricted to a small selected token subset, then end-to-end mobile LLM inference can preserve near-full-attention accuracy while materially reducing CPU/GPU use, latency and energy.

Falsifiers:
- NPU INT8 ranking fails to recover important token positions;
- sparse high-precision residual remains too large;
- cross-engine transfer/top-k overhead dominates;
- static-graph bucketing cannot track activation range;
- pipeline overhead/bubbles erase benefit;
- accuracy degrades on information-dense mobile Agent tasks.

The evaluated results support the hypothesis in the Snapdragon scope.

## Q4 — Research lineage / competing route

### Sustained PKU/BUPT heterogeneous mobile-AI line
A key predecessor from the same author lineage is **Fast On-device LLM Inference with NPUs (llm.npu, ASPLOS 2025)**.

llm.npu already decomposes mobile LLM inference across NPU and CPU/GPU at prompt/tensor/block levels and reports large prefill/energy gains.
ShadowNPU continues that line by attacking one of the remaining CPU/GPU fallback regions: attention.

This is important for our roadmap:
> NPU software stacks are not static baselines; they are actively improving and reclaiming CPU/GPU work.

### Competing routes
- C/G-Full: full float attention on CPU/GPU;
- C/G-Sparse: token-level dynamic sparse attention on CPU/GPU;
- C/G-Block-Sparse;
- NPU-Full INT8 attention;
- llm.npu native CPU/GPU attention;
- HeteroLLM GPU/NPU partitioning;
- CPU matrix/SIMD fast paths such as SME/SME2 routes;
- better NPU quantization / compiler support.

CG-06 must compete against this moving frontier, not a fixed 'NPU cannot do attention' assumption.

## Q5 — Key mechanism / control point

### 1. Quantization-tolerant pilot compute
ShadowNPU observes that top-k position recovery tolerates low-precision fluctuations far better than the exact attention output.

Across the paper's calibration analysis, NPU INT8 prediction of important QK positions reports >99% recall for multiple models/sparsity ratios, even when full NPU attention loses substantial task accuracy.

### 2. Head-specific sparsity
Attention heads have unequal importance; the system profiles head/layer sensitivity offline and assigns different sparsity ratios.

### 3. NPU compute-graph bucketing
Because QNN-style graphs fix tensor scales/shapes offline, multiple static graphs are prebuilt and bucketed by scale/shape, then selected online.

### 4. Head-wise NPU↔CPU/GPU pipeline
The implementation overlaps:
- NPU estimation;
- CPU/GPU top-k;
- CPU/GPU sparse QKV.

Fused launches and greedy head ordering reduce NPU under-utilization/pipeline bubbles.
Reported online pipeline planning overhead is <1 ms on MI14.

### 5. Resource-isolation intent
The default experiment allows only **one middle CPU core** for residual control/sparse compute; the objective is deliberately NPU-centric.

### Project control-point interpretation
The useful abstraction is not 'CPU or NPU'. It is:
> **decompose work by numerical semantics + precision + shape/dynamism + resource externality, then place/pipeline each sub-role on the best engine.**

This strengthens our broader heterogeneous-placement model while narrowing a simplistic CPU-resident thesis.

## Q6 — Experiment design

### Devices
- MI14: Snapdragon 8 Gen3, Hexagon V75, Cortex-A720 middle core;
- Redmi K60 Champion Edition: Snapdragon 8 Gen2, Hexagon V73, Cortex-A715 middle core.

### Models
- PhoneLM 0.5B / 1.5B;
- Qwen2 0.5B / 1.5B.

### Datasets
- ArxivSum: generic comprehension/summarization;
- DroidCall: mobile GUI/intent Agent task;
- Octopus: mobile system-API function-calling Agent task.

### Baselines
All compared under fully available NPU + only one middle CPU core by default:
1. C/G-Full — lossless float full attention;
2. C/G-Sparse — dynamic token sparse attention on CPU/GPU;
3. C/G-Block-Sparse — block sparse;
4. NPU-Full — INT8 full attention with static graph;
5. additional comparison to llm.npu native multi-core CPU/GPU attention.

### Important stage boundary
ShadowAttn replaces attention for **prefill** in the end-to-end integration.
Decode still uses full attention on CPU/GPU because decode is memory-bound in the evaluated design.

This matters: the paper does not eliminate all CPU/GPU attention from all LLM phases.

## Q7 — Data / artifact / reproducibility

### Strengths
- peer-reviewed MobiSys paper;
- two commercial smartphone generations;
- multiple mobile-sized models;
- one generic + two Agent-relevant datasets;
- accuracy/latency/energy/resource sensitivity;
- explicit ablations;
- implementation details;
- artifact badges: Available and Evaluated & Functional;
- Zenodo artifact archive is public.

### Reproduction boundary
This project did not independently rerun the Qualcomm QNN/Hexagon artifact.
A GitHub repository named `shadowNPU/shadowNPU` is currently empty and should **not** be treated as the evaluated artifact; the decision-grade artifact reference is the ACM/Zenodo archive.

### Reported quantitative anchors
Accuracy average across models/datasets:
- C/G-Full: **36.8**;
- ShadowNPU: **36.4**;
- C/G-Sparse: 29.4;
- C/G-Block-Sparse: 25.4;
- NPU-Full: 18.8.

Latency:
- attention kernel: up to **6.9x**, average **3.5x** faster than one-core C/G-Full;
- end-to-end: up to **4.5x**, average **2.9x** faster than one-core C/G-Full;
- vs llm.npu native attention using 4 CPU cores/GPU: up to **3.0x** lower latency while ShadowNPU uses only one middle CPU core.

Cross-device:
- on Snapdragon 8 Gen2 PhoneLM-0.5B, dataset-level speedups vs C/G-Full reported around 2x / 1.25x / 1.22x.

Energy (single attention kernel on Redmi K60):
- up to **7.66x lower energy** depending on model/baseline;
- example PhoneLM-0.5B: 3.72 J C/G-Full vs 0.66 J ShadowNPU.

Accuracy cost:
- paper reports **0.4 pp average loss** vs C/G-Full.

## Q8 — Evidence vs hypothesis

### [FACT — direct commercial-phone evidence]
On the evaluated Snapdragon phones, full INT8 NPU attention can badly damage task accuracy, while a decomposed NPU-estimation + sparse CPU/GPU path preserves near-full-attention accuracy.

### [FACT — heterogeneous system value]
Fine-grained NPU/CPU-GPU overlap and static-graph adaptation materially improve latency/resource use in the reported setup.

### [FACT — Agent relevance]
DroidCall and Octopus are mobile Agent/function-calling datasets, and ShadowNPU preserves high task accuracy there.

### [OBSERVATION]
Processor placement can depend on **what numerical property the sub-computation must preserve**, not only operator name or stage.

### [INFERENCE — project]
A strong NPU-centric software stack can shrink CPU fallback regions that would otherwise look like opportunities for a CPU-resident fast path.

### Not established
- Agent-semantic-aware placement;
- Huawei/NPU transfer;
- universal NPU advantage;
- decode-phase elimination of CPU/GPU;
- CPU matrix path vs ShadowNPU on the same hardware/workload;
- need for new CPU ISA/uArch.

## Q9 — Real contribution to the project decision

### CG-06 — CPU-Resident Latency-Critical Agent AI Fast Path
**Strengthen heterogeneous-control-point thesis + challenge/narrow CPU-resident region; no action/score change.**

Before ShadowNPU, CG-06 already required stage/operator-aware CPU↔NPU crossover analysis.
ShadowNPU raises the baseline materially:
> the relevant comparator is no longer a naive/full NPU path; it must include an **optimized NPU-centric path** that selectively moves quantization-sensitive residual work to CPU/GPU and pipelines the engines.

Therefore the CG-06 experiment must answer:
> Does a meaningful CPU-resident region still survive **after** NPU-centric quantization/sparsity/static-graph/pipeline optimizations?

This makes CG-06 harder to pass but more decision-relevant.

### C — Efficient System-Control Substrate
**Contextual support, no promotion.**
ShadowNPU demonstrates cross-engine scheduling complexity and resource-contention motivation, but the mechanism is operator/runtime-specific and not Agent-aware OS control.

### A / Agent semantics
**No direct impact.**
The placement decision comes from model/operator numerical behavior, not DemandState/RequiredProgress.

### R3 / uArch
**Remain BLOCKED.**
Existing NPU + CPU/GPU + compiler/runtime mechanisms already capture large value. No CPU hardware insufficiency is shown.

### Second-Bet search
The broad candidate **Agent-Aware Heterogeneous Stage Graph Placement** is **not differentiated yet**.

ShadowNPU shows that generic model/operator characteristics already justify sophisticated heterogeneous placement.
A differentiated Agent variant must prove incremental value from Agent-specific signals such as:
- semantic criticality;
- useful-by timing;
- cancellation/discardability;
- foreground QoE budget;
- state reuse across Agent stages
beyond optimized model/operator placement.

## Q10 — Next action

1. **KEEP PAPER-057 as P0**.
2. Create a canonical Claim for optimized NPU-centric reclaim of CPU/GPU fallback work.
3. Add ShadowNPU to CG-06's strong baseline and experiment inputs.
4. Replace the simple NPU comparator in EXP-CG06-001 with at least:
   - NPU-BASE;
   - NPU-OPT (quantization/sparsity/static-graph/pipeline optimized);
   - CPU-VECTOR;
   - CPU-MATRIX;
   - selective heterogeneous composition where applicable.
5. No score/action promotion for CG-06.
6. Snowball the PKU/BUPT line: llm.npu (ASPLOS 2025), HeteroLLM competing route, NPU compiler/quantization work.
7. Only call a CPU-specific architectural opportunity after the optimized NPU frontier is exhausted on matched phone workloads.

## Decision footer
- **New-regime relevance:** generic enabling / mobile-LLM amplified; Agent-relevant but not Agent-native
- **Evidence maturity:** **SYSTEM_VALUE** for evaluated Snapdragon on-device LLM/Agent-task inference
- **Decision impact:** strengthen CG-06 baseline and heterogeneous-control-point thesis; narrow CPU-resident whitespace
- **CG-06 impact:** INVEST / 86.5 unchanged; experiment baseline strengthened
- **C impact:** contextual only; no Agent-specific residual
- **A impact:** none
- **R3 impact:** remain BLOCKED
- **Second-Bet impact:** generic heterogeneous placement is crowded; Agent-specific incremental variable still unproven
- **Open questions:** Huawei transfer, CPU-MATRIX vs optimized NPU matched comparison, decode, newer NPUs, foreground-QoE externalities, Agent-specific placement residual
- **Primary source:** https://arxiv.org/abs/2508.16703
- **ACM source:** https://doi.org/10.1145/3745756.3809205
- **Artifact:** https://zenodo.org/records/19555734
