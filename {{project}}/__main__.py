from typing import Optional, Annotated

import typer

from . import cli, __version__, NAME


def _version(value: bool) -> None:
    if value:
        typer.echo(f"{NAME} {__version__}")
        raise typer.Exit(0)


@cli.command()
def main(
    _version: Annotated[
        Optional[bool],
        typer.Option(
            "--version",
            callback=_version,
            is_eager=True,
        ),
    ] = None,
) -> None:
    """."""


if __name__ == "__main__":
    cli()
