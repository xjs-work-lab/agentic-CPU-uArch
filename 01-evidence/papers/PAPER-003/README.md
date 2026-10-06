+++
id = "PAPER-003"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q_REVIEWED_2026-10-06"
decision_use = "DECISION_GRADE_WITH_SCOPE_BOUNDARY"
independence_assessment = "UNKNOWN"
title = "Inference in the Shadows: Taming Memory Bandwidth Contention in Mobile LLM Inference with SERENO"
primary_url = "https://www.usenix.org/system/files/osdi26-xin.pdf"
priority = "P0"
evidence_role = "direct smartphone foreground/background interference + strong generic foreground-protection baseline for A/C"
origin_paths = ["03-academic/paper-10q/PAPER-003.md"]
origin_blobs = ["6ce5cd2a0955c0076d00d87c087e40df39936a02"]
authors = ["Tong Xin", "Xinrui Shi", "Mingkai Dong", "Zeyu Mi"]
venue = "OSDI 2026"
+++

# PAPER-003 — Inference in the Shadows: Taming Memory Bandwidth Contention in Mobile LLM Inference with SERENO

## 30-second read
- **Why it matters:** Direct commercial-smartphone evidence that background NPU LLM inference can badly damage foreground QoE through shared-memory-bandwidth contention.
- **What it establishes:** The foreground-protection problem is real on evaluated Snapdragon phones, and a software-only fine-grained yielding/control loop captures a large fraction of the value.
- **Key boundary:** This is a strong **generic G1 baseline**, not evidence of Agent-specific residual or hardware necessity.
- **Primary source:** https://www.usenix.org/system/files/osdi26-xin.pdf

## Current decision use
**FULL 10Q REVIEW COMPLETE.**

Use as:
- direct smartphone SYSTEM_VALUE evidence for mixed foreground/background mobile AI;
- strongest-baseline evidence for foreground-QoS-aware bandwidth control;
- user-value anchor for Foreground-Protected Persistent Agent.

Do **not** use as:
- proof of DemandState value;
- proof of full-Agent workload behavior;
- proof of Huawei internal capability absence;
- proof that hardware/uArch changes are required.

## Reviews
- Current review: [review-2026-10-06.md](review-2026-10-06.md)
- Frozen V1 interpretation: [deep.md](deep.md)

## Migration fidelity
- V1 baseline: `960abb4ef50f050da3c6784d30826053d42e5c5d`
- Transform: `STRUCTURAL_REPACK`
- Source independence remains `UNKNOWN` unless explicitly assessed later.
