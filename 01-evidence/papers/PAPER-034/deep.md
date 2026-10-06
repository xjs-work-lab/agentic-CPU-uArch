> V1 semantic source copied/repacked from frozen baseline `960abb4ef50f050da3c6784d30826053d42e5c5d`.

## PAPER-034 — [PLACEMEM: Toward a Compute-Aware Memory Plane for Lifelong Agents](https://arxiv.org/abs/2607.04089)

**Background**  
Semantic memories may be corrected while serving systems continue to reuse compute artifacts derived from the old state.

**Method**  
PlaceMem uses versioned capsules that bind semantics, provenance, validity, dependencies and reusable runtime artifacts.

**Conclusion**  
A correction-follow probe on a real vLLM backend reports that full PlaceMem prevents stale selection while preserving the reuse latency path; an earlier pilot isolates control-plane effects with a mock generator.

**What we learn**  
The strongest cross-tier semantic signal may be **validity/provenance**, not reuse prediction.

**Boundary**  
Early prototype/position; no phone evidence.

---

---
