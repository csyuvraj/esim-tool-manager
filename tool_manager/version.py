import shutil
import subprocess

from rich.console import Console

from tool_manager.models import ToolRegistry

console = Console()


def version_tool(name: str) -> None:
    registry = ToolRegistry()

    tool = registry.get(name)

    if not shutil.which(tool.binary_name):
        console.print(f"{tool.display_name} is not installed.")
        return

    subprocess.run([tool.binary_name, "--version"])