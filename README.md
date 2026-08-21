<div align="center">
    <a href="https://pypi.python.org/pypi/ChatSMTP">
        <img src="https://img.shields.io/pypi/v/ChatSMTP.svg" alt="PyPI version" />
    </a>
    <a href="https://github.com/ChatArch/ChatSMTP/actions/workflows/ci.yml">
        <img src="https://github.com/ChatArch/ChatSMTP/actions/workflows/ci.yml/badge.svg" alt="Tests" />
    </a>
    <a href="https://arch.gh.wzhecnu.cn/ChatSMTP/">
        <img src="https://img.shields.io/badge/docs-mkdocs-blue.svg" alt="Documentation" />
    </a>
</div>

<div align="center">

[English](README.en.md) | [简体中文](README.md)
</div>

# ChatSMTP

ChatArch SMTP tooling package.

## 快速开始

```bash
pip install -e ".[dev,docs]"
chatsmtp --help
chatsmtp --version
chatsmtp --tree
chatsmtp --tree-brief
python -m pytest -q
mkdocs build --strict
python -m build
```

## CLI 树

ChatSMTP 使用共享的 `chatstyle.add_tree_option()` 从真实注册的 Click command surface 生成完整和简洁命令树。当前 CLI 是 root-only，因此两个视图的节点相同。

```text
chatsmtp
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

## CLI 规范

ChatSMTP 固定使用 `chatstyle>=0.2.0,<0.3.0` 提供 `--tree` / `--tree-brief`，并使用 `chatenv>=0.2.10,<0.3.0`、typed provider registration 和 ChatEnv 管理的 profile/storage 路径。新的 SMTP 能力应优先提供可复用 Python API，再接入 CLI、文档和测试。

- `CommandSchema` / `CommandField` 描述输入。
- `add_interactive_option()` 提供统一 `-i/-I`。
- `resolve_command_inputs()` 统一缺参补问、默认值、TTY 与校验。
- 默认生成 `config.py` 和 `chatenv.configs` entry point，使包可被 ChatEnv 发现；只有明确不需要 ChatEnv 接入时才使用 `--without-chatenv-provider`。

## 目录结构

- `src/`：包源码
- `tests/code-tests/`：代码测试和历史测试迁移
- `tests/cli-tests/`：真实 CLI 测试，doc-first
- `tests/mock-cli-tests/`：mock/fake CLI 测试，doc-first
- `docs/`：长期维护文档，由 mkdocs 构建

## 开发说明

扩展脚手架前，先阅读 `DEVELOP.md` 和 `AGENTS.md`。
