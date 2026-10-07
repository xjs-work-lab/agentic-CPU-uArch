+++
id = "PAPER-106"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
deep_review_protocol = "EDP_V1"
deep_review_date = "2026-10-07"
decision_critical = true
decision_use = "T6_LOCAL_PROGRAMMABLE_SKILL_PRODUCT_SIGNAL_AND_EXECUTABLE_LIFECYCLE_BOUNDARY"
independence_assessment = "INDEPENDENT_MULTI_INSTITUTION_ARXIV_PREPRINT"
title = "SkillDroid: Compile Once, Reuse Forever"
primary_url = "https://arxiv.org/abs/2604.14872"
priority = "P0"
evidence_role = "direct Android GUI evidence for converting successful Agent trajectories into persistent executable procedural skills; boundary evidence against premature native/JIT/code-cache CPU interpretation"
authors = ["Qijia Chen", "Andrea Bellucci", "Zhida Sun", "Giulio Jacucci"]
venue = "arXiv preprint, v1 submitted 2026-04-16"
artifact_urls = ["https://github.com/droidrun/droidrun"]
+++

# PAPER-106 — SkillDroid

## 30-second read
- **Core mechanism:** successful LLM-guided Android GUI trajectories become parameterized skill templates with typed slots, weighted UI locators and replay state.
- **Replay:** stored action skeletons execute through DroidRun/ADB with verification, step skipping, bounded fallback and failure-triggered recompilation.
- **Controlled baseline:** same 150 tasks, LLM/prompts/action/reset/checker stack, but no skill matching/replay/compilation.
- **Reported outcome:** 85.3% success vs 62.0%; 5.8 vs 11.3 mean LLM calls; 69.0 s vs 84.1 s mean latency.
- **Pure replay:** 35/150 rounds use zero LLM calls; all non-full-fallback Layer-2 variants total 79 rounds.
- **Critical boundary:** Windows 11 host + Pixel 9a/API 35 Android emulator + ADB; no physical-phone CPU/energy/thermal measurement.
- **"Compile" boundary:** structured GUI-action program stored in SQLite, not native/JIT/WASM code.
- **ADB boundary:** ~100 ms/action through ADB versus ~4 ms cited for native AccessibilityService execution.
- **T6 impact:** stronger product signal, weaker immediate CPU executable-lifecycle claim.
- **Portfolio impact:** no new Direction, score/lane change or uArch candidate.

See [deep.md](deep.md).
