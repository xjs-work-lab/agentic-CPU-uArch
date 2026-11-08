# PAPER-127 — MemGUI-Bench: Benchmarking Memory of Mobile GUI Agents in Dynamic Environments

- **Primary source:** https://arxiv.org/abs/2602.06075
- **Full text:** https://arxiv.org/html/2602.06075
- **Project site:** https://memgui-bench.github.io/
- **Authors:** Guangyi Liu, Pengxiang Zhao, Yaozhen Liang, Qinyi Luo, Shunye Tang, Yuxiang Chai, Weifeng Lin, Han Xiao, Wenhao Wang, Siheng Chen, Zhengxi Lu, Gao Wu, Hao Wang, Liang Liu, Yong Liu
- **Affiliations:** Zhejiang University, Nankai University, CUHK, Shanghai Jiao Tong University, vivo AI Lab
- **Published:** 2026-02 (arXiv preprint)
- **Review date:** 2026-11-09
- **Status:** FULL_TEXT_REVIEWED / AGENT_MEMORY_BENCHMARK / NOT_HARDWARE_EVIDENCE
- **Decision relevance:** A (problem significance and software-observability boundary); no direct CPU-uArch result.

## Q1 — Problem

Mobile GUI Agent benchmarks underrepresent memory-heavy tasks. The paper distinguishes short-term/in-session memory (retaining information across action sequences and app transitions) from long-term/cross-session memory (accumulating reusable experience from successes and failures).

## Q2 — Benchmark and evaluation

- 128 tasks across 26 applications; 115 memory-intensive and 13 standard tasks.
- 64 mirror task pairs to assess cross-task learning.
- 89.8% of tasks require cross-temporal and cross-spatial retention; 78.1% involve cross-application information transfer.
- Evaluation of 11 agents across five memory architectures.
- MemGUI-Eval uses staged triage, semantic analysis and targeted visual verification, with seven metrics spanning memory fidelity, learning and efficiency.

## Q3 — Results

The paper reports substantial memory deficits across evaluated agents, including 4–10× capability gaps on memory-intensive tasks. Short-term memory is indispensable. Explicit long-term memory improves cross-session learning by 21.9 percentage points in the reported evaluation, while cross-application transfer and computational cost remain bottlenecks.

## Q4 — Boundary for project A

This supports the existence and user relevance of Agent memory/progress problems. It does **not** show that the required state is inaccessible to the software runtime, nor that a privileged CPU/OS RequiredProgress field is needed. The benchmark is an agent-memory evaluation, not a hardware counter, microarchitecture or OS-state experiment.

The authors state that code, benchmark and results will be open-sourced and maintained at the project site; artifact completeness and version should be checked before claiming independent reproduction.

## Q5 — Decision impact

**A remains conditional, with problem significance strengthened but hardware-specific hypothesis unproven.** The correct next question is whether current software-visible workflow ledgers, UI snapshots, tool receipts and persistent memory can reconstruct the required progress/utility state at acceptable cost and accuracy.

## Evidence footer

Original arXiv full text reviewed. Confidence: medium for benchmark-reported findings; low for implications to CPU/OS hardware because the paper does not study hardware.
