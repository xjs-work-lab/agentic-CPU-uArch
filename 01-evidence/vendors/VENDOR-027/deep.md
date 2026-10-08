# VENDOR-027 — Primary-source technical 10Q

- Original: https://source.android.com/docs/core/perf/npu-manager
- Date reviewed: 2026-10-08
- Evidence depth: FULL_10Q — ANDROID_OFFICIAL_PLATFORM_DOC
- Decision role: P0 / direct AO1+AO2+AO3 strongest OS-level scheduling and cancellation baseline

## Q1 — Research problem
OS lacks predictable arbitration when LLM/camera/assistant workloads compete for NPU SRAM, weights and channels; direct vendor daemons produce priority conflicts, thermal and memory problems.

## Q2 — Why relevant now
Android 17+ public platform documentation introduces com.android.npumanager; this is modern smartphone platform architecture, not a 2004 scheduling algorithm. Not an Agent-specific progress ISA.

## Q3 — Falsifiable comparison
The document describes an OS mediator that can control model-load admission, reprioritization, system unload, and execution events. Its existence challenges the idea that these controls must be invented as Agent-specific new silicon.

## Q4 — Lineage and competing solutions
Earlier private vendor daemon/driver control; classic QoS; Android NNAPI burst and third-party accelerator runtime APIs. This is a *platform specification*, not a measured comparative experiment.

## Q5 — Mechanism/control
Framework NpuManager, system npu service and android.hardware.npu AIDL Scheduling HAL. ModelLoadRequest has ID, size class, priority. requestCanLoadModel grants load; notifyModelLoaded/notifyModelUnloaded complete lifecycle. Callback can request unload under foreground or thermal pressure; scheduling configuration includes appPriority/UID and driver role.

## Q6 — Work lifecycle specifics
WorkInfo status with queued/start/resume and ended/completed, cancelled by user, cancelled by system, paused and failed reasons. Event debouncing reduces callback storms. Supports model-load requests and preemption flow, but full GPU/CPU/NPU hardware coherence not specified.

## Q7 — Reported evaluation
The official page provides API/system design and VTS conformance hooks, no measured Agent latency, interrupt-to-resume cost, model memory reclamation time or battery. This is an API/capability evidence class, not phone Agent SYSTEM_VALUE.

## Q8 — Implementation/reproducibility
Official AOSP 2026-06-25 doc shows ModelLoadRequest, NPU Scheduling HAL structures, WorkInfo and callbacks; implementation and vendor HAL support remain device/version dependent. Android 17 support does not mean deployed on all retail phones.

## Q9 — Decision impact
Strong direct baseline for AO1 mixed-criticality NPU priority, AO2 NPU cancellation/preemption signals and AO3 model residency/reclaim. Kills broad newness of 'OS system NPU manager', 'work cancel event', 'model loading priority'. Residual possible only for Agent-private version/utility semantics and cross-engine physical state lifecycle beyond this interface.

## Q10 — Follow-up
Track release/vendor implementation evidence and public API semantics; compare public hardware descriptors before narrowing a new CPU-uArch concept. No experiments scheduled.

## Evidence footer
- Directly supported: published API, product, mechanism, implementation or migration text **inside the specific source's scope**
- Research inference: how that baseline narrows Agentic hardware novelty
- Not established: incremental Agent-specific CPU-uArch value, deployment on all Android devices or matched battery/foreground-QoE results
- No local experiments conducted or planned
