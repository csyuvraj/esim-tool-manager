"""
Configuration for ETM.
"""

from dataclasses import dataclass


@dataclass
class AppConfig:
    """Application configuration."""

    app_name: str = "eSim Tool Manager"
    version: str = "0.1.0"
    log_level: str = "INFO"