# Research task: independent validation and counter-evidence for two recent mobile

**Question:** Research task: independent validation and counter-evidence for two recent mobile Agent systems papers and their implications for a mobile CPU/LLVM/Runtime/heterogeneous-system research portfolio. Date cutoff: 2026-11-09. Search and synthesize primary academic papers (peer-reviewed and preprints clearly separated), official Android/AOSP/Qualcomm/Arm documentation, and artifact/code evidence. This is a targeted literature review, not a generic LLM survey.

Seed papers:
1) EdgePace, "Deadline- and Freshness-Aware LLM Scheduling on Unified-Memory Platforms", arXiv:2610.37307 (2026-10-27). Reported OnePlus 13 Snapdragon 8 Elite + Jetson evaluation, CPU hardware-counter feedback, safe prefill/decode suspension points, deadline/freshness-aware yielding; OnePlus camera deadline misses -91.3% while retaining 90.4% LLM throughput vs unmanaged inference.
2) Tandem, "Serving Hybrid Linear-Attention GUI Agents on Mobile NPUs", arXiv:2610.26660 (2026-10-19). Reported Snapdragon 8 Elite GUI-agent traces with Qwen3.5-4B hybrid linear-attention policy, recurrent-state reuse at prompt divergence, speculative rollback tail, fused verification, release of active NPU power vote while model remains loaded; vs llama.cpp fastest NPU config, text-step latency -30%, screenshot-step latency -16%, text-step energy -33%, standby power 0.76W to 0.22W.

Existing repository baselines to compare (do not assume paper identities if titles differ; verify):
- SERENO / PAPER-003
- Agent.xpu / HeRo / PAPER-098
- llm.npu / ShadowNPU and associated paper lineage
- Android NPU Manager / AOSP and Qualcomm QNN/Hexagon backend/session APIs
- Existing mobile LLM runtime memory caching, recurrent state, checkpoint/rollback, and accelerator power management.

Research questions:
A. Find genuinely independent teams' smartphone/mobile-agent papers since 2024 and especially 2026; include work on GUI agents, stateful/recurrent LLM serving, NPU scheduling, memory contention, foreground QoE/deadlines, accelerator preemption/yield, idle power.
B. For every close paper, extract exact authors, institutions, dates, device/SoC, model, workload/dataset/trace, baseline, metrics, key results, ablations, limitations, code/artifact availability, publication status.
C. Map research lineages: overlapping authors, institutions, datasets, phones, runtime/backend, code, citations. Distinguish independent replication from same-lab extension or shared platform comparisons.
D. Counter-evidence: Does Android NPU Manager, QNN, Hexagon or OEM runtime already expose the same scheduling/yield/session-power controls? Does EdgePace only beat unmanaged baselines? What is its CPU counter sampling overhead and portability? Are preemption/suspension points actually supported by the accelerator backend? Does Tandem only apply to one hybrid linear-attention model, app set, and backend? Are energy numbers per-step, standby, or whole-device? Are any comparisons against a strongest available baseline?
E. Assess what the new evidence really changes for:
- C: Runtime/OS heterogeneous scheduling and QoE.
- CG-06: CPU-local/LLVM/AArch64 inference and control fast paths.
- B-residual: CPU/NPU/DRAM derived-state validity/consistency residual.
- A: private RequiredProgress beyond software-observable workflow state.
Also note any implications for PT-A and R2 only if directly relevant.
F. Search for evidence that weakens the new claims: independent negative results, portability limitations, backend constraints, OEM implementation evidence, generic runtime solutions that make custom hardware unnecessary.

Output:
1) A cited synthesis with primary-source links and dates.
2) A comparison table for EdgePace, Tandem, SERENO, HeRo/Agent.xpu, Android NPU Manager/QNN, and any truly independent close work.
3) A lineage/independence map.
4) A claim-level counter-evidence matrix.
5) Explicit status per direction: strengthen / narrow / unchanged / weaken / refute / insufficient evidence.
6) Clearly label facts, inferences, hypotheses, and unsupported claims.
Do not infer new CPU hardware/ISA necessity from software scheduling improvements. Do not combine device-specific speedups. Do not treat arXiv preprints as peer-reviewed or independent replication. Prefer original papers and official docs.

# Independent Assessment of **Mobile Agent Acceleration** and Scheduling Runtimes

Recent preprints claim substantial latency and energy reductions for on-device agents via runtime scheduling and state reuse. However, systematic comparison with independent peer-reviewed literature reveals that these benefits largely exploit unmanaged baselines or specific execution phases rather than establishing new microarchitectural requirements.

## Systems Lineage and Baseline Comparison

The evaluated mobile agent execution stack spans multiple distinct paradigms, contrasting centralized multi-agent orchestrators with on-device heterogeneous execution frameworks. While distributed cloud serving systems optimize agent pipelines through length prediction or communication deferral [[1.1]](https://consensus.app/papers/maestro-workloadaware-crosscluster-scheduling-for-wang-zhou/c1da3835f6af5882b0a2d8241df8a6eb/) [[2.1]](https://consensus.app/papers/stageaware-communication-scheduling-for-disaggregated-sun-liao/af619818b3515743888d88414a9f125d/), on-device execution must negotiate tight hardware-level limits on commodity SoCs [[3.1]](https://consensus.app/papers/agentxpu-efficient-scheduling-of-agentic-llm-workloads-on-wei-zhang/2ff5ce2498735f3d9a5eaaddaf529b37/).

| System | Track / Status | Target Platform | Workload / Model | Primary Optimization Baseline | Key Outcome Reported |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Tandem** | Preprint (2026) [[4.1]](https://consensus.app/papers/tandem-serving-hybrid-linearattention-gui-agents-on-chen-ni/5f814847dce456ffb42e1fa93711846d/) | Snapdragon 8 Elite [[4.2]](https://consensus.app/papers/tandem-serving-hybrid-linearattention-gui-agents-on-chen-ni/5f814847dce456ffb42e1fa93711846d/) | GUI Agent / Qwen3.5-4B [[4.2]](https://consensus.app/papers/tandem-serving-hybrid-linearattention-gui-agents-on-chen-ni/5f814847dce456ffb42e1fa93711846d/) | llama.cpp NPU backend [[4.2]](https://consensus.app/papers/tandem-serving-hybrid-linearattention-gui-agents-on-chen-ni/5f814847dce456ffb42e1fa93711846d/) | **-30% text latency**, standby power 0.76W to 0.22W [[4.2]](https://consensus.app/papers/tandem-serving-hybrid-linearattention-gui-agents-on-chen-ni/5f814847dce456ffb42e1fa93711846d/) |
| **Agent.xpu** | Preprint (2025) [[3.2]](https://consensus.app/papers/agentxpu-efficient-scheduling-of-agentic-llm-workloads-on-wei-zhang/2ff5ce2498735f3d9a5eaaddaf529b37/) | Heterogeneous SoC [[3.3]](https://consensus.app/papers/agentxpu-efficient-scheduling-of-agentic-llm-workloads-on-wei-zhang/2ff5ce2498735f3d9a5eaaddaf529b37/) | Personal Agents / Llama-3B/8B [[3.4]](https://consensus.app/papers/agentxpu-efficient-scheduling-of-agentic-llm-workloads-on-wei-zhang/2ff5ce2498735f3d9a5eaaddaf529b37/) | Industrial iGPU engine & static NPU-iGPU [[3.4]](https://consensus.app/papers/agentxpu-efficient-scheduling-of-agentic-llm-workloads-on-wei-zhang/2ff5ce2498735f3d9a5eaaddaf529b37/) | **≥91% reactive latency drop**, 1.2–4.9× throughput [[3.4]](https://consensus.app/papers/agentxpu-efficient-scheduling-of-agentic-llm-workloads-on-wei-zhang/2ff5ce2498735f3d9a5eaaddaf529b37/) |
| **sd.npu** | Preprint (2025) [[5.1]](https://consensus.app/papers/accelerating-mobile-language-model-via-speculative-chen-xu/15214da29f7d5ee7ad25319cd3f94826/) | Snapdragon 8 Gen 2/3/Elite [[5.2]](https://consensus.app/papers/accelerating-mobile-language-model-via-speculative-chen-xu/15214da29f7d5ee7ad25319cd3f94826/) | Mobile RAG / Speculative Decoding [[5.3]](https://consensus.app/papers/accelerating-mobile-language-model-via-speculative-chen-xu/15214da29f7d5ee7ad25319cd3f94826/) | mllm engine (NPU/CPU) [[5.4]](https://consensus.app/papers/accelerating-mobile-language-model-via-speculative-chen-xu/15214da29f7d5ee7ad25319cd3f94826/) | **1.06–3.81× speedup**, 1.07–4.71× energy savings [[5.5]](https://consensus.app/papers/accelerating-mobile-language-model-via-speculative-chen-xu/15214da29f7d5ee7ad25319cd3f94826/) |
| **MobiRL** | Peer-Reviewed (2024) [[6.1]](https://consensus.app/papers/an-intelligent-scheduling-approach-on-mobile-os-for-dou-liu/d6fc3bbac2325b488ec2caa6dbaf30b3/) | Snapdragon 888 / AOSP [[6.2]](https://consensus.app/papers/an-intelligent-scheduling-approach-on-mobile-os-for-dou-liu/d6fc3bbac2325b488ec2caa6dbaf30b3/) | Interactive UI workloads [[6.3]](https://consensus.app/papers/an-intelligent-scheduling-approach-on-mobile-os-for-dou-liu/d6fc3bbac2325b488ec2caa6dbaf30b3/) | Commercial AOSP scheduler [[6.4]](https://consensus.app/papers/an-intelligent-scheduling-approach-on-mobile-os-for-dou-liu/d6fc3bbac2325b488ec2caa6dbaf30b3/) | **-4.1% frame drops**, -42.8% power consumption [[6.4]](https://consensus.app/papers/an-intelligent-scheduling-approach-on-mobile-os-for-dou-liu/d6fc3bbac2325b488ec2caa6dbaf30b3/) |
| **Orthrus** | Peer-Reviewed (2024) [[7.1]](https://consensus.app/papers/qosaware-power-management-via-scheduling-and-governing-sang-yan/c72a48d4730c5309962a1587a33d48b5/) | Google Pixel 3 / Android [[7.2]](https://consensus.app/papers/qosaware-power-management-via-scheduling-and-governing-sang-yan/c72a48d4730c5309962a1587a33d48b5/) | Widespread mobile apps [[7.2]](https://consensus.app/papers/qosaware-power-management-via-scheduling-and-governing-sang-yan/c72a48d4730c5309962a1587a33d48b5/) | Decoupled DVFS / CPU governors [[7.3]](https://consensus.app/papers/qosaware-power-management-via-scheduling-and-governing-sang-yan/c72a48d4730c5309962a1587a33d48b5/) | **Up to 35.7% power reduction** maintaining QoS [[7.3]](https://consensus.app/papers/qosaware-power-management-via-scheduling-and-governing-sang-yan/c72a48d4730c5309962a1587a33d48b5/) |

**Figure 1.** Personal LLM Agent System. Agent.xpu bridges the agent applications and heterogeneous SoC, orchestrating stateful on-device LLM flows from both foreground reactive agents and background proactive agents. [[3]](https://consensus.app/papers/agentxpu-efficient-scheduling-of-agentic-llm-workloads-on-wei-zhang/2ff5ce2498735f3d9a5eaaddaf529b37/)

*How to read: Architectural block diagram showing how an on-device personal LLM agent bridges user-facing reactive and proactive flows across heterogeneous SoC processing units.*

## Counter-Evidence and Architectural Constraints

Independent profiling highlights major blind spots in current mobile NPU agent claims:

- **Phase-Divergent Hardware Affinity**: Cross-layer measurement proves that NPUs excel strictly at compute-bound prefilling due to static graph optimizations, whereas CPUs consistently outperform NPUs during memory-bound decoding [[8.1]](https://consensus.app/papers/is-your-npu-ready-for-llms-dissecting-the-hidden-efficiency-cai-tian/ed1446e3dd9d5602a2067b9517cdea2b/) [[8.2]](https://consensus.app/papers/is-your-npu-ready-for-llms-dissecting-the-hidden-efficiency-cai-tian/ed1446e3dd9d5602a2067b9517cdea2b/). Because NPUs struggle with dynamic, small-kernel token generation [[5.6]](https://consensus.app/papers/accelerating-mobile-language-model-via-speculative-chen-xu/15214da29f7d5ee7ad25319cd3f94826/) [[8.3]](https://consensus.app/papers/is-your-npu-ready-for-llms-dissecting-the-hidden-efficiency-cai-tian/ed1446e3dd9d5602a2067b9517cdea2b/), serving engines routinely offload attention or decoding to CPUs or GPUs [[5.7]](https://consensus.app/papers/accelerating-mobile-language-model-via-speculative-chen-xu/15214da29f7d5ee7ad25319cd3f94826/) [[5.8]](https://consensus.app/papers/accelerating-mobile-language-model-via-speculative-chen-xu/15214da29f7d5ee7ad25319cd3f94826/).
- **Unmanaged Baselines and Power Control**: Much of the reported energy savings in recent preprints stems from addressing poor baseline runtime configurations. Profiling shows that uncoordinated NPU sleep latencies and CPU polling intervals in generic frameworks waste up to 40% of system energy [[8.4]](https://consensus.app/papers/is-your-npu-ready-for-llms-dissecting-the-hidden-efficiency-cai-tian/ed1446e3dd9d5602a2067b9517cdea2b/), while tuning CPU frequency governors alone cuts energy consumption by up to 39.7% without new hardware mechanisms [[8.5]](https://consensus.app/papers/is-your-npu-ready-for-llms-dissecting-the-hidden-efficiency-cai-tian/ed1446e3dd9d5602a2067b9517cdea2b/).
- **Shared-Memory Saturation**: Asymmetric memory contention dominates heterogeneous SoCs; memory-bound kernels quickly saturate shared LPDDR bandwidth and degrade co-running tasks far more than compute-bound operations [[3.5]](https://consensus.app/papers/agentxpu-efficient-scheduling-of-agentic-llm-workloads-on-wei-zhang/2ff5ce2498735f3d9a5eaaddaf529b37/) [[3.6]](https://consensus.app/papers/agentxpu-efficient-scheduling-of-agentic-llm-workloads-on-wei-zhang/2ff5ce2498735f3d9a5eaaddaf529b37/).
- **Compiler Fusion and Peak Bursts**: Monolithic operator fusion inside vendor NPU compilers creates severe peak-current bursts that induce voltage droops and trigger unwanted thermal or DVFS throttling under low-voltage battery conditions [[9.1]](https://consensus.app/papers/mitigating-compiler-fusioninduced-power-bursts-in-mobile-yuzawa-tomizuka/0e80718cbd8b5c73a6832a779b988bf2/) [[9.2]](https://consensus.app/papers/mitigating-compiler-fusioninduced-power-bursts-in-mobile-yuzawa-tomizuka/0e80718cbd8b5c73a6832a779b988bf2/).

**Figure 13.** Impact of CPU frequency scaling on throughput and energy during NPU inference for Qwen 1.5B, across prefill and decode on Xiaomi 17 and OnePlus 15. [[8]](https://consensus.app/papers/is-your-npu-ready-for-llms-dissecting-the-hidden-efficiency-cai-tian/ed1446e3dd9d5602a2067b9517cdea2b/)

*How to read: A four-panel plot comparing inference throughput and energy consumption across varied CPU frequencies during NPU execution on commercial mobile devices.*

## Implications for Systems Research Portfolio

Assessing these findings against CPU, LLVM, and runtime research directions establishes clear boundaries between validated software behavior and speculative microarchitectural proposals:

- **Runtime and OS Heterogeneous Scheduling (Status: Strengthen)**: Validated by peer-reviewed studies demonstrating that coordinated frequency governing and stage-elastic thread assignment mitigate QoS violations without hardware changes [[7.1]](https://consensus.app/papers/qosaware-power-management-via-scheduling-and-governing-sang-yan/c72a48d4730c5309962a1587a33d48b5/) [[6.1]](https://consensus.app/papers/an-intelligent-scheduling-approach-on-mobile-os-for-dou-liu/d6fc3bbac2325b488ec2caa6dbaf30b3/). Decoupling prefill and decode stages effectively prevents shared DRAM bandwidth saturation [[3.7]](https://consensus.app/papers/agentxpu-efficient-scheduling-of-agentic-llm-workloads-on-wei-zhang/2ff5ce2498735f3d9a5eaaddaf529b37/) [[3.8]](https://consensus.app/papers/agentxpu-efficient-scheduling-of-agentic-llm-workloads-on-wei-zhang/2ff5ce2498735f3d9a5eaaddaf529b37/).
- **CPU-Local and LLVM Fast Paths (Status: Strengthen)**: Peer-reviewed measurements confirm that memory-bound token decoding runs faster and more flexibly on mobile CPUs than on fixed-topology NPUs [[8.1]](https://consensus.app/papers/is-your-npu-ready-for-llms-dissecting-the-hidden-efficiency-cai-tian/ed1446e3dd9d5602a2067b9517cdea2b/) [[8.2]](https://consensus.app/papers/is-your-npu-ready-for-llms-dissecting-the-hidden-efficiency-cai-tian/ed1446e3dd9d5602a2067b9517cdea2b/). Inserting pre-compilation graph barriers mitigates compiler fusion power spikes without requiring novel execution units [[9.3]](https://consensus.app/papers/mitigating-compiler-fusioninduced-power-bursts-in-mobile-yuzawa-tomizuka/0e80718cbd8b5c73a6832a779b988bf2/).
- **Derived-State Consistency Residual (Status: Narrow)**: Reusing recurrent states across diverging prompt prefixes is effective in constrained domains [[4.3]](https://consensus.app/papers/tandem-serving-hybrid-linearattention-gui-agents-on-chen-ni/5f814847dce456ffb42e1fa93711846d/), but real-world mobile GUI environments exhibit substantial short- and long-term memory deficits across complex workflows [[10.1]](https://consensus.app/papers/memguibench-benchmarking-memory-of-mobile-gui-agents-in-liu-zhao/fcb6253470895805b58deaa3daa11ff9/) [[10.2]](https://consensus.app/papers/memguibench-benchmarking-memory-of-mobile-gui-agents-in-liu-zhao/fcb6253470895805b58deaa3daa11ff9/).
- **Hardware-Enforced Progress State (Status: Weaken / Insufficient Evidence)**: Factually, existing mobile system gains are achieved entirely via software scheduling, graph-level batching, and OS-level governor tuning [[5.9]](https://consensus.app/papers/accelerating-mobile-language-model-via-speculative-chen-xu/15214da29f7d5ee7ad25319cd3f94826/) [[7.1]](https://consensus.app/papers/qosaware-power-management-via-scheduling-and-governing-sang-yan/c72a48d4730c5309962a1587a33d48b5/) [[6.5]](https://consensus.app/papers/an-intelligent-scheduling-approach-on-mobile-os-for-dou-liu/d6fc3bbac2325b488ec2caa6dbaf30b3/). Inferring a necessity for new CPU ISA extensions or specialized execution hardware is an **unsupported hypothesis** contradicted by runtime-only solutions.
 
_These search results were found and analyzed using Consensus, an AI-powered search engine for research. Try it at https://consensus.app. © 2026 Consensus NLP, Inc. Personal, non-commercial use only; redistribution requires copyright holders’ consent._
 
## References
 
`1.` Wang J, Zhou X, Sun X, et al. Maestro: Workload-Aware Cross-Cluster Scheduling for LLM-based Multi-Agent Systems. *2026 IEEE 46th International Conference on Distributed Computing Systems (ICDCS).* 2026. doi:10.1109/2575-8411.2026.00031
 
> [1.1] We present Maestro, a workload-aware scheduling system designed for LLM-MAS serving under strict GPU budgets. (Abstract)
 
`2.` Sun Y, Liao X, Xie S, et al. Stage-Aware Communication Scheduling for Disaggregated LLM Serving. 2026. doi:10.48550/arxiv.2603.17456
 
> [2.1] It achieves this through a Defer-and-Promote principle implemented through a Reverse Multi-Level Queue (RMLQ) structure. (Abstract)
 
`3.` Wei X, Zhang J, Li H, et al. Agent.xpu: Efficient Scheduling of Agentic LLM Workloads on Heterogeneous SoC. *ArXiv.* 2025;abs/2506.24045. doi:10.48550/arxiv.2506.24045
 
> [3.1] These systems target multi-tenant cloud settings with abundant resources, whereas our focus is on single-device agents operating under tight SoC constraints. (Body)
 
> [3.2] This paper presents Agent$. (Abstract)
 
> [3.3] While modern heterogeneous SoCs integrate CPUs, iGPUs, and NPUs to support on-device intelligence, existing LLM engines assume static, single-shot inference and lack mechanisms for flow-level concurrency, prioritization, and efficient accelerator coordination. (Abstract)
 
> [3.4] $xpu delivers 1.2-4.9$\times$ proactive throughput and reduces reactive latency by at least 91%, compared with both industrial iGPU-only serving engine and NPU-iGPU static inference with optimal tensor-partitioning schemes. (Abstract)
 
> [3.5] Concurrent agentic flows often emit overlapping NPU and iGPU kernel executions, which intensify contention for the limited DDR bandwidth of modern shared-memory SoCs, potentially degrading the latency of each individual task. (Methods)
 
> [3.6] Memory-bound kernels are significantly more sensitive to, and more likely to saturate, shared DDR bandwidth than compute-bound kernels. (Methods)
 
> [3.7] This suggests that contention-aware kernel dispatching can maximize aggregate throughput by preventing concurrent memory-heavy accesses. (Methods)
 
> [3.8] $xpu introduces three key techniques: a heterogeneous execution graph (HEG) capturing NPU/iGPU affinity and elastic operator binding; flow-aware NPU-iGPU coordination with stage elasticity, decoupling prefill and decode to reduce bandwidth contention and enforce priorities; and fine-grained preemption with slack-aware piggybacking to guarantee reactive responsiveness without starving proactive work. (Abstract)
 
`4.` Chen Z, Ni J, Zheng X, et al. Tandem: Serving Hybrid Linear-Attention GUI Agents on Mobile NPUs. 2026. doi:10.48550/arxiv.2610.26660
 
> [4.1] Smartphone GUI agents complete tasks in mobile apps by repeatedly reading the screen and asking a model for the next action. (Abstract)
 
> [4.2] On a Snapdragon 8 Elite, Tandem reduces per-step latency by 30% for text-based screen descriptions and 16% for screenshots relative to llama.cpp's fastest NPU configuration, reduces energy per text step by 33%, and lowers standby power with the model loaded from 0.76 to 0.22 W. (Abstract)
 
> [4.3] Tandem saves recurrent state where consecutive prompts diverge, allowing later requests to reuse previously processed context. (Abstract)
 
`5.` Chen Z, Xu D, Shen H, Xu M, Wang S,  Y. Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution. *ArXiv.* 2025;abs/2510.15312. doi:10.48550/arxiv.2510.15312
 
> [5.1] In this work, we propose a holistic acceleration framework sd.npu, designed to maximize NPU efficiency for on-device RAG ecosystem. (Abstract)
 
> [5.2] We evaluate sd.npu on three representative smartphones with Qualcomm SoCs: Redmi K60 Pro (Snapdragon 8 Gen 2, Android 13, 12 GB RAM), Redmi K70 Pro (Snapdragon 8 Gen 3, Android 14, 16 GB RAM), and OnePlus 13 (Snapdragon 8 Gen Elite, Android 14, 24 GB RAM). (Methods)
 
> [5.3] We evaluate four common mobile tasks collected from prior work: document summarization ( summary ) [57], RAG-based question answering ( rag ) [57], UI automation ( ui ) [58] and automatic message reply ( tweet ) [46]. (Methods)
 
> [5.4] To eliminate performance gaps from backend design differences, we implement their algorithms atop mllm 1 . (Methods)
 
> [5.5] Experiments on commercial smartphones show that our framework significantly outperforms existing baselines, delivering 1.06$\times$--3.81$\times$ speedups and 1.07$\times$--4.71$\times$ energy savings across various RAG tasks. (Abstract)
 
> [5.6] Specifically, current hardware struggles with the variable workloads intrinsic to RAG: the transition between processing extensive contexts and generating tokens incurs significant overhead due to static graph constraints, while the memory-bound generation phase leaves computational resources underutilized. (Abstract)
 
> [5.7] - NPU-CPU/GPU co-scheduling (e.g., mllm [59], HeteroLLM [6], PowerInfer-V2 [60]): offloading only computeintensive operations in prefill to NPU, while executing precisionintensive kernels and decoding on CPUs or GPUs. (Methods)
 
> [5.8] 2 mllm [59] and other on-device LLM engines [6, 60] offload precisionsensitive operations, such as attention, to CPU/GPU to improve response quality. (Methods)
 
> [5.9] This approach masks the overhead of model reconfiguration by parallelizing the loading of decoding graphs with the computation of partitioned context chunks (chunked prefill), thereby ensuring continuous execution flow. (Abstract)
 
`6.` Dou X, Liu L, Xiao L. An Intelligent Scheduling Approach on Mobile OS for Optimizing UI Smoothness and Power. *ACM Transactions on Architecture and Code Optimization.* 2024;22:1 - 27. doi:10.1145/3674910
 
> [6.1] To this end, we propose MobiRL, a reinforcement learning-based scheduler for intelligently adjusting the CPU/GPU frequency to satisfy user demands accurately on mobile systems. (Abstract)
 
> [6.2] We conduct the experiments on the real h/w delivered by a well-known mobile company. (Methods)
 
> [6.3] Mobile devices need to respond quickly to diverse user inputs. (Abstract)
 
> [6.4] The experimental results on the latest delivered smartphones show that MobiRL outperforms the widely used commercial scheduler on real devices—reducing the frame drop rate by 4.1% and reducing power consumption by 42.8%, respectively. (Abstract)
 
> [6.5] MobiRL monitors the mobile system status and autonomously learns to optimize UI smoothness and power consumption by conducting CPU/GPU frequency-adjusting actions. (Abstract)
 
`7.` Sang Q, Yan J, Xie R, Hu C, Suo K, Cheng D. QoS-Aware Power Management via Scheduling and Governing Co-Optimization on Mobile Devices. *IEEE Transactions on Mobile Computing.* 2024;23:13654-13669. doi:10.1109/tmc.2024.3438267
 
> [7.1] To address the above issues, we propose Orthrus, a comprehensive QoS-aware power management approach that involves a governing approach based on deep reinforcement learning to adjust the frequency of heterogeneous cores, a scheduling algorithm based on finite state machine that assigns cores to QoS-related threads, and expert fuzzy control-based coordination mechanism between the two to manage the impact between scheduling and governing. (Abstract)
 
> [7.2] We implement Orthrus on Google Pixel 3 as the system service of Android and evaluate it using several widespread mobile applications. (Abstract)
 
> [7.3] The performance evaluation demonstrates that Orthrus reduces the average power consumption by up to 35.7% compared to three state-of-the-art techniques while ensuring the QoS on mobile platforms. (Abstract)
 
`8.` Cai G, Tian R, Yang L, et al. Is Your NPU Ready for LLMs? Dissecting the Hidden Efficiency Bottlenecks in Mobile LLM Inference. *ArXiv.* 2026;abs/2607.05475. doi:10.48550/arxiv.2607.05475
 
> [8.1] (2) We identify a distinct 'phase split' where NPUs excel at compute-bound prefilling, while CPUs outperform all other backends in memory-bound decoding. (Body)
 
> [8.2] (2) We identify a distinct ``phase split,''in which NPUs excel at compute-bound prefilling, while CPUs outperform all other backends in memory-bound decoding. (Abstract)
 
> [8.3] This is driven by the NPU's preference for large, fixed-shape workloads, which conflicts with the small-kernel, dynamic nature of decoding. (Body)
 
> [8.4] Suboptimal thread configurations, uncoordinated NPU sleep latencies, and CPU polling intervals result in up to 40% energy waste. (Body)
 
> [8.5] For example, tuning CPU frequency alone reduces energy consumption by up to $39.7\%$. (Abstract)
 
`9.` Yuzawa R, Tomizuka M. Mitigating Compiler Fusion-Induced Power Bursts in Mobile NPU Inference as the Battery Depletes. *ArXiv.* 2026;abs/2607.16555. doi:10.48550/arxiv.2607.16555
 
> [9.1] Under low-voltage conditions, however, a single inference can induce an instantaneous voltage droop in the power-delivery network, causing the power management integrated circuit to invoke dynamic voltage and frequency scaling (DVFS) and increase latency. (Abstract)
 
> [9.2] We show that aggressive operator fusion in a mobile NPU compiler can create monolithic superlayers whose concentrated execution produces large peak-current bursts. (Abstract)
 
> [9.3] We further evaluate a practical black-box mitigation: a measurement-guided, pre-compilation graph rewrite that inserts barriers at selected peak-to-average power ratio hot spots to prevent harmful superlayer merging in the vendor NPU compiler. (Abstract)
 
`10.` Liu G, Zhao P, Liang Y, et al. MemGUI-Bench: Benchmarking Memory of Mobile GUI Agents in Dynamic Environments. *ArXiv.* 2026;abs/2602.06075. doi:10.48550/arxiv.2602.06075
 
> [10.1] Our experiments reveal substantial memory deficits across all evaluated systems, including 4-10x capability gaps on memory-intensive tasks. (Abstract)
 
> [10.2] They further show that short-term memory is indispensable, while explicit long-term memory improves cross-session learning by 21.9 percentage points, with cross-application transfer and computational cost remaining major bottlenecks. (Abstract)
