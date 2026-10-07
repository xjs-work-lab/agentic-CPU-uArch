#!/usr/bin/env python3
import argparse
import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlsplit, unquote

from build_graph import load_nodes
from write_guard import assert_candidate_root

ARXIV_RE = re.compile(r"arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})(?:v\d+)?", re.I)
PATENT_URL_RE = re.compile(r"patents\.google\.com/patent/([A-Z]{2}\d+[A-Z]\d?)", re.I)
PATENT_TOKEN_RE = re.compile(r"\b([A-Z]{2}\d{6,}[A-Z]\d?)\b", re.I)
DOI_RE = re.compile(r"(10\.\d{4,9}/[^\s?#]+)", re.I)

def normalize_doi(v):
    if not v:
        return None
    v=str(v).strip()
    v=re.sub(r"^https?://(?:dx\.)?doi\.org/","",v,flags=re.I)
    v=re.sub(r"^doi:\s*","",v,flags=re.I)
    return v.rstrip(" .,/").lower() or None

def normalize_arxiv(v):
    if not v:
        return None
    m=re.search(r"(\d{4}\.\d{4,5})(?:v\d+)?",str(v).strip(),re.I)
    return m.group(1).lower() if m else None

def normalize_patent(v):
    if not v:
        return None
    return re.sub(r"[^A-Z0-9]","",str(v).upper()) or None

def normalize_url(v):
    if not v:
        return None
    try:
        s=urlsplit(str(v).strip())
        host=(s.hostname or "").lower()
        if host.startswith("www."):
            host=host[4:]
        path=re.sub(r"/+","/",unquote(s.path or "/"))
        if path != "/":
            path=path.rstrip("/")
        return host + path
    except Exception:
        return re.sub(r"[?#].*$","",str(v).strip().lower()).rstrip("/")

def title_fingerprint(v):
    if not v:
        return None
    s=unicodedata.normalize("NFKD",str(v)).lower()
    return "".join(ch for ch in s if ch.isalnum()) or None

def identities(n):
    url=n.get("primary_url")
    doi=normalize_doi(n.get("doi"))
    if not doi and url and "doi.org/" in str(url).lower():
        m=DOI_RE.search(str(url))
        doi=normalize_doi(m.group(1)) if m else None
    arxiv=normalize_arxiv(n.get("arxiv_id"))
    if not arxiv and url:
        m=ARXIV_RE.search(str(url))
        arxiv=m.group(1).lower() if m else None
    pub=normalize_patent(n.get("publication_number"))
    if not pub and url:
        m=PATENT_URL_RE.search(str(url))
        pub=normalize_patent(m.group(1)) if m else None
    if not pub and n.get("source_type")=="patent":
        m=PATENT_TOKEN_RE.search(str(n.get("venue",""))+" "+str(n.get("title","")))
        pub=normalize_patent(m.group(1)) if m else None
    return {
        "doi":doi,
        "arxiv":arxiv,
        "patent_publication":pub,
        "canonical_url":normalize_url(url),
        "title_fingerprint":title_fingerprint(n.get("title")),
        "patent_family_id":n.get("patent_family_id"),
        "evidence_independence_group":n.get("evidence_independence_group"),
    }

def canonical_target(by, source):
    seen=set()
    cur=source
    while cur.get("canonical_source_id"):
        if cur["id"] in seen:
            return None
        seen.add(cur["id"])
        nxt=by.get(cur["canonical_source_id"])
        if not nxt or nxt.get("type")!="SOURCE":
            return None
        cur=nxt
    return cur["id"]

def validate(root: Path):
    nodes=load_nodes(root)
    by={n["id"]:n for n in nodes}
    sources=[n for n in nodes if n.get("type")=="SOURCE"]
    errors=[]; warnings=[]
    ids={n["id"]:identities(n) for n in sources}

    for s in sources:
        alias=s.get("canonical_source_id")
        if alias:
            if s.get("record_state")!="ALIAS":
                errors.append(f"SOURCE_ALIAS_NOT_MARKED_ALIAS:{s['id']}:{alias}")
            if alias==s["id"] or alias not in by or by[alias].get("type")!="SOURCE":
                errors.append(f"SOURCE_ALIAS_BAD_TARGET:{s['id']}:{alias}")
            elif canonical_target(by,s) is None:
                errors.append(f"SOURCE_ALIAS_CYCLE:{s['id']}")
        elif s.get("record_state")=="ALIAS":
            errors.append(f"SOURCE_ALIAS_WITHOUT_CANONICAL:{s['id']}")

    for key in ("doi","arxiv","patent_publication","canonical_url"):
        groups=defaultdict(list)
        for s in sources:
            v=ids[s["id"]].get(key)
            if v:
                groups[v].append(s)
        for value,group in sorted(groups.items()):
            if len(group)<2:
                continue
            roots={canonical_target(by,s) for s in group}
            non_alias=[s["id"] for s in group if not s.get("canonical_source_id")]
            if len(roots)!=1 or None in roots or len(non_alias)!=1:
                errors.append(f"DUPLICATE_SOURCE_IDENTITY:{key}:{value}:{','.join(sorted(s['id'] for s in group))}")
            else:
                warnings.append(f"SOURCE_ALIAS_GROUP:{key}:{value}:canonical={non_alias[0]}:members={','.join(sorted(s['id'] for s in group))}")

    title_groups=defaultdict(list)
    for s in sources:
        fp=ids[s["id"]].get("title_fingerprint")
        if fp:
            title_groups[(s.get("source_type"),fp)].append(s)
    for (stype,fp),group in sorted(title_groups.items()):
        if len(group)>1:
            roots={canonical_target(by,s) for s in group}
            if len(roots)>1:
                warnings.append(f"POSSIBLE_DUPLICATE_TITLE:{stype}:{','.join(sorted(s['id'] for s in group))}")

    for meta_key,label in (("patent_family_id","SAME_PATENT_FAMILY"),
                           ("evidence_independence_group","SAME_EVIDENCE_INDEPENDENCE_GROUP")):
        groups=defaultdict(list)
        for s in sources:
            v=ids[s["id"]].get(meta_key)
            if v:
                groups[str(v)].append(s["id"])
        for v,members in sorted(groups.items()):
            if len(members)>1:
                warnings.append(f"{label}:{v}:{','.join(sorted(members))}")

    aliases={s["id"]:s.get("canonical_source_id") for s in sources if s.get("canonical_source_id")}
    for n in nodes:
        if n.get("type")=="EVIDENCE_CASE":
            for p in n.get("premises",[]):
                sid=p.get("ref_id")
                if p.get("ref_kind")=="SOURCE" and sid in aliases:
                    errors.append(f"ALIAS_SOURCE_USED_BY_EVIDENCE_CASE:{n['id']}:{sid}->{aliases[sid]}")
        elif n.get("type")=="EXPERIMENT":
            for sid in n.get("input_source_ids",[]):
                if sid in aliases:
                    errors.append(f"ALIAS_SOURCE_USED_BY_EXPERIMENT:{n['id']}:{sid}->{aliases[sid]}")

    return {
        "sources":len(sources),
        "canonical_sources":sum(not s.get("canonical_source_id") for s in sources),
        "aliases":sum(bool(s.get("canonical_source_id")) for s in sources),
        "errors":errors,
        "warnings":warnings,
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--check",action="store_true")
    ap.parse_args()
    root=Path(".").resolve()
    assert_candidate_root(root)
    result=validate(root)
    result["status"]="PASS" if not result["errors"] else "FAIL"
    print(json.dumps(result,indent=2,ensure_ascii=False))
    return 1 if result["errors"] else 0

if __name__=="__main__":
    raise SystemExit(main())
