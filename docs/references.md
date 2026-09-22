# References

This project combines a view of delegated software use with established interface and engineering practices. The manifesto and its requirement set are this project's proposal. The sources below do not endorse it.

Protocol links may point to evolving documents. An implementation and its assessment must name the exact versions it supports. A discovery document, schema, or protocol capability does not by itself establish successful use in a host.

## Framing the paradigm

| Source | Contribution | Boundary |
| --- | --- | --- |
| [The Reactive Manifesto](https://www.reactivemanifesto.org/) | A short statement of mutually supporting system properties | Its properties concern reactive systems; this project does not rename or reproduce their requirements |
| [CNCF Cloud Native Definition](https://github.com/cncf/toc/blob/main/DEFINITION.md) | Define a paradigm through changed conditions, system qualities, and useful outcomes | Cloud infrastructure choices are not requirements for agent-native applications |
| [The Twelve-Factor App](https://12factor.net/) | Turn a direction into concrete engineering practices with clear scope | Its SaaS practices remain independently useful; this project does not replace them or require twelve factors |
| [Mohist: Philosophy of Software Development](https://github.com/suraciii/mohist/blob/master/docs/philosophy.md) | Human purpose, review and correction, delegated use, executable rules, and applications organized around a user's agent | Mohist is one motivating application, not the required architecture |
| [软件的终结和最后的UI —— Agent时代的软件产品新形态是什么？](https://mp.weixin.qq.com/s/yNfU-k9tREesxYP9pO5I6w), 新奇骰子匠人 | Applications entering the user's agent through capabilities, instructions, Skills, and presentation | Claims about a final UI or the disappearance of direct use are predictions, not premises of this specification |

## Application and tool design

| Source | Contribution | Boundary |
| --- | --- | --- |
| [Every: Agent-native Architectures](https://every.to/guides/agent-native) | Capability coverage, composition, new uses, and improvement through experience | Tool granularity, file storage, and the distribution of judgment need to fit the domain |
| [Agent-Native: What is Agent-Native?](https://www.agent-native.com/docs/what-is-agent-native/) | Shared actions, data, and relevant context across agents and human views | Its framework is one implementation; this project does not require TypeScript or an embedded agent |
| [Anthropic: Writing effective tools for AI agents](https://www.anthropic.com/engineering/writing-tools-for-agents) | Task-driven tool design, meaningful context, bounded output, and evaluations | Observed performance depends on the task, model, and host; tool count or granularity has no universal optimum |

## Existing interface mechanisms

| Source | Contribution | Boundary |
| --- | --- | --- |
| [Command Line Interface Guidelines](https://clig.dev/) | Help, scripting, result channels, machine output, and non-interactive use | These are design guidelines, not a universal command schema |
| [GitHub CLI formatting and API commands](https://cli.github.com/manual/gh_api) | Concrete field selection, explicit methods, pagination, and request construction | Flags can alter request semantics; these behaviors are specific to this CLI |
| [Git status](https://git-scm.com/docs/git-status) | Stable porcelain output and NUL-delimited filenames for programs | Its native framing is useful without requiring a JSON wrapper |
| [OpenAPI Specification](https://spec.openapis.org/oas/latest.html) | Machine-readable HTTP interface descriptions | Domain semantics, side effects, and execution guarantees still need explicit contracts |
| [RFC 9110: HTTP semantics](https://www.rfc-editor.org/rfc/rfc9110.html) | Methods, status codes, conditional requests, and the meaning of acceptance | Transport success and domain completion can concern different activities |
| [RFC 9457: Problem Details](https://www.rfc-editor.org/rfc/rfc9457.html) | A standard error representation with identifiable problem types and occurrence detail | Human explanation is not a field to parse for programmatic recovery |
| [Stripe idempotent requests](https://docs.stripe.com/api/idempotent_requests) | A concrete contract for repeated parameters, retained outcomes, and key lifetime | Provider-specific guarantees do not establish exactly-once execution or a universal retention period |
| [Stripe Python SDK](https://github.com/stripe/stripe-python) | Client options and automatic retries as part of the callable contract | An SDK's internal retry does not necessarily preserve identity across fresh outer calls |
| [S3 presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html) | Scoped artifact access whose validity also depends on underlying credentials | Possession can grant access; the URL is sensitive material rather than an ordinary public citation |
| [MCP Tools, 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/server/tools) | Tool discovery, invocation, schemas, results, and errors in a named reference revision | Discovery occurs within a configured connection; tool metadata does not grant authority |
| [MCP Authorization, 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) | Protected service access and authorization discovery | Requirements vary by transport and protocol version; domain authorization remains necessary |
| [MCP Transports, 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports) | Stdio and Streamable HTTP framing and connection behavior | Protocol session and domain work lifetimes are separate |
| [MCP Resources, 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/server/resources) | Addressable context and host-mediated retrieval | A resource identifier does not guarantee a host can fetch it as a normal URL |
| [MCP Prompts, 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/server/prompts) | Reusable interaction templates | A prompt is not a universal Skill or an authorization grant |
| [Agent Skills specification](https://agentskills.io/specification) | A portable format for methods and progressive loading of instructions and resources | A Skill explains use; it is not an access grant or an execution guarantee |
| [AGENTS.md](https://agents.md/) | Repository guidance for coding agents | Loading and instruction handling depend on the host; it does not describe universal remote access |
| [The llms.txt proposal](https://llmstxt.org/) | A concise documentation entry point and links to agent-readable detail | It is a proposal and does not ensure every host discovers the product or can invoke it |
| [RFC 9727: API catalog discovery](https://www.rfc-editor.org/rfc/rfc9727.html) | A well-known URI and link relation for discovering API catalogs | Client support and an actual path to the catalog are still needed |
| [MCP Apps overview](https://apps.extensions.modelcontextprotocol.io/api/documents/overview.html) | Tools connected to interactive views in supporting hosts | UI delivery and host support do not replace the domain operation contract |
| [A2A core concepts](https://a2a-protocol.org/latest/topics/key-concepts/) | Agent descriptions, tasks, messages, and artifacts for delegated agent services | Ordinary tools and deterministic services do not need agent-to-agent collaboration |
| [WAI-ARIA modal dialog pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/) | Accessible labels, keyboard behavior, and focus management in a human decision surface | Declaring a role alone does not implement the required interaction behavior |
| [Linux rename](https://man7.org/linux/man-pages/man2/rename.2.html) and [fsync](https://man7.org/linux/man-pages/man2/fsync.2.html) | Atomic visibility, no-overwrite options, filesystem boundaries, and persistence | Platform-specific mechanisms do not establish a cross-platform durability or concurrency guarantee |
| [RFC 8174: BCP 14 requirement words](https://www.rfc-editor.org/rfc/rfc8174.html) | Explicit meanings for normative keywords | These keywords express this project's requirements, not the endorsement of an external body |

## Applying these sources

Use mature formats to express a clear domain contract. Keep the definition of agent-native independent of a vendor, model, runtime, or protocol. Verify claims about host support with the actual versions in use. The [interface topics](../spec/interfaces.md) connect these sources to specific design choices, examples, and verification cases.

The source material is credited for ideas and existing mechanisms. It is not included under this repository's license. The local examples and normative requirements are original project text.
