# Shared Strategic-Model Harmonization Audit

Date: 2026-10-07
Scope: CPU/uArch V2.3 semantic alignment only
Constraint: no research conclusion, Trend, Direction, score, maturity, portfolio or directory restructuring.

## Executive result

**PASS WITH MINOR SEMANTIC CLEANUP.**

The existing V2.3 model already matches the shared mother model:

```text
SOURCE → EVIDENCE_CASE → CLAIM → TREND → PRODUCT_EVOLUTION ROADMAP
                              ↘ DIRECTION → DIFFERENTIATION_PORTFOLIO ROADMAP
```

No structural migration is required.

## Audit findings

### 1. TREND semantics — PASS
TREND already means product/technology-stack evolution rather than originality.

No Trend object changed.

### 2. DIRECTION semantics — PASS
DIRECTION already means differentiated/original research whitespace.

No Direction object changed.

### 3. Product posture vocabulary — PASS in canonical objects / CLEANUP in management prose
Canonical Trend frontmatter already uses the shared five-value vocabulary.

The Product Evolution management view contained combined prose forms such as:
- PRODUCTIZE / ADAPT_AND_DIFFERENTIATE
- ADAPT_AND_DIFFERENTIATE / BENCHMARK
- WATCH → audit for upgrade

These were normalized to one canonical posture token, while secondary activities remain prose.

### 4. Differentiation posture vocabulary — PASS in schema / CLEANUP in management projection
The schema and Trend `direction_links` already use the shared five-value vocabulary.

The management table previously summarized postures more broadly than the canonical links and assigned FRONTIER_UNPROVEN to Trends that had no Direction yet.

The table is now a projection of the actual Direction links. Frontier Trends without Directions show no Direction posture.

### 5. Kill scope vocabulary — MINOR GAP FIXED
The policy already named the six desired scopes, but Decision Events did not have a QA-validated canonical `kill_scope` field.

Alignment:
- added the exact six-value vocabulary to the data model and graph rules;
- added QA validation;
- explicit historical/current standalone-Bet kills H-CAL and H-PAM now carry `KILL_DIFFERENTIATED_BET`;
- product posture `DROP_PRODUCT_ROUTE` is explicitly distinguished from decision scope `KILL_PRODUCT_ROUTE`.

No historical decision meaning changed.

### 6. EVIDENCE_CASE semantics — PASS
The graph already models SUPPORT / REBUT / UNDERCUT / SCOPE_LIMIT and requires premise, warrant, scope and boundary.

The shared contract now states explicitly:
- SOURCE = provenance/source-grounded facts;
- EVIDENCE_CASE = inferential route;
- CLAIM = current falsifiable/challengeable proposition.

No Evidence Case was removed or collapsed into audit prose.

### 7. Dual management views — PASS
- `ROADMAP-PRODUCT-2027-2029` = PRODUCT_EVOLUTION
- `ROADMAP-CURRENT` = DIFFERENTIATION_PORTFOLIO

The differentiation roadmap now labels its Product Evolution section as a cross-reference rather than a second canonical write location.

### 8. CPU/uArch domain gate — PASS
Preserved unchanged:

`STRUCTURAL_SIGNAL → SYSTEM_VALUE → SOFTWARE_INSUFFICIENCY → hardware-specific cause → UARCH_CANDIDATE`

## Non-actions by design

This harmonization does **not**:
- import STRATEGIC_ITEM or another sibling-repo object type;
- renumber directories;
- rename canonical IDs;
- modify T1–T8;
- modify Direction lanes/scores/maturity;
- reopen or close research directions;
- change Round 14-A conclusions;
- rewrite historical evidence.

## Result

V2.3 remains the active CPU/uArch data model, now explicitly bound to **STRATEGIC_KG_CORE_V1**.
