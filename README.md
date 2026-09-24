# Agent Native Manifesto

English | [简体中文](zh-CN/README.md)

**Design applications first for agents acting on behalf of users.**

## What is Agent Native?

An **Agent Native application** provides the capabilities, clear guidance, and current facts an agent needs to act on a user's behalf. The user can inspect results, participate directly, and change the work.

Users can state a goal in natural language and ask an agent to carry it through applications. The agent needs to find suitable capabilities, understand their terms and conditions, obtain current facts, perform operations, and check results. The application makes these conditions part of its product.

## Why applications need to change

Applications built around human navigation often leave the agent to reconstruct the product: infer which operation fits, discover hidden dependencies, read state through a screen, and decide whether a result means completion. That work creates needless explanation, guessing, failed attempts, and fragile handoffs.

Agent Native design makes an application's capabilities usable in the user's work. Clear guidance lowers the agent's inference burden. Current facts and inspectable results support sound next steps. Usable outputs carry work into other applications. Human views and decisions keep the user able to set direction, take responsibility, and correct the work.

## A task in practice

A user asks:

> Prepare a report of this week's customer problems. Give me a draft before publication.

The agent finds a suitable reporting application, learns the reporting scope and access conditions, retrieves relevant records, prepares a draft, and explains what the result covers. The user reviews the draft, approves a specific revision, or edits it before approval. The agent requests publication. The application checks the required authority and approval conditions, then publishes the selected revision.

## The manifesto

### Design applications first for users' agents

Start from the user's need. Make the product, its fit, its conditions, and the full path to a supported result reachable to the agent. Human decisions and access steps have explicit handoffs. The application enforces the business rules and authority it controls.

### Deliver context with capabilities

Provide clear guidance and current facts with the operations they explain. The agent includes that material in model input as needed. Let the agent choose, act, check results, and recover from known failures while keeping important choices open to the user's purpose.

### Let work cross application boundaries

Give later activities usable capabilities and results with clear meaning, origin, and authorized access.

### Delegate action, retain human direction

Keep inspection, editing, redirection, and takeover effective. Require the responsible user to make decisions reserved for a human. Make committed changes available to later agent operations. Distinguish changes to future work from effects already produced.

## Continue reading

- **Understand why applications need to change:** [Foundations](docs/foundations.md)
- **Understand how an application is organized:** [Application model](docs/application-model.md)
- **Understand what an application must provide:** [Core requirements](spec/core.md) and [interface guides](spec/interfaces.md)
- **Understand how to verify actual use:** [Evaluation](spec/evaluation.md) and [assessment template](examples/assessment-template.md)
- **See complete task paths:** [Local image tool](examples/local-tool.md) and [reporting service](examples/reporting-service.md)
- **See a documentation catalog case:** [Agent documentation catalog](examples/agent-documentation-catalog.md)
- **Review sources and their limits:** [References](docs/references.md)

## Status and scope

This is an independent working draft. It carries no standard endorsement. The examples are design documents and have not been evaluated as implementations. The project makes no certification claim.

Language understanding may run in the user's agent. An application may provide its own UI and agent while supporting external agents. No particular protocol, server, or SDK package is required. Apply requirements to the work and access paths being assessed.

## Contribute

Bring concrete tasks, counterexamples, and evidence from use. See [Contributing](CONTRIBUTING.md) for the editing rules and document check.

## License

Original prose is available under [CC BY 4.0](LICENSE). Code, including code examples, scripts, and workflow files, is available under the [MIT License](LICENSE-CODE). Referenced sources retain their own licenses. Attribute this work to the **Agent Native Manifesto contributors** and link to this repository when reusing its prose.
