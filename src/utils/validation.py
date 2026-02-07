"""
Input validation utilities for the Console Todo App.

This module provides validation functions for various inputs in the application.
"""


def validate_title(title: str) -> bool:
    """
    Validate a todo title.

    Args:
        title (str): The title to validate

    Returns:
        bool: True if the title is valid

    Raises:
        ValueError: If the title is invalid
    """
    if not isinstance(title, str):
        raise ValueError("Title must be a string")

    if not title.strip():
        raise ValueError("Title cannot be empty or whitespace only")

    if len(title.strip()) == 0:
        raise ValueError("Title cannot be empty")

    return True


def validate_task_id(task_id: int) -> bool:
    """
    Validate a task ID.

    Args:
        task_id (int): The task ID to validate

    Returns:
        bool: True if the task ID is valid

    Raises:
        ValueError: If the task ID is invalid
    """
    if not isinstance(task_id, int):
        raise ValueError("Task ID must be an integer")

    if task_id <= 0:
        raise ValueError("Task ID must be a positive integer")

    return True