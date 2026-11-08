# Tandem public artifact audit — 2026-11-09

## Repository identity and provenance

- Repository: https://github.com/flyingdoog/tandem
- Default branch: tandem
- GitHub API identifies it as a public fork of llama.cpp, MIT licensed.
- README says based on llama.cpp b11200 and describes the project as a drop-in replacement for llama-server.
- The code is inspectable; this is stronger artifact availability than a paper-only result. It is not independent replication or broad community validation.

## Source-level verification performed

### 1. Idle power release is implemented in the backend, not merely proposed

Source:
- Host backend: https://github.com/flyingdoog/tandem/blob/tandem/ggml/src/ggml-hexagon/ggml-hexagon.cpp#L105
- Power state machine: https://github.com/flyingdoog/tandem/blob/tandem/ggml/src/ggml-hexagon/ggml-hexagon.cpp#L4335
- Wake/restore path: https://github.com/flyingdoog/tandem/blob/tandem/ggml/src/ggml-hexagon/ggml-hexagon.cpp#L4385
- Idle timer loop: https://github.com/flyingdoog/tandem/blob/tandem/ggml/src/ggml-hexagon/ggml-hexagon.cpp#L4410
- DSP-side HTP power requests: https://github.com/flyingdoog/tandem/blob/tandem/ggml/src/ggml-hexagon/htp/main.c#L716
- DSP interface entry: https://github.com/flyingdoog/tandem/blob/tandem/ggml/src/ggml-hexagon/htp/main.c#L783

Code behavior observed:
- Default idle threshold is 3,000 ms; it can be disabled.
- The host timer checks request/response sequence counters. It does not relax votes while an op batch is still in flight.
- On idle, the DSP-side implementation removes the explicit bus-bandwidth vote, powers HMX down, restores default DCVS, removes protected-bus and DDR-performance votes.
- On the next batch, the host restores the saved DCVS/HMX/bandwidth requests and checks that the clock readback returns to at least the previous values, with a bounded wait.
- The model weights remain resident; the power votes are relaxed, not the model/server memory allocation.

This is direct code evidence that an application/runtime can implement idle NPU power management using existing Hexagon/FastRPC power interfaces. It does not establish identical API behavior on other OEMs or other accelerator backends.

### 2. Failure handling is part of the implementation

The host path retries a failed restore (10 ms, then 40 ms); after three failures it marks the power state faulty and refuses to submit further batches, so the server aborts rather than sending work to an NPU whose power state is unknown. The repository history includes a fault-injection commit (2026-10-03) reporting tests on Snapdragon 8 Elite: identical answers and first-token log probabilities on 61 prompts, and process exit within one second after injected restore failures.

Commit:
https://github.com/flyingdoog/tandem/commit/5148aa41982f087f19f6ed2491c759750b66661b

### 3. Measurement discipline

The artifact README states the main comparison is on OnePlus 13T, Snapdragon 8 Elite / Hexagon v79, 16 GB, Android 16, with a fine-tuned Qwen3.5-4B Q4_K_M policy. It uses 61 text requests and 21 screenshot requests from the deployed agent's traffic. It reports the same llama.cpp b11200 baseline and states the model/server is compared with the fastest NPU configuration.

A separate documentation commit says measurements were rerun with the screen on during every measurement because screen-off policy caps CPU and disproportionately slowed CPU baseline:
https://github.com/flyingdoog/tandem/commit/168213c51a0fce3dc0258f8e2840b2aabd294239

This is an important methodological detail: screen-on/off state materially changes CPU comparison. The project review must preserve the stated screen-on condition when quoting the 1.38 s vs 1.96 s and 4.76 s vs 5.66 s numbers.

### 4. Model and architecture generalization

The README says:
- Qwen3.5 2B/4B/9B are tested.
- LFM2 and Granite 4.0-H support the checkpoint policy and idle power release.
- Gated DeltaNet-specific kernels and MTP mechanisms do not apply to those other architectures.

Therefore the full reported performance package should not be generalized to arbitrary models; only the architecture-independent checkpoint/power parts have broader stated applicability.

### 5. Artifact status and limitations

- Public source exists and can be inspected.
- Repository metadata at retrieval: MIT license, fork=true, default branch tandem, 4 stars and 0 forks. This is an early research artifact, not evidence of adoption.
- No independent third-party reproduction was identified.
- The project is tightly coupled to Qualcomm Hexagon v79/v81; v73/v75 builds are described as untested.
- No Android OEM integration or AOSP NPU Manager integration is demonstrated.
- A separate code-level audit of the DMA state-copy coherence fix is still needed before treating all paper-reported cache-maintenance details as source-verified.

## Implication for the research portfolio

This audit upgrades the artifact confidence of Tandem's specific runtime claims. It narrows B-residual for:
- recurrent-state checkpoint reuse;
- speculative rollback state;
- NPU session power-vote release;
- one reported DMA/cache-maintenance path.

It does **not** eliminate B-residual as a broader cross-CPU/NPU/DRAM validity problem. The paper and code show one concrete implementation can handle specific state transfers with OS/runtime mechanisms; they do not cover every accelerator, every state type, or a universal coherence contract.

No new CPU hardware/ISA need is established.
