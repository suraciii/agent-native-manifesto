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

## Catalog contents

| Catalog entry | Linked material | Purpose |
| --- | --- | --- |
| Product overview | Supported work, outcomes, providers, limits, and conditions | Judge fit before detailed use |
| Agent quickstart | Installation or connection, identity, access, and first-use path | Start without hidden setup knowledge |
| Task guides | Goals, dependencies, choices, result checks, and recovery | Follow a recommended path or adapt it |
| Interface contracts | CLI, HTTP, MCP, SDK, or file contracts with versions | Select and invoke capabilities correctly |
| Human participation | Decisions, responsible roles, handoffs, and direct operations | Preserve human direction and authority |
| Diagnostics and recovery | Status, observed effects, unknowns, dependencies, and next actions | Continue after failure or uncertainty |
| Limits and lifecycle | Budgets, retention, deletion, export, revocation, and active-work limits | Bound the work and its consequences |

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

- The catalog does not install a tool or create a connection.
- The catalog does not authenticate a caller or grant authority.
- Credentials, tokens, and user-specific private data do not belong in the catalog.
- A catalog link is not proof that an operation succeeded.
- Operation contracts describe behavior; application code still validates inputs, enforces domain invariants and authority, and produces effects.
- The catalog should identify version or scope differences when more than one set of documentation is published.

## Assessment

Assess the catalog as part of the declared discovery and instruction path:

- Start from the normal discovery environment or the normal product entry point.
- Record which catalog entries the Agent found and used.
- Check that links lead to current, accurate, and reachable material.
- Test a common task, a boundary case, and a recoverable failure.
- Record unnecessary searching, missing dependencies, misleading descriptions, and extra human explanation.

This case defines an example content map. It does not claim that the hypothetical service or this repository publishes or supports the shown site.
