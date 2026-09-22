# Command-line interfaces

A CLI exposes capabilities through a process. It is often the simplest entry point for an agent with shell access and a shared filesystem. A CLI can execute locally or act as a client of a remote application.

This is an execution profile. Its requirement words and shared obligations come from the [core specification](../core.md). See the [interface overview](../interfaces.md) for selection and composition with other profiles.

## Role and fit

A caller needs the executable, a supported environment, sufficient filesystem or service access, and a way to capture output and process status. Help can be discovered on demand. Ordinary shell tools can transform inputs and results without putting every intermediate value in model context.

A hosted agent may have no shell, no installation permission, or no access to the user's local files. In that environment, a remote [HTTP](http-api.md) or [MCP](mcp.md) interface may be a more direct entry point. Installation and authentication belong in the comparison of user effort.

## Design choices

### Help, schemas, and methods

Root help explains the product and its command groups. Command help explains a specific operation, including effects and failures. A small tool can put its complete contract there. Large command families benefit from linked references or a machine-readable command description.

Help answers how to invoke an operation. A [Skill or guide](instructions.md) explains when and how to combine operations. Neither needs to duplicate parameter definitions already maintained by the command.

### Human output and script output

[GitHub CLI formatting](https://cli.github.com/manual/gh_help_formatting) lets callers select fields for supported commands with `--json` and shape results with `--jq`. [Git status](https://git-scm.com/docs/git-status) supplies a stable porcelain format and NUL-delimited paths. These illustrate two useful designs: structured records and a documented native stream. JSON is valuable when it preserves useful structure; it is not required for binary artifacts or every text result.

Choose an error convention and document it. A result envelope on stdout is easy to parse uniformly. Errors on stderr follow familiar process conventions but need separation from diagnostic logs. Either can work. Mixing a JSON record with progress text on the same channel makes both unreliable.

A stream also needs record boundaries and a final completion condition. A parseable prefix of a failed export is not necessarily a complete result. For raw filenames, newline splitting fails when a filename contains a newline; use the application's documented framing.

### Shell behavior is part of the interface

Use argument arrays when the host supports direct process invocation. When a shell is involved, quote literal data and keep executable syntax separate. Accept large or complex input through files or stdin. Document special meanings such as a leading `@`, wildcard expansion, or `--` as an option terminator.

A concrete example is [gh api](https://cli.github.com/manual/gh_api): adding field flags changes its default HTTP method from GET to POST. A caller intending a query must select the method explicitly. This is a documented product behavior, not a convention to assume for other CLIs.

Authentication, project selection, environment variables, working directory, and exit status can all affect an otherwise identical command. Expose relevant context without displaying secrets.

### Local exit and remote effects

The process may exit after submitting work that continues remotely. Killing the client may only end observation. A pipe consumer can also terminate before the producer finishes. The application needs an outcome and recovery contract independent of whether the terminal printed its last line.

A CLI built on an SDK should identify which layer owns retries. An outer retry loop can multiply the SDK's attempts or create a new logical operation with a new deduplication key. See [SDK effects and lifecycle](sdk.md).

## Requirements

### CLI-01 — Help and environment

The CLI MUST support `--help` at the root and relevant subcommands without performing business effects. Help MUST explain purpose, required inputs, defaults, output, examples, and how to obtain further detail. It MUST provide a way to identify the CLI version and, for remote clients, the target service and relevant active scope without revealing credentials.

Installation guidance MUST name supported environments and required dependencies. Basic local help SHOULD work without network access or authentication.

A small tool MAY describe its full contract in help. A large tool SHOULD provide machine-readable descriptions or linked reference documents. This profile does not define a universal `schema` command.

### CLI-02 — Non-interactive use

The CLI MUST accept business inputs through arguments, flags, files, or standard input. It MUST offer a non-interactive mode and MUST NOT wait indefinitely for a hidden prompt in that mode. Missing input MUST produce an actionable error or an explicit human handoff.

Authentication or a reserved human decision MAY use a browser or separate flow. The CLI MUST explain how the caller learns that the handoff is complete. Non-interactive mode MUST NOT bypass access policy.

Complex content SHOULD be accepted through a file or standard input to avoid fragile shell quoting. Credentials MUST NOT require ordinary command-line arguments where they can leak through process listings or history.

### CLI-03 — Results and process status

The CLI MUST separate documented results from progress and diagnostics. A machine-output mode MUST exclude terminal decorations and incidental prose from its result channel. Structured outcomes SHOULD use JSON or another documented parseable format; native file or text output MAY remain in its native format.

The CLI MUST document where errors appear and their machine-readable format when provided. A consumer MUST be able to distinguish an error record from diagnostic logs. This profile permits either a documented error envelope on stdout or a documented error channel on stderr.

Process success MUST use exit status zero; failure MUST use a nonzero status. Success MUST refer to the command's stated contract. A successful submission MUST still report that the underlying work is only accepted, with its work identity and status path.

A streamed result MUST document record boundaries and how to distinguish a complete result from partial output followed by failure.

### CLI-04 — Interruption and composition

For commands with effects, the CLI MUST document what termination or interruption does to the underlying operation, including remote work that continues after the process exits. It MUST expose the core recovery and repetition contract.

Outputs SHOULD preserve references needed by the next command. Scripts MUST be able to use the documented result format without parsing visual tables or localized messages. Bulk operations MUST declare whether their effects are atomic or item-specific.

## Example

These are read-only commands for an installed and authenticated GitHub CLI with network access. The repository and fields are explicit; the result is live data rather than a fixed expected value.

```sh
gh repo view cli/cli --json nameWithOwner,defaultBranchRef
```

The lower-level client can request the same information through HTTP and shape it to the same record:

```sh
gh api --method GET repos/cli/cli --jq '{nameWithOwner: .full_name, defaultBranchRef: {name: .default_branch}}'
```

The first command hides endpoint and field mapping. The second gives more protocol control. Both use the same remote product through a CLI. Neither demonstrates that all CLI operations have a structured equivalent or that one interface is always faster.

The [local tool example](../../examples/local-tool.md) shows a fully local product and an interruption boundary.

## Verification

| Requirement | Important cases |
| --- | --- |
| CLI-01 | Fresh installation; root and subcommand help offline; wrong project or endpoint; version identification |
| CLI-02 | Closed stdin; missing input; spaces, quotes, and leading option characters in data; authentication handoff |
| CLI-03 | Machine output with warnings; structured failures; accepted remote work; truncated streams and nonzero exit |
| CLI-04 | Lost response; client termination after remote acceptance; partial batches; multiple retry layers |

Use the [evaluation procedure](../evaluation.md) to test real tasks. Include the cost of installation and discovery separately from repeated use.

## Sources and related topics

- [Command Line Interface Guidelines](https://clig.dev/): help, non-interactive operation, output, and process conventions.
- [GitHub CLI formatting](https://cli.github.com/manual/gh_help_formatting) and [API command](https://cli.github.com/manual/gh_api): concrete field selection, request construction, and pagination behavior.
- [Git status](https://git-scm.com/docs/git-status): stable porcelain output and filename framing.
- Related profiles: [HTTP APIs](http-api.md), [SDKs](sdk.md), [instructions](instructions.md), and [files](files.md).
