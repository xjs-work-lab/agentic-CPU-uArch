#!/usr/bin/env python3
from pathlib import Path
import sys

MIGRATION_ID = "MIG-20261006-02"
FROZEN_V1 = "960abb4ef50f050da3c6784d30826053d42e5c5d"

def read_required(path: Path) -> str:
    if not path.is_file():
        raise RuntimeError(f"required governance marker missing: {path}")
    return path.read_text(encoding="utf-8")

def assert_allowed_root(root: Path) -> str:
    root = root.resolve()
    authority = read_required(root / "00-project/AUTHORITY.md")

    if MIGRATION_ID not in authority:
        raise RuntimeError("unexpected migration baseline")

    # Migration / pre-cutover state.
    if "CANDIDATE / NOT RESEARCH AUTHORITY" in authority:
        return "CANDIDATE"

    # Post-Human-Gate authority state.  This is intentionally stricter than
    # merely accepting an 'active' string: the Human Gate and immutable
    # cutover receipt must both exist and point back to the frozen V1 source.
    if "RESEARCH AUTHORITY / ACTIVE SSOT" in authority:
        human_gate = read_required(root / "00-project/HUMAN-GATE-PACKAGE.md")
        receipt = read_required(
            root / "history/migrations/receipts/MIG-20261006-02-CUTOVER.md"
        )

        if "APPROVED / CUTOVER AUTHORIZED" not in human_gate:
            raise RuntimeError("active authority lacks approved Human Gate")
        if "HUMAN GATE APPROVED" not in human_gate:
            raise RuntimeError("active authority Human Gate decision is not explicit")
        if "Explicit Human Gate decision:" not in receipt or "**APPROVED**" not in receipt:
            raise RuntimeError("active authority lacks approved cutover receipt")
        if FROZEN_V1 not in authority or FROZEN_V1 not in receipt:
            raise RuntimeError("active authority lost frozen V1 provenance")

        return "ACTIVE_AUTHORITY"

    raise RuntimeError(
        "target has neither valid candidate authority nor approved active authority state"
    )

# Backward-compatible entry point used by build_graph.py / health.py.
# Semantics are broader than the legacy function name after authority cutover.
def assert_candidate_root(root: Path) -> None:
    assert_allowed_root(root)

def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    state = assert_allowed_root(root)
    print(f"PASS: repository authority/write boundary verified: {root.resolve()} [{state}]")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
