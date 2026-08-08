import typer
from rich.console import Console

from tool_manager import __version__
from tool_manager.doctor import run_doctor
from tool_manager.install import install_tool
from tool_manager.list_tools import list_tools
from tool_manager.logs import show_logs
from tool_manager.update import update_tools
from tool_manager.version import version_tool
from tool_manager.uninstall import uninstall_tool

app = typer.Typer(help="eSim Tool Manager")
console = Console()


@app.command()
def doctor():
    run_doctor()


@app.command()
def version(tool: str = ""):
    if tool:
        version_tool(tool)
    else:
        typer.echo(__version__)


@app.command()
def install(tool: str):
    result = install_tool(tool)
    console.print(result.message)


@app.command()
def uninstall(tool: str):
    result = uninstall_tool(tool)
    console.print(result.message)


@app.command()
def list():
    list_tools()


@app.command()
def update():
    update_tools()


@app.command()
def logs():
    show_logs()
