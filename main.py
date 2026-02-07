#!/usr/bin/env python3
"""
Console Todo App - Main Entry Point

This is the main entry point for the Console Todo application.
It provides a command-line interface for managing todo tasks.
"""

import sys
from src.cli.parser import create_parser
from src.cli.command_handlers import handle_command


def main():
    """Main entry point for the application."""
    parser = create_parser()

    if len(sys.argv) == 1:
        parser.print_help()
        return 0

    args = parser.parse_args()

    # Handle the command
    result = handle_command(args)

    return result


if __name__ == "__main__":
    sys.exit(main())