import pytest
from unittest.mock import patch, mock_open
from tool_manager.models import Tool, ToolRegistry

def test_tool_model_defaults():
    tool = Tool(name="test", binary_name="test_bin", display_name="Test Tool")
    assert tool.name == "test"
    assert tool.binary_name == "test_bin"
    assert tool.display_name == "Test Tool"
    assert tool.installed is False
    assert tool.installed_version is None
    assert tool.latest_version is None

@patch("builtins.open", new_callable=mock_open, read_data="dummy")
@patch("yaml.safe_load")
def test_tool_registry_functionality(mock_yaml_load, mock_file):
    # Match the dictionary structure expected by ToolRegistry.__init__
    mock_yaml_load.return_value = {
        "ngspice": {"display_name": "Ngspice", "binary_name": "ngspice"},
        "kicad": {"display_name": "KiCad", "binary_name": "kicad"}
    }
    
    registry = ToolRegistry()
    tools = registry.all()
    
    # Test all()
    assert len(tools) == 2
    tool_names = [t.name for t in tools]
    assert "ngspice" in tool_names
    
    # Test get() success
    kicad = registry.get("kicad")
    assert kicad is not None
    assert kicad.display_name == "KiCad"
    
    # Test get() missing (raises KeyError)
    with pytest.raises(KeyError):
        registry.get("nonexistent")
