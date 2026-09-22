# Local tool example

This is an illustrative design, not an implemented or evaluated product. It shows how a small application can follow the [core specification](../spec/core.md) with the [CLI profile](../spec/interfaces.md). The instructions profile also applies to its user guidance. No new command syntax is defined here.

## Intended work

A person asks their coding agent to inspect a set of images and make smaller copies for a document. The installed tool can inspect image metadata and resize images. The host supplies shell execution and authorized filesystem access.

The application has no model runtime, remote service, user account database, or persistent task system. The agent composes its operations with ordinary file handling.

## Capabilities

| Capability | Input | Result and effects |
| --- | --- | --- |
| Inspect an image | Input path | Dimensions, format, and other documented metadata; no content change |
| Resize an image | Input path, maximum dimensions, output path | A new image with a documented aspect-ratio policy |
| Validate an output | Output path and intended constraints | Whether the file can be decoded and whether the checked constraints hold |

Root help explains purpose, version, supported formats, and the three operations. Operation help documents units, defaults, result formats, and significant failures. A short usage page explains the normal inspect, resize, and validate sequence.

The tool's machine mode emits one documented result record. Progress and diagnostics use a separate channel. Errors identify the failed input or condition and have a documented channel and nonzero exit status. Binary image content is written to the requested output file, not mixed into status JSON.

## Effects and interruption

Resizing never overwrites an existing output in the default mode. If a destination exists, the operation fails before changing it. This protects a human's existing work and makes accidental repetition visible.

The implementation writes to a temporary file and publishes a complete output using a method that atomically refuses an existing destination on supported filesystems. The documentation names the filesystem assumptions. It does not promise this behavior on every storage system.

If the process stops before publication, there is no final output. If it stops after publication but before reporting success, the output can exist. The caller checks the destination and validates it before deciding whether to retry. A successful inspection cannot always prove which caller created an existing file; this uncertainty is stated rather than guessed away.

Multi-image work has per-file results. If one file fails, the caller can identify completed outputs and remaining inputs. The application does not claim an all-or-nothing transaction across the batch.

## Human participation

The person can view the copies in any image viewer and change the desired dimensions. The agent then creates new outputs under the revised request. Editing a result externally is allowed; a later inspection reads the current file.

No separate graphical application is required. The artifact and its readable metadata provide inspection. Previously published files are not changed merely because the user changed the next operation.

## Scope and evaluation

Assess AN-01 through AN-06, AN-08, AN-09, and the applicable parts of AN-10. AN-07 is not applicable because each operation ends with its process and no continuing work is accepted. Account, billing, and retained-memory conditions are absent. Files are inputs and artifacts; direct file edits do not invoke hidden application behavior.

Select the CLI and instructions profiles. Add the file profile only if the product offers file edits or imports as an execution interface beyond ordinary input and output files.

Check:

- A fresh agent can find the help and complete the task without private instructions.
- Invalid formats and existing destinations fail with no unintended overwrite.
- A terminated process follows the stated publication boundary.
- Result channels parse correctly and retained references identify the outputs.
- A human can inspect the image and direct another operation.

Use the [evaluation procedure](../spec/evaluation.md) to test a real implementation. This design alone is not evidence that those checks pass.
