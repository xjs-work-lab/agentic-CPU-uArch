#!/usr/bin/env python3
"""Read-only repository archive audit: whole-tree inventory, local Markdown references, and stale active indexes.

No network, dependencies, mutation, scientific inference, or experiments.
Usage: python analysis/graph/repository_archive_audit.py [--json PATH] [--markdown PATH] [--strict-links]
"""
from __future__ import annotations
import argparse
import collections
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
SCAN_EXT = {".md", ".markdown"}
INLINE = re.compile(r'(?<!!)\[[^\]\n]*(?:\[[^\]\n]*\][^\]\n]*)?\]\(\s*<?([^\s)>]+)>?(?:\s+[^)]*)?\)')
IMAGE = re.compile(r'!\[[^\]\n]*\]\(\s*<?([^\s)>]+)>?(?:\s+[^)]*)?\)')
REF_DEF = re.compile(r'^\s*\[[^\]]+\]:\s*<?([^\s>]+)>?', re.MULTILINE)
HTML = re.compile(r'(?:href|src)=[\'"]([^\'"]+)[\'"]')
ACTIVE = [
    "README.md", "CONTINUE-HERE.md", "00-project/STATUS.md",
    "00-project/final-questions-status.md", "09-roadmap/README.md",
    "09-roadmap/leadership-decision-pack/README.md",
    "01-evidence/README.md", "07-validation/README.md",
]
KNOWN_REQUIRED = [
    "CONTINUE-HERE.md",
    "00-project/final-research-archive-acceptance-2026-10-09.md",
    "09-roadmap/current.md",
    "09-roadmap/management-final-public-evidence-2027-2029.md",
    "09-roadmap/leadership-decision-pack/archive/README.md",
    "09-roadmap/leadership-decision-pack/archive/round16c-17-page-speaker-notes-2026-10-09.md",
]
def analyze():
    allfiles = sorted(p for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts)
    rels = [p.relative_to(ROOT).as_posix() for p in allfiles]
    present = set(rels)
    folder_set = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*") if p.is_dir() and ".git" not in p.parts}
    by_root = collections.Counter(p.split("/")[0] for p in rels)
    ext = collections.Counter(Path(p).suffix or "(none)" for p in rels)
    broken = []
    checked = 0
    total_links = 0
    external_links = 0
    stale = []
    duplicates = collections.defaultdict(list)
    for rel, file in zip(rels, allfiles):
        if file.suffix not in SCAN_EXT:
            continue
        content = file.read_text(encoding="utf-8-sig", errors="replace")
        duplicates[hashlib.sha256(content.encode()).hexdigest()].append(rel)
        found = set()
        for regex in (INLINE, IMAGE, REF_DEF, HTML):
            found.update(m.group(1).strip() for m in regex.finditer(content))
        for url in sorted(found):
            total_links += 1
            if url.startswith(("https://", "http://", "mailto:", "data:", "plugin:", "skills:", "file:")) or url.startswith("//"):
                external_links += 1
                continue
            if url.startswith("#"):
                continue
            u = unquote(urlsplit(url).path)
            if not u or u.startswith("/"):
                # Absolute web-root paths cannot be proven inside this GitHub checkout.
                continue
            dest = (file.parent / u).resolve()
            try:
                rdest = dest.relative_to(ROOT.resolve()).as_posix()
            except ValueError:
                broken.append(dict(file=rel, target=url, reason="escapes repo root"))
                continue
            checked += 1
            if rdest not in present and rdest not in folder_set:
                broken.append(dict(file=rel, target=url, resolved=rdest))
    required_missing = sorted(set(KNOWN_REQUIRED) - present)
    # Header / current-authority audits: first 2500 chars only; later sections may preserve history.
    for p in ACTIVE:
        if p not in present: continue
        t = (ROOT/p).read_text(encoding="utf-8-sig", errors="replace")
        pre = t[:2500]
        if re.search(r'Wave 0 contains no migrated', pre, re.I):
            stale.append({"path":p,"type":"WAVE0_PLACEHOLDER","reason":"placeholder retained despite populated canonical objects"})
        if p == "09-roadmap/README.md" and "2026-10-09" not in pre:
            stale.append({"path":p,"type":"OUTDATED_LATEST_POINTER","reason":"claims Round15H latest; finished 17-page archive not top-linked"})
        if p == "09-roadmap/leadership-decision-pack/README.md" and "Round15I V4" in pre and "historical" not in pre.lower():
            stale.append({"path":p,"type":"EARLY_PILOT_FRAMING","reason":"earlier deck design shown as latest"})
        if p == "00-project/STATUS.md" and "CLOSED_WITH_BOUNDARIES" not in pre:
            stale.append({"path":p,"type":"STATUS_STALE","reason":"final closure missing from active header"})
    duplicated = [v for v in duplicates.values() if len(v)>1]
    return dict(
      total_files=len(allfiles), total_dirs=len(folder_set),
      by_root=dict(by_root.most_common()),
      by_extension=dict(ext.most_common()),
      total_markdown=sum(1 for f in allfiles if f.suffix in SCAN_EXT),
      unique_link_targets=total_links, checked_relative_links=checked,
      external_urls_identified=external_links, broken_relative_links=broken,
      stale_active_indexes=stale, missing_required_paths=required_missing,
      exact_content_duplicate_groups=duplicated[:100],
      note="File presence and local path targets are fully scanned. External URL liveness and factual freshness require separate original-source audit.",
    )
def report_md(data):
    def row(s, value): return f"| {s} | {value} |"
    out=["# Complete repository file-tree and local-link audit","",
        "Generated from the full checkout using only stdlib; **all tracked working-tree files** are considered.",
        "This is *not* an independent scientific source re-verification.", "",
        "| Item | Value |","|---|---|",
        row("Files",data["total_files"]),row("Directories",data["total_dirs"]),
        row("Markdown files",data["total_markdown"]),
        row("Relative link targets inspected",data["checked_relative_links"]),
        row("Unresolved local links",len(data["broken_relative_links"])),
        row("Stale active entrypoints",len(data["stale_active_indexes"])),
        row("Missing required final paths",len(data["missing_required_paths"])), "",
        "## Top-level distribution","",
        "| Area | File count |","|---|---:|"]
    out += [row(k,n) for k,n in data["by_root"].items()]
    out += ["","## Broken relative links",""]
    if data["broken_relative_links"]:
        out += [f"- `{e['file']}` → `{e['target']}` (resolved `{e.get('resolved',e.get('reason'))}`)" for e in data["broken_relative_links"][:150]]
        if len(data["broken_relative_links"])>150:out.append(f"- … and {len(data['broken_relative_links'])-150} more (JSON manifest)")
    else:out.append("None detected by the supported Markdown link forms.")
    out += ["","## Stale active entrypoints",""]
    out += [f"- `{e['path']}`: {e['type']} — {e['reason']}" for e in data["stale_active_indexes"]] or ["None"]
    out += ["","## Missing closeout deliverables",""]
    out += [f"- `{x}`" for x in data["missing_required_paths"]] or ["None"]
    out += ["","## Limits and interpretation","",
      "- A file being present does not imply its scientific content is still current. Current/legacy status comes from authority and decision-events.",
      "- GitHub archived slides are separate from the active 17-page source-of-truth decision logic.",
      "- Nonexistent local links are a structural finding; anchors, web link liveness and external image rights require additional checks.",
      "- The current PPTX is **not** present in the Git tree unless specifically uploaded later.",
      ""]
    return "\n".join(out)
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--json")
    p.add_argument("--markdown")
    p.add_argument("--strict-links",action="store_true")
    a=p.parse_args()
    data=analyze()
    if a.json: Path(a.json).write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
    if a.markdown: Path(a.markdown).write_text(report_md(data),encoding="utf-8")
    print(json.dumps({k:v for k,v in data.items() if k not in ("by_root","by_extension","broken_relative_links","exact_content_duplicate_groups")},ensure_ascii=False))
    print("BROKEN_RELATIVE_LINK_COUNT",len(data["broken_relative_links"]))
    return 1 if a.strict_links and (data["broken_relative_links"] or data["missing_required_paths"]) else 0
if __name__=="__main__": sys.exit(main())
