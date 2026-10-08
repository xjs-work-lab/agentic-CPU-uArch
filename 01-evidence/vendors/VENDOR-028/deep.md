# VENDOR-028 — Primary-source technical 10Q

- Original: https://source.android.com/docs/core/interaction/neural-networks/burst-executions
- Date reviewed: 2026-10-08
- Evidence depth: FULL_10Q — ANDROID_OFFICIAL_HISTORICAL_HAL_DOC
- Decision role: P0 / established dispatch-resource-persistence baseline

## Q1 — Research problem
Repeated inference frames or audio events incur framework→driver messaging and buffer-map overhead.

## Q2 — New-regime mapping
NN HAL 1.2 already offered rapid same-model burst execution, lifetime hints, persistent resource reuse and shared-memory FMQ, independent of Agent workloads.

## Q3 — Mechanism testable statement
Burst object hints high-performance driver state duration; mappings can be cached across requests; FMQ bypasses HIDL serialization path. These mechanisms challenge 'persistent execution context' generic novelty.

## Q4 — Lineage
Historical NN HAL 1.2/HIDL FMQ, later modern NN HAL AIDL, vendor QNN and new Android NPU Manager. NNAPI NDK API itself deprecated since Android 15.

## Q5 — Control point
IBurstContext, configureExecutionBurst, cached memory mappings, Request/Result FMQs; listener thread processes channel and releases resources on client demise.

## Q6 — Evidenced results
Official documentation shows code/semantics and describes intended latency reduction; it does not give numeric phone-energy or Agent-concurrency results.

## Q7 — Failure modes
FMQ has no intrinsic cross-process lifetime guarantee; stale/dead producer could strand consumer; bound to burst context to detect end. POD-only payload and callbacks for memory handles are constraints.

## Q8 — Status and public applicability
Official AOSP doc 2026-07-13; historical HAL infrastructure survives as prior art. Do not recommend NNAPI NDK API as new 2027–29 application integration surface after its Android 15 deprecation.

## Q9 — AO1/AO3 meaning
Low-IPC launch, resource-map reuse and lifecycle hints existed; remaining gap must be **Agent revision across varying models/engines**, not same prepared model burst.

## Q10 — Next
Use as negative baseline for novelty, track current vendor-specific memory registration plus Android 17 NPU manager; no new test execution.

## Evidence footer
- Directly supported: published API, product, mechanism, implementation or migration text **inside the specific source's scope**
- Research inference: how that baseline narrows Agentic hardware novelty
- Not established: incremental Agent-specific CPU-uArch value, deployment on all Android devices or matched battery/foreground-QoE results
- No local experiments conducted or planned
