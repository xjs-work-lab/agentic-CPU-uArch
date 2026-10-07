+++
id = "CLM-MOBILE-005"
type = "CLAIM"
record_state = "CURRENT"
claim_kind = "OBSERVATION"
status = "SUPPORTED"
scope = "on-device mobile personal-memory acquisition across screenshot, A11y tree, interaction-event and device-state modalities"
supersedes = []
+++

# CLM-MOBILE-005

## Proposition
Upstream long-term-memory acquisition on mobile devices has modality-dependent availability, capture-latency, storage, energy and semantic-completeness trade-offs; no single evaluated modality dominates across these dimensions.

## Evidence
PAPER-076 / MobiSys 2026 modality-aware acquisition demo.

## Boundary
This establishes a direct mobile acquisition cost surface, not a novel Agent-specific control abstraction.
Exact modality-level numeric values are not promoted because the accessible demo text did not expose the complete measurement tables.