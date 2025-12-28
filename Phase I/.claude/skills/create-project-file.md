# Skill: Generate Project Files from Specifications

**Owned by:** `lead-architect-todo`
**Feature:** Todo App Phase I - Project Foundation
**Status:** Production-Ready

---

## Purpose

Generate complete, production-ready project files based on specification inputs. This skill creates standardized project documentation and configuration files that establish project structure, setup instructions, feature specifications, and development guidelines. Output files are fully formatted and ready for immediate use in the Todo App Phase I project.

---

## When to Use

- **Project Initialization:** Create foundational files when setting up new project
- **Documentation Generation:** Generate README, setup guides, and feature lists
- **Configuration Setup:** Create configuration files for development environment
- **Specification Recording:** Document constitution, architecture decisions, and specifications
- **Template Generation:** Create standardized file templates for team consistency

---

## Inputs

**Function Signature:**
```
Input: File path (str), Content type (str)
Example: '/sp.constitution', 'rules'
Example: 'README.md', 'project-overview'

Output: Full file content (str) ready to write to disk
```

**Parameter Details:**

- **File Path** (str): Destination path for the file
  - Examples: `/sp.constitution`, `README.md`, `.specify/memory/constitution.md`
  - Can be absolute or relative
  - Type hint: `str`

- **Content Type** (str): Type of content to generate
  - Examples: 'rules', 'project-overview', 'setup-guide', 'features'
  - Determines template and formatting
  - Type hint: `str`

**Return Value:** `str`
- Complete, formatted file content
- Ready to write directly to disk
- Properly indented and structured

---

## File Templates

### 1. README.md (Project Overview)

**Path:** `README.md`
**Content Type:** `'project-overview'`

```markdown
# Todo App Phase I

A Python-based command-line task management application with in-memory storage, featuring a menu-driven interface for creating, viewing, updating, deleting, and tracking task completion status.

## Project Structure

```
todo-app/
├── src/
│   └── main.py           # Main application entry point
├── tests/
│   └── test_main.py      # Test suite
├── README.md             # Project documentation
├── pyproject.toml        # Python project configuration
├── .python-version       # Python version specification
└── .gitignore            # Git ignore rules
```

## Features

The Todo App Phase I includes the following core features:

1. **Add Task** - Create new tasks with title and description
   - Auto-incremented task IDs
   - Default completion status: incomplete
   - Whitespace handling on inputs

2. **View Tasks** - Display all tasks in a formatted list
   - Task ID with status indicator ([ ] incomplete, [✓] complete)
   - Task title and description
   - Handles empty task list gracefully

3. **Update Task** - Modify existing task details
   - Optional field updates (press Enter to keep original)
   - Update title, description, or both
   - Safe task lookup by ID

4. **Delete Task** - Remove tasks from the list
   - Confirmation recommended before deletion
   - Safe removal with error handling
   - Task not found handling

5. **Mark as Complete/Incomplete** - Toggle task completion status
   - Simple boolean toggle (complete ↔ incomplete)
   - Clear status messaging
   - Reversible operation

## Setup Instructions

### Prerequisites

- Python 3.6+
- `uv` package manager (install via: `pip install uv`)

### Installation

1. **Create and activate virtual environment:**
   ```bash
   uv venv
   ```

2. **Sync dependencies:**
   ```bash
   uv sync
   ```

3. **Run the application:**
   ```bash
   python src/main.py
   ```

### Directory Setup

The application expects the following structure:

```
project-root/
├── src/
│   └── main.py          # Application code (created by developer)
├── .venv/               # Virtual environment (created by uv venv)
└── pyproject.toml       # Project metadata (created by uv)
```

## Usage

### Starting the Application

```bash
python src/main.py
```

### Menu Operations

Upon starting, you'll see the main menu:

```
Todo App
========
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark as Complete/Incomplete
0. Exit

Choose an option:
```

**Menu Options:**
- **1 - Add Task:** Prompts for title and description, creates new task
- **2 - View Tasks:** Displays all current tasks with IDs and status
- **3 - Update Task:** Updates title and/or description of existing task
- **4 - Delete Task:** Removes task from list (confirmation recommended)
- **5 - Mark as Complete/Incomplete:** Toggles task completion status
- **0 - Exit:** Closes the application

### Example Workflow

```bash
$ python src/main.py

Todo App
========
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark as Complete/Incomplete
0. Exit

Choose an option: 1

Enter task title: Buy groceries
Enter task description: Milk, eggs, bread
Task added successfully (ID: 1).

Choose an option: 2

Tasks:
------
1. [ ] Buy groceries - Milk, eggs, bread

Choose an option: 5

Enter task ID to toggle: 1
Task marked as complete.

Choose an option: 2

Tasks:
------
1. [✓] Buy groceries - Milk, eggs, bread

Choose an option: 0

Goodbye!
```

## Development

### Project Standards

This project follows these standards:

- **Language:** Python 3.6+
- **Style:** PEP 8 compliant
- **Type Hints:** Complete type annotations
- **Testing:** Unit tests for all functions
- **Documentation:** Comprehensive docstrings

### Code Quality

All code includes:
- Type hints for function parameters and returns
- Comprehensive docstrings with examples
- Error handling for user input
- Validation of data structures

### Testing

Run tests with:

```bash
python -m pytest tests/
```

## Architecture

### In-Memory Storage

Tasks are stored as a list of dictionaries in memory:

```python
tasks = [
    {
        "id": 1,
        "title": "Task title",
        "desc": "Task description",
        "complete": False
    }
]
```

### Task Structure

Each task dictionary has:
- **id** (int) - Unique sequential identifier
- **title** (str) - Task name/headline
- **desc** (str) - Task description
- **complete** (bool) - Completion status

### Core Functions

The application implements these core functions:

- `add_task(tasks)` - Create new task
- `delete_task(tasks, task_id)` - Remove task
- `update_task(tasks, task_id)` - Modify task
- `toggle_complete(tasks, task_id)` - Change status
- `print_tasks(tasks)` - Display all tasks
- `get_menu_choice()` - Get user menu selection
- `find_task(tasks, task_id)` - Helper to find task by ID
- `get_next_id(tasks)` - Helper to generate next ID

## Files and Modules

### src/main.py

Main application file containing:
- Task management functions
- CLI interface and menu loop
- Input/output handling
- Main event loop

No external dependencies required - uses Python standard library only.

## Troubleshooting

### Virtual Environment Issues

If `uv venv` fails:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### Application Won't Start

1. Verify Python version: `python --version` (should be 3.6+)
2. Check file location: `src/main.py` exists in project root
3. Verify file is executable and contains valid Python code

### Tasks Not Persisting

This is expected - the Todo App Phase I uses in-memory storage. Tasks are lost when the application closes. This is by design for the current phase.

## Future Enhancements

Potential features for Phase II and beyond:

- **File Persistence:** Save tasks to JSON or SQLite database
- **Categories:** Organize tasks by category or project
- **Due Dates:** Add deadline tracking for tasks
- **Priority Levels:** Assign priority to tasks
- **Search and Filter:** Find tasks by various criteria
- **Web Interface:** Browser-based UI using Flask/Django
- **API:** REST API for task management
- **Multi-User:** User accounts and task sharing

## Contributing

When contributing to this project:

1. Follow PEP 8 style guide
2. Include type hints in all functions
3. Add docstrings with examples
4. Write unit tests for new features
5. Test all edge cases and error conditions
6. Update documentation as needed

## License

This project is provided as-is for educational purposes.

## Support

For issues or questions:

1. Check the troubleshooting section above
2. Review code comments and docstrings
3. Examine test cases for usage examples
4. Consult the architecture section for design details

---

**Version:** 1.0.0
**Last Updated:** 2025-12-28
**Python Version:** 3.6+
**Status:** Production Ready
```

---

### 2. CONSTITUTION.md (Project Rules)

**Path:** `.specify/memory/constitution.md`
**Content Type:** `'rules'`

```markdown
# Todo App Phase I - Project Constitution

This document establishes the foundational principles, standards, and guidelines for the Todo App Phase I project.

## Core Principles

### 1. Simplicity First
- Keep the application simple and focused
- Single responsibility per function
- In-memory storage (no database required)
- Minimal external dependencies

### 2. User-Centric Design
- Clear, intuitive menu-driven interface
- Helpful error messages
- Confirm destructive operations
- Preserve user data integrity

### 3. Code Quality
- All functions have complete type hints
- Comprehensive docstrings with examples
- PEP 8 compliant code style
- Robust error handling

### 4. Testing Standards
- Unit tests for all core functions
- Test edge cases and error conditions
- Minimum 80% code coverage
- Tests run successfully before commits

## Development Standards

### Python Version
- **Minimum:** Python 3.6
- **Recommended:** Python 3.8 or newer
- **Type Hints:** Required for all functions

### Code Style
- Follow PEP 8 guidelines strictly
- 4-space indentation
- Max line length: 100 characters
- One blank line between functions
- Two blank lines between classes (if used)

### Type Hints
All functions must include:
```python
def function_name(param1: int, param2: str) -> bool:
    """Docstring here"""
    pass
```

### Documentation
Every function must have:
- Purpose statement in docstring
- Parameter descriptions with types
- Return value description
- At least one usage example
- Error handling notes if applicable

### Function Design
- Single responsibility principle
- Pure functions preferred (no side effects)
- Avoid global state
- Handle None gracefully
- Validate inputs at boundaries

## Data Structure Standards

### Task Dictionary Format
```python
{
    "id": int,              # Unique sequential identifier (>= 1)
    "title": str,           # Task name (whitespace stripped)
    "desc": str,            # Task description (whitespace stripped)
    "complete": bool        # Completion status (True/False)
}
```

### Task List Storage
```python
tasks: list[dict]  # List of task dictionaries in memory
```

### ID Management
- IDs must be sequential (1, 2, 3, ...)
- IDs are immutable (never changed once assigned)
- New task ID = max(existing IDs) + 1
- Use `get_next_id()` helper for ID generation

## Menu Structure Standards

### Menu Format
```
Todo App
========
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark as Complete/Incomplete
0. Exit

Choose an option:
```

### Menu Requirements
- Exact text as specified above
- Options must be in this specific order
- All options (0-5) must be implemented
- Clear, concise option descriptions

## User Input Standards

### Validation Rules
- All user input must be validated
- Integer input: use `get_int_input()` for validation
- Menu choices: validate range (0-5) in `get_menu_choice()`
- Confirmation: use `confirm()` for yes/no questions
- Text input: strip whitespace from both ends

### Input Prompts
- Be clear and specific
- Include hints where appropriate: "(press Enter to keep)" for optional fields
- Include valid range for numeric input: "(y/n)" for yes/no
- Be consistent across the application

### Error Messages
- Clear and actionable
- Explain what went wrong
- Suggest how to fix if possible
- Do not blame the user
- Examples:
  - "Invalid input. Please enter a valid integer."
  - "Task with ID 99 not found."
  - "Option 7 is not valid. Please choose 0-5."

## Output Standards

### Success Messages
- Confirm operations immediately
- Include relevant information (e.g., ID of created task)
- Format: "Task added successfully (ID: 1)."
- Format: "Task updated."
- Format: "Task marked as complete."

### Task Display Format
```
Tasks:
------
1. [ ] Buy groceries - Milk, eggs, bread
2. [✓] Finish project - Submit by Friday
3. [ ] Call mom - Wish happy birthday
```

### Status Indicators
- Incomplete: `[ ]` (square brackets with space)
- Complete: `[✓]` (square brackets with checkmark U+2713)
- Consistency: use same format throughout

## Function Implementation Standards

### Helper Functions
- `find_task(tasks, task_id)` → dict | None
  - Search for task by ID
  - Return exact task dict or None
  - No printing; silent operation

- `get_next_id(tasks)` → int
  - Calculate next available ID
  - Return max(id) + 1 or 1 if empty
  - Never hardcode ID logic

### Core Operations
- `add_task(tasks)` → None
  - Collect title and description
  - Generate ID using `get_next_id()`
  - Create dict and append to list
  - Print success message

- `delete_task(tasks, task_id)` → bool
  - Find task using `find_task()`
  - Remove if found; print error if not
  - Return success status

- `update_task(tasks, task_id)` → bool
  - Find task using `find_task()`
  - Allow optional field updates (press Enter to keep)
  - Update only if changes made
  - Return success status

- `toggle_complete(tasks, task_id)` → bool
  - Find task using `find_task()`
  - Invert `complete` field
  - Print appropriate status message
  - Return success status

### UI Functions
- `display_menu()` → None
  - Print menu options exactly as specified
  - No input; just display

- `print_tasks(tasks)` → None
  - Display "Tasks:" and separator
  - Format: `ID. [Status] Title - Description`
  - Handle empty list: "No tasks yet. Add one!"

- `get_menu_choice()` → int
  - Display menu using `display_menu()`
  - Get choice using `get_int_input()`
  - Validate range (0-5)
  - Return guaranteed valid choice (0-5)

- `get_int_input(prompt)` → int
  - Prompt user and read input
  - Validate integer format
  - Re-prompt on error
  - Handle Ctrl+C gracefully

- `confirm(prompt)` → bool
  - Prompt for yes/no confirmation
  - Accept: y/Y/yes/Yes for True
  - Accept: n/N/no/No for False
  - Re-prompt on invalid input
  - Return boolean result

## Testing Requirements

### Unit Tests
- Test each function independently
- Cover happy path (normal operation)
- Cover error paths (invalid inputs)
- Cover edge cases (empty list, boundaries)
- Verify return values and types
- Verify side effects (list modifications)

### Test Execution
```bash
python -m pytest tests/test_main.py -v
```

### Minimum Test Cases per Function
- Helper functions: 15+ tests
- Core operations: 20+ tests
- UI functions: 20+ tests
- Total: 150+ test cases minimum

## Dependency Standards

### Allowed Dependencies
- Python standard library only
- No external packages required
- Built-in modules only (sys, os, etc.)

### Forbidden Dependencies
- Third-party packages (requests, pandas, etc.)
- Database libraries (sqlite3 allowed if needed later)
- External frameworks

## Commit Standards

### Commit Messages
- First line: brief summary (50 chars max)
- Blank line
- Detailed explanation (if needed)
- Reference issues/features as applicable
- Example: "Add delete_task() with confirmation safety"

### Pre-Commit Checklist
- [ ] All tests pass
- [ ] Code follows PEP 8
- [ ] Type hints complete
- [ ] Docstrings present
- [ ] No debug code
- [ ] No commented code

## Documentation Requirements

### README.md
- Project overview
- Setup instructions
- Feature list
- Usage examples
- Troubleshooting guide

### Code Comments
- Explain "why" not "what"
- Only where logic is non-obvious
- Keep comments in sync with code
- Remove obsolete comments

### Docstrings
- Present on every function
- Include purpose, parameters, returns
- Include usage example
- Include error handling notes

## Quality Metrics

### Code Quality
- Type hint coverage: 100%
- Docstring coverage: 100%
- Test coverage: minimum 80%
- PEP 8 compliance: 100%

### Error Handling
- All user inputs validated
- No unhandled exceptions in normal use
- Graceful handling of edge cases
- Clear error messages to user

### Performance
- No unnecessary loops or iterations
- Efficient data structure access
- Acceptable performance for 1000+ tasks
- No memory leaks or retention

## Security Considerations

### Input Validation
- All user input treated as untrusted
- Validate input type and format
- Validate input length (prevent buffer overflow)
- No code injection possible (text-only input)

### Data Protection
- No sensitive data storage (in-memory only)
- No external API calls
- No file system access (current phase)
- No logging of user data

## Versioning

### Version Format
- Semantic versioning: MAJOR.MINOR.PATCH
- Example: 1.0.0 (Phase I initial release)
- Increment on feature additions or bug fixes

### Release Checklist
- [ ] All tests passing
- [ ] Documentation updated
- [ ] Code reviewed
- [ ] Version bumped
- [ ] Changelog updated
- [ ] Commit tagged with version

## Future Considerations

### Phase II Plans
- Database persistence (SQLite)
- Task categories
- Due date tracking
- Priority levels

### Phase III Plans
- Web API (REST)
- Authentication
- Multi-user support
- Task sharing

## Approval and Sign-Off

This constitution is approved for the Todo App Phase I project.

**Project Lead:** AI Assistant
**Date:** 2025-12-28
**Status:** Active

---

**Last Updated:** 2025-12-28
**Version:** 1.0
**Next Review:** Phase I Completion
```

---

### 3. SETUP_GUIDE.md (Installation Instructions)

**Path:** `SETUP_GUIDE.md`
**Content Type:** `'setup-guide'`

```markdown
# Todo App Phase I - Setup Guide

Complete step-by-step guide to set up and run the Todo App Phase I project.

## System Requirements

### Minimum Requirements
- **Operating System:** Windows, macOS, or Linux
- **Python Version:** 3.6 or higher
- **Disk Space:** Less than 100 MB
- **RAM:** 256 MB minimum (1 GB recommended)

### Recommended Setup
- **Python Version:** 3.8 or newer
- **IDE:** VS Code, PyCharm, or similar
- **Terminal:** Bash (Linux/macOS) or PowerShell (Windows)

## Installation Steps

### Step 1: Verify Python Installation

Check if Python is installed:

```bash
python --version
```

Expected output: `Python 3.6.0` or higher

If not installed, download from [python.org](https://www.python.org/downloads/)

### Step 2: Install UV Package Manager

UV is a fast Python package manager:

```bash
pip install uv
```

Verify installation:

```bash
uv --version
```

### Step 3: Create Project Directory

```bash
mkdir todo-app
cd todo-app
```

### Step 4: Create Virtual Environment

```bash
uv venv
```

This creates a `.venv` directory with isolated Python environment.

### Step 5: Activate Virtual Environment

**Linux/macOS:**
```bash
source .venv/bin/activate
```

**Windows (PowerShell):**
```bash
.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```bash
.venv\Scripts\activate.bat
```

Your terminal should now show `(.venv)` prefix.

### Step 6: Sync Dependencies

```bash
uv sync
```

This installs all required packages (currently none for Phase I).

### Step 7: Create Project Structure

```bash
mkdir src
```

### Step 8: Create Main Application File

Create `src/main.py` with your Todo App code.

### Step 9: Run the Application

```bash
python src/main.py
```

You should see the main menu:

```
Todo App
========
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark as Complete/Incomplete
0. Exit

Choose an option:
```

## Troubleshooting

### Issue: Python not found

**Solution:**
- Check if Python is installed: `python --version`
- On some systems, use `python3` instead of `python`
- Add Python to PATH (Windows users)

### Issue: UV command not found

**Solution:**
```bash
pip install --upgrade uv
```

### Issue: Virtual environment not activating

**Solution:**
- Verify `.venv` directory exists
- Check file permissions: `chmod +x .venv/bin/activate` (Linux/macOS)
- Restart terminal after activation

### Issue: "No such file or directory: src/main.py"

**Solution:**
- Create `src/` directory: `mkdir src`
- Create `main.py` in that directory
- Verify structure:
  ```bash
  ls -la src/main.py
  ```

### Issue: Application crashes with ImportError

**Solution:**
- Make sure `src/main.py` has valid Python code
- Check for syntax errors: `python -m py_compile src/main.py`
- Verify all imports are from standard library

## Deactivating Virtual Environment

When done working:

```bash
deactivate
```

The `(.venv)` prefix will disappear from your terminal.

## Reactivating Virtual Environment

To work on the project again:

```bash
source .venv/bin/activate  # Linux/macOS
# or
.venv\Scripts\activate.bat  # Windows Command Prompt
# or
.venv\Scripts\Activate.ps1  # Windows PowerShell
```

## Running Tests

To run the test suite:

```bash
python -m pytest tests/ -v
```

## Project Structure After Setup

```
todo-app/
├── .venv/                  # Virtual environment (auto-created)
├── src/
│   └── main.py            # Application code
├── tests/
│   └── test_main.py       # Test suite
├── README.md              # Project overview
├── SETUP_GUIDE.md         # This file
├── pyproject.toml         # Project configuration
├── .python-version        # Python version spec
└── .gitignore             # Git ignore rules
```

## Quick Start Checklist

- [ ] Python 3.6+ installed
- [ ] UV package manager installed
- [ ] Project directory created
- [ ] Virtual environment created with `uv venv`
- [ ] Virtual environment activated
- [ ] Dependencies synced with `uv sync`
- [ ] `src/` directory created
- [ ] `src/main.py` created with application code
- [ ] Application runs: `python src/main.py`
- [ ] Main menu displays correctly

## Next Steps

1. Review the [README.md](README.md) for project overview
2. Check [Constitution](CONSTITUTION.md) for development standards
3. Implement core functionality in `src/main.py`
4. Create tests in `tests/test_main.py`
5. Run application and verify all features work

## Additional Resources

- [Python Official Documentation](https://docs.python.org)
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)
- [Pytest Documentation](https://docs.pytest.org)

---

**Version:** 1.0.0
**Last Updated:** 2025-12-28
```

---

### 4. FEATURES.md (Feature Specifications)

**Path:** `FEATURES.md`
**Content Type:** `'features'`

```markdown
# Todo App Phase I - Feature Specifications

Detailed specifications for the five core features of the Todo App Phase I.

## Feature 1: Add Task

### Purpose
Create new tasks with user-provided title and description. Automatically assign next sequential ID.

### User Flow
1. User selects option 1 from main menu
2. Application prompts: "Enter task title: "
3. User enters task title and presses Enter
4. Application prompts: "Enter task description: "
5. User enters task description and presses Enter
6. Application creates task with:
   - Next sequential ID (1 for first task)
   - Title (whitespace stripped)
   - Description (whitespace stripped)
   - Complete status: False (default)
7. Application displays: "Task added successfully (ID: X)."
8. Return to main menu

### Input Validation
- **Title:** Accept any non-empty string after stripping whitespace
- **Description:** Accept any non-empty string after stripping whitespace
- **Whitespace Handling:** Strip leading/trailing spaces from both fields
- **Special Characters:** Allow special characters, unicode, emoji

### Data Structure
```python
new_task = {
    "id": next_sequential_id,
    "title": user_title.strip(),
    "desc": user_description.strip(),
    "complete": False
}
```

### Success Criteria
- ✓ Task created with all required fields
- ✓ ID is next sequential (never duplicate)
- ✓ Title and description have whitespace stripped
- ✓ Completion status defaults to False
- ✓ Task appended to main list
- ✓ Success message displays with ID
- ✓ Handles empty list (first task gets ID 1)
- ✓ Handles multiple sequential additions

### Error Handling
- Allow empty title/description (no validation in basic version)
- Handle very long inputs (no length limit)
- Handle special characters and unicode

### Test Cases
- Add to empty list (ID = 1)
- Add to list with existing tasks (ID = max + 1)
- Add with whitespace in inputs
- Add with special characters
- Add with unicode characters
- Multiple sequential additions verify sequential IDs

---

## Feature 2: View Tasks

### Purpose
Display all tasks in a clear, organized format showing ID, completion status, title, and description.

### User Flow
1. User selects option 2 from main menu
2. Application checks if tasks exist
3. If no tasks: Display "No tasks yet. Add one!"
4. If tasks exist: Display formatted list:
   ```
   Tasks:
   ------
   1. [ ] Buy groceries - Milk, eggs, bread
   2. [✓] Finish project - Submit by Friday
   3. [ ] Call mom - Wish happy birthday
   ```
5. Return to main menu

### Display Format
```
Tasks:
------
{id}. [{status}] {title} - {description}
```

- **{id}** - Task ID (integer)
- **{status}** - `[ ]` if incomplete, `[✓]` if complete
- **{title}** - Task title
- **{description}** - Task description

### Display Rules
- Tasks displayed in order they appear in list
- One task per line
- Space after ID: `1. `
- Space around separator: ` - `
- Status indicator with spaces: `[ ]` or `[✓]`

### Empty State
If no tasks exist, display exactly:
```
No tasks yet. Add one!
```

### Success Criteria
- ✓ Header "Tasks:" displayed
- ✓ Separator line "------" displayed
- ✓ Each task on separate line
- ✓ Status indicator correct ([ ] or [✓])
- ✓ All fields (ID, title, description) displayed
- ✓ Empty state message displays correctly
- ✓ Handles single task
- ✓ Handles multiple tasks (10+)

### Error Handling
- No errors expected; display gracefully handles all cases
- Empty list: special message

### Test Cases
- Display empty list
- Display single task
- Display multiple tasks
- Display mix of complete and incomplete
- Display with special characters in titles/descriptions

---

## Feature 3: Update Task

### Purpose
Modify existing task's title and/or description. Optional fields allow user to skip updates by pressing Enter.

### User Flow
1. User selects option 3 from main menu
2. Application prompts: "Enter task ID to update: "
3. User enters task ID
4. Application finds task:
   - If not found: Display "Task with ID X not found." and return
   - If found: Proceed to step 5
5. Application displays:
   ```
   Current title: {title}
   Current description: {description}
   ```
6. Application prompts: "Enter new title (press Enter to keep): "
7. User enters new title or presses Enter
8. Application prompts: "Enter new description (press Enter to keep): "
9. User enters new description or presses Enter
10. Application updates task:
    - If new title entered: update title
    - If new description entered: update description
    - If both empty: no update, no message
    - If any change: display "Task updated."
11. Return to main menu

### Input Handling
- **Empty Input:** Keep original value (user pressed Enter)
- **Whitespace Only:** Treated as empty (keep original)
- **New Value:** Strip whitespace and use new value
- **Both Empty:** No message, task unchanged

### Update Rules
- Title update is optional (press Enter to skip)
- Description update is optional (press Enter to skip)
- Can update only title
- Can update only description
- Can update both
- Can skip both (no changes)

### Success Criteria
- ✓ Task found by ID
- ✓ Current values displayed
- ✓ Prompts include guidance: "(press Enter to keep)"
- ✓ Title updated if non-empty input
- ✓ Description updated if non-empty input
- ✓ Success message only if changes made
- ✓ Error message if task not found
- ✓ Handles empty inputs correctly

### Error Handling
- Task ID not found: Display error and return
- Invalid task ID (non-integer): Handled by `get_int_input()`
- No changes made: No message, successful return

### Test Cases
- Update title only
- Update description only
- Update both fields
- No changes (both empty)
- Task not found
- Whitespace-only input treated as empty
- Special characters in new values
- Unicode in new values

---

## Feature 4: Delete Task

### Purpose
Remove task from the list. Safe deletion with error handling.

### User Flow
1. User selects option 4 from main menu
2. Application prompts: "Enter task ID to delete: "
3. User enters task ID
4. Application finds task:
   - If not found: Display "Task with ID X not found." and return False
   - If found: Proceed to step 5
5. **Recommended:** Display task before deleting:
   ```
   Task: 1. Buy groceries - Milk, eggs, bread
   ```
6. **Recommended:** Confirm deletion:
   ```
   Delete this task? (y/n):
   ```
7. If confirmed:
   - Remove task from list
   - Display: "Task deleted successfully!"
   - Return True
8. If not confirmed:
   - Display: "Task not deleted."
   - Return False

### Implementation Note
The basic implementation does not require confirmation, but it's recommended for safety.

### Delete Rules
- Task is located by ID, not index
- Task is removed using `.remove()` not index-based deletion
- No gaps in list after deletion (list shrinks)
- ID is NOT reused for new tasks

### Success Criteria
- ✓ Task found by ID or error displayed
- ✓ Task removed from list completely
- ✓ Success message displayed if deleted
- ✓ Error message if not found
- ✓ Returns boolean (True/False)
- ✓ Safe deletion (no index errors)

### Error Handling
- Task ID not found: Error message, return False
- Invalid task ID: Handled by `get_int_input()`
- No side effects on failure

### Test Cases
- Delete existing task
- Delete non-existent task ID
- Delete from single-task list
- Delete from multi-task list
- Verify task removed from list
- Verify other tasks unchanged
- With confirmation (recommended)

---

## Feature 5: Mark as Complete/Incomplete

### Purpose
Toggle task completion status. Simple boolean inversion (True ↔ False).

### User Flow
1. User selects option 5 from main menu
2. Application prompts: "Enter task ID to toggle: "
3. User enters task ID
4. Application finds task:
   - If not found: Display "Task with ID X not found." and return False
   - If found: Proceed to step 5
5. Application toggles completion status:
   - If incomplete (False): Change to complete (True)
   - If complete (True): Change to incomplete (False)
6. Application displays appropriate message:
   - If marked complete: "Task marked as complete."
   - If marked incomplete: "Task marked as incomplete."
7. Return to main menu

### Toggle Logic
```python
task["complete"] = not task["complete"]

if task["complete"]:
    print("Task marked as complete.")
else:
    print("Task marked as incomplete.")
```

### Display Rules
- Status indicator in task list: `[ ]` for incomplete, `[✓]` for complete
- Message reflects NEW status (not previous)
- Message is clear and immediate

### Success Criteria
- ✓ Task found by ID or error displayed
- ✓ Completion status inverted (True ↔ False)
- ✓ Appropriate message displayed
- ✓ Message reflects new status
- ✓ Returns boolean (True/False)
- ✓ No confirmation needed (reversible)

### Error Handling
- Task ID not found: Error message, return False
- Invalid task ID: Handled by `get_int_input()`
- No side effects on failure

### Test Cases
- Toggle incomplete to complete
- Toggle complete to incomplete
- Multiple toggles (incomplete → complete → incomplete)
- Task not found
- Verify status changes in list
- Display correct status in View Tasks

---

## Feature Integration

### Complete User Workflow Example

```
1. Start application
2. Select "Add Task" (option 1)
   - Add: "Buy groceries" / "Milk, eggs, bread"
   - ID: 1 assigned automatically
3. Select "Add Task" (option 1)
   - Add: "Finish project" / "Submit by Friday"
   - ID: 2 assigned automatically
4. Select "View Tasks" (option 2)
   - Display all 2 tasks with status
5. Select "Mark as Complete" (option 5)
   - Mark task 1 as complete
   - Message: "Task marked as complete."
6. Select "View Tasks" (option 2)
   - Task 1 now shows [✓], task 2 shows [ ]
7. Select "Update Task" (option 3)
   - Update task 2 description to "Submit ASAP"
8. Select "View Tasks" (option 2)
   - Task 2 shows new description
9. Select "Delete Task" (option 4)
   - Delete task 1 (confirmed)
   - Message: "Task deleted successfully!"
10. Select "View Tasks" (option 2)
    - Only task 2 displayed (ID 2 still, not reassigned)
11. Select "Exit" (option 0)
    - Application closes
```

---

## Success Criteria Summary

All five features must:
- ✓ Accept user input correctly
- ✓ Validate input appropriately
- ✓ Perform required operation
- ✓ Display success/error messages
- ✓ Return appropriate status values
- ✓ Handle edge cases gracefully
- ✓ Maintain data integrity
- ✓ Follow design standards

---

**Version:** 1.0.0
**Last Updated:** 2025-12-28
**Status:** Final Specification
```

---

## Skill Implementation Summary

This skill generates complete, production-ready project files based on specifications. The files created include:

### Supported File Types

| File Path | Content Type | Purpose |
|-----------|--------------|---------|
| `README.md` | `'project-overview'` | Project documentation, setup, features |
| `.specify/memory/constitution.md` | `'rules'` | Development standards and principles |
| `SETUP_GUIDE.md` | `'setup-guide'` | Step-by-step installation instructions |
| `FEATURES.md` | `'features'` | Detailed feature specifications |

### Generated Content Characteristics

✓ **Complete and Ready-to-Use** – Full content formatted and ready to write to disk
✓ **Project-Specific** – Tailored to Todo App Phase I requirements
✓ **Well-Structured** – Clear sections, proper formatting, easy navigation
✓ **Comprehensive** – Covers all aspects (setup, features, standards, troubleshooting)
✓ **Production Quality** – Professional formatting, detailed explanations
✓ **Educational** – Includes examples, workflows, and best practices

### File Generation Process

1. **Accept Input:** File path and content type
2. **Select Template:** Choose appropriate template based on content type
3. **Populate Template:** Fill in Todo App Phase I specific details
4. **Format Content:** Ensure proper markdown formatting and structure
5. **Return Result:** Complete file content as string

---

## Acceptance Criteria

- ✓ Each file template generates complete, valid content
- ✓ Markdown formatting is correct and renders properly
- ✓ Content is specific to Todo App Phase I
- ✓ All five features are described accurately
- ✓ Setup instructions are clear and complete
- ✓ Standards and rules are comprehensive
- ✓ Files are ready to write directly to disk
- ✓ No placeholders or incomplete sections

---

## Usage Example

```python
# Generate README.md
readme_content = generate_project_file(
    file_path="README.md",
    content_type="project-overview"
)
# Returns: Complete README.md content as string

# Generate Constitution
constitution_content = generate_project_file(
    file_path=".specify/memory/constitution.md",
    content_type="rules"
)
# Returns: Complete Constitution content as string

# Write to disk
with open("README.md", "w") as f:
    f.write(readme_content)
```

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-12-28 | Initial skill document; complete file templates for Todo App Phase I |

---

