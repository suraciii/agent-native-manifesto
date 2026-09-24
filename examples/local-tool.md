# Local tool example

English | [简体中文](../zh-CN/examples/local-tool.md)

This design applies the [application model](../docs/application-model.md) and [core specification](../spec/core.md) to a local image tool. It is **not implemented or evaluated**.

## User task and environment

A user asks their coding agent:

> Make copies with a maximum long edge of 1600 pixels. Keep the originals and show me three samples before processing the rest.

The execution environment supplies shell execution and authorized filesystem access. The agent interprets the task; the installed tool inspects and resizes images. It has no model runtime, server, account database, or persistent task system.

This case starts with a known installed tool. It does not illustrate product discovery from a need; AN-01 still needs a separate assessment.

## Capabilities and context

| Capability | Input | Result and effects |
| --- | --- | --- |
| Inspect an image | Input path | Dimensions, format, and other documented metadata; no content change |
| Resize an image | Input path, maximum dimensions, output path | A new image with a documented aspect-ratio policy |
| Validate an output | Output path and intended constraints | Whether the file can be decoded and whether the checked constraints hold |

Help covers purpose, version, formats, operation contracts, and failures. A short inspect–resize–validate guide suffices; no separate Skill is needed. Inspection supplies current input facts.

Machine mode emits one documented result record. Progress and diagnostics use a separate channel. Errors identify the failed input or condition and use the documented error channel and nonzero exit status. Diagnostic records identify the operation or batch item, the observed effect, and the next check; they distinguish an unknown destination state from a known refusal. Raw process logs are not required. Image bytes go to the output file, not status JSON.

## A complete path

1. The agent reads help and checks formats and output policy within its available authority.
2. It inspects inputs, selects three samples, and chooses output paths that preserve originals.
3. The tool produces three copies with paths and metadata. Validation checks decoding and dimensions; the agent shows the actual samples in an available viewer.
4. The user asks for a maximum long edge of 1200 pixels. The agent creates new samples at separate paths, leaving earlier copies unchanged.
5. After review, the agent applies the agreed setting to remaining inputs. Per-file results identify completed outputs and failures.
6. The agent returns the selected copies for the user's document, distinct from earlier samples. Files remain under the user's control after exit.

Review belongs to the agent's task; the tool does not enforce a personal decision before resizing. Pausing between calls needs no task queue. External edits become visible on a later inspection. An ordinary viewer supplies participation without a tool-owned UI.

## Failure and correction paths

**Existing destination.** The operation refuses to overwrite an existing output and fails before changing it.

**Interrupted write.** The proposed implementation writes a temporary file, then publishes it with an atomic no-overwrite operation on documented supported filesystems. Before publication, no final output exists; afterward, it may exist even if the process stops before reporting success. The diagnostic record identifies the output and reports that publication is unknown; the caller must inspect and validate it before retrying.

The caller checks and validates the destination before retrying. Inspection may not prove which caller created it; that uncertainty remains explicit. Atomic publication alone does not guarantee crash durability.

**Partial batch.** Per-file results distinguish completed outputs, failures, and remaining inputs. The batch is not an all-or-nothing transaction.

**Changed preference.** New dimensions affect later outputs, not existing samples. A successful dimension check does not decide whether the user likes the image.

## Requirement mapping and evidence

Use [CLI](../spec/interfaces/cli.md) access with [instructions](../spec/interfaces/instructions.md) and [file](../spec/interfaces/files-and-artifacts.md) support. Direct file edits do not trigger hidden application work.

| Part of the case | Core requirements |
| --- | --- |
| Complete agent use path | [Scope and coverage](../spec/core.md#scope-and-coverage) |
| Task through normal help | AN-02 |
| Current input facts and bounded effects | AN-02, AN-03, AN-04 |
| Publication and interruption | AN-05, AN-06 |
| Usable output files | AN-08 |
| Sample review and changed dimensions | AN-09 |

AN-07 is not applicable: operations end with their processes; the application accepts no continuing work. Account and billing conditions are absent. This case uses no HTTP, MCP, or SDK access.

Record implementation evidence using the [evaluation procedure](../spec/evaluation.md) and [assessment template](assessment-template.md). No passing results are claimed here.
