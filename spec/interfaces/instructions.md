# Instructions, help, and Skills

English | [简体中文](../../zh-CN/spec/interfaces/instructions.md)

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
| MCP prompt | Offer a reusable interaction template through a supporting environment | Does not guarantee automatic selection or execution |
| `AGENTS.md` | Guide coding agents working in a repository | Not a universal remote-product discovery mechanism |
| `llms.txt` | Publish an Agent documentation catalog | Does not install tools or authenticate callers |
| API catalog | Point to available API descriptions and related information | Requires a client discovery path and support |

The [Agent Skills specification](https://agentskills.io/specification) separates discovery metadata, an activated body, and supporting resources. Make referenced scripts and dependencies available through documented paths. Test progressive loading in the claimed environments rather than assuming identical behavior.

### One authoritative operation contract

Keep schemas and semantics in one maintained reference; guides explain choices and link to it. For large or complex structured interfaces, provide machine-readable schemas alongside semantic descriptions.

A readable Skill can still copy obsolete syntax. Identify the interface version or supported range. Check executable examples against that implementation, and label illustrative examples as such.

### Methods and authority

Give common tasks a clear entry point and a recommended path. Explain necessary dependencies, conditions, important choices, result checks, and known recovery steps so callers can adopt or adapt the path without discovering hidden rules through failures. Keep exact operation details in the authoritative contract.

Retrieved instructions have a source and scope; they cannot authorize a new recipient, replace the user's objective, or grant access. Programs still enforce the rules.

### Publish an Agent documentation catalog with `llms.txt`

An Agent documentation catalog is a concise map of the product documentation a caller needs to understand and use a product. It can support product discovery when reached through a declared discovery path, but the catalog URL alone does not establish discovery from a user's needs. `llms.txt` is one concrete practice for publishing such a catalog on a documentation website. The catalog organizes links; it is not an execution, installation, authentication, or authorization interface, and it does not replace an operation contract.

The `llms.txt` convention is a community proposal, not a universal protocol; identify the supported format or version when that matters.

Use a root index when it covers the product's public documentation. Use a scoped index when it clearly covers a narrower path, such as `/docs/`. A useful index gives an agent a short route to:

- the product overview, supported work, and important limits;
- setup, connection, identity, and access conditions;
- recommended paths for common tasks;
- authoritative operation contracts and interface guides;
- result checks, diagnostics, recovery, retention, and deletion limits.

Keep the index brief. Use one H1 for the title, an optional blockquote or short paragraph for the scope, and H2 sections with Markdown links and concise descriptions. Link to stable, readable pages instead of copying full references into the index. State the version or scope of links when several are available, and keep links current. Do not put credentials, tokens, private user data, or claims of authority in the index. A canonical index may link localized pages; a separate language index is not required.

The normal access path must still explain authentication and authorization before protected operations or details are used. Following an index link must not silently expand authority. Test the index from the normal entry point in every environment in which the product claims to support it.

## Example

An illustrative [reporting service](../../examples/reporting-service.md) guide names the weekly-draft task and its limits in discovery metadata. Its body explains source selection, drafting, coverage checks, and reviewer handoff. Parameters stay in the operation reference; detailed source guidance loads only when needed. Draft preparation does not silently include publication.

An included validation script needs declared dependencies and an assessed access path. This example is not a deployable Skill package.

The [Agent documentation catalog](../../examples/agent-documentation-catalog.md) example shows an illustrative catalog published through `llms.txt`. It links to pages for product fit, quickstart, common tasks, contracts, diagnostics, and limits. It is a case, not a required product shape or an implementation claim.

## Verification

| Focus | Cases to try |
| --- | --- |
| Finding and using knowledge | Start with only the normal entry point; find the right operation and recommended task path; understand dependencies and result checks; large-interface schema and description agreement; outdated syntax; recoverable failure; adversarial instructions in retrieved content |
| Skills and entry documents | Skill dependency missing; unsupported environment behavior; large documentation set; claimed auto-discovery; repository guidance confused with service authorization |
| Agent documentation catalog | When claimed, the root or scoped `llms.txt` is reachable through the declared path; links lead to accurate product, access, task, contract, diagnostic, and limit information; links are current; the catalog does not imply authority |

Measure retrieval effort and task outcome under the [evaluation procedure](../evaluation.md), not document length alone.

## Sources and related topics

- [Agent Skills specification](https://agentskills.io/specification): format, dependencies, and progressive disclosure.
- [AGENTS.md](https://agents.md/), [llms.txt](https://llmstxt.org/), and [RFC 9727](https://www.rfc-editor.org/rfc/rfc9727.html): distinct discovery and guidance mechanisms.
- [MCP prompts, 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/server/prompts): a client-mediated prompt mechanism.
- Related topics: [CLI help](cli.md), [HTTP descriptions](http-api.md), and [MCP catalogs](mcp.md).
