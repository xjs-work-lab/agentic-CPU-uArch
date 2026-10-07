# TXN-20261008-SOURCE-IDENTITY-GATE-01

Date: 2026-10-08

## Trigger
Later discovery can rediscover an already-canonical paper/patent and accidentally create a second Source ID, inflating apparent evidence strength.

## Changes
- added hard Source Identity Gate;
- strong keys: DOI / arXiv work / patent publication / canonical URL;
- alias contract added for historical duplicates;
- alias usage in active Evidence Cases / Experiments is forbidden;
- patent-family and evidence-independence grouping supported;
- Graph QA now runs on direct pushes to main as well as pull requests.

## Historical duplicate repaired
PAPER-033 and PAPER-104 are identical primary source: LOCAL, arXiv 2608.15241.

Canonical: PAPER-104.
Historical alias: PAPER-033.

Active references migrated:
- EC-BR-003-A to PAPER-104
- EXP-BR-001 to PAPER-104

No research conclusion changes.

## Next
Continue Round 15A from the latest repository state. All newly discovered Sources must pass identity preflight before ID assignment.
