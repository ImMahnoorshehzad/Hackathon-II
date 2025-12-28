# Skill: Generate Main Menu Display Function

**Owned by:** `cli-interface-subagent`
**Feature:** Todo App Phase I - CLI Interface
**Status:** Production-Ready

---

## Purpose

Generate the `display_menu()` function that renders the main menu of the Todo App CLI. This function is the entry point for user interaction, presenting all available operations in a clear, organized format.

---

## When to Use

- **Initial CLI Setup:** When building the CLI module for the first time
- **Menu Refinement:** When updating menu options, layout, or formatting
- **Integration:** When integrating the menu into the main event loop
- **Testing:** When validating that the menu displays correctly across environments

---

## Inputs

None (function takes no parameters)

The function reads from:
- System console/stdout for output

---

## Step-by-Step Process

1. **Clear the screen (optional):** Consider using `os.system('clear')` on Unix or `os.system('cls')` on Windows for a fresh display
2. **Print the header:** Display "Todo App" with a separator line ("========")
3. **Print menu options:** Display each option on its own line:
   - Option 1: Add Task
   - Option 2: View Tasks
   - Option 3: Update Task
   - Option 4: Delete Task
   - Option 5: Mark as Complete/Incomplete
   - Option 0: Exit
4. **Print prompt:** Display "Choose an option:" to solicit user input
5. **Return control:** Function completes after printing; does not validate input or loop

---

## Output

**Function Name:** `display_menu()`

**Output to stdout:**
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

**Return Value:** None (void function)

---

## Implementation

### Python Code (Production-Ready)

```python
def display_menu():
    """
    Display the main menu of the Todo App.

    Prints a formatted menu showing all available operations:
    - Add Task
    - View Tasks
    - Update Task
    - Delete Task
    - Mark as Complete/Incomplete
    - Exit

    Takes no parameters and returns nothing. Used in conjunction with
    get_user_choice() to form the main event loop.
    """
    print("\nTodo App")
    print("========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark as Complete/Incomplete")
    print("0. Exit")
    print("\nChoose an option: ", end="")
```

### Design Notes

- **No User Input:** The function only prints; input handling is delegated to `get_user_choice()`
- **Separation of Concerns:** Menu display is decoupled from validation logic
- **Consistent Formatting:** All options use the same indentation and style
- **Blank Lines:** Strategic use of `print("\n...")` for readability
- **Standard Library Only:** Uses only built-in `print()` function

### Integration with Other Functions

This function is part of a modular CLI system:

```python
def main_loop(tasks):
    """Example main loop using display_menu()"""
    while True:
        display_menu()
        choice = get_user_choice()

        if choice == 0:
            print("Goodbye!")
            break
        elif choice == 1:
            add_task(tasks)
        elif choice == 2:
            view_tasks(tasks)
        elif choice == 3:
            update_task(tasks)
        elif choice == 4:
            delete_task(tasks)
        elif choice == 5:
            toggle_task_complete(tasks)
```

---

## Failure Handling

| Scenario | Handling |
|----------|----------|
| **Broken stdout pipe** | Function will raise `BrokenPipeError`; caller should catch and exit gracefully |
| **Permission denied** | Unlikely with stdout; would raise `PermissionError` at OS level |
| **Unicode errors** | Use `print(..., errors='replace')` if console doesn't support UTF-8 |
| **Large console buffers** | Function output is small (~10 lines); no buffer overflow risk |

**Recommended Error Handling at Call Site:**

```python
try:
    display_menu()
except BrokenPipeError:
    # Pipe was closed; exit gracefully
    sys.exit(0)
except Exception as e:
    print(f"Error displaying menu: {e}", file=sys.stderr)
    sys.exit(1)
```

---

## Acceptance Criteria

- ✓ Function prints exactly the specified menu layout to stdout
- ✓ All 6 options (0-5) are displayed in the correct order
- ✓ Header "Todo App" with separator line is shown first
- ✓ Prompt "Choose an option:" appears after all menu items
- ✓ No input validation occurs within the function
- ✓ Function completes without waiting for user response
- ✓ Output is identical across all platforms (Windows, Mac, Linux)
- ✓ Code uses only Python standard library

---

## Testing Checklist

```python
# Test 1: Function exists and is callable
assert callable(display_menu)

# Test 2: Function accepts no arguments
try:
    display_menu()
    test_passed = True
except TypeError:
    test_passed = False
assert test_passed

# Test 3: Output verification (capture stdout)
import io
import sys

captured_output = io.StringIO()
sys.stdout = captured_output
display_menu()
sys.stdout = sys.__stdout__

output = captured_output.getvalue()
assert "Todo App" in output
assert "========" in output
assert "1. Add Task" in output
assert "2. View Tasks" in output
assert "3. Update Task" in output
assert "4. Delete Task" in output
assert "5. Mark as Complete/Incomplete" in output
assert "0. Exit" in output
assert "Choose an option:" in output
```

---

## Usage Example

```python
if __name__ == "__main__":
    tasks = []

    while True:
        display_menu()

        try:
            choice = int(input())

            if choice == 0:
                print("Thank you for using Todo App. Goodbye!")
                break
            elif 1 <= choice <= 5:
                # Handle each menu option
                pass
            else:
                print("Invalid option. Please choose 0-5.")

        except ValueError:
            print("Invalid input. Please enter a number.")
```

---

## Dependencies and Constraints

| Constraint | Details |
|-----------|---------|
| **Python Version** | 3.7+ (uses standard `print()` function) |
| **External Packages** | None (standard library only) |
| **OS Compatibility** | All platforms (Linux, macOS, Windows) |
| **Character Encoding** | UTF-8 (for menu items and separators) |
| **Performance** | O(1) – instant display, no loops or iterations |

---

## Related Functions

This skill is a building block in the CLI module. Related functions that work with it:

- **`get_user_choice()`** – Reads and validates user menu selection (0-5)
- **`add_task(tasks)`** – Handles "Add Task" menu option
- **`view_tasks(tasks)`** – Handles "View Tasks" menu option
- **`update_task(tasks)`** – Handles "Update Task" menu option
- **`delete_task(tasks)`** – Handles "Delete Task" menu option
- **`toggle_task_complete(tasks)`** – Handles "Mark as Complete/Incomplete" option

---

## Production Checklist

Before deploying this function:

- [ ] Function is defined in `src/cli.py` or integrated into `main.py`
- [ ] No external imports required beyond `sys` (if using error handling)
- [ ] Output matches specification exactly (spacing, capitalization, punctuation)
- [ ] Tested with manual execution and captured output verification
- [ ] Integrated into main event loop
- [ ] Error handling is in place for broken pipes or output failures
- [ ] Code is documented with docstring as shown

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-12-28 | Initial skill document; production-ready implementation |

