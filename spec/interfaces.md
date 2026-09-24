# Interface guides

English | [简体中文](../zh-CN/spec/interfaces.md)

These guides apply the [core requirements](core.md) to existing access mechanisms and supporting material. Use them to choose interfaces and plan task checks. They define no additional requirements.

## Choose access paths

Choose mechanisms the intended agent can use to reach the supported outcome. Read the topics relevant to those paths; an application need not offer every interface listed here.

A path can combine interfaces. Preserve authority, state, and relevant context at each handoff, and test the complete task.

In-process functions and tool bindings can provide access without a server or packaged SDK. Apply the core to their inputs, effects, results, and recovery behavior.

### Capability access

| Mechanism | Boundary and role |
| --- | --- |
| [CLI](interfaces/cli.md) | Process invocation: help, inputs, output, and exit status |
| [HTTP API](interfaces/http-api.md) | Network requests: descriptions, credentials, responses, and conditions |
| [MCP](interfaces/mcp.md) | MCP client and server: tools, resources, prompts, and transport |
| [SDK](interfaces/sdk.md) | Program and library: callable contracts, local work, I/O, and lifecycle |

### Supporting contracts

Use these topics where the work involves files, instructions, or human views. They add no execution interface. File inputs and outputs alone do not define how a capability is invoked.

| Topic | Responsibility |
| --- | --- |
| [Files and artifacts](interfaces/files-and-artifacts.md) | Formats, versions, access, transfer, and any file-triggered behavior |
| [Instructions](interfaces/instructions.md) | Discovery, contracts, methods, and progressive loading |
| [Presentation](interfaces/presentation.md) | Views, edits, decisions, and coordination with agent work |

## Understand the different responsibilities

Execution, description, methods, and presentation are distinct. A CLI can call HTTP, an MCP server can use an SDK, and a Skill can guide either. MCP can use local stdio without an HTTP API. A view can present the same work without duplicating domain rules.

The [instructions topic](interfaces/instructions.md) separates finding a product, understanding an interface, selecting an operation, and checking current authority.

## Choose the smallest useful combination

1. Identify what the agent can run, install, connect to, retrieve, and render.
2. Find the boundary that already owns the capability. Add an adapter only when it removes caller work or reaches an intended environment.
3. Complete the path through context, authorization, results, correction, and human handoffs.
4. Add another interface only for a supported use, then evaluate the whole combination.

| Approach | Benefit | Failure to guard against |
| --- | --- | --- |
| Adapt an existing domain API | Reuse tested behavior and rules | Blindly exposing internal endpoints without useful names, parameters, or results |
| Build a domain operation shared by entry points | Hide repeated work behind one responsibility | Hiding consequential choices or implementing the same rules separately in each entry point |

Neither requires a universal internal service layer.

## Preserve one meaning across interfaces

These mappings of the [reporting service](../examples/reporting-service.md) illustrate shared meaning, not prescribed commands or endpoints.

| Domain meaning | CLI mapping | HTTP mapping | MCP mapping |
| --- | --- | --- | --- |
| Read a draft | Return content or a reference and revision | Retrieve the resource and revision | Read tool or resource supplies the same facts |
| Update the observed revision | Accept the expected revision | Conditional request or revision condition | Tool input includes the revision condition |
| Accept continuing work | Report acceptance and work identity | Acceptance response supplies a status reference | Tool result identifies accepted work |
| Retrieve an artifact | File or authorized retrieval reference | Representation or artifact endpoint | Content or a resource retrievable by the agent |

Syntax and controls can differ. Preserve outcomes, authority, domain invariants, and material facts. A view may support direct editing while a CLI replaces a complete draft.

The application owns effects and guarantees. The client owns request policy within those guarantees. The agent owns its rendering policy. Descriptions do not enforce these boundaries.

## Compare through use

Use the [evaluation procedure](evaluation.md#comparing-interfaces) to compare setup, repeated use, data handling, recovery, and maintenance. This repository has not established a performance ranking of interfaces.

## No mandatory new protocol

This project defines no universal agent manifest or wire protocol. Use existing standards. Justify a new convention with a concrete use case and interoperability evidence.
