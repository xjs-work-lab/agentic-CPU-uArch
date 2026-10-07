# PAPER-108 — SpecBox — FULL_10Q

## Q1 — Problem
Avoid permanent sandbox residency without paying repeated on-demand cold starts.

## Q2 — Agent relevance
Tool choice emerges online during reasoning, creating early-intent and cross-step dependency signals.

## Q3 — Hypothesis
Prediction/prewarming can overlap sandbox preparation with Agent reasoning. Phone-specific executable-lifecycle residual is not tested.

## Q4 — Baselines
Reserved Runtime and On-demand Runtime; microVM/WASM/snapshot techniques are treated as orthogonal lower-layer mechanisms.

## Q5 — Mechanism
Streaming intent prediction, stochastic prefetch, semantic result reuse and mmap shared-memory transport.

## Q6 — Evaluation
16-core server, 256 GiB RAM, Docker, Python/AgentScope, cloud Qwen3.5-Max; 32 MCP-compatible sandbox environments and 200 multi-turn traces. Most cold starts are 2–4 s, heavy cases approach ~20 s. Reported results include 4.53× lower cumulative provisioning latency vs On-demand, up to 2.9× lower P99 E2E at high load, and 45.9% lower peak memory vs Reserved.

## Q7 — Limitations
No smartphone, Android/AppFunctions, phone energy/thermal/QoE, JIT/interpreter or code-cache data.

## Q8 — Fact vs inference
FACT: sandbox lifecycle can dominate server Agent tail latency/resource use.
FACT: software-visible prediction/prewarm/reuse recovers substantial value.
INFERENCE: the strongest owner is C + T5/B-residual, not new uArch.

## Q9 — Project decision
Strong software-sufficiency evidence against a standalone T6 Direction.

## Q10 — Action
Close T6 standalone differentiation unless direct phone residual evidence appears.

Primary: https://arxiv.org/abs/2607.23933
