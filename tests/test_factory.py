import pytest
from unittest.mock import patch
from tool_manager.package_managers.factory import get_package_manager

@patch("tool_manager.package_managers.factory.platform.system")
def test_get_package_manager_linux(mock_system):
    mock_system.return_value = "Linux"
    pm = get_package_manager()
    assert pm.__class__.__name__ == "AptManager"

@patch("tool_manager.package_managers.factory.platform.system")
def test_get_package_manager_mac(mock_system):
    mock_system.return_value = "Darwin"
    pm = get_package_manager()
    assert pm.__class__.__name__ == "DummyPackageManager"

@patch("tool_manager.package_managers.factory.platform.system")
def test_get_package_manager_windows(mock_system):
    mock_system.return_value = "Windows"
    pm = get_package_manager()
    assert pm.__class__.__name__ == "DummyPackageManager"
