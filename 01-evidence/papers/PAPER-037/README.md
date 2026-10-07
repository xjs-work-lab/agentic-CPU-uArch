+++
id = "PAPER-037"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
independence_assessment = "INDEPENDENT_GROUP"
title = "ClawMobile: Rethinking Smartphone-Native Agentic Systems"
primary_url = "https://arxiv.org/abs/2602.22942"
priority = "P0"
evidence_role = "real-phone heterogeneous actuation + verify/recover runtime evidence"
review_depth = "FULL_10Q"
deep_review_protocol = "EDP_V1"
deep_review_date = "2026-10-07"
decision_critical = true
authors = ["Hongchao Du", "Shangyu Wu", "Qiao Li", "Riwei Pan", "Jinheng Li", "Youcheng Sun", "Chun Jason Xue"]
venue = "ACM EuroMLSys 2026"
+++

# PAPER-037 — ClawMobile

## 30-second read
- Real Google Pixel 9 / Android 16 evidence for a phone-resident Agent runtime coordinating deterministic backends and GUI automation.
- Six real-life tasks show reliability value from backend selection plus explicit progress verification/recovery.
- The runtime executes on the phone, but the paper explicitly states **model inference is remote**; this is not on-device-LLM compute evidence.
- Evaluation is small and the DroidRun comparator is host-tethered, so do not overgeneralize the 100% completion result.
- Primary source: https://arxiv.org/abs/2602.22942

See [deep.md](deep.md) for EDP v1 FULL_10Q.
