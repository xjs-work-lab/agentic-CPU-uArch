+++
id = "PAPER-055"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
independence_assessment = "UNKNOWN"
title = "Inference in the Shadows: Taming Memory Bandwidth Contention in Mobile LLM Inference with Sereno"
primary_url = "https://www.usenix.org/conference/osdi26/presentation/xin"
priority = "P0"
evidence_role = "direct commercial-smartphone foreground-QoS versus background inference interference evidence; high-value input for C and Foreground-Protected Persistent Agent anchor"
authors = ["Tong Xin", "Xinrui Shi", "Mingkai Dong", "Zeyu Mi"]
venue = "USENIX OSDI 2026"
+++

# PAPER-055 — Sereno

## 30-second read
- **Why it matters:** Directly measures the conflict between background mobile LLM inference and latency-sensitive foreground applications on commercial smartphones.
- **What it establishes:** NPU memory-bandwidth contention can severely harm foreground QoS while inference itself is only mildly affected; fine-grained software yield points can recover much of the QoS without hardware modification.
- **Reported anchors:** baseline interference raises aggregate foreground jank by 153%; SERENO reduces jank by up to 92.6% (58.5% average) while increasing LLM throughput by up to 67.9% (26.4% average) in the reported evaluation.
- **Portfolio pressure:** Strong direct evidence for the Foreground-Protected Persistent Agent user-value anchor and for C's system-control problem; simultaneously strengthens software-first baseline pressure.
- **Boundary:** Mobile LLM inference is not identical to full Agent execution; does not establish Agent-semantic residual or new uArch need.
- **Primary source:** https://www.usenix.org/conference/osdi26/presentation/xin
