+++
id = "EC-C-008-A"
type = "EVIDENCE_CASE"
record_state = "CURRENT"
relation = "SUPPORT"
target_kind = "CLAIM"
target_id = "CLM-C-007"
warrant = "WASH dynamically identifies contended-lock bottleneck threads, profiles core sensitivity and workload scalability, then applies thread-affinity decisions on asymmetric CPU configurations with measured performance/energy gains."
scope = "PAPER-062 evaluated Java/Jikes-RVM workloads on frequency-scaled x86 AMP hardware"
boundary = "Generic managed-runtime heterogeneous CPU scheduling prior art; not smartphone/Agent evidence."
[[premises]]
ref_kind = "SOURCE"
ref_id = "PAPER-062"
locator = "CGO 2016 Sections 1-8: runtime analyses, critical-thread inference, WASH scheduling and evaluation"
+++

# EC-C-008-A

## Inference
PAPER-062 → **SUPPORT** → CLM-C-007

## Boundary
This establishes automatic runtime fact extraction for heterogeneous CPU scheduling, not Agent-specific cross-resource control.
