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

## Quick Start

```bash
pip install -e ".[dev,docs]"
chatsmtp --help
chatsmtp --version
chatsmtp --tree
python -m pytest -q
mkdocs build --strict
python -m build
```

## CLI Tree

```text
chatsmtp  # ChatArch SMTP tooling package
├── --help  # show command help
├── --version  # show the installed package version
└── --tree  # show this CLI tree
```

## CLI Contract

This template depends on `chatenv>=0.2.0,<0.3.0`; add a direct `chatstyle` dependency only when a real interactive command needs it. New SMTP capabilities should expose reusable Python APIs before CLI wiring, docs, and tests.

- `CommandSchema` / `CommandField` for inputs.
- `add_interactive_option()` for the shared `-i/-I` switch.
- `resolve_command_inputs()` for missing args, defaults, TTY behavior, and validation.
- Generate `config.py` and a `chatenv.configs` entry point by default so the package is ChatEnv-discoverable; use `--without-chatenv-provider` only when ChatEnv integration is intentionally not needed.

## Layout

- `src/`: package source code
- `tests/code-tests/`: code tests and migrated historical tests
- `tests/cli-tests/`: real CLI tests, doc-first
- `tests/mock-cli-tests/`: mock/fake CLI tests, doc-first
- `docs/`: long-lived project docs built by mkdocs

## Development Notes

See `DEVELOP.md` and `AGENTS.md` before expanding the scaffold.
