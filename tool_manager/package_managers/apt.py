"""
APT package manager.
"""

from tool_manager.models import InstallResult, Tool
from tool_manager.package_managers.base import PackageManager


class AptManager(PackageManager):
    """Ubuntu APT package manager."""

    def install(self, tool: Tool) -> InstallResult:
        return InstallResult(True, f"Installing {tool.display_name} with apt")

    def uninstall(self, tool: Tool) -> bool:
        return True

    def get_installed_version(self, tool: Tool) -> str | None:
        return None

    def is_available(self) -> bool:
        return True