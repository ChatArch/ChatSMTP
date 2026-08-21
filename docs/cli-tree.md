# CLI 树

`ChatSMTP` 当前是 root-only CLI，并使用共享的 `chatstyle.add_tree_option()` 从真实注册的 Click command surface 生成命令树：

- `chatsmtp --tree` 显示参数签名，适合接口审查。
- `chatsmtp --tree-brief` 保留同一组节点和说明，但省略参数签名。

当前没有业务命令参数，因此完整和简洁视图相同。这个页面不能手写未来命令。

## 完整命令树

```text
chatsmtp
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

## 简洁命令树

```text
chatsmtp
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

## 状态契约

- `chatsmtp --help` 必须暴露 `--tree` 和 `--tree-brief`。
- `chatsmtp --tree` 必须 exit 0，并显示带参数签名的真实注册面。
- `chatsmtp --tree-brief` 必须 exit 0，并显示省略参数签名的同一注册面。
- `chatsmtp hello` 必须失败；`hello` 不是业务命令。
- 当前入口不会发送邮件、写入远端状态或打印 `CHATSMTP_API_KEY`。
- 新增 SMTP 能力时，先增加可复用 Python API，再新增 CLI command，并同步完整/简洁树。
