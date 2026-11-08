# VENDOR-027 update — Android NPU Manager and Qualcomm QAIRT control boundaries (2026-11-09)

This dated review supplements the existing FULL_10Q source review dated 2026-10-08; it does not replace the frozen historical review.

## AOSP Android 17 NPU Manager — exact public scope

Official documentation: https://source.android.com/docs/core/perf/npu-manager  
Last updated on the AOSP page: 2026-06-25.

The framework service com.android.npumanager exposes:
- model-load admission requests with request ID, coarse model-size class and priority;
- callback approval and model-loaded notification;
- unload requests when system resource pressure or thermal conditions require model release;
- Scheduling HAL app priority configuration;
- work lifecycle callbacks for requested, started, resumed, completed, user/system-cancelled, failed and paused work.

The API does not itself execute inference. Actual work still goes through vendor SDK/driver, and device-specific vendor implementations must implement the android.hardware.npu AIDL service. The published contract is therefore a system arbitration/lifecycle baseline, not proof that every retail Android 17 device implements identical preemption behavior.

## CTS evidence and its limits

Official CTS guide: https://source.android.com/docs/compatibility/cts/npu-cts  
Last updated on the AOSP page: 2026-07-07.

CtsNpuManagerMoblyTestCases checks NPU workload priority and access control. The documented foreground-before-background test is race-based, and its parameters must be tuned to the device. The default configuration runs 120 background inferences, waits 0.5 seconds, then starts 120 foreground inferences; the test is expected to pass two of three runs. This is compatibility evidence for prioritization, not a measured QoE/energy guarantee, Agent semantic scheduler, or proof of universal vendor deployment.

## Qualcomm QAIRT/HTP software control

Official QAIRT SDK references:
- https://docs.qualcomm.com/doc/80-63442-10/topic/htp_backend.html
- https://docs.qualcomm.com/bundle/publicresource/topics/80-63442-10/java_interface.html
- https://docs.qualcomm.com/doc/80-63442-10/topic/options.html

The current public SDK documentation exposes manual/automatic HTP performance-control strategy and a Java performanceRelease() method described as manually releasing the performance vote. The manual strategy votes while the backend is initialized and releases performance at backend destruction; other lower-level power infrastructure APIs allow clients to manage performance configurations. This confirms that performance-vote control is software-visible. It does not prove that all apps or SDK versions can release/restore votes with the same semantics while retaining a loaded model, nor does it expose a generic per-sublayer inference suspension API.

Tandem's own implementation is a concrete demonstration of runtime-managed idle NPU power release while retaining model weights. Treat this as a backend-specific software capability, not a new hardware primitive.

## Updated interpretation

- **Already covered by platform/runtime:** model admission, priority arbitration, model unload requests, work lifecycle, system cancellation/paused/resumed reporting, and manual performance-vote control.
- **Still not covered by these interfaces:** Agent-specific semantic progress, task utility, freshness windows, cross-tool completion requirements, and the policy that chooses which useful work should continue.
- **Still unproven:** identical availability across all OEM Android 17 devices, fine-grained subgraph preemption support across vendor backends, and any incremental CPU-uArch/ISA value.

**Decision impact:** reinforces C's software/platform baseline; narrows any claim that NPU priority, lifecycle, cancellation or power-vote release is novel hardware territory. No formal portfolio change.
