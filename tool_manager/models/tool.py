"""
Tool model for ETM.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Tool:
    """Represents a tool managed by ETM."""

    name: str
    display_name: str
    binary_name: str
    installed_version: Optional[str] = None
    latest_version: Optional[str] = None
    installed: bool = False