# Skill: Generate Robust Integer Input Function

**Owned by:** `cli-interface-subagent`
**Feature:** Todo App Phase I - CLI Interface
**Status:** Production-Ready

---

## Purpose

Generate the `get_int_input(prompt: str) -> int` function that safely and robustly reads integer input from the user. This function provides validation, error handling, and user-friendly feedback for all edge cases, including invalid input and keyboard interrupts.

---

## When to Use

- **Task ID Input:** When user needs to select a task by ID (View, Update, Delete, Complete/Incomplete)
- **Menu Selection:** When validating numeric menu choices
- **Any Integer Input:** Whenever application needs guaranteed integer input from user
- **Robust Input Handling:** When application must never crash from invalid user input

---

## Inputs

**Function Signature:**
```python
def get_int_input(prompt: str) -> int:
```

**Parameter Details:**

- **`prompt`** (str): The message displayed to user before input field
  - Should be descriptive and end with `: ` for clarity
  - Examples:
    - `"Enter task ID: "`
    - `"Enter choice (0-5): "`
    - `"How many tasks to display: "`

---

## Step-by-Step Process

1. **Infinite Loop Start:**
   - Begin a `while True` loop to keep asking until valid input received

2. **Display Prompt:**
   - Print the prompt to user with `input(prompt)`
   - Prompt does NOT include a newline; stays on same line as user input

3. **Try to Parse Integer:**
   - Attempt `int(user_input)` conversion
   - Catch `ValueError` if input is not a valid integer

4. **Handle ValueError:**
   - If conversion fails, print error message: `"Invalid input. Please enter a valid integer."`
   - Loop back to step 2 to ask again

5. **Handle KeyboardInterrupt:**
   - If user presses Ctrl+C, catch the exception
   - Print: `"\nGoodbye!"`
   - Exit program gracefully with `sys.exit(0)`

6. **Return Valid Integer:**
   - When valid integer is obtained, return it immediately
   - Exit the loop

---

## Output

**Function Name:** `get_int_input(prompt: str) -> int`

**Return Value:** A single integer entered by user

**Example Output Flow:**

```
Enter task ID: abc
Invalid input. Please enter a valid integer.
Enter task ID: 12.5
Invalid input. Please enter a valid integer.
Enter task ID: 5
```

In this example, the function returns `5` after rejecting two invalid inputs.

**Keyboard Interrupt Output:**

```
Enter task ID: ^C
Goodbye!
(Program exits with code 0)
```

---

## Implementation

### Python Code (Production-Ready)

```python
import sys


def get_int_input(prompt: str) -> int:
    """
    Safely read an integer from user input with validation and error handling.

    Displays the provided prompt and continuously asks for input until the user
    enters a valid integer. Handles two specific error cases:

    1. ValueError: User enters non-integer input (e.g., "abc", "12.5")
       - Displays error message and re-prompts
    2. KeyboardInterrupt: User presses Ctrl+C
       - Gracefully exits with goodbye message

    Args:
        prompt (str): The message to display before the input field.
                     Should include trailing space or colon (e.g., "Enter ID: ")

    Returns:
        int: A valid integer entered by the user

    Raises:
        SystemExit: Raised when user presses Ctrl+C (exits with code 0)

    Example:
        >>> task_id = get_int_input("Enter task ID: ")
        Enter task ID: abc
        Invalid input. Please enter a valid integer.
        Enter task ID: 5
        >>> print(task_id)
        5

    Example with Ctrl+C:
        >>> menu_choice = get_int_input("Choose option: ")
        Choose option: ^C
        Goodbye!
        (Program exits)
    """
    while True:
        try:
            # Request input from user and attempt conversion to integer
            user_input = input(prompt)
            return int(user_input)

        except ValueError:
            # User entered non-integer (e.g., "abc", "12.5", empty string with int())
            print("Invalid input. Please enter a valid integer.")

        except KeyboardInterrupt:
            # User pressed Ctrl+C; exit gracefully
            print("\nGoodbye!")
            sys.exit(0)
```

### Design Notes

- **Simple and Focused:** Does one thing well: read and validate integer input
- **No Range Validation:** Function does NOT validate against ranges (e.g., 0-5). Range validation is the responsibility of the caller
- **Graceful Degradation:** Both error cases (ValueError, KeyboardInterrupt) are handled without crashing
- **sys.exit() for Ctrl+C:** Using `sys.exit(0)` is the standard pattern for graceful program termination
- **Minimal Dependencies:** Only requires `sys` module from standard library
- **Type Hints:** Complete type hints for clarity and IDE support
- **Comprehensive Docstring:** Includes purpose, args, returns, raises, and usage examples

### Why This Design?

| Decision | Rationale |
|----------|-----------|
| **Infinite loop** | Ensures user must enter valid integer; no way to bypass validation |
| **Separate ValueError handling** | Distinguishes between bad input and user interruption |
| **sys.exit(0) on Ctrl+C** | Standard Unix convention; code 0 indicates graceful exit |
| **No range checking** | Keeps function single-purpose; caller validates business logic |
| **Error message is brief** | "Invalid input. Please enter a valid integer." is clear and not annoying |
| **Prompt stays on same line** | User typing appears directly after prompt for better UX |

---

## Failure Handling

| Scenario | Behavior | Example |
|----------|----------|---------|
| **Non-numeric input** | Print error; re-prompt | Input: "abc" → "Invalid input. Please enter a valid integer." |
| **Decimal number** | Print error; re-prompt | Input: "12.5" → Rejected (ValueError from `int()`) |
| **Empty input** | Print error; re-prompt | Input: "" → ValueError raised by `int("")` |
| **Very large number** | Accept if valid integer | Input: "999999999999" → Returns int successfully |
| **Negative number** | Accept if valid integer | Input: "-5" → Returns -5 (valid) |
| **Leading/trailing spaces** | Strip automatically | Input: "  5  " → Returns 5 (Python's `int()` handles this) |
| **Ctrl+C (KeyboardInterrupt)** | Print "Goodbye!" and exit | Input: Ctrl+C → Program exits with code 0 |
| **Ctrl+D (EOF)** | Raises EOFError (not caught) | Input: Ctrl+D → EOFError propagates (optional to catch) |
| **Broken pipe** | Raises BrokenPipeError | Input: Redirected to /dev/null → Error propagates |

**Note on EOFError and BrokenPipeError:**
- These are less common in interactive use
- Can be caught if needed, but current implementation lets them propagate as critical errors
- Suitable for standard interactive CLI usage

### Enhanced Version with EOFError Handling (Optional)

```python
def get_int_input(prompt: str) -> int:
    """Robust integer input with additional EOF handling"""
    while True:
        try:
            user_input = input(prompt)
            return int(user_input)

        except ValueError:
            print("Invalid input. Please enter a valid integer.")

        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            sys.exit(0)
```

---

## Acceptance Criteria

- ✓ Function accepts a string prompt parameter
- ✓ Function returns a single integer
- ✓ Non-integer input triggers error message: "Invalid input. Please enter a valid integer."
- ✓ After error, function re-prompts user immediately
- ✓ User can try multiple times until valid integer entered
- ✓ Valid integers are returned immediately (no additional prompts)
- ✓ Ctrl+C (KeyboardInterrupt) prints "Goodbye!" and exits with code 0
- ✓ Function never crashes or raises unhandled exceptions in normal use
- ✓ Only Python standard library is used (sys module)
- ✓ Type hints are present and correct
- ✓ Docstring includes usage examples
- ✓ Works on all platforms (Windows, Mac, Linux)

---

## Testing Checklist

```python
import sys
import io
from unittest.mock import patch

# Test 1: Function exists and is callable
assert callable(get_int_input)

# Test 2: Valid single-digit input
with patch('builtins.input', return_value='5'):
    result = get_int_input("Enter: ")
    assert result == 5
    assert isinstance(result, int)

# Test 3: Valid multi-digit input
with patch('builtins.input', return_value='42'):
    result = get_int_input("Enter: ")
    assert result == 42

# Test 4: Negative number input
with patch('builtins.input', return_value='-7'):
    result = get_int_input("Enter: ")
    assert result == -7

# Test 5: Large number input
with patch('builtins.input', return_value='999999999'):
    result = get_int_input("Enter: ")
    assert result == 999999999

# Test 6: Leading/trailing whitespace is handled
with patch('builtins.input', return_value='  15  '):
    result = get_int_input("Enter: ")
    assert result == 15

# Test 7: Invalid input followed by valid input (retry)
inputs = iter(['abc', '10'])
with patch('builtins.input', side_effect=inputs):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    result = get_int_input("Enter: ")
    sys.stdout = sys.__stdout__
    assert result == 10
    assert "Invalid input. Please enter a valid integer." in captured_output.getvalue()

# Test 8: Multiple invalid inputs then valid
inputs = iter(['abc', '12.5', 'hello', '999'])
with patch('builtins.input', side_effect=inputs):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    result = get_int_input("Enter: ")
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()
    assert result == 999
    assert output.count("Invalid input. Please enter a valid integer.") == 3

# Test 9: Empty string input is rejected
inputs = iter(['', '5'])
with patch('builtins.input', side_effect=inputs):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    result = get_int_input("Enter: ")
    sys.stdout = sys.__stdout__
    assert result == 5
    assert "Invalid input. Please enter a valid integer." in captured_output.getvalue()

# Test 10: Decimal input is rejected
inputs = iter(['3.14', '7'])
with patch('builtins.input', side_effect=inputs):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    result = get_int_input("Enter: ")
    sys.stdout = sys.__stdout__
    assert result == 7
    assert "Invalid input. Please enter a valid integer." in captured_output.getvalue()

# Test 11: Ctrl+C (KeyboardInterrupt) exits gracefully
with patch('builtins.input', side_effect=KeyboardInterrupt):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    try:
        get_int_input("Enter: ")
    except SystemExit as e:
        sys.stdout = sys.__stdout__
        assert e.code == 0
        assert "Goodbye!" in captured_output.getvalue()

# Test 12: Prompt is displayed to user
with patch('builtins.input', return_value='5') as mock_input:
    get_int_input("Custom Prompt: ")
    mock_input.assert_called_with("Custom Prompt: ")
```

---

## Usage Examples

### Example 1: Basic Task ID Selection
```python
# Get task ID from user
task_id = get_int_input("Enter task ID: ")
print(f"You selected task {task_id}")
```

**Interactive Flow:**
```
Enter task ID: abc
Invalid input. Please enter a valid integer.
Enter task ID: 5
You selected task 5
```

### Example 2: Menu Choice Selection
```python
def get_user_choice():
    """Get and validate menu choice"""
    choice = get_int_input("Choose an option (0-5): ")

    # Range validation happens here (outside get_int_input)
    while choice not in range(0, 6):
        print(f"Option {choice} is not valid. Please choose 0-5.")
        choice = get_int_input("Choose an option (0-5): ")

    return choice
```

**Interactive Flow:**
```
Choose an option (0-5): abc
Invalid input. Please enter a valid integer.
Choose an option (0-5): 7
Option 7 is not valid. Please choose 0-5.
Choose an option (0-5): 2
```

### Example 3: With Range Validation
```python
def get_task_id(max_id):
    """Get task ID with range validation"""
    while True:
        task_id = get_int_input(f"Enter task ID (1-{max_id}): ")

        if 1 <= task_id <= max_id:
            return task_id
        else:
            print(f"Error: Task ID must be between 1 and {max_id}.")
```

**Interactive Flow:**
```
Enter task ID (1-3): abc
Invalid input. Please enter a valid integer.
Enter task ID (1-3): 5
Error: Task ID must be between 1 and 3.
Enter task ID (1-3): 2
```

### Example 4: Integration with Menu Loop
```python
def main():
    """Main application loop"""
    tasks = []

    while True:
        display_menu()
        choice = get_int_input("Choose an option: ")

        if choice == 0:
            print("Goodbye!")
            break
        elif choice == 1:
            add_task(tasks)
        elif choice == 2:
            view_tasks(tasks)
        elif choice == 3:
            task_id = get_int_input("Enter task ID to update: ")
            update_task(tasks, task_id)
        elif choice == 4:
            task_id = get_int_input("Enter task ID to delete: ")
            delete_task(tasks, task_id)
        elif choice == 5:
            task_id = get_int_input("Enter task ID to toggle: ")
            toggle_task_complete(tasks, task_id)
        else:
            print("Invalid option. Please choose 0-5.")
```

---

## Integration with Other Functions

This skill is part of the input handling system:

```python
# Menu input flow
display_menu()
choice = get_int_input("Choose an option: ")  # Get integer with validation
validate_menu_choice(choice)                   # Validate against valid range

# Task operation flows
task_id = get_int_input("Enter task ID: ")    # Get integer with validation
if task_exists(task_id, tasks):               # Check if task exists
    update_task(tasks, task_id)
else:
    print(f"Error: Task {task_id} not found.")
```

---

## Dependencies and Constraints

| Constraint | Details |
|-----------|---------|
| **Python Version** | 3.6+ (uses f-strings and type hints) |
| **External Packages** | None (only `sys` module from standard library) |
| **OS Compatibility** | All platforms (Linux, macOS, Windows) |
| **Character Encoding** | Any (only processes ASCII digits) |
| **Performance** | O(1) per call; no loops or iterations within function |
| **Memory** | O(1) additional space; no data structures created |
| **Input Method** | Interactive stdin only (not suitable for scripted/batch input) |

---

## Related Functions

This skill is part of the robust input system:

- **`display_menu()`** – Shows main menu with all options
- **`get_user_choice()`** – Wraps `get_int_input()` with range validation (0-5)
- **`get_task_id(max_id)`** – Wraps `get_int_input()` with task ID range validation
- **`get_int_input(prompt)`** – Base integer input function (this skill)
- **`get_task_input()`** – Reads title and description (separate function)
- **`print_tasks(tasks)`** – Displays all tasks

**Recommended Helper Function: Menu Choice with Range Validation**
```python
def get_menu_choice() -> int:
    """Get menu choice with built-in range validation"""
    while True:
        choice = get_int_input("Choose an option (0-5): ")
        if 0 <= choice <= 5:
            return choice
        print(f"Option {choice} is not valid. Please choose 0-5.")
```

---

## Production Checklist

Before deploying this function:

- [ ] Function is defined in `src/cli.py` or integrated into `main.py`
- [ ] `import sys` is present at top of file
- [ ] Function handles ValueError (non-integer input)
- [ ] Function handles KeyboardInterrupt (Ctrl+C) gracefully
- [ ] Error message is: "Invalid input. Please enter a valid integer."
- [ ] Goodbye message on Ctrl+C is: "Goodbye!"
- [ ] Function returns integer type, not string
- [ ] Tested with valid single-digit input
- [ ] Tested with valid multi-digit input
- [ ] Tested with negative numbers
- [ ] Tested with whitespace (leading/trailing)
- [ ] Tested with empty string input (rejected)
- [ ] Tested with decimal input (rejected)
- [ ] Tested with non-numeric input (rejected)
- [ ] Tested with retry flow (multiple invalid, then valid)
- [ ] Tested with Ctrl+C (keyboard interrupt)
- [ ] Type hints are present and correct
- [ ] Docstring is complete with examples
- [ ] Code is integrated into menu and task input flows

---

## Common Patterns

### Pattern 1: Menu Choice with Validation
```python
while True:
    display_menu()
    choice = get_int_input("Choose an option: ")

    if choice in [0, 1, 2, 3, 4, 5]:
        return choice
    else:
        print(f"Option {choice} is not valid. Please choose 0-5.")
```

### Pattern 2: Task ID with Existence Check
```python
while True:
    task_id = get_int_input("Enter task ID: ")

    if any(task["id"] == task_id for task in tasks):
        return task_id
    else:
        print(f"Error: Task {task_id} not found.")
```

### Pattern 3: Quantity Input with Bounds
```python
while True:
    count = get_int_input("How many tasks to display: ")

    if 1 <= count <= len(tasks):
        return count
    else:
        print(f"Error: Please enter a number between 1 and {len(tasks)}.")
```

---

## Performance Characteristics

| Metric | Value |
|--------|-------|
| **Time Complexity** | O(1) per valid call |
| **Space Complexity** | O(1) – no dynamic allocation |
| **Typical Latency** | <100ms (I/O bound on user input) |
| **Max Iterations** | Unlimited (depends on user) |
| **String Parsing** | O(n) where n = length of input string (handled by `int()`) |

---

## Troubleshooting

### Issue: Function hangs waiting for input
**Solution:** This is normal behavior; function is waiting for user input. Press Ctrl+C to exit.

### Issue: Ctrl+C doesn't exit
**Solution:** Ensure `sys` is imported at top of file:
```python
import sys
```

### Issue: Negative numbers or zero are being rejected
**Solution:** They should not be. Test with:
```python
result = get_int_input("Enter number: ")  # Try -5, 0, etc.
```
Both should work. If rejected, check if caller has range validation wrapper.

### Issue: TypeError: expected string for prompt
**Solution:** Ensure you pass a string to the prompt parameter:
```python
# Correct
task_id = get_int_input("Enter ID: ")

# Incorrect
task_id = get_int_input(123)  # Pass string, not int
```

### Issue: Function returns string instead of int
**Solution:** This should not happen. Check that you're not wrapping it:
```python
# Correct - returns int
result = get_int_input("Enter: ")

# Incorrect - converts to string
result = str(get_int_input("Enter: "))
```

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-12-28 | Initial skill document; production-ready implementation with comprehensive error handling |

---

