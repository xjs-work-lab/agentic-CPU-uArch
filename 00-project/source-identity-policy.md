# Source Identity / Dedup Policy

Date: 2026-10-08
State: ACTIVE

## Purpose
Prevent the same paper, patent publication or official source from entering the SSOT under multiple active Source IDs and being incorrectly counted as independent evidence.

## Strong identity keys

Papers:
1. DOI
2. arXiv work ID with version suffix removed
3. canonical primary URL
4. normalized title as warning-only fallback

arXiv v1/v2/v3 are the same work unless a version delta is recorded inside the same canonical Source.

Patents:
1. patent publication number
2. patent family ID as a correlated-evidence grouping key

Different members of one patent family may remain separate publication Sources when claim text or jurisdiction materially matters, but they must not be counted as independent prior-art votes merely because there are multiple family members.

Vendor / official material:
canonical primary URL is a strong identity key. Related product page, newsroom and technical-blog items may remain separate Sources only when they contain materially different evidence.

## Alias contract
Historical duplicates are not deleted when deletion would damage migration/history fidelity.

Instead:
- one Source remains canonical;
- duplicate historical IDs use record_state = ALIAS;
- aliases carry canonical_source_id;
- active Evidence Cases and Experiments MUST reference the canonical Source;
- aliases do not count as independent corroboration.

## Evidence independence
Optional field: evidence_independence_group.
Use it when several Sources are different documents but derive from the same underlying evidence/event/data release.

Optional patent field: patent_family_id.
These are correlation keys, not duplicate keys.

## Hard gate
analysis/graph/source_identity.py --check fails on:
- duplicate DOI without explicit alias resolution;
- duplicate arXiv work ID without explicit alias resolution;
- duplicate patent publication without explicit alias resolution;
- duplicate canonical primary URL without explicit alias resolution;
- bad/cyclic alias;
- Evidence Case or Experiment referencing an alias.

Normalized-title collisions are warnings because legitimate documents can share similar titles.

## Research ingest preflight
Before assigning a new Source ID:
1. check DOI / arXiv ID / patent publication / canonical URL against the SSOT;
2. if matched, reuse and update the existing canonical Source;
3. if it is a newer version of the same work, perform delta review rather than creating a second independent Source;
4. if same patent family, record family relation and do not treat family members as independent corroboration;
5. only create a new Source ID after the identity gate is clear.

## Historical canonicalization

Confirmed canonical groups after the first full identity audit:

- Agent.xpu / arXiv 2506.24045: PAPER-113 canonical; PAPER-097 alias.
- MobiMem / arXiv 2512.15784: PAPER-103 canonical; PAPER-073 alias.
- Cordon / arXiv 2606.17573: PAPER-117 canonical; PAPER-041 alias.
- LOCAL / arXiv 2608.15241: PAPER-104 canonical; PAPER-033 and PAPER-089 aliases.
- Qualcomm Oryon Flex Cache official page: VENDOR-001 canonical; VENDOR-022 alias.
- AgentProg / arXiv 2512.10371 / DOI 10.1145/3745756.3809245: PAPER-030 canonical; PAPER-056 alias.

AgentProg demonstrates why normalized-title warnings remain part of the gate: the arXiv and publisher DOI routes can represent the same work without sharing a URL identity. Once confirmed, the canonical Source should record both identifiers so later discovery resolves directly.
