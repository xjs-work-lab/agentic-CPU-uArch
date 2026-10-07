+++
id = "CLM-AO1-002"
type = "CLAIM"
record_state = "CURRENT"
claim_kind = "OBSERVATION"
status = "SUPPORTED"
scope = "Agent CPU/tool/accelerator critical-path coupling"
supersedes = []
+++

# CLM-AO1-002

## Proposition
Agentic workflows repeatedly couple accelerator inference with CPU-side orchestration/tools and state transitions, so CPU/tool service, accelerator service, memory/state residency and phase handoff can jointly determine end-to-end latency rather than GPU/NPU throughput alone.

## Boundary
The strongest direct tool-critical-path measurements are server-side. Mobile magnitude and which tools remain local are not yet established.
