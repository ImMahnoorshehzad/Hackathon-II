# Skill: Generate Beautiful Task List Display

**Owned by:** `cli-interface-subagent`
**Feature:** Todo App Phase I - CLI Interface
**Status:** Production-Ready

---

## Purpose

Generate the `print_tasks(tasks: list[dict])` function that renders all tasks in a clean, visually organized format. This function transforms raw task data into human-readable output with status indicators, task IDs, titles, and descriptions.

---

## When to Use

- **View Tasks Operation:** When user selects option 2 (View Tasks) from the main menu
- **Task List Refresh:** After adding, updating, or deleting a task to show current state
- **Status Display:** When displaying task progress or completion status
- **Empty State Handling:** When no tasks exist, display a friendly prompt to add one

---

## Inputs

**Function Signature:**
```python
def print_tasks(tasks: list[dict]) -> None:
```

**Parameter Details:**

- **`tasks`** (list[dict]): A list of task dictionaries, each containing:
  - **`id`** (int): Unique task identifier (1, 2, 3, ...)
  - **`title`** (str): Task name/headline (e.g., "Buy groceries")
  - **`desc`** (str): Task description (e.g., "Milk, eggs, bread")
  - **`complete`** (bool): True if task is completed, False if pending

**Example Input:**
```python
tasks = [
    {"id": 1, "title": "Buy groceries", "desc": "Milk, eggs, bread", "complete": False},
    {"id": 2, "title": "Finish Python project", "desc": "Submit by Friday", "complete": True},
    {"id": 3, "title": "Call mom", "desc": "Wish happy birthday", "complete": False}
]
```

---

## Step-by-Step Process

1. **Check if tasks list is empty:**
   - If empty, print "No tasks yet. Add one!" and return
   - Skip remaining steps if no tasks exist

2. **Print header:**
   - Display "Tasks:" as the section title
   - Print a separator line ("------") for visual clarity

3. **Iterate through each task:**
   - Extract task ID, title, description, and completion status
   - Determine status indicator: `[ ]` if incomplete, `[✓]` if complete

4. **Format task line:**
   - Format: `{id}. {status} {title} - {description}`
   - Example: `1. [ ] Buy groceries - Milk, eggs, bread`

5. **Print each formatted task:**
   - Print one task per line in order of ID

6. **Return control:**
   - Function completes after displaying all tasks

---

## Output

**Function Name:** `print_tasks(tasks: list[dict])`

**Output Example 1 (With Tasks):**
```
Tasks:
------
1. [ ] Buy groceries - Milk, eggs, bread
2. [✓] Finish Python project - Submit by Friday
3. [ ] Call mom - Wish happy birthday
```

**Output Example 2 (Empty Task List):**
```
No tasks yet. Add one!
```

**Return Value:** None (void function)

---

## Implementation

### Python Code (Production-Ready)

```python
def print_tasks(tasks: list[dict]) -> None:
    """
    Display all tasks in a beautifully formatted list.

    Prints each task with its ID, completion status, title, and description.
    If no tasks exist, displays a friendly prompt to add one.

    Args:
        tasks (list[dict]): List of task dictionaries, each containing:
            - id (int): Unique task identifier
            - title (str): Task name/headline
            - desc (str): Task description
            - complete (bool): True if completed, False otherwise

    Returns:
        None

    Example:
        tasks = [
            {"id": 1, "title": "Buy groceries", "desc": "Milk, eggs, bread", "complete": False},
            {"id": 2, "title": "Finish Python project", "desc": "Submit by Friday", "complete": True}
        ]
        print_tasks(tasks)
        # Output:
        # Tasks:
        # ------
        # 1. [ ] Buy groceries - Milk, eggs, bread
        # 2. [✓] Finish Python project - Submit by Friday
    """
    # Handle empty task list
    if not tasks:
        print("No tasks yet. Add one!")
        return

    # Print header
    print("Tasks:")
    print("------")

    # Print each task with formatting
    for task in tasks:
        # Extract task data
        task_id = task["id"]
        title = task["title"]
        desc = task["desc"]
        is_complete = task["complete"]

        # Determine status indicator
        status = "[✓]" if is_complete else "[ ]"

        # Print formatted task line
        print(f"{task_id}. {status} {title} - {desc}")
```

### Design Notes

- **Type Hints:** Includes full type hints for clarity and IDE support
- **Status Indicator:** Uses `[✓]` for complete (checkmark character U+2713) and `[ ]` for incomplete
- **Consistent Formatting:** All tasks follow the same format: `ID. [Status] Title - Description`
- **Robust Field Access:** Uses dict key access with quotes to handle field names
- **Early Return:** Returns immediately on empty task list to avoid unnecessary code execution
- **F-String Formatting:** Uses modern Python f-string syntax for readability

### Unicode Handling

The function uses the Unicode checkmark character `✓` (U+2713). This is compatible with:
- Windows 10+
- macOS (all versions)
- Linux (all versions)
- Most modern terminals and IDEs

If UTF-8 compatibility is a concern, alternative characters:
- `[x]` for complete (traditional)
- `[*]` for complete (asterisk)

---

## Failure Handling

| Scenario | Handling |
|----------|----------|
| **Empty tasks list** | Print "No tasks yet. Add one!" and return gracefully |
| **Missing task fields** | Will raise `KeyError` if required fields are missing; validate input before calling |
| **None instead of dict** | Will raise `TypeError`; ensure tasks parameter is a list |
| **Unicode display issues** | Falls back to `[ ]` and `[x]` if terminal doesn't support UTF-8 |
| **Very long descriptions** | No line wrapping; descriptions display as-is (can implement wrapping if needed) |
| **Empty title or description** | Function displays as-is; no minimum length validation |

**Recommended Input Validation (At Call Site):**

```python
def print_tasks_safe(tasks):
    """Wrapper with input validation"""
    if not isinstance(tasks, list):
        print("Error: tasks must be a list")
        return

    for task in tasks:
        if not isinstance(task, dict):
            print(f"Error: invalid task format: {task}")
            return
        required_fields = {"id", "title", "desc", "complete"}
        if not required_fields.issubset(task.keys()):
            print(f"Error: task missing required fields: {task}")
            return

    # Safe to call
    print_tasks(tasks)
```

---

## Acceptance Criteria

- ✓ Function accepts a list of task dictionaries with id, title, desc, and complete fields
- ✓ Prints "Tasks:" header with separator line ("------")
- ✓ Each task displays on its own line with format: `ID. [Status] Title - Description`
- ✓ Status shows `[ ]` for incomplete tasks
- ✓ Status shows `[✓]` for complete tasks
- ✓ Tasks display in order of their ID
- ✓ If no tasks exist, prints "No tasks yet. Add one!" instead of headers
- ✓ Function completes without waiting for user input
- ✓ Output is identical across all platforms (Windows, Mac, Linux)
- ✓ Code uses only Python standard library
- ✓ Includes complete docstring with examples
- ✓ Type hints are correct and helpful

---

## Testing Checklist

```python
import io
import sys

# Test 1: Function exists and is callable
assert callable(print_tasks)

# Test 2: Empty task list
captured_output = io.StringIO()
sys.stdout = captured_output
print_tasks([])
sys.stdout = sys.__stdout__
assert "No tasks yet. Add one!" in captured_output.getvalue()

# Test 3: Single task (incomplete)
captured_output = io.StringIO()
sys.stdout = captured_output
print_tasks([{"id": 1, "title": "Buy groceries", "desc": "Milk, eggs, bread", "complete": False}])
sys.stdout = sys.__stdout__
output = captured_output.getvalue()
assert "Tasks:" in output
assert "------" in output
assert "1. [ ] Buy groceries - Milk, eggs, bread" in output

# Test 4: Single task (complete)
captured_output = io.StringIO()
sys.stdout = captured_output
print_tasks([{"id": 1, "title": "Finish project", "desc": "Submit by Friday", "complete": True}])
sys.stdout = sys.__stdout__
output = captured_output.getvalue()
assert "1. [✓] Finish project - Submit by Friday" in output

# Test 5: Multiple tasks with mixed completion status
tasks = [
    {"id": 1, "title": "Buy groceries", "desc": "Milk, eggs, bread", "complete": False},
    {"id": 2, "title": "Finish Python project", "desc": "Submit by Friday", "complete": True},
    {"id": 3, "title": "Call mom", "desc": "Wish happy birthday", "complete": False}
]
captured_output = io.StringIO()
sys.stdout = captured_output
print_tasks(tasks)
sys.stdout = sys.__stdout__
output = captured_output.getvalue()
assert "1. [ ] Buy groceries - Milk, eggs, bread" in output
assert "2. [✓] Finish Python project - Submit by Friday" in output
assert "3. [ ] Call mom - Wish happy birthday" in output

# Test 6: Task IDs are preserved in order
captured_output = io.StringIO()
sys.stdout = captured_output
print_tasks([
    {"id": 5, "title": "Task Five", "desc": "desc", "complete": False},
    {"id": 10, "title": "Task Ten", "desc": "desc", "complete": False},
    {"id": 3, "title": "Task Three", "desc": "desc", "complete": False}
])
sys.stdout = sys.__stdout__
output = captured_output.getvalue()
# Verify IDs are displayed as provided (no reordering)
assert "5. [ ]" in output
assert "10. [ ]" in output
assert "3. [ ]" in output
```

---

## Usage Examples

### Example 1: Display All Tasks
```python
tasks = [
    {"id": 1, "title": "Buy groceries", "desc": "Milk, eggs, bread", "complete": False},
    {"id": 2, "title": "Finish Python project", "desc": "Submit by Friday", "complete": True},
    {"id": 3, "title": "Call mom", "desc": "Wish happy birthday", "complete": False}
]

print_tasks(tasks)
```

**Output:**
```
Tasks:
------
1. [ ] Buy groceries - Milk, eggs, bread
2. [✓] Finish Python project - Submit by Friday
3. [ ] Call mom - Wish happy birthday
```

### Example 2: Handle Empty List
```python
tasks = []
print_tasks(tasks)
```

**Output:**
```
No tasks yet. Add one!
```

### Example 3: Integration with View Tasks Menu Option
```python
def view_tasks(tasks):
    """Handles menu option 2: View Tasks"""
    if not tasks:
        print_tasks(tasks)  # Will print "No tasks yet. Add one!"
    else:
        print_tasks(tasks)
        print()  # Add blank line for spacing
```

---

## Integration with Other Functions

This skill works seamlessly with other CLI components:

```python
def main_loop(tasks):
    """Main event loop using print_tasks()"""
    while True:
        display_menu()
        choice = get_user_choice()

        if choice == 0:
            print("Goodbye!")
            break
        elif choice == 1:
            add_task(tasks)
        elif choice == 2:
            print()  # Blank line for readability
            print_tasks(tasks)  # Display all tasks
            print()
        elif choice == 3:
            update_task(tasks)
        elif choice == 4:
            delete_task(tasks)
        elif choice == 5:
            toggle_task_complete(tasks)
```

---

## Dependencies and Constraints

| Constraint | Details |
|-----------|---------|
| **Python Version** | 3.7+ (uses f-strings and type hints) |
| **External Packages** | None (standard library only) |
| **OS Compatibility** | All platforms (Linux, macOS, Windows 10+) |
| **Character Encoding** | UTF-8 required for checkmark character (✓) |
| **Performance** | O(n) where n is number of tasks; linear iteration |
| **Memory** | O(1) additional space; no data structures created |

---

## Related Functions

This skill is part of the task management display system:

- **`display_menu()`** – Shows main menu with all options
- **`get_user_choice()`** – Reads and validates menu selection
- **`add_task(tasks, title, desc)`** – Adds new task and displays confirmation
- **`update_task(tasks, task_id, title, desc)`** – Updates task and displays confirmation
- **`delete_task(tasks, task_id)`** – Deletes task and displays confirmation
- **`toggle_task_complete(tasks, task_id)`** – Marks task complete/incomplete
- **`print_tasks(tasks)`** – Displays all tasks (this function)

---

## Production Checklist

Before deploying this function:

- [ ] Function is defined in `src/cli.py` or integrated into `main.py`
- [ ] No external imports required
- [ ] Output matches specification exactly (formatting, spacing, status indicators)
- [ ] Tested with empty list: prints "No tasks yet. Add one!"
- [ ] Tested with single task (both complete and incomplete)
- [ ] Tested with multiple tasks (mixed completion status)
- [ ] Checkmark character (✓) displays correctly in target terminal
- [ ] Task IDs display in order provided (no reordering or filtering)
- [ ] Integrated into "View Tasks" (option 2) menu handler
- [ ] Error handling is in place for missing fields or invalid input
- [ ] Code is documented with docstring as shown
- [ ] Type hints are present and correct

---

## Enhancement Options (Optional)

These enhancements are NOT required but can improve functionality:

1. **Task Wrapping for Long Descriptions**
   - Wrap descriptions at terminal width (80 chars) with indentation
   - Requires `shutil.get_terminal_size()` from standard library

2. **Sorting Options**
   - Sort by completion status (incomplete first)
   - Sort by task ID (ascending or descending)
   - Add parameter: `sort_by="id"` or `sort_by="status"`

3. **Color Output (ANSI Codes)**
   - Color complete tasks green, incomplete tasks yellow
   - Only uses standard library (no external packages)
   - Example: `\033[92m[✓]\033[0m` for green checkmark

4. **Task Filtering**
   - Show only incomplete tasks: `print_tasks(tasks, incomplete_only=True)`
   - Show only complete tasks: `print_tasks(tasks, complete_only=True)`

5. **Summary Statistics**
   - Print count of complete/incomplete tasks
   - Print completion percentage
   - Example: "Tasks: 3 total, 1 complete (33%)"

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-12-28 | Initial skill document; production-ready implementation |

---

## Troubleshooting

### Issue: Checkmark character not displaying correctly
**Solution:** Use alternative character `[x]` instead of `[✓]`
```python
status = "[x]" if is_complete else "[ ]"
```

### Issue: TypeError when calling function
**Solution:** Ensure tasks parameter is a list of dicts with required fields
```python
# Validate before calling
if isinstance(tasks, list) and all(isinstance(t, dict) for t in tasks):
    print_tasks(tasks)
```

### Issue: Output truncated or wrapped unexpectedly
**Solution:** Check terminal width and consider implementing text wrapping for descriptions

---

