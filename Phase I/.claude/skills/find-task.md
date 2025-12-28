# Skill: Generate Find Task Helper Function

**Owned by:** `core-todo-impl`
**Feature:** Todo App Phase I - Core Task Management
**Status:** Production-Ready

---

## Purpose

Generate the `find_task(tasks: list[dict], task_id: int) -> dict | None` helper function that searches for a task by ID and returns the task dictionary if found, or None if not found. This reusable utility eliminates code duplication across multiple operations (delete, update, toggle, etc.) and provides a single source of truth for task lookup logic.

---

## When to Use

- **Delete Operations:** Find task before deletion (safety check)
- **Update Operations:** Verify task exists before prompting for updates
- **Toggle Operations:** Check task exists before toggling status
- **Display Operations:** Show task details before performing operations
- **Code Reuse:** Avoid duplicate search logic across functions
- **Safety Checks:** Verify task exists before modification

---

## Inputs

**Function Signature:**
```python
def find_task(tasks: list[dict], task_id: int) -> dict | None:
```

**Parameter Details:**

- **`tasks`** (list[dict]): The in-memory list of tasks
  - May be empty
  - Each element is a dict with keys: id, title, desc, complete
  - Function does not modify the list
  - Type hint: `list[dict]`

- **`task_id`** (int): The ID of the task to find
  - Matched against task's "id" field
  - Type hint: `int`

**Return Value:**
- **`dict`** – The matching task dictionary if found
- **`None`** – If no task with that ID exists

---

## Step-by-Step Process

1. **Search Task List:**
   - Iterate through tasks list
   - Compare each task's "id" field with provided task_id
   - Continue until match found or list exhausted

2. **Task Found:**
   - Return the matching task dictionary immediately
   - No filtering or copying; return exact dict from list

3. **Task Not Found:**
   - Return None (sentinel value indicating not found)
   - No error messages printed (caller decides what to do)
   - Silent failure; caller handles feedback

---

## Output

**Function Name:** `find_task(tasks: list[dict], task_id: int) -> dict | None`

**Return Value:** Task dict or None

**Example Return Flow 1 (Task Found):**
```python
task = find_task(tasks, 1)
# Returns: {"id": 1, "title": "Buy groceries", "desc": "Milk, eggs, bread", "complete": False}
# or returns the actual dict from the list
```

**Example Return Flow 2 (Task Not Found):**
```python
task = find_task(tasks, 99)
# Returns: None
```

---

## Implementation

### Python Code (Production-Ready) - Using next() with Generator

```python
def find_task(tasks: list[dict], task_id: int) -> dict | None:
    """
    Find a task in the list by ID.

    Searches for a task with matching ID. Returns the task dictionary if
    found, or None if not found. Uses generator expression for efficient
    single-pass search with early exit capability.

    Args:
        tasks (list[dict]): The in-memory task list. Not modified.
        task_id (int): The ID to search for. Matched against task["id"].

    Returns:
        dict | None: The matching task dictionary if found, None otherwise.

    Example - Task found:
        >>> tasks = [
        ...     {"id": 1, "title": "Buy groceries", "desc": "Milk", "complete": False},
        ...     {"id": 2, "title": "Finish project", "desc": "By Friday", "complete": False}
        ... ]
        >>> task = find_task(tasks, 1)
        >>> print(task)
        {'id': 1, 'title': 'Buy groceries', 'desc': 'Milk', 'complete': False}

    Example - Task not found:
        >>> task = find_task(tasks, 99)
        >>> print(task)
        None

    Example - Using the result:
        >>> if task := find_task(tasks, 1):
        ...     print(f"Found: {task['title']}")
        ... else:
        ...     print("Task not found")
        Found: Buy groceries
    """
    return next((task for task in tasks if task["id"] == task_id), None)
```

### Alternative Implementation - Using Loop with Break

```python
def find_task(tasks: list[dict], task_id: int) -> dict | None:
    """
    Find a task in the list by ID (using loop).

    This implementation uses an explicit for loop with break for clarity
    and explicit control flow.
    """
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None
```

### Design Notes

**Primary Implementation (Using next()):**
- **Concise and Pythonic:** One-liner using generator expression
- **Efficient:** Early exit on match (generator stops iterating)
- **Readable:** Intent is clear to Python developers
- **Single Pass:** Only iterates until match found
- **Functional Style:** Matches functional programming patterns

**Why next() is Recommended:**
- More efficient than filtering entire list
- Generator stops at first match (early exit)
- Idiomatic Python for single-item search
- Cleaner than loop with break
- Handles empty case naturally (returns None)

**Alternative Approach (Loop):**
- More explicit; easier for beginners
- Equivalent performance
- More verbose (3 lines vs 1)
- Equally valid; choose based on team preference

---

## Implementation Comparison

| Approach | Pros | Cons | Recommendation |
|----------|------|------|-----------------|
| **next() + generator** | Concise, efficient, Pythonic, early exit | Requires generator understanding | ✓ Primary |
| **for loop + break** | Explicit, clear, easy to understand | More verbose (3 lines) | Alternative |
| **List comprehension + [0]** | Direct indexing | Slower, creates entire list, crashes if empty | ✗ Avoid |
| **filter() + next()** | Functional style | More verbose than generator | Not recommended |

---

## Code Reuse Examples

### Example 1: Used in delete_task()

**Before (with duplicate search):**
```python
def delete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return True
    print(f"Task with ID {task_id} not found.")
    return False
```

**After (using find_task):**
```python
def delete_task(tasks, task_id):
    task = find_task(tasks, task_id)
    if task:
        tasks.remove(task)
        return True
    print(f"Task with ID {task_id} not found.")
    return False
```

### Example 2: Used in update_task()

**Before (with duplicate search):**
```python
def update_task(tasks, task_id):
    task = None
    for t in tasks:
        if t["id"] == task_id:
            task = t
            break
    if task is None:
        print(f"Task with ID {task_id} not found.")
        return False
    # ... rest of function
```

**After (using find_task):**
```python
def update_task(tasks, task_id):
    task = find_task(tasks, task_id)
    if task is None:
        print(f"Task with ID {task_id} not found.")
        return False
    # ... rest of function
```

### Example 3: Used in toggle_complete()

**Before (with duplicate search):**
```python
def toggle_complete(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["complete"] = not task["complete"]
            if task["complete"]:
                print("Task marked as complete.")
            else:
                print("Task marked as incomplete.")
            return True
    print(f"Task with ID {task_id} not found.")
    return False
```

**After (using find_task):**
```python
def toggle_complete(tasks, task_id):
    task = find_task(tasks, task_id)
    if task is None:
        print(f"Task with ID {task_id} not found.")
        return False

    task["complete"] = not task["complete"]
    if task["complete"]:
        print("Task marked as complete.")
    else:
        print("Task marked as incomplete.")
    return True
```

---

## Failure Handling

| Scenario | Behavior | Returns |
|----------|----------|---------|
| **Task found** | Return matching task dict | `dict` (the task) |
| **Task not found** | Return None sentinel | `None` |
| **Empty list** | Return None (not found) | `None` |
| **Negative ID** | Return None (not found) | `None` |
| **ID zero** | Return None (not found) | `None` |
| **Very large ID** | Return None (not found) | `None` |
| **Duplicate IDs** | Return first matching task | `dict` (first match) |
| **tasks is None** | Raises TypeError on iteration | Exception |
| **task_id is not int** | May cause comparison issues | Silent failure or None |
| **Missing "id" key** | Raises KeyError on comparison | Exception |

**Note on Return Values:**
- Function returns the ACTUAL dict from the list (not a copy)
- Modifications to returned dict modify the original list
- This is intentional for operations that need to modify tasks

### Enhanced Version with Error Handling (Optional)

```python
def find_task(tasks: list[dict], task_id: int) -> dict | None:
    """Find task with input validation"""
    if not isinstance(tasks, list):
        raise TypeError("tasks must be a list")
    if not isinstance(task_id, int):
        raise TypeError("task_id must be an integer")

    return next((task for task in tasks if task.get("id") == task_id), None)
```

---

## Acceptance Criteria

- ✓ Function accepts tasks list parameter
- ✓ Function accepts task_id integer parameter
- ✓ Function returns task dict if found
- ✓ Function returns None if not found
- ✓ Does not print any messages (silent function)
- ✓ Does not modify the task list
- ✓ Works with empty list (returns None)
- ✓ Works with single task
- ✓ Works with multiple tasks
- ✓ Works with non-sequential IDs
- ✓ Returns first match if duplicate IDs exist
- ✓ Uses efficient search (next() or loop with break)
- ✓ Type hints are correct: `(list[dict], int) -> dict | None`
- ✓ Docstring is complete with examples
- ✓ Can be imported and reused across functions

---

## Testing Checklist

```python
# Test 1: Function exists and is callable
assert callable(find_task)

# Test 2: Find single task in list
tasks = [{"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False}]
result = find_task(tasks, 1)
assert result is not None
assert result["id"] == 1
assert isinstance(result, dict)

# Test 3: Task not found in single-task list
tasks = [{"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False}]
result = find_task(tasks, 99)
assert result is None

# Test 4: Find task in multi-task list (first task)
tasks = [
    {"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False},
    {"id": 2, "title": "Task 2", "desc": "Desc 2", "complete": False},
    {"id": 3, "title": "Task 3", "desc": "Desc 3", "complete": False}
]
result = find_task(tasks, 1)
assert result is not None
assert result["id"] == 1
assert result["title"] == "Task 1"

# Test 5: Find task in multi-task list (middle task)
result = find_task(tasks, 2)
assert result is not None
assert result["id"] == 2
assert result["title"] == "Task 2"

# Test 6: Find task in multi-task list (last task)
result = find_task(tasks, 3)
assert result is not None
assert result["id"] == 3
assert result["title"] == "Task 3"

# Test 7: Task not found in multi-task list
result = find_task(tasks, 99)
assert result is None

# Test 8: Empty list
tasks = []
result = find_task(tasks, 1)
assert result is None

# Test 9: Negative task ID not found
tasks = [{"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False}]
result = find_task(tasks, -5)
assert result is None

# Test 10: Task ID zero not found
result = find_task(tasks, 0)
assert result is None

# Test 11: Very large task ID not found
result = find_task(tasks, 999999)
assert result is None

# Test 12: Find task with non-sequential IDs
tasks = [
    {"id": 5, "title": "Task 5", "desc": "Desc 5", "complete": False},
    {"id": 10, "title": "Task 10", "desc": "Desc 10", "complete": False},
    {"id": 3, "title": "Task 3", "desc": "Desc 3", "complete": False}
]
result = find_task(tasks, 10)
assert result is not None
assert result["id"] == 10

# Test 13: Returned task is reference to original (not copy)
tasks = [{"id": 1, "title": "Original", "desc": "Desc", "complete": False}]
result = find_task(tasks, 1)
result["title"] = "Modified"
assert tasks[0]["title"] == "Modified"  # Original list modified

# Test 14: Modifying returned dict modifies original list
tasks = [{"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False}]
task = find_task(tasks, 1)
task["complete"] = True
assert tasks[0]["complete"] is True

# Test 15: Find completed task
tasks = [{"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": True}]
result = find_task(tasks, 1)
assert result is not None
assert result["complete"] is True

# Test 16: Find incomplete task
tasks = [{"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False}]
result = find_task(tasks, 1)
assert result is not None
assert result["complete"] is False

# Test 17: Find task with special characters
tasks = [{"id": 1, "title": "Task @#$%", "desc": "Symbols!", "complete": False}]
result = find_task(tasks, 1)
assert result is not None
assert result["title"] == "Task @#$%"

# Test 18: Find task with unicode characters
tasks = [{"id": 1, "title": "Task 🛒", "desc": "Buy 🥛", "complete": False}]
result = find_task(tasks, 1)
assert result is not None
assert result["title"] == "Task 🛒"

# Test 19: Find first task if duplicate IDs exist
tasks = [
    {"id": 1, "title": "Task 1a", "desc": "Desc 1a", "complete": False},
    {"id": 1, "title": "Task 1b", "desc": "Desc 1b", "complete": False},
    {"id": 2, "title": "Task 2", "desc": "Desc 2", "complete": False}
]
result = find_task(tasks, 1)
assert result["title"] == "Task 1a"  # First match

# Test 20: All task fields accessible
tasks = [
    {
        "id": 42,
        "title": "Complex Task",
        "desc": "Complex Description",
        "complete": True
    }
]
result = find_task(tasks, 42)
assert result["id"] == 42
assert result["title"] == "Complex Task"
assert result["desc"] == "Complex Description"
assert result["complete"] is True
```

---

## Usage Examples

### Example 1: Simple Find
```python
tasks = [
    {"id": 1, "title": "Buy groceries", "desc": "Milk, eggs, bread", "complete": False},
    {"id": 2, "title": "Finish project", "desc": "Submit by Friday", "complete": False}
]

task = find_task(tasks, 1)
if task:
    print(f"Found: {task['title']}")
else:
    print("Not found")
```

**Output:**
```
Found: Buy groceries
```

### Example 2: Using Walrus Operator (Python 3.8+)
```python
tasks = [...]

if task := find_task(tasks, 1):
    print(f"Found: {task['title']}")
else:
    print("Not found")
```

### Example 3: Display Task Before Operating
```python
task_id = 1
task = find_task(tasks, task_id)

if task:
    print(f"Task: {task['id']}. {task['title']} - {task['desc']}")
    print(f"Status: {'Complete' if task['complete'] else 'Incomplete'}")
else:
    print(f"Task {task_id} not found")
```

**Output:**
```
Task: 1. Buy groceries - Milk, eggs, bread
Status: Incomplete
```

### Example 4: Modify Found Task
```python
task = find_task(tasks, 1)
if task:
    task["title"] = "Buy vegetables"  # Modifies original list
    task["complete"] = True
```

**Result:**
```python
# Original tasks list modified
tasks[0] = {
    "id": 1,
    "title": "Buy vegetables",  # Updated
    "desc": "Milk, eggs, bread",
    "complete": True  # Updated
}
```

### Example 5: Used in delete_task() Function
```python
def delete_task(tasks, task_id):
    """Delete task using find_task helper"""
    task = find_task(tasks, task_id)

    if task is None:
        print(f"Task with ID {task_id} not found.")
        return False

    tasks.remove(task)
    return True
```

### Example 6: Used in update_task() Function
```python
def update_task(tasks, task_id):
    """Update task using find_task helper"""
    task = find_task(tasks, task_id)

    if task is None:
        print(f"Task with ID {task_id} not found.")
        return False

    # Display current values
    print(f"Current title: {task['title']}")
    print(f"Current description: {task['desc']}")

    # Get new values
    new_title = input("Enter new title (press Enter to keep): ").strip()
    new_desc = input("Enter new description (press Enter to keep): ").strip()

    # Update
    if new_title:
        task["title"] = new_title
    if new_desc:
        task["desc"] = new_desc

    if new_title or new_desc:
        print("Task updated.")

    return True
```

### Example 7: Used in toggle_complete() Function
```python
def toggle_complete(tasks, task_id):
    """Toggle task completion using find_task helper"""
    task = find_task(tasks, task_id)

    if task is None:
        print(f"Task with ID {task_id} not found.")
        return False

    task["complete"] = not task["complete"]

    if task["complete"]:
        print("Task marked as complete.")
    else:
        print("Task marked as incomplete.")

    return True
```

### Example 8: Safe Preview Before Deletion
```python
def delete_task_with_confirmation(tasks, task_id):
    """Delete with safety confirmation"""
    task = find_task(tasks, task_id)

    if task is None:
        print(f"Task with ID {task_id} not found.")
        return False

    # Show what will be deleted
    print(f"Task: {task['id']}. {task['title']} - {task['desc']}")

    # Get confirmation
    if confirm("Delete this task? (y/n): "):
        tasks.remove(task)
        print("Task deleted successfully!")
        return True
    else:
        print("Task not deleted.")
        return False
```

---

## Integration with Other Functions

This helper function reduces code duplication across the entire system:

```
find_task()  ← Reusable search function
    ↓
Used by:
├─ delete_task()      - Find before removing
├─ update_task()      - Find before updating fields
├─ toggle_complete()  - Find before toggling status
├─ print_single_task()  - Find and display specific task
└─ any other operation needing task lookup
```

**Before find_task():**
```
delete_task (10 lines)  ─┐
update_task (15 lines)  ─┼─ Each with duplicate search logic
toggle_complete (12 lines) ─┘
Total: 37 lines, repeated search code
```

**After find_task():**
```
find_task (1 line)       ┐
delete_task (6 lines)    ├─ Cleaner, DRY code
update_task (12 lines)   │
toggle_complete (8 lines)┘
Total: 27 lines, search logic in one place
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
| **Early Exit** | Yes (next() stops at first match) |

---

## Dependencies and Constraints

| Constraint | Details |
|-----------|---------|
| **Python Version** | 3.6+ (uses type hints); 3.10+ for `dict \| None` syntax |
| **Backward Compatibility** | Use `Optional[dict]` for Python 3.9 and earlier |
| **External Packages** | None (standard library only) |
| **OS Compatibility** | All platforms (Linux, macOS, Windows) |
| **Character Encoding** | UTF-8 (supports unicode in task data) |
| **Input Validation** | None in basic version (caller validates) |
| **Error Handling** | Propagates structural errors to caller |

### Type Hint Compatibility

**Python 3.10+ (Preferred):**
```python
def find_task(tasks: list[dict], task_id: int) -> dict | None:
```

**Python 3.9 and Earlier:**
```python
from typing import Optional

def find_task(tasks: list[dict], task_id: int) -> Optional[dict]:
```

---

## Related Functions

This helper function supports the entire task management system:

- **`find_task(tasks, task_id)`** – Find task by ID (this function)
- **`delete_task(tasks, task_id)`** – Uses `find_task()` for safe deletion
- **`update_task(tasks, task_id)`** – Uses `find_task()` for safe updates
- **`toggle_complete(tasks, task_id)`** – Uses `find_task()` for status toggle
- **`add_task(tasks)`** – Does not use (adds new task)
- **`print_tasks(tasks)`** – Does not use (displays all tasks)
- **`print_single_task(task)`** – Could use to find and display

---

## Production Checklist

Before deploying this function:

- [ ] Function is defined in `src/core.py` or `src/main.py`
- [ ] Function accepts `tasks` parameter (list of dicts)
- [ ] Function accepts `task_id` parameter (integer)
- [ ] Function returns dict when task found
- [ ] Function returns None when task not found
- [ ] Uses efficient search (next() or loop with break)
- [ ] Does not print any messages (silent function)
- [ ] Does not modify the task list
- [ ] Works with empty list
- [ ] Works with single task
- [ ] Works with multiple tasks
- [ ] Works with non-sequential IDs
- [ ] Returns reference to original dict (not copy)
- [ ] Type hints are present and correct
- [ ] Docstring is complete with examples
- [ ] Tested with all scenarios
- [ ] Imported and used in delete_task()
- [ ] Imported and used in update_task()
- [ ] Imported and used in toggle_complete()
- [ ] Reduces code duplication across operations

---

## Common Patterns

### Pattern 1: Simple Find
```python
task = find_task(tasks, task_id)
if task:
    # Use task
```

### Pattern 2: Walrus Operator (Python 3.8+)
```python
if task := find_task(tasks, task_id):
    # Use task
else:
    print("Not found")
```

### Pattern 3: Find and Modify
```python
task = find_task(tasks, task_id)
if task:
    task["title"] = "New title"
    task["complete"] = True
```

### Pattern 4: Find and Display
```python
task = find_task(tasks, task_id)
if task:
    print(f"{task['id']}. {task['title']} - {task['desc']}")
else:
    print(f"Task {task_id} not found")
```

### Pattern 5: Find and Remove
```python
task = find_task(tasks, task_id)
if task:
    tasks.remove(task)
```

---

## Troubleshooting

### Issue: Returns None even when task exists
**Solution:** Verify ID types match:
```python
# Debug: check types
print(f"Searching for {task_id} (type: {type(task_id)})")
for task in tasks:
    print(f"Checking {task['id']} (type: {type(task['id'])})")
```

### Issue: Function not found (NameError)
**Solution:** Ensure function is imported or defined first:
```python
# Define find_task first
def find_task(tasks, task_id):
    return next((t for t in tasks if t["id"] == task_id), None)

# Then use it in other functions
def delete_task(tasks, task_id):
    task = find_task(tasks, task_id)
```

### Issue: Modification not affecting original list
**Solution:** Ensure you're modifying the returned reference:
```python
# Correct - modifies original
task = find_task(tasks, 1)
task["title"] = "New"  # Modifies tasks[0]

# Incorrect - creates new dict
new_task = {**find_task(tasks, 1), "title": "New"}  # Doesn't affect tasks
```

### Issue: TypeError on comparison
**Solution:** Verify task_id is an integer:
```python
# Correct
task_id = 5
find_task(tasks, task_id)

# Incorrect
task_id = "5"
find_task(tasks, task_id)  # Might cause issues
```

---

## Enhancement Options (Optional)

These enhancements are NOT required but can improve functionality:

1. **Return Index Instead**
   - Return task index instead of dict
   - Useful for index-based operations
   - Simpler for removal: `del tasks[index]`

2. **Return Tuple (Task, Index)**
   - Return both task and its index
   - Provides both dict access and index-based operations
   - Example: `(task_dict, 2)`

3. **Case-Insensitive Search**
   - Add parameter: `find_task(tasks, title, case_sensitive=True)`
   - Search by title instead of ID
   - Useful for duplicate detection

4. **Partial Match Search**
   - Search by title prefix or substring
   - Fuzzy matching for user convenience
   - Returns first partial match

5. **Filter by Criteria**
   - Add parameter for custom filter function
   - Example: `find_task(tasks, task_id, filter_func=lambda t: t["complete"] is False)`
   - More flexible search capability

---

## Code Reduction Impact

### Using find_task() in delete_task()

**Before:**
```python
def delete_task(tasks, task_id):
    for task in tasks:  # ← Duplicate search
        if task["id"] == task_id:
            tasks.remove(task)
            return True
    print(f"Task with ID {task_id} not found.")
    return False
# 7 lines
```

**After:**
```python
def delete_task(tasks, task_id):
    task = find_task(tasks, task_id)
    if not task:
        print(f"Task with ID {task_id} not found.")
        return False
    tasks.remove(task)
    return True
# 6 lines, cleaner separation
```

**Savings:** 1 line, clearer intent, code reuse

### Using find_task() in update_task()

**Before:**
```python
def update_task(tasks, task_id):
    task = None
    for t in tasks:  # ← Duplicate search
        if t["id"] == task_id:
            task = t
            break
    if task is None:
        print(f"Task with ID {task_id} not found.")
        return False
    # ... rest
# 9 lines just for search
```

**After:**
```python
def update_task(tasks, task_id):
    task = find_task(tasks, task_id)
    if task is None:
        print(f"Task with ID {task_id} not found.")
        return False
    # ... rest
# 5 lines, much cleaner
```

**Savings:** 4 lines, improved readability

### Using find_task() in toggle_complete()

**Before:**
```python
def toggle_complete(tasks, task_id):
    for task in tasks:  # ← Duplicate search
        if task["id"] == task_id:
            # ... toggle logic
            return True
    print(f"Task with ID {task_id} not found.")
    return False
# 8 lines with search embedded
```

**After:**
```python
def toggle_complete(tasks, task_id):
    task = find_task(tasks, task_id)
    if task is None:
        print(f"Task with ID {task_id} not found.")
        return False
    # ... toggle logic
    return True
# 6 lines, search separated
```

**Savings:** 2 lines, cleaner logic separation

### Total Code Reduction

- delete_task: 7 lines → 6 lines (1 saved)
- update_task: 12 lines → 8 lines (4 saved)
- toggle_complete: 8 lines → 6 lines (2 saved)
- find_task: 1 line (new)

**Total:** 27 lines → 21 lines + 1 line (find_task) = 22 lines
**Savings:** 5 lines of code, single source of truth for search logic

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-12-28 | Initial skill document; reusable helper function for task lookup |

---

