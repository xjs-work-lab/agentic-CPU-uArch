# PAPER-120 — Full Paper Insight 10Q

**Primary source:** https://arxiv.org/abs/2607.08565
**Depth:** FULL_10Q / original 2026 paper
**Identity:** arXiv 2607.08565
**Evidence status:** PRODUCTION_TRACE_AND_REAL_CLUSTER_PREPRINT

## Q1 — Problem and target mapping
Agent-oriented LLM serving places repeated turn requests and massive KV reuse into heterogeneous server-instance routing. The relevant AO-5 question is how far simple, reconstructible session facts can improve scheduling before requesting private Agent semantics.

## Q2 — New-regime relevance
Agent sessions reuse prior KV context and only act after complete outputs; the relevant control point is request placement among cloud-serving instances, not priority among phone-app continuations.

## Q3 — Falsifiable hypothesis
Route first session request by load, subsequent requests by local KV hit; this retains reuse while avoiding a few-instance hotspot without per-session router metadata. It fails when global-tier bandwidth is inadequate, session history is truncated, or workload is unlike high-concurrency agent serving.

## Q4 — Research lineage and strongest competitors
Preprint from SJTU IPADS and Alibaba; measured against Bailian production scheduler, LMetric, pure load balance/vLLM and Dynamo under disaggregated serving; implemented with vLLM/LMCache and a Mooncake-like global KV tier.

## Q5 — Detailed mechanism
Requests carry full prior conversation. Infer a turn's position from historical message count rather than export an explicit 'Agent semantic progress' label or maintain a session-to-instance table. First turn balances instance load, follow-up turn sticks to best local KV cache when expected hit matches history; fallback balance on suspected eviction; long-session migration handles rare skew.

## Q6 — Production traces and experimental design
Two commercial coding-Agent serving traces from May 29 2026 peak period, two-hour collection, separate TB-class/~280B clusters, thousands of accelerators. Analysis reports idealized unlimited-cache reuse >80%; 67% intra-session; many reuse intervals <100s. Replay Trace1, modifying generated response length/history to reproduce reuse: this is a trace-replay limitation. Physical testbed 4 × 8 NVIDIA H20 GPUs (32 GPUs), 200Gbps RDMA, 160 cores and 1280GB DRAM per server.

## Q7 — Measured results and ablations
With a global KV tier, 10–16% more good tokens/s within TTFT/TPOT SLO under prefilling and decoding colocation; 2–34% more good prefill TPS under disaggregation across provisioning. Without a global KV tier, SMetric and Bailian are within ~1%. In disaggregated fully provisioned case median TTFT 1.1s vs 1.8s strongest baseline; result heavily depends on tier availability and saturation.

## Q8 — Artifact and reproducibility boundary
arXiv HTML full sections 2–5 including trace definition, simulator/replay adjustments, prefilter, sensitivity, deployment and limitations directly read. Paper says traces/system to be open-sourced upon publication, release not independently verified. Only a server LLM router; does not see Agent internal goals, tools or correctness; no phone energy/thermal/foreground QoE.

## Q9 — AO-5 inference and negative evidence
Session position and reuse/queue state have high information value despite being derived from request history. This is a strong pressure against generic 'new semantic hint' arguments, but does not disprove private DemandState fields that distinguish same observable session state.

## Q10 — Next action
Use in AO-5 as an inexpensive, reconstructible baseline for phase/session routing and show explicit platform transfer boundary. Do not conflate its token-throughput objective with phone user's required task progress.

## Decision footer
- Evidence maturity: SYSTEM_VALUE for the evaluated *software/server/benchmark* system, not target-phone SYSTEM_VALUE
- AO-5: AO-5 observable Agent session-stage scheduler counterexample (server-scope)
- Direct mobile CPU-uArch evidence: none
- Open gate: conditional information value of internal RequiredProgress over matched B4-TX, plus mobile transfer
- Primary source: https://arxiv.org/abs/2607.08565
