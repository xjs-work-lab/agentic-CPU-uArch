# PAPER-076 — Demo: Modality-Aware Long-Term Memory Acquisition for On-Device Mobile Personal Agents

## Source
- MobiSys Companion 2026, peer-reviewed demo, pages 197–198
- Authors: Liyu Zhang, Xiaomin Ouyang — HKUST
- DOI: https://doi.org/10.1145/3812835.3814986
- Scope: upstream multimodal memory-data acquisition during phone usage
- Modalities: screenshot, Accessibility tree, interaction events, device state
- App coverage: 15 representative real-world apps

## Q1 — Problem + target mapping
Persistent mobile Agents need long-term memory, but most memory systems begin after evidence has already been captured and structured.

This demo moves the systems boundary upstream:
> what should a phone continuously capture so that future Agent memory is useful, while respecting acquisition latency, storage and energy budgets?

This maps directly to the surviving H-PAM question about background acquisition/ingest cost.

## Q2 — Novelty / new-regime relevance
The demo makes four acquisition channels explicit and compares them under real mobile constraints.

Reported qualitative findings:
- screenshots: stable/rich but costly;
- A11y trees: cheaper, but availability/structure can be brittle;
- interaction events: lightweight, but incomplete in semantic content;
- device state: lightweight/contextual, but insufficient alone.

New-regime classification:
**Agent-amplified mobile sensing/acquisition**, not clearly Agent-native.

The need for reusable long-term personal memory amplifies acquisition duration and cross-app persistence, but the underlying energy/coverage trade-off resembles established mobile sensing problems.

## Q3 — Falsifiable hypothesis
If no single acquisition modality dominates simultaneously on semantic coverage, availability, latency, storage and energy, a mobile personal-memory layer should adapt what it captures rather than continuously collecting the richest representation.

Falsifiers:
- one modality becomes universally cheap and reliable;
- downstream memory quality is insensitive to modality choice;
- acquisition cost is negligible relative to all other Agent costs;
- OS/app restrictions make adaptive modality choice impossible.

The demo supports the first premise qualitatively.

## Q4 — Research lineage / competing route
Strong competing/prior-art routes:
- classic energy-aware mobile sensing;
- adaptive sampling/duty cycling;
- semantic/context-driven sensor selection;
- shared mobile context-monitoring runtimes;
- event-driven capture;
- application-accessibility telemetry;
- MUSE-class downstream insertion/index maintenance.

Thus the white space cannot simply be 'choose cheaper modality'.

## Q5 — Key mechanism / control point
The prototype exposes acquisition as a first-class upstream layer and combines:
- live telemetry;
- per-app modality availability;
- capture-cost measurements;
- multimodal memory-data construction.

Potential control variable:
> which modality or modality combination to capture and retain for a future memory need.

Project boundary:
the demo does **not** establish that this control variable must be Agent-specific rather than a generic sensing/value-vs-cost policy.

## Q6 — Experiment design
Directly reported:
- four modalities;
- 15 representative real-world apps;
- synchronized traces for availability, capture latency, storage overhead and energy consumption;
- app-level modality availability analysis.

Accessible source text does not expose all numeric modality-level measurements, so no exact energy/latency percentages are promoted into project scoring.

## Q7 — Data / artifact / reproducibility
Strengths:
- MobiSys 2026;
- direct target class: on-device mobile personal agents;
- real app coverage;
- acquisition-side latency/storage/energy explicitly measured;
- video/demo publicly referenced.

Limitations:
- 2-page demo rather than full systems paper;
- exact hardware and complete numeric tables are not available in the accessible text used in this review;
- no end-to-end comparison showing that adaptive modality choice improves Agent outcome;
- no CPU/NPU/DRAM profiling;
- no independent replication.

## Q8 — Evidence vs hypothesis
### [FACT]
Memory acquisition modalities differ in availability, capture cost and semantic completeness across evaluated mobile apps.

### [OBSERVATION]
Persistent Agent memory has an upstream acquisition budget that is absent from retrieval-only memory papers.

### [INFERENCE — project]
A long-lived personal Agent may need capture policy, but the policy may be generic mobile sensing rather than a new Agent-specific execution substrate.

### Not established
- distinct Agent-only capture semantics;
- >=5% end-outcome benefit from adaptive capture;
- lower-layer CPU/uArch mechanism;
- software insufficiency.

## Q9 — Real contribution to project decision
### H-PAM
Provides direct target-phone support for **acquisition being non-free**.

But it does not rescue H-PAM as a standalone Direction because:
- modality/cost trade-offs are generic mobile-sensing territory;
- no lower-level Agent-specific residual is shown;
- downstream MUSE already covers ingestion/index maintenance after capture.

### C
Acquisition becomes another workload for generic resource/QoS orchestration if future measurements show relevant interference.

### B-residual
Semantic completeness/validity may matter to B-residual, but this demo does not study lineage/invalidation.

## Q10 — Next action
1. KEEP as P0 direct mobile acquisition evidence.
2. Add a Claim that acquisition modality choice has real phone cost/coverage trade-offs.
3. Pressure-test novelty with mature mobile sensing/context-monitoring prior art.
4. Do not create an acquisition Direction without Agent-specific residual beyond generic value-vs-cost sensing.

## Decision footer
- **Evidence maturity:** STRUCTURAL_SIGNAL / direct mobile acquisition measurement
- **Decision impact:** narrows H-PAM toward acquisition, but does not promote it
- **Open questions:** exact numeric cost curves, end-outcome sensitivity, duty cycle, interference with foreground QoE
- **Primary source:** https://doi.org/10.1145/3812835.3814986