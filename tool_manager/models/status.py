"""
Status model for ETM.
"""

from dataclasses import dataclass


@dataclass
class ToolStatus:
    """Represents the current status of a tool."""

    installed: bool
    version: str = "Unknown"
    healthy: bool = False