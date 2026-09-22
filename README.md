# Agent-Native Manifesto

**Design applications first for agents acting for people.**

An **agent-native application** is designed first for an agent acting on a user's behalf. It exposes discoverable, understandable capabilities that agents can call and combine, together with the knowledge and current context needed to use them. People retain the means to inspect results, participate directly, and change the work.

People can express tasks in natural language through their preferred agent. The application supports the path from that request to usable results. Language understanding may run in the user's agent or host; the application can provide its capabilities through a CLI, functions, MCP, HTTP, or another suitable mechanism.

Agent use is the primary design path. Human views focus on showing work, enabling review, and supporting direct edits and decisions. An application can provide its own UI and its own agent while also supporting other agents.

## The manifesto

People use software to change something in the world. As agents undertake more of that use, applications must make their capabilities available within delegated work. People should be able to bring their agent, express an intention, and draw on the capabilities of many applications without repeatedly translating their purpose into each product's interface.

We build applications with four connected properties.

### Actionable

**Make useful capabilities directly available.**

An agent can find what an application does, learn its terms, obtain the required access, and perform meaningful operations. Capability contracts, task guidance, and current facts are part of the product. The application enforces the rules it controls and returns enough information to continue.

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

## From philosophy to working applications

The argument proceeds from the changed use relationship to product design, explicit requirements, and complete examples. Findings from actual use can refine both the design principles and the specification.

| Layer | Read | What it establishes |
| --- | --- | --- |
| Philosophy | [Foundations](docs/foundations.md) | Why applications should be designed first for agents; the person–agent–application interaction model |
| Product design | [Application model](docs/application-model.md) | How to organize capabilities, context, composition, and human participation across the full use cycle |
| Specification | [Core requirements](spec/core.md), [interface profiles](spec/interfaces.md), and [evaluation](spec/evaluation.md) | Observable obligations, their scope, and the evidence needed to assess them |
| Cases | [Local image tool](examples/local-tool.md) and [continuing reporting service](examples/reporting-service.md) | Natural-language tasks, application capabilities and context, agent actions, human changes, and requirement mappings |

The [interface overview](spec/interfaces.md) covers CLI, HTTP, MCP, and SDK access, together with supporting contracts for files and artifacts, instructions, and presentation. Apply them to the mechanisms actually used. No particular protocol, server architecture, or packaged SDK is required.

Use the [assessment template](examples/assessment-template.md) to record evidence from an implementation. The [references](docs/references.md) identify sources and the limits of what they establish.

## Status and scope

This is a **working draft** of an independent manifesto and specification. Requirements in `spec/` are proposals made by this project. They do not claim endorsement by a standards body or protocol maintainer.

The specification defines observable behavior. An application selects interfaces suited to its users and environment. It does not need every protocol, a model runtime, a server, a graphical UI, or an autonomous worker.

The examples are design illustrations. No application has been certified by this repository. An evaluation must name the exact specification revision, application, supported work, interfaces, and evidence.

## Contribute

Bring concrete tasks, counterexamples, and evidence from use. See [Contributing](CONTRIBUTING.md). The document check runs with `python3 scripts/check_docs.py`; it verifies repository structure, local links, requirement references, and JSON example syntax, not application behavior.

## License

Original prose is available under [CC BY 4.0](LICENSE). Code, including code examples, scripts, and workflow files, is available under the [MIT License](LICENSE-CODE). Referenced sources retain their own licenses. Attribute this work to the **Agent-Native Manifesto contributors** and link to this repository when reusing its prose.
