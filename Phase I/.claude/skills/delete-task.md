# Skill: Generate Safe Delete Task Function

**Owned by:** `core-todo-impl`
**Feature:** Todo App Phase I - Core Task Management
**Status:** Production-Ready

---

## Purpose

Generate the `delete_task(tasks: list[dict], task_id: int) -> bool` function that safely removes a task from the in-memory list by ID. This function searches for the task, deletes it if found, provides appropriate feedback, and returns a boolean indicating success or failure without raising index errors.

---

## When to Use

- **Menu Option 4:** When user selects "Delete Task" from main menu
- **Task Removal:** Whenever a task needs to be permanently removed
- **Safe Deletion:** When index errors must be avoided
- **Feedback Required:** When caller needs to know if deletion succeeded
- **Destructive Operations:** Typically paired with `confirm()` for safety

---

## Inputs

**Function Signature:**
```python
def delete_task(tasks: list[dict], task_id: int) -> bool:
```

**Parameter Details:**

- **`tasks`** (list[dict]): The in-memory list of tasks
  - May be empty
  - Each element is a dict with keys: id, title, desc, complete
  - Function modifies this list in-place (removes matching task)
  - Type hint: `list[dict]`

- **`task_id`** (int): The ID of the task to delete
  - Should match a task's "id" field
  - If no match found, function returns False
  - Type hint: `int`

**Return Value:** `bool`
- `True` if task found and deleted successfully
- `False` if task not found

---

## Step-by-Step Process

1. **Search for Task:**
   - Iterate through tasks list
   - Compare each task's "id" field with provided task_id
   - Continue until match found or list exhausted

2. **Task Found Branch:**
   - Remove task from list using `.remove()` method
   - This removes the FIRST occurrence of the task dict
   - Return `True` to indicate success

3. **Task Not Found Branch:**
   - Print error message: `"Task with ID {task_id} not found."`
   - Return `False` to indicate failure
   - No exception raised; graceful handling

4. **No Index Errors:**
   - Use iteration or list comprehension (not index access)
   - Avoid `tasks[i]` or `del tasks[i]` patterns
   - `.remove()` is safe; won't raise IndexError

---

## Output

**Function Name:** `delete_task(tasks: list[dict], task_id: int) -> bool`

**Return Value:** `True` (success) or `False` (failure)

**Example Output Flow 1 (Task Found):**
```
(No output - function runs silently and returns True)
Return value: True
```

**Example Output Flow 2 (Task Not Found):**
```
Task with ID 99 not found.
Return value: False
```

**Example Interactive Flow with Confirmation:**
```
Task: 1. Buy groceries - Milk, eggs, bread
Delete this task? (y/n): y
(Task is deleted; no output from delete_task itself)
Task deleted successfully!
```

**Example Interactive Flow with Cancellation:**
```
Task: 1. Buy groceries - Milk, eggs, bread
Delete this task? (y/n): n
Task not deleted.
```

---

## Implementation

### Python Code (Production-Ready) - Using .remove()

```python
def delete_task(tasks: list[dict], task_id: int) -> bool:
    """
    Delete a task from the task list by ID.

    Searches the task list for a task with matching ID. If found, removes
    the task from the list and returns True. If not found, prints an error
    message and returns False.

    This implementation uses list iteration and .remove(), avoiding index
    access and preventing IndexError exceptions.

    Args:
        tasks (list[dict]): The in-memory task list. Modified in-place by
                           removing the matching task if found.
        task_id (int): The ID of the task to delete. Matched against the
                      "id" field in each task dictionary.

    Returns:
        bool: True if task found and deleted successfully.
              False if task not found (error message printed).

    Example:
        >>> tasks = [
        ...     {"id": 1, "title": "Buy groceries", "desc": "Milk", "complete": False},
        ...     {"id": 2, "title": "Finish project", "desc": "By Friday", "complete": False}
        ... ]
        >>> delete_task(tasks, 1)
        True
        >>> print(tasks)
        [{"id": 2, "title": "Finish project", "desc": "By Friday", "complete": False}]

    Example - Task not found:
        >>> delete_task(tasks, 99)
        Task with ID 99 not found.
        False
    """
    # Iterate through tasks to find matching ID
    for task in tasks:
        if task["id"] == task_id:
            # Found task; remove it from list
            tasks.remove(task)
            return True

    # Task not found; print error and return False
    print(f"Task with ID {task_id} not found.")
    return False
```

### Alternative Implementation - Using List Comprehension

```python
def delete_task(tasks: list[dict], task_id: int) -> bool:
    """
    Delete a task from the task list by ID (using list comprehension).

    This implementation uses list comprehension to create a new list
    without the matching task, then reassigns it to the parameter.
    """
    # Find task to delete
    task_to_delete = None
    for task in tasks:
        if task["id"] == task_id:
            task_to_delete = task
            break

    # If found, remove and return True
    if task_to_delete:
        tasks[:] = [t for t in tasks if t["id"] != task_id]
        return True

    # Not found; print error and return False
    print(f"Task with ID {task_id} not found.")
    return False
```

### Alternative Implementation - Using next() with generator

```python
def delete_task(tasks: list[dict], task_id: int) -> bool:
    """
    Delete a task from the task list by ID (using next()).

    This implementation uses next() with a generator expression
    to find the task efficiently.
    """
    # Find task using next() and generator
    task_to_delete = next((t for t in tasks if t["id"] == task_id), None)

    # If found, remove and return True
    if task_to_delete:
        tasks.remove(task_to_delete)
        return True

    # Not found; print error and return False
    print(f"Task with ID {task_id} not found.")
    return False
```

### Design Notes

**Primary Implementation (Using .remove()):**
- **Simple and Clear:** Easy to understand; straightforward logic
- **Safe:** No index access; no IndexError possible
- **Efficient:** Linear search O(n), single pass through list
- **Pythonic:** Uses built-in `.remove()` method
- **In-Place Modification:** Modifies original list directly
- **Readable:** Loop structure is easy to follow

**Why .remove() is Recommended:**
- Finds and removes first matching object
- Raises ValueError if not found (we handle separately)
- More readable than list comprehension for this use case
- Better performance than filtering entire list

**Alternative Approaches:**
1. **List Comprehension** - More functional; creates new list
2. **next() + generator** - Most efficient; early exit possible
3. **enumerate with del** - NOT recommended (index errors risk)

---

## Implementation Comparison

| Approach | Pros | Cons | Recommendation |
|----------|------|------|-----------------|
| **for loop + .remove()** | Simple, clear, safe | One extra find | ✓ Primary |
| **List comprehension** | Functional style, clear intent | Creates new list | Alternative |
| **next() + generator** | Most efficient, early exit | Less readable | Advanced |
| **enumerate + del** | Direct removal | Risk of index errors | ✗ Avoid |

---

## Failure Handling

| Scenario | Behavior | Output |
|----------|----------|--------|
| **Task found** | Remove from list; return True | (No output) |
| **Task not found** | Print error message; return False | "Task with ID X not found." |
| **Empty list** | No task to find; return False | "Task with ID X not found." |
| **Negative ID** | No task matches; return False | "Task with ID -1 not found." |
| **ID zero** | No task matches (IDs start at 1); return False | "Task with ID 0 not found." |
| **Very large ID** | No task matches; return False | "Task with ID 999999 not found." |
| **tasks is None** | Raises TypeError on for loop | Propagates; caller must handle |
| **tasks is not a list** | Raises TypeError on iteration | Propagates; caller must handle |
| **task_id is None** | Raises TypeError on comparison | Propagates; caller must handle |
| **task_id is not int** | May cause comparison issues | Propagates or silent failure |
| **Duplicate IDs in list** | Removes first matching task only | Works correctly (removes first) |
| **Missing "id" key in task** | Raises KeyError on comparison | Propagates; data corruption |

**Note on Error Propagation:**
The basic implementation lets structural errors (TypeError, KeyError) propagate. This is appropriate because:
- Indicates caller passed invalid data
- Helps catch bugs in data structure
- Caller can wrap in try/except if needed

### Enhanced Version with Input Validation (Optional)

```python
def delete_task(tasks: list[dict], task_id: int) -> bool:
    """Delete task with input validation"""
    # Validate inputs
    if not isinstance(tasks, list):
        raise TypeError("tasks must be a list")
    if not isinstance(task_id, int):
        raise TypeError("task_id must be an integer")

    # Search and delete
    for task in tasks:
        if task.get("id") == task_id:
            tasks.remove(task)
            return True

    print(f"Task with ID {task_id} not found.")
    return False
```

---

## Acceptance Criteria

- ✓ Function accepts tasks list parameter
- ✓ Function accepts task_id integer parameter
- ✓ Function returns boolean (True or False)
- ✓ Returns True when task found and deleted
- ✓ Returns False when task not found
- ✓ Prints error message when task not found
- ✓ Error message format: "Task with ID {task_id} not found."
- ✓ Removes task from list (modifies in-place)
- ✓ Uses safe deletion (no index access)
- ✓ No IndexError raised on invalid ID
- ✓ Works with empty list
- ✓ Works with single task
- ✓ Works with multiple tasks
- ✓ Works with non-sequential IDs
- ✓ Type hints are correct: `(list[dict], int) -> bool`
- ✓ Docstring is complete with examples

---

## Testing Checklist

```python
import io
import sys
from unittest.mock import patch

# Test 1: Function exists and is callable
assert callable(delete_task)

# Test 2: Delete from single-task list
tasks = [{"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False}]
result = delete_task(tasks, 1)
assert result is True
assert len(tasks) == 0
assert isinstance(result, bool)

# Test 3: Delete from multi-task list
tasks = [
    {"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False},
    {"id": 2, "title": "Task 2", "desc": "Desc 2", "complete": False},
    {"id": 3, "title": "Task 3", "desc": "Desc 3", "complete": False}
]
result = delete_task(tasks, 2)
assert result is True
assert len(tasks) == 2
assert not any(t["id"] == 2 for t in tasks)
assert tasks[0]["id"] == 1
assert tasks[1]["id"] == 3

# Test 4: Delete first task from list
tasks = [
    {"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False},
    {"id": 2, "title": "Task 2", "desc": "Desc 2", "complete": False}
]
result = delete_task(tasks, 1)
assert result is True
assert len(tasks) == 1
assert tasks[0]["id"] == 2

# Test 5: Delete last task from list
tasks = [
    {"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False},
    {"id": 2, "title": "Task 2", "desc": "Desc 2", "complete": False}
]
result = delete_task(tasks, 2)
assert result is True
assert len(tasks) == 1
assert tasks[0]["id"] == 1

# Test 6: Task not found - empty list
tasks = []
captured_output = io.StringIO()
sys.stdout = captured_output
result = delete_task(tasks, 1)
sys.stdout = sys.__stdout__
assert result is False
assert "Task with ID 1 not found." in captured_output.getvalue()

# Test 7: Task not found - in populated list
tasks = [
    {"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False},
    {"id": 2, "title": "Task 2", "desc": "Desc 2", "complete": False}
]
captured_output = io.StringIO()
sys.stdout = captured_output
result = delete_task(tasks, 99)
sys.stdout = sys.__stdout__
assert result is False
assert "Task with ID 99 not found." in captured_output.getvalue()
assert len(tasks) == 2  # List unchanged

# Test 8: Task not found - negative ID
tasks = [{"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False}]
captured_output = io.StringIO()
sys.stdout = captured_output
result = delete_task(tasks, -5)
sys.stdout = sys.__stdout__
assert result is False
assert "Task with ID -5 not found." in captured_output.getvalue()

# Test 9: Task not found - ID zero
tasks = [{"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False}]
captured_output = io.StringIO()
sys.stdout = captured_output
result = delete_task(tasks, 0)
sys.stdout = sys.__stdout__
assert result is False
assert "Task with ID 0 not found." in captured_output.getvalue()

# Test 10: Task not found - very large ID
tasks = [{"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False}]
captured_output = io.StringIO()
sys.stdout = captured_output
result = delete_task(tasks, 999999)
sys.stdout = sys.__stdout__
assert result is False
assert "Task with ID 999999 not found." in captured_output.getvalue()

# Test 11: Delete from list with non-sequential IDs
tasks = [
    {"id": 5, "title": "Task 5", "desc": "Desc 5", "complete": False},
    {"id": 10, "title": "Task 10", "desc": "Desc 10", "complete": False},
    {"id": 3, "title": "Task 3", "desc": "Desc 3", "complete": False}
]
result = delete_task(tasks, 10)
assert result is True
assert len(tasks) == 2
assert not any(t["id"] == 10 for t in tasks)

# Test 12: Delete from list with gaps in IDs
tasks = [
    {"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False},
    {"id": 5, "title": "Task 5", "desc": "Desc 5", "complete": False},
    {"id": 9, "title": "Task 9", "desc": "Desc 9", "complete": False}
]
result = delete_task(tasks, 5)
assert result is True
assert len(tasks) == 2

# Test 13: Verify correct error message format
tasks = []
captured_output = io.StringIO()
sys.stdout = captured_output
delete_task(tasks, 42)
sys.stdout = sys.__stdout__
output = captured_output.getvalue().strip()
assert output == "Task with ID 42 not found."

# Test 14: List modification is in-place
original_tasks = [{"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False}]
task_list_ref = original_tasks
delete_task(task_list_ref, 1)
assert len(original_tasks) == 0  # Original list was modified

# Test 15: Completed tasks can be deleted
tasks = [{"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": True}]
result = delete_task(tasks, 1)
assert result is True
assert len(tasks) == 0

# Test 16: Delete only removes first matching task (duplicates)
# Note: In normal operation, duplicates shouldn't exist, but test robustness
tasks = [
    {"id": 1, "title": "Task 1", "desc": "Desc 1a", "complete": False},
    {"id": 1, "title": "Task 1", "desc": "Desc 1b", "complete": False},  # Duplicate ID
    {"id": 2, "title": "Task 2", "desc": "Desc 2", "complete": False}
]
result = delete_task(tasks, 1)
assert result is True
assert len(tasks) == 2
assert sum(1 for t in tasks if t["id"] == 1) == 1  # One duplicate remains

# Test 17: Delete with special characters in task data
tasks = [
    {"id": 1, "title": "Task @#$%", "desc": "Desc with symbols!", "complete": False}
]
result = delete_task(tasks, 1)
assert result is True
assert len(tasks) == 0

# Test 18: Delete with unicode characters in task data
tasks = [
    {"id": 1, "title": "Task 🛒", "desc": "Buy 🥛 and 🍞", "complete": False}
]
result = delete_task(tasks, 1)
assert result is True
assert len(tasks) == 0

# Test 19: Delete leaves other tasks unchanged
tasks = [
    {"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False},
    {"id": 2, "title": "Task 2", "desc": "Desc 2", "complete": True},
    {"id": 3, "title": "Task 3", "desc": "Desc 3", "complete": False}
]
delete_task(tasks, 2)
assert tasks[0]["id"] == 1
assert tasks[0]["title"] == "Task 1"
assert tasks[1]["id"] == 3
assert tasks[1]["complete"] is False

# Test 20: Multiple sequential deletes
tasks = [
    {"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False},
    {"id": 2, "title": "Task 2", "desc": "Desc 2", "complete": False},
    {"id": 3, "title": "Task 3", "desc": "Desc 3", "complete": False}
]
assert delete_task(tasks, 1) is True
assert len(tasks) == 2
assert delete_task(tasks, 3) is True
assert len(tasks) == 1
assert delete_task(tasks, 2) is True
assert len(tasks) == 0
assert delete_task(tasks, 1) is False
```

---

## Usage Examples

### Example 1: Simple Delete
```python
tasks = [
    {"id": 1, "title": "Buy groceries", "desc": "Milk, eggs, bread", "complete": False},
    {"id": 2, "title": "Finish project", "desc": "Submit by Friday", "complete": False}
]

if delete_task(tasks, 1):
    print("Task deleted successfully!")
else:
    print("Could not delete task.")
```

**Output:**
```
Task deleted successfully!
```

**Result:**
```python
tasks = [
    {"id": 2, "title": "Finish project", "desc": "Submit by Friday", "complete": False}
]
```

### Example 2: Delete with User Feedback
```python
def delete_task_operation(tasks, task_id):
    """Handle delete with feedback"""
    if delete_task(tasks, task_id):
        print("Task deleted successfully!")
    # else: error message already printed by delete_task()
```

**Interactive Flow:**
```
If task found:
(No output from delete_task)
Task deleted successfully!

If task not found:
Task with ID 99 not found.
(No additional message from delete_task_operation)
```

### Example 3: Delete with Confirmation (Recommended Pattern)
```python
def delete_task_with_confirmation(tasks, task_id):
    """Delete task with safety confirmation"""
    # Find and display task
    task = next((t for t in tasks if t["id"] == task_id), None)

    if not task:
        print(f"Task with ID {task_id} not found.")
        return False

    # Show what will be deleted
    print(f"Task: {task['id']}. {task['title']} - {task['desc']}")

    # Get confirmation
    if confirm("Delete this task? (y/n): "):
        # Perform deletion
        if delete_task(tasks, task_id):
            print("Task deleted successfully!")
            return True
    else:
        print("Task not deleted.")
        return False
```

**Interactive Flow:**
```
Task: 1. Buy groceries - Milk, eggs, bread
Delete this task? (y/n): y
Task deleted successfully!

Task: 1. Buy groceries - Milk, eggs, bread
Delete this task? (y/n): n
Task not deleted.
```

### Example 4: Delete from Menu Loop
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
            task_id = get_int_input("Enter task ID: ")
            update_task(tasks, task_id)
        elif choice == 4:
            task_id = get_int_input("Enter task ID to delete: ")

            # Find task to show before deleting
            task = next((t for t in tasks if t["id"] == task_id), None)
            if task:
                print(f"Task: {task['id']}. {task['title']} - {task['desc']}")
                if confirm("Delete this task? (y/n): "):
                    delete_task(tasks, task_id)
                    print("Task deleted successfully!")
                else:
                    print("Task not deleted.")
            else:
                print(f"Task with ID {task_id} not found.")

        elif choice == 5:
            task_id = get_int_input("Enter task ID: ")
            toggle_task_complete(tasks, task_id)

        print()
```

### Example 5: Bulk Delete by Criteria
```python
def delete_all_completed(tasks):
    """Delete all completed tasks"""
    completed = [t for t in tasks if t["complete"]]

    if not completed:
        print("No completed tasks to delete.")
        return

    print(f"Found {len(completed)} completed tasks:")
    for task in completed:
        print(f"  - {task['title']}")

    if confirm("Delete all these tasks? (yes/no): "):
        for task in completed:
            delete_task(tasks, task["id"])
        print(f"Deleted {len(completed)} tasks!")
    else:
        print("No tasks deleted.")
```

**Interactive Flow:**
```
Found 2 completed tasks:
  - Finish Python project
  - Call mom
Delete all these tasks? (yes/no): yes
Deleted 2 tasks!
```

---

## Integration with Other Functions

This function is part of the task management lifecycle:

```python
# Delete operation in main loop
def main():
    tasks = []

    while True:
        choice = get_menu_choice()  # User selects option 4

        if choice == 4:
            task_id = get_int_input("Enter task ID to delete: ")

            # Show task first (optional)
            task = next((t for t in tasks if t["id"] == task_id), None)
            if task:
                print_task(task)  # Display what will be deleted

                # Get confirmation (safety measure)
                if confirm("Delete? (y/n): "):
                    # Perform deletion
                    if delete_task(tasks, task_id):  # Returns True/False
                        print("Deleted successfully!")
                    # else: error already printed by delete_task()
```

**Function Dependency Graph:**
```
main() event loop
    ├─ get_menu_choice()  → Returns 4 (Delete)
    ├─ get_int_input()    → Gets task_id
    ├─ (find task for display)
    ├─ confirm()          → "Delete? (y/n):"
    └─ delete_task()      → Remove task, return True/False
        └─ print error if not found
```

---

## Performance Characteristics

| Metric | Value |
|--------|-------|
| **Time Complexity** | O(n) – linear search through list |
| **Space Complexity** | O(1) – no additional structures created |
| **Best Case** | O(1) – task is first in list |
| **Worst Case** | O(n) – task is last or not found |
| **Average Case** | O(n/2) – task in middle of list |
| **Comparison Operations** | Up to n comparisons (one per task) |

---

## Dependencies and Constraints

| Constraint | Details |
|-----------|---------|
| **Python Version** | 3.6+ (uses f-strings and type hints) |
| **External Packages** | None (standard library only) |
| **OS Compatibility** | All platforms (Linux, macOS, Windows) |
| **Character Encoding** | UTF-8 (supports unicode in task data) |
| **Input Validation** | None in basic version (caller validates) |
| **Error Handling** | Graceful; no exceptions on invalid ID |

### Required Data Structures

```python
# tasks parameter requirements
tasks = [
    {"id": int, "title": str, "desc": str, "complete": bool},
    # ... more tasks
]

# Each task must have "id" field
# task_id parameter must be integer
```

---

## Related Functions

This function is part of the complete task management system:

- **`display_menu()`** – Shows menu options (option 4: Delete Task)
- **`get_menu_choice()`** – Gets user's menu selection
- **`get_int_input(prompt)`** – Gets task_id from user
- **`confirm(prompt)`** – Gets confirmation before deleting
- **`print_tasks(tasks)`** – Shows all tasks
- **`add_task(tasks)`** – Creates new task
- **`update_task(tasks, task_id, ...)`** – Modifies existing task
- **`delete_task(tasks, task_id)`** – Removes task (this function)
- **`toggle_task_complete(tasks, task_id)`** – Changes completion status
- **`main()`** – Main event loop that calls `delete_task()`

---

## Production Checklist

Before deploying this function:

- [ ] Function is defined in `src/main.py` or `src/core.py`
- [ ] Function accepts `tasks` parameter (list of dicts)
- [ ] Function accepts `task_id` parameter (integer)
- [ ] Function searches list for matching task ID
- [ ] Function returns `True` when task found and deleted
- [ ] Function returns `False` when task not found
- [ ] Error message displays: "Task with ID {task_id} not found."
- [ ] Task is removed from list (in-place modification)
- [ ] Uses safe deletion (no index access)
- [ ] No IndexError raised on invalid ID
- [ ] Works with empty list
- [ ] Works with single task
- [ ] Works with multiple tasks
- [ ] Works with non-sequential IDs
- [ ] Works with gaps in ID numbering
- [ ] Type hints are present: `(list[dict], int) -> bool`
- [ ] Docstring is complete with examples
- [ ] Tested with delete confirmation
- [ ] Integrated into menu loop (option 4)
- [ ] Integrated with `confirm()` for safety

---

## Common Patterns

### Pattern 1: Simple Delete (No Feedback)
```python
tasks = [...]
delete_task(tasks, task_id)  # Ignore return value
```

### Pattern 2: Delete with Result Check
```python
if delete_task(tasks, task_id):
    print("Task deleted successfully!")
# else: error already printed by delete_task()
```

### Pattern 3: Delete with Confirmation (Recommended)
```python
if confirm(f"Delete task {task_id}? (y/n): "):
    if delete_task(tasks, task_id):
        print("Task deleted!")
```

### Pattern 4: Delete with Pre-check
```python
# Find task first
task = next((t for t in tasks if t["id"] == task_id), None)

if task:
    print_task(task)  # Show what will be deleted
    if confirm("Delete? (y/n): "):
        delete_task(tasks, task_id)
else:
    print(f"Task {task_id} not found.")
```

### Pattern 5: Safe Delete with Try/Except
```python
try:
    if delete_task(tasks, task_id):
        print("Deleted!")
except (TypeError, KeyError) as e:
    print(f"Error: {e}")
```

---

## Troubleshooting

### Issue: IndexError on deletion
**Solution:** Use `.remove()` instead of `del tasks[index]`:
```python
# Correct - no index errors possible
for task in tasks:
    if task["id"] == task_id:
        tasks.remove(task)

# Incorrect - can raise IndexError
for i, task in enumerate(tasks):
    if task["id"] == task_id:
        del tasks[i]  # Dangerous!
```

### Issue: Task not being deleted
**Solution:** Verify task ID matches exactly:
```python
# Verify ID types
print(f"Searching for: {task_id} (type: {type(task_id)})")
for task in tasks:
    print(f"Found: {task['id']} (type: {type(task['id'])})")
    if task["id"] == task_id:
        print("Match found!")
```

### Issue: Wrong task deleted
**Solution:** Check for duplicate IDs in list:
```python
# List duplicate IDs
from collections import Counter
ids = [t["id"] for t in tasks]
duplicates = [id for id, count in Counter(ids).items() if count > 1]
print(f"Duplicate IDs: {duplicates}")
```

### Issue: Error message not displaying
**Solution:** Verify print statement is executed:
```python
print(f"Task with ID {task_id} not found.")
```

### Issue: Function returns None instead of bool
**Solution:** Ensure all code paths return boolean:
```python
# All paths must return bool
for task in tasks:
    if task["id"] == task_id:
        tasks.remove(task)
        return True  # ← Explicit return

print(f"Task with ID {task_id} not found.")
return False  # ← Explicit return
```

### Issue: TypeError on list operation
**Solution:** Validate input types:
```python
if not isinstance(tasks, list):
    raise TypeError("tasks must be a list")
if not isinstance(task_id, int):
    raise TypeError("task_id must be an integer")
```

---

## Enhancement Options (Optional)

These enhancements are NOT required but can improve functionality:

1. **Soft Delete (Archive)**
   - Mark task as deleted instead of removing
   - Add "deleted" field: `{"id": 1, ..., "deleted": True}`
   - Allows recovery/undo operations

2. **Return Deleted Task**
   - Return the deleted task dict instead of bool
   - Allows caller to access deleted task data
   - Signal failure with None return

3. **Batch Delete by Criteria**
   - Add parameter for filter function
   - Delete all tasks matching criteria
   - Return count of deleted tasks

4. **Delete with Undo Stack**
   - Maintain stack of deleted tasks
   - Implement undo() function
   - Allows recovery of recently deleted tasks

5. **Audit Logging**
   - Log who deleted what and when
   - Add timestamp and deletion reason
   - Create audit trail for accountability

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-12-28 | Initial skill document; production-ready safe deletion implementation |

---

