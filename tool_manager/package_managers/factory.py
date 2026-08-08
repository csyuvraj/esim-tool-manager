"""
Package manager factory.
"""

import platform

from tool_manager.package_managers.apt import AptManager
from tool_manager.package_managers.base import PackageManager


class DummyPackageManager(PackageManager):
    """Fallback manager for unsupported operating systems."""

    def install(self, tool):
        from tool_manager.models import InstallResult

        return InstallResult(
            False,
            "Installation is currently supported only on Ubuntu/Linux.",
        )

    def uninstall(self, tool):
        return False

    def get_installed_version(self, tool):
        return None

    def is_available(self):
        return False

    def update_system(self):
        from tool_manager.models import InstallResult
        return InstallResult(
            False,
            "System update is currently supported only on Ubuntu/Linux.",
        )


def get_package_manager() -> PackageManager:
    system = platform.system()

    if system == "Linux":
        return AptManager()

    return DummyPackageManager()
