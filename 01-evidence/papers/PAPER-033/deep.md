# PAPER-033 — LOCAL — FULL_10Q reuse receipt

## Duplicate-primary resolution
PAPER-033 and PAPER-104 are the same primary paper:
LOCAL: Enabling Learning On-device Contiguously for Agent LLMs
https://arxiv.org/abs/2608.15241

Authoritative decision-grade review:
01-evidence/papers/PAPER-104/deep.md

## Why retain PAPER-033
PAPER-033 is a migrated evidence ID used by existing B-residual evidence cases. Retaining it avoids evidence drift.

## Reused findings
- KV validity includes token/context namespace/adapter/version state;
- stale-version KV can be detected and refreshed in software;
- Agent identity is provenance rather than necessarily a hard physical key;
- evaluated on a 24 GB single-GPU system, not smartphone silicon;
- strengthens T5/B software baseline and narrows B-residual.

## Decision
FULL_10Q evidence is reused from the identical primary source and is not counted as independent corroboration.
