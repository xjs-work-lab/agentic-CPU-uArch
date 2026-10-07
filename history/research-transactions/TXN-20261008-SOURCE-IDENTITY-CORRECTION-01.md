# TXN-20261008-SOURCE-IDENTITY-CORRECTION-01

Date: 2026-10-08
Type: Quality-gate provenance repair (immutable historical research preserved)

## What QA found
The Round-15A AO-3 commit passed deterministic graph projection but failed source identity QA. Four older arXiv papers had multiple active Source IDs. Additionally the new VENDOR-022 review referred to the same Qualcomm Oryon Flex Cache article already stored as VENDOR-001. These duplicate objects cannot count as independent corroboration.

## Identity mapping (one canonical source per work)
- PAPER-097 → PAPER-113 | Agent.xpu | arXiv 2506.24045
- PAPER-073 → PAPER-103 | MobiMem | arXiv 2512.15784
- PAPER-041 → PAPER-117 | Cordon | arXiv 2606.17573
- PAPER-089 → PAPER-104 | LOCAL | arXiv 2608.15241
- PAPER-033 → PAPER-104 already marked ALIAS | LOCAL
- VENDOR-022 → VENDOR-001 | same Qualcomm Flex Cache official article

## Repair
- Preserve all historical IDs, originals and full review cards.
- Set duplicate Source README front matter to record_state=ALIAS plus canonical_source_id.
- Rewrite live EVIDENCE_CASE premises and EXPERIMENT input_source_ids to canonical IDs; preserve historical prose with explicit corrections.
- Regenerate both graph projections from canonical object metadata.
- Do not interpret duplicate work records as independent supporting publications.

## Research impact
AO-3 still remains KEEP / EVIDENCE_MAPPED; no portfolio lane, hardware hypothesis maturity or score changes. The QA-triggered work fixes provenance integrity, not the research thesis.
