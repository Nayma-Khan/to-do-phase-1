# Implementation Plan: Console Todo App

**Branch**: `001-console-todo` | **Date**: 2026-02-07 | **Spec**: specs/001-console-todo/spec.md
**Input**: Feature specification from `/specs/001-console-todo/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Console Todo application supporting Add, View, Update, Delete, and Mark Complete operations via command line interface. The application stores all data in memory without persistence to files or databases, using Python 3.13+ with clean, modular structure.

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**: Standard library only (argparse, json, sys, os)
**Storage**: In-memory Python data structures (no external storage)
**Testing**: pytest (for any future test expansion)
**Target Platform**: Cross-platform (Windows, macOS, Linux)
**Project Type**: Single console application
**Performance Goals**: Sub-100ms response times for all operations
**Constraints**: No external dependencies beyond Python standard library, deterministic CLI behavior with input validation
**Scale/Scope**: Single-user, local application

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

Based on the project constitution principles:
- **Library-First**: Will implement as modular components that could function as a library
- **CLI Interface**: Expose functionality through command-line interface
- **Test-First**: Write tests before implementing functionality
- **Observability**: Ensure debuggability through clear text I/O

### Potential Violations
- **None identified**: The planned architecture aligns with all constitution principles

## Project Structure

### Documentation (this feature)

```text
specs/[###-feature]/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
main.py                 # Entry point and CLI loop
src/
├── models/
│   └── todo.py         # Todo data model
├── repository/
│   └── todo_repository.py  # In-memory storage
├── services/
│   └── todo_service.py # Business logic
├── cli/
│   ├── parser.py       # Argument parsing
│   └── command_handlers.py  # Command execution
└── utils/
    ├── validation.py   # Input validation
    ├── display.py      # Output formatting
    └── errors.py       # Error handling
```

**Structure Decision**: Single console application using layered architecture with clear separation of concerns. Models handle data representation, repository manages storage, services contain business logic, CLI handles user interaction, and utils provide helper functions.

## Phase 0: Outline & Research

### RT-001: Data Structure Selection
**Decision**: Choose appropriate Python data structure for in-memory todo storage
**Rationale**: Need to select between list, dictionary, or custom class for optimal performance and usability
**Alternatives considered**:
- Simple list of dictionaries
- Dictionary with ID as key and task object as value
- Custom class-based storage

### RT-002: CLI Framework Selection
**Decision**: Determine whether to use standard input() or a CLI framework like argparse
**Rationale**: CLI interaction method affects user experience and code organization
**Alternatives considered**:
- Built-in argparse module
- Standard input/output with manual parsing
- Third-party CLI framework (though limited to stdlib per constraints)

### RT-003: Validation Strategy
**Decision**: Define level and approach for input validation
**Rationale**: Proper validation prevents errors and improves user experience
**Alternatives considered**:
- Basic validation (non-empty checks)
- Comprehensive validation (format, length, character restrictions)

## Phase 1: Design & Contracts

### DT-001: Data Model Definition
- Entity: Todo
  - Properties: id (int), title (str), completed (bool)
  - Relationships: None (self-contained entity)
  - Validation rules: title must be non-empty string
  - State transitions: pending → completed, completed → pending

### DT-002: Service Contract Definition
- Service: TodoService
  - Methods:
    - add_task(title: str) -> int (returns task ID)
    - get_all_tasks() -> List[Todo]
    - update_task(task_id: int, title: str) -> bool
    - delete_task(task_id: int) -> bool
    - toggle_task_completion(task_id: int) -> bool

### DT-003: CLI Contract Definition
- Commands:
  - `add "task title"` - Add new task
  - `list` - Show all tasks
  - `update <id> "new title"` - Update task
  - `delete <id>` - Delete task
  - `complete <id>` - Mark task as complete
  - `incomplete <id>` - Mark task as incomplete
  - `help` - Show available commands
  - `quit` or `exit` - Exit application

## Phase 2: Implementation Approach

### IA-001: Development Sequence
1. Define the Todo data model
2. Implement in-memory storage repository
3. Build core TodoService with business logic
4. Create CLI interface with command routing
5. Add input validation and error handling
6. Test all functionality

### IA-002: Error Handling Strategy
- Invalid commands show help message
- Invalid task IDs show appropriate error
- Empty or invalid inputs are rejected with helpful messages
- Graceful degradation when possible

### IA-003: User Experience Design
- Clear prompts and feedback
- Intuitive command structure
- Helpful error messages
- Consistent output formatting

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |
