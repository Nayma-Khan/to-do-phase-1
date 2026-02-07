---
description: "Task list for Console Todo App implementation"
---

# Tasks: Console Todo App

**Input**: Design documents from `/specs/001-console-todo/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The feature specification does not explicitly request tests, so they are omitted.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- Project will use `src/` for source code and `main.py` as entry point
- Python files will follow standard structure based on plan.md

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project structure with src/ directory
- [ ] T002 Initialize Python project with proper directory structure
- [ ] T003 [P] Create main.py entry point file

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T004 Create Todo data model class in src/models/todo.py
- [ ] T005 Create in-memory TodoList repository in src/repository/todo_repository.py
- [ ] T006 [P] Create TodoService with business logic in src/services/todo_service.py
- [ ] T007 [P] Create CLI argument parser in src/cli/parser.py
- [ ] T008 [P] Create input validation utilities in src/utils/validation.py
- [ ] T009 Create error handling framework in src/utils/errors.py
- [ ] T010 [P] Create display formatting utilities in src/utils/display.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Tasks (Priority: P1) 🎯 MVP

**Goal**: Allow users to add new tasks to the todo list via command line

**Independent Test**: The app can accept new tasks via command line input and display them when viewing the list, delivering basic todo functionality.

### Implementation for User Story 1

- [ ] T011 [P] [US1] Implement add_task method in src/services/todo_service.py
- [ ] T012 [P] [US1] Implement todo creation validation in src/utils/validation.py
- [ ] T013 [US1] Create add command handler in src/cli/command_handlers.py
- [ ] T014 [US1] Connect add command to CLI parser in src/cli/parser.py
- [ ] T015 [US1] Add error handling for add operations in src/utils/errors.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View All Tasks (Priority: P1)

**Goal**: Allow users to view all current tasks in a formatted list

**Independent Test**: The app displays all currently stored tasks in a clear, readable format when requested, allowing users to see their todo items.

### Implementation for User Story 2

- [ ] T016 [P] [US2] Implement get_all_tasks method in src/services/todo_service.py
- [ ] T017 [P] [US2] Implement task display formatter in src/utils/display.py
- [ ] T018 [US2] Create list command handler in src/cli/command_handlers.py
- [ ] T019 [US2] Connect list command to CLI parser in src/cli/parser.py
- [ ] T020 [US2] Add error handling for list operations in src/utils/errors.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Tasks Complete (Priority: P2)

**Goal**: Allow users to mark tasks as complete/incomplete to track progress

**Independent Test**: The app allows marking tasks as complete and reflects this status in the display, showing which tasks are done.

### Implementation for User Story 3

- [ ] T021 [P] [US3] Implement toggle_task_completion method in src/services/todo_service.py
- [ ] T022 [P] [US3] Create complete/incomplete command handlers in src/cli/command_handlers.py
- [ ] T023 [US3] Connect complete command to CLI parser in src/cli/parser.py
- [ ] T024 [US3] Connect incomplete command to CLI parser in src/cli/parser.py
- [ ] T025 [US3] Add error handling for completion operations in src/utils/errors.py

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Update Task Description (Priority: P3)

**Goal**: Allow users to update the description of existing tasks

**Independent Test**: The app allows modifying existing task descriptions and saves these changes for future viewing.

### Implementation for User Story 4

- [ ] T026 [P] [US4] Implement update_task method in src/services/todo_service.py
- [ ] T027 [P] [US4] Create update command handler in src/cli/command_handlers.py
- [ ] T028 [US4] Connect update command to CLI parser in src/cli/parser.py
- [ ] T029 [US4] Add validation for update operations in src/utils/validation.py
- [ ] T030 [US4] Add error handling for update operations in src/utils/errors.py

**Checkpoint**: At this point, User Stories 1-4 should all work independently

---

## Phase 7: User Story 5 - Delete Tasks (Priority: P3)

**Goal**: Allow users to remove tasks they no longer need

**Independent Test**: The app allows removing specific tasks from the list and they no longer appear when viewing.

### Implementation for User Story 5

- [ ] T031 [P] [US5] Implement delete_task method in src/services/todo_service.py
- [ ] T032 [P] [US5] Create delete command handler in src/cli/command_handlers.py
- [ ] T033 [US5] Connect delete command to CLI parser in src/cli/parser.py
- [ ] T034 [US5] Add validation for delete operations in src/utils/validation.py
- [ ] T035 [US5] Add error handling for delete operations in src/utils/errors.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T036 [P] Add help command implementation in src/cli/command_handlers.py
- [ ] T037 [P] Add quit/exit command implementation in src/cli/command_handlers.py
- [ ] T038 Add comprehensive error messages in src/utils/errors.py
- [ ] T039 [P] Create main application loop in main.py
- [ ] T040 [P] Create comprehensive CLI entry point in main.py
- [ ] T041 Integrate all command handlers into main application flow
- [ ] T042 [P] Update documentation in README.md
- [ ] T043 Run full functionality test to validate all features work together

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - Builds upon data model from previous stories
- **User Story 4 (P3)**: Can start after Foundational (Phase 2) - Builds upon data model from previous stories
- **User Story 5 (P3)**: Can start after Foundational (Phase 2) - Builds upon data model from previous stories

### Within Each User Story

- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Different user stories can be worked on in parallel by different team members
- All tasks within a user story marked [P] can run in parallel

---

## Parallel Example: User Story 1

```bash
# Launch all parallel tasks for User Story 1 together:
Task: "Implement add_task method in src/services/todo_service.py"
Task: "Implement todo creation validation in src/utils/validation.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. Complete Phase 4: User Story 2
5. **STOP and VALIDATE**: Test User Stories 1 and 2 together - this is the MVP!
6. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 & 2 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 3 → Test independently → Deploy/Demo
4. Add User Story 4 → Test independently → Deploy/Demo
5. Add User Story 5 → Test independently → Deploy/Demo
6. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4 & 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Focus on clean, modular structure with separation of concerns