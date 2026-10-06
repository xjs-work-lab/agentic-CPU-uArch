> Exact V1 Stage16A matrix copied from frozen baseline.

# Stage 16A — CG-06 CPU↔NPU Crossover Experiment Matrix

Updated: 2026-10-05  
Lifecycle: CURRENT  
Stage: Stage16A Pass 3  
Canonical role: frozen measurement matrix for CG-06

## Decision question

> Where does CPU-resident execution beat NPU offload for latency-critical Agent-relevant AI stages after dispatch, communication, fallback and layout cost are counted?

This matrix tests **existing hardware + compiler/runtime paths first**.

It is not a new-ISA experiment.

---

## 1. Measurement protocol

### Timing run
- tracing: off/minimal;
- warmup: **10 runs**;
- measured: **30 runs**;
- if latency CV >3%, increase measured runs to **100**;
- report median, mean, P10/P90, CV.

### Trace run
- tracing: on;
- warmup: **3 runs**;
- measured: **5 runs**;
- use for operator/phase attribution, not primary latency.

Reason:
profiling/tracing overhead must not contaminate the primary timing result.

### Thermal/power
Record:
- power mode;
- starting thermal state;
- end thermal state;
- throttling indicator if available.

Do not compare cells from materially different thermal regimes.

---

## 2. H0 — harness sanity / CPU matrix capability

Purpose:
verify the measurement path itself.

Reference:
TOOL-012 / TOOL-013.

Required cells on an SME2-capable platform:

| Model | Backend | Matrix mode | Threads | Layout | Required |
|---|---|---|---:|---|---|
| TOOL-013 supported reference model | CPU | vector/baseline | 1 | runtime default | Yes |
| same | CPU | matrix/SME2 | 1 | runtime default | Yes |
| same | CPU | vector/baseline | 4 | runtime default | Yes |
| same | CPU | matrix/SME2 | 4 | runtime default | Yes |

Required outputs:
- E2E latency;
- CONV/GEMM;
- data movement/layout;
- portable/fallback share;
- delegated share;
- operator top-N.

Pass:
- records export through the Stage16A adapter;
- matrix on/off delta is reproducible;
- trace and timing runs remain separated.

---

## 3. H1 — minimum LLM stage crossover

Reference model families:
- **Llama-3.2-3B**
- **Qwen3-4B**

Reason:
both connect to PAPER-009's public mobile CPU/NPU evidence while keeping the first reproduction set tractable.

### Stage set

| Stage ID | Stage | Required input regime |
|---|---|---|
| P32 | Prefill | 32 input tokens |
| P128 | Prefill | 128 input tokens |
| P512 | Prefill | 512 input tokens |
| D128 | Decode | generate 128 tokens after fixed prompt |

If a backend cannot compile/support a cell, record **UNSUPPORTED**; do not silently replace it.

### Execution paths

1. **CPU-VECTOR**
   - best production-quality non-matrix CPU path;
2. **CPU-MATRIX**
   - best available existing matrix-extension path;
3. **NPU**
   - best supported production-quality NPU path.

Optional:
4. adaptive runtime placement, only after the first three are measured.

### CPU configurations
For CPU-VECTOR and CPU-MATRIX:
- threads: **1, 4**;
- layout state:
  - **COLD** — conversion/packing not retained;
  - **WARM** — reusable layout/state retained where the runtime supports it.

### NPU configurations
- layout state:
  - **COLD** — launch/transfer/conversion included;
  - **WARM** — reusable compiled/layout/state retained where supported.

### Minimum H1 matrix size
Per model/stage:
- CPU-VECTOR: 4 cells;
- CPU-MATRIX: 4 cells;
- NPU: 2 cells.

Total:
- **10 cells / model-stage**
- 2 models × 4 stages = **80 configuration cells**

Unsupported CPU-MATRIX/NPU cells remain explicit N/A/UNSUPPORTED.

---

## 4. Required decomposition per cell

### E2E
- stage latency;
- energy if available;
- thermal/power state.

### CPU
- dispatch/start;
- matrix/vector compute;
- framework/non-delegated;
- layout/data movement.

### NPU
- dispatch/launch;
- CPU↔NPU communication;
- queue;
- transfer/layout conversion;
- accelerator compute;
- synchronization;
- fallback;
- operator coverage.

### Reuse
- model/state residency;
- packed-layout reuse;
- input/output transfer bytes.

---

## 5. Derived crossover outputs

For every model/stage:
1. fastest backend by latency;
2. lowest-energy backend if energy exists;
3. joint latency+energy winner;
4. CPU-matrix uplift over CPU-vector;
5. NPU core-compute advantage;
6. launch/communication tax;
7. fallback tax;
8. layout/data-movement share;
9. warm-vs-cold reuse value.

Do not collapse the matrix into one “CPU vs NPU” average.

---

## 6. H2 — Agent-stage transfer

Only after H1 works.

Required Agent-stage classes:
- embedding;
- router/classifier;
- reranker;
- speech front-end;
- small planner/executor;
- short-context SLM;
- pre/post-processing.

For each real Agent pipeline:
- record the exact operator/shape trace;
- map the stage to the closest H1 regime;
- run CPU-VECTOR / CPU-MATRIX / NPU if supported.

Do not invent a synthetic Agent shape when a real pipeline shape is available.

---

## 7. CG-06 decision gates

### Continue INVEST
At least one representative stage family has a stable CPU-resident region with material:
- latency;
- energy;
- or end-outcome

value after the strongest NPU path is included.

### NARROW
CPU wins only because:
- backend support is missing;
- NPU graph is poorly compiled;
- avoidable fallback dominates.

Then CG-06 becomes a runtime/backend-coverage problem rather than CPU architecture differentiation.

### Hardware consideration
Blocked until:
- existing CPU vector/matrix path is saturated;
- compiler/runtime/layout reuse is strong;
- residual is stable;
- target-phone product value exists.

---

## 8. Canonical output contracts

Run manifest:
`../prototype/contracts/stage16a_run_manifest.schema.json`

Measurement record:
`../prototype/contracts/stage16a_measurement_record.schema.json`

TOOL-013 adapter:
`../analysis/stage16a/harness/tool013_timeline_to_stage16a.py`
