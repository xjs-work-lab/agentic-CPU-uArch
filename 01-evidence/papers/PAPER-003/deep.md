> V1 semantic source copied/repacked from frozen baseline `960abb4ef50f050da3c6784d30826053d42e5c5d`.
> Do not reinterpret this page as V2.2 metadata authority; the compact README owns the Source object.

# PAPER-003 — Inference in the Shadows: Taming Memory Bandwidth Contention in Mobile LLM Inference with SERENO

## Source
- Paper: https://www.usenix.org/system/files/osdi26-xin.pdf
- Authors: Tong Xin, Xinrui Shi, Mingkai Dong, Zeyu Mi
- Affiliation: IPADS / Shanghai Jiao Tong University
- Venue/status: OSDI 2026
- Target: OnePlus 13 / Snapdragon 8 Elite; OnePlus 12
- Project relevance: M4
- Priority: P0

## Q1 — What problem is the paper solving, and how does it map to smartphones?
**[FACT]** Background mobile LLM inference can substantially increase foreground jank while the background workload itself loses little throughput.

This is direct smartphone evidence for our strongest user-facing problem:
**foreground user + persistent/background AI concurrency**.

## Q2 — Is the problem/new mechanism actually new?
Foreground/background interference is old; **background LLM memory-bandwidth pressure on modern commercial phones** is a new operating regime.

Classification: **Agentic-amplified**. It is not Agent-native, but persistent Agents make the condition more frequent.

## Q3 — What falsifiable hypothesis is being tested?
**Hypothesis:** background LLM inference is over-consuming shared memory resources relative to its user value; protecting foreground bandwidth/latency can sharply reduce jank with small background throughput cost.

## Q4 — What is the research lineage / competing route?
Competes with:
- generic OS QoS;
- foreground/background priority;
- bandwidth throttling;
- CPU/GPU frequency control.

SERENO's importance is not novelty of “foreground first,” but commercial-phone evidence quantifying the conflict.

## Q5 — What is the key technical mechanism / control point?
Shared-memory/bandwidth-aware control for mixed foreground/background execution.

Project control point:
`foreground sensitivity + background AI demand → shared-resource allocation`.

## Q6 — How is the experiment designed?
**[FACT]** Commercial OnePlus devices; foreground interactive workloads run concurrently with background LLM inference.

Key anchors:
- aggregate foreground jank increased by ~153% under background LLM in reported experiments;
- background throughput degradation was small (~1.01% prefill, ~1.64% decode);
- SERENO reports up to 92.6%, average 58.5% jank reduction;
- reported average SERENO jank is ~6.21% vs Native ~4.91%;
- compared with vanilla speculative decoding, one Reader comparison reports 72.1% jank reduction with 6.2% throughput degradation.

## Q7 — What data/artifact/reproducibility support exists?
Peer-reviewed OSDI paper with commercial-device methodology. Public artifact status is not currently used as a critical dependency in our repo.

## Q8 — Do the results actually support the hypothesis?
Yes for the evaluated mobile LLM interference regime.

**Boundary:** SERENO does not prove Agent semantic discard/defer/yield is useful; it proves the user-facing interference problem is real and that strong generic resource control already helps.

## Q9 — What is the real contribution / technology control point for us?
SERENO is the strongest **M4 problem anchor** and simultaneously a difficult baseline.

It kills:
- “background AI should have lower priority” as novelty.

It leaves open:
- whether Agent-specific knowledge can selectively defer/discard low-value work while preserving useful progress better than generic foreground protection.

A Stage12E derived comparison uses the reported 6.21% SERENO average jank and 58.5% reduction vs PowerServe to infer a PowerServe average of ~14.96%. Relative to Native 4.91%, this means SERENO removes roughly **87% of excess jank** in that comparison.

**[INFERENCE]** Therefore M4 differentiation should focus less on additional jank reduction and more on **required Agent progress at a fixed near-native QoE envelope**.

## Q10 — What should we do next?
- Keep as P0 M4 anchor.
- Treat SERENO-like generic QoS/bandwidth control as part of B4.
- Test M4 only through **B5/B6 − B4**.

## Decision footer
- Evidence maturity: SYSTEM_VALUE for mixed foreground/background mobile AI
- Decision impact: KEEP M4 problem; narrow mechanism
- Open questions: incremental Agent semantic value
- Primary source: paper above
