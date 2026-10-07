# TXN-20261008-SOURCE-IDENTITY-AGENTPROG-01

Date: 2026-10-08

## Trigger
Source Identity QA reported a normalized-title collision between PAPER-030 and PAPER-056.

## Review
Both records have the same AgentProg title and author list.
PAPER-030 is the arXiv / MobiSys canonical record.
PAPER-056 is the ACM DOI entry for the same work.

## Resolution
- PAPER-030 remains canonical.
- Added arXiv ID 2512.10371 and DOI 10.1145/3745756.3809245 to PAPER-030.
- PAPER-056 becomes ALIAS → PAPER-030.
- Active EC-A-005-A and EXP-A-001 inputs migrated to PAPER-030.
- Current graph projections regenerated semantically.

## Decision impact
No technical conclusion changes.
The change prevents one paper from being counted as two independent pieces of evidence.
