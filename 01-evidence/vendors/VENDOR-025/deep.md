# VENDOR-025 — Source deep review / 10Q

**Primary:** https://www.qualcomm.com/snapdragon/smartphones/ai
**Date reviewed:** 2026-10-08
**Independence:** VENDOR_SELF_REPORT
**Source type:** Official platform documentation / vendor engineering information; no independent device benchmark implied.

## Q1 — Public disclosure
Qualcomm's official smartphone AI page describes a low-power Sensing Hub enabling continuous background context processing, with Dual Micro NPUs for audio/voice/sensors and dual always-sensing ISPs; it positions the design for personal/proactive AI.

## Q2 — Mechanism
Separate always-on sensing/ML compute path alongside a higher-performance Hexagon NPU and application processing. Vendor highlights local, low-power context capture and personal-context representation.

## Q3 — Target workload
Sustained multimodal observation and personalized assistant context, distinct from running a heavy full Agent reasoner on each event.

## Q4 — Quantitative evidence
The reviewed smartphone AI page provides no matched third-party millijoule/event, screen-off power, false wake or actual proactive intervention duty-cycle benchmark for the sensing-hub claim.

## Q5 — Evidence classification
Disclosure of named sensing processors and ISPs is a product-architecture signal. Efficiency and proactive-user-value statements are vendor-origin, not independently verified.

## Q6 — Relationship to MediaTek
VENDOR-019 describes a dedicated Super Efficient NPU 2.0 alongside NPU 1090. These vendor descriptions support architectural market convergence, not equivalence of microarchitectures or an independently replicated measured outcome.

## Q7 — Existing ecosystem
AOSP CHRE (VENDOR-024) and Apple's old AOP two-pass wake path (VENDOR-026) demonstrate established low-power event filtering; this Qualcomm source is an additional product signal, not a new invention claim.

## Q8 — Scope boundary
No public mapping here from generic dual micro-NPU sensing to trustworthy per-user proactive Agent intervention, permissions, tool/intent routing or context-handoff cost. Dynamic web page; recheck snapshot when used in roadmap.

## Q9 — AO-4 impact
Raises competitive baseline beyond MediaTek-only dual NPU: dedicated efficient event sensing is already a broad smartphone strategy. Strongens follow/product relevance, weakens generic differentiated hardware novelty.

## Q10 — Next
Track actual wake granularity, hub model footprints, sensor-fusion APIs, AP/NPU escalation state transfer and foreground QoE on future independent device traces.

## Decision footer
- **AO-4 impact:** PRODUCT_SIGNAL / competing low-power contextual sensing domain
- **Evidence maturity:** PRODUCT_OR_PLATFORM_ARCHITECTURE_SIGNAL; not phone Agent SYSTEM_VALUE
- **No hardware promotion:** no
- **Source identity:** original URL is unique against existing canonical official sources in this SSOT
- **Primary:** https://www.qualcomm.com/snapdragon/smartphones/ai
