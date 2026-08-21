# ChatSMTP 文档

`ChatSMTP` 是 ChatArch SMTP tooling 方向的 Python CLI 包壳。当前公开 CLI 只提供包信息与真实命令树；后续新增 SMTP 能力时，应先落到可复用 Python API，再扩展 CLI、文档和测试。

<div class="grid cards" markdown>

-   :material-console-line: **CLI 树**

    ---

    查看当前真实命令面：[`chatsmtp --tree`](cli-tree.md) / `chatsmtp --tree-brief`。

-   :material-email-fast: **SMTP 边界**

    ---

    当前版本是轻量入口，不发送邮件、不保存凭据、不连接 SMTP 服务。

-   :material-shield-check: **验证契约**

    ---

    `--tree`、`--tree-brief`、README、MkDocs 和测试必须同步更新。

</div>

## 快速开始

```bash
pip install ChatSMTP
chatsmtp --version
chatsmtp --tree
chatsmtp --tree-brief
```

## 开发验证

```bash
pip install -e ".[dev,docs]"
python -m pytest -q
mkdocs build --strict
python -m build
```
