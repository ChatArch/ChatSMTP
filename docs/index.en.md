# ChatSMTP Docs

`ChatSMTP` is the ChatArch Python CLI package shell for SMTP tooling. The public CLI currently exposes package metadata and the real command tree only; future SMTP capabilities should start with reusable Python APIs before extending CLI commands, docs, and tests.

<div class="grid cards" markdown>

-   :material-console-line: **CLI Tree**

    ---

    Inspect the current real command surface: [`chatsmtp --tree`](cli-tree.md).

-   :material-email-fast: **SMTP Boundary**

    ---

    The current version is a lightweight entrypoint and does not send mail, store credentials, or connect to SMTP services.

-   :material-shield-check: **Verification Contract**

    ---

    `--tree`, README, MkDocs, and tests must stay synchronized.

</div>

## Quick Start

```bash
pip install ChatSMTP
chatsmtp --version
chatsmtp --tree
```

## Development Verification

```bash
pip install -e ".[dev,docs]"
python -m pytest -q
mkdocs build --strict
python -m build
```
