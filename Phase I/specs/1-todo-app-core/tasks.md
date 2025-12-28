# Implementation Tasks: Todo App Phase I Core

**Feature Branch**: `1-todo-app-core`
**Created**: 2025-12-28
**Status**: Ready for Implementation
**Specification**: [spec.md](spec.md)
**Plan**: [plan.md](plan.md)

---

## Overview

This document defines testable, dependency-ordered implementation tasks for the Todo App Phase I Core. Tasks follow the red-green-refactor TDD cycle and are organized by user story priority. Each task is independently testable and includes acceptance criteria aligned with the specification.

**Total Tasks**: 24 tasks across 7 phases
**Testing Approach**: TDD (red-green-refactor) with 50+ unit and integration tests
**Target Coverage**: >= 80% code coverage

---

## Dependencies & Execution Order

### User Story Priority Order (from spec.md)

1. **P1 - User Story 1**: Add New Task (foundational, required for MVP)
2. **P1 - User Story 2**: View All Tasks (foundational, required for MVP)
3. **P1 - User Story 3**: Delete Task (foundational, required for MVP)
4. **P2 - User Story 4**: Update Task (valuable, not MVP-blocking)
5. **P2 - User Story 5**: Mark Task Complete/Incomplete (valuable, not MVP-blocking)

### Execution Strategy

**Phase 1 (Setup)**: Create project structure and UV environment
**Phase 2 (Foundational)**: Implement helper functions (blocking for all user stories)
**Phase 3-7 (User Stories)**: Implement P1 and P2 features in priority order with integrated testing
**Parallel Opportunities**: US4 and US5 can be implemented in parallel after US1-3 are complete

### Suggested MVP Scope

Implement **Phases 1-5** (Setup + Foundational + US1, US2, US3) to achieve minimum viable product with 5 core features. US4 and US5 can be completed afterward as enhancements.

---

## Phase 1: Setup & Project Structure

**Goal**: Initialize Python 3.13+ project with UV package manager, create directory structure, and prepare for development.

**Independent Test**: Verify project structure exists, Python interpreter available, UV venv created, and empty src/main.py can be executed.

### Tasks

- [ ] T001 Initialize Python 3.13+ project with UV: run `uv init --python 3.13` in repo root
- [ ] T002 Create UV virtual environment: run `uv venv` and activate with `.venv/bin/activate` (Windows: `.venv\Scripts\activate.ps1`)
- [ ] T003 Sync UV dependencies: run `uv sync` to install base dependencies
- [ ] T004 Create src/ directory structure: `mkdir -p src tests`
- [ ] T005 Create pyproject.toml with Python 3.13+ requirement and metadata (name, version, description)
- [ ] T006 Optionally add pytest dev dependency: run `uv add --dev pytest` for testing framework
- [ ] T007 Create empty src/main.py with shebang and module docstring
- [ ] T008 Verify project structure: `ls -la src/ tests/` shows both directories
- [ ] T009 Test Python 3.13+ execution: run `python --version` and confirm 3.13+
- [ ] T010 Create .python-version file with `3.13` to enforce Python version

**Success Criteria**:
- ✅ UV venv is active and `python --version` shows 3.13+
- ✅ src/ and tests/ directories exist
- ✅ src/main.py exists and is executable
- ✅ pyproject.toml correctly specifies Python 3.13+ requirement

---

## Phase 2: Foundational Functions (Blocking for All User Stories)

**Goal**: Implement helper functions that are reusable across all user stories and operations.

**Dependencies**: Phase 1 (Setup) must be complete
**Independent Test**: Each helper function has isolated unit tests with edge cases (empty list, single item, multiple items)
**Parallel Opportunities**: T011-T013 can be implemented in parallel (independent functions, no dependencies)

### Tasks

- [ ] T011 [P] Implement find_task() helper in src/main.py: signature `find_task(tasks: list[dict], task_id: int) -> dict | None`
  - RED: Write test_find_task_returns_dict_when_found()
  - GREEN: Return first task dict where id matches
  - REFACTOR: Add docstring, type hints, examples
  - **Test**: Covers found, not found, empty list

- [ ] T012 [P] Implement get_next_id() helper in src/main.py: signature `get_next_id(tasks: list[dict]) -> int`
  - RED: Write test_get_next_id_returns_1_when_empty()
  - GREEN: Return max(ids) + 1 or 1 if empty
  - REFACTOR: Add docstring, type hints, edge case handling
  - **Test**: Covers empty list, single task, multiple tasks, sequential numbering

- [ ] T013 [P] Implement get_int_input() UI helper in src/main.py: signature `get_int_input(prompt: str) -> int`
  - RED: Write test_get_int_input_validates_integer()
  - GREEN: Loop until valid integer; catch ValueError
  - REFACTOR: Add Ctrl+C handling (KeyboardInterrupt → "Goodbye!", sys.exit(0))
  - **Test**: Covers valid input, non-numeric input, Ctrl+C

- [ ] T014 [P] Implement confirm() UI helper in src/main.py: signature `confirm(prompt: str) -> bool`
  - RED: Write test_confirm_returns_true_for_yes_variants()
  - GREEN: Accept y/Y/yes/Yes → True, n/N/no/No → False, re-prompt on invalid
  - REFACTOR: Add docstring, type hints, error messaging
  - **Test**: Covers yes variants, no variants, invalid input, case-insensitivity

- [ ] T015 Implement display_menu() UI function in src/main.py: signature `display_menu() -> None`
  - RED: Write test_display_menu_prints_6_options()
  - GREEN: Print menu header "Todo App", separator, 6 options (1-5 + 0)
  - REFACTOR: Ensure exact format per spec
  - **Test**: Verifies menu format, option count, clarity

- [ ] T016 Implement get_menu_choice() UI function in src/main.py: signature `get_menu_choice() -> int`
  - RED: Write test_get_menu_choice_returns_0_to_5()
  - GREEN: Call display_menu(), get integer 0-5, re-prompt if invalid
  - REFACTOR: Add validation loop, error messages
  - **Test**: Covers valid choices, out-of-range choices, non-numeric input

**Success Criteria**:
- ✅ All 6 helper/UI functions implemented with correct signatures
- ✅ 15+ unit tests written and passing (find_task: 3, get_next_id: 3, get_int_input: 3, confirm: 3, display_menu: 2, get_menu_choice: 2)
- ✅ Type hints present on all functions
- ✅ Docstrings explain purpose, args, returns
- ✅ PEP 8 compliant

---

## Phase 3: User Story 1 - Add New Task (P1 - MVP Critical)

**User Story**: As a user, I want to create a new task by entering a title and description so that I can add items to my task list.

**Acceptance Scenarios** (from spec.md):
1. Creating task in empty list assigns ID 1 and displays success message
2. Sequential additions auto-increment IDs (1, 2, 3, ...)
3. Whitespace is stripped from title/description
4. Multiple tasks stored correctly in in-memory list

**Dependencies**: Phase 2 (Foundational functions must be complete)
**Independent Test**: Create task → verify ID, title, desc stored; test sequential IDs; test whitespace stripping
**Test Approach**: 5 unit tests + 2 integration tests for add_task()

### Tasks

- [ ] T017 [US1] Write failing test: test_add_task_creates_task_with_id_1_in_empty_list()
  - Test adds task to empty list, verifies ID=1, title matches input, desc matches input

- [ ] T018 [US1] Write failing test: test_add_task_auto_increments_id()
  - Test adds task to list with existing task (ID=1), verifies new task gets ID=2

- [ ] T019 [US1] Write failing test: test_add_task_strips_whitespace()
  - Test adds task with `"  Buy groceries  "` and `"  Milk, eggs  "`, verifies stored without whitespace

- [ ] T020 [US1] Implement add_task() function in src/main.py: signature `add_task(tasks: list[dict]) -> None`
  - RED: All 3 tests above fail
  - GREEN: Prompt for title, prompt for description, generate ID, append dict to tasks, print success message
  - REFACTOR: Extract prompting into helper, add docstring, type hints
  - **Accept**: Tests T017-T019 pass; success message printed; task appended to list

- [ ] T021 [US1] Write integration test: test_add_task_integration_view_tasks()
  - Test adds task via add_task(), then view list and verify task appears with correct formatting

- [ ] T022 [US1] Implement print_tasks() function in src/main.py: signature `print_tasks(tasks: list[dict]) -> None`
  - RED: Write test_print_tasks_shows_empty_message() and test_print_tasks_shows_formatted_list()
  - GREEN: If empty, print "No tasks yet. Add one!"; else print header, separator, each task formatted
  - REFACTOR: Add docstring, ensure format matches spec (ID, status, title, desc)
  - **Accept**: Empty list shows message; populated list shows all tasks with ID, status [ ] or [✓], title, desc

**Success Criteria**:
- ✅ add_task() accepts title and description via input prompts
- ✅ Task automatically assigned sequential ID starting at 1
- ✅ Whitespace stripped from title/description
- ✅ Task appended to tasks list
- ✅ Success message displays: "Task added successfully (ID: X)."
- ✅ print_tasks() displays all tasks in formatted list or empty state message
- ✅ 5 unit tests + 2 integration tests written and passing
- ✅ 80%+ code coverage for US1 functions

---

## Phase 4: User Story 2 - View All Tasks (P1 - MVP Critical)

**User Story**: As a user, I want to see all my tasks in a formatted list so that I can review what I need to do.

**Acceptance Scenarios** (from spec.md):
1. Empty list displays "No tasks yet. Add one!"
2. List with mixed statuses displays ID, status indicator [ ]/[✓], title, description
3. Special characters and unicode display correctly
4. Long descriptions display on single line without truncation

**Dependencies**: Phase 2 (Foundational) + Phase 3 (US1 - add_task required for testing)
**Independent Test**: Add tasks with various content → view → verify formatting
**Test Approach**: 4 unit tests for print_tasks() covering empty, single, multiple, special chars

### Tasks

- [ ] T023 [US2] Write failing test: test_print_tasks_empty_list()
  - Verify output contains "No tasks yet. Add one!"

- [ ] T024 [US2] Write failing test: test_print_tasks_formatted_list()
  - Create task list with 2 incomplete, 1 complete task; verify output format with ID, [ ]/[✓], title, desc

- [ ] T025 [US2] Write failing test: test_print_tasks_special_characters()
  - Create task with unicode/special chars (émojis, symbols); verify displayed correctly

- [ ] T026 [US2] Refactor print_tasks() implementation to pass all tests
  - Format: `ID. [Status] Title - Description` where Status is [ ] for incomplete, [✓] for complete
  - **Accept**: All 4 tests pass; formatting exactly matches spec; no truncation

**Success Criteria**:
- ✅ Empty task list displays "No tasks yet. Add one!"
- ✅ Populated list shows header "Tasks:" and separator line
- ✅ Each task formatted as: `ID. [Status] Title - Description`
- ✅ Status indicator: [ ] for incomplete, [✓] for complete
- ✅ All content (including special chars, unicode) displays correctly
- ✅ No truncation of long descriptions (single line display)
- ✅ 4 unit tests + 1 integration test written and passing

---

## Phase 5: User Story 3 - Delete Task (P1 - MVP Critical)

**User Story**: As a user, I want to delete a task by ID so that I can remove completed or unwanted items from my list.

**Acceptance Scenarios** (from spec.md):
1. Deleting existing task removes it and reduces list size
2. Attempting to delete non-existent ID displays error and leaves list unchanged
3. Deleting last task leaves empty list
4. New tasks after deletion get next sequential ID (no ID reuse)

**Dependencies**: Phase 2 (Foundational) + Phase 3 (US1 - add_task required for testing)
**Independent Test**: Add tasks → delete by ID → verify task removed and ID generation correct
**Test Approach**: 5 unit tests for delete_task() covering exists, not exists, cascading effects

### Tasks

- [ ] T027 [US3] Write failing test: test_delete_task_removes_existing_task()
  - Create 3 tasks (IDs 1,2,3), delete ID 2, verify list has 2 tasks (IDs 1,3)

- [ ] T028 [US3] Write failing test: test_delete_task_not_found_error()
  - Attempt to delete ID 99, verify error message printed, list unchanged

- [ ] T029 [US3] Write failing test: test_delete_task_last_task()
  - Create 1 task, delete it, verify list is empty

- [ ] T030 [US3] Write failing test: test_delete_task_sequential_ids_no_gaps()
  - Create 3 tasks, delete ID 2, add new task, verify new task gets ID 4 (not 2)

- [ ] T031 [US3] Implement delete_task() function in src/main.py: signature `delete_task(tasks: list[dict], task_id: int) -> bool`
  - RED: Tests T027-T030 fail
  - GREEN: Find task by ID, remove if exists, return True; if not found, print error, return False
  - REFACTOR: Use find_task() helper, add docstring, type hints
  - **Accept**: All 4 tests pass; task removed; error displayed for non-existent; return value correct

- [ ] T032 [US3] Write integration test: test_delete_task_via_menu()
  - Add task via menu → delete via menu → verify removed from list

**Success Criteria**:
- ✅ delete_task() accepts task ID as parameter
- ✅ Removes task if found; displays nothing if successful deletion
- ✅ Displays "Task with ID X not found." if ID doesn't exist
- ✅ Returns True if deleted, False if not found
- ✅ List remains unchanged if delete fails
- ✅ Next task created after deletion gets next sequential ID
- ✅ 4 unit tests + 1 integration test written and passing
- ✅ Cumulative coverage for US1+US2+US3 >= 80%

---

## Phase 6: User Story 4 - Update Task (P2 - Valuable Enhancement)

**User Story**: As a user, I want to update a task's title and/or description by ID so that I can modify task details.

**Acceptance Scenarios** (from spec.md):
1. Update title only (Enter for description keeps original)
2. Update description only (Enter for title keeps original)
3. Non-existent task displays error; no changes made
4. Success message displays only if changes made

**Dependencies**: Phase 2 (Foundational) + Phase 3 (US1 - add_task required for testing)
**Independent Test**: Add task → update fields → verify changes persisted correctly
**Test Approach**: 4 unit tests for update_task() covering partial updates, no changes, invalid ID

### Tasks

- [ ] T033 [P] [US4] Write failing test: test_update_task_title_only()
  - Create task, update title (new value) + description (empty/Enter), verify title changed, desc unchanged

- [ ] T034 [P] [US4] Write failing test: test_update_task_description_only()
  - Create task, update title (empty/Enter) + description (new value), verify desc changed, title unchanged

- [ ] T035 [P] [US4] Write failing test: test_update_task_not_found_error()
  - Attempt to update non-existent ID 99, verify error message, return False, no changes made

- [ ] T036 [P] [US4] Write failing test: test_update_task_no_changes_no_message()
  - Create task, update both fields with Enter/no input, verify no changes, success message not printed

- [ ] T037 [US4] Implement update_task() function in src/main.py: signature `update_task(tasks: list[dict], task_id: int) -> bool`
  - RED: Tests T033-T036 fail
  - GREEN: Find task, display current values, prompt for new title (Enter = keep), prompt for desc (Enter = keep), update if changed, print success only if changed, return True if found
  - REFACTOR: Extract prompting logic, add docstring, type hints
  - **Accept**: All 4 tests pass; partial updates work; no changes mode works; error handling correct

- [ ] T038 [P] [US4] Write integration test: test_update_task_via_menu()
  - Add task → update via menu → view to verify changes persisted

**Success Criteria**:
- ✅ update_task() accepts task ID as parameter
- ✅ Displays current title and description
- ✅ Prompts for new title (Enter = keep original)
- ✅ Prompts for new description (Enter = keep original)
- ✅ Updates task if changes made
- ✅ Displays "Task updated." only if changes made (not for no-op updates)
- ✅ Returns True if task found, False if not found
- ✅ Displays "Task with ID X not found." if ID doesn't exist
- ✅ 4 unit tests + 1 integration test written and passing

---

## Phase 7: User Story 5 - Mark Task Complete/Incomplete (P2 - Valuable Enhancement)

**User Story**: As a user, I want to toggle a task's completion status by ID so that I can track which tasks are done.

**Acceptance Scenarios** (from spec.md):
1. Toggle incomplete → complete displays "Task marked as complete."
2. Toggle complete → incomplete displays "Task marked as incomplete."
3. Non-existent task displays error; no changes made
4. Toggled task displays correct status indicator [ ]/[✓] in list view

**Dependencies**: Phase 2 (Foundational) + Phase 3 (US1, US2 - add and view required for testing)
**Independent Test**: Add task → toggle complete → verify status changed and message displayed
**Test Approach**: 3 unit tests for toggle_complete() covering both directions, not found

### Tasks

- [ ] T039 [P] [US5] Write failing test: test_toggle_complete_incomplete_to_complete()
  - Create task with complete=False, toggle, verify complete=True, message says "Task marked as complete."

- [ ] T040 [P] [US5] Write failing test: test_toggle_complete_complete_to_incomplete()
  - Create task with complete=True, toggle, verify complete=False, message says "Task marked as incomplete."

- [ ] T041 [P] [US5] Write failing test: test_toggle_complete_not_found_error()
  - Attempt to toggle non-existent ID 99, verify error message, return False, no changes made

- [ ] T042 [US5] Implement toggle_complete() function in src/main.py: signature `toggle_complete(tasks: list[dict], task_id: int) -> bool`
  - RED: Tests T039-T041 fail
  - GREEN: Find task, invert complete status (not complete), print appropriate message, return True if found
  - REFACTOR: Use find_task() helper, add docstring, type hints
  - **Accept**: All 3 tests pass; toggle works both directions; error handling correct; message matches spec

- [ ] T043 [P] [US5] Write integration test: test_toggle_complete_via_menu()
  - Add task → toggle via menu → view to verify status changed to [✓]

- [ ] T044 Implement main() event loop in src/main.py: signature `main() -> None`
  - Initialize empty task list: `tasks: list[dict] = []`
  - Loop: display menu → get choice → dispatch to operation (1=add, 2=view, 3=update, 4=delete, 5=toggle, 0=exit) → continue
  - On exit (0): print "Goodbye!" and break loop
  - **Accept**: Calls all 5 operations correctly; menu displays; transitions between operations work

- [ ] T045 Write integration test: test_main_complete_workflow()
  - Execute full app workflow: add 3 tasks → view → update 1 → toggle 1 → delete 1 → view final state
  - Verify all operations work together without crashes

- [ ] T046 Verify pytest coverage >= 80%: run `pytest tests/ --cov=src --cov-report=term-missing`
  - Generate coverage report
  - Document coverage percentage
  - **Accept**: Coverage >= 80%; all functions have tests; no untested code paths

**Success Criteria**:
- ✅ toggle_complete() accepts task ID as parameter
- ✅ Inverts task complete status (False → True, True → False)
- ✅ Displays "Task marked as complete." when toggling to True
- ✅ Displays "Task marked as incomplete." when toggling to False
- ✅ Returns True if toggled, False if not found
- ✅ Displays "Task with ID X not found." if ID doesn't exist
- ✅ Status indicator [✓] appears in list view when complete=True
- ✅ Status indicator [ ] appears in list view when complete=False
- ✅ main() event loop initializes empty task list
- ✅ main() displays menu and accepts choice 0-5
- ✅ main() dispatches to correct operation based on choice
- ✅ main() exits gracefully on choice 0 (prints "Goodbye!")
- ✅ 3 unit tests + 2 integration tests written and passing
- ✅ All 50+ tests passing; coverage >= 80%

---

## Phase 8: Code Quality & Polish

**Goal**: Ensure all code meets quality standards, add comprehensive documentation, and prepare for release.

**Dependencies**: All user story phases complete; all tests passing

### Tasks

- [ ] T047 Code quality review: verify all functions have type hints and docstrings
  - Checklist: Every function has `def func(arg: type) -> type:` signature
  - Every function has docstring explaining purpose, args, returns, usage
  - No commented-out code or debug print statements

- [ ] T048 PEP 8 compliance check: verify code formatting
  - Line length < 100 characters (except long strings)
  - 4-space indentation throughout
  - No trailing whitespace
  - Module docstring at top of src/main.py

- [ ] T049 Create README.md with project description, setup instructions, usage examples
  - Title, description, requirements (Python 3.13+, UV)
  - Installation: `uv init`, `uv venv`, `uv sync`
  - Running: `python src/main.py`
  - Testing: `pytest tests/ -v`
  - Features: Brief description of 5 operations

- [ ] T050 Final manual testing: execute `python src/main.py` and verify all 5 operations work
  - Add 3 tasks with various content
  - View list
  - Update 1 task
  - Delete 1 task
  - Toggle completion status
  - View final list
  - Exit gracefully (Ctrl+C or option 0)
  - **Accept**: All operations execute without crashes; no unhandled exceptions

- [ ] T051 Create git commit with all implementation: `git add src/ tests/ specs/ && git commit -m "feat: implement todo app phase I core"`
  - Commit message includes summary of 5 features and test coverage
  - All files staged and committed
  - Verify with `git log -1`

**Success Criteria**:
- ✅ All functions have type hints (parameters and return types)
- ✅ All functions have docstrings (purpose, args, returns)
- ✅ PEP 8 compliant (formatting, naming, style)
- ✅ No debug code, commented-out code, or print statements for debugging
- ✅ README.md describes project, setup, and usage
- ✅ Manual testing successful (all 5 features work, graceful error handling)
- ✅ Git commit created with descriptive message
- ✅ All 50+ tests passing with 80%+ coverage

---

## Test Coverage Target

**Total Test Count**: 50+ tests
- **Data Model Tests**: 5-10 (dict structure, ID uniqueness, whitespace handling, status toggle)
- **Helper Function Tests**: 5 (find_task x3, get_next_id x3)
- **Core Operation Tests**: 20+ (add x3, delete x3, update x4, view x2-3, toggle x3)
- **UI Function Tests**: 10+ (menu display, input validation, error messages, edge cases)
- **Integration Tests**: 5+ (complete workflows, sequential operations, state consistency)

**Coverage Requirement**: >= 80% of src/main.py code
**Test Framework**: pytest (optional dev dependency)

---

## Implementation Notes

### Red-Green-Refactor TDD Cycle

For each function (or set of related functions):

1. **RED**: Write failing test(s) that specify expected behavior
   ```python
   def test_add_task_creates_task_with_id_1_in_empty_list():
       tasks = []
       # Simulate user input: title="Buy groceries", desc="Milk, eggs"
       # Call add_task(tasks)
       assert len(tasks) == 1
       assert tasks[0]["id"] == 1
       assert tasks[0]["title"] == "Buy groceries"
   ```

2. **GREEN**: Implement minimal code to make test pass
   ```python
   def add_task(tasks: list[dict]) -> None:
       title = input("Title: ")
       desc = input("Description: ")
       task_id = get_next_id(tasks)
       tasks.append({"id": task_id, "title": title, "desc": desc, "complete": False})
       print(f"Task added successfully (ID: {task_id}).")
   ```

3. **REFACTOR**: Improve code quality without changing logic
   - Add type hints
   - Add docstrings
   - Extract duplicated code
   - Ensure PEP 8 compliance
   - Do NOT change the behavior tested by the failing test

### Independent Test Strategy

Each user story is independently testable:
- US1 (Add): Test by creating task and verifying it in list
- US2 (View): Test by viewing empty list and populated list
- US3 (Delete): Test by deleting and verifying removal
- US4 (Update): Test by updating fields and verifying persistence
- US5 (Toggle): Test by toggling status and verifying change

All user stories can be tested after Phase 2 (Foundational) is complete, but US1-3 (MVP) should be prioritized before US4-5.

### Parallel Implementation

After Phase 2 is complete:
- US4 (Update) and US5 (Toggle) can be implemented in parallel (no dependencies between them)
- However, US1, US2, US3 must complete before the main() event loop is fully tested
- Recommended: Complete US1-3 first (MVP), then US4-5 in parallel

---

## Success Metrics

| Metric | Target | Verification |
|--------|--------|--------------|
| **MVP Functional** | All 5 features work without crashes | Manual testing + integration tests |
| **Code Quality** | Type hints, docstrings, PEP 8 | Code review + linting checks |
| **Test Coverage** | >= 80% of codebase | `pytest --cov` report |
| **Spec Compliance** | All acceptance scenarios pass | Test cases mapped 1:1 to spec |
| **UI Polish** | Clear menu, graceful error handling | Manual testing demo |
| **No External Deps** | Standard library only | Dependency audit (pyproject.toml) |

---

## Next Steps

1. **Begin Phase 1**: Initialize UV project and create directory structure (T001-T010)
2. **Complete Phase 2**: Implement foundational helper and UI functions (T011-T016)
3. **Execute Phases 3-7**: Implement user stories in priority order (T017-T043)
4. **Complete Phase 8**: Final code quality review and release (T047-T051)
5. **Verification**: Run full test suite and manual testing
6. **Release**: Push to GitHub branch `1-todo-app-core`

---

**Tasks Version**: 1.0
**Status**: Ready for Implementation
**Recommended Start**: Phase 1, Task T001

