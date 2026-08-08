import shutil
import subprocess
from typing import Optional

from tool_manager.models import InstallResult, Tool
from tool_manager.package_managers.base import PackageManager


class AptManager(PackageManager):

    def install(self, tool: Tool) -> InstallResult:
        command = ["sudo", "apt", "install", "-y", tool.binary_name]

        try:
            subprocess.run(command, check=True)
            return InstallResult(True, "Installed successfully.")
        except subprocess.CalledProcessError:
            return InstallResult(False, "Installation failed.")

    def uninstall(self, tool: Tool) -> bool:
        command = ["sudo", "apt", "remove", "-y", tool.binary_name]

        try:
            subprocess.run(command, check=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def get_installed_version(self, tool: Tool) -> Optional[str]:
        if shutil.which(tool.binary_name):
            try:
                result = subprocess.run(
                    [tool.binary_name, "--version"],
                    capture_output=True,
                    text=True,
                )
                return result.stdout.splitlines()[0]
            except Exception:
                return None

        return None

    def is_available(self) -> bool:
        return shutil.which("apt") is not None

    def update_system(self) -> InstallResult:
        try:
            subprocess.run(["sudo", "apt", "update"], check=True)
            subprocess.run(["sudo", "apt", "upgrade", "-y"], check=True)
            return InstallResult(True, "System updated successfully.")
        except subprocess.CalledProcessError:
            return InstallResult(False, "System update failed.")
