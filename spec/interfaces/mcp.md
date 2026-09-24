# Model Context Protocol

English | [简体中文](../../zh-CN/spec/interfaces/mcp.md)

MCP connects a client to a server's tools, resources, and prompts. This guide applies the [core requirements](../core.md); see the [interface overview](../interfaces.md).

Examples and sources use **MCP 2025-11-25**. Evaluate the revision actually supported by the application and client environment.

## Role and fit

The client must support the transport, authorization, and required capabilities. MCP does not establish global product discovery: a user, registry, administrator, or client still supplies the server entry point.

## Design choices

### Tools, resources, and prompts

| Primitive | Typical purpose | Example in a reporting service |
| --- | --- | --- |
| Tool | Perform an operation, including a bounded query | Search relevant records; revise a draft |
| Resource | Provide addressable context or content | Read a report revision or its supporting material |
| Prompt | Provide a reusable interaction template | Start a guided report-review activity |

In the reference revision, tools are model-controlled, resources are application-driven, and prompts are user-controlled design patterns. Clients may present them differently; listing a resource does not load it into the model.

Use resources for addressable, reusable context. Search can remain a tool. A [Skill](instructions.md) can teach a method across tools and resources; it is not interchangeable with a prompt.

### Tool boundaries

Adapters should preserve domain rules without exposing every storage primitive. A tool can combine work, but its description and schema need to expose input meaning, effects, and consequential choices such as publishing, billing, and notifying.

Tool annotations describe expected behavior; a catalog entry does not authorize an action on every object. Check current authority and object conditions at execution, even when the client caches the catalog.

When wrapping a CLI, use its machine format and process semantics. Do not disguise a broad shell executor as a narrow domain tool.

### Results and context cost

The reference revision supports structured results, optional output schemas, and content blocks. Follow its compatibility guidance for structured and text representations. Report domain failures through the tool-result mechanism, separately from protocol errors. Retain identifiers and use resource links for detail where retrieval is supported.

A resource URI need not be directly fetchable. A server-side `file` resource is not necessarily local to the agent. Check resource retrieval and any UI handoff in each supported client environment.

Test catalog pagination and updates; measure tool selection and context use in each client environment. Do not assume lazy discovery or full catalog injection; vague descriptions can hide capabilities even in a small catalog.

### Transport and authorization

Stdio reserves stdout for protocol messages; a logging banner can corrupt the connection. Streamable HTTP has separate request, stream, and security rules.

The reference authorization specification defines resource and authorization-server discovery for protected HTTP access. Tokens must target the receiving service; upstream calls need appropriate upstream authorization, not blind forwarding of the caller's token.

Local transport can receive credentials from the client environment. It does not grant unrestricted filesystem or network authority; enforce the applicable scope. If the client cannot complete the required access flow, provide a supported handoff instead of asking the model to carry secrets in task content.

### Connection state and continuing work

Protocol sessions, tool calls, and domain work have different lifetimes. Supported task or progress facilities can carry the AN-07 contract; they do not define it. Disconnection alone does not establish cancellation.

Give persistent objects and work explicit identifiers or documented scope that survives supported reconnection. Do not infer an action's target from unstated conversational history.

## Example

This illustrative [reporting service](../../examples/reporting-service.md) tool uses the reference revision's fields; it is not a running server.

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

The contract still needs identifier scope, URI retrieval, and error behavior. After reading the content, a later update supplies the observed revision to a separate operation.

## Verification

| Focus | Cases to try |
| --- | --- |
| Protocol and catalog | Selected revision; multi-page catalogs; schema mismatch; business versus protocol error; stdout contamination in stdio |
| Domain behavior and authorization | Incorrect authority; upstream token separation; cross-user object access; reconnected callers with explicit work identities |
| Context and client behavior | Client exposes tools but not the assumed resource path; stale catalog; unavailable UI extension; large results and limited context |

Use the [evaluation procedure](../evaluation.md), including tasks in each claimed client environment.

## Sources and related topics

- MCP 2025-11-25: [tools](https://modelcontextprotocol.io/specification/2025-11-25/server/tools), [resources](https://modelcontextprotocol.io/specification/2025-11-25/server/resources), and [prompts](https://modelcontextprotocol.io/specification/2025-11-25/server/prompts).
- The same revision's [transports](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports) and [authorization](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization).
- [Writing effective tools](https://www.anthropic.com/engineering/writing-tools-for-agents): task-based tool design and evaluation, with no universal optimal granularity.
- Related topics: [HTTP](http-api.md), [CLI](cli.md), [instructions](instructions.md), and [presentation](presentation.md).
