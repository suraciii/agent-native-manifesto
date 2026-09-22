# Interface profiles

An interface should let the intended agent use a domain capability with clear inputs, effects, results, and recovery behavior. CLI, HTTP, and MCP operate at different boundaries and can be combined. A client library, document format, or human view can complete the same use path.

These profiles map the [core specification](core.md) to concrete interfaces. The requirement words have the same meaning as in the core. Each topic contains its role, design choices, normative requirements, examples, verification cases, and primary sources. The topic document owns its requirements; this overview owns selection and composition.

## Select the assessed profiles

An application MUST identify at least one execution profile: CLI, HTTP, MCP, SDK, or files. It MAY select several. Instructions and presentation are supporting profiles; they do not alone establish an execution path. A continuing-work service uses an execution profile plus AN-07.

A selected profile must cover the assessed outcomes through its documented paths. Handoffs to another declared interface are permitted. They must preserve authority, state, and relevant context and must be included in evaluation. Listing many interfaces does not compensate for missing behavior.

These are the execution profiles defined by this draft, not a claim that all software interfaces fit one universal wire format. An additional mechanism needs an explicit behavioral mapping and assessment scope before a conformance claim can rely on it.

| Topic | Primary boundary | Read it to decide |
| --- | --- | --- |
| [CLI](interfaces/cli.md) | Host to process | How help, arguments, output, and process status support an agent with shell access |
| [HTTP API](interfaces/http-api.md) | Client to remote service | How descriptions, authorization, responses, conflicts, and persistent operations work |
| [MCP](interfaces/mcp.md) | Supporting host to MCP server | How tools, resources, prompts, transport, and host behavior fit together |
| [SDK](interfaces/sdk.md) | Program to library | When typed composition helps and how hidden I/O and retries affect the contract |
| [Files](interfaces/files.md) | Caller content to application state | When edits take effect and how format, ownership, storage, and conflicts are handled |
| [Instructions](interfaces/instructions.md) | Product knowledge to caller | What help, Skills, API catalogs, and repository guidance each contribute |
| [Presentation](interfaces/presentation.md) | Application facts to human participation | How views, edits, decisions, and agent work remain connected |

## Understand the different responsibilities

A CLI executes operations through a process; `--help` describes their use. An HTTP API accepts network requests; OpenAPI describes its operations. MCP supplies discovery and invocation mechanisms inside a connected host-server relationship. A Skill explains a method that uses available capabilities.

These mechanisms do not compete on one axis. A CLI can call HTTP, an MCP server can use an SDK, and a Skill can guide either. A graphical view can present the same work without owning another set of business rules.

Discovering a product, finding its interface description, selecting an operation, and checking whether an action is currently permitted are separate questions. The [instructions topic](interfaces/instructions.md) maps each question to useful mechanisms. A schema or catalog cannot replace validation of the current object and authority.

## Choose the smallest useful combination

Start with the [application model](../docs/application-model.md) and a concrete user outcome.

1. **Identify the actual host environment.** Can it run a process, install a package, call authenticated HTTP, connect to MCP, read shared files, or render an interactive view?
2. **Find the boundary that already owns the capability.** Reuse established domain operations. Add an adapter when it removes real caller work or makes the capability available to an intended host.
3. **Complete the use path.** Include installation or connection, relevant context, authorization, result inspection, correction, and any human handoff.
4. **Add another interface only for a supported use.** A local tool need not gain a server merely to offer a protocol. A remote service need not force a shell installation on users whose host can connect directly.
5. **Evaluate the whole combination.** A well-described operation can still be unusable if the host cannot follow its artifact references or complete its authorization flow.

Two implementation approaches commonly fit:

| Approach | Benefit | Failure to guard against |
| --- | --- | --- |
| Expose an existing domain API through a small adapter | Reuse tested behavior and keep one place for rules | Preserve semantics and provide usable tool names, parameters, and results rather than blindly copy every internal endpoint |
| Build a focused domain operation used by several entry points | Hide repeated multi-step work behind one responsibility | Do not hide consequential choices or create a second implementation of the same rules in each entry point |

Neither approach requires a universal internal service layer. A small application can implement its domain boundary in one process.

## Preserve one meaning across interfaces

The [reporting service example](../examples/reporting-service.md) can offer the same work through several mappings. This table is illustrative, not an endpoint or command specification.

| Domain meaning | CLI mapping | HTTP mapping | MCP mapping |
| --- | --- | --- | --- |
| Read an identified draft | A command returns content or a reference and revision | Retrieve the resource and its revision | A read tool or resource supplies the same facts |
| Update the observed revision | A command accepts the expected revision | A conditional request or documented revision condition | Tool input includes the relevant revision condition |
| Accept continuing work | Command success reports acceptance and work identity | An acceptance response supplies a status reference | Tool result identifies the accepted work |
| Retrieve an artifact | A usable file or authorized retrieval reference | A representation or authorized artifact endpoint | Content or a resource reference retrievable by the host |

The mappings need not have identical syntax or expose identical low-level controls. They must preserve the assessed outcome, authority, domain invariants, and material facts. A richer view may support direct editing while a CLI supports replacement of a complete draft.

Place policy where it can be enforced. The application owns its effects, conflicts, and deduplication guarantees. A client owns its request policy within those guarantees. A host owns its agent and rendering policy. A document explains these boundaries; it does not replace them.

## Compare through use

Claims that one interface always uses fewer tokens, is safer, or is faster need task and host evidence. Cost depends on the whole path:

- **First use:** installation, authentication, catalog or help discovery, and required instructions.
- **Repeated use:** cached descriptions, connection reuse, process startup, field selection, and programmatic composition.
- **Data handling:** pagination, local transformation, large artifacts, and what actually enters model context.
- **Failure and correction:** retries, partial results, resumption, and human intervention.
- **Maintenance:** contract drift, adapters, supported versions, and host-specific integration work.

For a comparison, use equivalent tasks, authority, data, and result checks. Record interface versions and actual calls, including SDK retries and automatic pagination. Separate intended human review from intervention needed to repair a failed integration. The [evaluation procedure](evaluation.md) defines the evidence to report.

This repository provides design analysis and specifications. It does not publish an empirical performance ranking of these interfaces.

## No mandatory new protocol

This project defines behavioral requirements and interface profiles. It does not define a universal agent manifest, new tool schema, or common wire protocol. Use existing standards where they fit. Add a new convention only when a concrete use case and interoperability evidence justify it.

The [references](../docs/references.md) identify sources and their limits. The individual topics link directly to the standards and product behavior behind their design choices.
