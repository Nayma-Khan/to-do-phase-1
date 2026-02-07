"""
Todo data model for the Console Todo App.

This module defines the Todo class which represents a single todo item
with properties: id, title, and completion status.
"""


class Todo:
    """
    Represents a single todo item in the application.

    Attributes:
        id (int): Unique identifier for the task
        title (str): The description of what needs to be done
        completed (bool): Indicates whether the task has been completed
    """

    def __init__(self, id: int, title: str, completed: bool = False):
        """
        Initialize a Todo object.

        Args:
            id (int): Unique identifier for the task
            title (str): The description of what needs to be done
            completed (bool): Whether the task is completed (default: False)
        """
        self.id = id
        self.title = title
        self.completed = completed

    def __repr__(self):
        """String representation of the Todo object."""
        return f"Todo(id={self.id}, title='{self.title}', completed={self.completed})"

    def __eq__(self, other):
        """Check equality between two Todo objects."""
        if not isinstance(other, Todo):
            return False
        return (self.id == other.id and
                self.title == other.title and
                self.completed == other.completed)

    def to_dict(self):
        """Convert the Todo object to a dictionary."""
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Todo object from a dictionary."""
        return cls(
            id=data["id"],
            title=data["title"],
            completed=data.get("completed", False)
        )