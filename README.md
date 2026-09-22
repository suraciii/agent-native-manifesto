# Agent Native Manifesto

**Design applications first for agents acting for people.**

People can express a task in natural language through their agent and ask it to carry the work across applications. The agent connects that purpose to available capabilities, obtains the facts needed to act, and uses results to decide what follows.

An **Agent Native application** supplies the capabilities, knowledge, and current context needed for this use. People retain the means to inspect results, participate directly, and change the work.

## The manifesto

### Design the complete path an agent needs to do the work

When an application supports an outcome, design the operations, context access, results, and exception paths an agent needs to reach it. Human decisions and access steps are part of that path, with clear handoffs. The application enforces the rules and authority it controls.

A reporting application needs to let the agent find authorized source records, understand their coverage, prepare a draft, retrieve it, and handle failures. Each of these steps belongs in the product design.

An agent may use several applications for one task. Each application contributes useful domain capabilities and results that can enter the next activity. A complete workflow or a small operation can each serve this role.

### Provide capabilities with the knowledge needed to use them

The application explains what each operation does, when it applies, what it changes, and how to examine the result. It makes relevant objects, conditions, and current state available alongside that explanation. Feedback connects the action to what actually happened, including partial results and uncertainty.

For a weekly report, this includes what counts as a customer problem, which period the report covers, and how complete the available records are. Recommended methods state their assumptions so the agent can judge whether they fit the task. Guidance does not acquire authority to replace the person's purpose.

### Make human changes effective in subsequent work

People can inspect and edit the results of agent actions, revise direction, change authority, or take over. The application makes relevant committed changes available to subsequent operations. Human views support these actions on the same relevant objects and facts that agents use.

If a person edits the report and asks for a different focus, the agent can read the saved revision and accepted direction before preparing an update. It can then reconcile the edit with the new request. The application distinguishes changes to future work from effects that have already occurred.

We judge this design through use: whether people obtain useful results, the effort and cost of reaching them, and whether they can understand and influence the work. People choose how much to delegate; direct participation can itself be valuable.

## From philosophy to working applications

The argument proceeds from the changed use relationship to product design, explicit requirements, and complete examples. Findings from actual use can refine both the design principles and the specification.

| Layer | Read | What it establishes |
| --- | --- | --- |
| Philosophy | [Foundations](docs/foundations.md) | Why applications should be designed first for agents; the person–agent–application interaction model |
| Product design | [Application model](docs/application-model.md) | How to support complete agent use, supply context, carry results between applications, and make human participation effective |
| Specification | [Core requirements](spec/core.md), [interface profiles](spec/interfaces.md), and [evaluation](spec/evaluation.md) | Observable obligations, their scope, and the evidence needed to assess them |
| Cases | [Local image tool](examples/local-tool.md) and [continuing reporting service](examples/reporting-service.md) | Natural-language tasks, application capabilities and context, agent actions, human changes, and requirement mappings |

The [interface overview](spec/interfaces.md) covers CLI, HTTP, MCP, and SDK access, together with supporting contracts for files and artifacts, instructions, and presentation. Apply them to the mechanisms actually used. No particular protocol, server architecture, or packaged SDK is required.

Use the [assessment template](examples/assessment-template.md) to record evidence from an implementation. The [references](docs/references.md) identify sources and the limits of what they establish.

## Status and scope

This is a **working draft** of an independent manifesto and specification. Requirements in `spec/` are proposals made by this project. They do not claim endorsement by a standards body or protocol maintainer.

The specification defines observable behavior. Language understanding may run in the user's agent or host. An application may provide its own UI and agent while also supporting other agents. A local tool, host function, or remote service can each provide capabilities; the applicable requirements follow the work and access paths being assessed.

The examples are design illustrations. No application has been certified by this repository. An evaluation must name the exact specification revision, application, supported work, interfaces, and evidence.

## Contribute

Bring concrete tasks, counterexamples, and evidence from use. See [Contributing](CONTRIBUTING.md). The document check runs with `python3 scripts/check_docs.py`; it verifies repository structure, local links, requirement references, and JSON example syntax, not application behavior.

## License

Original prose is available under [CC BY 4.0](LICENSE). Code, including code examples, scripts, and workflow files, is available under the [MIT License](LICENSE-CODE). Referenced sources retain their own licenses. Attribute this work to the **Agent Native Manifesto contributors** and link to this repository when reusing its prose.
