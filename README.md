# Agent-Native Manifesto

**Build applications that people can use through their agents.**

An **agent-native application** takes an agent acting for a user as its primary direct user. It organizes its capabilities so that the agent can discover, understand, use, and combine them in the user's work. People retain the means to understand results, take part, and change direction.

The user's agent may come from the application or another product. An application can be agent-native with ordinary code, a command-line interface, or an API. Its defining property is the relation of use it supports.

## The manifesto

People use software to change something in the world. As agents undertake more of that use, applications must make their capabilities available within delegated work. People should be able to bring their agent, express an intention, and draw on the capabilities of many applications without repeatedly translating their purpose into each product's interface.

We build applications with four connected properties.

### Actionable

**Make useful capabilities directly available.**

An agent can find what an application does, learn its terms, obtain the required access, and perform meaningful operations. Each operation has a clear contract. The application enforces the rules it controls and returns enough information to continue.

### Composable

**Let capabilities take part in work beyond a fixed path.**

An agent can combine operations, carry results between applications, and respond to new conditions. Tools hide unnecessary implementation detail while preserving useful choices. Established procedures can become callable programs; judgment can remain with people and their agents.

### Inspectable

**Make work and its effects open to examination.**

People and agents can inspect relevant state, results, changes, and uncertainty. Claims about progress have evidence. Feedback is timely, focused, and connected to the action that produced it. A summary provides a path to the facts behind it.

### Correctable

**Keep work responsive to human purpose.**

People can question assumptions, edit work, change requirements, revise authority, and take over. The application makes those changes effective within stated limits. It distinguishes what can still change from effects that have already occurred.

These properties make useful delegation possible. Actionable capabilities provide the means to act. Composition extends what can be done. Inspection supports judgment. Correction keeps the work answerable to its purpose.

We judge progress through use: the value of the result, the effort of explanation and coordination, the cost of execution, and the person's ability to understand and influence what happens. Direct participation can itself be valuable. People choose how much to delegate.

## From idea to application

| Read | Purpose |
| --- | --- |
| [Foundations](docs/foundations.md) | Why this relation changes application design; terms and boundaries |
| [Application model](docs/application-model.md) | Product forms, responsibilities, discovery, and the full use cycle |
| [Core specification](spec/core.md) | Requirements shared across interface choices |
| [Interface profiles](spec/interfaces.md) | Selection, composition, and comparison of execution and participation interfaces |
| [Evaluation](spec/evaluation.md) | How to check contracts and test actual delegated use |
| [Local tool example](examples/local-tool.md) | A small application with no server or task system |
| [Reporting service example](examples/reporting-service.md) | Continuing work, review, publication, and recovery |
| [References](docs/references.md) | Sources, existing standards, and the limits of each |

Each interface topic has its own design analysis, requirements, examples, verification cases, and sources: [CLI](spec/interfaces/cli.md), [HTTP API](spec/interfaces/http-api.md), [MCP](spec/interfaces/mcp.md), [SDK](spec/interfaces/sdk.md), [files](spec/interfaces/files.md), [instructions and Skills](spec/interfaces/instructions.md), and [presentation](spec/interfaces/presentation.md).

## Status and scope

This is a **working draft** of an independent manifesto and specification. Requirements in `spec/` are proposals made by this project. They do not claim endorsement by a standards body or protocol maintainer.

The specification defines observable behavior. An application selects interfaces suited to its users and environment. It does not need every protocol, a model runtime, a server, a graphical UI, or an autonomous worker.

The examples are design illustrations. No application has been certified by this repository. An evaluation must name the exact specification revision, application, supported work, interfaces, and evidence.

## Contribute

Bring concrete tasks, counterexamples, and evidence from use. See [Contributing](CONTRIBUTING.md). The document check runs with `python3 scripts/check_docs.py`; it verifies repository structure, local links, requirement references, and JSON example syntax, not application behavior.

## License

Original prose is available under [CC BY 4.0](LICENSE). Code, including code examples, scripts, and workflow files, is available under the [MIT License](LICENSE-CODE). Referenced sources retain their own licenses. Attribute this work to the **Agent-Native Manifesto contributors** and link to this repository when reusing its prose.
