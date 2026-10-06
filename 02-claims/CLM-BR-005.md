+++
id = "CLM-BR-005"
type = "CLAIM"
record_state = "CURRENT"
claim_kind = "OBSERVATION"
status = "SUPPORTED"
scope = "device-free strong-baseline sensitivity"
supersedes = []
+++

# CLM-BR-005

## Proposition
In the Stage15 device-free model, B-residual's >=5% region collapses rapidly as GenericSafePreservationCapture rises: 26/108 passing cells at 25%, 13/108 at 50%, and 2/108 at 75%.

## Current interpretation
The completed B-residual kill-test quantitatively narrows plausible residual regions.

## Boundary
Synthetic sensitivity result, not phone measurement.

## Migration
- frozen V1 baseline: `960abb4ef50f050da3c6784d30826053d42e5c5d`
- transform: `STRUCTURAL_REPACK`
