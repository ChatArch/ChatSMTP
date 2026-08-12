# CLI 树

`chatsmtp --tree` 从真实注册的 Click command surface 生成。当前 `ChatSMTP` 只有根级包信息入口，没有业务子命令；模板 `hello` 命令不属于公开接口。

## 顶层命令

```text
chatsmtp  # ChatArch SMTP tooling package
├── --help  # show command help
├── --version  # show the installed package version
└── --tree  # show this CLI tree
```

## 状态契约

- `chatsmtp --help` 必须暴露 `--tree`。
- `chatsmtp --tree` 必须 exit 0，并只列出真实注册的命令/选项。
- `chatsmtp hello` 必须失败；`hello` 不是业务命令。
- 新增 SMTP 能力时，先增加可复用 Python API，再新增 CLI command，并同步本页。
