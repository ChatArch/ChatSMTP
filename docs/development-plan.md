# 能力边界

`ChatSMTP` 当前是 SMTP tooling 的轻量包入口。正式命令只包含根级帮助、版本和真实 CLI 树。

## 当前能力

```text
chatsmtp --version  # 输出安装版本
chatsmtp --tree     # 输出真实 Click command surface
```

## 未在当前版本实现

- SMTP 连接配置。
- 邮件发送、草稿、附件或模板处理。
- 凭据写入、登录或 profile mutation。

## 扩展契约

- 新增实质 CLI 命令前，先实现可 import 的 Python API。
- 涉及 SMTP 凭据时必须使用 ChatEnv/ChatStyle 的敏感字段和遮蔽规则。
- 任何发送邮件或修改远端状态的命令都需要 dry-run / `--apply` 或明确确认边界。
