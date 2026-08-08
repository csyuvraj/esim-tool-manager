"""
Installation module.
"""

import shutil
import subprocess

from rich.console import Console

from tool_manager.models import InstallResult, ToolRegistry
from tool_manager.package_managers.factory import get_package_manager

console = Console()


def install_tool(name: str) -> InstallResult:
    registry = ToolRegistry()
    tool = registry.get(name)

    if shutil.which(tool.binary_name):
        return InstallResult(True, f"[yellow]{tool.display_name} is already installed.[/yellow]")

    console.print(f"Installing {tool.display_name}...\n")
    manager = get_package_manager()
    result = manager.install(tool)

    if result.success:
        return InstallResult(True, "[green]✓ Installed successfully.[/green]")
    
    return InstallResult(False, f"[red]✗ {result.message}[/red]")
