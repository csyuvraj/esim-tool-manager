from rich.console import Console
from rich.table import Table

from tool_manager.models import ToolRegistry

console = Console()


def list_tools() -> None:
    registry = ToolRegistry()

    table = Table(title="Supported Tools")
    table.add_column("Tool")
    table.add_column("Binary")

    for tool in registry.all():
        table.add_row(tool.display_name, tool.binary_name)

    console.print(table)