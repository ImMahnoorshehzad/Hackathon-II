---
ID: 2
TITLE: Generate Implementation Plan - Architecture & Design
STAGE: plan
DATE_ISO: 2025-12-28
SURFACE: agent
MODEL: claude-haiku-4-5-20251001
FEATURE: 1-todo-app-core
BRANCH: 1-todo-app-core
USER: system
COMMAND: /sp.plan
LABELS: ["architecture", "design", "data-model", "function-contracts", "tdd-strategy", "implementation-roadmap"]
LINKS:
  SPEC: specs/1-todo-app-core/spec.md
  TICKET: null
  ADR: null
  PR: null
FILES_YAML:
  - specs/1-todo-app-core/plan.md
TESTS_YAML: []
---

## Prompt

Execution Plan: Todo App Phase I

1. UV Initialization: Run 'uv init --python 3.13', create requirements.txt, 'uv venv', 'uv sync'.
2. Repo Setup: Create folders (/src, specs history), files (/sp.constitution, README.md, CLAUDE.md).
3. Spec Generation: Write /sp.specify, version in history.
4. Code Build: Use subagents to generate /src/main.py with menu and features.
5. Testing: Add /src/tests.py, run tests.
6. Run: Demonstrate with 'python src/main.py'.
7. GitHub: Commit all, push to repo.

---

## Response

### Implementation Plan Generated: Todo App Phase I Core (v1.0)

**Feature Branch**: `1-todo-app-core`
**Created**: 2025-12-28
**Status**: Final Plan – Ready for Task Generation
**Specification**: [spec.md](spec.md)

I have generated a comprehensive architectural design and implementation plan for the Todo App Phase I Core. The plan addresses all phases from technical context through deployment and includes detailed function contracts, data model specifications, and TDD strategy.

### Plan Structure

**Phase 0: Technical Context & Unknowns**
- ✅ Constitutional requirements check: ALL PASS
- ✅ Technical decisions documented (language, storage, CLI, testing)
- ✅ No [NEEDS CLARIFICATION] markers – specification is unambiguous
- ✅ Research tasks completed (Python 3.13, in-memory storage, CLI patterns, validation, ID strategies)

**Phase 1: Design & Architecture**
- ✅ Data Model: Task entity with 4 fields (id, title, desc, complete)
- ✅ State Transitions: New → (Mark Complete/Incomplete) → Delete
- ✅ Function Contracts: 2 helpers + 5 core operations + 4 UI functions + main loop
- ✅ Code Organization: src/main.py structure with ~400-500 lines
- ✅ Technology Stack: Python 3.13+, UV, in-memory list, pytest (optional dev)
- ✅ Input Validation: Complete matrix of all input types and error handling

**Phase 2: Implementation Strategy**
- ✅ Red-Green-Refactor TDD Cycle: Detailed process for each function
- ✅ Implementation Order: Helpers → Core Ops → UI → Main Loop → Tests
- ✅ Test Strategy: 50+ tests across 5 categories (data model, helpers, operations, UI, integration)
- ✅ Code Quality Standards: Type hints, docstrings, PEP 8, no boilerplate

**Phase 3: Deployment & Release**
- ✅ Build Steps: UV init (done) → Implementation → Testing → Manual testing → Commit
- ✅ GitHub Workflow: Commit, push, optional PR
- ✅ Success Criteria: 6 measurable acceptance points
- ✅ Risk Assessment: 4 identified risks with mitigations

### Architectural Decisions

**1. Data Model**
- **Decision**: Store tasks as list of dictionaries with {id, title, desc, complete}
- **Rationale**: Simple, in-memory, matches specification requirements, easy to test
- **Alternatives Considered**: ORM (too complex), database (violates Phase I), namedtuple (less flexible)
- **Invariants Enforced**: Unique IDs, sequential numbering, immutable ID field, ephemeral storage

**2. ID Generation Strategy**
- **Decision**: Use `max(existing_ids) + 1` or 1 if empty via get_next_id() helper
- **Rationale**: Handles deletions correctly (no gap-filling needed), simple to understand, testable
- **Alternatives Considered**: UUID (overkill), increment counter (requires state), array length (breaks with deletions)
- **Implementation**: Helper function ensures single source of truth

**3. Function Architecture**
- **Decision**: Modular design with 2 helpers + 5 core ops + 4 UI funcs + main loop
- **Rationale**: Separation of concerns (data, business logic, UI), reusable helpers, testable units
- **Alternatives Considered**: Monolithic main() (hard to test), class-based (over-engineered)
- **Dependency**: Helper functions used by all operations

**4. Input Validation Strategy**
- **Decision**: Validate at point of input; re-prompt on error; catch Ctrl+C gracefully
- **Rationale**: Ensures data quality, prevents crashes, user-friendly experience
- **Alternatives Considered**: Validate on operation (incomplete), no validation (crashes)
- **Implementation**: get_int_input() and confirm() helpers handle validation loops

**5. Error Handling Approach**
- **Decision**: Print clear error messages; re-prompt or continue; no exceptions from user input
- **Rationale**: CLI should not crash on user error; guidance helps users correct mistakes
- **Alternatives Considered**: Strict validation (poor UX), no error handling (crashes)
- **Examples**: "Task with ID X not found.", "Invalid input. Please enter a valid integer."

### Function Contracts (Detailed)

**Helper Functions** (Foundation):
- `find_task(tasks, task_id) → dict | None` – Search-once, reusable across all operations
- `get_next_id(tasks) → int` – ID generation, ensures uniqueness and sequencing

**Core Operations** (Business Logic):
- `add_task(tasks) → None` – Create tasks interactively, auto-assign ID
- `delete_task(tasks, task_id) → bool` – Remove tasks safely, handle missing IDs
- `update_task(tasks, task_id) → bool` – Modify title/desc with optional fields
- `print_tasks(tasks) → None` – Display formatted list or empty state message
- `toggle_complete(tasks, task_id) → bool` – Toggle completion status, show appropriate message

**UI Functions** (User Interaction):
- `display_menu() → None` – Display exact 6-option menu format
- `get_menu_choice() → int` – Display menu and return valid choice (0-5)
- `get_int_input(prompt) → int` – Get validated integer with error handling
- `confirm(prompt) → bool` – Get yes/no confirmation with flexible input

**Main Event Loop**:
- `main() → None` – Initialize empty task list, loop menu-operation-continue until exit

### Code Organization

**File: src/main.py** (~400-500 lines)
```
Imports (sys, typing)
├── Helper Functions (find_task, get_next_id)
├── Core Operations (add, delete, update, print, toggle)
├── UI Functions (menu, choice, int input, confirm)
├── Main Event Loop
└── Entry Point
```

**File: tests/test_main.py** (~400+ lines)
```
Imports (pytest, sys.path adjustment)
├── Data Model Tests (5-10 tests)
├── Helper Function Tests (5 tests)
├── Core Operation Tests (20+ tests)
├── UI Function Tests (10+ tests)
└── Integration Tests (5+ tests)
```

### TDD Implementation Strategy

**Red-Green-Refactor Cycle for Each Function:**

1. **RED** – Write failing test first
   - Test expected behavior from spec acceptance scenarios
   - Example: `def test_add_task_creates_task_with_id_1():`
   - Run; verify test fails

2. **GREEN** – Implement minimal code to pass
   - Write just enough to make test pass
   - No over-engineering or future-proofing
   - Example: Create dict, append, print message

3. **REFACTOR** – Improve without changing logic
   - Extract helpers, add type hints, add docstrings
   - Ensure PEP 8 compliance
   - No logic changes; quality improvements only

**Implementation Order**:
1. Helpers (foundation for all operations)
2. Core operations (business logic)
3. UI functions (user interaction)
4. Main loop (orchestration)
5. Comprehensive tests (coverage >= 80%)

### Test Coverage Strategy

**50+ Tests Across 5 Categories:**

| Category | Tests | Focus |
|----------|-------|-------|
| Data Model | 5-10 | Dict structure, ID uniqueness, whitespace, status toggle |
| Helpers | 5 | find_task (found/not found/empty), get_next_id (empty/single/multiple) |
| Operations | 20+ | Add (empty/multiple/whitespace), View (empty/single/multiple), Delete (exists/not/cascade), Update (both/partial/no-change), Toggle (both directions/not found) |
| UI | 10+ | Menu format, input validation, error messages, edge cases |
| Integration | 5+ | Complete workflows, sequential ops, state consistency |

**Success Criterion**: >= 80% code coverage; all acceptance scenarios have tests

### Risk Assessment & Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| **Complex input validation** | Crashes on edge cases | Comprehensive test cases for all input types (Ctrl+C, empty, non-numeric, etc.) |
| **ID management errors** | Data corruption, duplicate IDs | Helper function (get_next_id) with dedicated tests; invariants enforced |
| **Scope creep** | Phase I not completed | Scope locked in constitution; Phase II clearly delineated for extensions |
| **Poor test coverage** | Bugs in production | TDD enforced; minimum 80% coverage required; all acceptance scenarios tested |

### Success Criteria

| Criterion | Target | Verification |
|-----------|--------|--------------|
| **MVP Functional** | All 5 features work without crashes | Manual testing + integration tests |
| **Code Quality** | Type hints, docstrings, PEP 8 | Code review + linting checks |
| **Test Coverage** | >= 80% of codebase | pytest coverage report |
| **Spec Compliance** | All acceptance scenarios pass | Test cases mapped 1:1 to spec scenarios |
| **UI Polish** | Clear menu, graceful error handling | Manual testing; demo execution |
| **No External Deps** | Standard library only | Dependency audit (pyproject.toml) |

### Deployment Checklist

- [ ] UV initialization complete (uv init --python 3.13, uv venv, uv sync)
- [ ] src/main.py implemented with all functions
- [ ] tests/test_main.py written with 50+ tests
- [ ] All tests pass (pytest tests/ -v)
- [ ] Coverage >= 80% (pytest --cov)
- [ ] Manual testing: python src/main.py (all 5 features work)
- [ ] Code quality: type hints, docstrings, PEP 8 verified
- [ ] Commit: git add src/ tests/ specs/ && git commit -m "feat: implement todo app phase I core"
- [ ] Push: git push origin 1-todo-app-core
- [ ] PR created (optional): Reference spec, acceptance scenarios

### Recommended Next Steps

1. **Task Generation**: Run `/sp.tasks` to generate testable, dependency-ordered work items
2. **Implementation**: Execute tasks in order using red-green-refactor TDD
3. **Testing**: Run pytest to verify all tests pass (coverage >= 80%)
4. **Manual Testing**: Execute `python src/main.py` and test all 5 features
5. **Code Review**: Verify type hints, docstrings, PEP 8 compliance
6. **Commit & Push**: Create git commit and push to origin

---

## Outcome

✅ **Implementation Plan Complete and Ready for Task Generation**

The architectural design and implementation plan is production-ready and fully aligned with:
- Todo App Evolution - Phase I Constitution (v1.0.0)
- Feature Specification: Todo App Phase I Core (v1.0)
- Spec-Driven Development (SDD) methodology

The plan includes:
- ✅ Unambiguous data model with invariants
- ✅ Complete function contracts for 11 functions
- ✅ Detailed TDD strategy with implementation order
- ✅ 50+ test cases across 5 categories (80%+ coverage target)
- ✅ Risk assessment with mitigations
- ✅ Deployment checklist and success criteria

**Next Command**: `/sp.tasks` to generate testable, dependency-ordered implementation tasks.

