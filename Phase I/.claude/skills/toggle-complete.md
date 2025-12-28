# Skill: Generate Toggle Task Completion Function

**Owned by:** `core-todo-impl`
**Feature:** Todo App Phase I - Core Task Management
**Status:** Production-Ready

---

## Purpose

Generate the `toggle_complete(tasks: list[dict], task_id: int) -> bool` function that safely toggles a task's completion status. This function finds the task by ID, inverts its `complete` boolean field, provides clear feedback about the new status, and returns a boolean indicating success or failure.

---

## When to Use

- **Menu Option 5:** When user selects "Mark as Complete/Incomplete" from main menu
- **Completion Tracking:** When toggling task completion status
- **Status Change:** When task is marked done or reverted to pending
- **Quick Updates:** When only completion status needs to change (not title/description)

---

## Inputs

**Function Signature:**
```python
def toggle_complete(tasks: list[dict], task_id: int) -> bool:
```

**Parameter Details:**

- **`tasks`** (list[dict]): The in-memory list of tasks
  - Contains existing task dicts with id, title, desc, complete
  - Function modifies task's `complete` field in-place
  - Type hint: `list[dict]`

- **`task_id`** (int): The ID of the task to toggle
  - Matched against task's "id" field
  - If no match found, function returns False
  - Type hint: `int`

**Return Value:** `bool`
- `True` if task found and toggled successfully
- `False` if task not found

---

## Step-by-Step Process

1. **Find Task by ID:**
   - Search tasks list for task with matching ID
   - Iterate through all tasks until match found
   - If not found, skip to step 4

2. **Toggle Completion Status:**
   - Get current value: `current_status = task['complete']`
   - Invert it: `task['complete'] = not current_status`
   - This flips True ↔ False

3. **Print Status Message:**
   - Determine new status from inverted value
   - If now True: print "Task marked as complete."
   - If now False: print "Task marked as incomplete."
   - Message reflects new status (not old status)

4. **Return Success/Failure:**
   - If task found and toggled: return `True`
   - If task not found: print error message and return `False`
   - Error message: `"Task with ID {task_id} not found."`

---

## Output

**Function Name:** `toggle_complete(tasks: list[dict], task_id: int) -> bool`

**Return Value:** `True` (success) or `False` (task not found)

**Example Output Flow 1 (Toggle False → True):**
```
Task marked as complete.
Return value: True
```

Task before: `{"id": 1, ..., "complete": False}`
Task after: `{"id": 1, ..., "complete": True}`

**Example Output Flow 2 (Toggle True → False):**
```
Task marked as incomplete.
Return value: True
```

Task before: `{"id": 1, ..., "complete": True}`
Task after: `{"id": 1, ..., "complete": False}`

**Example Output Flow 3 (Task Not Found):**
```
Task with ID 99 not found.
Return value: False
```

**Example Interactive Flow with Menu:**
```
Todo App
========
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark as Complete/Incomplete
0. Exit

Choose an option: 5

Enter task ID: 1
Task marked as complete.
```

---

## Implementation

### Python Code (Production-Ready)

```python
def toggle_complete(tasks: list[dict], task_id: int) -> bool:
    """
    Toggle the completion status of a task.

    Searches for a task by ID. If found, inverts the 'complete' boolean
    field (True becomes False, False becomes True), prints a status message
    indicating the new state, and returns True. If not found, prints an
    error message and returns False.

    Args:
        tasks (list[dict]): The in-memory task list. Modified in-place if
                           task is found by inverting its 'complete' field.
        task_id (int): The ID of the task to toggle. Matched against the
                      "id" field in task dictionaries.

    Returns:
        bool: True if task found and toggled successfully.
              False if task not found (error message printed).

    Example - Toggle incomplete to complete:
        >>> tasks = [
        ...     {"id": 1, "title": "Buy groceries", "desc": "Milk", "complete": False}
        ... ]
        >>> toggle_complete(tasks, 1)
        Task marked as complete.
        True
        >>> tasks[0]["complete"]
        True

    Example - Toggle complete to incomplete:
        >>> tasks[0]["complete"] = True
        >>> toggle_complete(tasks, 1)
        Task marked as incomplete.
        True
        >>> tasks[0]["complete"]
        False

    Example - Task not found:
        >>> toggle_complete(tasks, 99)
        Task with ID 99 not found.
        False
    """
    # Find task by ID
    for task in tasks:
        if task["id"] == task_id:
            # Toggle the completion status
            task["complete"] = not task["complete"]

            # Print status message based on new status
            if task["complete"]:
                print("Task marked as complete.")
            else:
                print("Task marked as incomplete.")

            return True

    # Task not found
    print(f"Task with ID {task_id} not found.")
    return False
```

### Design Notes

- **Simple Boolean Toggle:** Uses `not` operator to invert True ↔ False
- **Dynamic Message:** Message reflects new status, not old status
- **Single Pass Search:** Finds and toggles in one loop iteration
- **Early Return:** Returns immediately after toggling or error
- **Clear Feedback:** User knows the new status of the task
- **No Confirmation:** Toggling is reversible (can toggle again)
- **In-Place Modification:** Direct update to task dict
- **Type Hints:** Complete type annotations
- **Comprehensive Docstring:** Includes purpose, args, returns, and examples

### Why This Design?

| Decision | Rationale |
|----------|-----------|
| **Use `not` operator** | Simplest way to toggle boolean in Python |
| **Show new status** | User knows result of operation immediately |
| **No confirmation** | Toggle is reversible; user can redo if needed |
| **Single message** | Clear, simple; not verbose or confusing |
| **Early return on find** | Efficient; stops searching after finding task |
| **Return bool** | Caller knows if operation succeeded |
| **In-place modification** | Direct update; no need to rebuild list |

---

## Completion Status Messages

### Message Logic

```python
if task["complete"]:
    print("Task marked as complete.")
else:
    print("Task marked as incomplete.")
```

### Examples

| Before | After | Message |
|--------|-------|---------|
| `False` (incomplete) | `True` (complete) | "Task marked as complete." |
| `True` (complete) | `False` (incomplete) | "Task marked as incomplete." |

### Message Clarity

- **Reflects new state** – Message tells user what state task is in NOW
- **Action-oriented** – Uses "marked as" to show action performed
- **Clear terminology** – "complete" vs "incomplete" (not "done"/"not done")
- **Consistent format** – Both messages follow same pattern

---

## Failure Handling

| Scenario | Behavior | Output |
|----------|----------|--------|
| **Task found, incomplete → complete** | Toggle to True; print message | "Task marked as complete." |
| **Task found, complete → incomplete** | Toggle to False; print message | "Task marked as incomplete." |
| **Task not found** | Print error; return False | "Task with ID X not found." |
| **Empty list** | Print error; return False | "Task with ID X not found." |
| **Negative ID** | Print error (not found); return False | "Task with ID -1 not found." |
| **Very large ID** | Print error (not found); return False | "Task with ID 999999 not found." |
| **Duplicate IDs** | Toggles first matching task only | Works correctly |
| **tasks is None** | Raises TypeError on iteration | Propagates |
| **task_id is not int** | May cause comparison issues | Silent failure or exception |
| **Missing 'complete' key** | Raises KeyError on access | Propagates |
| **Ctrl+C** | Raises KeyboardInterrupt | Propagates |

**Note on Error Handling:**
The basic implementation lets structural errors (TypeError, KeyError) propagate. This is appropriate because:
- Indicates caller passed invalid data
- Helps catch bugs in data structure
- Caller can wrap in try/except if needed

### Enhanced Version with Input Validation (Optional)

```python
def toggle_complete(tasks: list[dict], task_id: int) -> bool:
    """Toggle complete with input validation"""
    if not isinstance(tasks, list):
        raise TypeError("tasks must be a list")
    if not isinstance(task_id, int):
        raise TypeError("task_id must be an integer")

    for task in tasks:
        if task.get("id") == task_id:
            task["complete"] = not task["complete"]

            if task["complete"]:
                print("Task marked as complete.")
            else:
                print("Task marked as incomplete.")

            return True

    print(f"Task with ID {task_id} not found.")
    return False
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
- ✓ Toggles completion status (inverts boolean value)
- ✓ Prints "Task marked as complete." when marked complete
- ✓ Prints "Task marked as incomplete." when marked incomplete
- ✓ Message reflects new status (not previous status)
- ✓ Returns True when task found and toggled
- ✓ Modifies task dict in-place
- ✓ Works with incomplete → complete transition
- ✓ Works with complete → incomplete transition
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
assert callable(toggle_complete)

# Test 2: Toggle incomplete to complete
tasks = [{"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False}]
captured_output = io.StringIO()
sys.stdout = captured_output
result = toggle_complete(tasks, 1)
sys.stdout = sys.__stdout__
output = captured_output.getvalue()

assert result is True
assert tasks[0]["complete"] is True
assert "Task marked as complete." in output
assert isinstance(result, bool)

# Test 3: Toggle complete to incomplete
tasks = [{"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": True}]
captured_output = io.StringIO()
sys.stdout = captured_output
result = toggle_complete(tasks, 1)
sys.stdout = sys.__stdout__
output = captured_output.getvalue()

assert result is True
assert tasks[0]["complete"] is False
assert "Task marked as incomplete." in output

# Test 4: Toggle back to complete
tasks = [{"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False}]
toggle_complete(tasks, 1)
assert tasks[0]["complete"] is True
toggle_complete(tasks, 1)
assert tasks[0]["complete"] is False
toggle_complete(tasks, 1)
assert tasks[0]["complete"] is True

# Test 5: Task not found
tasks = [{"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False}]
captured_output = io.StringIO()
sys.stdout = captured_output
result = toggle_complete(tasks, 99)
sys.stdout = sys.__stdout__
output = captured_output.getvalue()

assert result is False
assert "Task with ID 99 not found." in output
assert tasks[0]["complete"] is False  # Unchanged

# Test 6: Empty list
tasks = []
captured_output = io.StringIO()
sys.stdout = captured_output
result = toggle_complete(tasks, 1)
sys.stdout = sys.__stdout__
output = captured_output.getvalue()

assert result is False
assert "Task with ID 1 not found." in output

# Test 7: Toggle in multi-task list (finds correct task)
tasks = [
    {"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False},
    {"id": 2, "title": "Task 2", "desc": "Desc 2", "complete": False},
    {"id": 3, "title": "Task 3", "desc": "Desc 3", "complete": False}
]
result = toggle_complete(tasks, 2)

assert result is True
assert tasks[0]["complete"] is False  # Unchanged
assert tasks[1]["complete"] is True   # Toggled
assert tasks[2]["complete"] is False  # Unchanged

# Test 8: Toggle with negative ID
tasks = [{"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False}]
captured_output = io.StringIO()
sys.stdout = captured_output
result = toggle_complete(tasks, -5)
sys.stdout = sys.__stdout__

assert result is False
assert "Task with ID -5 not found." in output

# Test 9: Toggle with ID zero
tasks = [{"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False}]
captured_output = io.StringIO()
sys.stdout = captured_output
result = toggle_complete(tasks, 0)
sys.stdout = sys.__stdout__

assert result is False
assert "Task with ID 0 not found." in output

# Test 10: Toggle with very large ID
tasks = [{"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False}]
captured_output = io.StringIO()
sys.stdout = captured_output
result = toggle_complete(tasks, 999999)
sys.stdout = sys.__stdout__

assert result is False
assert "Task with ID 999999 not found." in output

# Test 11: Toggle preserves other fields
tasks = [
    {
        "id": 1,
        "title": "Buy groceries",
        "desc": "Milk, eggs, bread",
        "complete": False
    }
]
toggle_complete(tasks, 1)

assert tasks[0]["id"] == 1
assert tasks[0]["title"] == "Buy groceries"
assert tasks[0]["desc"] == "Milk, eggs, bread"
assert tasks[0]["complete"] is True

# Test 12: Multiple toggles in sequence
tasks = [{"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False}]

result1 = toggle_complete(tasks, 1)
assert result1 is True
assert tasks[0]["complete"] is True

result2 = toggle_complete(tasks, 1)
assert result2 is True
assert tasks[0]["complete"] is False

result3 = toggle_complete(tasks, 1)
assert result3 is True
assert tasks[0]["complete"] is True

# Test 13: Toggle first task in list
tasks = [
    {"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False},
    {"id": 2, "title": "Task 2", "desc": "Desc 2", "complete": False}
]
result = toggle_complete(tasks, 1)

assert result is True
assert tasks[0]["complete"] is True
assert tasks[1]["complete"] is False

# Test 14: Toggle last task in list
tasks = [
    {"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False},
    {"id": 2, "title": "Task 2", "desc": "Desc 2", "complete": False}
]
result = toggle_complete(tasks, 2)

assert result is True
assert tasks[0]["complete"] is False
assert tasks[1]["complete"] is True

# Test 15: Toggle with non-sequential IDs
tasks = [
    {"id": 5, "title": "Task 5", "desc": "Desc 5", "complete": False},
    {"id": 10, "title": "Task 10", "desc": "Desc 10", "complete": True},
    {"id": 3, "title": "Task 3", "desc": "Desc 3", "complete": False}
]
result = toggle_complete(tasks, 10)

assert result is True
assert tasks[1]["complete"] is False  # Was True, now False

# Test 16: Verify correct message for incomplete to complete
tasks = [{"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False}]
captured_output = io.StringIO()
sys.stdout = captured_output
toggle_complete(tasks, 1)
sys.stdout = sys.__stdout__
output = captured_output.getvalue().strip()

assert output == "Task marked as complete."

# Test 17: Verify correct message for complete to incomplete
tasks = [{"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": True}]
captured_output = io.StringIO()
sys.stdout = captured_output
toggle_complete(tasks, 1)
sys.stdout = sys.__stdout__
output = captured_output.getvalue().strip()

assert output == "Task marked as incomplete."

# Test 18: List modification is in-place
original_tasks = [{"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False}]
task_ref = original_tasks
toggle_complete(task_ref, 1)

assert original_tasks[0]["complete"] is True  # Original modified

# Test 19: Toggle with special characters in task data
tasks = [
    {"id": 1, "title": "Task @#$%", "desc": "Desc with symbols!", "complete": False}
]
result = toggle_complete(tasks, 1)

assert result is True
assert tasks[0]["complete"] is True

# Test 20: Toggle with unicode characters in task data
tasks = [
    {"id": 1, "title": "Task 🛒", "desc": "Buy 🥛 and 🍞", "complete": False}
]
result = toggle_complete(tasks, 1)

assert result is True
assert tasks[0]["complete"] is True
assert tasks[0]["title"] == "Task 🛒"  # Title unchanged
```

---

## Usage Examples

### Example 1: Toggle Incomplete to Complete
```python
tasks = [
    {"id": 1, "title": "Buy groceries", "desc": "Milk, eggs, bread", "complete": False}
]

toggle_complete(tasks, 1)
```

**Output:**
```
Task marked as complete.
```

**Result:**
```python
tasks[0]["complete"] = True
```

### Example 2: Toggle Complete to Incomplete
```python
# Assuming task is currently complete
tasks[0]["complete"] = True

toggle_complete(tasks, 1)
```

**Output:**
```
Task marked as incomplete.
```

**Result:**
```python
tasks[0]["complete"] = False
```

### Example 3: Toggle with Result Check
```python
tasks = [
    {"id": 1, "title": "Buy groceries", "desc": "Milk, eggs, bread", "complete": False}
]

if toggle_complete(tasks, 1):
    print("Completion status updated!")
else:
    print("Task not found.")
```

**Output:**
```
Task marked as complete.
Completion status updated!
```

### Example 4: Multiple Toggles
```python
tasks = [
    {"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False},
    {"id": 2, "title": "Task 2", "desc": "Desc 2", "complete": False},
    {"id": 3, "title": "Task 3", "desc": "Desc 3", "complete": False}
]

# Mark all tasks as complete
for task in tasks:
    toggle_complete(tasks, task["id"])
```

**Output:**
```
Task marked as complete.
Task marked as complete.
Task marked as complete.
```

**Result:**
```python
# All tasks now have complete=True
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
            update_task(tasks, task_id)
        elif choice == 4:
            task_id = get_int_input("Enter task ID to delete: ")
            delete_task(tasks, task_id)
        elif choice == 5:
            task_id = get_int_input("Enter task ID to toggle: ")
            toggle_complete(tasks, task_id)

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

Choose an option: 5

Enter task ID to toggle: 1
Task marked as complete.

Todo App
========
...
```

### Example 6: With Confirmation (Optional Safety)
```python
def toggle_with_confirmation(tasks, task_id):
    """Toggle completion with user confirmation"""
    # Find task
    task = next((t for t in tasks if t["id"] == task_id), None)

    if not task:
        print(f"Task with ID {task_id} not found.")
        return False

    # Show current status
    status = "complete" if task["complete"] else "incomplete"
    new_status = "incomplete" if task["complete"] else "complete"

    print(f"Current status: {status}")

    # Get confirmation
    if confirm(f"Mark as {new_status}? (y/n): "):
        toggle_complete(tasks, task_id)
        return True
    else:
        print("Status not changed.")
        return False
```

**Interactive Flow:**
```
Current status: incomplete
Mark as complete? (y/n): y
Task marked as complete.
```

---

## Integration with Other Functions

This function is part of the task management lifecycle:

```python
# Toggle operation in main loop
def main():
    tasks = []

    while True:
        choice = get_menu_choice()

        if choice == 5:
            task_id = get_int_input("Enter task ID: ")
            toggle_complete(tasks, task_id)  # Returns True/False
            # Message already printed by toggle_complete()
```

**Function Dependency Graph:**
```
main() event loop
    ├─ get_menu_choice()      → Returns 5 (Toggle)
    ├─ get_int_input()        → Gets task_id
    └─ toggle_complete()      → Find task, toggle, print status, return bool
        ├─ Search for task by ID
        ├─ Invert complete field
        ├─ Print "complete" or "incomplete" message
        └─ Return True/False
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
| **Toggle Operation** | O(1) – boolean inversion constant time |

---

## Dependencies and Constraints

| Constraint | Details |
|-----------|---------|
| **Python Version** | 3.6+ (uses f-strings and type hints) |
| **External Packages** | None (standard library only) |
| **OS Compatibility** | All platforms (Linux, macOS, Windows) |
| **Character Encoding** | Any (only modifies boolean field) |
| **Input Validation** | None in basic version (caller validates) |
| **Error Handling** | Graceful; no exceptions on invalid ID |

### Required Data Structures

```python
# tasks parameter requirements
tasks = [
    {"id": int, "title": str, "desc": str, "complete": bool},
    # ... more tasks
]

# Each task must have 'complete' field (boolean)
# task_id parameter must be integer
```

---

## Related Functions

This function is part of the complete task management system:

- **`display_menu()`** – Shows menu options (option 5: Mark as Complete/Incomplete)
- **`get_menu_choice()`** – Gets user's menu selection
- **`get_int_input(prompt)`** – Gets task_id from user
- **`print_tasks(tasks)`** – Shows all tasks with completion status
- **`add_task(tasks)`** – Creates new task (complete=False)
- **`update_task(tasks, task_id)`** – Modifies task title/description
- **`delete_task(tasks, task_id)`** – Removes task
- **`toggle_complete(tasks, task_id)`** – Changes completion status (this function)
- **`main()`** – Main event loop that calls `toggle_complete()`

---

## Production Checklist

Before deploying this function:

- [ ] Function is defined in `src/main.py` or `src/core.py`
- [ ] Function accepts `tasks` parameter (list of dicts)
- [ ] Function accepts `task_id` parameter (integer)
- [ ] Function searches list for matching task ID
- [ ] Function toggles the `complete` boolean field
- [ ] Function uses `not` operator to invert boolean
- [ ] Function returns `True` when task found
- [ ] Function returns `False` when task not found
- [ ] Prints "Task marked as complete." when marked complete
- [ ] Prints "Task marked as incomplete." when marked incomplete
- [ ] Error message displays: "Task with ID {task_id} not found."
- [ ] Message reflects NEW status (not previous status)
- [ ] Works with empty list
- [ ] Works with single task
- [ ] Works with multiple tasks
- [ ] Works with non-sequential IDs
- [ ] Works with first, middle, and last tasks in list
- [ ] Multiple toggles work correctly (False → True → False)
- [ ] Other fields preserved after toggle
- [ ] Type hints are present: `(list[dict], int) -> bool`
- [ ] Docstring is complete with examples
- [ ] Tested with all scenarios (incomplete→complete, complete→incomplete, not found)
- [ ] Integrated into menu loop (option 5)

---

## Common Patterns

### Pattern 1: Simple Toggle
```python
task_id = get_int_input("Enter task ID: ")
toggle_complete(tasks, task_id)
```

### Pattern 2: Toggle with Result Check
```python
task_id = get_int_input("Enter task ID: ")
if toggle_complete(tasks, task_id):
    print("Status updated!")
# else: error already printed
```

### Pattern 3: Toggle with Confirmation (Optional)
```python
task_id = get_int_input("Enter task ID: ")

# Find task first
task = next((t for t in tasks if t["id"] == task_id), None)

if task:
    status = "complete" if task["complete"] else "incomplete"
    new_status = "incomplete" if task["complete"] else "complete"

    if confirm(f"Mark as {new_status}? (y/n): "):
        toggle_complete(tasks, task_id)
else:
    print(f"Task {task_id} not found.")
```

### Pattern 4: Toggle Multiple Tasks
```python
def mark_all_complete(tasks):
    """Mark all incomplete tasks as complete"""
    for task in tasks:
        if not task["complete"]:
            toggle_complete(tasks, task["id"])
```

### Pattern 5: Toggle in Menu Loop
```python
choice = get_menu_choice()

if choice == 5:
    task_id = get_int_input("Enter task ID: ")
    toggle_complete(tasks, task_id)
```

---

## Troubleshooting

### Issue: Complete field not changing
**Solution:** Verify `not` operator is being used:
```python
# Correct - inverts boolean
task["complete"] = not task["complete"]

# Incorrect - sets to True always
task["complete"] = True
```

### Issue: Wrong message printing
**Solution:** Check message is based on NEW status:
```python
# Correct - checks after toggle
task["complete"] = not task["complete"]
if task["complete"]:
    print("Task marked as complete.")

# Incorrect - checks before toggle
if task["complete"]:
    print("Task marked as incomplete.")
task["complete"] = not task["complete"]
```

### Issue: Task not being found
**Solution:** Verify ID comparison logic:
```python
# Check for type mismatch
print(f"Searching for: {task_id} (type: {type(task_id)})")
for task in tasks:
    if task["id"] == task_id:
        print("Found!")
```

### Issue: Message not displaying
**Solution:** Verify print statements are being executed:
```python
if task["complete"]:
    print("Task marked as complete.")
else:
    print("Task marked as incomplete.")
```

### Issue: Multiple tasks toggled at once
**Solution:** Ensure search stops after finding first match:
```python
# Correct - returns after finding task
for task in tasks:
    if task["id"] == task_id:
        task["complete"] = not task["complete"]
        print(...)
        return True
```

### Issue: TypeError on boolean operation
**Solution:** Verify task has `complete` field:
```python
# Validate before toggling
if "complete" not in task:
    print(f"Error: Task missing 'complete' field")
else:
    task["complete"] = not task["complete"]
```

---

## Enhancement Options (Optional)

These enhancements are NOT required but can improve functionality:

1. **Show Current Status First**
   - Display task before prompting for confirmation
   - Show current completion status
   - Help user verify they selected correct task

2. **Return Completion Status**
   - Return the new completion status instead of bool
   - Let caller know the new state
   - Allow conditional feedback based on new state

3. **Confirmation Before Toggle**
   - Ask user to confirm the toggle action
   - Use `confirm()` function for safety
   - Allow user to cancel operation

4. **Detailed Status Message**
   - Include task title in status message
   - Show both old and new status
   - Provide more context about the change

5. **Audit Logging**
   - Record when task was toggled
   - Log who toggled the task (if multi-user)
   - Create history of status changes

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-12-28 | Initial skill document; production-ready toggle implementation |

---

