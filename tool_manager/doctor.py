"""
System health checks for ETM.
"""

import platform
import shutil
import socket
import sys

from rich.console import Console
from rich.table import Table

from tool_manager.models import ToolRegistry

console = Console()


def check(mark: bool) -> str:
    return "✅ Yes" if mark else "❌ No"


def run_doctor() -> None:
    """Run system diagnostics."""

    table = Table(title="ETM Doctor")

    table.add_column("Component")
    table.add_column("Status")

    table.add_row("Operating System", platform.system())
    table.add_row("Python >= 3.9", check(sys.version_info >= (3, 9)))
    table.add_row("Git", check(shutil.which("git") is not None))
    table.add_row("Homebrew", check(shutil.which("brew") is not None))
    table.add_row("pip3", check(shutil.which("pip3") is not None))

    try:
        socket.create_connection(("google.com", 80), timeout=2)
        internet = True
    except OSError:
        internet = False

    table.add_row("Internet", check(internet))

    registry = ToolRegistry()

    for tool in registry.all():
        table.add_row(
            tool.display_name,
            check(shutil.which(tool.binary_name) is not None),
        )

    console.print(table)