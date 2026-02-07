# Data Model: Console Todo App

**Feature**: 001-console-todo
**Created**: 2026-02-07

## Entities

### Todo
**Description**: Represents a single todo item in the application

**Fields**:
- `id`: Integer (required) - Unique identifier for the task
- `title`: String (required) - The description of what needs to be done
- `completed`: Boolean (required) - Indicates whether the task has been completed

**Example**:
```python
{
    "id": 1,
    "title": "Buy groceries",
    "completed": False
}
```

**Validation Rules**:
- `id` must be a positive integer
- `title` must be a non-empty string (1+ characters)
- `completed` must be a boolean value

**State Transitions**:
- `pending` (completed=False) → `completed` (completed=True) when task is marked complete
- `completed` (completed=True) → `pending` (completed=False) when task is marked incomplete

## Collections

### TodoList
**Description**: In-memory collection of Todo items

**Structure**:
- Python list containing Todo objects: `[todo1, todo2, ...]`
- Maintains insertion order of tasks
- Indexed by position for internal operations, but uses ID for user-facing operations

**Operations**:
- Add new todo to the list
- Retrieve all todos
- Find specific todo by ID
- Update specific todo by ID
- Delete specific todo by ID
- Toggle completion status by ID

## Relationships
- TodoList contains multiple Todo instances
- Each Todo has a unique id within the TodoList
- No cross-references between Todo items