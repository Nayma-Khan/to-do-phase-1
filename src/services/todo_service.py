"""
TodoService for the Console Todo App.

This module implements the business logic for managing todos,
including validation and coordination between the repository and other layers.
"""

from typing import List, Dict
from src.repository.todo_repository import TodoRepository
from src.models.todo import Todo
from src.utils.validation import validate_title


class TodoService:
    """
    Service layer for todo operations.

    This service coordinates between the repository and validation logic
    to provide a clean API for todo operations.
    """

    def __init__(self, repository: TodoRepository = None):
        """
        Initialize the TodoService.

        Args:
            repository (TodoRepository): The repository to use for data storage.
                                        If None, creates a new repository.
        """
        self.repository = repository or TodoRepository()

    def add_task(self, title: str) -> int:
        """
        Add a new task to the todo list.

        Args:
            title (str): The title of the task to add

        Returns:
            int: The ID of the newly created task

        Raises:
            ValueError: If the title is invalid
        """
        validate_title(title)
        return self.repository.add_todo(title)

    def get_all_tasks(self) -> List[Dict]:
        """
        Retrieve all tasks from the todo list.

        Returns:
            List[Dict]: A list of task dictionaries with id, title, and completed fields
        """
        todos = self.repository.get_all_todos()
        return [todo.to_dict() for todo in todos]

    def update_task(self, task_id: int, title: str) -> bool:
        """
        Update the title of an existing task.

        Args:
            task_id (int): The ID of the task to update
            title (str): The new title for the task

        Returns:
            bool: True if update was successful, False if task not found

        Raises:
            ValueError: If the new title is invalid
        """
        validate_title(title)
        return self.repository.update_todo(task_id, title)

    def delete_task(self, task_id: int) -> bool:
        """
        Remove a task from the todo list.

        Args:
            task_id (int): The ID of the task to delete

        Returns:
            bool: True if deletion was successful, False if task not found
        """
        return self.repository.delete_todo(task_id)

    def toggle_task_completion(self, task_id: int) -> bool:
        """
        Toggle the completion status of a task.

        Args:
            task_id (int): The ID of the task to update

        Returns:
            bool: True if toggle was successful, False if task not found
        """
        return self.repository.toggle_completion(task_id)

    def get_task_by_id(self, task_id: int) -> Dict:
        """
        Get a specific task by its ID.

        Args:
            task_id (int): The ID of the task to retrieve

        Returns:
            Dict: The task dictionary if found, None otherwise
        """
        todo = self.repository.get_todo_by_id(task_id)
        return todo.to_dict() if todo else None