# References

These sources inform this project's proposal; they do not endorse it. Implementations and assessments must name the exact protocol versions they use.

## Framing the paradigm

| Source | Contribution | Boundary |
| --- | --- | --- |
| [The Reactive Manifesto](https://www.reactivemanifesto.org/) | Explain changed demands and how design choices support a shared goal | Its architecture choices concern reactive systems; this project does not require message passing |
| [CNCF Cloud Native Definition](https://github.com/cncf/toc/blob/main/DEFINITION.md) | Define a paradigm through changed conditions, system qualities, and useful outcomes | Cloud infrastructure choices are not requirements for Agent Native applications |
| [Manifesto for Agile Software Development](https://agilemanifesto.org/) | State design priorities and distinguish them from detailed principles | Its values concern software development; this project addresses application use |
| [Local-first software](https://www.inkandswitch.com/essay/local-first/) | Derive design goals from users' activities and examine concrete products and prototypes against them | Local storage and CRDTs are not requirements for Agent Native applications |
| [The Extensible Web Manifesto](https://github.com/extensibleweb/manifesto/blob/master/README.md) | Explain how exposed capabilities support new uses and how use can improve a specification | Its low-level browser primitives do not prescribe the granularity of application operations |
| [The Twelve-Factor App](https://12factor.net/) | Turn a direction into concrete engineering practices with clear scope | Its SaaS practices remain independently useful; this project does not replace them or require twelve factors |
| [Mohist: Philosophy of Software Development](https://github.com/suraciii/mohist/blob/master/docs/philosophy.md) | Human purpose, review and correction, delegated use, executable rules, and applications organized around a user's agent | Mohist is one motivating application, not the required architecture |
| [软件的终结和最后的UI —— Agent时代的软件产品新形态是什么？](https://mp.weixin.qq.com/s/yNfU-k9tREesxYP9pO5I6w), 新奇骰子匠人 | Applications entering the user's agent through capabilities, instructions, Skills, and presentation | Claims about a final UI or the disappearance of direct use are predictions, not premises of this specification |

## Application and tool design

| Source | Contribution | Boundary |
| --- | --- | --- |
| [Every: Agent-native Architectures](https://every.to/guides/agent-native) | Capability coverage, composition, and new uses | Tool granularity, file storage, and the distribution of judgment need to fit the domain |
| [Agent-Native: What is Agent-Native?](https://www.agent-native.com/docs/what-is-agent-native/) | Shared actions, data, and relevant context across agents and human views | Its framework is one implementation; this project does not require TypeScript or an embedded agent |
| [Anthropic: Writing effective tools for AI agents](https://www.anthropic.com/engineering/writing-tools-for-agents) | Task-driven tool design, meaningful context, bounded output, and evaluations | Observed performance depends on the task, model, and host; tool count or granularity has no universal optimum |

## Existing interface mechanisms

Primary sources and their limits live with the topics that use them:

| Topic | Sources covered |
| --- | --- |
| [CLI](../spec/interfaces/cli.md) | Command Line Interface Guidelines, GitHub CLI, Git porcelain output |
| [HTTP](../spec/interfaces/http-api.md) | OpenAPI, HTTP semantics, Problem Details, API catalogs, Stripe idempotency, S3 presigned URLs |
| [MCP](../spec/interfaces/mcp.md) | Tools, resources, prompts, transports, and authorization in MCP 2025-11-25 |
| [SDK](../spec/interfaces/sdk.md) | Stripe Python client behavior and generated OpenAPI bindings |
| [Files and artifacts](../spec/interfaces/files-and-artifacts.md) | Linux rename and fsync guarantees and limits |
| [Instructions](../spec/interfaces/instructions.md) | Agent Skills, AGENTS.md, llms.txt, and API catalogs |
| [Presentation](../spec/interfaces/presentation.md) | MCP Apps and WAI-ARIA interaction guidance |

[A2A core concepts](https://a2a-protocol.org/latest/topics/key-concepts/) covers agent descriptions, tasks, messages, and artifacts for delegated agent services. Ordinary tools and deterministic services do not need agent-to-agent collaboration.

Requirement words follow [BCP 14](https://www.rfc-editor.org/rfc/rfc8174.html); they express this project's obligations, not an external endorsement.

## Applying these sources

Use established formats for clear domain contracts and verify support in the claimed hosts. Referenced material retains its own licenses. This project's requirements and examples are original text.
