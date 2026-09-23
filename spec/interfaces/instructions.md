# Instructions, help, and Skills

Product descriptions support [product discovery](../core.md#an-01--discover-and-understand-the-product). Instructions explain how to use a [capability access path](../interfaces.md); they do not provide access themselves. This guide applies the [core requirements](../core.md).

## Role and fit

A small tool may need only help and an example. Larger products can separate overview, reference, and methods for selective loading. Use Skills for recurring tasks that need guidance beyond parameters; implement stable mechanical sequences as programs where useful.

## Design choices

### Separate four questions

| Question | Useful information | Typical mechanism |
| --- | --- | --- |
| Which product can help? | Purpose, provider, needs served, benefits, limits, access conditions | Product page, registry, package metadata |
| How do I connect and describe the interface? | Endpoint or executable, version, authentication, contract location | Help, OpenAPI, MCP setup, API catalog |
| Which operation fits this goal? | Purpose, input, effects, results, failures | Subcommand help, operation reference, tool catalog |
| Can this action happen now? | Authority, object state, revision, required decision | Authorized context reads and operation validation |

Finding an operation in a named product is not the same as finding a product from a need. Pages and descriptions support AN-01 only through paths the intended agents can reach. A direct product link from the user starts with a known product; it does not by itself show discovery from a need.

A catalog or static contract cannot establish current authority and object state.

### Choose a document's responsibility

| Document or mechanism | Responsibility | Limit |
| --- | --- | --- |
| Product overview | Explain the product's purpose, value, limits, and routes into it | Not a discovery path by itself or a complete operation reference |
| Command help or API reference | Explain exact operations | Not every method for a user goal |
| Agent Skill | Explain when and how to perform a class of tasks, with optional resources or scripts | Does not grant access or replace validation |
| MCP prompt | Offer a reusable interaction template through a supporting host | Does not guarantee automatic selection or execution |
| `AGENTS.md` | Guide coding agents working in a repository | Not a universal remote-product discovery mechanism |
| `llms.txt` | Provide an agent-readable documentation index | Does not install tools or authenticate callers |
| API catalog | Point to available API descriptions and related information | Requires a client discovery path and support |

The [Agent Skills specification](https://agentskills.io/specification) separates discovery metadata, an activated body, and supporting resources. Make referenced scripts and dependencies available through documented paths. Test progressive loading in the claimed hosts rather than assuming identical behavior.

### One authoritative operation contract

Keep schemas and semantics in one maintained reference; guides explain choices and link to it. For large or complex structured interfaces, provide machine-readable schemas alongside semantic descriptions.

A readable Skill can still copy obsolete syntax. Identify the interface version or supported range. Check executable examples against that implementation, and label illustrative examples as such.

### Methods and authority

Methods explain preconditions, choices, result checks, and recovery while leaving room to adapt. Retrieved instructions have a source and scope; they cannot authorize a new recipient, replace the user's objective, or grant access. Programs still enforce the rules.

## Example

An illustrative [reporting service](../../examples/reporting-service.md) guide names the weekly-draft task and its limits in discovery metadata. Its body explains source selection, drafting, coverage checks, and reviewer handoff. Parameters stay in the operation reference; detailed source guidance loads only when needed. Draft preparation does not silently include publication.

An included validation script needs declared dependencies and an assessed access path. This example is not a deployable Skill package.

## Verification

| Focus | Cases to try |
| --- | --- |
| Finding and using knowledge | Start with only the normal entry point; find the right operation; large-interface schema and description agreement; outdated syntax; recoverable failure; adversarial instructions in retrieved content |
| Skills and entry documents | Skill dependency missing; unsupported host behavior; large documentation set; claimed auto-discovery; repository guidance confused with service authorization |

Measure retrieval effort and task outcome under the [evaluation procedure](../evaluation.md), not document length alone.

## Sources and related topics

- [Agent Skills specification](https://agentskills.io/specification): format, dependencies, and progressive disclosure.
- [AGENTS.md](https://agents.md/), [llms.txt](https://llmstxt.org/), and [RFC 9727](https://www.rfc-editor.org/rfc/rfc9727.html): distinct discovery and guidance mechanisms.
- [MCP prompts, 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/server/prompts): a host-mediated prompt mechanism.
- Related topics: [CLI help](cli.md), [HTTP descriptions](http-api.md), and [MCP catalogs](mcp.md).
