# PAPER-095 — MobiLoRA: Accelerating LoRA-based LLM Inference on Mobile Devices via Context-aware KV Cache Optimization

## Source
- ACL 2025 Long Papers
- Southeast University + Honor Device Co., Ltd.
- official ACL Anthology paper reviewed
- Priority: P0 mobile LoRA/KV baseline

## Q1 — Problem + target mapping
Different LoRA adapters produce different KV tensors even for identical token prefixes, so ordinary prefix-cache reuse does not directly transfer across adapters.

On resource-limited mobile devices this increases cache memory and TTFT.

For H-CAL, this directly tests whether adapter identity / application lifecycle / KV locality are already software-visible and optimizable.

## Q2 — Novelty / new-regime relevance
MobiLoRA exploits two context classes:
- **semantic context:** same/shared prompt prefixes across different LoRAs;
- **system context:** mobile application lifecycle such as foreground, background or killed.

It extends a radix cache with LoRA identity and app metadata, and stores later adapters' KV states as encoded deltas from an anchor where similarity permits.

Classification:
**DIRECT MOBILE SOFTWARE BASELINE**.

## Q3 — Falsifiable hypothesis
If KV tensors across LoRA adapters retain exploitable similarity and mobile app lifecycle predicts reuse probability, cross-adapter delta encoding plus context-aware eviction should reduce memory/recompute cost and TTFT.

Falsifiers:
- cross-adapter KV similarity is too weak;
- delta encode/decode overhead outweighs reuse;
- app state poorly predicts future reuse;
- approximation harms generation quality.

The paper reports substantial TTFT improvements in its evaluation.

## Q4 — Research lineage / competing route
Competing routes:
- ordinary per-adapter KV caches;
- LRU eviction;
- vLLM/SGLang prefix caching;
- no cross-LoRA cache reuse;
- recompute after adapter switch;
- generic compression/quantization.

MobiLoRA's key challenge to H-CAL is that **adapter identity and mobile app state are already explicit software cache signals**.

## Q5 — Key mechanism / control point
### CtxAttention
Context-aware radix tree records LoRA association, KV location, anchor information, app ID and recency.

### Similarity-aware delta encoding
KV tensors for another LoRA sharing the prefix are stored as compressed differences from an anchor.

### System-context-aware eviction
Foreground/background/killed app status participates in retention/eviction decisions.

## Q6 — Experiment design
MobiLoRA is implemented on an LLM serving stack and evaluated with real-world mobile application usage traces.

Reported TTFT acceleration:
**18.1%–81.3%** across evaluated settings.

The exact result is an inference-serving improvement, not training energy or live-update evidence.

## Q7 — Data / artifact / reproducibility
Strengths:
- peer reviewed;
- direct mobile setting;
- LoRA-specific KV mechanism;
- system-level mobile context included;
- industry coauthors from a device vendor.

Limitations:
- focuses on inference with multiple adapters, not adapter weights changing during a live session;
- no local gradient training;
- does not establish behavior immediately after an adapter publication;
- not a CPU/uArch mechanism.

## Q8 — Evidence vs hypothesis
### [FACT]
LoRA adapter identity changes KV state enough to break direct ordinary cache reuse.

### [FACT]
Software can explicitly attach LoRA/app context to cache metadata and exploit cross-adapter similarity.

### [OBSERVATION]
Much of the adapter/KV state H-CAL might otherwise claim is visible to the serving runtime.

### [INFERENCE — project]
The remaining novelty of H-CAL cannot be ordinary LoRA cache identity, retention, eviction or cross-adapter reuse.

## Q9 — Real contribution to project decision
MobiLoRA substantially narrows the H-CAL residual:
- adapter identity → already software-visible;
- app foreground/background state → already software-visible;
- KV retention/eviction → strong mobile software prior art;
- cross-adapter similarity/reuse → strong software baseline.

What remains distinct is **in-place adapter update/version publication while serving**, and LOCAL already handles that in software.

## Q10 — Next action
1. KEEP as P0 H-CAL / B-residual / R2 strongest baseline.
2. Require any new cache/hardware proposal to beat MobiLoRA + LOCAL.
3. Do not open a new Direction for LoRA/KV cache semantics alone.
4. No portfolio score change.

## Decision footer
- **Evidence maturity:** mobile software SYSTEM_VALUE for LoRA serving
- **H-CAL impact:** strongly narrows
- **Hardware impact:** none
- **Primary source:** https://aclanthology.org/2025.acl-long.1140/
