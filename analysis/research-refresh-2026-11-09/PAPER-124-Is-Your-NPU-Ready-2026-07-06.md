# PAPER-124 — Is Your NPU Ready for LLMs? Dissecting the Hidden Efficiency Bottlenecks in Mobile LLM Inference

- **Primary source:** https://arxiv.org/abs/2607.05475
- **Full text:** https://arxiv.org/html/2607.05475
- **DOI printed in manuscript:** https://doi.org/10.1145/3857370
- **Authors:** Guanyu Cai, Ruiming Tian, Lang Yang, Zhouhong Ren, Jinliang Yuan, Lingkun Li, Jiliang Wang
- **Affiliations:** Tsinghua University; Beijing Jiaotong University
- **arXiv status:** v1 submitted 2026-07-06 (the arXiv record currently lists only v1).
- **Manuscript venue metadata:** full-text source identifies *Proceedings of the ACM on Measurement and Analysis of Computing Systems (POMACS)*, Vol. 10, Issue 3, Article 67, DOI 10.1145/3857370. The ACM DOI landing page could not be independently fetched in this review; therefore this card does **not** upgrade the source to publisher-verified peer-reviewed status. Verify the publisher record before using that label.
- **Review date:** 2026-11-09
- **Status:** FULL_TEXT_REVIEWED / CROSS_LAYER_MOBILE_BENCHMARK / PUBLICATION_STATUS_NEEDS_PUBLISHER_CHECK
- **Decision relevance:** CG-06 (direct), C (direct system scheduling), B-residual (shared-memory/cache boundary), R2 (background context only).

## Q1 — Problem and target mapping

The paper argues that mobile LLM results cannot be understood from nominal TOPS or a single framework. It measures framework, backend, model phase, memory hierarchy and energy attribution together. This is directly relevant to the CPU/LLVM and heterogeneous execution questions in this project, although the experiments are inference benchmarks rather than full Agent workflows.

## Q2 — Experimental scope

- Four Qualcomm smartphones spanning three SoC generations: Xiaomi 14 (SM8650 / NPU V75), Xiaomi 15 (SM8750 / V79), Xiaomi 17 and OnePlus 15 (SM8850 / V81); 16 GB DRAM each.
- Five frameworks: llama.cpp, MLC-LLM, MLLM, MNN and Qualcomm GENIE.
- Three backends: CPU, GPU and NPU.
- Five quantized model families: Llama 3.2 1B/3B, Qwen 2.5 1.5B/7B and Phi 3.5-mini 3.8B.
- More than 400 configurations. The paper uses 4-bit weight quantization by default, with selected W4A16 configurations.
- 256-token prefill/decode benchmark, plus layer/operator and memory/compute microbenchmarks.
- One warm-up and at least three recorded trials. Screen off, airplane mode, background services/notifications/network disabled; only the inference process active.

The controlled, isolated test environment is useful for backend attribution, but it deliberately excludes concurrent foreground apps and does not directly measure a full mobile Agent loop.

## Q3 — Main result 1: framework and operator implementation matter enormously

On OnePlus 15, Qwen2.5-1.5B NPU prefill reaches 1463.7 tokens/s in GENIE, 700.9 in MNN and 115.1 in llama.cpp. Decode throughput is much closer: about 23.0 tokens/s for GENIE versus 22.8 for llama.cpp. The paper attributes the prefill gap to graph offload granularity and operator implementation, not simply to hardware capability. At large MatMul widths, QNN's implementation uses the matrix accelerator and reduces measured cycles by roughly 27–48x versus the compared llama.cpp operator; at decode-like small widths the advantage largely disappears.

**Interpretation:** CPU/NPU/LLVM decisions must be evaluated at operator and phase granularity. A weak custom NPU kernel can lose badly to a mature vendor path even on the same NPU; conversely, a large advertised NPU peak does not predict token decode.

## Q4 — Main result 2: phase-dependent CPU/NPU crossover

For Qwen2.5-1.5B on OnePlus 15, llama.cpp CPU decode is 55.7 tokens/s versus 23.0 tokens/s for GENIE NPU. Across the four Qualcomm phones and tested models, CPU generally leads decode, while NPU leads compute-bound prefill. The paper links this to dynamic small-kernel decode, growing context/KV traffic, static graph shape and cache/memory characteristics.

The microbenchmark discussion reports a much larger CPU cache footprint and cached read bandwidth than the tested NPU path; the reported NPU DDR bandwidth is also lower than CPU/GPU in the tested configuration. These are platform measurements, not universal properties of every NPU or SoC.

## Q5 — Main result 3: host-side control can dominate accelerator energy

PowerBench uses Qualcomm Power Telemetry counters exposed through Linux powercap zones to attribute SoC, CPU, GPU and NPU energy. The paper reports:
- Host CPU can account for up to 30% of measured system energy during NPU inference because of polling/synchronization.
- Adjusting RPC polling interval reduces energy/token by 30.9–37.8% in tested settings.
- Increasing NPU sleep latency from the default can reduce energy/token by 44.6–50.9% in tested settings.
- Thread/core affinity can cause up to 35% performance variance.
- CPU frequency tuning during NPU inference produces up to 39.7% energy reduction in the reported decode case.

The paper's energy-oriented configuration uses a 20 µs polling interval, 65,535 µs NPU sleep latency and low CPU frequency. It estimates 53.6–54.8% lower total energy on three task datasets, but latency rises about 15.1–15.5% on MathQA/RoleBench; the prefill-heavy LongBench case is about 0.8% faster. This is a trade-off, not a free 54% efficiency gain.

## Q6 — Quality, artifact and reproducibility boundaries

- PowerBench is described as a lightweight/header-only C++ library built on Qualcomm Power Telemetry. A public PowerBench source repository was not located in this review; QPT/OnePlusOSS and the manuscript should be checked before claiming the measurement tool is reproducible end-to-end.
- The testbed is Qualcomm-only; no Apple or MediaTek device is included.
- Screen off and isolated inference means no actual foreground Agent/GUI interaction, camera coexistence, or user QoE measurement.
- The frameworks do not all use identical operator maturity or quantization path. The paper exposes this as a result, but it complicates simple hardware-vs-hardware attribution.
- The manuscript's arXiv record lists v1 from 2026-07-06. The manuscript includes POMACS/DOI metadata, but the final ACM publisher record was not independently retrieved in this review.

## Q7 — Facts, inferences and non-claims

- **[FACT]** The paper measures four Qualcomm phones, five frameworks, three backends and more than 400 configurations.
- **[FACT]** In the reported OnePlus 15 Qwen2.5-1.5B case, CPU decode reaches 55.7 tokens/s versus 23.0 tokens/s on GENIE NPU.
- **[FACT]** CPU-side polling, sleep latency, thread affinity and DVFS materially affect accelerator-run energy/performance in the measured environment.
- **[INFERENCE]** CG-06 should explicitly include CPU-local decode and control-path optimization, phase-aware backend dispatch, CPU/accelerator orchestration and LLVM/kernel quality—not merely CPU arithmetic kernel speed.
- **[INFERENCE]** C should include host-side polling, synchronization, sleep/wake and DVFS configuration as first-class Runtime/OS controls.
- **[NOT ESTABLISHED]** These results imply all phone workloads should decode on CPU, or that CPU is always more energy efficient.
- **[NOT ESTABLISHED]** The results prove a new CPU microarchitecture feature, ISA extension or dedicated Agent hardware is needed.
- **[NOT ESTABLISHED]** The isolated benchmark predicts whole-day battery or foreground application QoE.

## Q8 — Decision impact

**Preliminary: STRENGTHEN CG-06 and C as software/system tracks.** This paper is a high-value missed source for the previous repository closure because it provides a cross-layer mobile CPU/GPU/NPU baseline. It does not justify a new hardware Primary Bet. It narrows the question from “NPU vs CPU” to “which phase, operator, framework and host-control regime is actually critical?”

## Q9 — Next action

1. Verify the ACM DOI/publisher record and whether PowerBench source is public.
2. Compare exact device/framework/model settings with Tandem and sd.npu; avoid merging their numbers.
3. Build a phase/backend/energy table for CG-06.
4. Search for independent results on MediaTek/Apple and real foreground Agent workloads.

## Evidence footer

Original arXiv full text read. The DOI and POMACS metadata are present in the manuscript, but publisher status and PowerBench artifact availability remain unverified in this review. Confidence: high for the reported test setup and within-paper results; medium for transfer to other vendors and full Agent workloads.


## 2026-11-09 baseline-currentness correction

The paper's framework table lists Qualcomm GENIE **2.39.0**. Qualcomm's official QAIRT HTP documentation, updated 2026-09-03, now identifies LLM Decode performance modes as new in QAIRT **2.48** and supported on Hexagon V79+ (including the V79/V81 phones in this paper). These modes explicitly reduce HMX frequency for memory-bound decode while scaling DDR/HVX/CENG; the same SDK also exposes CPU/HTP performance infrastructure and RPC control-latency configuration.

Official reference: https://docs.qualcomm.com/bundle/publicresource/topics/80-63442-10/htp_backend.html

Therefore the paper's best-practice configuration and 53.6–54.8% estimated energy reduction should be read as measured against its 2.39-era framework/runtime baseline, not as the latest available Qualcomm profile. The result remains important, but a current comparison needs QAIRT 2.48 decode profiles as an additional baseline. This is a baseline-freshness issue, not evidence that the newer profiles automatically solve Agent-level scheduling.
