"""
Command Line Interface for ETM.
"""

import typer

from tool_manager import __version__
from tool_manager.doctor import run_doctor

app = typer.Typer(
    name="etm",
    help="eSim Tool Manager",
)


@app.command()
def doctor() -> None:
    """Run system diagnostics."""
    run_doctor()


@app.command()
def version() -> None:
    """Show ETM version."""
    typer.echo(f"ETM v{__version__}")