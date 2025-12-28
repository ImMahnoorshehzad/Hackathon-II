# Implementation Plan: Todo App Phase I Core

**Feature Branch**: `1-todo-app-core`
**Created**: 2025-12-28
**Status**: Final Plan
**Specification**: [spec.md](spec.md)

---

## Executive Summary

This plan outlines the architectural design and implementation strategy for the Todo App Phase I Core—a Python 3.13+ CLI application with in-memory task storage and menu-driven interface. The application implements five core features (Add, View, Delete, Update, Mark Complete) using test-driven development (TDD) and follows the Spec-Driven Development (SDD) methodology established in the project constitution.

**Key Principles:**
- Spec-driven development with SDD + SpecifyPlus
- Test-driven development (red-green-refactor)
- Python 3.13+ with UV package manager
- Standard library only (no external dependencies for Phase I)
- In-memory storage (ephemeral, by design)
- Clean code: type hints, docstrings, PEP 8 compliance

---

## Phase 0: Technical Context & Unknowns

### Constitutional Requirements Check

**Adherence to Constitution** (`Todo App Evolution - Phase I Constitution v1.0.0`):

- ✅ **Spec-Driven Development**: Feature has complete spec (spec.md) ← SDD mandate satisfied
- ✅ **Python 3.13+**: Explicitly required, enforced via .python-version
- ✅ **UV Mandatory**: Project initialized with `uv init --python 3.13`, uv venv, uv sync
- ✅ **Five Core Features**: Add, View, Delete, Update, Mark Complete (scope locked, Phase I only)
- ✅ **In-Memory Storage**: List of dicts {id, title, desc, complete}; no persistence
- ✅ **Clean Code**: Type hints, docstrings, PEP 8, no boilerplate
- ✅ **Project Structure**: /src for code, specs history, README.md, CLAUDE.md, constitution.md

**Gate Evaluation**: ✅ **PASS** - All constitutional requirements satisfied

### Technical Context

| Aspect | Decision | Rationale |
|--------|----------|-----------|
| **Language** | Python 3.13+ | Modern syntax, performance, security; enforced by constitution |
| **Package Manager** | UV | Deterministic, fast, reproducible; mandatory per constitution |
| **Storage** | In-memory list of dicts | Simple, no infra dependencies; Phase I design choice |
| **CLI Framework** | None (built-in input/print) | Standard library only; no external packages Phase I |
| **Testing Framework** | pytest (optional) | Development dependency, installed via `uv add --dev pytest` |
| **Code Quality** | Type hints + docstrings | Mandatory per constitution; enforced via code review |

### Unknowns Resolved (Phase 0 Research)

**No NEEDS CLARIFICATION markers** – The specification is unambiguous and complete. All design decisions are documented in the spec's Assumptions section.

**Research Tasks Completed**:
1. ✅ Python 3.13 compatibility with standard library I/O (input/print)
2. ✅ Best practices for in-memory task storage (list of dicts)
3. ✅ CLI menu patterns for interactive Python apps
4. ✅ Input validation and error handling in CLI context
5. ✅ Auto-increment ID assignment strategies (max(ids) + 1)

**Findings Consolidated** in Technical Context above (no separate research.md needed; all resolved)

---

## Phase 1: Design & Architecture

### Data Model

**Primary Entity: Task**

```python
Task: dict = {
    "id": int,              # Unique sequential identifier (1, 2, 3, ...)
                           # Immutable once assigned; never reused even after deletion
                           # Generated via: next_id = max(existing_ids) + 1 or 1 if empty

    "title": str,          # Task name (user input, whitespace stripped)
                           # Constraints: non-empty after strip, accepts unicode/special chars

    "desc": str,           # Task description (user input, whitespace stripped)
                           # Constraints: non-empty after strip, accepts unicode/special chars

    "complete": bool       # Completion status: False (new task), True (marked complete)
                           # Toggled via: complete = not complete
}
```

**Task List Storage**

```python
tasks: list[dict] = [
    {"id": 1, "title": "...", "desc": "...", "complete": False},
    {"id": 2, "title": "...", "desc": "...", "complete": True},
    # ... up to n tasks
]
```

**Constraints & Invariants:**
1. Task IDs are unique (never duplicate)
2. Task IDs are sequential (no gaps, even after deletion)
3. Task IDs are immutable (never changed once assigned)
4. Task IDs are never reused (deleted IDs stay deleted)
5. Title and description are non-empty after whitespace stripping
6. Complete status is always a boolean (True or False)
7. Storage is ephemeral (lost on application exit; by design)

**State Transitions:**
- New task: `complete = False` (always)
- Mark Complete: `complete = False → True`
- Mark Incomplete: `complete = True → False`
- Update: `title` and/or `desc` can change; `id` and `complete` do not change
- Delete: Task removed entirely (no soft delete in Phase I)

### Function Contracts

**Helper Functions** (reusable utilities):

```python
# Helper: Find task by ID
def find_task(tasks: list[dict], task_id: int) -> dict | None:
    """
    Find a task in the list by ID.

    Args:
        tasks: List of task dictionaries
        task_id: ID to search for

    Returns:
        Task dict if found, None if not found

    Usage:
        task = find_task(tasks, 1)
        if task:
            print(f"Found: {task['title']}")
    """
    return next((t for t in tasks if t["id"] == task_id), None)

# Helper: Get next available ID
def get_next_id(tasks: list[dict]) -> int:
    """
    Calculate the next available task ID.

    Args:
        tasks: List of task dictionaries

    Returns:
        Next ID (max(existing_ids) + 1 or 1 if empty)

    Usage:
        next_id = get_next_id(tasks)
        new_task = {"id": next_id, "title": "...", "desc": "...", "complete": False}
    """
    return max((t["id"] for t in tasks), default=0) + 1
```

**Core Operation Functions**:

```python
# Core: Add Task
def add_task(tasks: list[dict]) -> None:
    """
    Create a new task interactively.

    Prompts user for title and description, auto-assigns ID, appends to list.

    Args:
        tasks: Task list (modified in-place)

    Output:
        "Task added successfully (ID: X)."
    """
    # 1. Prompt for title
    # 2. Prompt for description
    # 3. Generate ID using get_next_id()
    # 4. Create task dict
    # 5. Append to tasks list
    # 6. Print success message with ID
    pass

# Core: View Tasks
def print_tasks(tasks: list[dict]) -> None:
    """
    Display all tasks in formatted list.

    Args:
        tasks: Task list (not modified)

    Output:
        Formatted list or "No tasks yet. Add one!"
    """
    # 1. If empty: print "No tasks yet. Add one!"
    # 2. Else:
    #    - Print "Tasks:" header
    #    - Print "------" separator
    #    - For each task: print formatted line with ID, status, title, desc
    pass

# Core: Delete Task
def delete_task(tasks: list[dict], task_id: int) -> bool:
    """
    Delete a task by ID.

    Args:
        tasks: Task list (modified in-place if task found)
        task_id: ID to delete

    Returns:
        True if deleted, False if not found

    Output:
        "Task with ID X not found." if not found
    """
    # 1. Find task using find_task()
    # 2. If found: remove from list, return True
    # 3. If not found: print error, return False
    pass

# Core: Update Task
def update_task(tasks: list[dict], task_id: int) -> bool:
    """
    Update a task's title and/or description.

    Args:
        tasks: Task list (modified in-place if task found)
        task_id: ID to update

    Returns:
        True if task found (updated or not), False if not found

    Output:
        "Task updated." if changes made
        "Task with ID X not found." if not found
    """
    # 1. Find task using find_task()
    # 2. If not found: print error, return False
    # 3. Display current values
    # 4. Prompt for new title (Enter = keep original)
    # 5. Prompt for new description (Enter = keep original)
    # 6. Update if changes made
    # 7. Print success only if changes, return True
    pass

# Core: Mark Complete/Incomplete
def toggle_complete(tasks: list[dict], task_id: int) -> bool:
    """
    Toggle task completion status.

    Args:
        tasks: Task list (modified in-place if task found)
        task_id: ID to toggle

    Returns:
        True if toggled, False if not found

    Output:
        "Task marked as complete." or "Task marked as incomplete."
        "Task with ID X not found." if not found
    """
    # 1. Find task using find_task()
    # 2. If not found: print error, return False
    # 3. Invert completion status: complete = not complete
    # 4. Print appropriate message based on new status
    # 5. Return True
    pass

# UI: Display Menu
def display_menu() -> None:
    """
    Display the main menu.

    Args: None

    Output:
        Menu with 6 options (1-5, 0)
    """
    # Print exact menu format:
    # Todo App
    # ========
    # 1. Add Task
    # 2. View Tasks
    # 3. Update Task
    # 4. Delete Task
    # 5. Mark as Complete/Incomplete
    # 0. Exit
    # Choose an option: [cursor here]
    pass

# UI: Get Menu Choice
def get_menu_choice() -> int:
    """
    Display menu and get valid user choice.

    Returns:
        Integer 0-5 (guaranteed valid)

    Process:
        1. Display menu
        2. Get integer input with validation
        3. Validate range 0-5
        4. Re-prompt on invalid
        5. Return valid choice
    """
    # 1. Call display_menu()
    # 2. Get integer input with error handling
    # 3. Validate range
    # 4. Return valid choice (0-5)
    pass

# UI: Get Integer Input
def get_int_input(prompt: str) -> int:
    """
    Get validated integer input from user.

    Args:
        prompt: Display prompt

    Returns:
        Valid integer

    Process:
        1. Prompt user
        2. Try to parse integer
        3. On ValueError: print error, re-prompt
        4. On Ctrl+C: print "Goodbye!", exit
        5. Return integer
    """
    # Loop:
    # 1. Try: return int(input(prompt))
    # 2. Except ValueError: print error, loop
    # 3. Except KeyboardInterrupt: print "Goodbye!", sys.exit(0)
    pass

# UI: Confirm Action
def confirm(prompt: str) -> bool:
    """
    Get yes/no confirmation from user.

    Args:
        prompt: Display prompt (e.g., "Delete? (y/n): ")

    Returns:
        True for yes, False for no

    Process:
        1. Prompt user
        2. Accept y/Y/yes/Yes → True
        3. Accept n/N/no/No → False
        4. On invalid: re-prompt
        5. Return boolean
    """
    # Loop:
    # 1. Get input and lowercase
    # 2. If in ['y', 'yes']: return True
    # 3. If in ['n', 'no']: return False
    # 4. Else: print error, loop
    pass
```

**Main Event Loop**:

```python
def main():
    """
    Main application event loop.

    Process:
        1. Initialize empty task list
        2. Loop:
           - Display menu and get choice
           - Execute corresponding operation
           - Continue until user selects 0 (Exit)
    """
    # tasks: list[dict] = []
    # while True:
    #     choice = get_menu_choice()
    #     if choice == 0: break
    #     elif choice == 1: add_task(tasks)
    #     elif choice == 2: print_tasks(tasks)
    #     elif choice == 3: update_task(tasks, ...)
    #     elif choice == 4: delete_task(tasks, ...)
    #     elif choice == 5: toggle_complete(tasks, ...)
    # print("Goodbye!")
    pass

if __name__ == "__main__":
    main()
```

### Code Organization

**File: `src/main.py`**

```
main.py
├── Imports (sys, typing annotations)
├── Helper Functions
│   ├── find_task()
│   └── get_next_id()
├── Core Operations
│   ├── add_task()
│   ├── delete_task()
│   ├── update_task()
│   ├── print_tasks()
│   └── toggle_complete()
├── UI Functions
│   ├── display_menu()
│   ├── get_menu_choice()
│   ├── get_int_input()
│   └── confirm()
├── Main Event Loop
│   └── main()
└── Entry Point
    └── if __name__ == "__main__": main()
```

**Total Lines**: ~400-500 (implementation with docstrings)

### Technology Stack

| Component | Technology | Rationale |
|-----------|-----------|-----------|
| **Language** | Python 3.13+ | Modern, readable, enforced by constitution |
| **Package Manager** | UV | Deterministic, fast, mandatory per constitution |
| **Storage** | In-memory list of dicts | Simple, no infrastructure; Phase I design |
| **CLI Framework** | Built-in (input/print) | Standard library only; no external packages |
| **Testing** | pytest (optional dev dep) | Standard Python testing framework |
| **Type Checking** | Type hints (built-in) | Type safety via annotations, no external tool |
| **Linting** | Manual review (PEP 8) | Code quality via constitution standards |

### Input Validation & Error Handling

| Input Type | Validation | Error Handling |
|-----------|-----------|-----------------|
| **Menu Choice** | Must be integer 0-5 | Re-prompt with error: "Option X not valid. Please choose 0-5." |
| **Task ID** | Must be integer, must exist | Re-prompt with error: "Task with ID X not found." |
| **Title/Desc** | Any non-empty string | Strip whitespace; accept unicode, special chars |
| **Yes/No Input** | y/Y/yes/Yes or n/N/no/No | Re-prompt with error: "Invalid input. Please enter 'y' or 'n'." |
| **Ctrl+C** | KeyboardInterrupt | Catch and print "Goodbye!", exit(0) |

---

## Phase 2: Implementation Strategy

### Red-Green-Refactor TDD Cycle

**For each function:**

1. **RED** – Write failing test
   - Test the expected behavior (from spec acceptance scenarios)
   - Run test; verify it fails
   - Example: `test_add_task_creates_task_with_id_1()`

2. **GREEN** – Implement minimal code
   - Write just enough code to pass the test
   - No over-engineering or future-proofing
   - Example: Create task dict, append to list, print message

3. **REFACTOR** – Improve code quality
   - Extract helpers (find_task, get_next_id)
   - Add type hints and docstrings
   - Ensure PEP 8 compliance
   - No logic changes; quality improvements only

**Order of Implementation:**

1. Helper functions (find_task, get_next_id) – foundation
2. Core operations (add, delete, update, view, toggle) – business logic
3. UI functions (menu, input, confirm) – user interaction
4. Main loop – orchestration
5. All tests – comprehensive coverage

### Test Strategy

**Test File: `tests/test_main.py`**

**Test Categories:**

1. **Data Model Tests** (5-10 tests)
   - Task dict structure and fields
   - ID uniqueness and sequencing
   - Whitespace stripping
   - Complete status toggle

2. **Helper Function Tests** (5 tests)
   - find_task: found, not found, empty list
   - get_next_id: empty list, single task, multiple tasks

3. **Core Operation Tests** (20+ tests)
   - Add Task: empty list, multiple adds, whitespace, special chars
   - View Tasks: empty, single, multiple, mixed status
   - Delete Task: exists, not exists, cascading effects
   - Update Task: both fields, one field, no changes
   - Toggle Complete: both directions, not found

4. **UI Tests** (10+ tests)
   - Menu display format
   - Input validation (menu choice, task ID, yes/no)
   - Error messages
   - Edge cases (Ctrl+C, empty input)

5. **Integration Tests** (5+ tests)
   - Complete workflow: add → view → update → toggle → delete
   - Multiple operations in sequence
   - State consistency across operations

**Success Criteria:**
- Minimum 80% code coverage
- All acceptance scenarios from spec have corresponding tests
- All tests pass before release

### Code Quality Standards

| Standard | Requirement |
|----------|------------|
| **Type Hints** | All function parameters and returns must have type annotations |
| **Docstrings** | All functions must have docstrings explaining purpose, args, returns, usage |
| **PEP 8 Compliance** | Code must follow PEP 8 style guide (4-space indent, <100 char lines) |
| **No Debug Code** | No print() statements for debugging; no commented-out code in commits |
| **No Boilerplate** | No unnecessary helper classes, decorators, or abstractions |
| **DRY Principle** | Common patterns extracted into reusable functions (find_task, get_next_id) |

---

## Phase 3: Deployment & Release

### Build Steps

1. **UV Initialization** (already done)
   ```bash
   uv init --python 3.13
   uv venv
   source .venv/bin/activate
   uv sync
   ```

2. **Code Implementation**
   - Write src/main.py with all functions
   - Write tests/test_main.py with comprehensive tests

3. **Testing**
   ```bash
   python -m pytest tests/ -v
   ```
   - All tests pass (100% acceptance scenarios covered)
   - Coverage >= 80%

4. **Manual Testing**
   ```bash
   python src/main.py
   ```
   - All 5 features work without crashes
   - Menu displays correctly
   - Error handling is graceful

5. **Code Quality Check**
   - Type hints present on all functions
   - Docstrings present on all functions
   - PEP 8 compliance verified (via manual review)
   - No debug code in commits

### GitHub Workflow

1. **Commit Code**
   ```bash
   git add src/ tests/ specs/
   git commit -m "feat: implement todo app phase I core

   Implement 5 core features with TDD:
   - Add Task: Create tasks with auto-ID
   - View Tasks: Display formatted list
   - Delete Task: Remove tasks safely
   - Update Task: Modify task details
   - Mark Complete/Incomplete: Toggle status

   All features tested and working."
   ```

2. **Push to Remote**
   ```bash
   git push origin 1-todo-app-core
   ```

3. **Create Pull Request** (optional for Phase I)
   - Link to spec and plan
   - Reference acceptance scenarios
   - Document any assumptions or decisions

---

## Success Criteria

| Criterion | Acceptance | Status |
|-----------|-----------|--------|
| **MVP Functional** | All 5 features work without crashes | TBD (Implementation) |
| **Code Quality** | Type hints, docstrings, PEP 8 | TBD (Implementation) |
| **Test Coverage** | >= 80% code coverage | TBD (Implementation) |
| **Spec Compliance** | All acceptance scenarios pass | TBD (Implementation) |
| **UI Polish** | Menu clear, errors graceful | TBD (Implementation) |
| **No Dependencies** | Standard library only, no external packages | TBD (Implementation) |

---

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| **Complex input validation** | Crashes on edge cases | Comprehensive test cases for all input types |
| **ID management errors** | Data consistency broken | Helper function (get_next_id) with tests |
| **Scope creep** | Phase I features not completed | Scope locked in constitution; Phase II for extensions |
| **Poor test coverage** | Bugs in production** | TDD enforced; 80%+ coverage required |

---

## Next Steps (Tasks Phase)

1. Run `/sp.tasks` to generate testable, dependency-ordered work items
2. Implement features in task order using red-green-refactor TDD
3. Verify all tests pass and coverage >= 80%
4. Manual testing and demo
5. Commit and push to GitHub

---

**Plan Version**: 1.0
**Status**: Ready for Task Generation
**Next Command**: `/sp.tasks` to generate implementation tasks

