# 参考资料

[English](../../docs/references.md) | 简体中文

这些来源为本项目的提议提供参考，并不为其背书。实现和评估必须注明所使用的确切协议版本。

## 范式的论述方式

| 来源 | 启发 | 适用边界 |
| --- | --- | --- |
| [The Reactive Manifesto](https://www.reactivemanifesto.org/) | 解释需求如何变化，以及设计选择如何支持共同目标 | 其架构选择针对响应式系统；本项目不要求消息传递 |
| [CNCF Cloud Native Definition](https://github.com/cncf/toc/blob/main/DEFINITION.md) | 通过变化的条件、系统品质和有用结果定义范式 | 云基础设施选择不是 Agent Native 应用的要求 |
| [Manifesto for Agile Software Development](https://agilemanifesto.org/) | 表明设计优先级，并与详细原则区分 | 其价值观针对软件开发；本项目讨论应用使用 |
| [Local-first software](https://www.inkandswitch.com/essay/local-first/) | 从用户活动推导设计目标，并据此检视具体产品和原型 | 本地存储和 CRDT 不是 Agent Native 应用的要求 |
| [The Extensible Web Manifesto](https://github.com/extensibleweb/manifesto/blob/master/README.md) | 解释开放能力如何支持新用途，以及使用如何改进规范 | 其底层浏览器原语不规定应用操作的粒度 |
| [The Twelve-Factor App](https://12factor.net/) | 将方向转化为范围清晰的具体工程实践 | 其 SaaS 实践仍有独立价值；本项目不替代它们，也不要求十二要素 |
| [Mohist: Philosophy of Software Development](https://github.com/suraciii/mohist/blob/master/docs/philosophy.md) | 人的目的、复核与纠正、委托使用、可执行规则，以及围绕用户 Agent 组织的应用 | Mohist 是启发本项目的应用之一，不是必需架构 |
| [软件的终结和最后的UI —— Agent时代的软件产品新形态是什么？](https://mp.weixin.qq.com/s/yNfU-k9tREesxYP9pO5I6w)，新奇骰子匠人 | 应用通过能力、说明文档、Skill 和呈现进入用户的 Agent | 关于最终界面或直接使用消失的说法属于预测，不是本规范的前提 |

## 应用与工具设计

| 来源 | 启发 | 适用边界 |
| --- | --- | --- |
| [Every: Agent-native Architectures](https://every.to/guides/agent-native) | 能力覆盖、组合与新用途 | 工具粒度、文件存储和判断责任的分配需要适合具体领域 |
| [Agent-Native: What is Agent-Native?](https://www.agent-native.com/docs/what-is-agent-native/) | Agent 与面向人的视图共享操作、数据和相关上下文 | 其框架是一种实现；本项目不要求 TypeScript 或内置 Agent |
| [Anthropic: Writing effective tools for AI agents](https://www.anthropic.com/engineering/writing-tools-for-agents) | 任务驱动的工具设计、有意义的上下文、有界输出与评估 | 观察到的性能取决于任务、模型和运行环境；工具数量或粒度不存在通用最优值 |

## 现有接口机制

主要来源及其限制，放在使用它们的相应指南中：

| 主题 | 涵盖的来源 |
| --- | --- |
| [CLI](../spec/interfaces/cli.md) | Command Line Interface Guidelines、GitHub CLI、Git porcelain 输出 |
| [HTTP](../spec/interfaces/http-api.md) | OpenAPI、HTTP 语义、Problem Details、API 目录、Stripe 幂等性、S3 预签名 URL |
| [MCP](../spec/interfaces/mcp.md) | MCP 2025-11-25 中的工具、资源、提示模板、传输与授权 |
| [SDK](../spec/interfaces/sdk.md) | Stripe Python 客户端行为与生成的 OpenAPI 绑定 |
| [文件与产出物](../spec/interfaces/files-and-artifacts.md) | Linux rename 和 fsync 的保证与限制 |
| [说明文档](../spec/interfaces/instructions.md) | Agent Skills、AGENTS.md、llms.txt 和 API 目录 |
| [呈现](../spec/interfaces/presentation.md) | MCP Apps 和 WAI-ARIA 交互指导 |

[A2A core concepts](https://a2a-protocol.org/latest/topics/key-concepts/) 涵盖委托式 Agent 服务的 Agent 描述、任务、消息和产出物。普通工具和确定性服务不需要 Agent 之间的协作。

要求词遵循 [BCP 14](https://www.rfc-editor.org/rfc/rfc8174.html)，表达本项目的责任，不代表外部背书。

## 运用这些来源

用成熟格式表达清楚的领域契约，并在声称支持的环境中验证。引用材料保留各自的许可证。本项目的要求与示例是原创文字。
