from typing import Optional, Annotated
from pathlib import Path

import typer
from loguru import logger

from . import cli, __version__, NAME


def _version(value: bool) -> None:
    if value:
        typer.echo(f"{NAME} {__version__}")
        raise typer.Exit(0)


@cli.callback()
def _all(
    log_file_path: Path = typer.Option(
        Path("~").expanduser() / ".log" / f"{NAME}.log",
        help="Log file path",
    ),
    _version: Annotated[
        Optional[bool],
        typer.Option(
            "--version",
            callback=_version,
            is_eager=True,
        ),
    ] = None,
) -> None:
    logger.remove()
    logger.add(log_file_path)


@cli.command()
def main() -> None:
    """."""


if __name__ == "__main__":
    cli()
