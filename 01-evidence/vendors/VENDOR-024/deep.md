# VENDOR-024 — Source deep review / 10Q

**Primary:** https://source.android.com/docs/core/interaction/contexthub
**Date reviewed:** 2026-10-08
**Independence:** OFFICIAL_AOSP_PLATFORM_DOCUMENTATION
**Source type:** Official platform documentation / vendor engineering information; no independent device benchmark implied.

## Q1 — Problem and product scope
Android documents that the main applications processor (AP) is inefficient for frequent, short context events while screen-off; CHRE is a portable runtime for small trusted nanoapps on a lower-power processor.

## Q2 — Mechanism
CHRE is an event-driven C/C++ nanoapp environment implemented on a vendor-specific low-power processor. Context Hub HAL uses AP↔hub messaging and nanoapp discovery/load/unload; nanoapps use event handlers and sensor/GNSS/Wi-Fi/WWAN/audio interfaces.

## Q3 — Workload
Short bursts of sensor and contextual inference without waking the AP, not complex general-purpose cross-app Agent intent/action pipelines.

## Q4 — Quantitative evidence
Official documentation offers architectural claims about avoiding AP wakes and reduced battery cost, not a normalized joules/event improvement against a specific Agent workload.

## Q5 — Control point
Place trusted sensing/preprocessing near always-on signals, batch/triage events, escalate selected events through HAL message passing.

## Q6 — Constraints
CHRE is system-trusted, not available to arbitrary third-party apps. Nanoapps have restricted C/C++ libraries and resource budgets; CHRE is distinct from Sensors HAL and vendor sensor framework.

## Q7 — Provenance
Primary: Android Open Source Project architecture/reference API documentation; review included 'Key concepts', 'Context Hub HAL', 'CHRE system overview', 'Mandatory system features', and optional sensor/GNSS/Wi-Fi/audio sections.

## Q8 — Evidence pressure
Strong pre-existing software/platform and low-power hardware baseline; eliminates the novelty of basic screen-off context sensing or an independent always-on coprocessor.

## Q9 — AO-4 decision
Any Agent-specific claim must establish what extra context features, permission-aware intervention gating, confidence metadata and cross-domain handoff are needed after CHRE-style filtering. CHRE documentation does not evidence turnkey proactive multimodal Agent reasoning.

## Q10 — Next discriminating public evidence
Find practical context-event rates, AP wakes, CHRE memory/compute limits, privacy/consent boundaries, and when an LP-NPU intermediary adds value above trusted CHRE preprocessing.

## Decision footer
- **AO-4 impact:** STRONG_ESTABLISHED_BASELINE / low-power context processing independent of application processor
- **Evidence maturity:** PRODUCT_OR_PLATFORM_ARCHITECTURE_SIGNAL; not phone Agent SYSTEM_VALUE
- **No hardware promotion:** no
- **Source identity:** original URL is unique against existing canonical official sources in this SSOT
- **Primary:** https://source.android.com/docs/core/interaction/contexthub
