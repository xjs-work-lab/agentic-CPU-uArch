# VENDOR-029 — Primary-source technical 10Q

- Original: https://docs.qualcomm.com/nav/home/htp_shared_buffer_tutorial.html?product=924033590759186372
- Date reviewed: 2026-10-08
- Evidence depth: SECTION_REVIEW — QUALCOMM_OFFICIAL_INDEXED_TECH_DOC
- Decision role: P0 / vendor SDK shared-buffer and memory-control baseline with explicit limitations

## Q1 — Research problem
Repeated CPU-client→HTP inference may copy tensor data, store multiple tensor allocations or repeatedly handle weights/spill buffers.

## Q2 — Mobile mapping
Qualcomm's Android HTP backend supports host CPU using FastRPC, DSP-resident native HTP mode and several shared-buffer descriptor schemes. Important CPU↔NPU path product evidence.

## Q3 — Mechanism premise
Official tutorial states shared buffers *can* eliminate host→accelerator data copy (not a universal zero-copy claim); buffer types depend on FastRPC/native mode.

## Q4 — Lineage
Vendor runtime/host-DSP memory handles, Android ION/DMA buffers, existing NNAPI/AHardwareBuffer/Android burst baselines. These are ordinary platform primitives, not Agent-native inventions.

## Q5 — Detailed resource/control path
QNN_MEM_TYPE_ION one-to-one tensor/FD/handle and QNN_HTP_MEM_SHARED_BUFFER multiple tensor offsets in shared buffer. External WEIGHTS_BUFFER, SHARED_SPILLFILL and SHARED_VTCMBACKUP can be registered to share contexts/scratch depending mode.

## Q6 — Important capabilities and restrictions
Indexed official doc lists FastRPC external buffer mode as sequential-execution dependent for weights and spill-fill; native mode supports some concurrent buffer reuse. External sharing may require binary-created context, alignment and DMA buffers; multiple context registration, graph switching, udma64 and securepd combinations have restrictions in documented cases.

## Q7 — Measured evaluation
SDK document supplies API semantics, not measured phone joules, copy frequency, queue latency or Agent revision-cost; text describes which buffer types are supported, not actual per-SKU speedup.

## Q8 — Source-depth honesty
Direct web full-body fetching of docs.qualcomm.com did not succeed this round. Reviewed **official indexed per-section technical extracts and capability/limitations tables**, not every line of current SDK manual. REVIEW_DEPTH=SECTION_REVIEW (not FULL_10Q). Do not make binary compatibility or performance assertions beyond those excerpts.

## Q9 — AO1/AO3 decision
Generic zero-copy and external buffer lifetime exist; any new Agent fabric must address cross-model/version invalidation and multi-engine state ownership *after* QNN baseline, not invent shared memory.

## Q10 — Next
Follow official QAIRT SDK changes/versions and compatible buffer restrictions in public future material; no local test required for strategic assessment.

## Evidence footer
- Directly supported: published API, product, mechanism, implementation or migration text **inside the specific source's scope**
- Research inference: how that baseline narrows Agentic hardware novelty
- Not established: incremental Agent-specific CPU-uArch value, deployment on all Android devices or matched battery/foreground-QoE results
- No local experiments conducted or planned
