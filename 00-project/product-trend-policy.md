# Product-Trend and Differentiation Policy

Date: 2026-10-07
Applies to: 2027–2029 Agentic smartphone CPU / system / uArch roadmap.

## Core rule

> **Prior art constrains novelty, not product relevance.**

A good paper can reduce the originality of a broad claim while **increasing confidence that the mechanism is becoming an important product trend**.

Therefore every important Direction or mechanism must be judged on two independent axes:

1. **Product evolution relevance** — should a 2027–2029 smartphone product adopt, adapt, benchmark or prepare for it?
2. **Differentiation / research whitespace** — is there still a non-commoditized control point worth original research investment?

Do not use one axis as a proxy for the other.

---

## Axis A — Product evolution posture

Use exactly one primary posture token. Secondary implementation activities may be described in prose, but must not be expressed as a second posture token:

### PRODUCTIZE
Evidence is strong enough that the capability should be treated as part of the likely future product stack.

Typical condition:
- repeated system/product evidence;
- clear user/system value;
- implementation path is understandable;
- novelty may already be crowded.

### ADAPT_AND_DIFFERENTIATE
The trend is credible and product-relevant, but target-product integration, efficiency, robustness or architecture adaptation still offers meaningful leverage.

This is the default posture for:
- academic mechanism → commercial phone transfer;
- competitor mechanism → own-stack adaptation;
- existing ISA/runtime capability → better compiler/runtime/system integration.

### BENCHMARK_AND_PREPARE
The trend has credible signal but target-product economics or transfer are not yet proven.

Action:
- maintain measurements;
- prepare hooks/observability;
- build strongest baseline;
- avoid premature silicon commitment.

### WATCH
Evidence is emerging or indirect.
Track the trend and collect seeds, but do not commit product architecture.

### DROP_PRODUCT_ROUTE
Only use when product value itself is weak, displaced by a superior route, economically implausible, or outside the 2027–2029 scope.

**Existing prior art alone is not a reason to use DROP_PRODUCT_ROUTE.**

---

## Axis B — Differentiation / research posture

Use one of:

### DIFFERENTIATED_BET
A new-regime control point remains insufficiently captured by strongest known baselines and has a clear discriminating experiment.

### RESIDUAL_RESEARCH
The broad idea is known, but a target-specific residual may still support original work.

### CROWDED_BUT_VALUABLE
The mechanism/product direction is important but broad novelty is largely gone.
Primary goal is productization, adaptation and engineering excellence.

### FRONTIER_UNPROVEN
Potentially important structural signal exists, but current evidence is too weak to assign a Direction.

### CLOSED_DIFFERENTIATION
The broad differentiated thesis is no longer credible.
This does **not** imply the product capability should be removed.

---

## Trend maturity

Keep trend maturity separate from evidence maturity of a specific Direction.

- **ESTABLISHED_PRODUCT_TREND** — repeated evidence and/or productization across multiple sources.
- **EMERGING_PRODUCT_TREND** — credible system/product trajectory, still incomplete.
- **FRONTIER_SIGNAL** — early signal requiring coverage audit.
- **UNSUPPORTED** — insufficient evidence even for trend tracking.

A Direction can be SYSTEM_VALUE while the broader trend is only EMERGING, or a trend can be ESTABLISHED while a specific differentiated Direction is CLOSED.

---

## Kill-scope discipline

Every Kill/Narrow decision must say exactly what is killed:

- **KILL_BROAD_NOVELTY** — prior art already covers the broad concept.
- **KILL_DIFFERENTIATED_BET** — not enough residual for an original Bet.
- **KILL_MECHANISM** — mechanism fails value/cost/correctness.
- **KILL_ARCHITECTURE_NECESSITY** — product value exists but does not require the proposed hardware architecture.
- **KILL_PRODUCT_ROUTE** — the product capability itself is not worth pursuing.
- **KILL_WORDING_ONLY** — claim language is too strong.

Unless the canonical `kill_scope` is **KILL_PRODUCT_ROUTE**, a research Kill must not be read as “do not build this capability.”

---

## Productization gap is a valid research gap

Academic prior art does not close:
- phone power;
- thermal behavior;
- tail latency;
- foreground QoE;
- silicon area/cost;
- OS/kernel integration;
- compiler automation;
- security/authority;
- multi-generation compatibility;
- reliability;
- product telemetry;
- deployment and recovery;
- interaction with vendor-specific CPU/NPU topology.

These may justify **ADAPT_AND_DIFFERENTIATE** even when broad novelty is closed.

---

## Hardware gate remains strict

Product relevance does not waive the uArch gate:

`STRUCTURAL_SIGNAL → SYSTEM_VALUE → SOFTWARE_INSUFFICIENCY → hardware-specific cause → UARCH_CANDIDATE`

A mechanism can be PRODUCTIZE or ADAPT_AND_DIFFERENTIATE entirely in software/runtime and never become a uArch candidate.

---

## Required roadmap output

The final roadmap must expose both layers:

### Layer 1 — Product Evolution Map
What the future smartphone CPU/SoC/system stack should gain, regardless of originality.

### Layer 2 — Differentiation Portfolio
Where the team should:
- make an original Bet;
- extend/adapt prior work;
- benchmark competitors;
- keep a reserve;
- stop investing.

The leadership-facing result should read:
**trend → product action → differentiation posture → strongest evidence → unresolved residual → next gate**.
