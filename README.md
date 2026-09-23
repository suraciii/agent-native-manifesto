# Agent Native Manifesto

English | [简体中文](zh-CN/README.md)

**Design applications first for agents acting on behalf of users.**

An **Agent Native application** supplies capabilities, clear guidance, and current facts for agents acting on behalf of users. Users retain the means to inspect results, participate directly, and change the work.

## The manifesto

### Design applications first for users' agents

Make the product discoverable from users' needs, with a clear account of its help, conditions, and limits. Provide a complete path through operations, results, and exceptions. Delegated work should not require imitating human screen navigation; necessary human decisions and access steps need explicit handoffs. The application enforces the rules and authority it controls.

### Deliver context with capabilities

Provide clear guidance and current facts that the host or agent can use in model input. Give common tasks a usable path, with conditions, important choices, and result checks. Known usage rules should not have to be discovered through repeated guesswork and failed attempts.

Guidance supports agents in organizing and adapting work to the user's purpose. It cannot settle that purpose or grant authority.

### Let work cross application boundaries

Users' work can continue beyond a product. Supply capabilities and results that the next activity can use, with clear meaning, origin, and authorized access. A small operation and a complete workflow can each contribute to a larger task.

### Delegate action, retain human direction

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
