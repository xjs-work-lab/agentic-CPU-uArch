#!/usr/bin/env python3
import json
from collections import defaultdict, deque
from pathlib import Path
from write_guard import assert_candidate_root
from build_graph import load_nodes, build_projection

def scc_cycles(adj):
    index=0; stack=[]; on=set(); idx={}; low={}; cycles=[]
    def visit(v):
        nonlocal index
        idx[v]=low[v]=index; index+=1; stack.append(v); on.add(v)
        for w in adj.get(v,[]):
            if w not in idx:
                visit(w); low[v]=min(low[v],low[w])
            elif w in on:
                low[v]=min(low[v],idx[w])
        if low[v]==idx[v]:
            comp=[]
            while True:
                w=stack.pop(); on.remove(w); comp.append(w)
                if w==v: break
            if len(comp)>1 or (len(comp)==1 and comp[0] in adj.get(comp[0],[])): cycles.append(sorted(comp))
    verts=set(adj)
    for vs in adj.values(): verts.update(vs)
    for v in sorted(verts):
        if v not in idx: visit(v)
    return cycles

def validate(root: Path):
    nodes=load_nodes(root); by={}; errors=[]; warnings=[]
    for n in nodes:
        if n["id"] in by: errors.append(f"DUPLICATE_ID:{n['id']}")
        by[n["id"]]=n
    def req(i,t,ctx):
        n=by.get(i)
        if not n: errors.append(f"UNRESOLVED:{i}:{ctx}"); return None
        if t and n["type"]!=t: errors.append(f"TYPE_MISMATCH:{i}:{t}!={n['type']}:{ctx}")
        return n
    support=defaultdict(list); just=defaultdict(list); actor_parent=defaultdict(list)
    used_sources=set()
    for n in nodes:
        t=n["type"]; i=n["id"]
        if t=="SOURCE":
            for a in n.get("publisher_actor_ids",[]): req(a,"ACTOR",f"{i}.publisher_actor_ids")
        elif t=="DISCOVERY_RUN":
            if n.get("lifecycle")=="CLOSED" and not n.get("as_of"): errors.append(f"DISCOVERY_CLOSED_WITHOUT_ASOF:{i}")
        elif t=="CLAIM":
            for a in n.get("subject_actor_ids",[]): req(a,"ACTOR",f"{i}.subject_actor_ids")
        elif t=="EVIDENCE_CASE":
            ps=n.get("premises",[])
            if not ps: errors.append(f"EVIDENCE_CASE_NO_PREMISE:{i}")
            if n.get("relation") in {"SUPPORT","REBUT","SCOPE_LIMIT"} and n.get("target_kind")!="CLAIM": errors.append(f"BAD_CASE_TARGET:{i}")
            if n.get("relation")=="UNDERCUT" and n.get("target_kind")!="EVIDENCE_CASE": errors.append(f"BAD_UNDERCUT_TARGET:{i}")
            req(n["target_id"],n["target_kind"],f"{i}.target")
            just[i].append(n["target_id"])
            for p in ps:
                req(p["ref_id"],p["ref_kind"],f"{i}.premise")
                if p["ref_kind"]=="CLAIM": just[p["ref_id"]].append(i)
                if p["ref_kind"]=="SOURCE": used_sources.add(p["ref_id"])
            for f in ("warrant","scope","boundary"):
                if not n.get(f): errors.append(f"EVIDENCE_CASE_MISSING_{f.upper()}:{i}")
            if n.get("relation")=="SUPPORT" and n.get("target_kind")=="CLAIM": support[n["target_id"]].append(n)
        elif t=="ACTOR":
            p=n.get("parent_actor_id")
            if p: req(p,"ACTOR",f"{i}.parent_actor_id"); actor_parent[i].append(p)
            leak={"competitive_action","investment_lane","strategic_priority"} & set(n)
            if leak: errors.append(f"ACTOR_STRATEGY_LEAK:{i}:{sorted(leak)}")
        elif t=="CAPABILITY":
            if not n.get("actor_links"): errors.append(f"CAPABILITY_NO_ACTOR:{i}")
            if not n.get("evidence_claims"): errors.append(f"CAPABILITY_NO_EVIDENCE_CLAIM:{i}")
            for a in n.get("actor_links",[]): req(a["actor_id"],"ACTOR",f"{i}.actor_links")
            for c in n.get("evidence_claims",[]): req(c,"CLAIM",f"{i}.evidence_claims")
            leak={"competitive_action","investment_lane","strategic_priority"} & set(n)
            if leak: errors.append(f"CAPABILITY_STRATEGY_LEAK:{i}:{sorted(leak)}")
        elif t=="DIRECTION":
            for c in n.get("related_claims",[]): req(c,"CLAIM",f"{i}.related_claims")
            for c in n.get("related_capabilities",[]): req(c,"CAPABILITY",f"{i}.related_capabilities")
        elif t=="EXPERIMENT":
            if not n.get("direction_ids"): errors.append(f"EXPERIMENT_NO_DIRECTION:{i}")
            if not n.get("tests_claim_ids"): errors.append(f"EXPERIMENT_NO_TESTED_CLAIM:{i}")
            for d in n.get("direction_ids",[]): req(d,"DIRECTION",f"{i}.direction_ids")
            for c in n.get("tests_claim_ids",[]): req(c,"CLAIM",f"{i}.tests_claim_ids")
            for s in n.get("input_source_ids",[]): req(s,"SOURCE",f"{i}.input_source_ids"); used_sources.add(s)
        elif t=="DECISION_EVENT":
            req(n["subject_id"],n["subject_kind"],f"{i}.subject")
            for c in n.get("trigger_claims",[]): req(c,"CLAIM",f"{i}.trigger_claims")
            for e in n.get("trigger_experiments",[]): req(e,"EXPERIMENT",f"{i}.trigger_experiments")
        elif t=="ROADMAP":
            for d in n.get("direction_ids",[]): req(d,"DIRECTION",f"{i}.direction_ids")
    jc=scc_cycles(just)
    if jc: errors.append(f"JUSTIFICATION_CYCLE:{jc}")
    ac=scc_cycles(actor_parent)
    if ac: errors.append(f"ACTOR_PARENT_CYCLE:{ac}")
    for n in nodes:
        if n["type"]=="CLAIM":
            if n.get("status")=="SUPPORTED" and not support.get(n["id"]): errors.append(f"SUPPORTED_CLAIM_UNGROUNDED:{n['id']}")
            if n.get("claim_kind")=="BOUNDARY":
                ok=any(any(p["ref_kind"]=="DISCOVERY_RUN" for p in ec.get("premises",[])) for ec in support.get(n["id"],[]))
                if not ok: errors.append(f"BOUNDARY_WITHOUT_DISCOVERY_RUN:{n['id']}")
        if n["type"]=="SOURCE" and n["id"] not in used_sources:
            warnings.append(f"UNCONNECTED_SOURCE:{n['id']}")
        if n["type"]=="SOURCE" and n.get("independence_assessment")=="UNKNOWN":
            warnings.append(f"INDEPENDENCE_UNKNOWN:{n['id']}")

    # Evidence Depth Policy v1 — rescue-mode warnings.
    # A paper is decision-critical here when it directly premises a supported claim used by
    # a Direction scheduled in the current ROADMAP. During rescue mode this is warning-only.
    roadmap_dirs=set()
    for n in nodes:
        if n["type"]=="ROADMAP" and n.get("record_state")=="CURRENT":
            roadmap_dirs.update(n.get("direction_ids",[]))
    critical_source_dirs=defaultdict(set)
    for d in sorted(roadmap_dirs):
        dn=by.get(d)
        if not dn or dn.get("type")!="DIRECTION":
            continue
        for c in dn.get("related_claims",[]):
            for ec in support.get(c,[]):
                for p in ec.get("premises",[]):
                    if p.get("ref_kind")=="SOURCE":
                        critical_source_dirs[p["ref_id"]].add(d)
    for sid,ds in sorted(critical_source_dirs.items()):
        src=by.get(sid,{})
        if src.get("source_type")=="paper" and src.get("priority") in {"P0","P1"}:
            depth=str(src.get("review_depth",""))
            if not depth.startswith("FULL_10Q"):
                warnings.append(f"DECISION_CRITICAL_PAPER_NOT_FULL_10Q:{sid}:{','.join(sorted(ds))}")

    required={"A","CG-06","EXP-A-001","EXP-CG06-001","CLM-A-001","CLM-CG06-EXP-001","DR-HUAWEI-CG06-BASELINE"}
    missing=sorted(required-set(by))
    if missing: errors.append(f"PILOT_REQUIRED_OBJECTS_MISSING:{missing}")
    if not (root/"history/migrations/receipts").is_dir(): errors.append("RECEIPT_DIRECTORY_MISSING")
    return errors,warnings,nodes

def dependency_graph(nodes):
    dep=defaultdict(set)
    for n in nodes:
        i=n["id"]; t=n["type"]
        if t=="EVIDENCE_CASE":
            for p in n.get("premises",[]): dep[p["ref_id"]].add(i)
            dep[i].add(n["target_id"])
        elif t=="CAPABILITY":
            for c in n.get("evidence_claims",[]): dep[c].add(i)
        elif t=="DIRECTION":
            for c in n.get("related_claims",[]): dep[c].add(i)
            for c in n.get("related_capabilities",[]): dep[c].add(i)
        elif t=="EXPERIMENT":
            for c in n.get("tests_claim_ids",[]): dep[c].add(i)
            for s in n.get("input_source_ids",[]): dep[s].add(i)
        elif t=="DECISION_EVENT":
            for c in n.get("trigger_claims",[]): dep[c].add(i)
            for e in n.get("trigger_experiments",[]): dep[e].add(i)
        elif t=="ROADMAP":
            for d in n.get("direction_ids",[]): dep[d].add(i)
    return dep

def impact(nodes,root_id):
    dep=dependency_graph(nodes); seen={root_id}; q=deque([root_id]); out=[]
    while q:
        u=q.popleft()
        for v in sorted(dep.get(u,())):
            if v not in seen: seen.add(v); q.append(v); out.append(v)
    return out

def main():
    root=Path(".").resolve(); assert_candidate_root(root)
    errors,warnings,nodes=validate(root)
    projection=build_projection(root)
    current=json.loads((root/"views/graph/current.json").read_text(encoding="utf-8"))
    if current!=projection: errors.append("GRAPH_PROJECTION_NOT_DETERMINISTIC")
    result={
      "status":"PASS" if not errors else "FAIL",
      "errors":errors,"warnings":warnings,
      "counts":projection["counts"],
      "impact_PAPER_052":impact(nodes,"PAPER-052"),
      "impact_PAPER_009":impact(nodes,"PAPER-009")
    }
    print(json.dumps(result,indent=2,ensure_ascii=False))
    return 1 if errors else 0

if __name__=="__main__":
    raise SystemExit(main())
