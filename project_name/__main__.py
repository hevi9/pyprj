from typing import Optional, Annotated

import typer

from . import app, __version__


def _version(value: bool) -> None:
    if value:
        typer.echo(f"creat {__version__}")
        raise typer.Exit(0)


@app.callback()
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
    app()
