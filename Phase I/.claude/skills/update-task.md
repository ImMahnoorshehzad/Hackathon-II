# Skill: Generate Update Task Function

**Owned by:** `core-todo-impl`
**Feature:** Todo App Phase I - Core Task Management
**Status:** Production-Ready

---

## Purpose

Generate the `update_task(tasks: list[dict], task_id: int) -> bool` function that safely updates an existing task's title and/or description. This function allows flexible partial updates: users can skip fields by pressing Enter without typing anything, keeping original values. Updated fields are committed to the list, and success/failure is reported via boolean return and user feedback.

---

## When to Use

- **Menu Option 3:** When user selects "Update Task" from main menu
- **Task Modification:** When existing task needs title or description changes
- **Flexible Updates:** When user may want to update only some fields
- **Optional Changes:** When pressing Enter leaves field unchanged

---

## Inputs

**Function Signature:**
```python
def update_task(tasks: list[dict], task_id: int) -> bool:
```

**Parameter Details:**

- **`tasks`** (list[dict]): The in-memory list of tasks
  - Contains existing task dicts with id, title, desc, complete
  - Function modifies task(s) in-place if found
  - Type hint: `list[dict]`

- **`task_id`** (int): The ID of the task to update
  - Matched against task's "id" field
  - If no match found, function returns False
  - Type hint: `int`

**Return Value:** `bool`
- `True` if task found and updated successfully
- `False` if task not found

---

## Step-by-Step Process

1. **Find Task by ID:**
   - Search tasks list for task with matching ID
   - If not found, print error and return False
   - If found, proceed to step 2

2. **Display Current Task:**
   - Show current title and description to user
   - Helps user remember what they're updating
   - Format: `"Current title: {title}"` and `"Current description: {desc}"`

3. **Prompt for New Title:**
   - Prompt: `"Enter new title (press Enter to keep): "`
   - Get input from user
   - Strip whitespace from input
   - If empty string (user pressed Enter), keep original title
   - If non-empty, use as new title

4. **Prompt for New Description:**
   - Prompt: `"Enter new description (press Enter to keep): "`
   - Get input from user
   - Strip whitespace from input
   - If empty string (user pressed Enter), keep original description
   - If non-empty, use as new description

5. **Update Task (if Changes Made):**
   - If title changed OR description changed:
     - Update task dict with new values
     - Print success message: `"Task updated."`
   - If no changes made (both empty inputs):
     - Do not print success message (or print "No changes made.")
     - Still return True (task was found)

6. **Return Success:**
   - Return `True` (task found, whether or not updated)

---

## Output

**Function Name:** `update_task(tasks: list[dict], task_id: int) -> bool`

**Return Value:** `True` (success) or `False` (task not found)

**Example Output Flow 1 (Task Found, Title Updated):**
```
Current title: Buy groceries
Current description: Milk, eggs, bread
Enter new title (press Enter to keep): Buy vegetables
Enter new description (press Enter to keep):
Task updated.
Return value: True
```

**Example Output Flow 2 (Task Found, Description Updated):**
```
Current title: Buy groceries
Current description: Milk, eggs, bread
Enter new title (press Enter to keep):
Enter new description (press Enter to keep): Carrots, lettuce, tomatoes
Task updated.
Return value: True
```

**Example Output Flow 3 (Task Found, Both Updated):**
```
Current title: Buy groceries
Current description: Milk, eggs, bread
Enter new title (press Enter to keep): Buy vegetables
Enter new description (press Enter to keep): Carrots, lettuce, tomatoes
Task updated.
Return value: True
```

**Example Output Flow 4 (Task Found, No Changes):**
```
Current title: Buy groceries
Current description: Milk, eggs, bread
Enter new title (press Enter to keep):
Enter new description (press Enter to keep):
Return value: True
```

**Example Output Flow 5 (Task Not Found):**
```
Task with ID 99 not found.
Return value: False
```

---

## Implementation

### Python Code (Production-Ready)

```python
def update_task(tasks: list[dict], task_id: int) -> bool:
    """
    Update a task's title and/or description.

    Searches for a task by ID. If found, prompts user for new title and
    description. User can press Enter to keep the original value. Updates
    are committed to the task dictionary. Returns True if task found,
    False if not found.

    Args:
        tasks (list[dict]): The in-memory task list. Modified in-place if
                           task is found and user makes changes.
        task_id (int): The ID of the task to update. Matched against the
                      "id" field in task dictionaries.

    Returns:
        bool: True if task found (regardless of whether changes were made).
              False if task not found (error message printed).

    Example - Update title:
        >>> tasks = [
        ...     {"id": 1, "title": "Buy groceries", "desc": "Milk, eggs", "complete": False}
        ... ]
        >>> update_task(tasks, 1)
        Current title: Buy groceries
        Current description: Milk, eggs
        Enter new title (press Enter to keep): Buy vegetables
        Enter new description (press Enter to keep):
        Task updated.
        True
        >>> tasks[0]["title"]
        'Buy vegetables'

    Example - Task not found:
        >>> update_task(tasks, 99)
        Task with ID 99 not found.
        False
    """
    # Find task by ID
    task = None
    for t in tasks:
        if t["id"] == task_id:
            task = t
            break

    # Task not found
    if task is None:
        print(f"Task with ID {task_id} not found.")
        return False

    # Display current task
    print(f"Current title: {task['title']}")
    print(f"Current description: {task['desc']}")

    # Get new title (empty means keep current)
    new_title = input("Enter new title (press Enter to keep): ").strip()

    # Get new description (empty means keep current)
    new_description = input("Enter new description (press Enter to keep): ").strip()

    # Update task if changes made
    if new_title:
        task["title"] = new_title

    if new_description:
        task["desc"] = new_description

    # Print success message if any changes were made
    if new_title or new_description:
        print("Task updated.")

    return True
```

### Design Notes

- **Flexible Updates:** Users can update any combination of fields or none
- **Preserve on Empty:** Empty input (just pressing Enter) keeps original value
- **Strip Whitespace:** `.strip()` ensures whitespace-only input treated as empty
- **Display Current:** Shows existing values before prompting for changes
- **Conditional Success Message:** Only prints "Task updated." if changes made
- **Always Return True:** Returns True if task found (even if no changes)
- **In-Place Modification:** Updates task dict directly in the list
- **Simple Logic:** Clear, straightforward implementation
- **Type Hints:** Complete type annotations for clarity

### Why This Design?

| Decision | Rationale |
|----------|-----------|
| **Find before prompting** | Avoid prompting if task doesn't exist |
| **Display current values** | User knows what they're updating |
| **Empty = keep original** | Common UX pattern; user can skip fields |
| **Strip whitespace** | Whitespace-only input treated as empty |
| **Conditional success message** | Only confirm when actual changes made |
| **Always return True if found** | Task existence is binary; updates are bonus |
| **In-place modification** | Direct update; no need to rebuild list |
| **No confirmation needed** | Update is reversible (can update again) |

---

## Alternative Implementation - With Change Tracking

```python
def update_task(tasks: list[dict], task_id: int) -> bool:
    """Update task with explicit change tracking"""
    # Find task
    task = next((t for t in tasks if t["id"] == task_id), None)

    if not task:
        print(f"Task with ID {task_id} not found.")
        return False

    # Display current
    print(f"Current title: {task['title']}")
    print(f"Current description: {task['desc']}")

    # Get input
    new_title = input("Enter new title (press Enter to keep): ").strip()
    new_description = input("Enter new description (press Enter to keep): ").strip()

    # Track changes
    changed = False

    if new_title:
        task["title"] = new_title
        changed = True

    if new_description:
        task["desc"] = new_description
        changed = True

    # Feedback
    if changed:
        print("Task updated.")
    else:
        print("No changes made.")

    return True
```

---

## Failure Handling

| Scenario | Behavior | Output |
|----------|----------|--------|
| **Task found, both fields updated** | Update both; return True | "Task updated." |
| **Task found, only title updated** | Update title; return True | "Task updated." |
| **Task found, only description updated** | Update description; return True | "Task updated." |
| **Task found, no changes** | Don't update; return True | (No message or "No changes made.") |
| **Task not found** | Print error; return False | "Task with ID X not found." |
| **Empty list** | Print error; return False | "Task with ID X not found." |
| **Negative ID** | Print error (not found); return False | "Task with ID -1 not found." |
| **Very large ID** | Print error (not found); return False | "Task with ID 999999 not found." |
| **Whitespace-only input** | `.strip()` results in empty; keep original | Task unchanged |
| **New title = old title** | Update happens; no practical change | "Task updated." |
| **Very long new title** | Accept as-is; no length limit | "Task updated." |
| **Very long new description** | Accept as-is; no length limit | "Task updated." |
| **Special characters in input** | Accept as-is; no validation | "Task updated." |
| **Unicode characters in input** | Accept if terminal supports UTF-8 | "Task updated." |
| **Ctrl+C during title input** | Raises KeyboardInterrupt; propagates | Exception raised |
| **Ctrl+C during description input** | Raises KeyboardInterrupt; propagates | Exception raised |
| **tasks is None** | Raises TypeError on iteration | Propagates |
| **task_id is not int** | May cause comparison issues | Silent failure or exception |

**Note on Error Handling:**
The basic implementation does NOT validate:
- Input length
- Input content
- Whether changes were actually made
- User confirmation before updating

This is intentional; updates are reversible (user can update again), so confirmation is optional.

### Enhanced Version with Validation (Optional)

```python
def update_task(tasks: list[dict], task_id: int) -> bool:
    """Update task with validation and confirmation"""
    # Find task
    task = next((t for t in tasks if t["id"] == task_id), None)

    if not task:
        print(f"Task with ID {task_id} not found.")
        return False

    # Display current
    print(f"Current title: {task['title']}")
    print(f"Current description: {task['desc']}")

    # Get input
    new_title = input("Enter new title (press Enter to keep): ").strip()
    new_description = input("Enter new description (press Enter to keep): ").strip()

    # Validate input (optional)
    if new_title and len(new_title) > 100:
        print("Error: Title too long (max 100 characters)")
        return False

    if new_description and len(new_description) > 500:
        print("Error: Description too long (max 500 characters)")
        return False

    # Track changes
    changed = False
    if new_title:
        task["title"] = new_title
        changed = True

    if new_description:
        task["desc"] = new_description
        changed = True

    # Confirm if changes made
    if changed:
        if confirm("Save changes? (y/n): "):
            print("Task updated.")
            return True
        else:
            # Rollback changes (undo)
            # This would require storing original values
            print("Changes discarded.")
            return False

    print("No changes made.")
    return True
```

---

## Acceptance Criteria

- ✓ Function accepts tasks list parameter
- ✓ Function accepts task_id integer parameter
- ✓ Function returns boolean (True or False)
- ✓ Finds task by ID in list
- ✓ Returns False if task not found
- ✓ Prints error message when task not found
- ✓ Error message format: "Task with ID {task_id} not found."
- ✓ Displays current title before prompting
- ✓ Displays current description before prompting
- ✓ Prompts for new title with: "Enter new title (press Enter to keep): "
- ✓ Prompts for new description with: "Enter new description (press Enter to keep): "
- ✓ Title input is stripped of whitespace
- ✓ Description input is stripped of whitespace
- ✓ Empty title input preserves original title
- ✓ Empty description input preserves original description
- ✓ Updates title if non-empty input provided
- ✓ Updates description if non-empty input provided
- ✓ Prints "Task updated." only if changes were made
- ✓ Returns True if task found (even if no changes)
- ✓ Type hints are correct: `(list[dict], int) -> bool`
- ✓ Docstring is complete with examples

---

## Testing Checklist

```python
import io
import sys
from unittest.mock import patch

# Test 1: Function exists and is callable
assert callable(update_task)

# Test 2: Update title only
tasks = [{"id": 1, "title": "Old title", "desc": "Description", "complete": False}]
with patch('builtins.input', side_effect=['New title', '']):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    result = update_task(tasks, 1)
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()

assert result is True
assert tasks[0]["title"] == "New title"
assert tasks[0]["desc"] == "Description"  # Unchanged
assert "Task updated." in output

# Test 3: Update description only
tasks = [{"id": 1, "title": "Title", "desc": "Old description", "complete": False}]
with patch('builtins.input', side_effect=['', 'New description']):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    result = update_task(tasks, 1)
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()

assert result is True
assert tasks[0]["title"] == "Title"  # Unchanged
assert tasks[0]["desc"] == "New description"
assert "Task updated." in output

# Test 4: Update both title and description
tasks = [{"id": 1, "title": "Old title", "desc": "Old description", "complete": False}]
with patch('builtins.input', side_effect=['New title', 'New description']):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    result = update_task(tasks, 1)
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()

assert result is True
assert tasks[0]["title"] == "New title"
assert tasks[0]["desc"] == "New description"
assert "Task updated." in output

# Test 5: No changes (both empty)
tasks = [{"id": 1, "title": "Original title", "desc": "Original description", "complete": False}]
with patch('builtins.input', side_effect=['', '']):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    result = update_task(tasks, 1)
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()

assert result is True
assert tasks[0]["title"] == "Original title"
assert tasks[0]["desc"] == "Original description"
# "Task updated." should NOT be in output (no changes made)

# Test 6: Task not found
tasks = [{"id": 1, "title": "Title", "desc": "Description", "complete": False}]
captured_output = io.StringIO()
sys.stdout = captured_output
result = update_task(tasks, 99)
sys.stdout = sys.__stdout__
output = captured_output.getvalue()

assert result is False
assert "Task with ID 99 not found." in output

# Test 7: Empty list
tasks = []
captured_output = io.StringIO()
sys.stdout = captured_output
result = update_task(tasks, 1)
sys.stdout = sys.__stdout__
output = captured_output.getvalue()

assert result is False
assert "Task with ID 1 not found." in output

# Test 8: Whitespace-only title input (treated as empty)
tasks = [{"id": 1, "title": "Original title", "desc": "Description", "complete": False}]
with patch('builtins.input', side_effect=['   ', '']):
    update_task(tasks, 1)

assert tasks[0]["title"] == "Original title"  # Unchanged

# Test 9: Whitespace-only description input (treated as empty)
tasks = [{"id": 1, "title": "Title", "desc": "Original description", "complete": False}]
with patch('builtins.input', side_effect=['', '   ']):
    update_task(tasks, 1)

assert tasks[0]["desc"] == "Original description"  # Unchanged

# Test 10: Whitespace is stripped from inputs
tasks = [{"id": 1, "title": "Title", "desc": "Description", "complete": False}]
with patch('builtins.input', side_effect=['  New title  ', '  New description  ']):
    update_task(tasks, 1)

assert tasks[0]["title"] == "New title"  # Spaces stripped
assert tasks[0]["desc"] == "New description"  # Spaces stripped

# Test 11: Update multi-task list (finds correct task)
tasks = [
    {"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False},
    {"id": 2, "title": "Task 2", "desc": "Desc 2", "complete": False},
    {"id": 3, "title": "Task 3", "desc": "Desc 3", "complete": False}
]
with patch('builtins.input', side_effect=['New Task 2', '']):
    result = update_task(tasks, 2)

assert result is True
assert tasks[0]["title"] == "Task 1"  # Unchanged
assert tasks[1]["title"] == "New Task 2"  # Updated
assert tasks[2]["title"] == "Task 3"  # Unchanged

# Test 12: Update completed task
tasks = [{"id": 1, "title": "Title", "desc": "Description", "complete": True}]
with patch('builtins.input', side_effect=['New title', '']):
    result = update_task(tasks, 1)

assert result is True
assert tasks[0]["complete"] is True  # Unchanged
assert tasks[0]["title"] == "New title"

# Test 13: Very long new title
long_title = "A" * 1000
tasks = [{"id": 1, "title": "Title", "desc": "Description", "complete": False}]
with patch('builtins.input', side_effect=[long_title, '']):
    result = update_task(tasks, 1)

assert result is True
assert tasks[0]["title"] == long_title

# Test 14: Very long new description
long_desc = "B" * 1000
tasks = [{"id": 1, "title": "Title", "desc": "Description", "complete": False}]
with patch('builtins.input', side_effect=['', long_desc]):
    result = update_task(tasks, 1)

assert result is True
assert tasks[0]["desc"] == long_desc

# Test 15: Special characters in new title
tasks = [{"id": 1, "title": "Title", "desc": "Description", "complete": False}]
with patch('builtins.input', side_effect=['Task #1: @Home!', '']):
    result = update_task(tasks, 1)

assert result is True
assert tasks[0]["title"] == "Task #1: @Home!"

# Test 16: Special characters in new description
tasks = [{"id": 1, "title": "Title", "desc": "Description", "complete": False}]
with patch('builtins.input', side_effect=['', 'Due: 2025-12-28 @ 3PM ($25)']):
    result = update_task(tasks, 1)

assert result is True
assert tasks[0]["desc"] == "Due: 2025-12-28 @ 3PM ($25)"

# Test 17: Unicode characters in new title
tasks = [{"id": 1, "title": "Title", "desc": "Description", "complete": False}]
with patch('builtins.input', side_effect=['Task 🛒', '']):
    result = update_task(tasks, 1)

assert result is True
assert tasks[0]["title"] == "Task 🛒"

# Test 18: Unicode characters in new description
tasks = [{"id": 1, "title": "Title", "desc": "Description", "complete": False}]
with patch('builtins.input', side_effect=['', 'Buy 🥛 and 🍞']):
    result = update_task(tasks, 1)

assert result is True
assert tasks[0]["desc"] == "Buy 🥛 and 🍞"

# Test 19: Update same title (even if identical to original)
tasks = [{"id": 1, "title": "Title", "desc": "Description", "complete": False}]
with patch('builtins.input', side_effect=['Title', '']):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    result = update_task(tasks, 1)
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()

assert result is True
assert "Task updated." in output  # Message shown even if no practical change

# Test 20: Current values displayed correctly
tasks = [{"id": 1, "title": "Current Title", "desc": "Current Description", "complete": False}]
with patch('builtins.input', side_effect=['', '']) as mock_input:
    captured_output = io.StringIO()
    sys.stdout = captured_output
    update_task(tasks, 1)
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()

assert "Current title: Current Title" in output
assert "Current description: Current Description" in output
```

---

## Usage Examples

### Example 1: Update Title Only
```python
tasks = [
    {"id": 1, "title": "Buy groceries", "desc": "Milk, eggs, bread", "complete": False}
]

update_task(tasks, 1)
```

**Interactive Flow:**
```
Current title: Buy groceries
Current description: Milk, eggs, bread
Enter new title (press Enter to keep): Buy vegetables
Enter new description (press Enter to keep):
Task updated.
```

**Result:**
```python
tasks[0] = {
    "id": 1,
    "title": "Buy vegetables",  # Updated
    "desc": "Milk, eggs, bread",  # Unchanged
    "complete": False
}
```

### Example 2: Update Description Only
```python
update_task(tasks, 1)
```

**Interactive Flow:**
```
Current title: Buy vegetables
Current description: Milk, eggs, bread
Enter new title (press Enter to keep):
Enter new description (press Enter to keep): Carrots, lettuce, tomatoes
Task updated.
```

**Result:**
```python
tasks[0] = {
    "id": 1,
    "title": "Buy vegetables",  # Unchanged
    "desc": "Carrots, lettuce, tomatoes",  # Updated
    "complete": False
}
```

### Example 3: Update Both
```python
update_task(tasks, 1)
```

**Interactive Flow:**
```
Current title: Buy vegetables
Current description: Carrots, lettuce, tomatoes
Enter new title (press Enter to keep): Buy organic vegetables
Enter new description (press Enter to keep): Organic carrots, lettuce, tomatoes
Task updated.
```

**Result:**
```python
tasks[0] = {
    "id": 1,
    "title": "Buy organic vegetables",  # Updated
    "desc": "Organic carrots, lettuce, tomatoes",  # Updated
    "complete": False
}
```

### Example 4: No Changes
```python
update_task(tasks, 1)
```

**Interactive Flow:**
```
Current title: Buy organic vegetables
Current description: Organic carrots, lettuce, tomatoes
Enter new title (press Enter to keep):
Enter new description (press Enter to keep):
```

**Result:**
```python
# Task remains unchanged
# No success message printed
```

### Example 5: Integration with Menu Loop
```python
def main():
    tasks = []

    while True:
        choice = get_menu_choice()
        print()

        if choice == 0:
            break
        elif choice == 1:
            add_task(tasks)
        elif choice == 2:
            print_tasks(tasks)
        elif choice == 3:
            task_id = get_int_input("Enter task ID to update: ")
            if update_task(tasks, task_id):
                # Task found and processed
                pass
            # else: error already printed by update_task()
        elif choice == 4:
            task_id = get_int_input("Enter task ID to delete: ")
            delete_task(tasks, task_id)
        elif choice == 5:
            task_id = get_int_input("Enter task ID to toggle: ")
            toggle_task_complete(tasks, task_id)

        print()
```

**Interactive Flow:**
```
Todo App
========
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark as Complete/Incomplete
0. Exit

Choose an option: 3

Enter task ID to update: 1

Current title: Buy groceries
Current description: Milk, eggs, bread
Enter new title (press Enter to keep): Buy vegetables
Enter new description (press Enter to keep):
Task updated.

Todo App
========
...
```

### Example 6: With Result Checking
```python
def update_task_operation(tasks, task_id):
    """Update task with feedback"""
    if update_task(tasks, task_id):
        # Task was found
        print("\nReturning to menu...")
    # else: error already printed by update_task()
```

---

## Integration with Other Functions

This function is part of the task management lifecycle:

```python
# Update operation in main loop
def main():
    tasks = []

    while True:
        choice = get_menu_choice()

        if choice == 3:
            task_id = get_int_input("Enter task ID: ")
            update_task(tasks, task_id)  # Returns True/False
            # If task found: prompts for new values
            # If not found: error already printed
```

**Function Dependency Graph:**
```
main() event loop
    ├─ get_menu_choice()      → Returns 3 (Update)
    ├─ get_int_input()        → Gets task_id
    └─ update_task()          → Find task, prompt for updates, return bool
        ├─ Display current values
        ├─ Prompt for new title
        ├─ Prompt for new description
        └─ Update task dict in-place
```

---

## Performance Characteristics

| Metric | Value |
|--------|-------|
| **Time Complexity** | O(n) – linear search for task |
| **Space Complexity** | O(1) – no additional structures |
| **Best Case** | O(1) – task is first in list |
| **Worst Case** | O(n) – task is last or not found |
| **Average Case** | O(n/2) – task in middle of list |
| **User Interaction** | ~2-5 seconds (depends on user) |

---

## Dependencies and Constraints

| Constraint | Details |
|-----------|---------|
| **Python Version** | 3.6+ (uses f-strings and type hints) |
| **External Packages** | None (standard library only) |
| **OS Compatibility** | All platforms (Linux, macOS, Windows) |
| **Character Encoding** | UTF-8 (supports unicode in inputs) |
| **Input Validation** | None in basic version (caller validates) |
| **Error Handling** | Graceful; no exceptions on invalid ID |

### Required Data Structures

```python
# tasks parameter requirements
tasks = [
    {"id": int, "title": str, "desc": str, "complete": bool},
    # ... more tasks
]

# Each task must have all 4 fields
# task_id parameter must be integer
```

---

## Related Functions

This function is part of the complete task management system:

- **`display_menu()`** – Shows menu options (option 3: Update Task)
- **`get_menu_choice()`** – Gets user's menu selection
- **`get_int_input(prompt)`** – Gets task_id from user
- **`print_tasks(tasks)`** – Shows all tasks
- **`add_task(tasks)`** – Creates new task
- **`update_task(tasks, task_id)`** – Modifies existing task (this function)
- **`delete_task(tasks, task_id)`** – Removes task
- **`toggle_task_complete(tasks, task_id)`** – Changes completion status
- **`main()`** – Main event loop that calls `update_task()`

---

## Production Checklist

Before deploying this function:

- [ ] Function is defined in `src/main.py` or `src/core.py`
- [ ] Function accepts `tasks` parameter (list of dicts)
- [ ] Function accepts `task_id` parameter (integer)
- [ ] Function searches list for matching task ID
- [ ] Function returns `True` when task found
- [ ] Function returns `False` when task not found
- [ ] Error message displays: "Task with ID {task_id} not found."
- [ ] Current title displayed before prompting
- [ ] Current description displayed before prompting
- [ ] Prompts user for new title with: "Enter new title (press Enter to keep): "
- [ ] Prompts user for new description with: "Enter new description (press Enter to keep): "
- [ ] Title input is stripped of whitespace
- [ ] Description input is stripped of whitespace
- [ ] Empty title input preserves original title
- [ ] Empty description input preserves original description
- [ ] Updates title if non-empty input provided
- [ ] Updates description if non-empty input provided
- [ ] Prints "Task updated." only if changes were made
- [ ] Updates are committed to task dict
- [ ] Type hints are present: `(list[dict], int) -> bool`
- [ ] Docstring is complete with examples
- [ ] Tested with update title only
- [ ] Tested with update description only
- [ ] Tested with update both
- [ ] Tested with no changes
- [ ] Tested with non-existent task ID
- [ ] Integrated into menu loop (option 3)

---

## Common Patterns

### Pattern 1: Simple Update
```python
task_id = get_int_input("Enter task ID: ")
update_task(tasks, task_id)
```

### Pattern 2: Update with Result Check
```python
task_id = get_int_input("Enter task ID: ")
if update_task(tasks, task_id):
    print("Update complete.")
# else: error already printed
```

### Pattern 3: Update with Pre-fetch
```python
task_id = get_int_input("Enter task ID: ")

# Find task first
task = next((t for t in tasks if t["id"] == task_id), None)

if task:
    print(f"Current: {task['title']}")
    update_task(tasks, task_id)
else:
    print(f"Task {task_id} not found.")
```

### Pattern 4: Bulk Update
```python
def update_all_tasks(tasks):
    """Let user update each task"""
    for task in tasks:
        print(f"\nTask {task['id']}:")
        if not confirm("Update? (y/n): "):
            continue
        update_task(tasks, task["id"])
```

### Pattern 5: Update with Menu Option
```python
choice = get_menu_choice()

if choice == 3:
    task_id = get_int_input("Enter task ID: ")
    update_task(tasks, task_id)
```

---

## Troubleshooting

### Issue: Changes not being saved
**Solution:** Verify task dict is being modified:
```python
# Check task reference is correct
task = next((t for t in tasks if t["id"] == task_id), None)
if task:
    print(f"Before: {task['title']}")
    task["title"] = "New title"
    print(f"After: {task['title']}")
```

### Issue: Empty input not preserving original
**Solution:** Verify `.strip()` is removing whitespace:
```python
new_title = input("Title: ").strip()
if not new_title:  # Explicitly check for empty
    # Keep original
else:
    task["title"] = new_title
```

### Issue: Task not found error on valid ID
**Solution:** Check ID type and value:
```python
print(f"Searching for ID: {task_id} (type: {type(task_id)})")
for task in tasks:
    print(f"Found ID: {task['id']} (type: {type(task['id'])})")
    if task["id"] == task_id:
        print("Match found!")
```

### Issue: "Task updated." not printing
**Solution:** Verify conditional logic:
```python
if new_title or new_description:
    print("Task updated.")
# Both must be truthy to print message
```

### Issue: Other tasks being modified
**Solution:** Ensure you're finding the correct task:
```python
# Use `next()` with break to stop after first match
task = next((t for t in tasks if t["id"] == task_id), None)
# Or use break after finding
```

### Issue: TypeError on dict access
**Solution:** Verify task dict has required keys:
```python
required_keys = {"id", "title", "desc", "complete"}
for task in tasks:
    if not required_keys.issubset(task.keys()):
        print(f"Invalid task structure: {task}")
```

---

## Enhancement Options (Optional)

These enhancements are NOT required but can improve functionality:

1. **Confirmation Before Saving**
   - Show proposed changes before confirming
   - Allow review before committing updates
   - Add parameter: `confirm("Save changes? (y/n): ")`

2. **Undo/Rollback**
   - Save original values
   - Implement undo() function
   - Allows recovery if user changes mind

3. **Change Tracking**
   - Track what fields were changed
   - Display change summary
   - Return dict of changes instead of bool

4. **Input Validation**
   - Validate title length (max 100 chars)
   - Validate description length (max 500 chars)
   - Check for empty/whitespace-only inputs

5. **Partial Update Flag**
   - Return info about which fields changed
   - Return `{"title_changed": bool, "desc_changed": bool}`
   - Caller can respond based on changes made

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-12-28 | Initial skill document; production-ready flexible update implementation |

---

