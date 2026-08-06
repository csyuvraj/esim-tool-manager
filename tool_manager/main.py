"""
Main entry point for the eSim Tool Manager.
"""

from tool_manager import __version__


def main() -> None:
    """Start the application."""
    print("=" * 40)
    print("      eSim Tool Manager (ETM)")
    print(f"           Version {__version__}")
    print("=" * 40)


if __name__ == "__main__":
    main()