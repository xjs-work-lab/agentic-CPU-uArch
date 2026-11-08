# PAPER-122 / PAPER-123 second-pass full-text cross-check — 2026-11-09

This note refines the initial evidence cards after reviewing full paper sections, the Tandem artifact README, and AOSP/QNN platform documentation. It supersedes any abbreviated interpretation in the first discovery note where the details below differ.

## PAPER-122 EdgePace — refined facts and limits

**Original:** https://arxiv.org/abs/2610.37307  
**Version:** v1, submitted 2026-10-27; arXiv preprint.  
**Authors/institutions:** Teng Mei, Chengxuan Pei, Weijun Wang, Jie Wu, Marco Canini, Yunming Xiao; CUHK-Shenzhen, Tsinghua AIR, Fudan, KAUST.  
**Target:** OnePlus 13 / Snapdragon 8 Elite plus three NVIDIA Jetson platforms.

### Exact mechanism

- Fine Plan divides prefill and decode into legal sublayer submission quanta.
- Monitor samples four foreground CPU PMU counters: CPU cycles, retired instructions, LLC read misses, and memory-related backend stall cycles.
- It normalizes LLC misses per second, MPKI and stall fraction; scheduler consumes a shared-memory snapshot rather than reading counters in each submission decision.
- Scheduler chooses Bypass, Admit or Hold at safe boundaries; freshness urgency can override a high-risk Hold.
- The code changes the llama.cpp backend submission path, not model kernels or CPU ISA.

### Exact OnePlus example

For the OnePlus 13 camera workload with Qwen2.5-1.5B, deadline misses fall from 66.78% unmanaged to 5.83% (91.3% relative reduction) while 90.4% of unmanaged LLM throughput is retained (10.188 tokens/s). The paper also reports MNN and QAIRT comparisons in the phone case, but it does not report a direct SERENO implementation/run.

### PMU overhead — do not misattribute

The detailed PMU read-cost table is measured on **Jetson Orin Nano Super**, not the OnePlus 13:
- 2 ms sampling: median 80.9 µs read, 4.04% of the interval.
- 20 ms sampling: median 130.8 µs read, 0.65% of the interval.
- Local decision check averages 1.856 µs.
These percentages are sampling cost relative to the interval, not application slowdown or total CPU utilization. The OnePlus PMU sampling overhead is not separately reported in the retrieved result.

### Strongest limitations

- One phone model for the smartphone case; the other platforms are Jetson.
- OnePlus workload is foreground camera processing plus background LLM feedback, not a complete GUI Agent action loop.
- Risk calibration is required for each platform and foreground load.
- EdgePace explicitly cites SERENO and distinguishes its workload/control point, but no head-to-head SERENO comparison is reported.
- No public EdgePace code/artifact was located in this review.

**Interpretation:** Strong C evidence and useful CG-06 PMU feedback example; not a new hardware primitive and not proof of a universal Android PMU interface.

## PAPER-123 Tandem — refined facts and limits

**Original:** https://arxiv.org/abs/2610.26660  
**Artifact:** https://github.com/flyingdoog/tandem  
**Version:** arXiv preprint, submitted 2026-10-19.  
**Authors:** Zhuomin Chen, Jingchao Ni, Xu Zheng, Yong Chen, Mo Sha, Wei Cheng, Dongsheng Luo. The team/institutions are distinct from EdgePace, SERENO and HeRo/Agent.xpu in the current source set.

### Devices, model and workload

- Primary: OnePlus 13T, Snapdragon 8 Elite, Hexagon v79, 16 GB, Android 16.
- Next generation: OnePlus 15, Snapdragon 8 Elite Gen 5, Hexagon v81, 16 GB, Android 16.
- Main policy: LoRA-fine-tuned Qwen3.5-4B, Q4_K_M.
- Main trace: 61 text requests and 21 screenshot requests.
- Additional: 510 held-out steps from 54 episodes in 12 apps; AndroidControl's 300 public test steps from 56 episodes; 100 real tasks in 17 phone apps.
- Baseline: llama.cpp b11200 fastest NPU configuration, without speculation, with the same work-queue correctness fix. MNN and CPU/GPU backends are also measured.

### Mechanisms and exact scope

1. Divergence-point recurrent checkpoints: save where consecutive Agent prompts stop sharing a prefix.
2. Remove chat-only tail passes and repeated state snapshots.
3. Keep most prefill on matrix kernels; create short rollback-state tail for speculative decoding.
4. Column-shared verification kernel reuses each weight block across proposed tokens.
5. Idle power release after 3 seconds with no submitted/in-flight batch: drops bandwidth vote, powers down HMX, drops DDR performance mode and restores platform defaults; before next batch, restores active votes and waits for clocks.
6. The model remains loaded in memory; the app unloads the server after a separate five-minute idle timer.

### Results and correct denominators

- On Snapdragon 8 Elite, paper summary reports 30% lower text-step latency, 16% lower screenshot-step latency and 33% lower energy per text step versus llama.cpp's fastest NPU configuration.
- Standby power with model loaded and screen off falls from 0.76 W to 0.22 W. This is standby power, not active inference power or all-day battery.
- On Snapdragon 8 Elite Gen 5, text-step latency reduction is 27%; screenshot-step reduction is about 16%.
- AndroidControl: 28% lower text-step latency and 13% lower screenshot-step latency in the reported 300-step test.
- The paper reports action fidelity: optimizations change at most one free-text summary per trace in the cited tests and do not change action outputs in those tests.
- CPU/GPU baselines are much slower in the paper's tested Qwen3.5-4B configuration, but those numbers are model/backend/device-specific and should not be generalized to all phone LLMs.

### Critical B-residual boundary: DMA coherence is software-maintained

The paper describes a concrete DMA/cache issue: a convolution writes input through DMA, while a state-copy operator reads through the NPU data cache; stale cache lines can copy an earlier layer's state for small batches. Tandem cleans and invalidates the source range through the operating system before reading. This is a real state-validity problem, but the reported solution is explicit OS cache maintenance, not a new CPU hardware state register. It narrows the broad B-residual claim while leaving other cross-engine cases open.

### Artifact and generalization

- Public MIT-licensed llama.cpp fork, based on b11200, adding about 3,000 lines of C/C++ across 24 files.
- Qwen3.5 2B/4B/9B tested; LFM2 and Granite 4.0-H also tested for checkpoint policy and idle power release. Gated DeltaNet kernels and MTP mechanisms do not apply to those other architectures.
- Main results are Qualcomm-only (Hexagon v79/v81); other accelerator backends need their own matrix/vector kernels and power integration.
- The paper is a preprint; no independent third-party replication is identified.

**Interpretation:** Strong direct mobile GUI-Agent evidence for software runtime, recurrent state reuse and NPU power management. It materially narrows B-residual for these specific mechanisms; it does not prove all cross-CPU/NPU/DRAM coherence or all Agent progress state is solved.

## Cross-paper lineage summary

- EdgePace and Tandem are independent author groups and target different workloads: sensor/camera feedback versus GUI action loops.
- EdgePace cites SERENO but has no head-to-head comparison; it extends the problem framing with deadlines/freshness and PMU signals.
- Tandem's open artifact gives stronger inspectability than EdgePace's currently located artifact record.
- Neither paper demonstrates a new CPU ISA or a hardware feature that cannot be expressed in existing runtime/vendor APIs.
