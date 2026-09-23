# Command-line interfaces

A CLI exposes local or remote capabilities through a process. This guide applies the [core requirements](../core.md); use the [interface overview](../interfaces.md) to choose access paths.

## Role and fit

The host needs an executable, appropriate access, and a way to capture output and exit status. State installation requirements for supported environments. Shell tools can transform data without loading it all into model context. If the host cannot install or run commands, consider remote HTTP or MCP access.

## Design choices

### Help, schemas, and methods

Root help identifies command groups; command help explains operations. Make `--help` available without business effects, and keep basic local help usable without network access or authentication. A small tool can keep its whole contract there. Larger tools can link to references or machine-readable descriptions. [Skills and guides](instructions.md) explain methods without copying parameter definitions.

### Non-interactive use

Accept task inputs through arguments, files, or stdin. In non-interactive mode, report missing input or provide an explicit human handoff instead of waiting for a hidden prompt. Sign-in and reserved human decisions can use a browser or separate flow; explain how the caller learns that the handoff is complete. The application's access policy still applies.

### Human output and script output

[GitHub CLI](https://cli.github.com/manual/gh_help_formatting) offers `--json` field selection and `--jq` transformations. [Git status](https://git-scm.com/docs/git-status) offers porcelain output and NUL-delimited paths. Structured records and native streams can both work; binary or text artifacts need no JSON wrapper.

Document result and error channels. Keep machine output free of terminal decorations and separate result and error records from diagnostics. An error record can use stdout or stderr under a documented contract.

For streams, define record boundaries and completion: a parseable prefix may still be a failed export. Newline splitting is unsafe for filenames that can contain newlines.

### Shell behavior is part of the interface

Prefer argument arrays for direct process calls. With a shell, quote literal data and separate it from executable syntax. Use files or stdin for complex input; explain special characters such as `@`, wildcards, and `--`.

In [gh api](https://cli.github.com/manual/gh_api), field flags change the default method from GET to POST. Queries then need an explicit method; other CLIs may differ.

Expose the CLI version, target service, active project, authentication scope, and relevant environment without leaking secrets. Working directory and environment variables can change a command's meaning. Use protected credential mechanisms; command-line arguments can expose secrets in process listings or history.

### Local exit and remote effects

A zero exit status can confirm submission while remote work is still pending. Return the work identity and a way to check its status. Client termination may only end observation of that work. A pipe consumer may also stop before its producer finishes. Define recovery independently of the last printed line.

For batches, state whether effects are atomic or item-specific and report partial results. A CLI wrapping an SDK needs one retry policy per logical operation. Outer retries can multiply attempts or create new operations; see [SDK retry ownership](sdk.md#retry-ownership).

## Example

These read-only commands require an installed, authenticated GitHub CLI and network access. Results are live data.

```sh
gh repo view cli/cli --json nameWithOwner,defaultBranchRef
```

The lower-level client returns the same fields through an explicit HTTP request:

```sh
gh api --method GET repos/cli/cli --jq '{nameWithOwner: .full_name, defaultBranchRef: {name: .default_branch}}'
```

The first command hides endpoint mapping; the second exposes it. Both reach the same product. For local execution and interruption, see the [image tool](../../examples/local-tool.md).

## Verification

| Focus | Cases to try |
| --- | --- |
| Help and environment | Fresh installation; root and subcommand help offline; wrong project or endpoint; version identification |
| Non-interactive use | Closed stdin; missing input; spaces, quotes, and leading option characters in data; authentication handoff |
| Results and status | Machine output with warnings; structured failures; accepted remote work; truncated streams and nonzero exit |
| Interruption and composition | Lost response; client termination after remote acceptance; partial batches; multiple retry layers |

Use the [evaluation procedure](../evaluation.md) for task trials and setup costs.

## Sources and related topics

- [Command Line Interface Guidelines](https://clig.dev/): help, non-interactive operation, output, and process conventions.
- [GitHub CLI formatting](https://cli.github.com/manual/gh_help_formatting) and [API command](https://cli.github.com/manual/gh_api): concrete field selection, request construction, and pagination behavior.
- [Git status](https://git-scm.com/docs/git-status): stable porcelain output and filename framing.
- Related topics: [HTTP APIs](http-api.md), [SDKs](sdk.md), [instructions](instructions.md), and [files and artifacts](files-and-artifacts.md).
