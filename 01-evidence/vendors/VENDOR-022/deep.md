> **Historical alias supplementary review:** This review is retained under VENDOR-022 for audit history. The original Qualcomm source is canonically **VENDOR-001**. It must not be counted as a second independent vendor source.

# VENDOR-022 — Qualcomm Oryon Flex Cache — deep vendor card

## Q1 — Original technical disclosure
Official Qualcomm OnQ article dated 2026-08-25 by Francisco Cheng: https://www.qualcomm.com/news/onq/2026/08/oryon-cpu-5ghz-flexcache .

The vendor discloses that heterogeneous Oryon cores can access a common cache pool dynamically allocated based on workload demand. Prime cores can use the full pool where beneficial.

## Q2 — Mechanism / control point
Flexible CPU-cache allocation increases the chance that a CPU working set remains resident across core/task migration, potentially reducing off-chip memory access and cold starts. The public article does not specify cache capacity, all tag/way policies, coherence protocol, latency or measurable data-copy savings for Agent applications.

## Q3 — Target Agentic operating regime
Qualcomm expressly cites multi-step Agent workflows whose steps hand off across CPU cores and emphasizes CPU orchestration. Gaming, multitasking and video editing are also cited; hence the cache primitive is broadly useful, not Agent-exclusive.

## Q4 — Quantitative/product claims
The 5 GHz Oryon CPU frequency is disclosed in the article, but **there is no controlled quantitative Agent/Flex-Cache improvement in the cited source**. Do not conflate general CPU frequency with the state-fabric opportunity.

## Q5 — Source claims versus verified facts
PUBLIC DISCLOSURE: shared, dynamically allocated heterogeneous-CPU cache pool.
VENDOR POSITIONING: fewer memory trips and smoother Agent/task handoff.
NOT PUBLICLY VERIFIED HERE: CPU↔NPU/GPU coherence, context/adapter version metadata, explicit Agent-state persistence or Agent-specific energy/latency attribution.

## Q6 — Strong baseline/prior art
Generic heterogeneous migration/cache-demand policy is prior art (PATENT-024 US9626295B2 claim 1/23). Shared caches and coherence are established mechanisms. This vendor signal does not restore novelty to generic cache hierarchy proposals.

## Q7 — Competitor/product value
Strong mobile architecture signal that CPU working-set placement matters for multi-step, stateful workloads. The article alone does not demonstrate a heterogeneous xPU memory/state fabric.

## Q8 — Independent source pressure
MobiMem's Action Memory shows phone software can avoid expensive repeated inference, but the direct Snapdragon evaluation is CPU-only. LOCAL demonstrates versioned KV and memory coexistence on one 24GB GPU, not modern mobile SoC cross-engine preservation. These results bound extrapolation.

## Q9 — Decision impact
Supports CLM-AO3-004 and AO-1 product context; **does not** establish CLM-AO3-006 hardware necessity or a differentiated uArch investment. Product signal and open architecture hypothesis remain separate.

## Q10 — Further public evidence to seek
Qualcomm cache-controller allocation/coherence documentation, independent cache handoff tests, CPU/NPU derived-state handoff descriptions, observed residency/memory bandwidth behavior and power/latency comparisons to runtime-managed baselines.

## Footer
- Source confidence: high for vendor-disclosed design direction; moderate for causal performance value
- Independence: VENDOR_SELF_REPORT
- Claim-reviewed: not a patent
- Original URL: https://www.qualcomm.com/news/onq/2026/08/oryon-cpu-5ghz-flexcache
