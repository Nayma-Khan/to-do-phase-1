"""
Display formatting utilities for the Console Todo App.

This module provides functions for formatting and displaying todo items.
"""


def format_task_list(tasks):
    """
    Format a list of tasks for display.

    Args:
        tasks (list): List of task dictionaries with id, title, and completed fields

    Returns:
        str: Formatted string representation of the task list
    """
    if not tasks:
        return "No tasks in your todo list."

    # Create header
    header = f"{'ID':<4} {'Status':<8} {'Title'}"
    separator = "-" * 50

    # Format each task
    task_lines = []
    for task in tasks:
        status = "[x]" if task['completed'] else "[ ]"
        line = f"{task['id']:<4} {status:<8} {task['title']}"
        task_lines.append(line)

    # Combine all parts
    result = [header, separator] + task_lines
    return "\n".join(result)


def format_single_task(task):
    """
    Format a single task for display.

    Args:
        task (dict): Task dictionary with id, title, and completed fields

    Returns:
        str: Formatted string representation of the task
    """
    if not task:
        return "Task not found."

    status = "[x]" if task['completed'] else "[ ]"
    return f"ID: {task['id']}, Status: {status}, Title: {task['title']}"


def format_success_message(operation, task_id=None, details=None):
    """
    Format a success message for an operation.

    Args:
        operation (str): The operation that was performed
        task_id (int, optional): The ID of the affected task
        details (str, optional): Additional details about the operation

    Returns:
        str: Formatted success message
    """
    if task_id is not None:
        return f"Successfully {operation} task {task_id}."
    elif details:
        return f"Successfully {operation}. {details}"
    else:
        return f"Successfully {operation}."