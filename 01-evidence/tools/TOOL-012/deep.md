> V1 semantic source copied/repacked from frozen baseline `960abb4ef50a8f5b0bd357c067f08346025d`.
> Do not reinterpret this page as V2.2 metadata authority; the compact README owns the Source object.

### TOOL-012 — ExecuTorch + Arm SME2 on vivo X300

Primary source:
https://pytorch.org/blog/accelerating-on-device-ml-inference-with-executorch-and-arm-sme2/

Fixtures:
- `cg06_executorch_sme2_vivo_x300.csv`
- `cg06_executorch_operator_breakdown.csv`

Direct public-device facts used:
- vivo X300 Android flagship;
- SqueezeSAM;
- ExecuTorch + XNNPACK + KleidiAI;
- 1 CPU core, Normal mode:
  - INT8: 555.8 ms -> 304.1 ms with SME2;
  - FP16: 1163.0 ms -> 298.2 ms;
- 4 CPU cores, Normal mode:
  - INT8: 195 ms -> 180 ms;
  - FP16: 374 ms -> 193 ms;
- SME2-on data movement:
  - INT8: 125.8 ms / 41.4%;
  - FP16: 119.1 ms / 39.9%.

Boundary:
this is real smartphone CPU AI evidence, not CPU-vs-NPU data and not Agent end-to-end evidence.
