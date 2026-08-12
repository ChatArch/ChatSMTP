# Capability Boundary

`ChatSMTP` is currently a lightweight package entrypoint for SMTP tooling. Formal commands include root-level help, version, and the real CLI tree only.

## Current Capabilities

```text
chatsmtp --version  # print installed version
chatsmtp --tree     # print the real Click command surface
```

## Not Implemented In This Version

- SMTP connection configuration.
- Mail sending, drafts, attachments, or template handling.
- Credential writes, login, or profile mutation.

## Extension Contract

- Add an importable Python API before adding substantive CLI commands.
- SMTP credentials must use ChatEnv/ChatStyle sensitive-field and masking rules.
- Commands that send mail or mutate remote state need dry-run / `--apply` or an explicit confirmation boundary.
