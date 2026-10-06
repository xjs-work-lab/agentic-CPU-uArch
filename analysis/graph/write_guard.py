#!/usr/bin/env python3
from pathlib import Path
import sys

def assert_candidate_root(root: Path) -> None:
    root = root.resolve()
    marker = root / "00-project/AUTHORITY.md"
    if not marker.is_file():
        raise RuntimeError(f"candidate authority marker missing: {marker}")
    text = marker.read_text(encoding="utf-8")
    if "CANDIDATE / NOT RESEARCH AUTHORITY" not in text:
        raise RuntimeError("target is not marked candidate/not-authority")
    if "MIG-20261006-02" not in text:
        raise RuntimeError("unexpected migration baseline")

def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    assert_candidate_root(root)
    print(f"PASS: candidate root verified: {root.resolve()}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
