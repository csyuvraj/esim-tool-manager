import pytest
from unittest.mock import patch, MagicMock
from tool_manager.doctor import get_ver

def test_get_ver_success():
    """Test that get_ver correctly parses standard subprocess output."""
    with patch('tool_manager.doctor.subprocess.run') as mock_run:
        mock_run.return_value = MagicMock(stdout="git version 2.34.1\n")
        
        result = get_ver(["git", "--version"])
        
        assert "✓" in result
        assert "git version 2.34.1" in result

def test_get_ver_command_not_found():
    """Test that get_ver handles missing commands gracefully."""
    with patch('tool_manager.doctor.subprocess.run', side_effect=FileNotFoundError):
        result = get_ver(["some_missing_command"])
        
        assert "✗ Not found" in result

def test_get_ver_execution_error():
    """Test that get_ver catches general execution exceptions."""
    with patch('tool_manager.doctor.subprocess.run') as mock_run:
        mock_run.side_effect = Exception("General error")
        
        result = get_ver(["apt", "--version"])
        
        assert "✗ Not found" in result
