"""
Package manager factory.
"""

import platform

from tool_manager.package_managers.apt import AptManager
from tool_manager.package_managers.base import PackageManager


def get_package_manager() -> PackageManager:
    """Return the appropriate package manager."""

    system = platform.system()

    if system == "Linux":
        return AptManager()

    raise RuntimeError(f"Unsupported operating system: {system}")