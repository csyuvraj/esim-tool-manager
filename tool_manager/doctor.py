import platform
import socket
import sys
import subprocess

from rich.console import Console
from rich.table import Table

from tool_manager.models import ToolRegistry
from tool_manager.package_managers.factory import get_package_manager

console = Console()

def get_ver(cmd):
    try:
        out = subprocess.run(cmd, capture_output=True, text=True).stdout.strip().split('\n')[0]
        return f"[green]✓ {out}[/green]" if out else "[red]✗ Not found[/red]"
    except Exception:
        return "[red]✗ Not found[/red]"

def run_doctor() -> None:
    table = Table(title="ETM Doctor")
    table.add_column("Component")
    table.add_column("Version / Status")

    table.add_row("OS", platform.system())
    table.add_row("Python", f"[green]✓ {sys.version.split()[0]}[/green]" if sys.version_info >= (3, 9) else "[red]✗ < 3.9[/red]")
    table.add_row("Git", get_ver(["git", "--version"]))
    table.add_row("APT", get_ver(["apt", "--version"]))

    try:
        socket.create_connection(("1.1.1.1", 53), timeout=2)
        table.add_row("Internet", "[green]✓ Connected[/green]")
    except OSError:
        table.add_row("Internet", "[red]✗ Offline[/red]")

    pm = get_package_manager()
    for tool in ToolRegistry().all():
        ver = pm.get_installed_version(tool)
        table.add_row(tool.display_name, f"[green]✓ {ver}[/green]" if ver else "[red]✗ Not installed[/red]")

    console.print(table)
