"""
In-memory TodoList repository for the Console Todo App.

This module implements the repository pattern for storing and managing
Todo objects in memory using a list of dictionaries.
"""

from typing import List, Dict, Optional
from src.models.todo import Todo


class TodoRepository:
    """
    In-memory repository for managing Todo objects.

    This repository stores Todo objects in a list and provides methods
    for CRUD operations on the todo items.
    """

    def __init__(self):
        """Initialize the repository with an empty list of todos."""
        self._todos: List[Todo] = []
        self._next_id = 1

    def add_todo(self, title: str) -> int:
        """
        Add a new todo to the repository.

        Args:
            title (str): The title of the new todo

        Returns:
            int: The ID of the newly created todo
        """
        new_todo = Todo(id=self._next_id, title=title, completed=False)
        self._todos.append(new_todo)
        todo_id = self._next_id
        self._next_id += 1
        return todo_id

    def get_all_todos(self) -> List[Todo]:
        """
        Retrieve all todos from the repository.

        Returns:
            List[Todo]: A list of all Todo objects
        """
        return self._todos.copy()

    def get_todo_by_id(self, todo_id: int) -> Optional[Todo]:
        """
        Find a specific todo by its ID.

        Args:
            todo_id (int): The ID of the todo to find

        Returns:
            Optional[Todo]: The Todo object if found, None otherwise
        """
        for todo in self._todos:
            if todo.id == todo_id:
                return todo
        return None

    def update_todo(self, todo_id: int, title: str) -> bool:
        """
        Update the title of an existing todo.

        Args:
            todo_id (int): The ID of the todo to update
            title (str): The new title for the todo

        Returns:
            bool: True if update was successful, False if todo not found
        """
        for todo in self._todos:
            if todo.id == todo_id:
                todo.title = title
                return True
        return False

    def delete_todo(self, todo_id: int) -> bool:
        """
        Remove a todo from the repository.

        Args:
            todo_id (int): The ID of the todo to delete

        Returns:
            bool: True if deletion was successful, False if todo not found
        """
        for i, todo in enumerate(self._todos):
            if todo.id == todo_id:
                del self._todos[i]
                return True
        return False

    def toggle_completion(self, todo_id: int) -> bool:
        """
        Toggle the completion status of a todo.

        Args:
            todo_id (int): The ID of the todo to update

        Returns:
            bool: True if toggle was successful, False if todo not found
        """
        for todo in self._todos:
            if todo.id == todo_id:
                todo.completed = not todo.completed
                return True
        return False

    def get_next_id(self) -> int:
        """
        Get the next available ID for a new todo.

        Returns:
            int: The next available ID
        """
        return self._next_id