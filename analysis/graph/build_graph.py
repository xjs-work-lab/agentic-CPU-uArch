#!/usr/bin/env python3
"""Wave 0 empty graph projection builder."""
import json
from pathlib import Path
from write_guard import assert_candidate_root

def main() -> int:
    root = Path(".").resolve()
    assert_candidate_root(root)
    out = root / "views/graph/current.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    data = {
        "schema_version": "2.2",
        "authority": "GENERATED_NOT_AUTHORITY",
        "migration_id": "MIG-20261006-02",
        "nodes": [],
        "edges": [],
        "edge_provenance_types": ["CANONICAL_SEMANTIC","GENERATED_REVERSE","GENERATED_TRANSITIVE"]
    }
    out.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(f"WROTE: {out}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
