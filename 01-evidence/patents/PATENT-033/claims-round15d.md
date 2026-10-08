# PATENT-033 — Round15D Original Claims 1 / Independent / Dependent Re-audit

Dated: 2026-10-08. Canonical existing Source ID retained; no duplicate re-entry. This is a supplementary direct-claim decision audit, not a patent examination/legal opinion.

Original: https://patents.google.com/patent/CN120704926A/en

## Scope and status
CN application publicly pending; priority 2025-06-16; published 2025-09-26, not evidence of chip productization.

## Original independent/dependent claims reviewed
Independent 1: master coordinator allocates atomic Agent operations, monitors execution failure during commit, finds failing Agent and partial/full rollback. Dependent 2 resource locks/preconditions/snapshots; 4 replacement-Agent state handoff or rollback; 5 snapshot+unfinished transaction migration; 6 rollback state verification; 7 progress-dependent simulated commit, conditional on claim 1–6.

## Claim scope versus opportunity
Broad Agent transactional recovery, snapshot and state migration strongly crowded. This patent speaks of coordinator/software RPA transaction recovery, **not physical CPU/NPU command kill, register/KV state reclamation or cache coherence**.

## Precise Keep/Kill
KILL **broad novelty formulations** where the claimed control already overlaps. KEEP **bounded architecture-hypothesis research** only where genuine smartphone cross-xPU physical lifecycle or non-reconstructible user-goal control remains outside the directly reviewed claim features, with hardware necessity **not established**.

## Method caveat
Patent claims delimit specific technical combinations, not every concept with similar words; applications do not prove shipped products; public legal status may require official register checks if a legal decision is needed. This study is not FTO or infringement advice, and no experiments are undertaken.
