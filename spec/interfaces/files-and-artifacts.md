# Files and artifacts

This guide covers files used as input, context, editable content, or output. It applies AN-08 in the [core requirements](../core.md). File inputs and outputs alone do not define an execution interface; applications need not produce files.

## Role and fit

Files suit content that ordinary editors or programs can use through an authorized filesystem or transfer path. Shared state or domain constraints may require controlled import instead of direct commitment through file edits.

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

Use only the roles needed by the supported work. If an import accepts only part of a file, state that policy before the import and identify accepted and rejected parts.

### Optional file-driven behavior

An application may reload configuration or watch a directory for submissions. Define the trigger, validation, authority, effects, and results. A watcher alone does not distinguish draft saves from submissions. Ordinary file input and output need no such trigger.

### Native content and structured metadata

Use suitable native formats without unnecessary wrappers. Metadata may live in the object model; define its relation to the content. Do not hide essential metadata in removable comments. Disclose export losses such as omitted review history or provenance.

### Publication, concurrency, and durability

Temporary-file publication with [rename](https://man7.org/linux/man-pages/man2/rename.2.html) can provide atomic visibility on supported systems, subject to replacement and filesystem rules. Crash durability may require [fsync](https://man7.org/linux/man-pages/man2/fsync.2.html) on both the file and its directory. State the storage and platform assumptions for these guarantees.

Atomic publication does not resolve competing writers. Use the declared conflict policy. Checking for absence before an overwriting rename is not atomic no-overwrite; comparing a hash before an unguarded write is not compare-and-swap.

### Paths and trust

Server-local paths may need authorized transfer; file-like resource URIs may need protocol reads. Enforce any declared workspace boundary, including symlinks and concurrent path changes. A file edit does not grant permission to bypass validation or execute embedded commands.

## Example

In the illustrative [reporting service](../../examples/reporting-service.md), a caller exports a revision as Markdown, edits it, and imports it with the expected base revision. A conflict preserves the submitted content for reconciliation under the product's policy. Local edits do not commit or publish the report; export references identify their source revision.

The local [image tool](../../examples/local-tool.md) instead uses a no-overwrite output policy.

## Verification

| Focus | Cases to try |
| --- | --- |
| Format and meaning | Input and output formats; context freshness; invalid structured content; save versus commit; accepted and rejected import rows; export information loss |
| Change and access | Interrupted write; simultaneous writers; cross-filesystem publication; existing destination; symlink or path-boundary cases; remote retrieval |

Where file-driven behavior is offered, test its trigger, validation, and results. Test claimed storage guarantees on supported platforms with controlled faults. An ordinary successful write does not establish crash durability. Use the [evaluation procedure](../evaluation.md).

## Sources and related topics

- [Linux rename](https://man7.org/linux/man-pages/man2/rename.2.html) and [fsync](https://man7.org/linux/man-pages/man2/fsync.2.html): concrete filesystem guarantees and their limits, not cross-platform promises.
- [Git status](https://git-scm.com/docs/git-status): an example of explicit machine framing for paths with unusual characters.
- Related topics: [CLI](cli.md), [SDK](sdk.md), [MCP resources](mcp.md), and [presentation](presentation.md).
