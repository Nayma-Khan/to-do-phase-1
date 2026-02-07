"""
Command handlers for the Console Todo App.

This module implements the logic for handling different CLI commands.
"""

import sys
from src.services.todo_service import TodoService
from src.utils.display import format_task_list, format_success_message
from src.utils.errors import handle_error, create_validation_error, create_not_found_error
from src.repository.todo_repository import TodoRepository


# Global service instance - in a real app, you'd want to manage this more carefully
todo_service = TodoService()


def handle_command(args):
    """
    Handle a parsed command from the CLI.

    Args:
        args: Parsed arguments from argparse

    Returns:
        int: Exit code (0 for success, 1 for error)
    """
    command = args.command

    if command == 'add':
        return handle_add_command(args)
    elif command == 'list':
        return handle_list_command(args)
    elif command == 'update':
        return handle_update_command(args)
    elif command == 'delete':
        return handle_delete_command(args)
    elif command == 'complete':
        return handle_complete_command(args)
    elif command == 'incomplete':
        return handle_incomplete_command(args)
    elif command == 'help':
        return handle_help_command(args)
    elif command == 'quit' or command == 'exit':
        return handle_exit_command(args)
    else:
        print("Unknown command. Use 'help' to see available commands.")
        return 1


def handle_add_command(args):
    """
    Handle the 'add' command to add a new task.

    Args:
        args: Parsed arguments

    Returns:
        int: Exit code (0 for success, 1 for error)
    """
    try:
        title = ' '.join(args.title)
        task_id = todo_service.add_task(title)
        print(format_success_message("added", task_id))
        return 0
    except Exception as e:
        return handle_error(e)


def handle_list_command(args):
    """
    Handle the 'list' command to display all tasks.

    Args:
        args: Parsed arguments

    Returns:
        int: Exit code (0 for success, 1 for error)
    """
    try:
        tasks = todo_service.get_all_tasks()
        formatted_list = format_task_list(tasks)
        print(formatted_list)
        return 0
    except Exception as e:
        return handle_error(e)


def handle_update_command(args):
    """
    Handle the 'update' command to update a task.

    Args:
        args: Parsed arguments

    Returns:
        int: Exit code (0 for success, 1 for error)
    """
    try:
        task_id = args.id
        title = ' '.join(args.title)

        success = todo_service.update_task(task_id, title)
        if success:
            print(format_success_message("updated", task_id))
            return 0
        else:
            print(f"Error: Task with ID {task_id} not found", file=sys.stderr)
            return 1
    except Exception as e:
        return handle_error(e)


def handle_delete_command(args):
    """
    Handle the 'delete' command to remove a task.

    Args:
        args: Parsed arguments

    Returns:
        int: Exit code (0 for success, 1 for error)
    """
    try:
        task_id = args.id

        success = todo_service.delete_task(task_id)
        if success:
            print(format_success_message("deleted", task_id))
            return 0
        else:
            print(f"Error: Task with ID {task_id} not found", file=sys.stderr)
            return 1
    except Exception as e:
        return handle_error(e)


def handle_complete_command(args):
    """
    Handle the 'complete' command to mark a task as complete.

    Args:
        args: Parsed arguments

    Returns:
        int: Exit code (0 for success, 1 for error)
    """
    try:
        task_id = args.id

        success = todo_service.toggle_task_completion(task_id)
        if success:
            print(format_success_message("marked complete", task_id))
            return 0
        else:
            print(f"Error: Task with ID {task_id} not found", file=sys.stderr)
            return 1
    except Exception as e:
        return handle_error(e)


def handle_incomplete_command(args):
    """
    Handle the 'incomplete' command to mark a task as incomplete.

    Args:
        args: Parsed arguments

    Returns:
        int: Exit code (0 for success, 1 for error)
    """
    try:
        task_id = args.id

        # Get the current task to check its status
        task = todo_service.get_task_by_id(task_id)
        if task is None:
            print(f"Error: Task with ID {task_id} not found", file=sys.stderr)
            return 1

        # If already incomplete, no need to change
        if not task['completed']:
            print(f"Task {task_id} is already incomplete")
            return 0

        # Toggle to make it incomplete
        success = todo_service.toggle_task_completion(task_id)
        if success:
            print(format_success_message("marked incomplete", task_id))
            return 0
        else:
            print(f"Error: Task with ID {task_id} not found", file=sys.stderr)
            return 1
    except Exception as e:
        return handle_error(e)


def handle_help_command(args):
    """
    Handle the 'help' command to show available commands.

    Args:
        args: Parsed arguments

    Returns:
        int: Exit code (0 for success, 1 for error)
    """
    try:
        # The parser's help will be shown by main() when no command is provided
        # So we'll just print a message here
        print("Showing help...")
        # We'll rely on argparse to show the help by calling the parser
        # Since this function is called after parsing, we'll print a custom help
        print("""
Console Todo App - Available Commands:

add "task title"     - Add a new task to the todo list
list                 - Display all tasks in the todo list
update <id> "title"  - Update the title of an existing task
delete <id>          - Remove a task from the todo list
complete <id>        - Mark a task as completed
incomplete <id>      - Mark a task as incomplete
help                 - Show this help message
quit/exit            - Exit the application

Examples:
  python main.py add "Buy groceries"
  python main.py list
  python main.py complete 1
  python main.py update 1 "Buy weekly groceries"
  python main.py delete 1
        """)
        return 0
    except Exception as e:
        return handle_error(e)


def handle_exit_command(args):
    """
    Handle the 'quit' or 'exit' command to exit the application.

    Args:
        args: Parsed arguments

    Returns:
        int: Exit code (0 for success, 1 for error)
    """
    try:
        print("Exiting the application...")
        return 0
    except Exception as e:
        return handle_error(e)