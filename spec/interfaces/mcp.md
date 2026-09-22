# Model Context Protocol

MCP lets a supporting host discover and use capabilities exposed by a server. It supplies protocol mechanisms for tools, resources, and prompts. An application still owns the meaning and effects of its operations.

This is an execution profile governed by the [core specification](../core.md). The [interface overview](../interfaces.md) explains its relation to CLI and HTTP. Protocol examples and source links in this topic use **MCP 2025-11-25** as an explicit reference revision. Applications may support other revisions; evaluate their actual contracts rather than extrapolate these examples to every version.

## Role and fit

MCP is useful when the intended hosts can establish its transport, authenticate, discover the required capabilities, and expose them to the agent or user. It reduces the need for a different integration mechanism for every application.

It does not establish global product discovery. A user, registry, administrator, or host still supplies a path to the server. A known server's tools also do not establish that the current user can perform every action on every object.

## Design choices

### Tools, resources, and prompts

| Primitive | Typical purpose | Example in a reporting service |
| --- | --- | --- |
| Tool | Perform an operation, including a bounded query | Search relevant records; revise a draft |
| Resource | Provide addressable context or content | Read a report revision or its supporting material |
| Prompt | Provide a reusable interaction template | Start a guided report-review activity |

In the reference revision, tools are model-controlled, resources are application-driven, and prompts are user-controlled design patterns. The protocol allows hosts to present them in different ways. A server that lists resources cannot assume the host automatically loads them into the model.

Resources are useful when identity, reuse, and focused retrieval matter. Search can still be a tool. A [Skill](instructions.md) can teach a longer method using several tools and resources; it is not interchangeable with every MCP prompt.

### Tool boundaries

A thin adapter around an existing API can preserve mature domain rules and reduce duplicate implementation. It still needs review of naming, parameter meaning, result size, and useful granularity. Automatically exposing hundreds of storage operations can move domain assembly and validation burdens to the caller.

A task-oriented tool can collect related context or carry out a complete domain action. Keep meaningful decisions visible. A tool that publishes, bills, and notifies as one action needs that combined effect in its contract.

Calling an existing CLI from a server can be reasonable when the CLI owns the domain behavior. Use its documented machine format and process semantics. Avoid hiding a broad shell executor behind a narrow-sounding tool name: the declared capability should match the actual authority and effects.

### Results and context cost

The reference revision supports structured tool results with optional output schemas and also text or other content blocks. Follow its compatibility guidance for structured and text representations. Preserve identifiers needed for the next step and use resource links for substantial detail when the host can actually retrieve them.

A resource URI is not necessarily a URL the host can fetch directly. In particular, a server-side `file` resource is not automatically a local file in the agent's environment. State the retrieval path and test it in the claimed hosts.

Catalog pagination, caching, and host tool selection affect cost. A large catalog need not be injected into every model request, but the server cannot assume every host has lazy discovery. Conversely, a compact catalog can conceal useful capabilities if its descriptions are vague. Measure the actual host behavior.

### Transport and authorization

The reference revision defines stdio and Streamable HTTP. Stdio reserves stdout for protocol messages; a logging banner can corrupt the connection. Streamable HTTP has its own request, stream, and security requirements. A remote MCP server is not just an arbitrary REST endpoint with renamed methods.

For protected HTTP access, the reference authorization specification defines resource and authorization-server discovery. Tokens need to be intended for the receiving service. When the server calls an upstream API, it uses the appropriate separately obtained upstream authorization, rather than blindly forwarding the caller's token.

Local transport can receive credentials from the host environment. "Local" does not imply unrestricted filesystem or network authority. The host and application must still enforce the applicable scope.

### Connection state and continuing work

A protocol session, a tool call, and a domain task are different things. Their lifetimes vary by revision and implementation. Durable work needs an explicit application identity and recovery contract under AN-07.

If a selected revision and host support task or progress facilities, they can carry that contract. They do not by themselves establish business completion, recovery, or cancellation of already committed effects. A transport disconnection alone does not establish cancellation.

## Requirements

### MCP-01 — Declared protocol and discoverable capabilities

The server MUST identify and follow its supported MCP revision and negotiate capabilities as required by that revision. Tools and resources needed for the assessed work MUST be discoverable through the protocol or its documented handoffs.

Tool descriptions and input schemas MUST express the operation's semantics. Where structured results are returned, the server SHOULD publish an output schema supported by the selected protocol revision. Domain execution errors MUST be reported through that revision's tool-result mechanism, distinct from protocol errors.

Servers MUST follow the selected transport's message framing and output rules. Descriptive logging MUST NOT corrupt the protocol channel.

### MCP-02 — Domain behavior and authorization

MCP exposure MUST preserve the core contracts. Tool annotations are hints and MUST NOT replace authority checks. A tool list is a catalog, not proof that every listed action is permitted on every object.

A protected HTTP transport MUST document its authorization method and SHOULD use the applicable MCP authorization specification. Local transports MUST document how the host supplies access safely. The server MUST NOT ask the model to place secrets in task content to work around host limitations.

Persistent domain state MUST have explicit identifiers or another documented scope that remains valid across the supported connection lifecycle. A server MUST NOT rely on unstated conversational memory to resolve the target of an action.

### MCP-03 — Context and host behavior

The server SHOULD keep tool catalogs and results focused, with documented ways to retrieve detail. It MUST NOT claim that all hosts discover, load, or render every advertised capability automatically.

For every assessed host, the application MUST test the required tools, resource access, authorization, and handoffs. If a UI extension is offered, its support and the usable path on hosts without it MUST be documented.

The tested contract MUST include catalog pagination and update behavior where used. Cached discovery information MUST NOT substitute for checking current authority and object conditions at execution.

## Example

This is an illustrative tool definition for the [reporting service](../../examples/reporting-service.md), using the reference revision's fields. It is not a running server or evidence of protocol conformance.

```json
{
  "name": "read_report",
  "description": "Read the current draft of an authorized report. Returns its revision and content reference. Does not publish or modify it.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "report_id": { "type": "string" }
    },
    "required": ["report_id"],
    "additionalProperties": false
  },
  "outputSchema": {
    "type": "object",
    "properties": {
      "report_id": { "type": "string" },
      "revision": { "type": "string" },
      "content_uri": { "type": "string" }
    },
    "required": ["report_id", "revision", "content_uri"]
  }
}
```

The server still defines the identifier's scope, the URI retrieval method, and the error behavior in its contract. The host discovers this tool, calls it, and retrieves the referenced content through a supported path. A later update supplies the relevant revision to a separate domain operation. Adding a read-only annotation would help a trusted host describe risk; it would not enforce read-only behavior.

## Verification

| Requirement | Important cases |
| --- | --- |
| MCP-01 | Selected revision; multi-page catalogs; schema mismatch; business versus protocol error; stdout contamination in stdio |
| MCP-02 | Incorrect authority; upstream token separation; cross-user object access; reconnected callers with explicit work identities |
| MCP-03 | Host exposes tools but not the assumed resource path; stale catalog; unavailable UI extension; large results and limited context |

Use the [evaluation procedure](../evaluation.md), including tasks in each claimed host. Syntax-valid example JSON is not a protocol or host compatibility test.

## Sources and related topics

- MCP 2025-11-25: [tools](https://modelcontextprotocol.io/specification/2025-11-25/server/tools), [resources](https://modelcontextprotocol.io/specification/2025-11-25/server/resources), and [prompts](https://modelcontextprotocol.io/specification/2025-11-25/server/prompts).
- The same revision's [transports](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports) and [authorization](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization).
- [Writing effective tools](https://www.anthropic.com/engineering/writing-tools-for-agents): task-based tool design and evaluation, with no universal optimal granularity.
- Related profiles: [HTTP](http-api.md), [CLI](cli.md), [instructions](instructions.md), and [presentation](presentation.md).
