#!/usr/bin/env python3
"""
Todo App Phase I Core - A Python 3.13+ CLI todo application.

This application provides a menu-driven interface for managing a list of tasks
with in-memory storage. Features include adding, viewing, updating, deleting,
and marking tasks as complete.

Usage:
    python src/main.py

Features:
    - Add Task: Create new tasks with title and description
    - View Tasks: Display all tasks in formatted list
    - Update Task: Modify task title and/or description
    - Delete Task: Remove tasks by ID
    - Mark Complete/Incomplete: Toggle task completion status
"""

import sys
from typing import Optional


# ============================================================================
# Helper Functions
# ============================================================================

def find_task(tasks: list[dict], task_id: int) -> Optional[dict]:
    """
    Find a task in the list by ID.

    Args:
        tasks: List of task dictionaries
        task_id: ID to search for

    Returns:
        Task dict if found, None if not found

    Usage:
        task = find_task(tasks, 1)
        if task:
            print(f"Found: {task['title']}")
    """
    return next((t for t in tasks if t["id"] == task_id), None)


def get_next_id(tasks: list[dict]) -> int:
    """
    Calculate the next available task ID.

    Args:
        tasks: List of task dictionaries

    Returns:
        Next ID (max(existing_ids) + 1 or 1 if empty)

    Usage:
        next_id = get_next_id(tasks)
        new_task = {"id": next_id, "title": "...", "desc": "...", "complete": False}
    """
    return max((t["id"] for t in tasks), default=0) + 1


# ============================================================================
# Core Operations
# ============================================================================

def add_task(tasks: list[dict]) -> None:
    """
    Create a new task interactively.

    Prompts user for title and description, auto-assigns ID, appends to list.

    Args:
        tasks: Task list (modified in-place)

    Output:
        "Task added successfully (ID: X)."
    """
    title = input("Title: ").strip()
    desc = input("Description: ").strip()

    task_id = get_next_id(tasks)
    tasks.append({
        "id": task_id,
        "title": title,
        "desc": desc,
        "complete": False
    })
    print(f"Task added successfully (ID: {task_id}).")


def print_tasks(tasks: list[dict]) -> None:
    """
    Display all tasks in formatted list.

    Args:
        tasks: Task list (not modified)

    Output:
        Formatted list or "No tasks yet. Add one!"
    """
    if not tasks:
        print("No tasks yet. Add one!")
        return

    print("Tasks:")
    print("------")
    for task in tasks:
        status = "[X]" if task["complete"] else "[ ]"
        print(f"{task['id']}. {status} {task['title']} - {task['desc']}")


def delete_task(tasks: list[dict], task_id: int) -> bool:
    """
    Delete a task by ID.

    Args:
        tasks: Task list (modified in-place if task found)
        task_id: ID to delete

    Returns:
        True if deleted, False if not found

    Output:
        "Task with ID X not found." if not found
    """
    task = find_task(tasks, task_id)
    if task:
        tasks.remove(task)
        return True
    else:
        print(f"Task with ID {task_id} not found.")
        return False


def update_task(tasks: list[dict], task_id: int) -> bool:
    """
    Update a task's title and/or description.

    Args:
        tasks: Task list (modified in-place if task found)
        task_id: ID to update

    Returns:
        True if task found (updated or not), False if not found

    Output:
        "Task updated." if changes made
        "Task with ID X not found." if not found
    """
    task = find_task(tasks, task_id)
    if not task:
        print(f"Task with ID {task_id} not found.")
        return False

    print(f"Current title: {task['title']}")
    print(f"Current description: {task['desc']}")

    new_title = input("New title (press Enter to keep): ").strip()
    new_desc = input("New description (press Enter to keep): ").strip()

    changed = False
    if new_title:
        task["title"] = new_title
        changed = True
    if new_desc:
        task["desc"] = new_desc
        changed = True

    if changed:
        print("Task updated.")

    return True


def toggle_complete(tasks: list[dict], task_id: int) -> bool:
    """
    Toggle task completion status.

    Args:
        tasks: Task list (modified in-place if task found)
        task_id: ID to toggle

    Returns:
        True if toggled, False if not found

    Output:
        "Task marked as complete." or "Task marked as incomplete."
        "Task with ID X not found." if not found
    """
    task = find_task(tasks, task_id)
    if not task:
        print(f"Task with ID {task_id} not found.")
        return False

    task["complete"] = not task["complete"]
    if task["complete"]:
        print("Task marked as complete.")
    else:
        print("Task marked as incomplete.")

    return True


# ============================================================================
# UI Functions
# ============================================================================

def display_menu() -> None:
    """
    Display the main menu.

    Args: None

    Output:
        Menu with 6 options (1-5, 0)
    """
    print("\nWelcome to my Todo App")
    print("========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark as Complete/Incomplete")
    print("0. Exit")


def get_menu_choice() -> int:
    """
    Display menu and get valid user choice.

    Returns:
        Integer 0-5 (guaranteed valid)

    Process:
        1. Display menu
        2. Get integer input with validation
        3. Validate range 0-5
        4. Re-prompt on invalid
        5. Return valid choice
    """
    while True:
        display_menu()
        choice = get_int_input("Choose an option: ")
        if 0 <= choice <= 5:
            return choice
        print(f"Option {choice} not valid. Please choose 0-5.")


def get_int_input(prompt: str) -> int:
    """
    Get validated integer input from user.

    Args:
        prompt: Display prompt

    Returns:
        Valid integer

    Process:
        1. Prompt user
        2. Try to parse integer
        3. On ValueError: print error, re-prompt
        4. On Ctrl+C: print "Goodbye!", exit
        5. Return integer
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            sys.exit(0)


def confirm(prompt: str) -> bool:
    """
    Get yes/no confirmation from user.

    Args:
        prompt: Display prompt (e.g., "Delete? (y/n): ")

    Returns:
        True for yes, False for no

    Process:
        1. Prompt user
        2. Accept y/Y/yes/Yes → True
        3. Accept n/N/no/No → False
        4. On invalid: re-prompt
        5. Return boolean
    """
    while True:
        response = input(prompt).lower()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


# ============================================================================
# Main Event Loop
# ============================================================================

def main() -> None:
    """
    Main application event loop.

    Process:
        1. Initialize empty task list
        2. Loop:
           - Display menu and get choice
           - Execute corresponding operation
           - Continue until user selects 0 (Exit)
    """
    tasks: list[dict] = []

    while True:
        choice = get_menu_choice()

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

    print("Goodbye! Have a nice day.")


if __name__ == "__main__":
    main()
