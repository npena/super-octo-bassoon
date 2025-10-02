"""Command line interface for super-octo-bassoon."""

import click

from .hello import get_version, hello_world


@click.command()
@click.option(
    "--name",
    "-n",
    help="Name to greet",
    default=None,
)
@click.option(
    "--version",
    "-v",
    is_flag=True,
    help="Show version and exit",
)
def main(name: str, version: bool) -> None:
    """Super Octo Bassoon - A hello world CLI application."""
    if version:
        click.echo(f"super-octo-bassoon version {get_version()}")
        return
    # Generate greeting (logic in hello module for testability)
    greeting = hello_world(name)
    click.echo(greeting)


if __name__ == "__main__":
    main()
