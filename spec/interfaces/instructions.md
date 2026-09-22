# Instructions, help, and Skills

Instructions help a caller discover a product, understand its contracts, and apply useful methods. Their organization is part of the product interface: readers need a reliable route from an unfamiliar goal to the relevant operation.

This is a supporting profile governed by the [core specification](../core.md). Instructions explain how to use a documented [capability access path](../interfaces.md); they do not supply that access by themselves.

## Role and fit

A short local tool may need only command help and an example. A broad service may need an overview, a capability index, detailed references, and optional task guides. The structure should let an agent retrieve the next useful piece without loading everything.

A Skill is useful when a recurring task requires domain knowledge, a method, or supporting resources beyond the operation's parameter description. Stable mechanical sequences can be implemented as programs or domain operations instead of asking a model to reconstruct them every time.

## Design choices

### Separate four questions

| Question | Useful information | Typical mechanism |
| --- | --- | --- |
| Which product can help? | Purpose, provider, supported work, access conditions | Product page, registry, package metadata, user link |
| How do I connect and describe the interface? | Endpoint or executable, version, authentication, contract location | Help, OpenAPI, MCP setup, API catalog |
| Which operation fits this goal? | Purpose, input, effects, results, failures | Subcommand help, operation reference, tool catalog |
| Can this action happen now? | Authority, object state, revision, required decision | Authorized context reads and operation validation |

A directory listing cannot answer all four. Likewise, a static contract cannot promise that a previously authorized operation remains valid after an object changes.

### Choose a document's responsibility

| Document or mechanism | Responsibility | Limit |
| --- | --- | --- |
| Product overview | Explain the product and routes into it | Not a complete operation reference |
| Command help or API reference | Explain exact operations | Not every method for a user goal |
| Agent Skill | Explain when and how to perform a class of tasks, with optional resources or scripts | Does not grant access or replace validation |
| MCP prompt | Offer a reusable interaction template through a supporting host | Does not guarantee automatic selection or execution |
| `AGENTS.md` | Guide coding agents working in a repository | Not a universal remote-product discovery mechanism |
| `llms.txt` | Provide an agent-readable documentation index | Does not install tools or authenticate callers |
| API catalog | Point to available API descriptions and related information | Requires a client discovery path and support |

The [Agent Skills specification](https://agentskills.io/specification) uses a small discovery description, an activated body, and supporting resources loaded as needed. Its format and experimental metadata do not establish that every host behaves identically. Evaluate the hosts claimed by the product.

The [AGENTS.md convention](https://agents.md/) supplies repository guidance. The [llms.txt proposal](https://llmstxt.org/) supplies a documentation entry point. [RFC 9727](https://www.rfc-editor.org/rfc/rfc9727.html) supplies an API catalog mechanism. Select them for their actual responsibilities rather than treating filenames as interchangeable manifest standards.

### One authoritative operation contract

Keep an operation's schema and semantic contract in one maintained location. A tutorial can explain the choice and link to that reference. Generate repeated reference material where useful, and check executable examples against the supported implementation.

A Skill that copies an old command syntax can remain readable while becoming wrong. Version references, dependency declarations, and checked examples make this failure visible. A document's ability to fit in context does not establish its accuracy.

### Methods and authority

A good method describes the goal, relevant preconditions, useful sequence, decision points, result checks, and recoverable failures. It should let the agent adapt within the user's authority rather than mistake one example sequence for the only valid workflow.

Treat retrieved content as information with a source and scope. A document or returned web page cannot authorize a new recipient, change the user's objective, or grant additional credentials merely by instructing the agent to do so. Program boundaries continue to enforce the applicable rules.

## Requirements

### DOC-01 — Find, learn, and apply

The application MUST separate product overview, operation reference, and typical methods sufficiently for a caller to find relevant material without reading everything. One small document MAY serve all three purposes.

Instructions MUST identify the interface and version or supported version range they describe and link to the authoritative contract. Repeated parameter tables SHOULD be generated or replaced by links to avoid drift. Examples presented as executable MUST be checked against that implementation. Illustrative examples MUST be labeled as such.

A task guide SHOULD explain relevant failure and result-checking paths, including points that need a human decision. Instructions MUST NOT silently substitute their own goals or access grants for the user's task and authority.

### DOC-02 — Skills and entry documents

When distributing an Agent Skill, the application SHOULD use the published Agent Skills format and progressive disclosure. Dependencies and referenced scripts MUST be available through documented paths. Skill instructions MUST NOT claim to grant permissions or override host policy.

A Markdown entry page or `llms.txt` MAY guide documentation discovery. An `AGENTS.md` file can guide work in a repository. Neither establishes universal remote tool discovery. A product-specific `agent.md` convention MUST state which clients recognize it, if any.

Existing API catalog mechanisms, such as RFC 9727, SHOULD be considered before inventing a discovery protocol. Discovery still depends on client support and registration or retrieval paths.

## Example

This is a design example for the [reporting service](../../examples/reporting-service.md), not a deployable Skill package.

The product entry says that the service turns authorized customer records into reviewable reports. It points to supported access methods and a guide for preparing a weekly draft.

The guide's discovery description names that task and its limits. Its body explains how to select source scope, prepare a draft, inspect source coverage, and hand the result to a person for review. Exact parameters remain in the operation reference. Publication is a separately authorized action; it is not silently added to every report-preparation task.

Detailed source-selection guidance is loaded only when relevant. An optional script that validates exported content declares its runtime and input contract. If the script itself is an execution interface in the assessment, assess the corresponding CLI or SDK profile as well.

## Verification

| Requirement | Important cases |
| --- | --- |
| DOC-01 | Start with only the normal entry point; find the right operation; outdated syntax; recoverable failure; adversarial instructions in retrieved content |
| DOC-02 | Skill dependency missing; unsupported host behavior; large documentation set; claimed auto-discovery; repository guidance confused with service authorization |

Measure irrelevant material loaded, repeated lookups, wrong-operation selection, and task outcome. A shorter guide is an improvement only if it preserves enough information for successful use. Follow the [evaluation procedure](../evaluation.md).

## Sources and related topics

- [Agent Skills specification](https://agentskills.io/specification): format, dependencies, and progressive disclosure.
- [AGENTS.md](https://agents.md/), [llms.txt](https://llmstxt.org/), and [RFC 9727](https://www.rfc-editor.org/rfc/rfc9727.html): distinct discovery and guidance mechanisms.
- [MCP prompts, 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/server/prompts): a host-mediated prompt mechanism.
- Related profiles: [CLI help](cli.md), [HTTP descriptions](http-api.md), and [MCP catalogs](mcp.md).
