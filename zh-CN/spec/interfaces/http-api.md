# HTTP API

[English](../../../spec/interfaces/http-api.md) | 简体中文

本指南将[核心要求](../core.md)应用于 HTTP 访问。进程内 API 等其他访问路径见[接口概览](../interfaces.md)。

## 作用与适用条件

HTTP 适合共享远程状态和运行于不同环境的客户端。网络边界带来不确定性：客户端断连后，可能不知道写入是否完成。

HTTP 定义请求语义；[OpenAPI](https://spec.openapis.org/oas/latest.html) 描述操作和数据。领域指导解释如何使用它们。端点可以提供资源更新，也可以提供发布之类的操作。

## 设计选择

### 描述与发现

从产品入口链接到 API 地址、支持的版本、描述和身份验证指导。[RFC 9727](https://www.rfc-editor.org/rfc/rfc9727.html) 支持 API 目录，但客户端仍需要相应的发现和授权能力。

解释省略、null、空值和经过遮蔽的值；仅靠 schema 无法区分“未知”和“未返回”。审查从 OpenAPI 生成的工具是否具有有用的边界、名称、响应大小和授权方式。

### 错误与当前状态

[Problem Details](https://www.rfc-editor.org/rfc/rfc9457.html) 用 `type` 标识问题，用 `detail` 解释本次情况。恢复应依据定义明确的字段，而不是解析叙述文字。

`If-Match` 不满足通常返回 412；其他业务冲突可以使用 409。GET 可以返回 200，而工作记录却报告失败：请求成功与工作成功不同。

发生并发变化时，分页游标不保证快照一致性。说明排序和边界，让调用方能遍历变化中的集合。字段裁剪应保留下一步所需的标识符和修订版本。

### 重复、条件与持续工作

区分以下机制：

| 机制 | 解决什么问题 | 仍需回答的问题 |
| --- | --- | --- |
| 幂等方法语义 | 重复执行预期效果 | 这一次尝试是否完成，现在能获得什么响应？ |
| 服务定义的去重键 | 同一逻辑操作的重复尝试 | 范围、保留期和参数规则是什么？ |
| 条件写入 | 基于此前观察的修订版本执行操作 | 调用方如何解决冲突？ |
| 工作标识 | 跟踪超出一次请求的执行 | 哪些效果和待定事项在中断后保留？ |

[Stripe](https://docs.stripe.com/api/idempotent_requests) 可以保留第一次结果，包括错误；比较复用键时的参数；并在保留期后清理键。这些是该提供方的特定保证。每次重试都换新键，会使同一逻辑提交的恢复失效。

对于异步工作，保留状态资源。对于流和 webhook，定义访问、交付和刷新行为，并在相关时说明顺序和重复处理。除非契约另有说明，请求超时不会取消远程工作。

### 身份验证与产出物交付

使用服务文档规定的凭证流程。在资源隐藏策略允许的范围内，解释身份验证和权限失败。不要将可复用的账户凭证放进资源 URL。

[S3 预签名 URL](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html) 使持有者获得范围限定的产出物访问权限，包括在有效期内重复使用。底层凭证过期可能缩短其有效期。

将这些链接视为敏感信息。需要长期引用时，使用对象标识与经过授权的获取方式。支持此能力的宿主可以通过不透明句柄，将访问材料保留在模型上下文之外。大型产出物可以使用独立获取路径，避免在每次响应中重复内容。

## 示例

以下[报告服务](../../examples/reporting-service.md)交互仅作示例，不规定端点路径。

| 步骤 | 交互 | 含义 |
| --- | --- | --- |
| 读取 | GET 草稿，获得强 ETag | 调用方看到一个已标识的修订版本 |
| 修改 | 在 `If-Match` 中携带该值提交更新 | 仅当所观察的修订版本仍匹配时应用更新 |
| 冲突 | 收到 412 和文档规定的问题信息 | 重新读取并解决冲突；不要盲目重试基于旧版本的写入 |
| 提交工作 | 收到异步接受响应与状态引用 | 工作已存在，结果尚未完成 |
| 检查 | GET 状态与产出物引用 | 区分领域结果与 HTTP 成功 |

下方是该冲突的一种可能的 Problem Details 响应体。`about:blank` 使用 HTTP 状态的含义；应用需要更具体的问题类型时，可以自行定义并说明相应的类型 URI。

```json
{
  "type": "about:blank",
  "title": "Precondition Failed",
  "status": 412,
  "detail": "The draft changed after it was read. Retrieve the current revision before submitting an update."
}
```

使用方根据状态和条件写入契约恢复，无需解析 `detail`。

## 验证

| 重点 | 可尝试的用例 |
| --- | --- |
| 描述与访问 | 首次访问、过期凭证、适用时错误的目标受众或范围、受保护的描述、私有产出物获取 |
| 请求与响应 | 省略与 null 的区别；类型明确的失败；并发变化时的分页；有界结果 |
| 效果与持续工作 | 写入提交后响应丢失；复用键时输入改变；去重记录过期；过期 ETag；更新交付中断 |

应用与任务证据见[评估流程](../evaluation.md)。

## 来源与相关主题

- [OpenAPI](https://spec.openapis.org/oas/latest.html)、[RFC 9110 HTTP semantics](https://www.rfc-editor.org/rfc/rfc9110.html) 和 [RFC 9457 Problem Details](https://www.rfc-editor.org/rfc/rfc9457.html)。
- [RFC 9727 API catalogs](https://www.rfc-editor.org/rfc/rfc9727.html)。
- [Stripe idempotent requests](https://docs.stripe.com/api/idempotent_requests) 和 [S3 presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html)：提供方特定的契约，不是通用默认值。
- 相关主题：[CLI](cli.md)、[MCP](mcp.md)、[SDK](sdk.md)和[呈现](presentation.md)。
