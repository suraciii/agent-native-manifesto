# Agent Native Manifesto

**Design applications first for agents acting on behalf of users.**

An **Agent Native application** supplies the capabilities, knowledge, and current context needed by agents acting on behalf of users. Users retain the means to inspect results, participate directly, and change the work.

## The manifesto

### Attract users' agents by showing how the product can help

Present the product where its intended agents look for help with users' needs. Explain the help it offers in terms of the user's work, not just its functions or protocols. Make its conditions and limits clear, and connect its claims to the capabilities that deliver them.

### Design the complete path an agent needs to do the work

Design the operations, context, results, and exception paths needed to reach a supported outcome. Include clear handoffs for human decisions and access steps. The application enforces the rules and authority it controls.

Tasks can span applications. Each contributes capabilities and results that the next activity can use.

### Provide capabilities with the knowledge needed to use them

Explain what each operation does, when it applies, what it changes, and how to examine the result. Supply current facts and feedback, including partial results and uncertainty.

Recommended methods state their assumptions. Guidance can help the agent choose a means; it cannot replace the user's purpose or grant authority.

### Make human changes effective in subsequent work

Users can inspect and edit results, revise direction, change authority, or take over. Make committed changes available to later agent operations. Distinguish changes to future work from effects already produced.

Where a decision is reserved for a human, require the responsible user's own decision. Delegated authority cannot supply it.

Users choose how much to delegate within their authority and responsibilities. Direct participation can itself be valuable.

## From philosophy to working applications

| Read | Purpose |
| --- | --- |
| [Foundations](docs/foundations.md) | The argument and interaction model |
| [Application model](docs/application-model.md) | Design choices and terms |
| [Core requirements](spec/core.md) and [interface guides](spec/interfaces.md) | Shared obligations and practical guidance |
| [Evaluation](spec/evaluation.md) and [assessment template](examples/assessment-template.md) | Tests, evidence, and claims |
| [Local image tool](examples/local-tool.md) and [reporting service](examples/reporting-service.md) | Complete illustrative use paths |
| [References](docs/references.md) | Sources and their limits |

## Status and scope

This is an independent **working draft**, not an endorsed standard. The examples are designs, not evaluated implementations; the project does not certify applications.

Language understanding can run in the user's agent or host. An application may provide its own UI and agent while supporting external agents. No particular protocol, server, or SDK package is required. Apply requirements to the work and access paths being assessed.

## Contribute

Bring concrete tasks, counterexamples, and evidence from use. See [Contributing](CONTRIBUTING.md) for the editing rules and document check.

## License

Original prose is available under [CC BY 4.0](LICENSE). Code, including code examples, scripts, and workflow files, is available under the [MIT License](LICENSE-CODE). Referenced sources retain their own licenses. Attribute this work to the **Agent Native Manifesto contributors** and link to this repository when reusing its prose.
