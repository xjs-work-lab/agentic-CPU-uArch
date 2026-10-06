+++
id = "CLM-MEM-001"
type = "CLAIM"
record_state = "CURRENT"
claim_kind = "OBSERVATION"
status = "SUPPORTED"
scope = "generic personal/client-device vector-index storage and dynamic-update software capture"
supersedes = []
+++

# CLM-MEM-001

## Proposition
A substantial fraction of local vector-memory capacity and dynamic-index overhead can be reduced through generic software/data-structure techniques such as selective embedding recomputation, graph pruning, segmentation and on-demand index residency, without Agent-specific hardware support in evaluated personal/client systems.

## Evidence
- PAPER-070 / LEANN — recomputation + compact graph index.
- PAPER-072 / CD-ANN — segmented HNSW + on-demand client residency + localized dynamic insertion.

## Boundary
The two papers cover different hardware/settings and are not direct smartphone-Agent replications.

This Claim does not establish that:
- mobile heterogeneous execution overhead disappears;
- semantic memory consolidation is equivalent to ANN insertion;
- phone energy/thermal value is captured;
- Agent-specific operation semantics have no residual.
