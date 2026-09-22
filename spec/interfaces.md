# Interface profiles

These profiles map the [core specification](core.md) to concrete interfaces. The requirement words have the same meaning as in the core. Profile requirements are normative when that profile is selected for an assessment.

An application MUST identify at least one execution profile: CLI, HTTP, MCP, SDK, or files. It MAY select several. Instructions and presentation are supporting profiles; they do not alone establish an execution path. A continuing-work service uses an execution profile plus AN-07.

A selected profile must cover the assessed outcomes through its documented paths. Handoffs to another declared interface are permitted. They must preserve authority, state, and relevant context and must be included in evaluation. Listing many interfaces does not compensate for missing behavior.

## Different jobs, different mechanisms

| Mechanism | Job | What it does not establish by itself |
| --- | --- | --- |
| CLI | Invoke a process with inputs and receive outputs | Global product discovery or remote authorization |
| Command help | Explain commands and their use | A complete machine schema or enforcement of rules |
| HTTP API | Invoke remote operations | Automatic adaptation to every agent host |
| OpenAPI | Describe HTTP operations and data | Complete domain meaning or reliable execution |
| MCP | Standardize discovery and use within a connected host-server relationship | Global product search or domain correctness |
| SDK | Expose functions and types in a programming environment | Runtime validation or installation in every host |
| Files | Exchange durable content and structured data | Automatic application of edits or safe concurrent writes |
| Skill | Explain methods and supply optional resources or scripts | Permission to act or guarantees about effects |
| Human view | Support inspection, editing, and decisions | A separate authority over application facts |

Choose a useful supported combination. An application can expose the same operation through a CLI, HTTP, and MCP without copying its business rules into three implementations.

## CLI profile

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

### CLI-04 — Interruption and composition

For commands with effects, the CLI MUST document what termination or interruption does to the underlying operation, including remote work that continues after the process exits. It MUST expose the core recovery and repetition contract.

Outputs SHOULD preserve references needed by the next command. Scripts MUST be able to use the documented result format without parsing visual tables or localized messages. Bulk operations MUST declare whether their effects are atomic or item-specific.

## HTTP profile

### HTTP-01 — Description and access

The service MUST publish an interface description for the assessed operations. It SHOULD use OpenAPI with semantic descriptions and examples. An alternative machine-readable description needs a documented reason and a usable client path.

The entry point MUST identify the API address, supported version, authentication requirements, and documentation. Access to protected details MAY require authorization. A public entry page need only explain the access process.

HTTP clients MUST use the service's documented credential mechanism. Authentication and authorization failures MUST be distinguishable. Credentials MUST NOT be embedded in ordinary resource URLs.

### HTTP-02 — Requests and responses

The API MUST validate inputs and document success and failure response structures. It MUST use HTTP status semantics consistently. Domain failures MUST provide enough structured or native-format detail for recovery without relying only on a status number.

Collections MUST document ordering, pagination or bounds, and consistency where these affect correct use. Resource references MUST have a defined scope. Large artifacts SHOULD have a separate retrieval path rather than require inclusion in every response.

### HTTP-03 — Effects and continuing work

Mutating requests MUST satisfy AN-06. The service MUST NOT imply exactly-once execution merely because it accepts an idempotency key. It MUST specify the actual deduplication guarantee.

Asynchronous acceptance MUST provide a work or operation reference and a status path. If a stream or webhook is offered, the service MUST define authorization, delivery, reconnection or refresh, and ordering or deduplication where relevant. A broken stream MUST NOT silently determine the business outcome.

A resource revision or equivalent condition SHOULD protect writes based on previously read state. An approval of a specific revision MUST be checked at execution.

## MCP profile

### MCP-01 — Declared protocol and discoverable capabilities

The server MUST identify and follow its supported MCP revision and negotiate capabilities as required by that revision. Tools and resources needed for the assessed work MUST be discoverable through the protocol or its documented handoffs.

Tool descriptions and input schemas MUST express the operation's semantics. Where structured results are returned, the server SHOULD publish an output schema supported by the selected protocol revision. Domain execution errors MUST be reported through that revision's tool-result mechanism, distinct from protocol errors.

### MCP-02 — Domain behavior and authorization

MCP exposure MUST preserve the core contracts. Tool annotations are hints and MUST NOT replace authority checks. A tool list is a catalog, not proof that every listed action is permitted on every object.

A protected HTTP transport MUST document its authorization method and SHOULD use the applicable MCP authorization specification. Local transports MUST document how the host supplies access safely. The server MUST NOT ask the model to place secrets in task content to work around host limitations.

Persistent domain state MUST have explicit identifiers or another documented scope that remains valid across the supported connection lifecycle. A server MUST NOT rely on unstated conversational memory to resolve the target of an action.

### MCP-03 — Context and host behavior

The server SHOULD keep tool catalogs and results focused, with documented ways to retrieve detail. It MUST NOT claim that all hosts discover, load, or render every advertised capability automatically.

For every assessed host, the application MUST test the required tools, resource access, authorization, and handoffs. If a UI extension is offered, its support and the usable path on hosts without it MUST be documented.

## SDK profile

### SDK-01 — Callable contract

The SDK MUST document supported languages, runtimes, versions, initialization, and access requirements. Public operations MUST have documented parameters, effects, results, and errors. Types SHOULD describe these contracts where the language supports them.

Runtime validation MUST enforce the relevant rules even if callers bypass type checking. The SDK MUST document which work runs locally and which invokes a service. Host code-execution support MUST be stated as an environment requirement.

### SDK-02 — Effects and lifecycle

The SDK MUST preserve the underlying service's authority, retry, and conflict contracts. Automatic retries MUST be limited to operations and conditions for which they are safe, with a bounded policy. Cancellation, timeouts, streaming, and cleanup MUST have documented meanings where offered.

## File profile

### FILE-01 — Format and meaning

The application MUST document file formats, paths or discovery rules, required fields, ownership, and the operation that makes an edit effective. It MUST define whether a file is authoritative state, a draft, an import, or an export.

Structured inputs MUST be validated before producing effects. Invalid content MUST yield a useful failure rather than silent partial interpretation. A native content format MAY carry its own syntax instead of a new JSON wrapper.

### FILE-02 — Change and access

For shared mutable files, the application MUST declare and enforce a conflict policy. It MUST describe the effect of incomplete writes or interrupted imports. An application MUST NOT expose direct file or database writes as a way to bypass invariants required by other interfaces.

References to files MUST be meaningful in the caller's environment, or provide an authorized transfer path. A local path on a remote server alone is not a usable artifact reference for a remote caller.

## Instructions profile

### DOC-01 — Find, learn, and apply

The application MUST separate product overview, operation reference, and typical methods sufficiently for a caller to find relevant material without reading everything. One small document MAY serve all three purposes.

Instructions MUST name the interface and version they describe and link to the authoritative contract. Repeated parameter tables SHOULD be generated or replaced by links to avoid drift. Examples presented as executable MUST be checked against that implementation. Illustrative examples MUST be labeled as such.

### DOC-02 — Skills and entry documents

When distributing an Agent Skill, the application SHOULD use the published Agent Skills format and progressive disclosure. Dependencies and referenced scripts MUST be available through documented paths. Skill instructions MUST NOT claim to grant permissions or override host policy.

A Markdown entry page or `llms.txt` MAY guide documentation discovery. An `AGENTS.md` file can guide work in a repository. Neither establishes universal remote tool discovery. A product-specific `agent.md` convention MUST state which clients recognize it, if any.

Existing API catalog mechanisms, such as RFC 9727, SHOULD be considered before inventing a discovery protocol. Discovery still depends on client support and registration or retrieval paths.

## Presentation profile

### UI-01 — Shared facts and human actions

Views MUST identify the relevant work, object, or revision. Displayed claims about business facts MUST be grounded in the application's data. Human actions MUST enforce the appropriate authority and domain rules and make relevant changes available to later agent work.

A view MUST distinguish a proposed action from one already executed. A decision affecting a specific result MUST bind to that result or revision as required by AN-04.

### UI-02 — Delivery and access

Views MAY be standalone, linked, or embedded. The application MUST state host requirements, access conditions, and any expiry. A host-specific rendering feature MUST NOT silently remove the assessed core outcome on another host claimed as supported; provide a documented handoff or narrow the supported-host claim.

An application using MCP Apps or another UI protocol MUST follow its sandbox and communication requirements for the supported version. Credentials and application authority MUST remain protected at the operation boundary.

## No mandatory new protocol

This project defines behavioral requirements and interface profiles. It does not define a universal agent manifest, new tool schema, or common wire protocol. Use existing standards where they fit. Add a new convention only when a concrete use case and interoperability evidence justify it.

See [References](../docs/references.md) for the sources behind these profiles and [Evaluation](evaluation.md) for the checks they require.
