#!/usr/bin/env python3
"""Wave 0 authority/empty-graph health check."""
import json
from pathlib import Path
from write_guard import assert_candidate_root

def main() -> int:
    root = Path(".").resolve()
    assert_candidate_root(root)
    graph_path = root / "views/graph/current.json"
    if not graph_path.is_file():
        raise RuntimeError("generated graph projection missing")
    graph = json.loads(graph_path.read_text(encoding="utf-8"))
    errors = []
    if graph.get("authority") != "GENERATED_NOT_AUTHORITY": errors.append("graph authority invalid")
    if graph.get("migration_id") != "MIG-20261006-02": errors.append("baseline mismatch")
    if graph.get("nodes"): errors.append("Wave 0 must contain zero research nodes")
    if graph.get("edges"): errors.append("Wave 0 must contain zero research edges")
    if errors:
        print("FAIL")
        for e in errors: print(f"- {e}")
        return 1
    print("PASS: Wave 0 authority isolation and empty graph state")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
