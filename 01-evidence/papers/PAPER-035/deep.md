> V1 semantic source copied/repacked from frozen baseline `960abb4ef50f050da3c6784d30826053d42e5c5d`.

## PAPER-035 — [Invalidation Contracts for Cross-Episode Agent Memory](https://arxiv.org/abs/2609.00243)

**Background**  
Agents reuse learned fixes across episodes, but server-side data drift can silently make those memories wrong.

**Method**  
The protocol attaches cacheability hints, version stamps, dependency vectors and subgraph invalidation information.

**Conclusion**  
Across ~9,400 episodes, the paper reports deterministic version-validity behavior; row-level invalidation recovers 29–33% of baseline token cost on four of seven models and avoids broad over-eviction.

**What we learn**  
Validity/version/dependency is a real Agent-memory control plane, but the broad idea is already emerging rapidly.

**Boundary**  
Application/protocol memory, not smartphone S2/S3 physical state.

---

---
