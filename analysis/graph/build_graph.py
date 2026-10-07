#!/usr/bin/env python3
import argparse
import json
import tomllib
from pathlib import Path
from write_guard import assert_candidate_root

ROOTS = [
    "01-evidence","02-claims","03-evidence-cases","04-actors",
    "05-capabilities","06-directions","07-validation","08-decisions","09-roadmap"
]

def parse_frontmatter(path: Path, root: Path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("+++\n"):
        return None
    end = text.find("\n+++\n", 4)
    if end < 0:
        raise ValueError(f"unterminated TOML front matter: {path}")
    meta = tomllib.loads(text[4:end])
    meta["_path"] = path.relative_to(root).as_posix()
    return meta

def load_nodes(root: Path):
    nodes=[]
    for rel in ROOTS:
        base=root/rel
        if not base.exists():
            continue
        for path in sorted(base.rglob("*.md")):
            meta=parse_frontmatter(path, root)
            if meta:
                nodes.append(meta)
    return nodes

def canonical_edges(nodes):
    edges=[]
    def add(s,r,t):
        edges.append({"source":s,"relation":r,"target":t,"provenance":"CANONICAL_SEMANTIC"})
    for n in nodes:
        i=n["id"]; t=n["type"]
        if t=="SOURCE":
            for a in n.get("publisher_actor_ids",[]): add(i,"PUBLISHED_BY",a)
            for p in n.get("provenance_parents",[]): add(i,"PROVENANCE_PARENT",p)
        elif t=="CLAIM":
            for a in n.get("subject_actor_ids",[]): add(i,"SUBJECT_ACTOR",a)
            for c in n.get("supersedes",[]): add(i,"SUPERSEDES",c)
        elif t=="EVIDENCE_CASE":
            for p in n.get("premises",[]): add(i,"HAS_PREMISE",p["ref_id"])
            add(i,n["relation"],n["target_id"])
        elif t=="CAPABILITY":
            for a in n.get("actor_links",[]): add(i,"ACTOR_LINK",a["actor_id"])
            for c in n.get("evidence_claims",[]): add(i,"EVIDENCED_BY_CLAIM",c)
        elif t=="DIRECTION":
            for c in n.get("related_claims",[]): add(i,"RELATED_CLAIM",c)
            for c in n.get("related_capabilities",[]): add(i,"RELATED_CAPABILITY",c)
            for a in n.get("related_actors",[]): add(i,"RELATED_ACTOR",a)
        elif t=="EXPERIMENT":
            for d in n.get("direction_ids",[]): add(i,"TESTS_FOR_DIRECTION",d)
            for c in n.get("tests_claim_ids",[]): add(i,"TESTS_CLAIM",c)
            for s in n.get("input_source_ids",[]): add(i,"INPUT_SOURCE",s)
        elif t=="DECISION_EVENT":
            add(i,"SUBJECT",n["subject_id"])
            for c in n.get("trigger_claims",[]): add(i,"TRIGGER_CLAIM",c)
            for e in n.get("trigger_experiments",[]): add(i,"TRIGGER_EXPERIMENT",e)
        elif t=="ROADMAP":
            for d in n.get("direction_ids",[]): add(i,"SCHEDULES",d)
    return edges

REVERSE={
"PUBLISHED_BY":"PUBLISHES","PROVENANCE_PARENT":"PROVENANCE_CHILD",
"SUBJECT_ACTOR":"SUBJECT_OF_CLAIM","SUPERSEDES":"SUPERSEDED_BY",
"HAS_PREMISE":"PREMISE_OF_CASE","SUPPORT":"SUPPORTED_BY_CASE",
"REBUT":"REBUTTED_BY_CASE","SCOPE_LIMIT":"SCOPED_BY_CASE","UNDERCUT":"UNDERCUT_BY_CASE",
"ACTOR_LINK":"HAS_CAPABILITY_LINK","EVIDENCED_BY_CLAIM":"EVIDENCES_CAPABILITY",
"RELATED_CLAIM":"USED_BY_DIRECTION","RELATED_CAPABILITY":"USED_BY_DIRECTION",
"RELATED_ACTOR":"USED_BY_DIRECTION","TESTS_FOR_DIRECTION":"HAS_EXPERIMENT",
"TESTS_CLAIM":"TESTED_BY_EXPERIMENT","INPUT_SOURCE":"INPUT_TO_EXPERIMENT",
"SUBJECT":"HAS_DECISION_EVENT","TRIGGER_CLAIM":"TRIGGERS_DECISION",
"TRIGGER_EXPERIMENT":"TRIGGERS_DECISION","SCHEDULES":"SCHEDULED_BY"
}

def build_projection(root: Path):
    nodes=load_nodes(root)
    edges=canonical_edges(nodes)
    canon=list(edges)
    for e in canon:
        r=REVERSE.get(e["relation"])
        if r:
            edges.append({"source":e["target"],"relation":r,"target":e["source"],"provenance":"GENERATED_REVERSE"})
    edges.sort(key=lambda x:(x["source"],x["relation"],x["target"],x["provenance"]))
    node_view=[]
    for n in nodes:
        v={"id":n["id"],"type":n["type"],"path":n["_path"]}
        for k in ("record_state","status","claim_kind","lifecycle","direction_class","investment_lane","competitive_action","evidence_maturity"):
            if k in n: v[k]=n[k]
        node_view.append(v)
    node_view.sort(key=lambda x:(x["type"],x["id"]))
    return {
        "schema_version":"2.2",
        "authority":"GENERATED_NOT_AUTHORITY",
        "migration_id":"MIG-20261006-02",
        "nodes":node_view,
        "edges":edges,
        "counts":{
            "nodes":len(node_view),
            "canonical_semantic_edges":sum(e["provenance"]=="CANONICAL_SEMANTIC" for e in edges),
            "generated_reverse_edges":sum(e["provenance"]=="GENERATED_REVERSE" for e in edges)
        }
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--check",action="store_true")
    args=ap.parse_args()
    root=Path(".").resolve()
    assert_candidate_root(root)
    projection=build_projection(root)
    out=root/"views/graph/current.json"
    rendered=json.dumps(projection,indent=2,ensure_ascii=False)+"\n"
    if args.check:
        if not out.exists() or out.read_text(encoding="utf-8") != rendered:
            print("FAIL: generated graph projection differs")
            return 1
        print(f"PASS: graph projection deterministic ({projection['counts']})")
        return 0
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(rendered,encoding="utf-8")
    print(f"WROTE: {out}")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
