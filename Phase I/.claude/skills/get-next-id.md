# Skill: Generate Get Next ID Helper Function

**Owned by:** `core-todo-impl`
**Feature:** Todo App Phase I - Core Task Management
**Status:** Production-Ready

---

## Purpose

Generate the `get_next_id(tasks: list[dict]) -> int` helper function that safely calculates the next available task ID. This function returns the maximum existing ID plus one, or 1 if the list is empty. This eliminates hardcoded ID logic and handles edge cases robustly, even if tasks have missing or non-sequential IDs.

---

## When to Use

- **Add Task Operation:** Generate ID when creating new task
- **Bulk Import:** Generate IDs for imported tasks
- **Task Recovery:** Generate IDs when rebuilding list
- **ID Collision Avoidance:** Guarantee unique sequential IDs
- **Centralized ID Logic:** Single source of truth for ID generation

---

## Inputs

**Function Signature:**
```python
def get_next_id(tasks: list[dict]) -> int:
```

**Parameter Details:**

- **`tasks`** (list[dict]): The in-memory list of tasks
  - May be empty
  - Each element is a dict with "id" field (integer)
  - Function does not modify the list
  - Type hint: `list[dict]`

**Return Value:** `int`
- Next available ID (guaranteed unique)
- Always >= 1
- Always > max existing ID

---

## Step-by-Step Process

1. **Check if List is Empty:**
   - If tasks list is empty, return 1 (first task ID)
   - Skip remaining steps

2. **Find Maximum ID:**
   - Iterate through all tasks
   - Extract each task's "id" field
   - Track the maximum value encountered

3. **Calculate Next ID:**
   - Add 1 to the maximum ID
   - Result is guaranteed to be unique
   - Return the result

---

## Output

**Function Name:** `get_next_id(tasks: list[dict]) -> int`

**Return Value:** Integer ID for next task

**Example Output Flow 1 (Empty List):**
```python
tasks = []
next_id = get_next_id(tasks)
# Returns: 1
```

**Example Output Flow 2 (One Task):**
```python
tasks = [
    {"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False}
]
next_id = get_next_id(tasks)
# Returns: 2
```

**Example Output Flow 3 (Multiple Tasks):**
```python
tasks = [
    {"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False},
    {"id": 2, "title": "Task 2", "desc": "Desc 2", "complete": False},
    {"id": 3, "title": "Task 3", "desc": "Desc 3", "complete": False}
]
next_id = get_next_id(tasks)
# Returns: 4
```

**Example Output Flow 4 (Non-Sequential IDs):**
```python
tasks = [
    {"id": 5, "title": "Task 5", "desc": "Desc 5", "complete": False},
    {"id": 10, "title": "Task 10", "desc": "Desc 10", "complete": False},
    {"id": 3, "title": "Task 3", "desc": "Desc 3", "complete": False}
]
next_id = get_next_id(tasks)
# Returns: 11 (max(5, 10, 3) + 1)
```

---

## Implementation

### Python Code (Production-Ready) - Using max() with default

```python
def get_next_id(tasks: list[dict]) -> int:
    """
    Calculate the next available task ID.

    Returns the maximum ID in the list plus one, ensuring sequential and
    unique IDs. If the list is empty, returns 1. Safely handles edge cases
    including empty lists, non-sequential IDs, and gaps in ID numbering.

    Args:
        tasks (list[dict]): The in-memory task list. Not modified.
                           Each task should have an "id" field (integer).

    Returns:
        int: The next available ID (always >= 1).

    Example - Empty list:
        >>> tasks = []
        >>> get_next_id(tasks)
        1

    Example - Single task:
        >>> tasks = [{"id": 1, "title": "Task 1", "desc": "Desc", "complete": False}]
        >>> get_next_id(tasks)
        2

    Example - Multiple tasks:
        >>> tasks = [
        ...     {"id": 1, "title": "Task 1", "desc": "Desc", "complete": False},
        ...     {"id": 2, "title": "Task 2", "desc": "Desc", "complete": False},
        ...     {"id": 3, "title": "Task 3", "desc": "Desc", "complete": False}
        ... ]
        >>> get_next_id(tasks)
        4

    Example - Non-sequential IDs:
        >>> tasks = [
        ...     {"id": 5, "title": "Task 5", "desc": "Desc", "complete": False},
        ...     {"id": 10, "title": "Task 10", "desc": "Desc", "complete": False}
        ... ]
        >>> get_next_id(tasks)
        11
    """
    return max((task["id"] for task in tasks), default=0) + 1
```

### Alternative Implementation - Using Loop

```python
def get_next_id(tasks: list[dict]) -> int:
    """
    Calculate the next available task ID (using loop).

    This implementation uses an explicit loop for clarity.
    """
    if not tasks:
        return 1

    max_id = 0
    for task in tasks:
        if task["id"] > max_id:
            max_id = task["id"]

    return max_id + 1
```

### Alternative Implementation - Using sorted()

```python
def get_next_id(tasks: list[dict]) -> int:
    """
    Calculate the next available task ID (using sorted).

    This implementation sorts tasks by ID and returns last ID + 1.
    """
    if not tasks:
        return 1

    ids = sorted([task["id"] for task in tasks])
    return ids[-1] + 1
```

### Design Notes

**Primary Implementation (Using max()):**
- **Concise and Pythonic:** One-liner with generator expression
- **Efficient:** Single pass through list, O(n) time
- **Safe:** Uses `default=0` to handle empty list
- **Clear Intent:** Obviously finding maximum and adding 1
- **No Intermediate Lists:** Generator avoids creating list copy
- **Functional Style:** Pure function, no side effects

**Why max() is Recommended:**
- Most idiomatic Python for finding maximum
- Efficient (single pass, early termination impossible but unnecessary)
- Safe default parameter handles empty case
- Readable to Python developers
- Performant for typical task list sizes

**Alternative Approaches:**
1. **Loop** – More explicit; easier for beginners
2. **sorted()** – Less efficient; O(n log n); requires list creation
3. **Manual max tracking** – Similar to loop; more verbose

---

## Implementation Comparison

| Approach | Pros | Cons | Recommendation |
|----------|------|------|-----------------|
| **max() + generator** | Concise, Pythonic, efficient, pure | Requires generator understanding | ✓ Primary |
| **for loop + tracking** | Explicit, clear, easy to understand | Verbose (5 lines) | Alternative |
| **sorted() + index** | Direct access to last element | Inefficient O(n log n), creates list | ✗ Avoid |
| **list comprehension + max** | Clear intent | Creates intermediate list | Not recommended |

---

## Integration with add_task()

**Before (Hardcoded ID Logic):**
```python
def add_task(tasks):
    """Add task with hardcoded ID generation"""
    title = input("Enter task title: ").strip()
    desc = input("Enter task description: ").strip()

    # ID logic embedded in function
    task_id = len(tasks) + 1  # ← Assumes sequential IDs
    task = {
        "id": task_id,
        "title": title,
        "desc": desc,
        "complete": False
    }
    tasks.append(task)
    print(f"Task added successfully (ID: {task_id}).")
```

**After (Using get_next_id):**
```python
def add_task(tasks):
    """Add task using get_next_id helper"""
    title = input("Enter task title: ").strip()
    desc = input("Enter task description: ").strip()

    # ID generation delegated to helper
    task_id = get_next_id(tasks)
    task = {
        "id": task_id,
        "title": title,
        "desc": desc,
        "complete": False
    }
    tasks.append(task)
    print(f"Task added successfully (ID: {task_id}).")
```

**Benefits:**
- Cleaner add_task() function (one less line)
- Reusable ID logic (used in add_task, bulk import, etc.)
- Safe handling of non-sequential IDs
- Single source of truth for ID generation

---

## Failure Handling

| Scenario | Behavior | Returns |
|----------|----------|---------|
| **Empty list** | Return 1 (first ID) | `1` |
| **Single task** | Return 2 (max + 1) | `2` |
| **Multiple tasks** | Return max ID + 1 | `int` |
| **Non-sequential IDs** | Return max + 1 (not count) | `int` |
| **Gaps in IDs** | Return max + 1 (ignores gaps) | `int` |
| **ID = 1 only** | Return 2 | `2` |
| **Large IDs** | Return largest + 1 | `int` |
| **Negative IDs** | Return max + 1 (works anyway) | `int` |
| **ID = 0** | Return max + 1 (unusual but safe) | `int` |
| **tasks is None** | Raises TypeError on iteration | Exception |
| **task["id"] missing** | Raises KeyError | Exception |
| **task["id"] not int** | Comparison works if comparable | Safe or Exception |

**Note on Edge Cases:**
The implementation is robust:
- Empty list handled by `default=0`
- Non-sequential IDs handled by `max()` (not `len()`)
- Gaps in numbering don't cause issues
- Works even if IDs are unusual (0, negative, large)

### Enhanced Version with Error Handling (Optional)

```python
def get_next_id(tasks: list[dict]) -> int:
    """Get next ID with error handling and validation"""
    if not isinstance(tasks, list):
        raise TypeError("tasks must be a list")

    if not tasks:
        return 1

    try:
        max_id = max(task["id"] for task in tasks)
        return max_id + 1
    except KeyError:
        raise KeyError("Task dict missing 'id' field")
    except TypeError:
        raise TypeError("task['id'] must be an integer")
```

---

## Acceptance Criteria

- ✓ Function accepts tasks list parameter
- ✓ Function returns integer
- ✓ Returns 1 if list is empty
- ✓ Returns max(id) + 1 for non-empty list
- ✓ Works with single task
- ✓ Works with multiple tasks
- ✓ Handles non-sequential IDs correctly
- ✓ Handles gaps in ID numbering
- ✓ Returns next unique ID (never duplicates existing)
- ✓ Does not modify the task list
- ✓ Does not print any messages
- ✓ Works even if IDs are unusual (0, negative, large)
- ✓ Type hints are correct: `(list[dict]) -> int`
- ✓ Docstring is complete with examples
- ✓ Can be imported and reused in add_task()

---

## Testing Checklist

```python
# Test 1: Function exists and is callable
assert callable(get_next_id)

# Test 2: Empty list returns 1
tasks = []
result = get_next_id(tasks)
assert result == 1
assert isinstance(result, int)

# Test 3: Single task
tasks = [{"id": 1, "title": "Task 1", "desc": "Desc", "complete": False}]
result = get_next_id(tasks)
assert result == 2

# Test 4: Two tasks
tasks = [
    {"id": 1, "title": "Task 1", "desc": "Desc", "complete": False},
    {"id": 2, "title": "Task 2", "desc": "Desc", "complete": False}
]
result = get_next_id(tasks)
assert result == 3

# Test 5: Multiple tasks
tasks = [
    {"id": 1, "title": "Task 1", "desc": "Desc", "complete": False},
    {"id": 2, "title": "Task 2", "desc": "Desc", "complete": False},
    {"id": 3, "title": "Task 3", "desc": "Desc", "complete": False},
    {"id": 4, "title": "Task 4", "desc": "Desc", "complete": False},
    {"id": 5, "title": "Task 5", "desc": "Desc", "complete": False}
]
result = get_next_id(tasks)
assert result == 6

# Test 6: Non-sequential IDs (5, 10, 3)
tasks = [
    {"id": 5, "title": "Task 5", "desc": "Desc", "complete": False},
    {"id": 10, "title": "Task 10", "desc": "Desc", "complete": False},
    {"id": 3, "title": "Task 3", "desc": "Desc", "complete": False}
]
result = get_next_id(tasks)
assert result == 11  # max(5, 10, 3) + 1

# Test 7: Gaps in numbering (1, 3, 5)
tasks = [
    {"id": 1, "title": "Task 1", "desc": "Desc", "complete": False},
    {"id": 3, "title": "Task 3", "desc": "Desc", "complete": False},
    {"id": 5, "title": "Task 5", "desc": "Desc", "complete": False}
]
result = get_next_id(tasks)
assert result == 6  # max(1, 3, 5) + 1

# Test 8: Out of order (10, 1, 5, 3)
tasks = [
    {"id": 10, "title": "Task 10", "desc": "Desc", "complete": False},
    {"id": 1, "title": "Task 1", "desc": "Desc", "complete": False},
    {"id": 5, "title": "Task 5", "desc": "Desc", "complete": False},
    {"id": 3, "title": "Task 3", "desc": "Desc", "complete": False}
]
result = get_next_id(tasks)
assert result == 11  # max(10, 1, 5, 3) + 1

# Test 9: Single task with ID 1
tasks = [{"id": 1, "title": "Task 1", "desc": "Desc", "complete": False}]
result = get_next_id(tasks)
assert result == 2

# Test 10: Single task with large ID
tasks = [{"id": 999, "title": "Task 999", "desc": "Desc", "complete": False}]
result = get_next_id(tasks)
assert result == 1000

# Test 11: Tasks with ID 0 (edge case)
tasks = [
    {"id": 0, "title": "Task 0", "desc": "Desc", "complete": False},
    {"id": 1, "title": "Task 1", "desc": "Desc", "complete": False}
]
result = get_next_id(tasks)
assert result == 2

# Test 12: Negative IDs (unusual but safe)
tasks = [
    {"id": -5, "title": "Task -5", "desc": "Desc", "complete": False},
    {"id": 3, "title": "Task 3", "desc": "Desc", "complete": False}
]
result = get_next_id(tasks)
assert result == 4  # max(-5, 3) + 1

# Test 13: All tasks with same ID (data integrity issue, but safe)
tasks = [
    {"id": 5, "title": "Task A", "desc": "Desc A", "complete": False},
    {"id": 5, "title": "Task B", "desc": "Desc B", "complete": False},
    {"id": 5, "title": "Task C", "desc": "Desc C", "complete": False}
]
result = get_next_id(tasks)
assert result == 6

# Test 14: List not modified
tasks = [
    {"id": 1, "title": "Task 1", "desc": "Desc", "complete": False}
]
original_tasks = [task.copy() for task in tasks]
get_next_id(tasks)
assert tasks == original_tasks  # Unchanged

# Test 15: Multiple calls return sequential IDs
tasks = []
id1 = get_next_id(tasks)
assert id1 == 1
tasks.append({"id": id1, "title": "Task 1", "desc": "Desc", "complete": False})

id2 = get_next_id(tasks)
assert id2 == 2
tasks.append({"id": id2, "title": "Task 2", "desc": "Desc", "complete": False})

id3 = get_next_id(tasks)
assert id3 == 3

# Test 16: Very large list
tasks = [
    {"id": i, "title": f"Task {i}", "desc": "Desc", "complete": False}
    for i in range(1, 1001)
]
result = get_next_id(tasks)
assert result == 1001

# Test 17: Mixed complete/incomplete tasks
tasks = [
    {"id": 1, "title": "Task 1", "desc": "Desc", "complete": False},
    {"id": 2, "title": "Task 2", "desc": "Desc", "complete": True},
    {"id": 3, "title": "Task 3", "desc": "Desc", "complete": False}
]
result = get_next_id(tasks)
assert result == 4

# Test 18: Tasks with special characters
tasks = [
    {"id": 1, "title": "Task @#$%", "desc": "Desc!", "complete": False},
    {"id": 2, "title": "Task 🛒", "desc": "Desc 🥛", "complete": False}
]
result = get_next_id(tasks)
assert result == 3

# Test 19: Returns same type as input IDs (integer)
tasks = [{"id": 5, "title": "Task 5", "desc": "Desc", "complete": False}]
result = get_next_id(tasks)
assert isinstance(result, int)
assert result == 6

# Test 20: Result is guaranteed unique and > all existing IDs
tasks = [
    {"id": 10, "title": "Task 10", "desc": "Desc", "complete": False},
    {"id": 5, "title": "Task 5", "desc": "Desc", "complete": False},
    {"id": 20, "title": "Task 20", "desc": "Desc", "complete": False}
]
result = get_next_id(tasks)
assert result > 10
assert result > 5
assert result > 20
assert result == 21
```

---

## Usage Examples

### Example 1: Simple Get Next ID
```python
tasks = [
    {"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False},
    {"id": 2, "title": "Task 2", "desc": "Desc 2", "complete": False}
]

next_id = get_next_id(tasks)
print(f"Next ID: {next_id}")  # Output: Next ID: 3
```

### Example 2: Empty List
```python
tasks = []
next_id = get_next_id(tasks)
print(f"First task ID: {next_id}")  # Output: First task ID: 1
```

### Example 3: Non-Sequential IDs
```python
tasks = [
    {"id": 5, "title": "Task 5", "desc": "Desc", "complete": False},
    {"id": 10, "title": "Task 10", "desc": "Desc", "complete": False},
    {"id": 3, "title": "Task 3", "desc": "Desc", "complete": False}
]

next_id = get_next_id(tasks)
print(f"Next ID: {next_id}")  # Output: Next ID: 11
```

### Example 4: Used in add_task() Function
```python
def add_task(tasks):
    """Add task using get_next_id helper"""
    title = input("Enter task title: ").strip()
    desc = input("Enter task description: ").strip()

    # Use helper to get next ID
    task_id = get_next_id(tasks)

    task = {
        "id": task_id,
        "title": title,
        "desc": desc,
        "complete": False
    }

    tasks.append(task)
    print(f"Task added successfully (ID: {task_id}).")
```

**Usage:**
```python
tasks = []

add_task(tasks)  # User enters: "Task 1", "Description 1"
# Output: Task added successfully (ID: 1).

add_task(tasks)  # User enters: "Task 2", "Description 2"
# Output: Task added successfully (ID: 2).

print(tasks)
# Output: [
#     {'id': 1, 'title': 'Task 1', 'desc': 'Description 1', 'complete': False},
#     {'id': 2, 'title': 'Task 2', 'desc': 'Description 2', 'complete': False}
# ]
```

### Example 5: Handling Imported Tasks with Non-Sequential IDs
```python
def import_tasks(tasks, imported_data):
    """Import tasks that may have non-sequential IDs"""
    max_existing_id = get_next_id(tasks) - 1

    for imported_task in imported_data:
        # Reassign ID to avoid conflicts
        new_id = get_next_id(tasks)
        task = {
            "id": new_id,
            "title": imported_task["title"],
            "desc": imported_task["desc"],
            "complete": imported_task.get("complete", False)
        }
        tasks.append(task)

    print(f"Imported {len(imported_data)} tasks")
```

### Example 6: Bulk Create Tasks
```python
def create_tasks_from_list(task_list, titles):
    """Create multiple tasks"""
    for title in titles:
        task_id = get_next_id(task_list)
        task = {
            "id": task_id,
            "title": title,
            "desc": "Auto-created task",
            "complete": False
        }
        task_list.append(task)
    print(f"Created {len(titles)} tasks")

# Usage
tasks = []
create_tasks_from_list(tasks, [
    "Buy groceries",
    "Clean house",
    "Finish project",
    "Call mom"
])
```

### Example 7: Recovery After Data Loss
```python
def recover_tasks(old_tasks, recovered_ids):
    """Recover tasks with reassigned IDs"""
    tasks = []
    for id_to_recover in recovered_ids:
        old_task = find_task(old_tasks, id_to_recover)
        if old_task:
            new_id = get_next_id(tasks)
            new_task = {
                "id": new_id,
                "title": old_task["title"],
                "desc": old_task["desc"],
                "complete": old_task["complete"]
            }
            tasks.append(new_task)
    return tasks
```

---

## Integration with Other Functions

This helper function supports the entire task management system:

```
get_next_id()  ← Centralized ID generation
    ↓
Used by:
├─ add_task()        - Generate ID for new task
├─ import_tasks()    - Generate IDs for imported data
├─ bulk_create()     - Generate IDs for bulk operations
└─ recovery()        - Generate IDs during data recovery
```

**Dependency Graph:**
```
add_task(tasks)
    ├─ input() × 2 (title, description)
    ├─ get_next_id(tasks)  ← Get next available ID
    ├─ dict creation
    ├─ tasks.append()
    └─ print() confirmation
```

---

## Performance Characteristics

| Metric | Value |
|--------|-------|
| **Time Complexity** | O(n) – single pass through list |
| **Space Complexity** | O(1) – no additional structures |
| **Best Case** | O(n) – must check all tasks |
| **Worst Case** | O(n) – must check all tasks |
| **Average Case** | O(n) – must check all tasks |
| **Typical List Size** | 10-1000 tasks (negligible) |

---

## Dependencies and Constraints

| Constraint | Details |
|-----------|---------|
| **Python Version** | 3.6+ (uses type hints) |
| **External Packages** | None (standard library only) |
| **OS Compatibility** | All platforms (Linux, macOS, Windows) |
| **Character Encoding** | Any (only processes integers) |
| **Input Validation** | None in basic version (caller validates) |
| **Error Handling** | Propagates structural errors to caller |

### Required Data Structures

```python
# tasks parameter requirements
tasks = [
    {"id": int, "title": str, "desc": str, "complete": bool},
    # ... more tasks
]

# Each task must have "id" field (integer)
# Field name must be exactly "id" (case-sensitive)
```

---

## Related Functions

This helper function supports the entire task management system:

- **`get_next_id(tasks)`** – Get next available ID (this function)
- **`add_task(tasks)`** – Uses `get_next_id()` to create new task
- **`find_task(tasks, task_id)`** – Finds task by ID
- **`delete_task(tasks, task_id)`** – Removes task
- **`update_task(tasks, task_id)`** – Modifies task
- **`toggle_complete(tasks, task_id)`** – Changes completion status
- **`print_tasks(tasks)`** – Displays all tasks
- **`main()`** – Main event loop

---

## Production Checklist

Before deploying this function:

- [ ] Function is defined in `src/core.py` or `src/main.py`
- [ ] Function accepts `tasks` parameter (list of dicts)
- [ ] Function returns integer
- [ ] Returns 1 for empty list
- [ ] Returns max(id) + 1 for non-empty list
- [ ] Works with single task
- [ ] Works with multiple tasks
- [ ] Handles non-sequential IDs correctly
- [ ] Handles gaps in ID numbering
- [ ] Does not modify the task list
- [ ] Does not print any messages (silent function)
- [ ] Type hints are present: `(list[dict]) -> int`
- [ ] Docstring is complete with examples
- [ ] Tested with empty list
- [ ] Tested with single and multiple tasks
- [ ] Tested with non-sequential IDs
- [ ] Tested with gaps in numbering
- [ ] Used in add_task() function
- [ ] Returns guaranteed unique ID
- [ ] Imported and reusable across functions

---

## Common Patterns

### Pattern 1: Generate ID Before Creating Task
```python
next_id = get_next_id(tasks)
new_task = {
    "id": next_id,
    "title": "Task",
    "desc": "Description",
    "complete": False
}
tasks.append(new_task)
```

### Pattern 2: Generate ID in Inline Assignment
```python
tasks.append({
    "id": get_next_id(tasks),
    "title": input("Title: ").strip(),
    "desc": input("Description: ").strip(),
    "complete": False
})
```

### Pattern 3: Bulk Create with Sequential IDs
```python
for title in title_list:
    tasks.append({
        "id": get_next_id(tasks),
        "title": title,
        "desc": "Auto-created",
        "complete": False
    })
```

### Pattern 4: Generate ID for Imported Task
```python
imported_data = {"title": "Imported", "desc": "From external"}
new_task = {
    "id": get_next_id(tasks),
    "title": imported_data["title"],
    "desc": imported_data["desc"],
    "complete": False
}
tasks.append(new_task)
```

### Pattern 5: Get ID Without Adding Task (Peek)
```python
# See what the next ID would be without modifying list
next_id_preview = get_next_id(tasks)
print(f"Next task will have ID: {next_id_preview}")
# ... do something else ...
# When ready to add task
actual_id = get_next_id(tasks)  # May be different if list changed
```

---

## Troubleshooting

### Issue: ID returns len(tasks) + 1 (doesn't account for non-sequential IDs)
**Solution:** Ensure you're using `max()` not `len()`:
```python
# Correct - finds maximum ID
result = max((task["id"] for task in tasks), default=0) + 1

# Incorrect - assumes sequential IDs
result = len(tasks) + 1
```

### Issue: Returns 0 instead of 1 for empty list
**Solution:** Set default parameter correctly:
```python
# Correct - default=0, then +1 = 1
result = max((task["id"] for task in tasks), default=0) + 1

# Incorrect - default=None would cause error
result = max((task["id"] for task in tasks)) + 1
```

### Issue: Duplicate IDs generated
**Solution:** This shouldn't happen with correct implementation. Verify:
1. `get_next_id()` is called each time (not cached)
2. List is updated with each append
3. No manual ID assignment overriding result

```python
# Correct - function called each time
id1 = get_next_id(tasks)  # Returns 1
tasks.append({"id": id1, ...})
id2 = get_next_id(tasks)  # Returns 2 (sees updated list)

# Incorrect - ID cached
id = get_next_id(tasks)   # Returns 1
id1 = id  # 1
id2 = id  # 1 (same, causes duplicate!)
tasks.append({"id": id1, ...})
tasks.append({"id": id2, ...})
```

### Issue: KeyError on task["id"]
**Solution:** Verify all tasks have "id" field:
```python
# Check for missing ID field
for task in tasks:
    if "id" not in task:
        print(f"Task missing 'id' field: {task}")
```

### Issue: TypeError on max()
**Solution:** Verify task["id"] values are integers:
```python
# Check ID types
for task in tasks:
    if not isinstance(task["id"], int):
        print(f"Task has non-integer ID: {task}")
```

---

## Comparison: len(tasks) + 1 vs max() + 1

### Scenario: Non-Sequential IDs After Deletion

**Using len(tasks) + 1 (WRONG):**
```python
tasks = [
    {"id": 1, ...},
    {"id": 2, ...},
    {"id": 3, ...}
]
len(tasks) = 3
next_id = len(tasks) + 1 = 4  # Correct

# Delete task with ID 2
tasks.remove(tasks[1])
len(tasks) = 2
next_id = len(tasks) + 1 = 3  # WRONG! ID 3 already exists
```

**Using max() + 1 (CORRECT):**
```python
tasks = [
    {"id": 1, ...},
    {"id": 2, ...},
    {"id": 3, ...}
]
max([1, 2, 3]) + 1 = 4  # Correct

# Delete task with ID 2
tasks.remove(tasks[1])
max([1, 3]) + 1 = 4  # CORRECT! Avoids ID 3
```

**Conclusion:** Always use `max()` instead of `len()` for robust ID generation!

---

## Enhancement Options (Optional)

These enhancements are NOT required but can improve functionality:

1. **Return Tuple (ID, Count)**
   - Return both next ID and task count
   - Useful for status display
   - Example: `(4, 3)` means "next ID is 4, have 3 tasks"

2. **Safe Mode with Validation**
   - Check all tasks have valid IDs
   - Raise exception on missing/invalid ID fields
   - Ensure data integrity

3. **Gap Filling (Optional)**
   - Instead of max + 1, find first missing ID
   - Example: IDs [1, 3, 4] → return 2 (fill gap)
   - More efficient list space usage

4. **Custom ID Prefix**
   - Generate IDs with prefix (T001, T002, etc.)
   - Support different ID schemes
   - Requires refactoring to strings

5. **Audit Logging**
   - Log ID generation events
   - Track who requested ID and when
   - Create audit trail for ID assignment

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-12-28 | Initial skill document; robust, efficient ID generation |

---

