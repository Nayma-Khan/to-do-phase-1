"""
CLI argument parser for the Console Todo App.

This module implements the command-line argument parsing using argparse.
"""

import argparse


def create_parser():
    """
    Create and configure the argument parser for the todo app.

    Returns:
        argparse.ArgumentParser: Configured argument parser
    """
    parser = argparse.ArgumentParser(
        description="Console Todo App - Manage your tasks from the command line",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py add "Buy groceries"
  python main.py list
  python main.py complete 1
  python main.py update 1 "Buy weekly groceries"
  python main.py delete 1
  python main.py help
        """.strip()
    )

    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Add command
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('title', nargs='+', help='The title of the task to add')

    # List command
    list_parser = subparsers.add_parser('list', help='Display all tasks')

    # Update command
    update_parser = subparsers.add_parser('update', help='Update a task')
    update_parser.add_argument('id', type=int, help='The ID of the task to update')
    update_parser.add_argument('title', nargs='+', help='The new title for the task')

    # Delete command
    delete_parser = subparsers.add_parser('delete', help='Delete a task')
    delete_parser.add_argument('id', type=int, help='The ID of the task to delete')

    # Complete command
    complete_parser = subparsers.add_parser('complete', help='Mark a task as complete')
    complete_parser.add_argument('id', type=int, help='The ID of the task to mark complete')

    # Incomplete command
    incomplete_parser = subparsers.add_parser('incomplete', help='Mark a task as incomplete')
    incomplete_parser.add_argument('id', type=int, help='The ID of the task to mark incomplete')

    # Help command
    subparsers.add_parser('help', help='Show this help message')

    # Quit/Exit commands (handled the same way)
    subparsers.add_parser('quit', help='Exit the application')
    subparsers.add_parser('exit', help='Exit the application')

    return parser