# Quickstart: Console Todo App

**Feature**: 001-console-todo
**Created**: 2026-02-07

## Overview
Quick start guide for the Console Todo App - a command-line todo application with in-memory storage.

## Getting Started

### Prerequisites
- Python 3.13+
- Command line access

### Running the Application
```bash
python main.py --help
```

### Basic Commands
1. **Add a task**:
   ```bash
   python main.py add "Buy groceries"
   ```

2. **View all tasks**:
   ```bash
   python main.py list
   ```

3. **Complete a task**:
   ```bash
   python main.py complete 1
   ```

4. **Update a task**:
   ```bash
   python main.py update 1 "Buy weekly groceries"
   ```

5. **Delete a task**:
   ```bash
   python main.py delete 1
   ```

### Expected Output
- Tasks are displayed with ID, completion status [ ], and title
- Successful operations return confirmation
- Invalid commands show help text

### Next Steps
- Review all available commands with `python main.py help`
- Test all core functionality: add, list, complete, update, delete
- Verify error handling with invalid inputs