from typing import Optional

import typer

app = typer.Typer()


def _version(show_and_exit: bool) -> None:
    from . import __version__

    if show_and_exit:
        typer.echo(f"{__package__} {__version__}")
        raise typer.Exit()


@app.command()
def main(
    _version: Optional[bool] = typer.Option(
        None,
        "--version",
        callback=_version,
        is_eager=True,
        help="Show version.",
    ),
) -> None:
    """Usage"""


if __name__ == "__main__":
    app()
