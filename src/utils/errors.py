"""
Error handling framework for the Console Todo App.

This module defines custom exceptions and error handling utilities.
"""


class ValidationError(Exception):
    """
    Exception raised for validation errors in the application.
    """
    pass


class NotFoundError(Exception):
    """
    Exception raised when a requested resource is not found.
    """
    pass


def handle_error(error: Exception) -> int:
    """
    Handle an error by printing an appropriate message and returning an exit code.

    Args:
        error (Exception): The error to handle

    Returns:
        int: The exit code to use (1 for errors, 0 for success)
    """
    if isinstance(error, ValidationError):
        print(f"Error: {error}", file=__import__('sys').stderr)
    elif isinstance(error, NotFoundError):
        print(f"Error: {error}", file=__import__('sys').stderr)
    else:
        print(f"Error: {error}", file=__import__('sys').stderr)

    return 1


def create_validation_error(message: str) -> ValidationError:
    """
    Create a validation error with the given message.

    Args:
        message (str): The error message

    Returns:
        ValidationError: A new ValidationError instance
    """
    return ValidationError(message)


def create_not_found_error(message: str) -> NotFoundError:
    """
    Create a not found error with the given message.

    Args:
        message (str): The error message

    Returns:
        NotFoundError: A new NotFoundError instance
    """
    return NotFoundError(message)