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
| [OpenAPI Specification](https://spec.openapis.org/oas/latest.html) | Machine-readable HTTP interface descriptions | Domain semantics, side effects, and execution guarantees still need explicit contracts |
| [MCP Tools](https://modelcontextprotocol.io/specification/latest/server/tools) | Tool discovery, invocation, schemas, results, and errors | Discovery occurs within a configured connection; tool metadata does not grant authority |
| [MCP Authorization](https://modelcontextprotocol.io/specification/latest/basic/authorization) | Protected service access and authorization discovery | Requirements vary by transport and protocol version; domain authorization remains necessary |
| [Agent Skills specification](https://agentskills.io/specification) | A portable format for methods and progressive loading of instructions and resources | A Skill explains use; it is not an access grant or an execution guarantee |
| [The llms.txt proposal](https://llmstxt.org/) | A concise documentation entry point and links to agent-readable detail | It is a proposal and does not ensure every host discovers the product or can invoke it |
| [RFC 9727: API catalog discovery](https://www.rfc-editor.org/rfc/rfc9727.html) | A well-known URI and link relation for discovering API catalogs | Client support and an actual path to the catalog are still needed |
| [MCP Apps overview](https://apps.extensions.modelcontextprotocol.io/api/documents/overview.html) | Tools connected to interactive views in supporting hosts | UI delivery and host support do not replace the domain operation contract |
| [A2A core concepts](https://a2a-protocol.org/latest/topics/key-concepts/) | Agent descriptions, tasks, messages, and artifacts for delegated agent services | Ordinary tools and deterministic services do not need agent-to-agent collaboration |
| [RFC 8174: BCP 14 requirement words](https://www.rfc-editor.org/rfc/rfc8174.html) | Explicit meanings for normative keywords | These keywords express this project's requirements, not the endorsement of an external body |

## Applying these sources

Use mature formats to express a clear domain contract. Keep the definition of agent-native independent of a vendor, model, runtime, or protocol. Verify claims about host support with the actual versions in use.

The source material is credited for ideas and existing mechanisms. It is not included under this repository's license. The local examples and normative requirements are original project text.
