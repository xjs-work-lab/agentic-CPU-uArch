# VENDOR-026 — Source deep review / 10Q

**Primary:** https://machinelearning.apple.com/research/hey-siri
**Date reviewed:** 2026-10-08
**Independence:** OFFICIAL_APPLE_ENGINEERING_ACCOUNT_HISTORIC_PRIOR_ART
**Source type:** Official platform documentation / vendor engineering information; no independent device benchmark implied.

## Q1 — Problem
Continuous wake-word listening on iPhone without keeping main processor active throughout the day.

## Q2 — Mechanism
iPhone's Always On Processor (AOP) uses a compact on-device DNN on microphone samples; on sufficient score it wakes the application processor for a larger second-pass detector. Initial disclosed example: five 32-unit hidden layers versus five 192-unit layers.

## Q3 — Control
Threshold-based two-pass gating; a time-bounded second-chance lower-threshold state handles near misses. Optional speaker-verification stage reduces impersonation and false wakes.

## Q4 — Evaluation
Article discusses false accepts (per hour) and false rejects, long negative-audio testing and production sampling. It does not publish a matched Agent-level energy comparison. False wake and missed wake are different metrics.

## Q5 — Hardware relevance
Direct historical iPhone demonstration of always-on tiny-model execution on a low-power auxiliary processor and threshold-triggered AP escalation.

## Q6 — Workload difference
Wake-word spotting over a narrow audio pattern is not long-horizon multimodal latent-intent prediction, continuous screenshot understanding, or cross-app actions. Do not transfer accuracy or battery cost as equivalent.

## Q7 — Source depth
Reviewed complete Apple Research engineering article, including detector DNN design, responsiveness/power two-pass section, personalized scoring and testing/tuning methodology; published 2017-10-01.

## Q8 — Prior art
Kills broad novelty of a tiny always-on classifier waking a larger processor, and of general false-wake/false-miss threshold balancing.

## Q9 — Remaining Agent-specific gap
The composition of privacy-governed temporal context, personalized multi-intent no-action gating, multi-stage xPU escalation and useful state transfer is distinct, but still only a hypothesis for hardware-specific residual.

## Q10 — Next
Do not pursue simple wake-word-trigger generalization as a new bet. Investigate whether richer multimodal proactive state requires novel contextual handoff/permission or whether CHRE-style nanoapps plus software gates suffice.

## Decision footer
- **AO-4 impact:** PRIOR_ART_BOUNDARY / two-stage always-on detection and wake-up
- **Evidence maturity:** PRODUCT_OR_PLATFORM_ARCHITECTURE_SIGNAL; not phone Agent SYSTEM_VALUE
- **No hardware promotion:** no
- **Source identity:** original URL is unique against existing canonical official sources in this SSOT
- **Primary:** https://machinelearning.apple.com/research/hey-siri
