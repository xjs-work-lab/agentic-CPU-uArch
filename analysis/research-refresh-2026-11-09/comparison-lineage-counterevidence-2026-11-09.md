# Independent validation and counter-evidence matrix — 2026-11-09

## Executive finding

The new literature strengthens the case for **software and Runtime/OS co-optimization**, especially phase-aware CPU/NPU execution, foreground QoE, NPU session/power management, graph scheduling and Agent state reuse. It does **not** create evidence for a new Agent-specific CPU ISA or microarchitecture Primary Bet.

The most decision-relevant new-to-repository source is PAPER-124 (cross-layer CPU/GPU/NPU mobile inference measurement). The most directly Agent-native new paper is PAPER-123 (Tandem). PAPER-122 (EdgePace) adds a new deadline/freshness-aware control loop but is not a full GUI-agent benchmark. PAPER-126 (sd.npu) and PAPER-127 (MemGUI-Bench) are older but important prior-art items missing from the October repository closure.

## 1. Source comparison

| Source | Status / lineage | Device and workload | Mechanism | Baseline and result | Project relevance |
|---|---|---|---|---|---|
| PAPER-003 SERENO | OSDI 2026, peer-reviewed; SJTU/IPADS lineage | OnePlus 12/13; foreground apps + background mobile LLM | Memory-bandwidth-aware yield/control using speculative decoding | Up to 92.6%, average 58.5% jank reduction; strong generic foreground protection baseline | C baseline; narrows novelty of generic foreground-first control |
| PAPER-098 HeRo | DAC 2026 / arXiv; Peking University IF-Lab; same lineage as Agent.xpu per existing repo audit | Redmi K80 / OnePlus 13; Agentic RAG dynamic DAG | Shape-aware sub-stage partition, criticality/affinity and bandwidth-aware concurrency | Up to 10.94× vs GPU-only; up to ~1.5× vs static xPU mapping | C Agent-aware system value; not independent replication of Agent.xpu |
| PAPER-122 EdgePace | arXiv preprint, 2026-10-27; CUHK-Shenzhen/Tsinghua AIR/Fudan/KAUST | OnePlus 13 camera+LLM feedback; Jetson multi-camera/robotics | Safe sublayer quanta in prefill/decode; CPU PMU demand+stall counters; deadline/freshness-aware Bypass/Admit/Hold | OnePlus camera misses 66.78%→5.83% (-91.3%) while retaining 90.4% of unmanaged LLM throughput; also compares MNN/QAIRT and classical scheduling | C strengthened; CPU-counter feedback relevant to CG-06; not GUI Agent or hardware evidence |
| PAPER-123 Tandem | arXiv preprint, 2026-10-19; FIU/UH/NEC Labs/SMU/independent researcher; separate from EdgePace/SERENO/HeRo teams | OnePlus 13T (Snapdragon 8 Elite/Hexagon v79) and OnePlus 15 (Snapdragon 8 Elite Gen 5/Hexagon v81); GUI Agent | Divergence-point recurrent checkpoints, rollback-aware prefill, shared verification, idle NPU power-vote release | vs llama.cpp fastest NPU config: text-step -30%, screenshot-step -16%, energy/text-step -33%, loaded-model standby 0.76→0.22 W; open fork and implementation | C/CG-06 strengthened; B-residual narrowed for software state/power; no hardware proof |
| PAPER-124 Is Your NPU Ready | arXiv v1 2026-07-06; Tsinghua/BJTU; manuscript lists POMACS DOI metadata, publisher status still needs confirmation | Xiaomi 14/15/17 and OnePlus 15; 5 frameworks, 3 backends, 5 models, >400 configs | PowerBench backend energy; phase/backend profiling; RPC polling, NPU sleep, affinity and DVFS tuning | CPU decode 55.7 tok/s vs NPU 23.0 on OnePlus 15 Qwen2.5-1.5B; 53.6–54.8% estimated energy reduction with 15.1–15.5% latency increase on two tasks | Strong CG-06/C evidence; high-value missed cross-layer baseline |
| PAPER-125 Compiler fusion power bursts | arXiv preprint 2026-07-17; UC Berkeley/Sony | Snapdragon 8 Gen 3; MobileNetV4 and Hiera vision backbones | PAPR-guided Q-DQ graph barriers before NPU compiler | 3.12→1.94 A peak current (-37.8%) with 3.76% latency overhead at one favorable setting; low-PAPR cases regress | Compiler/power stability side track; not CPU-uArch evidence |
| PAPER-126 sd.npu | arXiv full-text version 2025-12-17; PKU/BUPT; mllm implementation | Redmi K60 Pro, Redmi K70 Pro, OnePlus 13; RAG, UI automation, auto-reply | Progressive graph switching + NPU-tailored retrieval speculative decoding | 1.06–3.81× speedup; 1.11–4.18× energy reduction vs vanilla; up to 2.53×/4.71× vs speculative-decoding integrations | Important missed NPU/Agent software prior art |
| PAPER-127 MemGUI-Bench | arXiv preprint 2026-02; ZJU/Nankai/CUHK/SJTU/vivo AI Lab | 128 tasks / 26 apps / 11 agents | Short/long-term GUI memory benchmark and staged evaluation | 4–10× memory-task capability gaps; explicit long-term memory +21.9 pp cross-session learning | A problem relevance; not hardware evidence |

**Do not combine the percentages across these papers.** Their devices, models, workloads, metrics, and baselines differ.

## 2. Research lineage and independence

- **SERENO**: SJTU/IPADS team; peer-reviewed OSDI 2026. Direct smartphone foreground/background memory contention. EdgePace cites it as prior work but does not report a head-to-head SERENO run.
- **EdgePace**: different authors/institutions from SERENO, HeRo and Tandem. Independent research group, but it uses the same general Qualcomm mobile ecosystem and the same OnePlus 13 generation as SERENO. It adds sensor deadline/freshness and safe prefill/decode quanta. This is an independent new system, **not an independent replication of SERENO**.
- **HeRo / Agent.xpu**: same lineage according to the existing PAPER-098 source review; treat as sustained group capability, not independent replication.
- **Tandem**: authors and institutions differ from EdgePace, SERENO and HeRo. It has a public GitHub fork of llama.cpp, around 3,000 added C/C++ lines across 24 files, and direct Snapdragon phone tests. It is an independent system paper, but not a replication of another team's same mechanism.
- **sd.npu**: Peking University/BUPT; distinct author list from HeRo but Peking University is an institutional overlap. Same broad mobile NPU/RAG problem family; not a replication of HeRo or Tandem.
- **PAPER-124**: Tsinghua/BJTU measurement team, separate from the above systems groups. It measures backend/framework behavior rather than a single Agent runtime.
- **PAPER-125**: UC Berkeley/Sony team, independent NPU power/compiler study.
- **PAPER-127**: multi-institution GUI memory benchmark, separate from the systems scheduling teams.

## 3. Counter-evidence and limits

### 3.1 EdgePace

- Its 91.3% OnePlus 13 deadline-miss reduction is against unmanaged inference, not against SERENO. The paper does include classical scheduling policies and compares MNN/QAIRT configurations, but no direct SERENO implementation/measurement.
- The OnePlus 13 case is a camera foreground task with background LLM feedback; it is not a full GUI Agent action loop.
- PMU read overhead is reported on Jetson Orin Nano Super: median 80.9 µs at a 2 ms interval (4.04%) and 130.8 µs at 20 ms (0.65%). The local scheduler check averages 1.856 µs. These are not measured application slowdowns and are not the OnePlus 13 PMU overhead.
- The runtime needs per-platform and foreground-load calibration. It changes the llama.cpp backend submission path, not the CPU ISA or model kernels. No public EdgePace artifact was found in this review.
- Therefore it is strong C evidence, but not proof of a universal Android counter interface or Agent-only hardware state.

### 3.2 Tandem

- Stronger baseline than unmanaged: the paper compares with llama.cpp's fastest NPU configuration and offers a public fork.
- The main results are tied to hybrid linear-attention GUI-agent serving, the tested Qwen3.5 models, Hexagon v79/v81 and two OnePlus generations. The paper also reports tests on other recurrent architectures and AndroidControl, but this is not broad OEM production evidence.
- The 33% figure is energy per text step; 0.76→0.22 W is loaded-model standby power with the screen off. Neither is a whole-day battery claim.
- Runtime state reuse and power-vote release are software mechanisms; they narrow the claim that these functions inherently require a new CPU structure.

### 3.3 Android NPU Manager and Qualcomm runtime APIs

- AOSP Android 17 NPU Manager provides model admission, priority arbitration, unload requests under foreground/thermal pressure and work lifecycle events including resumed, paused and system-cancelled states. Vendor AIDL implementation is required.
- Android CTS includes a Mobly test for foreground-before-background NPU completion and access control. Its documentation explicitly says the test is race-based, needs device-specific tuning and expects two passes out of three. This is compatibility evidence, not a full QoE/energy evaluation, Agent semantic scheduler, or proof of universal vendor deployment.
- The HAL exposes scheduling/observation and lifecycle; inference still executes through vendor SDK/driver. The API does not express Agent semantic progress, output freshness, tool utility or required task completion.
- Qualcomm QAIRT documents manual/automatic HTP performance-control strategies and a performanceRelease() API. This establishes software-visible performance-vote control, but does not mean every SDK/device has a generic per-sublayer pause API or that an app can rely on identical behavior across OEMs.

### 3.4 Cross-layer mobile inference and compiler power

- PAPER-124 uses isolated inference with screen off and no background services. It is a strong CPU/GPU/NPU baseline but not direct concurrent Agent evidence.
- PAPER-124's 53.6–54.8% energy estimates trade off against up to ~15.5% latency increase on two workloads; do not present as a free gain.
- PAPER-125's 173 mV margin is an exploratory estimate from a fitted slope without confidence intervals, and its graph-splitting method is model/resolution/compiler-specific.
- PAPER-126 and PAPER-127 are important prior art but do not prove a new hardware feature.

## 4. Updated portfolio assessment (preliminary; not a formal decision event)

| Direction | Status | Reason |
|---|---|---|
| C — Runtime/OS heterogeneous orchestration | **STRENGTHEN** | SERENO, HeRo, EdgePace, Tandem, sd.npu and Android NPU Manager establish real phone value for priority, deadline/freshness, state reuse, graph switching and accelerator lifecycle control. Differentiated Agent semantics beyond strong software baselines remain unproven. |
| CG-06 — CPU-local / LLVM / AArch64 fast paths | **STRENGTHEN** | PAPER-124 gives direct CPU decode, operator/framework and host-side polling/DVFS evidence; EdgePace shows CPU PMU feedback can guide cross-engine QoE; Tandem demonstrates backend-aware runtime state and power control. This supports software/kernel/compiler work, not a new ISA. |
| B-residual — cross-engine derived-state validity | **NARROW** | Tandem and sd.npu solve selected recurrent-state, rollback and graph-switch problems in software; Android NPU Manager reports lifecycle. The remaining hypothesis must be limited to physical cross-CPU/NPU/DRAM state-validity or coherence gaps that software cannot cheaply reconstruct. No such residual is measured yet. |
| A — private RequiredProgress | **KEEP CONDITIONAL / NARROW** | PAPER-121 ProgRouter already derives semantic progress from a software workflow ledger; PAPER-127 shows genuine GUI memory deficits and benefit from long-term memory. Neither proves an irreducible hardware-private progress signal. A requires a matched-observability residual experiment/design, not more general memory evidence. |
| PT-A — trusted action/effect validation | **UNCHANGED** | This batch does not directly evaluate permission binding, target binding, external effect receipts or bounded recovery. |
| R2 — CPU continuation microstate/locality | **UNCHANGED** | No new direct phone CPU continuation-microstate/cache-locality evidence. PAPER-124 provides background cache hierarchy measurements only. |

**No formal investment portfolio change is proposed in this batch.** Preserve the October decision snapshot until the compiler/microarchitecture and industry batches are complete.

## 5. Main learning

The field is moving quickly in software-visible control:
- stage- and phase-aware CPU/NPU selection;
- host-side polling, sleep/wake and power-vote tuning;
- graph switching and prefill/decode scheduling;
- Agent recurrent-state checkpoint and rollback;
- foreground deadlines, freshness and QoE;
- platform-level NPU admission and lifecycle reporting.

This raises the bar for any hardware proposal. A candidate hardware feature must demonstrate incremental value after these software baselines, not merely solve a problem that a runtime or SDK already exposes.

## 6. Next batch

Move to CPU microarchitecture, compiler and vendor-platform developments:
1. AArch64/SME2/LLVM and mobile CPU kernel/dispatch changes since 2026-10-08.
2. New phone SoC CPU/cache/interconnect/memory disclosures from Arm, Qualcomm, MediaTek, Apple and Samsung.
3. New papers on CPU decode, CPU/NPU phase-aware scheduling, graph compilation and CPU-side energy.
4. Search explicitly for results that would strengthen or refute R2 and any new CPU hardware direction.

No PPT/PPTX files are modified in this refresh.
