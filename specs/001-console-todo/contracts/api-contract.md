# API Contract: Console Todo App

**Feature**: 001-console-todo
**Created**: 2026-02-07
**Version**: 1.0

## Service Interface: TodoService

### Core Operations

#### add_task(title: str) -> int
**Description**: Adds a new task to the todo list
**Parameters**:
- `title` (string): The description of the task to add
**Returns**: Integer - The ID of the newly created task
**Errors**:
- ValidationError: If title is empty or invalid
**Postcondition**: Task is added to the list with completed=False

#### get_all_tasks() -> List[dict]
**Description**: Retrieves all tasks in the todo list
**Parameters**: None
**Returns**: List of task objects with id, title, and completed fields
**Errors**: None
**Postcondition**: None

#### update_task(task_id: int, title: str) -> bool
**Description**: Updates the title of an existing task
**Parameters**:
- `task_id` (int): The ID of the task to update
- `title` (str): The new title for the task
**Returns**: Boolean - True if update was successful, False if task not found
**Errors**:
- ValidationError: If new title is empty
**Postcondition**: Task title is updated if task exists

#### delete_task(task_id: int) -> bool
**Description**: Removes a task from the todo list
**Parameters**:
- `task_id` (int): The ID of the task to delete
**Returns**: Boolean - True if deletion was successful, False if task not found
**Errors**: None (silently returns False if task doesn't exist)
**Postcondition**: Task is removed from the list if it existed

#### toggle_task_completion(task_id: int) -> bool
**Description**: Toggles the completion status of a task
**Parameters**:
- `task_id` (int): The ID of the task to update
**Returns**: Boolean - True if toggle was successful, False if task not found
**Errors**: None (silently returns False if task doesn't exist)
**Postcondition**: Task completion status is flipped if task exists

## CLI Interface

### Command Format
```
python main.py <command> [arguments]
```

### Available Commands

#### `add "task title"`
**Description**: Adds a new task to the todo list
**Arguments**:
- `task title` (string): The title of the task to add (in quotes if multiple words)
**Example**: `python main.py add "Buy groceries"`

#### `list`
**Description**: Displays all tasks in the todo list
**Arguments**: None
**Example**: `python main.py list`

#### `update <id> "new title"`
**Description**: Updates the title of an existing task
**Arguments**:
- `id` (integer): The ID of the task to update
- `new title` (string): The new title for the task
**Example**: `python main.py update 1 "Updated task title"`

#### `delete <id>`
**Description**: Removes a task from the todo list
**Arguments**:
- `id` (integer): The ID of the task to delete
**Example**: `python main.py delete 1`

#### `complete <id>`
**Description**: Marks a task as completed
**Arguments**:
- `id` (integer): The ID of the task to mark complete
**Example**: `python main.py complete 1`

#### `incomplete <id>`
**Description**: Marks a task as incomplete
**Arguments**:
- `id` (integer): The ID of the task to mark incomplete
**Example**: `python main.py incomplete 1`

#### `help`
**Description**: Shows available commands
**Arguments**: None
**Example**: `python main.py help`

#### `quit` or `exit`
**Description**: Exits the application
**Arguments**: None
**Example**: `python main.py quit`

## Error Responses
All operations follow this error handling pattern:
- **ValidationError**: Message to stderr: "Error: [description of validation issue]"
- **NotFoundError**: Message to stderr: "Error: Task with ID [id] not found"
- **GeneralError**: Message to stderr: "Error: [general error description]"

## Success Responses
- **Success**: Result to stdout in human-readable format
- **Structured Output**: Optionally available in JSON format with --json flag