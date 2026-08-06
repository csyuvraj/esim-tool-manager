"""
Base package manager.
"""

from abc import ABC, abstractmethod

from tool_manager.models import InstallResult, Tool


class PackageManager(ABC):
    """Abstract base class for package managers."""

    @abstractmethod
    def install(self, tool: Tool) -> InstallResult:
        pass

    @abstractmethod
    def uninstall(self, tool: Tool) -> bool:
        pass

    @abstractmethod
    def get_installed_version(self, tool: Tool) -> str | None:
        pass

    @abstractmethod
    def is_available(self) -> bool:
        pass