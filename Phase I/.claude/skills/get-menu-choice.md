# Skill: Generate Menu Choice Validation Function

**Owned by:** `cli-interface-subagent`
**Feature:** Todo App Phase I - CLI Interface
**Status:** Production-Ready

---

## Purpose

Generate the `get_menu_choice() -> int` function that orchestrates the complete menu interaction workflow: displaying the menu, reading user input with validation, checking choice validity, and returning a guaranteed valid menu option (0-5). This function combines three operations into a single, cohesive unit.

---

## When to Use

- **Main Event Loop:** In the primary application loop to get each menu selection
- **Menu Workflow:** Every time user should see the menu and select an option
- **Input Orchestration:** When you need guaranteed valid choice without external validation logic
- **User Interaction:** As the sole entry point for menu-driven navigation

---

## Inputs

**Function Signature:**
```python
def get_menu_choice() -> int:
```

**No Parameters:** Function takes no arguments and encapsulates all menu interaction logic.

**Implicit Dependencies:**
- Calls `display_menu()` to show menu options
- Calls `get_int_input()` to read and validate integer input
- Validates against known valid range (0-5)

---

## Step-by-Step Process

1. **Enter Menu Loop:**
   - Begin infinite `while True` loop
   - Loop continues until valid choice (0-5) obtained

2. **Display Menu:**
   - Call `display_menu()` to print menu options
   - Menu shows options 0-5

3. **Get Integer Input:**
   - Call `get_int_input("Choose an option: ")` to read user input
   - This function handles ValueError and KeyboardInterrupt internally
   - Returns guaranteed integer (or exits on Ctrl+C)

4. **Validate Choice Range:**
   - Check if returned integer is in valid range: 0, 1, 2, 3, 4, or 5
   - If valid, proceed to step 6

5. **Handle Invalid Choice:**
   - If choice outside valid range, print error message
   - Error message: `"Option {choice} is not valid. Please choose 0-5."`
   - Loop back to step 1 (display menu and ask again)

6. **Return Valid Choice:**
   - When valid choice obtained, return it immediately
   - Exit loop and function completes

---

## Output

**Function Name:** `get_menu_choice() -> int`

**Return Value:** An integer from the set {0, 1, 2, 3, 4, 5}

**Example Output Flow 1 (Valid First Try):**
```
Todo App
========
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark as Complete/Incomplete
0. Exit

Choose an option: 2
```
Function returns: `2`

**Example Output Flow 2 (Invalid, then Valid):**
```
Todo App
========
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark as Complete/Incomplete
0. Exit

Choose an option: abc
Invalid input. Please enter a valid integer.
Todo App
========
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark as Complete/Incomplete
0. Exit

Choose an option: 7
Option 7 is not valid. Please choose 0-5.
Todo App
========
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark as Complete/Incomplete
0. Exit

Choose an option: 3
```
Function returns: `3`

**Example Output Flow 3 (Non-Integer, then Valid):**
```
Todo App
========
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark as Complete/Incomplete
0. Exit

Choose an option: hello
Invalid input. Please enter a valid integer.
Todo App
========
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark as Complete/Incomplete
0. Exit

Choose an option: 0
```
Function returns: `0`

---

## Implementation

### Python Code (Production-Ready)

```python
def get_menu_choice() -> int:
    """
    Display menu and get a valid menu choice from user.

    This function orchestrates the complete menu interaction workflow:
    1. Display the menu (0-5 options)
    2. Read integer input from user (with error handling)
    3. Validate that choice is in valid range (0-5)
    4. Re-prompt on invalid choice
    5. Return guaranteed valid choice

    The menu loop continues until user selects a valid option (0-5).
    Non-integer input is handled by get_int_input() and triggers re-prompt.
    Out-of-range integers trigger local validation error and re-display menu.

    Returns:
        int: A valid menu choice in range [0, 1, 2, 3, 4, 5]

    Raises:
        SystemExit: If user presses Ctrl+C (handled by get_int_input())

    Example:
        >>> choice = get_menu_choice()
        Todo App
        ========
        1. Add Task
        2. View Tasks
        3. Update Task
        4. Delete Task
        5. Mark as Complete/Incomplete
        0. Exit

        Choose an option: 2
        >>> print(choice)
        2

    Example with invalid choice:
        >>> choice = get_menu_choice()
        Todo App
        ========
        1. Add Task
        2. View Tasks
        3. Update Task
        4. Delete Task
        5. Mark as Complete/Incomplete
        0. Exit

        Choose an option: 7
        Option 7 is not valid. Please choose 0-5.
        Todo App
        ========
        1. Add Task
        2. View Tasks
        3. Update Task
        4. Delete Task
        5. Mark as Complete/Incomplete
        0. Exit

        Choose an option: 2
        >>> print(choice)
        2
    """
    while True:
        # Display menu options to user
        display_menu()

        # Get integer input from user (handles ValueError and KeyboardInterrupt)
        choice = get_int_input("Choose an option: ")

        # Validate that choice is in valid range
        if choice in range(0, 6):  # Valid range: 0, 1, 2, 3, 4, 5
            return choice

        # If choice is out of range, show error and loop to re-display menu
        print(f"Option {choice} is not valid. Please choose 0-5.")
```

### Design Notes

- **Orchestration Pattern:** Combines three operations (display, input, validate) into one cohesive function
- **Separation of Concerns:** Delegates integer parsing to `get_int_input()`, menu display to `display_menu()`
- **Range Validation:** Uses `range(0, 6)` to check valid choices (more Pythonic than manual comparisons)
- **Clear Error Message:** Includes the invalid choice in error message for user context
- **No Magic Numbers:** Uses `range(0, 6)` instead of hardcoded 0-5 (maintainable)
- **Early Return:** Returns immediately on valid choice to exit loop efficiently

### Why This Design?

| Decision | Rationale |
|----------|-----------|
| **while True loop** | Ensures menu displays and user is re-prompted until valid choice |
| **Call display_menu()** | Encapsulates menu formatting; single source of truth |
| **Call get_int_input()** | Delegates integer validation; avoids duplicating error handling |
| **range(0, 6)** | Pythonic way to check membership in set {0,1,2,3,4,5} |
| **Include choice in error** | User sees what they entered; helps understand why it's invalid |
| **Error message format** | Matches output format of other CLI error messages |
| **No parameters** | Menu and prompt are fixed; no need for parameterization |

---

## Failure Handling

| Scenario | Who Handles | Behavior |
|----------|------------|----------|
| **Non-integer input** (e.g., "abc") | `get_int_input()` | Prints "Invalid input. Please enter a valid integer." and loops |
| **Decimal input** (e.g., "12.5") | `get_int_input()` | Prints "Invalid input. Please enter a valid integer." and loops |
| **Empty string** | `get_int_input()` | Prints "Invalid input. Please enter a valid integer." and loops |
| **Out-of-range integer** (e.g., 7) | `get_menu_choice()` | Prints "Option 7 is not valid. Please choose 0-5." and redisplays menu |
| **Negative integer** (e.g., -1) | `get_menu_choice()` | Prints "Option -1 is not valid. Please choose 0-5." and redisplays menu |
| **Very large integer** (e.g., 999) | `get_menu_choice()` | Prints "Option 999 is not valid. Please choose 0-5." and redisplays menu |
| **Ctrl+C (KeyboardInterrupt)** | `get_int_input()` | Prints "Goodbye!" and exits program with code 0 |
| **Ctrl+D (EOF)** | `get_int_input()` | Raises EOFError (or can be caught if get_int_input() is enhanced) |

### Error Handling Flow Diagram

```
┌─────────────────────────────────┐
│   get_menu_choice()             │
├─────────────────────────────────┤
│                                 │
│  ┌──────────────────────────┐   │
│  │ display_menu()           │   │
│  └──────────────────────────┘   │
│           ↓                      │
│  ┌──────────────────────────┐   │
│  │ get_int_input()          │   │
│  │ ├─ ValueError?           │   │
│  │ │  → Re-prompt in loop   │   │
│  │ ├─ KeyboardInterrupt?    │   │
│  │ │  → Exit(0)             │   │
│  │ └─ Valid int? Return ✓   │   │
│  └──────────────────────────┘   │
│           ↓                      │
│  ┌──────────────────────────┐   │
│  │ Validate range (0-5)     │   │
│  │ ├─ Valid? Return ✓       │   │
│  │ └─ Invalid?              │   │
│  │    Print error           │   │
│  │    Loop back to display  │   │
│  └──────────────────────────┘   │
│                                 │
└─────────────────────────────────┘
```

---

## Acceptance Criteria

- ✓ Function takes no parameters
- ✓ Function returns an integer
- ✓ Function displays menu by calling `display_menu()`
- ✓ Function gets input by calling `get_int_input()`
- ✓ Function validates choice is in range 0-5
- ✓ Valid choices (0, 1, 2, 3, 4, 5) are returned immediately
- ✓ Invalid choices print error: "Option {choice} is not valid. Please choose 0-5."
- ✓ After invalid choice, menu redisplays and user is re-prompted
- ✓ Non-integer input handled by `get_int_input()` (no crash)
- ✓ Ctrl+C (KeyboardInterrupt) exits gracefully via `get_int_input()`
- ✓ Function loops until guaranteed valid choice obtained
- ✓ Type hint is correct: `() -> int`
- ✓ Docstring includes purpose, examples, and return value

---

## Testing Checklist

```python
import sys
from unittest.mock import patch
import io

# Test 1: Function exists and is callable
assert callable(get_menu_choice)

# Test 2: Valid choice 0 (Exit) - first try
with patch('builtins.input', return_value='0'):
    result = get_menu_choice()
    assert result == 0
    assert isinstance(result, int)

# Test 3: Valid choice 1 (Add Task)
with patch('builtins.input', return_value='1'):
    result = get_menu_choice()
    assert result == 1

# Test 4: Valid choice 2 (View Tasks)
with patch('builtins.input', return_value='2'):
    result = get_menu_choice()
    assert result == 2

# Test 5: Valid choice 3 (Update Task)
with patch('builtins.input', return_value='3'):
    result = get_menu_choice()
    assert result == 3

# Test 6: Valid choice 4 (Delete Task)
with patch('builtins.input', return_value='4'):
    result = get_menu_choice()
    assert result == 4

# Test 7: Valid choice 5 (Mark Complete/Incomplete)
with patch('builtins.input', return_value='5'):
    result = get_menu_choice()
    assert result == 5

# Test 8: Invalid choice (too high) - then valid
inputs = iter(['7', '2'])
with patch('builtins.input', side_effect=inputs):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    result = get_menu_choice()
    sys.stdout = sys.__stdout__
    assert result == 2
    output = captured_output.getvalue()
    assert "Option 7 is not valid. Please choose 0-5." in output

# Test 9: Invalid choice (negative) - then valid
inputs = iter(['-1', '3'])
with patch('builtins.input', side_effect=inputs):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    result = get_menu_choice()
    sys.stdout = sys.__stdout__
    assert result == 3
    output = captured_output.getvalue()
    assert "Option -1 is not valid. Please choose 0-5." in output

# Test 10: Non-integer input - then valid
# (get_int_input handles the non-integer, shows error, loops, then we provide valid)
inputs = iter(['abc', '4'])
with patch('builtins.input', side_effect=inputs):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    result = get_menu_choice()
    sys.stdout = sys.__stdout__
    assert result == 4
    output = captured_output.getvalue()
    assert "Invalid input. Please enter a valid integer." in output

# Test 11: Multiple invalid choices before valid
inputs = iter(['7', 'abc', '10', '0'])
with patch('builtins.input', side_effect=inputs):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    result = get_menu_choice()
    sys.stdout = sys.__stdout__
    assert result == 0
    output = captured_output.getvalue()
    assert "Option 7 is not valid. Please choose 0-5." in output
    assert "Invalid input. Please enter a valid integer." in output
    assert "Option 10 is not valid. Please choose 0-5." in output

# Test 12: Display menu is called
with patch('builtins.input', return_value='1'):
    with patch('builtins.print') as mock_print:
        result = get_menu_choice()
        # Verify display_menu() was called (prints "Todo App", "========", options, etc.)
        calls = [call[0][0] for call in mock_print.call_args_list]
        assert any("Todo App" in str(call) for call in calls)
        assert any("Exit" in str(call) for call in calls)

# Test 13: Returns immediately on valid first choice
with patch('builtins.input', return_value='5'):
    with patch('builtins.print') as mock_print:
        result = get_menu_choice()
        assert result == 5
        # Verify display_menu only called once (no loop repeats)
        todo_app_calls = sum(1 for call in mock_print.call_args_list
                             if "Todo App" in str(call[0]))
        assert todo_app_calls == 1

# Test 14: Menu redisplays on invalid choice
inputs = iter(['8', '2'])
with patch('builtins.input', side_effect=inputs):
    with patch('builtins.print') as mock_print:
        result = get_menu_choice()
        # Menu should display twice (once for initial, once after error)
        todo_app_calls = sum(1 for call in mock_print.call_args_list
                             if "Todo App" in str(call[0]))
        assert todo_app_calls == 2
```

---

## Usage Examples

### Example 1: Main Application Loop
```python
def main():
    """Main application event loop"""
    tasks = []

    while True:
        choice = get_menu_choice()

        if choice == 0:
            print("Thank you for using Todo App. Goodbye!")
            break
        elif choice == 1:
            add_task(tasks)
        elif choice == 2:
            print_tasks(tasks)
        elif choice == 3:
            update_task(tasks)
        elif choice == 4:
            delete_task(tasks)
        elif choice == 5:
            toggle_task_complete(tasks)
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

Choose an option: abc
Invalid input. Please enter a valid integer.
Todo App
========
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark as Complete/Incomplete
0. Exit

Choose an option: 7
Option 7 is not valid. Please choose 0-5.
Todo App
========
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark as Complete/Incomplete
0. Exit

Choose an option: 2
(displays tasks)
```

### Example 2: No Additional Validation Needed
```python
# Because get_menu_choice() returns GUARANTEED valid choice (0-5),
# no additional validation needed in main loop

choice = get_menu_choice()
# choice is definitely 0, 1, 2, 3, 4, or 5
# Can safely use in if/elif/else without range check
```

### Example 3: Handling Menu Repetition
```python
def interactive_session():
    """Demonstrates continuous menu interaction"""
    tasks = []

    print("Welcome to Todo App!")
    print()

    while True:
        choice = get_menu_choice()
        print()  # Blank line for readability

        if choice == 0:
            print("Goodbye!")
            break
        elif choice == 1:
            title = input("Enter task title: ").strip()
            desc = input("Enter task description: ").strip()
            add_task(tasks, title, desc)
            print("Task added successfully!")
        elif choice == 2:
            if not tasks:
                print("No tasks yet. Add one!")
            else:
                print_tasks(tasks)
        # ... handle other options
        print()  # Blank line before next menu
```

---

## Integration with Other Functions

This function is the central orchestrator in the menu interaction system:

```
main() event loop
    ├─ get_menu_choice()  ← Returns guaranteed valid choice
    │   ├─ display_menu()  ← Shows options 0-5
    │   └─ get_int_input() ← Reads and validates integer
    │       ├─ ValueError handler
    │       └─ KeyboardInterrupt handler
    │
    ├─ if choice == 0: exit
    ├─ elif choice == 1: add_task()
    ├─ elif choice == 2: print_tasks() or view_tasks()
    ├─ elif choice == 3: update_task()
    ├─ elif choice == 4: delete_task()
    └─ elif choice == 5: toggle_task_complete()
```

**Guaranteed Properties:**
- Function always returns int in range [0, 5]
- No need for bounds checking in caller
- Caller can safely assume valid choice
- No if/else needed to validate choice range

---

## Dependencies and Constraints

| Constraint | Details |
|-----------|---------|
| **Python Version** | 3.7+ (uses f-strings and type hints) |
| **External Packages** | None (standard library only) |
| **Dependencies** | Requires `display_menu()` and `get_int_input()` to be defined |
| **OS Compatibility** | All platforms (Linux, macOS, Windows) |
| **Character Encoding** | Any (only processes ASCII digits) |
| **Performance** | O(1) amortized; depends on user input speed |
| **Input Method** | Interactive stdin only (not suitable for scripted input) |

### Required Functions (Must Exist)

```python
# Required: display_menu() function
def display_menu() -> None:
    """Displays menu options 0-5"""
    print("\nTodo App")
    print("========")
    # ... prints all menu options
    print("\nChoose an option: ", end="")

# Required: get_int_input() function
def get_int_input(prompt: str) -> int:
    """Gets and validates integer input from user"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            sys.exit(0)
```

---

## Related Functions

This function is the central hub in the menu interaction system:

- **`display_menu()`** – Shows menu options; called by `get_menu_choice()`
- **`get_int_input(prompt)`** – Reads integer with validation; called by `get_menu_choice()`
- **`get_menu_choice()`** – Orchestrates menu interaction (this function)
- **`add_task(tasks, title, desc)`** – Handles menu option 1
- **`view_tasks(tasks)` / `print_tasks(tasks)`** – Handles menu option 2
- **`update_task(tasks, task_id, ...)`** – Handles menu option 3
- **`delete_task(tasks, task_id)`** – Handles menu option 4
- **`toggle_task_complete(tasks, task_id)`** – Handles menu option 5
- **`main()`** – Main event loop; calls `get_menu_choice()` repeatedly

---

## Production Checklist

Before deploying this function:

- [ ] Function is defined in `src/cli.py` or integrated into `main.py`
- [ ] `display_menu()` function exists and is called
- [ ] `get_int_input()` function exists and is called
- [ ] Function validates choice in range [0, 1, 2, 3, 4, 5]
- [ ] Error message for out-of-range: "Option {choice} is not valid. Please choose 0-5."
- [ ] Menu redisplays after invalid choice
- [ ] Function returns integer type (not string)
- [ ] Tested with all valid choices (0-5)
- [ ] Tested with out-of-range integers (positive and negative)
- [ ] Tested with non-integer input (handled by `get_int_input()`)
- [ ] Tested with Ctrl+C (handled by `get_int_input()`)
- [ ] Tested with retry flow (multiple invalid, then valid)
- [ ] Type hint is correct: `() -> int`
- [ ] Docstring is complete with examples
- [ ] Function is integrated into main event loop
- [ ] No magic numbers; uses `range(0, 6)` for clarity
- [ ] Error message includes invalid choice for user context

---

## Common Patterns

### Pattern 1: Simple Main Loop
```python
def main():
    tasks = []
    while True:
        choice = get_menu_choice()
        if choice == 0:
            break
        # Handle choices 1-5
```

### Pattern 2: With Operation Handler Dispatch
```python
def main():
    tasks = []
    operations = {
        0: lambda: exit_app(),
        1: lambda: add_task(tasks),
        2: lambda: print_tasks(tasks),
        3: lambda: update_task(tasks),
        4: lambda: delete_task(tasks),
        5: lambda: toggle_task_complete(tasks)
    }

    while True:
        choice = get_menu_choice()
        operations[choice]()  # Safe because choice guaranteed in [0, 5]
```

### Pattern 3: With Operation Feedback
```python
def main():
    tasks = []
    while True:
        choice = get_menu_choice()
        print()  # Blank line

        if choice == 0:
            print("Thank you for using Todo App!")
            break
        elif choice == 1:
            add_task(tasks)
            print("Task added successfully!")
        elif choice == 2:
            print_tasks(tasks)
        # ... other options

        print()  # Blank line before next menu
```

---

## Performance Characteristics

| Metric | Value |
|--------|-------|
| **Time Complexity** | O(1) amortized; depends on user |
| **Space Complexity** | O(1) – no dynamic allocation |
| **Best Case** | O(1) – user enters valid choice immediately |
| **Worst Case** | O(k) where k = number of invalid attempts before valid choice |
| **Average Case** | O(1) – most users enter valid choice quickly |
| **Menu Display Calls** | 1 for valid first try, 2+ for invalid attempts |

---

## Troubleshooting

### Issue: Function hangs waiting for input
**Solution:** This is normal; waiting for user input. Press Ctrl+C to exit.

### Issue: Ctrl+C doesn't exit
**Solution:** Ensure `get_int_input()` is properly catching KeyboardInterrupt and calling `sys.exit(0)`.

### Issue: Invalid choice shows error but doesn't redisplay menu
**Solution:** Verify error message is printed and `while True` loop continues. Check that `display_menu()` is called at start of loop.

### Issue: Function returns string instead of int
**Solution:** This should not happen. Verify `get_int_input()` returns `int()` and not `str()`.

### Issue: Choice 6 or 7 accepted
**Solution:** Check range validation: `if choice in range(0, 6):` covers {0, 1, 2, 3, 4, 5} only. Use `range(0, 6)` not `range(0, 7)`.

### Issue: Negative numbers incorrectly accepted
**Solution:** Negative numbers are correctly rejected by `range(0, 6)`. If accepting -1, check range validation logic.

### Issue: Menu displays twice even on valid first choice
**Solution:** Check that function returns immediately after valid choice. Verify no extra `display_menu()` calls in loop.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-12-28 | Initial skill document; production-ready orchestration function |

---

