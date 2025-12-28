# Feature Specification: Todo App Phase I Core

**Feature Branch**: `1-todo-app-core`
**Created**: 2025-12-28
**Status**: Final
**Input**: User description: "Specifications for Todo App Phase I: Language: Python 3.13+, Storage: In-memory list of dicts (keys: id, title, desc, complete). CLI Interface: Menu loop (e.g., 1: Add, 2: View, etc., 0: Exit). Feature Specs: 1. Add: Input title/desc, auto ID, append to list. 2. Delete: Input ID, remove if exists. 3. Update: Input ID, then new title/desc. 4. View: Print formatted list with status. 5. Mark: Input ID, toggle complete. UV: Initialize with requirements.txt (python=3.13). Error Handling: Validate inputs, handle invalid IDs."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Add New Task (Priority: P1)

As a user, I want to create a new task by entering a title and description so that I can add items to my task list. The system automatically assigns a unique ID and stores the task.

**Why this priority**: Task creation is the foundational feature—without the ability to add tasks, there is no task list. P1 is critical for MVP.

**Independent Test**: This story can be tested by starting the app, selecting "Add Task", entering a title and description, and verifying the task appears in the task list with an auto-assigned ID. Demonstrates core data entry and storage.

**Acceptance Scenarios**:

1. **Given** the app is running with an empty task list, **When** I select "Add Task", enter title "Buy groceries" and description "Milk, eggs, bread", **Then** the system creates the task with ID 1 and displays "Task added successfully (ID: 1)."
2. **Given** the task list already has one task with ID 1, **When** I add another task with title "Finish project", **Then** the new task receives ID 2 (auto-increment).
3. **Given** I add a task with whitespace in title/description, **When** the task is stored, **Then** whitespace is stripped from both fields.
4. **Given** I add multiple tasks in sequence, **When** each task is created, **Then** all tasks are stored in the in-memory list with unique sequential IDs (1, 2, 3, ...).

---

### User Story 2 - View All Tasks (Priority: P1)

As a user, I want to see all my tasks in a formatted list so that I can review what I need to do. The list shows task ID, status indicator (complete/incomplete), title, and description.

**Why this priority**: Viewing tasks is essential to the user experience. Without viewing, users cannot verify additions or plan their work. P1 for MVP.

**Independent Test**: This story can be tested by adding several tasks with different completion statuses, then selecting "View Tasks" and verifying the formatted output displays all tasks with correct status indicators, IDs, titles, and descriptions.

**Acceptance Scenarios**:

1. **Given** the task list is empty, **When** I select "View Tasks", **Then** the system displays "No tasks yet. Add one!"
2. **Given** the task list contains 3 tasks (2 incomplete, 1 complete), **When** I select "View Tasks", **Then** the system displays:
   - A header "Tasks:" and separator line
   - All 3 tasks with format: `ID. [Status] Title - Description`
   - Incomplete tasks show `[ ]`, complete task shows `[✓]`
3. **Given** tasks have special characters or unicode in title/description, **When** I view the list, **Then** all characters display correctly.
4. **Given** task description is very long, **When** I view the list, **Then** the entire description is shown on one line.

---

### User Story 3 - Delete Task (Priority: P1)

As a user, I want to delete a task by ID so that I can remove completed or unwanted items from my list. The system safely removes the task without crashing if the ID doesn't exist.

**Why this priority**: Ability to remove tasks is essential for list management. P1 for MVP.

**Independent Test**: This story can be tested by creating several tasks, selecting "Delete Task", entering a valid task ID, and verifying the task is removed. Also test with invalid ID and verify graceful error message.

**Acceptance Scenarios**:

1. **Given** the task list contains 3 tasks, **When** I select "Delete Task", enter ID 2, **Then** the system removes the task with ID 2 and list has 2 remaining tasks (IDs 1 and 3).
2. **Given** the task list contains tasks, **When** I select "Delete Task", enter ID 99 (non-existent), **Then** the system displays "Task with ID 99 not found." and the list remains unchanged.
3. **Given** the task list contains 1 task, **When** I delete it, **Then** the system removes the task and the list is empty.
4. **Given** I delete a task, **When** I add a new task, **Then** the new task receives the next sequential ID (not reusing the deleted ID).

---

### User Story 4 - Update Task (Priority: P2)

As a user, I want to update a task's title and/or description by ID so that I can modify task details. I can update just the title, just the description, or both. Pressing Enter without input keeps the original value.

**Why this priority**: Task editing is important for user experience but not strictly required for MVP. P2 allows basic add/view/delete without update.

**Independent Test**: This story can be tested by adding a task, selecting "Update Task", entering the task ID, optionally entering new title/description, and verifying the task is updated or unchanged as appropriate.

**Acceptance Scenarios**:

1. **Given** a task exists with title "Buy groceries" and description "Milk, eggs, bread", **When** I update it with new title "Buy vegetables" and press Enter for description, **Then** the task now has title "Buy vegetables" and original description "Milk, eggs, bread".
2. **Given** a task exists, **When** I update it, entering only a new description and pressing Enter for title, **Then** only the description is updated, title remains unchanged.
3. **Given** a task exists, **When** I try to update a non-existent task ID 99, **Then** the system displays "Task with ID 99 not found." and no changes are made.
4. **Given** I update a task with new values, **When** the update completes, **Then** the system displays "Task updated." only if changes were made.

---

### User Story 5 - Mark Task Complete/Incomplete (Priority: P2)

As a user, I want to toggle a task's completion status by ID so that I can track which tasks are done. The status indicator changes from `[ ]` to `[✓]` when marked complete, and vice versa.

**Why this priority**: Task completion tracking is valuable but not strictly required for MVP. Covered by basic add/view/delete. P2.

**Independent Test**: This story can be tested by adding a task (initially incomplete), selecting "Mark as Complete", verifying the task shows `[✓]` in the list, then toggling it back to incomplete and verifying `[ ]` appears.

**Acceptance Scenarios**:

1. **Given** a task exists with complete=False, **When** I select "Mark as Complete/Incomplete", enter the task ID, **Then** the task now has complete=True and displays "Task marked as complete."
2. **Given** a task is marked complete, **When** I toggle it again, **Then** it becomes incomplete and displays "Task marked as incomplete."
3. **Given** I try to toggle a non-existent task ID 99, **When** I enter it, **Then** the system displays "Task with ID 99 not found." and no change occurs.
4. **Given** a task is toggled to complete, **When** I view the task list, **Then** the task displays with `[✓]` status indicator.

---

### Edge Cases

- What happens when user enters non-numeric input for task ID? → System displays error: "Invalid input. Please enter a valid integer." and re-prompts.
- How does system handle very long task titles or descriptions? → Accepts and displays without truncation or wrapping (single line in list view).
- What if user presses Ctrl+C during operation? → Application exits gracefully without error.
- What if the in-memory list contains duplicate IDs (data corruption)? → System correctly identifies first matching task and updates/deletes only that instance.
- What if user enters whitespace-only string for title/description? → After `.strip()`, treated as empty string; for Add, accepted as-is; for Update, empty string treated as "keep original".

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST display a menu with 6 options: 1-Add Task, 2-View Tasks, 3-Update Task, 4-Delete Task, 5-Mark as Complete/Incomplete, 0-Exit.
- **FR-002**: System MUST accept user selection (0-5) from menu and execute corresponding action.
- **FR-003**: System MUST prompt for task title and description when user selects "Add Task".
- **FR-004**: System MUST auto-increment task IDs starting from 1 (next ID = max(existing IDs) + 1 or 1 if empty).
- **FR-005**: System MUST store tasks in in-memory Python list of dictionaries with keys: id (int), title (str), desc (str), complete (bool).
- **FR-006**: System MUST display all tasks in formatted list when user selects "View Tasks", showing: ID, status indicator ([ ] or [✓]), title, description.
- **FR-007**: System MUST display "No tasks yet. Add one!" when the task list is empty and user selects "View Tasks".
- **FR-008**: System MUST accept task ID from user when selecting "Delete Task", remove the task, and confirm removal.
- **FR-009**: System MUST display error "Task with ID X not found." when user attempts to delete/update/mark a non-existent task.
- **FR-010**: System MUST accept task ID and optional new title/description when user selects "Update Task".
- **FR-011**: System MUST treat empty input (just pressing Enter) as "keep original value" when updating a task.
- **FR-012**: System MUST toggle task complete status (False ↔ True) when user selects "Mark as Complete/Incomplete".
- **FR-013**: System MUST strip leading/trailing whitespace from all user text input (title, description).
- **FR-014**: System MUST validate integer input for task IDs and re-prompt if user enters non-integer.
- **FR-015**: System MUST exit the application when user selects option 0.

### Key Entities

- **Task**: Represents a single task item with four immutable fields:
  - `id` (int): Unique sequential identifier assigned at creation (never changes, never reused)
  - `title` (str): Task name provided by user (whitespace stripped)
  - `desc` (str): Task description provided by user (whitespace stripped)
  - `complete` (bool): Completion status; False when created, toggled via Mark Complete action

- **Task List**: In-memory Python list containing all task dictionaries; persists only for duration of application run; loses all data when application exits (by design for Phase I).

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Application launches successfully with `python src/main.py` without errors and displays main menu.
- **SC-002**: User can complete all five core operations (add, view, delete, update, mark complete) without encountering crashes or unhandled exceptions.
- **SC-003**: All user input validation works correctly (invalid menu choice rejected, invalid task ID rejected, non-integer input rejected).
- **SC-004**: Task IDs are sequential with no gaps (1, 2, 3, ... even after deletions); next task receives max existing ID + 1.
- **SC-005**: All five features work together in expected sequence: user can add multiple tasks, view them, update one, delete one, mark one complete, and view updated list correctly.
- **SC-006**: Menu interface displays exactly 6 options (1-5 for features, 0 for exit) with no missing or extra options.
- **SC-007**: Task completion status correctly toggles between incomplete `[ ]` and complete `[✓]` in list view.
- **SC-008**: Error messages are clear and actionable (e.g., "Task with ID X not found." vs vague "Error").
- **SC-009**: Application gracefully handles edge cases (empty list, non-existent IDs, Ctrl+C) without crashes.
- **SC-010**: All code includes type hints, docstrings, and PEP 8 compliance with no commented-out code.

## Assumptions

1. **Python Environment**: Python 3.13+ is installed and available; UV package manager is used for project initialization.
2. **CLI Environment**: Application runs in a standard terminal/console supporting basic text I/O (input, print).
3. **User Expertise**: Users are comfortable with CLI menus and can enter numeric selections and text without special training.
4. **No Persistence**: In-memory storage means all tasks are lost when application exits; this is intentional for Phase I.
5. **Single User**: No multi-user support or concurrent access; application is single-threaded, single-user only.
6. **Standard Library Only**: No external dependencies (pytest/testing libraries optional for dev).
7. **ID Auto-Increment**: ID assignment follows simple rule: `next_id = max(existing_ids) + 1`, not `len(tasks) + 1` (handles edge case of deletions).
8. **Whitespace Handling**: Title and description inputs have leading/trailing whitespace stripped; internal whitespace preserved.
9. **No Confirmation on Delete**: Delete operation removes immediately (confirmation is optional enhancement, not Phase I requirement).

## Out of Scope (Phase II and Beyond)

- Database or file-based persistence
- Task categories, priorities, or due dates
- Recurring tasks or scheduling
- Task search or filtering
- Multi-user support or authentication
- Web interface or API
- Undo/redo functionality
- Task attachments or notes
- Notifications or reminders
- Data export/import

---

**Specification Version**: 1.0
**Status**: Ready for Planning
**Next Step**: Run `/sp.clarify` if clarifications needed, or `/sp.plan` to proceed to architectural planning.
