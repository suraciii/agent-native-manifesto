# Agent 文档 catalog 示例

[English](../../examples/agent-documentation-catalog.md) | 简体中文

这是一个面向有文档网站的应用的示例 catalog。它把 `llms.txt` 作为一种具体的发布实践。本例不是要求、可部署的网站，也不代表某项实现已经接受评估。

## 目的

catalog 为 Agent 提供从用户需要到应用使用材料的简短路径。它组织文档链接，不把所有契约或操作复制进一个文件。

catalog 应帮助 Agent 回答这些问题：

- 这个产品能否满足用户的需要？
- 需要安装、连接或授权什么？
- 哪条任务路径适合当前目标？
- 哪份契约定义了要使用的操作？
- 如何检查结果，或从失败中恢复？
- 有哪些限制、成本、保留规则和必须由人作出的决定？

## `llms.txt` 的示例形态

下面是一个虚构的客户报告服务的内容示例。URL 代表产品发布的文档网站。

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

catalog 的价值在于连接产品适用性、任务指引、权威契约和恢复材料。产品需要不同内容时，可以采用不同的分组和路径。

## Agent 使用路径

1. Agent 从用户需要出发，通过产品声明的发现路径找到 catalog。
2. Agent 阅读产品概览，判断产品是否符合需要和使用条件。
3. Agent 按快速开始或访问文档操作，但不把文档当作授权。
4. Agent 选择任务指南，遵循其依赖关系，并加载相关契约。
5. Agent 执行操作、检查结果；需要时使用诊断或恢复路径。
6. 如果任务保留了必须由人作出的决定，Agent 向负责的用户呈现所需事实和决定。

## 边界

catalog 中的链接不是操作成功的证据。操作契约描述行为；应用代码仍然负责验证输入、强制执行领域不变量和权限约束，并产生效果。catalog 的其他边界见[说明文档指南](../spec/interfaces/instructions.md#使用-llmstxt-发布-agent-文档-catalog)。

## 评估

按[评估流程](../spec/evaluation.md)将 catalog 作为声明的发现和说明路径的一部分进行评估：从正常入口开始，记录 Agent 使用了哪些条目，并测试一项常见任务和一次可恢复失败。记录不必要的查找、缺失的依赖和误导性描述。

本例定义的是一种内容组织方式，不声称虚构服务或本仓库发布或支持所示网站。
