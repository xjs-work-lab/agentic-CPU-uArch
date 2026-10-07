# TXN-20261007-SCHEMA-TREND-V23-01

Date: 2026-10-07
Type: DATA_MODEL_EVOLUTION

## Decision
Add canonical TREND objects and split Roadmap semantics into Product Evolution vs Differentiation Portfolio.

## Compatibility
No existing canonical object is renamed or moved.
No historical Decision Event is rewritten.

## Added
- T1–T8 TREND nodes
- ROADMAP-PRODUCT-2027-2029

## Enriched
- ROADMAP-CURRENT → DIFFERENTIATION_PORTFOLIO
- product-evolution-map → canonical PRODUCT_EVOLUTION ROADMAP
- graph projection schema 2.3
- Graph QA validates Trend maturity/posture, Direction links and Roadmap kinds

## Reason
Prevent prior-art/novelty pressure from accidentally suppressing product-relevant technology trends.
