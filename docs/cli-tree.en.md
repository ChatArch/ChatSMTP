# CLI Tree

`ChatSMTP` is currently a root-only CLI and uses the shared `chatstyle.add_tree_option()` runtime to render its real registered Click command surface:

- `chatsmtp --tree` includes parameter signatures for interface review.
- `chatsmtp --tree-brief` preserves the same nodes and descriptions while omitting signatures.

There are no business-command parameters yet, so the full and brief views are identical. This page must not invent future commands.

## Full command tree

```text
chatsmtp
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

## Brief command tree

```text
chatsmtp
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

## Status Contract

- `chatsmtp --help` must expose `--tree` and `--tree-brief`.
- `chatsmtp --tree` must exit 0 and show the registered surface with signatures.
- `chatsmtp --tree-brief` must exit 0 and show the same surface without signatures.
- `chatsmtp hello` must fail; `hello` is not a business command.
- The current entries do not send mail, write remote state, or print `CHATSMTP_API_KEY`.
- Future SMTP capabilities must add reusable Python APIs first, then CLI commands, and then update both trees.
