# Local tool example

This is an illustrative design, not an implemented or evaluated product. It applies the [application model](../docs/application-model.md) to a small tool and maps the use path to the [core specification](../spec/core.md). No new command syntax is defined here.

## User task and environment

A person asks their coding agent:

> Make copies with a maximum long edge of 1600 pixels. Keep the originals and show me three samples before processing the rest.

The installed tool inspects image metadata and resizes images. The host supplies shell execution and authorized filesystem access. The agent interprets the natural-language request and organizes the work. The application has no model runtime, remote service, account database, or persistent task system.

## Capabilities and context

| Capability | Input | Result and effects |
| --- | --- | --- |
| Inspect an image | Input path | Dimensions, format, and other documented metadata; no content change |
| Resize an image | Input path, maximum dimensions, output path | A new image with a documented aspect-ratio policy |
| Validate an output | Output path and intended constraints | Whether the file can be decoded and whether the checked constraints hold |

Root help explains purpose, version, supported formats, and the three operations. Operation help documents units, defaults, result formats, output policy, and significant failures. A short usage page explains the usual inspect, resize, and validate method. Image inspection supplies the current facts for the selected inputs. A separate Skill is not needed for this small use path.

The tool's machine mode emits one documented result record. Progress and diagnostics use a separate channel. Errors identify the failed input or condition and have a documented channel and nonzero exit status. Binary image content is written to the requested output file, not mixed into status JSON.

## A complete path

1. The agent finds the installed tool's help and learns how to inspect, resize, and validate. It checks the supported formats and output policy within the host's existing authority.
2. The agent inspects relevant inputs, selects three samples, and chooses output paths that preserve the originals. The application provides file facts and operation contracts; the agent supplies the task-specific sequence.
3. The tool produces three copies within the requested bound and returns their paths and relevant metadata. Validation checks decoding and dimensions. The agent makes the actual samples available in a viewer supported by the environment.
4. The person asks for a maximum long edge of 1200 pixels. The agent creates revised samples at new output paths, keeping the earlier copies distinct. No claim is made that the earlier files changed.
5. After the person reviews the revised samples, the agent applies the agreed setting to the remaining inputs. Per-file results identify completed outputs and any failures.
6. The agent returns the selected copies for use in the person's document, with enough information to distinguish them from the earlier samples. The files remain under the user's filesystem control after the tool exits.

The agent can pause between calls for review without the application implementing a task queue. Editing a result externally is allowed; a later inspection reads the current file. An ordinary image viewer supplies human participation without requiring the tool to have its own graphical UI.

## Failure and correction paths

**Existing destination.** Resizing does not overwrite an existing output in this design. If a destination exists, the operation fails before changing it. This preserves the person's work and makes accidental repetition visible.

**Interrupted write.** The proposed implementation writes to a temporary file and publishes a complete output using a method that atomically refuses an existing destination on supported filesystems. Its documentation identifies those assumptions. Before publication, no final output exists; after publication, the output can exist even if the process stops before reporting success.

The caller checks the destination and validates it before deciding whether to retry. A successful inspection cannot always prove which caller created an existing file; that uncertainty remains explicit. No crash-durability guarantee follows merely from atomic publication.

**Partial batch.** Each image has a result. If one fails, the caller can identify completed outputs and remaining inputs. The application does not claim an all-or-nothing transaction across the batch.

**Changed preference.** New dimensions apply to subsequent operations. Existing samples remain available for comparison. A successful dimension check does not decide whether the person likes the image; viewing the sample supports that judgment.

## Requirement mapping and evidence

Select [CLI](../spec/interfaces/cli.md) for capability access, with [instructions](../spec/interfaces/instructions.md) and [files and artifacts](../spec/interfaces/files-and-artifacts.md) as supporting profiles. Files carry inputs and outputs; direct edits do not invoke hidden application behavior.

| Part of the case | Core requirements | Evidence required from an implementation |
| --- | --- | --- |
| Natural-language task through normal help | AN-01, AN-02, AN-10 | An agent can find the relevant operations without hidden instructions; descriptions and versions match behavior |
| Current input facts and bounded effects | AN-02, AN-03, AN-04 | Inspection is accurate; invalid inputs fail appropriately; original files remain unchanged |
| Output publication and interruption | AN-05, AN-06 | Reported outcomes match files on disk; existing destinations are preserved; controlled interruption follows the declared boundary |
| Results used in the next activity | AN-08 | The authorized caller can retrieve, decode, and use the selected copies |
| Sample review and changed dimensions | AN-09 | The person can inspect the samples and the later outputs reflect the revised request |

AN-07 is not applicable: every operation ends with its process and the application accepts no continuing work. Account, billing, and retained-memory conditions are absent. HTTP, MCP, and SDK profiles are outside this case's scope.

The table names checks to perform, not passing results. Use the [evaluation procedure](../spec/evaluation.md) and [assessment template](assessment-template.md) to record each applicable core and profile requirement. Application behavior and agent task trials remain **not evaluated** in this design example.
