"""
Custom exceptions for ETM.
"""


class ETMError(Exception):
    """Base exception for ETM."""


class ToolNotFoundError(ETMError):
    """Raised when a tool is not found."""


class InstallationError(ETMError):
    """Raised when installation fails."""


class PackageManagerError(ETMError):
    """Raised when package manager fails."""