"""
Result models for ETM.
"""

from dataclasses import dataclass


@dataclass
class InstallResult:
    """Represents the result of an installation."""

    success: bool
    message: str