"""
Main entry point.
"""

import typer

from tool_manager.cli import app

main = typer.main.get_command(app)

if __name__ == "__main__":
    main()