> V1 semantic source copied/repacked from frozen baseline `960abb4ef50f050da3c6784d30826053d42e5c5d`.

## PAPER-029 — [An Efficient Context Management System for On-Device LLMaaS](https://doi.org/10.1145/3774906.3800479)

**Authors:** Wangsong Yin, Mengwei Xu, Yuanchun Li, Xuanzhe Liu  
**Venue/status:** SenSys 2026

### Background
If an on-device LLM becomes an OS-level service shared by multiple applications, each application can maintain a large persistent context, dominated by KV cache. Mobile RAM cannot keep every context resident.

### Problem
Naive app-level memory management or coarse disk swapping makes context switching expensive when many stateful LLM clients coexist.

### Method
Libra decouples LLM context management from applications and manages KV state in fine-grained chunks. It combines:
- tolerance-aware per-chunk compression;
- a swapping/recompute pipeline;
- chunk lifecycle / ahead-of-time swap policy.

The authors implement the system on COTS edge/mobile devices, including a smartphone configuration with UFS storage and a heterogeneous mobile SoC.

### Main conclusion
The paper reports large context-switch latency reductions versus its selected mobile/edge baselines, including up to 20× and 9.7× average improvement over a strong chunk-based baseline.

### What we learn
Libra strengthens the M3 reframe: **persistent model/context state is a real mobile-system problem, but much of its value can be captured by runtime + memory/storage management without CPU microarchitectural changes.**

For C1, this is pressure on StateAffinity as a mandatory ABI field. Before adding explicit semantic state identity, B4 must include capable context managers and history/prediction.

### Boundary
This is LLM context/KV management, not an Agent workflow semantic study. It does not measure CPU cache/TLB/predictor continuity or prove a CPU-uArch requirement.

---
