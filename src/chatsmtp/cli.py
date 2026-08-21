"""CLI entrypoint for chatsmtp."""

from __future__ import annotations

import click
from chatstyle import add_tree_option

from chatsmtp import __version__


@click.group(name="chatsmtp", invoke_without_command=True)
@click.version_option(__version__, prog_name="chatsmtp")
@add_tree_option(renderer_options={"root_name": "chatsmtp"})
@click.pass_context
def main(ctx: click.Context) -> None:
    """ChatArch SMTP tooling package."""
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())


if __name__ == "__main__":
    main()
