# Skill: Generate Yes/No Confirmation Function

**Owned by:** `cli-interface-subagent`
**Feature:** Todo App Phase I - CLI Interface
**Status:** Production-Ready

---

## Purpose

Generate the `confirm(prompt: str) -> bool` function that safely asks users to confirm actions with yes/no responses. This function provides flexible input acceptance (y/Y/yes/Yes for True, n/N/no/No for False), input validation with re-prompting, and guaranteed boolean return values.

---

## When to Use

- **Destructive Operations:** Before deleting a task (deletion is irreversible)
- **Data Modification:** Confirming updates that change task state
- **Critical Actions:** Any operation user might want to reconsider
- **User Safety:** When wrong choice could have negative consequences
- **Completion Toggles:** Confirming mark as complete/incomplete actions

---

## Inputs

**Function Signature:**
```python
def confirm(prompt: str) -> bool:
```

**Parameter Details:**

- **`prompt`** (str): The confirmation question displayed to user
  - Should be a clear question ending with a hint about valid responses
  - Examples:
    - `"Delete this task? (y/n): "`
    - `"Are you sure? (yes/no): "`
    - `"Mark task as complete? (y/n): "`
    - `"Update task description? (yes/no): "`

---

## Step-by-Step Process

1. **Infinite Loop Start:**
   - Begin a `while True` loop to keep asking until valid response received

2. **Display Prompt:**
   - Print the prompt to user with `input(prompt)`
   - Prompt stays on same line as user response

3. **Normalize Input:**
   - Convert user input to lowercase for case-insensitive comparison
   - Strip leading/trailing whitespace

4. **Check for Affirmative Response:**
   - Check if input equals "y" or "yes"
   - If match, return `True` and exit function

5. **Check for Negative Response:**
   - Check if input equals "n" or "no"
   - If match, return `False` and exit function

6. **Handle Invalid Input:**
   - If input matches neither affirmative nor negative
   - Print error message: `"Invalid input. Please enter 'y' or 'n'."`
   - Loop back to step 2 to ask again

7. **Handle Keyboard Interrupt (Optional):**
   - If user presses Ctrl+C, can either:
     - Exit gracefully (recommend returning False as "no")
     - Propagate exception and let caller handle

---

## Output

**Function Name:** `confirm(prompt: str) -> bool`

**Return Value:**
- `True` if user confirms (y/Y/yes/Yes)
- `False` if user declines (n/N/no/No)

**Example Output Flow 1 (Yes Response):**
```
Delete this task? (y/n): yes
```
Function returns: `True`

**Example Output Flow 2 (No Response):**
```
Mark task as complete? (y/n): n
```
Function returns: `False`

**Example Output Flow 3 (Invalid, then Valid):**
```
Are you sure? (yes/no): maybe
Invalid input. Please enter 'y' or 'n'.
Are you sure? (yes/no): y
```
Function returns: `True`

**Example Output Flow 4 (Multiple Invalid, then Valid):**
```
Update task? (y/n): abc
Invalid input. Please enter 'y' or 'n'.
Update task? (y/n): 1
Invalid input. Please enter 'y' or 'n'.
Update task? (y/n): yes
```
Function returns: `True`

---

## Implementation

### Python Code (Production-Ready)

```python
def confirm(prompt: str) -> bool:
    """
    Ask user for yes/no confirmation and return boolean result.

    Displays the provided prompt and repeatedly asks for input until the user
    provides a valid response. Accepts multiple forms of yes (y/Y/yes/Yes) and
    no (n/N/no/No), with flexible capitalization and whitespace handling.

    Args:
        prompt (str): The confirmation question displayed to user.
                     Should indicate valid responses (e.g., "(y/n): ")

    Returns:
        bool: True if user confirms (y/Y/yes/Yes)
              False if user declines (n/N/no/No)

    Example:
        >>> if confirm("Delete this task? (y/n): "):
        ...     delete_task()
        ... else:
        ...     print("Task not deleted.")

        Delete this task? (y/n): yes
        True

    Example with invalid input:
        >>> result = confirm("Are you sure? (yes/no): ")
        Are you sure? (yes/no): maybe
        Invalid input. Please enter 'y' or 'n'.
        Are you sure? (yes/no): y
        >>> print(result)
        True

    Example with various valid inputs:
        >>> confirm("Continue? (y/n): ")  # User enters: Y → Returns True
        >>> confirm("Continue? (y/n): ")  # User enters: NO → Returns False
        >>> confirm("Continue? (y/n): ")  # User enters: Yes → Returns True
        >>> confirm("Continue? (y/n): ")  # User enters: n → Returns False
    """
    while True:
        # Get input from user
        response = input(prompt)

        # Normalize: lowercase and strip whitespace
        response = response.lower().strip()

        # Check for affirmative responses
        if response in ["y", "yes"]:
            return True

        # Check for negative responses
        if response in ["n", "no"]:
            return False

        # Invalid input; re-prompt
        print("Invalid input. Please enter 'y' or 'n'.")
```

### Design Notes

- **Flexible Input:** Accepts y/Y/yes/Yes and n/N/no/No in any case
- **Whitespace Handling:** `.strip()` removes leading/trailing spaces
- **Case Insensitive:** `.lower()` normalizes all inputs for comparison
- **Early Returns:** Returns immediately on valid response to exit loop
- **Clear Error Message:** "Invalid input. Please enter 'y' or 'n'." guides user
- **Simple Logic:** Uses `in` operator for membership testing
- **Comprehensive Docstring:** Includes purpose, args, returns, and examples

### Why This Design?

| Decision | Rationale |
|----------|-----------|
| **Case insensitive** | User shouldn't need to match exact case; common UX pattern |
| **Multiple valid inputs** | "y" and "yes" both acceptable; gives users flexibility |
| **Strip whitespace** | User might accidentally add spaces; be forgiving |
| **Infinite loop** | Ensures valid response obtained before continuing |
| **Early returns** | Clean exit; no need for complex conditional logic |
| **Simple error message** | Brief, actionable; not verbose or condescending |
| **No Ctrl+C handling** | Let KeyboardInterrupt propagate; caller can handle if needed |

---

## Failure Handling

| Scenario | Behavior | Example |
|----------|----------|---------|
| **Empty input** | Invalid; re-prompt | Input: "" → "Invalid input. Please enter 'y' or 'n'." |
| **Single letter 'y'** | Accept as True | Input: "y" → Returns True |
| **Single letter 'Y'** | Accept as True | Input: "Y" → Returns True |
| **Word "yes"** | Accept as True | Input: "yes" → Returns True |
| **Word "Yes"** | Accept as True | Input: "Yes" → Returns True |
| **Word "YES"** | Accept as True | Input: "YES" → Returns True |
| **Single letter 'n'** | Accept as False | Input: "n" → Returns False |
| **Single letter 'N'** | Accept as False | Input: "N" → Returns False |
| **Word "no"** | Accept as False | Input: "no" → Returns False |
| **Word "No"** | Accept as False | Input: "No" → Returns False |
| **Word "NO"** | Accept as False | Input: "NO" → Returns False |
| **Leading/trailing spaces** | Strip and process | Input: "  yes  " → Returns True |
| **Invalid input** | Re-prompt | Input: "maybe" → "Invalid input. Please enter 'y' or 'n'." |
| **Decimal/numeric input** | Invalid; re-prompt | Input: "1" → "Invalid input. Please enter 'y' or 'n'." |
| **Other text** | Invalid; re-prompt | Input: "yep" → "Invalid input. Please enter 'y' or 'n'." |
| **Ctrl+C (KeyboardInterrupt)** | Raises exception (can be caught) | Input: Ctrl+C → Exception propagates |

**Note on KeyboardInterrupt:**
The basic implementation lets KeyboardInterrupt propagate. This is appropriate because:
- Caller can handle it if needed
- Matches behavior of `get_int_input()`
- User is explicitly pressing Ctrl+C to interrupt

If you want to handle it gracefully:
```python
except KeyboardInterrupt:
    print("\nGoodbye!")
    return False  # or sys.exit(0)
```

### Enhanced Version with Ctrl+C Handling (Optional)

```python
import sys

def confirm(prompt: str) -> bool:
    """Confirm with graceful Ctrl+C handling"""
    while True:
        try:
            response = input(prompt).lower().strip()

            if response in ["y", "yes"]:
                return True
            elif response in ["n", "no"]:
                return False
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

        except KeyboardInterrupt:
            print("\nGoodbye!")
            sys.exit(0)
```

---

## Acceptance Criteria

- ✓ Function accepts a string prompt parameter
- ✓ Function returns a boolean (True or False)
- ✓ Accepts "y" and "yes" (any case) and returns True
- ✓ Accepts "n" and "no" (any case) and returns False
- ✓ Rejects empty input and re-prompts
- ✓ Rejects invalid input with error message: "Invalid input. Please enter 'y' or 'n'."
- ✓ Input is case-insensitive (Y/N/Yes/No/YES/NO all work)
- ✓ Leading/trailing whitespace is stripped
- ✓ User can retry multiple times until valid input
- ✓ Function returns immediately on valid input
- ✓ Works on all platforms (Windows, Mac, Linux)
- ✓ Type hints are present and correct
- ✓ Docstring includes purpose, examples, and valid inputs

---

## Testing Checklist

```python
import sys
import io
from unittest.mock import patch

# Test 1: Function exists and is callable
assert callable(confirm)

# Test 2: Accept 'y' → True
with patch('builtins.input', return_value='y'):
    result = confirm("Continue? (y/n): ")
    assert result is True
    assert isinstance(result, bool)

# Test 3: Accept 'Y' → True
with patch('builtins.input', return_value='Y'):
    result = confirm("Continue? (y/n): ")
    assert result is True

# Test 4: Accept 'yes' → True
with patch('builtins.input', return_value='yes'):
    result = confirm("Continue? (y/n): ")
    assert result is True

# Test 5: Accept 'Yes' → True
with patch('builtins.input', return_value='Yes'):
    result = confirm("Continue? (y/n): ")
    assert result is True

# Test 6: Accept 'YES' → True
with patch('builtins.input', return_value='YES'):
    result = confirm("Continue? (y/n): ")
    assert result is True

# Test 7: Accept 'n' → False
with patch('builtins.input', return_value='n'):
    result = confirm("Continue? (y/n): ")
    assert result is False

# Test 8: Accept 'N' → False
with patch('builtins.input', return_value='N'):
    result = confirm("Continue? (y/n): ")
    assert result is False

# Test 9: Accept 'no' → False
with patch('builtins.input', return_value='no'):
    result = confirm("Continue? (y/n): ")
    assert result is False

# Test 10: Accept 'No' → False
with patch('builtins.input', return_value='No'):
    result = confirm("Continue? (y/n): ")
    assert result is False

# Test 11: Accept 'NO' → False
with patch('builtins.input', return_value='NO'):
    result = confirm("Continue? (y/n): ")
    assert result is False

# Test 12: Accept input with leading spaces → True
with patch('builtins.input', return_value='  yes  '):
    result = confirm("Continue? (y/n): ")
    assert result is True

# Test 13: Accept input with trailing spaces → False
with patch('builtins.input', return_value='  no  '):
    result = confirm("Continue? (y/n): ")
    assert result is False

# Test 14: Reject empty string and retry
inputs = iter(['', 'y'])
with patch('builtins.input', side_effect=inputs):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    result = confirm("Continue? (y/n): ")
    sys.stdout = sys.__stdout__
    assert result is True
    assert "Invalid input. Please enter 'y' or 'n'." in captured_output.getvalue()

# Test 15: Reject invalid input and retry
inputs = iter(['maybe', 'yes'])
with patch('builtins.input', side_effect=inputs):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    result = confirm("Continue? (y/n): ")
    sys.stdout = sys.__stdout__
    assert result is True
    assert "Invalid input. Please enter 'y' or 'n'." in captured_output.getvalue()

# Test 16: Reject numeric input and retry
inputs = iter(['1', 'n'])
with patch('builtins.input', side_effect=inputs):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    result = confirm("Continue? (y/n): ")
    sys.stdout = sys.__stdout__
    assert result is False
    assert "Invalid input. Please enter 'y' or 'n'." in captured_output.getvalue()

# Test 17: Multiple invalid inputs before valid
inputs = iter(['maybe', 'yep', '1', 'no', 'yes'])
with patch('builtins.input', side_effect=inputs):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    result = confirm("Continue? (y/n): ")
    sys.stdout = sys.__stdout__
    assert result is True
    output = captured_output.getvalue()
    # Should have 4 error messages (for inputs: 'maybe', 'yep', '1', 'no')
    assert output.count("Invalid input. Please enter 'y' or 'n'.") == 4

# Test 18: Reject partial matches
inputs = iter(['ye', 'y'])
with patch('builtins.input', side_effect=inputs):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    result = confirm("Continue? (y/n): ")
    sys.stdout = sys.__stdout__
    assert result is True
    assert "Invalid input. Please enter 'y' or 'n'." in captured_output.getvalue()

# Test 19: Reject "yeah" (not exact match)
inputs = iter(['yeah', 'no'])
with patch('builtins.input', side_effect=inputs):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    result = confirm("Continue? (y/n): ")
    sys.stdout = sys.__stdout__
    assert result is False
    assert "Invalid input. Please enter 'y' or 'n'." in captured_output.getvalue()

# Test 20: Custom prompt is used
with patch('builtins.input', return_value='y') as mock_input:
    confirm("Custom prompt: ")
    mock_input.assert_called_with("Custom prompt: ")

# Test 21: Returns immediately on first valid response
with patch('builtins.input', return_value='yes'):
    with patch('builtins.print') as mock_print:
        result = confirm("Continue? (y/n): ")
        assert result is True
        # Verify no error messages printed (only valid input given)
        calls = [str(call) for call in mock_print.call_args_list]
        assert not any("Invalid input" in str(call) for call in calls)
```

---

## Usage Examples

### Example 1: Delete Task Confirmation
```python
def delete_task(tasks, task_id):
    """Delete a task with user confirmation"""
    task = find_task(tasks, task_id)

    if not task:
        print(f"Error: Task {task_id} not found.")
        return

    # Display task before deleting
    print(f"Task: {task['id']}. {task['title']} - {task['desc']}")

    # Get confirmation
    if confirm("Delete this task? (y/n): "):
        tasks.remove(task)
        print("Task deleted successfully!")
    else:
        print("Task not deleted.")
```

**Interactive Flow:**
```
Task: 1. Buy groceries - Milk, eggs, bread
Delete this task? (y/n): maybe
Invalid input. Please enter 'y' or 'n'.
Delete this task? (y/n): y
Task deleted successfully!
```

### Example 2: Update Task Confirmation
```python
def update_task(tasks, task_id):
    """Update a task with confirmation"""
    task = find_task(tasks, task_id)

    if not task:
        print(f"Error: Task {task_id} not found.")
        return

    # Show current task
    print(f"Current: {task['title']}")

    # Get new input
    new_title = input("New title: ").strip()
    new_desc = input("New description: ").strip()

    # Confirm before updating
    if confirm("Save changes? (yes/no): "):
        task["title"] = new_title
        task["desc"] = new_desc
        print("Task updated!")
    else:
        print("Changes discarded.")
```

**Interactive Flow:**
```
Current: Buy groceries
New title: Buy vegetables
New description: Carrots, lettuce, tomatoes
Save changes? (yes/no): yes
Task updated!
```

### Example 3: Mark Complete Confirmation (Optional)
```python
def toggle_task_complete(tasks, task_id):
    """Toggle task complete status with optional confirmation"""
    task = find_task(tasks, task_id)

    if not task:
        print(f"Error: Task {task_id} not found.")
        return

    current_status = "complete" if task["complete"] else "incomplete"
    new_status = "incomplete" if task["complete"] else "complete"

    # For sensitive operations, ask for confirmation
    if confirm(f"Mark as {new_status}? (y/n): "):
        task["complete"] = not task["complete"]
        print(f"Task marked as {new_status}!")
    else:
        print("Status not changed.")
```

**Interactive Flow:**
```
Mark as complete? (y/n): Y
Task marked as complete!
```

### Example 4: Batch Operation with Confirmation
```python
def delete_all_completed(tasks):
    """Delete all completed tasks with confirmation"""
    completed = [t for t in tasks if t["complete"]]

    if not completed:
        print("No completed tasks to delete.")
        return

    print(f"Found {len(completed)} completed tasks:")
    for task in completed:
        print(f"  - {task['title']}")

    if confirm("Delete all these tasks? (yes/no): "):
        for task in completed:
            tasks.remove(task)
        print(f"Deleted {len(completed)} tasks!")
    else:
        print("No tasks deleted.")
```

**Interactive Flow:**
```
Found 2 completed tasks:
  - Finish Python project
  - Call mom
Delete all these tasks? (yes/no): no
No tasks deleted.
```

---

## Integration with Other Functions

This function works with destructive or significant operations:

```python
# Operation pattern: Show → Confirm → Execute
def delete_task(tasks, task_id):
    task = find_task(tasks, task_id)
    if task:
        print_task(task)  # Show what will be deleted
        if confirm("Delete? (y/n): "):  # Get confirmation
            tasks.remove(task)  # Execute operation
            print("Deleted!")

# Operation pattern: Get input → Confirm → Apply
def update_task(tasks, task_id):
    task = find_task(tasks, task_id)
    if task:
        new_data = get_task_input()  # Get new data
        if confirm("Save changes? (y/n): "):  # Confirm before applying
            task.update(new_data)
            print("Updated!")

# Menu integration: Operations that need confirmation
def main():
    tasks = []
    while True:
        choice = get_menu_choice()

        if choice == 0:
            break
        elif choice == 1:
            add_task(tasks)
        elif choice == 2:
            print_tasks(tasks)
        elif choice == 3:
            task_id = get_int_input("Enter task ID: ")
            update_task(tasks, task_id)  # May use confirm() internally
        elif choice == 4:
            task_id = get_int_input("Enter task ID: ")
            delete_task(tasks, task_id)  # Uses confirm() for safety
        elif choice == 5:
            task_id = get_int_input("Enter task ID: ")
            toggle_task_complete(tasks, task_id)
```

---

## Dependencies and Constraints

| Constraint | Details |
|-----------|---------|
| **Python Version** | 3.6+ (uses f-strings and type hints) |
| **External Packages** | None (standard library only) |
| **OS Compatibility** | All platforms (Linux, macOS, Windows) |
| **Character Encoding** | Any (only processes ASCII text) |
| **Performance** | O(1) per call; depends on user input |
| **Memory** | O(1) additional space; no data structures |
| **Input Method** | Interactive stdin only |

---

## Related Functions

This function is part of the user interaction system:

- **`display_menu()`** – Shows menu options
- **`get_int_input(prompt)`** – Reads integer with validation
- **`get_menu_choice()`** – Gets valid menu selection (0-5)
- **`get_task_input()`** – Reads task title and description
- **`confirm(prompt)`** – Gets yes/no confirmation (this function)
- **`add_task(tasks, ...)`** – May use input functions
- **`delete_task(tasks, task_id)`** – Uses `confirm()` for safety
- **`update_task(tasks, task_id, ...)`** – May use `confirm()` to verify changes
- **`toggle_task_complete(tasks, task_id)`** – May use `confirm()` for significant actions

---

## Production Checklist

Before deploying this function:

- [ ] Function is defined in `src/cli.py` or integrated into `main.py`
- [ ] Function handles "y"/"Y"/"yes"/"Yes" and returns True
- [ ] Function handles "n"/"N"/"no"/"No" and returns False
- [ ] Function rejects invalid input with error message
- [ ] Function re-prompts after invalid input
- [ ] Input is case-insensitive (all case variations work)
- [ ] Leading/trailing whitespace is stripped
- [ ] Empty input is rejected
- [ ] Function returns boolean type (True or False)
- [ ] Tested with all valid yes responses
- [ ] Tested with all valid no responses
- [ ] Tested with invalid input (rejects and re-prompts)
- [ ] Tested with empty string (rejects)
- [ ] Tested with whitespace (strips and processes)
- [ ] Tested with multiple invalid attempts then valid
- [ ] Type hints are present and correct: `(str) -> bool`
- [ ] Docstring is complete with examples
- [ ] Integrated into delete_task() and other destructive operations
- [ ] Error message is: "Invalid input. Please enter 'y' or 'n'."

---

## Common Patterns

### Pattern 1: Simple Confirmation (Recommended)
```python
if confirm("Delete? (y/n): "):
    # Perform destructive operation
    delete_task(tasks, task_id)
else:
    # Cancel operation
    print("Operation cancelled.")
```

### Pattern 2: Show Before Confirming
```python
# Show what will be affected
print_task(task)

# Get confirmation
if confirm("Delete this task? (y/n): "):
    delete_task(task)
```

### Pattern 3: Get Input, Confirm Changes
```python
# Get new data from user
new_title = input("New title: ")
new_desc = input("New description: ")

# Confirm before applying
if confirm("Save changes? (y/n): "):
    task["title"] = new_title
    task["desc"] = new_desc
```

### Pattern 4: Bulk Operation with Confirmation
```python
# Identify items to affect
items = find_matching_items(criteria)

# Show summary
print(f"Will affect {len(items)} items")

# Get confirmation before bulk operation
if confirm("Continue? (yes/no): "):
    for item in items:
        delete_item(item)
```

---

## Performance Characteristics

| Metric | Value |
|--------|-------|
| **Time Complexity** | O(1) amortized; depends on user input |
| **Space Complexity** | O(1) – no dynamic allocation |
| **Best Case** | O(1) – user enters valid response immediately |
| **Worst Case** | O(k) where k = number of invalid attempts |
| **Average Case** | O(1) – most users answer yes/no correctly |
| **String Operations** | O(n) where n = length of input (typically <10 chars) |

---

## Troubleshooting

### Issue: Function hangs waiting for input
**Solution:** This is normal; waiting for user response. Press Ctrl+C to interrupt.

### Issue: Ctrl+C doesn't exit cleanly
**Solution:** Wrap call in try/except to handle KeyboardInterrupt:
```python
try:
    if confirm("Delete? (y/n): "):
        delete_task()
except KeyboardInterrupt:
    print("\nOperation cancelled.")
```

### Issue: "yes" not being accepted
**Solution:** Verify input is exactly "yes" (not "yeah" or "yep"). Check that `.lower()` and `.strip()` are being applied.

### Issue: Capitalized "Yes" not working
**Solution:** `.lower()` should handle this. Test with:
```python
test = "YES".lower().strip()
assert test in ["y", "yes"]
```

### Issue: Whitespace not being stripped
**Solution:** Ensure `.strip()` is called:
```python
response = input(prompt).lower().strip()
```

### Issue: Empty string returning True
**Solution:** "" is not in ["y", "yes"] or ["n", "no"], so should be rejected. Check string comparison logic.

### Issue: Partial matches accepted (e.g., "ye" returning True)
**Solution:** Use exact match with `in` operator, not substring search:
```python
# Correct - exact match
if response in ["y", "yes"]:

# Incorrect - substring match
if response.startswith("y"):
```

---

## Enhancement Options (Optional)

These enhancements are NOT required but can improve functionality:

1. **Custom Valid Responses**
   - Add parameter: `confirm(prompt, yes_answers=None, no_answers=None)`
   - Allow customization of accepted responses

2. **Default Response**
   - Add parameter: `confirm(prompt, default="n")`
   - If user presses Enter without input, use default

3. **Max Attempts**
   - Add parameter: `confirm(prompt, max_attempts=3)`
   - Exit after N invalid attempts instead of infinite loop

4. **Ctrl+C Handling**
   - Catch KeyboardInterrupt and return False
   - Treat Ctrl+C as "no" response

5. **Colored Output (ANSI)**
   - Highlight prompt or error message in color
   - Only uses standard library (no external packages)

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-12-28 | Initial skill document; production-ready implementation with comprehensive validation |

---

