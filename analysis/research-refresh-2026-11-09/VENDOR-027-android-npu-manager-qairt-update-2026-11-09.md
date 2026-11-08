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


## Important QAIRT 2.48 finding — phase-specific LLM decode performance profiles

Official HTP backend documentation: https://docs.qualcomm.com/bundle/publicresource/topics/80-63442-10/htp_backend.html  
The page states **Updated: 2026-09-03**, QAIRT SDK 80-63442-10, API version 5.50.0, and identifies the LLM Decode performance modes as **new in version 2.48**.

The documented modes include:
- llm_decode_burst
- llm_decode_sustained_high_performance
- llm_decode_high_performance
- llm_decode_balanced / low_balanced / default
- llm_decode_high_power_saver / power_saver / low_power_saver / extreme_power_saver

The docs state these modes are supported on Hexagon V79 and newer (V79, V81, V85, V89). They explicitly distinguish prefill/encode (compute-bound, HMX-heavy) from decode (memory-bandwidth-bound, narrow GEMV). The decode profiles reduce HMX frequency aggressively while scaling DDR bus, HVX core and CENG by performance tier; DDR Perf Mode is enabled only for the highest decode burst profile. The documentation also describes per-stage INIT / INFERENCE / DE-INIT application and lower votes after stage completion.

The same QAIRT docs expose QNN HTP Performance Infrastructure APIs to control CPU and HTP system settings, including DCVS/clock/voltage votes and RPC control latency. The docs recommend >0 and <200 µs for latency-critical applications, versus default 0 µs when no special latency setting is needed. They also document explicit power-config creation, setting and removal APIs.

### Why this matters to PAPER-124

PAPER-124's framework table identifies Qualcomm GENIE version **2.39.0**, whereas the current public QAIRT docs describe 2.48 LLM-decode profiles. The PAPER-124 experiments therefore do **not** establish performance/energy results against these newer decode profiles. The paper's 20 µs polling / 65,535 µs sleep / low-CPU-frequency policy is a useful measurement result, but it should not be treated as the current strongest Qualcomm vendor baseline until compared with QAIRT 2.48's phase-specific profiles and RPC control-latency options.

This is a key **baseline-freshness gap**, not proof that QAIRT 2.48 solves all scheduling. The profiles are selectable backend performance configurations; the application still needs to choose an appropriate profile for the current phase and workload. The documentation does not show automatic semantic Agent scheduling, output freshness, cross-app deadlines or full GUI action progress.

### Updated project interpretation

- The vendor stack already exposes more phase-aware decode power policy than the October 8 summary recorded.
- This narrows the novelty of generic "lower HMX, keep DDR/HVX appropriate" power tuning as a new research contribution.
- A remaining CG-06 opportunity is to measure and coordinate CPU-side dispatch/polling/affinity, phase transitions, model/backend selection and Agent foreground QoE **against the latest QAIRT profiles**, not against older defaults alone.
- No new CPU ISA or microarchitecture feature follows from this documentation.
