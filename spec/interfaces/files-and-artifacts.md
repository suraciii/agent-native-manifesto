# Files and artifacts

Files can carry inputs, context, editable content, or outputs. An artifact is a result kept available for inspection or further use; a file is one possible representation. The general result contract comes from AN-08 in the [core specification](../core.md).

This is a supporting profile for assessed work that uses files. It does not establish a separate execution interface or require an application to use files. A CLI that accepts an image and writes a resized copy uses CLI access, with files as input and output. A function can return a value directly without creating a file.

## Role and fit

Files work well when content is central, the caller and application share an authorized filesystem or transfer path, and ordinary editors or programs can inspect the work. Document the format, access, relevant version, and relation to application state so that another operation can use the content.

An application with shared remote state, strong domain constraints, or many concurrent actors may need controlled import and update operations. A file representation can remain useful even when a validated operation owns commitment.

## Design choices

### Define the file's role

| Role | When it becomes effective | Main obligation |
| --- | --- | --- |
| Input or context | An operation reads the content | State format, access, and any freshness constraints |
| Authoritative document | The application reads the accepted document version | State the validation and consistency rules |
| Draft | A user or agent edits it before submission | Do not imply that saving publishes or commits |
| Import | A defined import operation accepts its contents | Validate, report scope and partial effects |
| Export | A snapshot is written for another use | State freshness, access, and information loss |
| Artifact | A completed output is made available | Supply usable identity, media information, and retrieval |

Reading a source file, saving a draft, importing data, and publishing a result have different meanings. The application needs only the roles used by its supported work.

### Optional file-driven behavior

Some applications explicitly use file changes or submissions to trigger work. A configuration change may take effect on reload. A processing tool may watch a directory and accept completed submissions. In such designs, file handling forms part of the capability access contract.

Document the trigger, validation, authority, effects, and result of that behavior. A filesystem watcher alone does not define whether a change is a draft save, a committed update, or a new submission. Apply the core requirements to the actual trigger and effect boundary. Ordinary file inputs and outputs do not require this design.

### Native content and structured metadata

Use existing formats that fit the content. Markdown, images, CSV, and domain-specific document formats can be appropriate. Metadata can live in the application's object model instead of forcing every native file into a new wrapper.

Where metadata is required, define its schema and relation to the content. Do not hide essential instructions or authorization in comments that a normal editor may remove. An export of a document may omit review history or provenance; that loss should be visible.

### Publication, concurrency, and durability

On supported systems, writing a temporary file and renaming it can prevent readers from seeing a partially written destination. The [Linux rename documentation](https://man7.org/linux/man-pages/man2/rename.2.html) distinguishes atomic replacement, no-replacement options, and cross-filesystem limits. Atomic visibility does not imply crash durability: [fsync documentation](https://man7.org/linux/man-pages/man2/fsync.2.html) explains that persisting a file may also require persisting its directory entry.

These mechanisms solve different problems from concurrent intent. Two valid writers can still overwrite each other's complete output. Use the application's declared conflict policy, such as an expected revision, serialization, or explicit exclusive ownership.

A check that the destination does not exist followed by an ordinary overwriting rename is not an atomic no-overwrite operation. A hash comparison separated from an unguarded write is not a compare-and-swap. State the platform assumptions behind any guarantee.

### Paths and trust

A path is interpreted in an environment. A local server path does not give a remote agent access to the artifact. A resource identified with a file-like URI may require a protocol read rather than a filesystem open.

When the application promises a workspace boundary, its path handling needs to enforce that boundary, including symbolic links and concurrent path changes where applicable. Do not accept a file edit as permission to bypass domain validation or execute embedded commands. File ownership and execution authority are separate concepts.

## Requirements

### FILE-01 — Format and meaning

**Applies when the assessed work uses files as inputs, context, content, or outputs.**

The application MUST document supported file formats, paths or discovery rules, ownership, and each file's role. It MUST identify required fields where a format has them. Where file changes affect application behavior, it MUST define the operation or trigger that makes them effective.

Structured inputs MUST be validated before producing effects. Invalid content MUST yield a useful failure rather than silent partial interpretation. A native content format MAY carry its own syntax instead of a new JSON wrapper.

Where an import permits partial application, the application MUST state that policy before commitment and identify accepted and rejected parts. Saving a draft MUST NOT be reported as a committed application change unless that is the declared contract.

### FILE-02 — Change and access

**Applies to file access, writes, and transfers managed by the application in the assessed work.**

For application-managed writes to shared mutable files, the application MUST declare and enforce a conflict policy. For writes or imports, it MUST describe the effect of incomplete writes or interrupted imports. An application MUST NOT expose direct file or database writes as a way to bypass invariants required by other interfaces.

References to files MUST be meaningful in the caller's environment, or provide an authorized transfer path. A local path on a remote server alone is not a usable artifact reference for a remote caller.

Claims of atomicity, no-overwrite behavior, or durability MUST state their storage and platform assumptions. Declared path or workspace restrictions MUST be enforced where file access occurs.

## Example

This is an illustrative workflow for the [reporting service](../../examples/reporting-service.md).

The caller exports a draft revision as Markdown, edits it, and submits it through an import operation with the expected base revision. The file is a draft until import succeeds. If another user has revised the report, import reports a conflict and preserves the submitted content for reconciliation according to the product's policy.

The import operation can be invoked through the service's declared CLI, HTTP, or MCP access. Exported content supports that path; it does not require a separate execution interface. The service's publication operation remains separate. Editing a local file does not publish a report. An export link or downloaded path still needs its relation to the source revision so the agent can reason about freshness.

For a fully local alternative, see the [image-tool example](../../examples/local-tool.md). It uses a no-overwrite output policy rather than a remote revision system.

## Verification

| Requirement | Important cases |
| --- | --- |
| FILE-01 | Input and output formats; context freshness; invalid structured content; save versus commit; accepted and rejected import rows; export information loss |
| FILE-02 | Interrupted write; simultaneous writers; cross-filesystem publication; existing destination; symlink or path-boundary cases; remote retrieval |

For a claimed file-driven path, also test the declared trigger, rejection of invalid submissions, and observable results. Run write, concurrency, and durability cases only where those behaviors are offered. Test storage guarantees on the supported platform and use controlled faults to test interruption. A successful write in one ordinary run does not establish crash durability. Apply the [evaluation procedure](../evaluation.md).

## Sources and related topics

- [Linux rename](https://man7.org/linux/man-pages/man2/rename.2.html) and [fsync](https://man7.org/linux/man-pages/man2/fsync.2.html): concrete filesystem guarantees and their limits, not cross-platform promises.
- [Git status](https://git-scm.com/docs/git-status): an example of explicit machine framing for paths with unusual characters.
- Related profiles: [CLI](cli.md), [SDK](sdk.md), [MCP resources](mcp.md), and [presentation](presentation.md).
