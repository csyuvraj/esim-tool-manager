"""
Command Line Interface for ETM.
"""

import typer

app = typer.Typer(
    name="etm",
    help="eSim Tool Manager (ETM)",
)


@app.command()
def doctor():
    """Check the system status."""
    typer.echo("Running ETM Doctor...")


@app.command()
def version():
    """Show ETM version."""
    typer.echo("eSim Tool Manager v0.1.0")
    