from rich.console import Console
from tool_manager.package_managers.factory import get_package_manager

console = Console()

def update_tools():
    console.print("Updating system packages...")
    pm = get_package_manager()
    result = pm.update_system()
    
    if result.success:
        console.print(f"[green]✓ {result.message}[/green]")
    else:
        console.print(f"[yellow]{result.message}[/yellow]")
