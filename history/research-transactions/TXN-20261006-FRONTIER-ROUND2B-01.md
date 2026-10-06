# TXN-20261006-FRONTIER-ROUND2B-01 — H-SCL convergence after WASH

## Question
Does automatic runtime semantic/criticality inference preserve a distinct H-SCL architectural opportunity after AutoDroid-V2, MUSched and Syrup?

## Source completed
- PAPER-062 — Portable Performance on Asymmetric Multicore Processors / WASH (CGO 2016), FULL_10Q.

## New canonical objects
- CLM-C-007
- EC-C-008-A
- DEC-C-005

## Decision
**Do not promote H-SCL to a separate Direction.**

Broad pattern coverage is now:
- semantic→program: PAPER-058 AutoDroid-V2;
- semantic→mobile CPU scheduling: PAPER-060 MUSched;
- portable cross-layer policy: PAPER-061 Syrup;
- automatic runtime criticality inference/heterogeneous CPU placement: PAPER-062 WASH.

Surviving residual questions are folded into A and C.

## Portfolio
- A remains PRIMARY_BET / 82.5.
- C remains STRATEGIC_ENABLER / second-Bet watch / 72.
- CG-06 remains INVEST / 86.5.
- second differentiated Primary Bet remains unfilled.
- R3 remains BLOCKED.

## Pending source
Interactive Context for Mobile OS Resource Management (IEEE TMC 2020) remains PENDING_FULLTEXT and is not decision-grade.

## Next smallest useful step
Stop searching for a standalone semantic-control architecture pattern.
Continue the second-Bet search at the **Agent-specific residual** level: look for evidence that Agent blocked/ready/criticality/cancelability/state-reuse facts change cross-resource smartphone decisions beyond B4-TX/G1.
