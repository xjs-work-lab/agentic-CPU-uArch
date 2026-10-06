# Graph Tooling — A + CG-06 Pilot

Run from repository root:

```bash
python analysis/graph/write_guard.py .
python analysis/graph/build_graph.py --check
python analysis/graph/health.py
```

The builder parses TOML front matter from canonical Markdown objects and regenerates `views/graph/current.json`.

The health checker validates:
- endpoint types;
- Evidence Case grounding;
- Discovery Run requirement for BOUNDARY Claims;
- justification/Actor cycles;
- Actor/Capability strategic-state leakage;
- Experiment→tested-Claim links;
- deterministic graph projection;
- Pilot required objects;
- bounded impact traversal.

Graph algorithms report structure/impact only. They never change research or strategic state.
