import shutil
import subprocess

from rich.console import Console

from tool_manager.models import InstallResult, ToolRegistry
from tool_manager.package_managers.factory import get_package_manager

console = Console()


def uninstall_tool(name: str) -> InstallResult:
    registry = ToolRegistry()

    tool = registry.get(name)

    if not shutil.which(tool.binary_name):
        return InstallResult(True, f"{tool.display_name} is not installed.")

    manager = get_package_manager()

    return InstallResult(
        manager.uninstall(tool),
        f"{tool.display_name} uninstall attempted.",
    )