<!--
SYNC IMPACT REPORT
==================
Version: 1.0.0 (from template → initial)
Ratified: 2025-12-28
Last Amended: 2025-12-28

Modified Principles:
- Principle 1: Spec-Driven Development (SDD) with SpecifyPlus
- Principle 2: Python 3.13+ & UV Mandatory Initialization
- Principle 3: Five Core Features Only (Add/Delete/Update/View/Mark Complete)
- Principle 4: In-Memory Storage (Phase I)
- Principle 5: Clean Code & No Boilerplate

Added Sections:
- Tech Stack Requirements (Python 3.13+, UV, standard library)
- Project Structure Requirements (GitHub repo, /src, specs history, README.md, CLAUDE.md)
- UV Initialization Rule (uv venv, uv sync mandatory)
- Deliverables (Working CLI app with all 5 features)

Removed Sections: None (initial constitution)

Templates Updated:
- ✅ .specify/templates/spec-template.md (ensure SDD alignment)
- ✅ .specify/templates/plan-template.md (ensure UV/Python requirements)
- ✅ .specify/templates/tasks-template.md (ensure feature scope alignment)
- ✅ CLAUDE.md (SDD guidance confirmed)

Follow-up TODOs: None (all placeholders filled)
-->

# Todo App Evolution - Phase I Constitution

## Core Principles

### I. Spec-Driven Development (SDD) with SpecifyPlus

**MUST** adhere to specification-driven development using SpecifyPlus methodology.

Every feature begins with a written specification (spec.md), proceeds through architectural planning (plan.md), defines testable tasks (tasks.md), and implements via red-green-refactor test-driven development. All agents and subagents follow this workflow strictly. No implementation without prior specification approval. Specs are living documents—amendments require new versions, version history tracking, and PHR (Prompt History Record) documentation.

**Rationale:** SDD ensures clarity, traceability, and alignment between user intent, design, and implementation. Reduces rework, prevents feature creep, and creates audit trail of decisions.

---

### II. Python 3.13+ & UV Package Manager Mandatory

**MUST** use Python 3.13 or newer as the runtime environment.

**MUST** initialize all projects with UV package manager (`uv init --python 3.13`).

UV is mandatory for dependency management, virtual environment creation (`uv venv`), and lock file generation (`uv.lock`). All Python dependencies MUST be declared in `pyproject.toml` with version pinning via `uv.lock`. No project initialization is valid without `uv venv` and `uv sync` completion.

**Rationale:** UV provides deterministic, fast, and reproducible Python environments. Python 3.13+ ensures modern syntax, performance improvements, and security patches. Lock files guarantee team consistency and reproducible CI/CD.

---

### III. Five Core Features Only (Phase I Scope)

**MUST** strictly implement only the following five core features:

1. **Add Task** – Create new tasks with auto-incremented ID, title, and description.
2. **View Tasks** – Display all tasks with completion status indicators in formatted list.
3. **Update Task** – Modify task title and/or description; optional field updates.
4. **Delete Task** – Remove task from list; safe deletion with error handling.
5. **Mark as Complete/Incomplete** – Toggle task completion status.

No additional features, CLI options, or scope expansion in Phase I. Each feature MUST have a dedicated spec, plan, tasks list, and passing test suite. Feature boundaries are non-negotiable; all requests for additional features are explicitly deferred to Phase II.

**Rationale:** Focused scope prevents scope creep, ensures quality, and delivers working product quickly. Phase II can extend with persistence, categories, priorities, and web interface.

---

### IV. In-Memory Storage (Phase I)

**MUST** use in-memory Python data structures (list of dictionaries) for task storage.

No database, file persistence, or external storage in Phase I. All tasks are lost when the application closes. Data structure: `tasks = [{"id": int, "title": str, "desc": str, "complete": bool}, ...]`. This design is intentional—Phase II will introduce persistence.

**Rationale:** In-memory storage is simple, fast, and eliminates infrastructure dependencies. Focuses team on feature implementation and testing logic. Persistence is a Phase II feature addition, not a Phase I requirement.

---

### V. Clean Code & No Boilerplate

**MUST** write clean, focused, and purposeful code.

Every function has a single responsibility. Type hints are mandatory (`def add_task(tasks: list[dict]) -> None:`). Docstrings with examples are mandatory. No commented-out code, no debug statements in commits, no unused imports. Code MUST be reviewed for clarity, maintainability, and adherence to PEP 8 before PR merge. Helper functions (`find_task()`, `get_next_id()`) are reusable utilities that eliminate duplication.

**Rationale:** Clean code is maintainable code. Future developers (including AI agents) can understand intent rapidly. Boilerplate obscures logic and wastes review time. Reusable helpers reduce defects and accelerate feature development.

---

## Tech Stack Requirements

**Python:** 3.13+
**Package Manager:** UV (mandatory; uv init, uv venv, uv sync)
**Dependencies:** Python standard library only (Phase I)
**Testing:** pytest (optional, added via `uv add --dev pytest`)
**CLI Framework:** None (use built-in input/print)
**Persistence:** None (Phase I; in-memory only)

All dependencies MUST be declared in `pyproject.toml` with explicit version constraints. Lock file (`uv.lock`) MUST be committed to repository. No transitive dependencies without documented justification.

---

## Project Structure Requirements

**Repository Structure:**
```
todo-app-phase-1/
├── .specify/
│   ├── memory/
│   │   └── constitution.md           # This file
│   ├── templates/
│   │   ├── spec-template.md
│   │   ├── plan-template.md
│   │   ├── tasks-template.md
│   │   └── phr-template.prompt.md
│   └── scripts/
│       └── bash/
│           └── create-phr.sh
├── history/
│   ├── prompts/
│   │   ├── constitution/             # Constitution amendment PHRs
│   │   ├── add-task/                 # Feature: Add Task
│   │   ├── delete-task/              # Feature: Delete Task
│   │   ├── update-task/              # Feature: Update Task
│   │   ├── view-tasks/               # Feature: View Tasks
│   │   ├── mark-complete/            # Feature: Mark Complete
│   │   └── general/                  # General PHRs
│   └── adr/                          # Architectural Decision Records
├── specs/
│   ├── add-task/
│   │   ├── spec.md
│   │   ├── plan.md
│   │   └── tasks.md
│   ├── delete-task/
│   │   ├── spec.md
│   │   ├── plan.md
│   │   └── tasks.md
│   ├── update-task/
│   │   ├── spec.md
│   │   ├── plan.md
│   │   └── tasks.md
│   ├── view-tasks/
│   │   ├── spec.md
│   │   ├── plan.md
│   │   └── tasks.md
│   └── mark-complete/
│       ├── spec.md
│       ├── plan.md
│       └── tasks.md
├── src/
│   └── main.py                       # Application entry point
├── tests/
│   └── test_main.py                  # Test suite
├── .python-version                   # 3.13
├── .gitignore
├── pyproject.toml                    # UV project configuration
├── uv.lock                           # Dependency lock file
├── README.md                         # Project overview & setup
└── CLAUDE.md                         # AI-assisted development guidance
```

**GitHub Repository:**
- Public or private; GitHub-hosted.
- Branch protection: `main` branch requires PR review before merge.
- Commit message format: `<type>: <description>` (e.g., `feat: add task creation`, `docs: update constitution`).
- All commits MUST include reference to spec/plan/tasks/PHR where applicable.

---

## UV Initialization Rule (Non-Negotiable)

**Project initialization MUST follow this exact sequence:**

```bash
# 1. Create and navigate to project directory
mkdir todo-app-phase-1
cd todo-app-phase-1

# 2. Install UV (if not present)
pip install uv

# 3. Initialize project with Python 3.13
uv init --python 3.13

# 4. Create virtual environment
uv venv

# 5. Activate virtual environment
source .venv/bin/activate  # Linux/macOS
# or: .venv\Scripts\activate.bat  # Windows

# 6. Sync dependencies
uv sync

# 7. Create project directories
mkdir -p src tests .specify/memory

# 8. Create core files (main.py, test_main.py, constitution.md, etc.)
```

**MUST NOT** skip `uv venv` or `uv sync`. **MUST NOT** use pip directly for package management (use `uv add` and `uv remove`). **MUST** commit `pyproject.toml` and `uv.lock` to repository. **MUST** ensure CI/CD runs `uv sync` before testing.

**Rationale:** Strict initialization sequence ensures reproducible environments across developers, CI/CD, and containers. Eliminates "works on my machine" problems and enforces dependency transparency.

---

## Deliverables

**Phase I Deliverable: Working CLI Application**

The Todo App Phase I MUST deliver:

1. **Executable CLI Program** – `python src/main.py` launches interactive menu-driven interface.
2. **All Five Features Functional** – Add, View, Update, Delete, Mark Complete operations work without error.
3. **Clean User Interaction** – Menu displays options 0-5, accepts input, displays results and errors clearly.
4. **Error Handling** – Graceful handling of invalid input, non-existent task IDs, empty lists.
5. **Complete Test Suite** – All functions tested; minimum 80% code coverage; passing before release.
6. **Full Documentation** – README.md with setup/usage, specs for all features, CLAUDE.md guidance, constitution.
7. **Spec-Driven Artifacts** – All features have spec.md, plan.md, tasks.md, and PHR history.
8. **Clean Codebase** – Type hints, docstrings, PEP 8 compliant, no boilerplate, reusable helpers.

**Success Criteria:**
- ✅ App starts: `python src/main.py` without errors
- ✅ All 5 features work: user can add, view, update, delete, mark tasks
- ✅ Tests pass: `python -m pytest tests/ -v` shows all green
- ✅ Code quality: type hints, docstrings, <100 char lines, PEP 8
- ✅ Specifications complete: all features documented in specs/
- ✅ README complete: setup, usage, architecture, troubleshooting
- ✅ PHR history: every significant decision recorded

---

## Governance

**Constitution Authority:**
This constitution supersedes all other practices, guidelines, or informal agreements. In case of conflict, constitution rules are absolute. Amendments require explicit approval and documented version history.

**Amendment Procedure:**
1. Propose amendment with rationale to team/lead.
2. Create new version of constitution (increment version per semantic versioning).
3. Update dependent templates and guidance files.
4. Create PHR (Prompt History Record) documenting amendment.
5. Commit to repository with message: `docs: amend constitution to vX.Y.Z (<reason>)`.

**Compliance Review:**
- All PRs MUST verify compliance with constitution before merge.
- Spec/plan/tasks MUST enforce feature scope (5 features only).
- Code MUST include type hints and docstrings.
- Tests MUST achieve minimum coverage.
- Dependencies MUST be justified and pinned in uv.lock.

**Guidance Files:**
- **CLAUDE.md** – AI-assisted development practices and SDD workflow.
- **README.md** – Project overview, setup, usage examples.
- **FEATURES.md** – Detailed feature specifications (created via `create-project-file` skill).

---

**Version**: 1.0.0 | **Ratified**: 2025-12-28 | **Last Amended**: 2025-12-28
