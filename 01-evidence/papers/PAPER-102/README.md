+++
id = "PAPER-102"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
independence_assessment = "INDEPENDENT_VERIFICATION_GROUP"
title = "Don't Act Blindly: Robust GUI Automation via Action-Effect Verification and Self-Correction"
primary_url = "https://aclanthology.org/2026.acl-long.1335/"
priority = "P0"
evidence_role = "causal software baseline for action-effect verification and recovery"
review_depth = "FULL_10Q"
deep_review_protocol = "EDP_V1"
deep_review_date = "2026-10-07"
decision_critical = true
authors = ["Yuzhe Zhang", "Xianwei Xue", "Xingyong Wu", "Mengke Chen", "Chen Liu", "Xinran He", "Run Shao", "Feiran Liu", "Huanmin Xu", "Qiutong Pan", "Haiwei Wang"]
venue = "ACL 2026 Long"
+++

# PAPER-102 — Don't Act Blindly / VeriGUI

## 30-second read
- Strong causal software baseline for PT-A verification: robust SFT + verification-aware RL improves recovery metrics and online AndroidWorld performance.
- VeriGUI-3B RSR 51.1%, 7B 52.5%; explicit reward ablations show verification reward contributes beyond action reward alone.
- This strengthens “verification has value” while simultaneously raising the software baseline: much of recovery can be learned in the Agent model.
- AndroidWorld evaluation is emulator-based; it does not solve action-target TOCTOU from PAPER-101.
- Primary source: https://aclanthology.org/2026.acl-long.1335/

See [deep.md](deep.md) for EDP v1 FULL_10Q.
