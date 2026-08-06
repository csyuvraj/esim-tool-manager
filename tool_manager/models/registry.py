"""
Tool registry.
"""

import yaml

from tool_manager.models.tool import Tool


class ToolRegistry:
    """Loads and stores supported tools."""

    def __init__(self, path: str = "tool_manager/data/tools.yaml") -> None:
        self._tools: dict[str, Tool] = {}

        with open(path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

        for name, info in data.items():
            self.register(
                Tool(
                    name=name,
                    display_name=info["display_name"],
                    binary_name=info["binary_name"],
                )
            )

    def register(self, tool: Tool) -> None:
        self._tools[tool.name] = tool

    def get(self, name: str) -> Tool:
        return self._tools[name]

    def all(self) -> list[Tool]:
        return list(self._tools.values())