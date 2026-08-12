# CLI Tree

`chatsmtp --tree` is generated from the real registered Click command surface. `ChatSMTP` currently exposes root-level package information entries only and no business subcommands; a template `hello` command is not part of the public interface.

## Top-level command

```text
chatsmtp  # ChatArch SMTP tooling package
├── --help  # show command help
├── --version  # show the installed package version
└── --tree  # show this CLI tree
```

## Status Contract

- `chatsmtp --help` must expose `--tree`.
- `chatsmtp --tree` must exit 0 and list only real registered commands/options.
- `chatsmtp hello` must fail; `hello` is not a business command.
- Future SMTP capabilities must add reusable Python APIs first, then CLI commands, and then update this page.
