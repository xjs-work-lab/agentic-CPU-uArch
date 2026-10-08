# VENDOR-030 — Primary-source technical 10Q

- Original: https://developer.android.com/ndk/guides/neuralnetworks/migration-guide
- Date reviewed: 2026-10-08
- Evidence depth: FULL_10Q — ANDROID_OFFICIAL_LIFECYCLE_DOC
- Decision role: API evolution / avoid deprecated NNAPI as 2027+ investment

## Q1 — Research problem
ML acceleration needs rapid runtime update cycles beyond a static neural-network OS application API.

## Q2 — Product signal
Android officially deprecated NNAPI NDK API in Android 15, citing Transformer/diffusion and model/runtime innovation.

## Q3 — Mechanism
Google directs developers to updatable TensorFlow Lite in Play Services, optional GPU delegate and AICore for foundation models/Gemini Nano.

## Q4 — Prior art
Existing NNAPI/HAL is historical mechanism evidence but not a default forward-facing integration proposal. NN HAL interface remains supported in Android official AOSP driver documentation.

## Q5 — Control
Public app developers select supported runtime/delegate/APIs; inference scheduling and driver backend may remain vendor owned. No new hardware policy exposed.

## Q6 — Results
No benchmark; official lifecycle/guidance statement only.

## Q7 — Transfer
Android ecosystem applicable, not proof all OEMs moved or NN HAL removed.

## Q8 — Confidence
Full short migration page verified; last updated 2026-03-06.

## Q9 — Implication
Roadmap should focus portable compiler/runtime/driver contracts and updated NPU manager, not revive NDK NNAPI API.

## Q10 — Next
Track supported LiteRT/TFLite/AICore and vendor runtime evolution from official sources.

## Evidence footer
- Directly supported: published API, product, mechanism, implementation or migration text **inside the specific source's scope**
- Research inference: how that baseline narrows Agentic hardware novelty
- Not established: incremental Agent-specific CPU-uArch value, deployment on all Android devices or matched battery/foreground-QoE results
- No local experiments conducted or planned
