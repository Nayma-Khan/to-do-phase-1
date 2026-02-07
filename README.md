<<<<<<< HEAD
# Console Todo App

A simple command-line todo application with in-memory storage, built with Python.

## Features

- Add new tasks
- View all tasks
- Update task descriptions
- Delete tasks
- Mark tasks as complete/incomplete
- Clean, intuitive command-line interface

## Prerequisites

- Python 3.13+

## Installation

1. Clone or download the repository
2. Navigate to the project directory
3. Run the application directly with Python

## Usage

### Adding a Task
```bash
python main.py add "Buy groceries"
```

### Listing All Tasks
```bash
python main.py list
```

### Updating a Task
```bash
python main.py update 1 "Buy weekly groceries"
```

### Deleting a Task
```bash
python main.py delete 1
```

### Marking a Task as Complete
```bash
python main.py complete 1
```

### Marking a Task as Incomplete
```bash
python main.py incomplete 1
```

### Getting Help
```bash
python main.py help
```

### Exiting the Application
```bash
python main.py quit
# or
python main.py exit
```

## Project Structure

```
src/
├── models/
│   └── todo.py           # Todo data model
├── repository/
│   └── todo_repository.py # In-memory storage
├── services/
│   └── todo_service.py   # Business logic
├── cli/
│   ├── parser.py         # Argument parsing
│   └── command_handlers.py # Command execution
└── utils/
    ├── validation.py     # Input validation
    ├── display.py        # Output formatting
    └── errors.py         # Error handling
```

## Architecture

The application follows a clean, layered architecture:

- **Models**: Define the data structures
- **Repository**: Handle data storage and retrieval
- **Services**: Contain business logic
- **CLI**: Handle command-line interface
- **Utils**: Provide utility functions

## Data Model

Each todo item has:
- `id`: Unique identifier (integer)
- `title`: Description of the task (string)
- `completed`: Completion status (boolean)

## Error Handling

The application validates all inputs and provides appropriate error messages for invalid operations.

## Limitations

- Data is stored only in memory and will be lost when the application exits
- Single-user, offline application
- No persistence to files or databases
=======
# to-do-phase-1
>>>>>>> e6aa32e5ebc6a415a0edd2253eda3ea33d0e88c2
