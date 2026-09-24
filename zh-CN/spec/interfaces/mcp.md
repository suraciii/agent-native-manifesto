# Model Context Protocol

[English](../../../spec/interfaces/mcp.md) | 简体中文

MCP 将客户端连接到服务器的工具、资源和提示模板。本指南应用[核心要求](../core.md)；另见[接口概览](../interfaces.md)。

示例与来源使用 **MCP 2025-11-25**。评估时，应以应用和客户端环境实际支持的协议修订版本为准。

## 作用与适用条件

客户端必须支持所需的传输、授权和能力。MCP 不建立全局产品发现：仍需由用户、注册表、管理员或客户端提供服务器入口。

## 设计选择

### 工具、资源与提示模板

| 基础机制 | 典型用途 | 报告服务中的示例 |
| --- | --- | --- |
| 工具（Tool） | 执行操作，包括有界查询 | 搜索相关记录；修改草稿 |
| 资源（Resource） | 提供可寻址的上下文或内容 | 读取报告修订版本或支撑材料 |
| 提示模板（Prompt） | 提供可复用的交互模板 | 发起一次引导式报告复核活动 |

在所引用的协议修订版本中，工具由模型控制、资源由应用驱动、提示模板由用户控制，这是其设计模式。客户端的呈现方式可能不同；列出资源并不意味着已将其加载进模型。

用资源提供可寻址、可复用的上下文。搜索仍可以是工具。[Skill](instructions.md) 可以教授跨工具与资源的方法，但它不能与提示模板等同。

### 工具边界

适配器应保留领域规则，不必暴露每个存储原语。工具可以组合工作，但其描述和 schema 需要说明输入含义、效果，以及发布、计费和通知等重要选择。

工具注解描述预期行为；目录条目不会授权调用方对所有对象执行操作。即使客户端缓存了目录，执行时仍要检查当前权限和对象条件。

包装 CLI 时，使用它的机器格式和进程语义。不要把通用 shell 执行器伪装成范围狭窄的领域工具。

### 结果与上下文成本

所引用的协议修订版本支持结构化结果、可选的输出 schema 和内容块。遵循其关于结构化与文本表示的兼容性指导。通过工具结果机制报告领域失败，并与协议错误区分。保留标识符，并在支持获取时使用资源链接提供细节。

资源 URI 不一定能直接获取。服务器端的 `file` 资源未必位于 Agent 本地。在每个受支持的客户端环境中检查资源获取和界面交接。

测试目录分页与更新；在每个客户端环境中度量工具选择和上下文使用。不要假设客户端会按需发现工具或注入整个目录；即使目录很小，含糊的描述也可能掩盖能力。

### 传输与授权

Stdio 将 stdout 保留给协议消息；一条日志横幅就可能破坏连接。Streamable HTTP 对请求、流和安全有独立规则。

所引用的授权规范为受保护的 HTTP 访问定义资源发现与授权服务器发现。令牌必须以接收服务为目标；上游调用需要适当的上游授权，不能盲目转发调用方的令牌。

本地传输可以从客户端环境接收凭证。这不意味着授予无限制的文件系统或网络权限；仍须执行适用范围。如果客户端无法完成所需访问流程，应提供受支持的交接，而不是让模型在任务内容中携带秘密。

### 连接状态与持续工作

协议会话、工具调用和领域工作的生命周期不同。受支持的任务或进度机制可以承载 AN-07 契约，却不能定义该契约。仅有断连不能证明工作已取消。

为持久对象和工作提供明确标识符，或说明在受支持的重连后仍然有效的范围。不要从未说明的对话历史中推断操作目标。

## 示例

以下[报告服务](../../examples/reporting-service.md)工具使用所引用修订版本的字段，仅作示例，并非运行中的服务器。

```json
{
  "name": "read_report",
  "description": "Read the current draft of an authorized report. Returns its revision and content reference. Does not publish or modify it.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "report_id": { "type": "string" }
    },
    "required": ["report_id"],
    "additionalProperties": false
  },
  "outputSchema": {
    "type": "object",
    "properties": {
      "report_id": { "type": "string" },
      "revision": { "type": "string" },
      "content_uri": { "type": "string" }
    },
    "required": ["report_id", "revision", "content_uri"]
  }
}
```

契约仍需说明标识符范围、URI 获取方式和错误行为。读取内容后，后续更新通过另一项操作提交已观察的修订版本。

## 验证

| 重点 | 可尝试的用例 |
| --- | --- |
| 协议与目录 | 选定的协议修订版本；多页目录；schema 不匹配；业务错误与协议错误；stdio 中 stdout 被污染 |
| 领域行为与授权 | 权限不符；上游令牌分离；跨用户对象访问；重连调用方使用明确的工作标识 |
| 上下文与客户端行为 | 客户端提供工具但不支持假定的资源路径；过期目录；界面扩展不可用；大型结果与有限上下文 |

使用[评估流程](../evaluation.md)，包括在每个声称支持的客户端环境中执行任务。

## 来源与相关主题

- MCP 2025-11-25：[tools](https://modelcontextprotocol.io/specification/2025-11-25/server/tools)、[resources](https://modelcontextprotocol.io/specification/2025-11-25/server/resources) 和 [prompts](https://modelcontextprotocol.io/specification/2025-11-25/server/prompts)。
- 同一修订版本的 [transports](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports) 和 [authorization](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)。
- [Writing effective tools](https://www.anthropic.com/engineering/writing-tools-for-agents)：基于任务的工具设计与评估，不存在通用的最优粒度。
- 相关主题：[HTTP](http-api.md)、[CLI](cli.md)、[说明文档](instructions.md)和[呈现](presentation.md)。
