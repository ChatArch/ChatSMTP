# Development Guide

## CLI Rules

- Use `chatstyle>=0.2.0,<0.3.0` as the canonical CLI interaction and tree runtime.
- Keep the public root explicitly named `chatsmtp`; expose `--version`, `--tree`, and `--tree-brief`.
- Use ChatStyle `add_tree_option()` and the registered Click renderer instead of a package-local tree implementation.
- Keep the typed `chatsmtp.config` provider registered through `chatenv.configs`; use `chatenv>=0.2.10,<0.3.0` and ChatEnv-managed profile/storage paths.
- Prefer `CommandSchema`, `CommandField`, `add_interactive_option()`, and `resolve_command_inputs()` for future interactive commands.
- Prefer reusable Python APIs before CLI wiring for new SMTP capabilities.
- Missing required args should auto-enter interactive mode only when recoverable and explicitly designed.
- `-i` forces interactive mode; `-I` disables prompting and must fail fast.
- Prompt defaults must match actual execution defaults.
- Sensitive values must stay masked in prompts and summaries.
- Prefer lazy imports in CLI wiring and keep implementation imports local when possible.

## Docs and Tests

- Use doc-first CLI testing.
- Put real CLI coverage under `tests/cli-tests/`.
- Put mock/fake CLI coverage under `tests/mock-cli-tests/`.
- Keep `README.md`, `docs/`, and `CHANGELOG.md` in sync with user-facing changes.

## Automation

- Keep automation small and reviewable.
- Prefer commands that can run in CI without interactive prompts.
- Ensure generated defaults are safe for local development.
