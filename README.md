# Agent Native Manifesto

English | [简体中文](zh-CN/README.md)

**Design applications for the user's agent, not the platform's ranking.**

*Independent working draft. Examples are design documents, not evaluated implementations. No certification claim.*

## What is Agent Native?

An **Agent Native application** lets a user's agent find and invoke its operations, understand what they mean and what is true now, and carry the result into the next step. The action remains within the authority the user grants, and the user can inspect and correct the result. The user can participate directly and change the work.

Users can state a goal in natural language and ask their agent to carry it through applications. The agent needs to find suitable capabilities, understand their terms and conditions, obtain current facts, perform operations, check results, and carry the result forward. The application makes these conditions part of its product.

## Why applications need to change

The interface that hides complexity from the user also hides the contract from the agent. Applications built around human navigation often leave the user's agent to reconstruct the product: infer which operation fits, discover hidden dependencies, read state through a screen, and decide whether a result means completion. That work creates needless explanation, guessing, failed attempts, and fragile handoffs.

Agent Native design makes an application's capabilities usable in the user's work. Clear guidance lowers the agent's inference burden. Current facts and inspectable results support sound next steps. Usable outputs carry work into other applications. Human views and decisions keep the user able to set direction, take responsibility, and correct the work.

## A task in practice

A user asks:

> Prepare a report of this week's customer problems. Give me a draft before publication.

The user's agent finds a suitable reporting application, learns the reporting scope and access conditions, retrieves relevant records, prepares a draft, and explains what the result covers. The user reviews the draft, approves a specific revision, or edits it before approval. The agent requests publication. The application checks the required authority and approval conditions, then publishes the selected revision.

## The manifesto

These claims follow from the conditions of delegated use set out in [Foundations](docs/foundations.md). They apply when a user delegates work to an agent; they do not ask every application to abandon direct human use. The test is whether the user's purpose can pass through the agent without reconstruction, loss of authority, or unverifiable results.

### Make the product discoverable by the user's agent

Start from the user's need. Make the product, its fit and conditions, and the full path to a supported result reachable by the user's agent, not only through the platform's directory.

### Make the operation legible, not just callable

Provide clear guidance on the operation's meaning, conditions, effects, and limits, with current facts. The agent uses that material as needed. Let the agent choose, act, check results, and recover from known failures while keeping important choices open to the user's purpose.

### Preserve meaning, origin, and authorized access across boundaries

When work continues in another application, give later activities usable capabilities and results with clear meaning, origin, scope, and authorized access.

### Delegate action; keep judgment effective

Keep inspection, editing, redirection, and takeover effective. Require the responsible user to make decisions reserved for a human, with explicit handoffs for human decisions and access steps. Make committed changes available to later agent operations. Distinguish changes to future work from effects already produced. The application enforces the business rules and authority constraints it is responsible for.

Platform directories and rankings are distribution channels. They do not define the product. An application that is legible only to a ranking system is easier to replace. An application that is legible to the user's agent can remain a means to the user's purpose.

## Continue reading

### Understand

- [Foundations](docs/foundations.md): why applications need to change.
- [Application model](docs/application-model.md): how an application is organized.

### Specify and verify

- [Core requirements](spec/core.md) and [interface guides](spec/interfaces.md): what an application must provide.
- [Evaluation](spec/evaluation.md) and [assessment template](spec/assessment-template.md): how to verify actual use. The template is a blank form, not a completed case.

### Apply

- [Local image tool](examples/local-tool.md) and [reporting service](examples/reporting-service.md): complete task paths.
- [Agent documentation catalog](examples/agent-documentation-catalog.md): a documentation catalog case.

### Sources

- [References](docs/references.md): sources and their limits.

## Status and scope

This is an independent working draft. It carries no standard endorsement. The examples are design documents and have not been evaluated as implementations. The project makes no certification claim.

Language understanding may run in the user's agent. An application may provide its own UI and agent while supporting external agents. No particular protocol, server, or SDK package is required. Apply requirements to the work and access paths being assessed.

## Contribute

Bring concrete tasks, counterexamples, and evidence from use. See [Contributing](CONTRIBUTING.md) for the editing rules and document check.

## License

Original prose is available under [CC BY 4.0](LICENSE). Code, including code examples, scripts, and workflow files, is available under the [MIT License](LICENSE-CODE). Referenced sources retain their own licenses. Attribute this work to the **Agent Native Manifesto contributors** and link to this repository when reusing its prose.
