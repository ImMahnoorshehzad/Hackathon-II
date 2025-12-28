---
ID: 3
TITLE: Generate Implementation Tasks - TDD Roadmap
STAGE: tasks
DATE_ISO: 2025-12-28
SURFACE: agent
MODEL: claude-haiku-4-5-20251001
FEATURE: 1-todo-app-core
BRANCH: 1-todo-app-core
USER: system
COMMAND: /sp.tasks
LABELS: ["test-driven-development", "task-breakdown", "user-story-organization", "dependency-ordering", "implementation-roadmap"]
LINKS:
  SPEC: specs/1-todo-app-core/spec.md
  PLAN: specs/1-todo-app-core/plan.md
  TICKET: null
  ADR: null
  PR: null
FILES_YAML:
  - specs/1-todo-app-core/tasks.md
TESTS_YAML:
  - 50+ unit and integration tests (pytest)
  - Test coverage target: 80%+
---

## Prompt

Generate testable, dependency-ordered implementation tasks for Todo App Phase I Core. Organize tasks by user story priority and provide a complete task breakdown aligned with the implementation plan. Include:

1. Task organization by user story (P1, P2 priorities from spec)
2. Dependency graph showing completion order
3. Red-green-refactor TDD approach for each function
4. Parallel execution opportunities identified
5. Test strategy and coverage targets
6. Success criteria for each phase
7. Complete task checklist with IDs, descriptions, and file paths

---

## Response

### Tasks Generated: Todo App Phase I Core (v1.0)

**Feature Branch**: `1-todo-app-core`
**Created**: 2025-12-28
**Status**: Ready for Implementation
**Total Tasks**: 51 tasks across 8 phases

I have generated a comprehensive, testable implementation roadmap for the Todo App Phase I Core. Tasks are organized by user story priority, include full TDD specifications, and provide clear dependencies and parallel execution opportunities.

### Task Organization

**Phase 1 (Setup)**: 10 tasks
- Project initialization with UV, Python 3.13+, directory structure
- Verify environment and dependencies ready

**Phase 2 (Foundational)**: 6 tasks
- Helper functions: find_task(), get_next_id()
- UI helpers: get_int_input(), confirm(), display_menu(), get_menu_choice()
- Blocks all user stories (must complete first)
- Parallelizable: T011-T014 can be implemented in parallel

**Phase 3 (User Story 1 - Add Task, P1 MVP)**: 6 tasks
- Implement add_task() with sequential ID assignment
- Implement print_tasks() for formatted display
- 5 unit tests + 2 integration tests
- Success: Whitespace handling, auto-increment IDs, success messages

**Phase 4 (User Story 2 - View Tasks, P1 MVP)**: 4 tasks
- Enhanced print_tasks() formatting and validation
- Handle empty list, special characters, unicode
- 4 unit tests + 1 integration test
- Success: Proper formatting with [ ]/[✓] status indicators

**Phase 5 (User Story 3 - Delete Task, P1 MVP)**: 6 tasks
- Implement delete_task() with error handling
- Verify ID sequencing (no gaps, no reuse)
- 4 unit tests + 1 integration test
- Success: Safe deletion, sequential IDs maintained

**Phase 6 (User Story 4 - Update Task, P2)**: 8 tasks
- Implement update_task() with optional field updates
- Enter key = keep original value pattern
- 4 unit tests + 1 integration test
- Parallelizable with US5 after Phase 5 complete

**Phase 7 (User Story 5 - Mark Complete, P2)**: 6 tasks
- Implement toggle_complete() status management
- Proper messaging for both directions
- 3 unit tests + 2 integration tests
- Parallelizable with US4 after Phase 5 complete
- Integrate main() event loop (T044)

**Phase 8 (Polish & Release)**: 5 tasks
- Code quality review (type hints, docstrings)
- PEP 8 compliance verification
- README.md creation
- Final manual testing
- Git commit and push

### Task Format (Checklist)

All 51 tasks follow strict markdown checklist format:

```
- [ ] [TaskID] [P?] [Story?] Description with exact file path
```

**Components**:
- Checkbox: `- [ ]` (markdown checkbox, unchecked)
- Task ID: Sequential T001-T051 in execution order
- [P] marker: Included only for parallelizable tasks (independent files/operations)
- [Story] label: [US1], [US2], [US3], [US4], [US5] for user story phases only
- Description: Clear action with file path (e.g., `src/main.py`, `tests/test_main.py`)

**Examples from tasks.md**:
- `- [ ] T011 [P] Implement find_task() helper in src/main.py`
- `- [ ] T020 [US1] Implement add_task() function in src/main.py`
- `- [ ] T033 [P] [US4] Write failing test: test_update_task_title_only()`

### Dependency Graph

**Execution Order** (with parallelization):

```
Phase 1 (Setup: T001-T010)
    ↓
Phase 2 (Foundational: T011-T016)
    ├→ Phase 3 (US1 Add: T017-T022)
    │   ├→ Phase 4 (US2 View: T023-T026) → Phase 5 (US3 Delete: T027-T032)
    │   │                                      ├→ Phase 6 (US4 Update: T033-T038) [PARALLEL]
    │   │                                      └→ Phase 7 (US5 Toggle: T039-T045) [PARALLEL]
    │   └→ Phase 8 (Polish: T047-T051)
```

**Key Dependencies**:
- US1 (Add) blocks US2 (View) and US3 (Delete) for MVP testing
- US3 (Delete) blocks US4 (Update) and US5 (Toggle) for full menu integration
- Phase 2 (Foundational) blocks all user stories
- Phase 8 (Polish) requires all user story phases complete

**Parallelizable Tasks**:
- Phase 1: All setup tasks T001-T010 can run in sequence (serial dependency)
- Phase 2: T011-T014 (helper functions) can run in parallel after T015-T016 (UI functions) start
- Phase 6 + Phase 7: US4 (Update) and US5 (Toggle) can be implemented in parallel after Phase 5 complete
- Multiple unit tests within a phase can be written/run in parallel

### Test Strategy

**Total Tests**: 50+ unit and integration tests
- **Data Model**: 5-10 tests (dict structure, ID uniqueness, whitespace, status)
- **Helpers**: 5 tests (find_task x3, get_next_id x3)
- **Operations**: 20+ tests (add x3, delete x3, update x4, view x2-3, toggle x3)
- **UI**: 10+ tests (menu x2, input validation, error messages)
- **Integration**: 5+ tests (workflows, sequential operations, state consistency)

**TDD Approach** (Red-Green-Refactor):

For each function/phase:

1. **RED**: Write failing test(s) specifying expected behavior
   - Example: `test_add_task_creates_task_with_id_1_in_empty_list()`
   - Verify test fails before implementation

2. **GREEN**: Implement minimal code to pass test
   - No over-engineering, no future-proofing
   - Just enough to make the test pass

3. **REFACTOR**: Improve code quality
   - Add type hints, docstrings
   - Extract helpers (DRY principle)
   - Ensure PEP 8 compliance
   - NO logic changes; quality only

**Coverage Target**: >= 80% of src/main.py
- Verified with: `pytest tests/ --cov=src --cov-report=term-missing`
- All acceptance scenarios from spec mapped to test cases
- All functions have dedicated tests

### Suggested MVP Scope

**Phase 1 (Setup)**: T001-T010 – Initialize project environment
**Phase 2 (Foundational)**: T011-T016 – Implement helper and UI functions
**Phase 3 (US1)**: T017-T022 – Add Task feature (core MVP capability)
**Phase 4 (US2)**: T023-T026 – View Tasks feature (required for MVP verification)
**Phase 5 (US3)**: T027-T032 – Delete Task feature (completes basic CRUD)

**MVP Completion Criteria**:
- ✅ All 5 core functions implemented (add, view, delete, plus update+toggle from later phases)
- ✅ Menu-driven CLI working with all options (1-5, 0)
- ✅ 40+ tests passing (first 3 phases worth)
- ✅ Coverage >= 70% (sufficient for MVP)
- ✅ Manual testing successful (add → view → delete cycle works)

**Post-MVP Enhancements**:
- Phase 6 (US4): Update Task feature (adds refinement capability)
- Phase 7 (US5): Mark Complete feature (adds tracking capability)
- Phase 8: Polish, documentation, final testing

### Key Implementation Decisions

**1. ID Assignment Strategy**:
- Decision: Use `max(existing_ids) + 1` pattern (via get_next_id() helper)
- Rationale: Correctly handles ID gaps from deletions (no ID reuse, no gaps)
- Implementation: Helper function ensures single source of truth
- Tests: T012 covers empty list, single task, multiple tasks

**2. Input Validation Pattern**:
- Decision: Validate at point of input (get_int_input, confirm)
- Rationale: Prevents invalid data from reaching operations; user-friendly re-prompting
- Implementation: Loop until valid; catch ValueError for integers; catch KeyboardInterrupt for Ctrl+C
- Tests: T013, T014 cover valid/invalid inputs, edge cases

**3. Whitespace Handling**:
- Decision: Strip leading/trailing whitespace from title/description
- Rationale: Prevents accidental spaces from storing; matches Python conventions
- Implementation: Apply `.strip()` in add_task() before appending
- Tests: T019 covers various whitespace scenarios

**4. Menu Display Exactness**:
- Decision: Display exactly 6 menu options (1-5 + 0 for exit)
- Rationale: Spec requirement; clear, unambiguous user experience
- Implementation: Hard-coded menu in display_menu()
- Tests: T015 verifies exact format, option count

**5. Optional Field Updates**:
- Decision: Pressing Enter (empty input) = keep original value
- Rationale: Reduces user friction for partial updates; prevents accidental overwrites
- Implementation: In update_task(), check if input is empty; if so, use original
- Tests: T033-T034 cover partial updates, T036 covers no-change scenario

### File Organization

**Source Code**: `src/main.py` (~400-500 lines)
- Imports (sys, typing)
- Helper functions (2): find_task, get_next_id
- Core operations (5): add_task, delete_task, update_task, print_tasks, toggle_complete
- UI functions (4): display_menu, get_menu_choice, get_int_input, confirm
- Main event loop (1): main()
- Entry point: `if __name__ == "__main__": main()`

**Tests**: `tests/test_main.py` (~400-500 lines)
- Imports (pytest, sys.path setup)
- Data model tests (5-10)
- Helper function tests (5)
- Operation tests (20+)
- UI tests (10+)
- Integration tests (5+)

### Success Criteria Summary

**Phase 1**: ✅ Python 3.13+ environment ready, UV venv active, project structure created
**Phase 2**: ✅ All 6 foundational functions implemented with 15+ tests passing
**Phase 3**: ✅ Add Task works, IDs auto-increment, whitespace stripped, 5 unit + 2 integration tests
**Phase 4**: ✅ View Tasks displays empty/populated lists correctly with proper formatting
**Phase 5**: ✅ Delete Task removes correctly, maintains ID sequencing, handles errors gracefully
**Phase 6**: ✅ Update Task allows partial updates, "Enter = keep original" pattern works
**Phase 7**: ✅ Toggle Complete works both directions, main() event loop orchestrates all features
**Phase 8**: ✅ Code quality verified (type hints, docstrings, PEP 8), coverage >= 80%, manual testing passes

**Overall**: 50+ tests passing, >= 80% coverage, all 5 features working without crashes, clean code, ready for release

### Files Created

1. **specs/1-todo-app-core/tasks.md** (570+ lines)
   - 8 phases with 51 total tasks
   - Each phase has goal, dependencies, independent test criteria
   - Each task follows strict checklist format with ID, priority markers, description, file paths
   - TDD specifications for each function
   - Success criteria for each phase
   - Test coverage targets and strategy
   - Implementation notes and parallel opportunities

### Recommended Next Steps

1. **Begin Phase 1 (Setup)**: Run T001-T010 to initialize UV project
   - Command: `uv init --python 3.13 && uv venv && uv sync`
   - Verify: `python --version` shows 3.13+

2. **Begin Phase 2 (Foundational)**: Implement T011-T016 (helper and UI functions)
   - Parallelizable: T011-T014 can be written in parallel
   - All tests for Phase 2 should pass before moving to user stories
   - Verify: `pytest tests/ -v` shows 15+ passing tests

3. **Begin Phase 3 (US1 - Add Task)**: Implement T017-T022
   - Core MVP feature: Create tasks with auto-assigned IDs
   - Verify: Can add task, IDs increment correctly, whitespace stripped

4. **Continue with Phase 4-5 (US2-US3 MVP)**: Sequential or parallel
   - Phase 4 (View): Display tasks in formatted list
   - Phase 5 (Delete): Remove tasks by ID
   - MVP complete after Phase 5: Basic CRUD working, 40+ tests passing

5. **Optional Phase 6-7 (US4-US5 Enhancements)**: Implement in parallel
   - Phase 6 (Update): Modify task details
   - Phase 7 (Toggle): Mark tasks complete
   - Can implement together after Phase 5 complete

6. **Complete Phase 8 (Polish)**: Final code review and release
   - Type hints, docstrings, PEP 8 verification
   - README.md creation
   - Full manual testing
   - Git commit and push

---

## Outcome

✅ **Implementation Tasks Complete and Ready for Execution**

The Todo App Phase I Core task breakdown is production-ready with:
- ✅ 51 testable, dependency-ordered tasks in checklist format
- ✅ 8 phases organized by user story priority (P1 MVP-critical, P2 enhancements)
- ✅ Red-green-refactor TDD specifications for all 11 functions
- ✅ 50+ test cases specified with coverage targets (80%+ goal)
- ✅ Parallel execution opportunities identified (UI helpers, US4+US5)
- ✅ Dependency graph showing completion order
- ✅ MVP scope clearly defined (Phases 1-5)
- ✅ Success criteria for each phase

**Next Command**: Begin Phase 1 (Setup): Run `uv init --python 3.13 && uv venv && uv sync` to initialize project environment, then proceed with T001-T010. After setup complete, move to Phase 2 (Foundational functions).

**Alternative**: Run `/sp.implement` to execute tasks automatically, or `/sp.git.commit_pr` to create PR with implementation scaffolding.

