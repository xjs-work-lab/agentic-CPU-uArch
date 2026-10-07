#!/usr/bin/env python3
import argparse
import json
import tomllib
from pathlib import Path
from write_guard import assert_candidate_root

ROOTS = [
    "01-evidence","02-claims","03-evidence-cases","04-actors",
    "05-capabilities","06-trends","06-opportunities","06-directions","07-validation","08-decisions","09-roadmap"
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

OPPORTUNITY_ROLE_REL = {
    "PROBLEM_SIGNAL": "OPPORTUNITY_PROBLEM_SIGNAL",
    "PRODUCT_SIGNAL": "OPPORTUNITY_PRODUCT_SIGNAL",
    "MECHANISM": "OPPORTUNITY_MECHANISM",
    "STRONG_BASELINE": "OPPORTUNITY_STRONG_BASELINE",
    "PRIOR_ART_BOUNDARY": "OPPORTUNITY_PRIOR_ART_BOUNDARY",
    "OPEN_GAP": "OPPORTUNITY_OPEN_GAP",
    "ARCH_HYPOTHESIS": "OPPORTUNITY_ARCH_HYPOTHESIS",
}

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
        elif t=="TREND":
            for c in n.get("related_claims",[]): add(i,"TREND_EVIDENCE_CLAIM",c)
            for c in n.get("related_capabilities",[]): add(i,"TREND_CAPABILITY_SIGNAL",c)
            for d in n.get("direction_links",[]): add(i,"HAS_DIRECTION",d["direction_id"])
        elif t=="ARCHITECTURE_OPPORTUNITY":
            for link in n.get("claim_links",[]):
                add(i,OPPORTUNITY_ROLE_REL[link["role"]],link["claim_id"])
            for tr in n.get("related_trends",[]): add(i,"OPPORTUNITY_TREND",tr)
            for d in n.get("related_directions",[]): add(i,"OPPORTUNITY_DIRECTION",d)
            for c in n.get("related_capabilities",[]): add(i,"OPPORTUNITY_CAPABILITY",c)
            for a in n.get("related_actors",[]): add(i,"OPPORTUNITY_ACTOR",a)
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
            for tr in n.get("trend_ids",[]): add(i,"SCHEDULES_TREND",tr)
    return edges

REVERSE={
"PUBLISHED_BY":"PUBLISHES","PROVENANCE_PARENT":"PROVENANCE_CHILD",
"SUBJECT_ACTOR":"SUBJECT_OF_CLAIM","SUPERSEDES":"SUPERSEDED_BY",
"HAS_PREMISE":"PREMISE_OF_CASE","SUPPORT":"SUPPORTED_BY_CASE",
"REBUT":"REBUTTED_BY_CASE","SCOPE_LIMIT":"SCOPED_BY_CASE","UNDERCUT":"UNDERCUT_BY_CASE",
"ACTOR_LINK":"HAS_CAPABILITY_LINK","EVIDENCED_BY_CLAIM":"EVIDENCES_CAPABILITY",
"TREND_EVIDENCE_CLAIM":"SUPPORTS_TREND","TREND_CAPABILITY_SIGNAL":"SIGNALS_TREND",
"HAS_DIRECTION":"PART_OF_TREND",
"OPPORTUNITY_PROBLEM_SIGNAL":"PROBLEM_SIGNAL_FOR_OPPORTUNITY",
"OPPORTUNITY_PRODUCT_SIGNAL":"PRODUCT_SIGNAL_FOR_OPPORTUNITY",
"OPPORTUNITY_MECHANISM":"MECHANISM_FOR_OPPORTUNITY",
"OPPORTUNITY_STRONG_BASELINE":"STRONG_BASELINE_FOR_OPPORTUNITY",
"OPPORTUNITY_PRIOR_ART_BOUNDARY":"PRIOR_ART_BOUNDARY_FOR_OPPORTUNITY",
"OPPORTUNITY_OPEN_GAP":"OPEN_GAP_FOR_OPPORTUNITY",
"OPPORTUNITY_ARCH_HYPOTHESIS":"ARCH_HYPOTHESIS_FOR_OPPORTUNITY",
"OPPORTUNITY_TREND":"CONTEXT_FOR_OPPORTUNITY",
"OPPORTUNITY_DIRECTION":"ROUTE_FOR_OPPORTUNITY",
"OPPORTUNITY_CAPABILITY":"CAPABILITY_SIGNAL_FOR_OPPORTUNITY",
"OPPORTUNITY_ACTOR":"ACTOR_SIGNAL_FOR_OPPORTUNITY",
"RELATED_CLAIM":"USED_BY_DIRECTION","RELATED_CAPABILITY":"USED_BY_DIRECTION",
"RELATED_ACTOR":"USED_BY_DIRECTION","TESTS_FOR_DIRECTION":"HAS_EXPERIMENT",
"TESTS_CLAIM":"TESTED_BY_EXPERIMENT","INPUT_SOURCE":"INPUT_TO_EXPERIMENT",
"SUBJECT":"HAS_DECISION_EVENT","TRIGGER_CLAIM":"TRIGGERS_DECISION",
"TRIGGER_EXPERIMENT":"TRIGGERS_DECISION","SCHEDULES":"SCHEDULED_BY",
"SCHEDULES_TREND":"TREND_SCHEDULED_BY"
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
        for k in ("record_state","status","claim_kind","lifecycle","direction_class","investment_lane","competitive_action","evidence_maturity","trend_maturity","product_posture","coverage_state","opportunity_stage","priority_rank","roadmap_kind","kill_scope"):
            if k in n: v[k]=n[k]
        if "trend_ids" in n: v["trend_ids"]=n["trend_ids"]
        if "direction_links" in n: v["direction_links"]=n["direction_links"]
        node_view.append(v)
    node_view.sort(key=lambda x:(x["type"],x["id"]))
    return {
        "schema_version":"2.4",
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


def build_dependency_projection(root: Path):
    nav=build_projection(root)
    reverse_relations={
        "HAS_PREMISE": "PREMISE_TO_CASE",
        "EVIDENCED_BY_CLAIM": "CLAIM_TO_CAPABILITY",
        "TREND_EVIDENCE_CLAIM": "CLAIM_TO_TREND",
        "TREND_CAPABILITY_SIGNAL": "CAPABILITY_TO_TREND",
        "RELATED_CLAIM": "CLAIM_TO_DIRECTION",
        "RELATED_CAPABILITY": "CAPABILITY_TO_DIRECTION",
        "INPUT_SOURCE": "SOURCE_TO_EXPERIMENT",
        "TESTS_CLAIM": "CLAIM_TO_EXPERIMENT",
        "TRIGGER_CLAIM": "CLAIM_TO_DECISION",
        "TRIGGER_EXPERIMENT": "EXPERIMENT_TO_DECISION",
        "SCHEDULES": "DIRECTION_TO_ROADMAP",
        "SCHEDULES_TREND": "TREND_TO_ROADMAP",
        "OPPORTUNITY_PROBLEM_SIGNAL": "CLAIM_TO_OPPORTUNITY_PROBLEM",
        "OPPORTUNITY_PRODUCT_SIGNAL": "CLAIM_TO_OPPORTUNITY_PRODUCT",
        "OPPORTUNITY_MECHANISM": "CLAIM_TO_OPPORTUNITY_MECHANISM",
        "OPPORTUNITY_STRONG_BASELINE": "CLAIM_TO_OPPORTUNITY_BASELINE",
        "OPPORTUNITY_PRIOR_ART_BOUNDARY": "CLAIM_TO_OPPORTUNITY_PRIOR_ART",
        "OPPORTUNITY_OPEN_GAP": "CLAIM_TO_OPPORTUNITY_GAP",
        "OPPORTUNITY_ARCH_HYPOTHESIS": "CLAIM_TO_OPPORTUNITY_HYPOTHESIS",
        "OPPORTUNITY_TREND": "TREND_TO_OPPORTUNITY",
        "OPPORTUNITY_CAPABILITY": "CAPABILITY_TO_OPPORTUNITY",
    }
    same_relations={
        "SUPPORT": "CASE_SUPPORTS",
        "REBUT": "CASE_REBUTS",
        "SCOPE_LIMIT": "CASE_SCOPE_LIMITS",
        "UNDERCUT": "CASE_UNDERCUTS",
        "SUBJECT": "DECISION_TO_SUBJECT",
        "OPPORTUNITY_DIRECTION": "OPPORTUNITY_TO_DIRECTION",
    }
    edges=[]
    for e in nav["edges"]:
        if e["provenance"]!="CANONICAL_SEMANTIC":
            continue
        r=e["relation"]
        if r in reverse_relations:
            edges.append({
                "source":e["target"],
                "relation":reverse_relations[r],
                "target":e["source"],
                "provenance":"DERIVED_DEPENDENCY",
            })
        elif r in same_relations:
            edges.append({
                "source":e["source"],
                "relation":same_relations[r],
                "target":e["target"],
                "provenance":"DERIVED_DEPENDENCY",
            })
    edges.sort(key=lambda x:(x["source"],x["relation"],x["target"]))
    return {
        "schema_version":"2.4",
        "view_kind":"CANONICAL_DEPENDENCY",
        "authority":"GENERATED_NOT_AUTHORITY",
        "migration_id":"MIG-20261006-02",
        "nodes":nav["nodes"],
        "edges":edges,
        "counts":{"nodes":len(nav["nodes"]),"dependency_edges":len(edges)}
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--check",action="store_true")
    args=ap.parse_args()
    root=Path(".").resolve()
    assert_candidate_root(root)
    projection=build_projection(root)
    dependency=build_dependency_projection(root)
    out=root/"views/graph/current.json"
    dep_out=root/"views/graph/dependency.json"
    rendered=json.dumps(projection,indent=2,ensure_ascii=False)+"\n"
    dep_rendered=json.dumps(dependency,indent=2,ensure_ascii=False)+"\n"
    if args.check:
        failed=False
        if not out.exists() or out.read_text(encoding="utf-8") != rendered:
            print("FAIL: generated graph projection differs")
            failed=True
        if not dep_out.exists() or dep_out.read_text(encoding="utf-8") != dep_rendered:
            print("FAIL: generated dependency projection differs")
            failed=True
        if failed:
            return 1
        print(f"PASS: graph projections deterministic ({projection['counts']}, dependency={dependency['counts']})")
        return 0
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(rendered,encoding="utf-8")
    dep_out.write_text(dep_rendered,encoding="utf-8")
    print(f"WROTE: {out}")
    print(f"WROTE: {dep_out}")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
