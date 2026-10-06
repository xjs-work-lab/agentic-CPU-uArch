+++
id = "CLM-R2-EXP-001"
type = "CLAIM"
record_state = "CURRENT"
claim_kind = "HYPOTHESIS"
status = "OPEN"
scope = "R2 discriminating hypothesis"
supersedes = []
+++

# CLM-R2-EXP-001

## Proposition
On representative smartphone Agent workloads, repeated continuations retain a causal CPU-local cache/TLB/branch warm-state penalty large enough that an Agent-specific mechanism adds >=~5% meaningful performance/energy value beyond strong software locality plus generic shared/coherent hardware.

## Boundary
No positive target-phone PMU result exists; hardware work remains gated.

## Migration
- frozen V1 baseline: `960abb4ef50f050da3c6784d30826053d42e5c5d`
- transform: `STRUCTURAL_REPACK / EXPLICIT_HYPOTHESIS_OBJECTIZATION`
