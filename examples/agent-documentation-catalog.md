# Agent documentation catalog example

English | [简体中文](../zh-CN/examples/agent-documentation-catalog.md)

This is an illustrative catalog for an application with a documentation website. It uses `llms.txt` as one concrete publishing practice. It is not a requirement, a deployable website, or evidence that an implementation has been evaluated.

## Purpose

The catalog gives an Agent a short path from a user's need to the product material needed to use the application. It organizes links to documentation; it does not copy every contract or operation into one file.

The catalog should help an Agent answer these questions:

- Can this product help with the user's need?
- What must be installed, connected, or authorized?
- Which task path fits the goal?
- Which contract defines the operation?
- How can the result be checked or the work recovered?
- What limits, costs, retention, and human decisions apply?

## Illustrative `llms.txt` shape

The following is a content example for a hypothetical customer reporting service. The URLs represent the product's published documentation site.

```text
# Customer reporting service

> Prepare inspectable customer-problem reports and publish approved revisions.

## Start here

- [Product overview](https://example.com/docs/overview.md): Supported reports, sources, limits, and review conditions.
- [Agent quickstart](https://example.com/docs/agent-quickstart.md): Connection, identity, access, and first-use steps.

## Tasks

- [Prepare a weekly draft](https://example.com/docs/tasks/weekly-draft.md): Sources, scope, dependencies, checks, and recovery.
- [Review and publish a revision](https://example.com/docs/tasks/review-and-publish.md): Human decision, revision binding, and publication checks.

## Contracts

- [HTTP API](https://example.com/docs/contracts/http-api.md): Operations, inputs, results, errors, and versions.
- [Work and artifact access](https://example.com/docs/contracts/work-and-artifacts.md): Status, drafts, exports, and authorized references.

## Recovery and limits

- [Diagnostics](https://example.com/docs/diagnostics.md): Known effects, unknown outcomes, dependency failures, and next checks.
- [Limits and retention](https://example.com/docs/limits.md): Budgets, retention, deletion, revocation, and active work.
```

The catalog is useful because it connects product fit, task guidance, authoritative contracts, and recovery material. The exact sections and paths can differ when the product has different needs.

## Agent use path

1. The Agent starts with the user's need and reaches the catalog through the product's declared discovery path.
2. It reads the overview and decides whether the product fits the need and conditions.
3. It follows the quickstart or access documentation without treating documentation as authorization.
4. It selects a task guide, follows its dependencies, and loads the relevant contract.
5. It performs the operation, checks the result, and follows the diagnostic or recovery path when needed.
6. It presents required facts and decisions to the responsible user when the task reserves a decision for a human.

## Boundaries

A catalog link is not proof that an operation succeeded. Operation contracts describe behavior; application code still validates inputs, enforces domain invariants and authority, and produces effects. The [instructions guide](../spec/interfaces/instructions.md#publish-an-agent-documentation-catalog-with-llmstxt) defines the catalog's other limits.

## Assessment

Assess the catalog as part of the declared discovery and instruction path under the [evaluation procedure](../spec/evaluation.md): start from the normal entry point, record which entries the Agent used, and test one common task and one recoverable failure. Record unnecessary searching, missing dependencies, and misleading descriptions.

This case defines an example content map. It does not claim that the hypothetical service or this repository publishes or supports the shown site.
