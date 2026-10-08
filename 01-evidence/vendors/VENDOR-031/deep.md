# VENDOR-031 — Primary-source technical 10Q

- Original: https://developer.android.com/ai/gemini-nano
- Date reviewed: 2026-10-08
- Evidence depth: FULL_10Q — ANDROID_OFFICIAL_PRODUCT_DOC
- Decision role: Official on-device AI service and privacy boundary (AO4+AO5 software platform baseline)

## Q1 — Research problem
Applications need on-device foundation models with model distribution, resource updates and privacy/safety controls.

## Q2 — Product/UX direction
Android AICore offers on-device Gemini Nano to ML Kit GenAI/Prompt/Summarization interfaces, using device hardware and model update infrastructure.

## Q3 — Mechanism
System service exposes higher-level models with safety and model updates and hides detailed hardware interface from apps; local request execution.

## Q4 — Current software baseline
Managed model caching/distribution and accelerator usage are already platform capabilities. Not a proof of specialized Agent execution-state coherence.

## Q5 — Security/permission
Official documentation says restricted package binding, indirect internet through Private Compute Services, request isolation without retaining input/output; privacy governance is part of correct Agent systems.

## Q6 — Research scope
Product/runtime design only; cannot assume arbitrary always-on Agent can read every context signal or third-party package can use private AICore capabilities.

## Q7 — Measurement evidence
No direct multi-agent foreground-QoE or battery/thermal quantification; no OS-level hidden DemandState API described.

## Q8 — Source
Official Android Gemini Nano page (2026-04-02) describes ML Kit feature classes and service/security architecture.

## Q9 — AO4/AO5 meaning
Consent, package trust, model service and safety constraints may dominate willingness to surface intent/progress metadata across system layers; first exploit existing AICore gate/runtimes.

## Q10 — Next
Observe official expansion of privacy-aware on-device agent APIs rather than assume new silicon is needed.

## Evidence footer
- Directly supported: published API, product, mechanism, implementation or migration text **inside the specific source's scope**
- Research inference: how that baseline narrows Agentic hardware novelty
- Not established: incremental Agent-specific CPU-uArch value, deployment on all Android devices or matched battery/foreground-QoE results
- No local experiments conducted or planned
