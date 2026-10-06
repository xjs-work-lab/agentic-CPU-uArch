+++
id = "EC-A-006-A"
type = "EVIDENCE_CASE"
record_state = "CURRENT"
relation = "SUPPORT"
target_kind = "CLAIM"
target_id = "CLM-AGENT-005"
warrant = "AutoDroid-V2 directly compares task-level script/code lowering against step-wise mobile GUI-Agent execution and reports large reductions in on-device inference latency and token use while improving evaluated task success."
scope = "PAPER-058 evaluated DroidTask/AitW subset and Snapdragon 8 Gen2 phone latency setup"
boundary = "Upper-layer application/runtime semantic-lowering evidence; dynamic-UI limitations remain; no OS/CPU/uArch conclusion."
[[premises]]
ref_kind = "SOURCE"
ref_id = "PAPER-058"
locator = "MobiSys 2025 evaluation: task success, token use, Snapdragon 8 Gen2 latency; artifact phone-latency workflow"
+++

# EC-A-006-A

## Inference
PAPER-058 → **SUPPORT** → CLM-AGENT-005

## Warrant
The evaluated task-level program route replaces repeated step-wise model calls with one generated executable plan plus reusable app knowledge, and materially reduces phone-side inference cost.

## Boundary
This supports software semantic lowering in the evaluated mobile GUI-Agent regime. It does not prove that a portable lower-layer semantic-control interface adds value.
