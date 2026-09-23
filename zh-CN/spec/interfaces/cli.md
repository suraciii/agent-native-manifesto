# 命令行接口

[English](../../../spec/interfaces/cli.md) | 简体中文

CLI 通过进程提供本地或远程能力。本指南应用[核心要求](../core.md)；选择访问路径时，参阅[接口概览](../interfaces.md)。

## 作用与适用条件

宿主需要可执行程序、适当权限，以及捕获输出和退出状态的方式。说明受支持环境的安装要求。Shell 工具可以转换数据，而不必把全部数据加载到模型上下文中。如果宿主不能安装或运行命令，可考虑远程 HTTP 或 MCP 访问。

## 设计选择

### 帮助、schema 与方法

根命令帮助标明命令组，子命令帮助解释具体操作。让 `--help` 不产生业务效果，并使基本的本地帮助在没有网络或身份验证时仍可使用。小型工具可以把完整契约放在帮助中。较大的工具可以链接到参考资料或机器可读描述。[Skill 与指南](instructions.md)解释方法，不复制参数定义。

### 非交互使用

通过参数、文件或 stdin 接收任务输入。在非交互模式下，报告缺失输入或提供明确的人工交接，不要等待隐藏提示。登录和必须由人作出的决定可以通过浏览器或独立流程完成；说明调用方如何得知交接完成。应用的访问策略仍然适用。

### 人读输出与脚本输出

[GitHub CLI](https://cli.github.com/manual/gh_help_formatting) 提供 `--json` 字段选择和 `--jq` 转换。[Git status](https://git-scm.com/docs/git-status) 提供 porcelain 输出及以 NUL 分隔的路径。结构化记录和原生流都可使用；二进制或文本产出物无需 JSON 包装。

说明结果与错误通道。机器输出应避免终端装饰，将结果和错误记录与诊断信息分开。根据明确的契约，错误记录可以使用 stdout 或 stderr。

对于流，定义记录边界和完成条件：前缀可解析，不代表导出成功。文件名可能包含换行时，按换行拆分并不安全。

### Shell 行为也是接口的一部分

直接调用进程时，优先使用参数数组。通过 shell 调用时，为字面数据正确加引号，并将其与可执行语法分开。复杂输入使用文件或 stdin；解释 `@`、通配符和 `--` 等特殊字符。

在 [gh api](https://cli.github.com/manual/gh_api) 中，字段选项会把默认方法从 GET 改为 POST。此时查询需要明确指定方法；其他 CLI 可能不同。

提供 CLI 版本、目标服务、当前项目、身份验证范围和相关环境信息，同时避免泄露秘密。工作目录和环境变量可能改变命令含义。使用受保护的凭证机制；命令行参数可能在进程列表或历史记录中暴露秘密。

### 本地退出与远程效果

退出状态为零可能只确认已提交，远程工作仍在等待中。返回工作标识及查询状态的方法。客户端终止可能只结束对该工作的观察。管道的消费端也可能在生产端完成前停止。独立定义恢复方式，不要依赖最后打印的一行。

对于批次，说明效果是原子的，还是逐项产生的，并报告部分结果。CLI 包装 SDK 时，每个逻辑操作需要统一的重试策略。外层重试可能倍增尝试次数或创建新操作；见 [SDK 重试责任](sdk.md#重试责任)。

## 示例

以下只读命令需要已安装并完成身份验证的 GitHub CLI，以及网络连接。结果来自实时数据。

```sh
gh repo view cli/cli --json nameWithOwner,defaultBranchRef
```

较底层的客户端通过显式 HTTP 请求返回相同字段：

```sh
gh api --method GET repos/cli/cli --jq '{nameWithOwner: .full_name, defaultBranchRef: {name: .default_branch}}'
```

第一个命令隐藏端点映射，第二个将其显式呈现。两者访问同一产品。本地执行与中断见[图像工具](../../examples/local-tool.md)。

## 验证

| 重点 | 可尝试的用例 |
| --- | --- |
| 帮助与环境 | 全新安装；离线读取根命令和子命令帮助；错误项目或端点；版本识别 |
| 非交互使用 | stdin 已关闭；输入缺失；数据包含空格、引号或选项前导字符；身份验证交接 |
| 结果与状态 | 机器输出伴有警告；结构化失败；已接受的远程工作；流被截断及非零退出 |
| 中断与组合 | 响应丢失；远程接受后客户端终止；批次部分完成；多层重试 |

任务试验和设置成本见[评估流程](../evaluation.md)。

## 来源与相关主题

- [Command Line Interface Guidelines](https://clig.dev/)：帮助、非交互操作、输出和进程约定。
- [GitHub CLI formatting](https://cli.github.com/manual/gh_help_formatting) 和 [API command](https://cli.github.com/manual/gh_api)：具体的字段选择、请求构造和分页行为。
- [Git status](https://git-scm.com/docs/git-status)：稳定的 porcelain 输出及文件名边界格式。
- 相关主题：[HTTP API](http-api.md)、[SDK](sdk.md)、[说明文档](instructions.md)和[文件与产出物](files-and-artifacts.md)。
