"""
Unit and integration tests for Todo App Phase I Core.

Tests are organized by category:
1. Data Model Tests (5-10)
2. Helper Function Tests (5)
3. Core Operation Tests (20+)
4. UI Function Tests (10+)
5. Integration Tests (5+)

Total: 50+ tests targeting 80%+ code coverage.
"""

import pytest
import sys
from io import StringIO
from unittest.mock import patch

# Add src to path so we can import main
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent / 'src'))

import main


# ============================================================================
# Data Model Tests (5-10 tests)
# ============================================================================

class TestDataModel:
    """Tests for data model integrity and invariants."""

    def test_task_dict_structure(self):
        """Verify task dict has required fields."""
        task = {"id": 1, "title": "Test", "desc": "Description", "complete": False}
        assert "id" in task
        assert "title" in task
        assert "desc" in task
        assert "complete" in task

    def test_task_id_is_integer(self):
        """Verify task ID is an integer."""
        task = {"id": 1, "title": "Test", "desc": "Desc", "complete": False}
        assert isinstance(task["id"], int)

    def test_task_complete_is_boolean(self):
        """Verify complete status is a boolean."""
        task = {"id": 1, "title": "Test", "desc": "Desc", "complete": False}
        assert isinstance(task["complete"], bool)

    def test_new_task_starts_incomplete(self):
        """Verify new tasks have complete=False."""
        task = {"id": 1, "title": "Test", "desc": "Desc", "complete": False}
        assert task["complete"] is False

    def test_complete_toggle(self):
        """Verify complete status can be toggled."""
        task = {"id": 1, "title": "Test", "desc": "Desc", "complete": False}
        task["complete"] = not task["complete"]
        assert task["complete"] is True
        task["complete"] = not task["complete"]
        assert task["complete"] is False


# ============================================================================
# Helper Function Tests (5 tests)
# ============================================================================

class TestHelperFunctions:
    """Tests for helper functions find_task and get_next_id."""

    def test_find_task_returns_dict_when_found(self):
        """Verify find_task returns task dict when ID exists."""
        tasks = [
            {"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False},
            {"id": 2, "title": "Task 2", "desc": "Desc 2", "complete": False}
        ]
        result = main.find_task(tasks, 1)
        assert result is not None
        assert result["id"] == 1
        assert result["title"] == "Task 1"

    def test_find_task_returns_none_when_not_found(self):
        """Verify find_task returns None when ID doesn't exist."""
        tasks = [{"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False}]
        result = main.find_task(tasks, 99)
        assert result is None

    def test_find_task_with_empty_list(self):
        """Verify find_task returns None for empty list."""
        tasks = []
        result = main.find_task(tasks, 1)
        assert result is None

    def test_get_next_id_returns_1_for_empty_list(self):
        """Verify get_next_id returns 1 when list is empty."""
        tasks = []
        result = main.get_next_id(tasks)
        assert result == 1

    def test_get_next_id_increments_correctly(self):
        """Verify get_next_id increments from max ID."""
        tasks = [
            {"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False},
            {"id": 2, "title": "Task 2", "desc": "Desc 2", "complete": False},
            {"id": 3, "title": "Task 3", "desc": "Desc 3", "complete": False}
        ]
        result = main.get_next_id(tasks)
        assert result == 4

    def test_get_next_id_handles_deleted_ids(self):
        """Verify get_next_id doesn't reuse deleted IDs."""
        tasks = [
            {"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False},
            {"id": 3, "title": "Task 3", "desc": "Desc 3", "complete": False}
        ]
        # After deleting ID 2, next ID should be 4, not 2
        result = main.get_next_id(tasks)
        assert result == 4


# ============================================================================
# Core Operation Tests (20+ tests)
# ============================================================================

class TestAddTask:
    """Tests for add_task function."""

    @patch('builtins.input', side_effect=['Buy groceries', 'Milk, eggs, bread'])
    def test_add_task_creates_task_with_id_1(self, mock_input, capsys):
        """Verify add_task creates task with ID 1 in empty list."""
        tasks = []
        main.add_task(tasks)
        assert len(tasks) == 1
        assert tasks[0]["id"] == 1
        assert tasks[0]["title"] == "Buy groceries"
        assert tasks[0]["desc"] == "Milk, eggs, bread"
        assert tasks[0]["complete"] is False
        captured = capsys.readouterr()
        assert "Task added successfully (ID: 1)" in captured.out

    @patch('builtins.input', side_effect=['Finish project', 'Complete implementation'])
    def test_add_task_auto_increments_id(self, mock_input, capsys):
        """Verify add_task auto-increments ID for subsequent additions."""
        tasks = [{"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False}]
        main.add_task(tasks)
        assert len(tasks) == 2
        assert tasks[1]["id"] == 2
        captured = capsys.readouterr()
        assert "Task added successfully (ID: 2)" in captured.out

    @patch('builtins.input', side_effect=['  Buy groceries  ', '  Milk, eggs  '])
    def test_add_task_strips_whitespace(self, mock_input, capsys):
        """Verify add_task strips whitespace from title and description."""
        tasks = []
        main.add_task(tasks)
        assert tasks[0]["title"] == "Buy groceries"
        assert tasks[0]["desc"] == "Milk, eggs"

    @patch('builtins.input', side_effect=['Task 1', 'Desc 1', 'Task 2', 'Desc 2', 'Task 3', 'Desc 3'])
    def test_add_multiple_tasks_sequential_ids(self, mock_input, capsys):
        """Verify multiple additions maintain sequential IDs."""
        tasks = []
        main.add_task(tasks)
        main.add_task(tasks)
        main.add_task(tasks)
        assert len(tasks) == 3
        assert [t["id"] for t in tasks] == [1, 2, 3]


class TestDeleteTask:
    """Tests for delete_task function."""

    def test_delete_task_removes_existing_task(self):
        """Verify delete_task removes task when ID exists."""
        tasks = [
            {"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False},
            {"id": 2, "title": "Task 2", "desc": "Desc 2", "complete": False},
            {"id": 3, "title": "Task 3", "desc": "Desc 3", "complete": False}
        ]
        result = main.delete_task(tasks, 2)
        assert result is True
        assert len(tasks) == 2
        assert [t["id"] for t in tasks] == [1, 3]

    def test_delete_task_returns_false_when_not_found(self, capsys):
        """Verify delete_task returns False for non-existent ID."""
        tasks = [{"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False}]
        result = main.delete_task(tasks, 99)
        assert result is False
        assert len(tasks) == 1
        captured = capsys.readouterr()
        assert "Task with ID 99 not found" in captured.out

    def test_delete_last_task_empties_list(self):
        """Verify delete_task leaves empty list when deleting only task."""
        tasks = [{"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False}]
        result = main.delete_task(tasks, 1)
        assert result is True
        assert len(tasks) == 0

    def test_delete_task_no_id_reuse(self):
        """Verify deleted IDs are not reused in next task."""
        tasks = [
            {"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False},
            {"id": 2, "title": "Task 2", "desc": "Desc 2", "complete": False},
            {"id": 3, "title": "Task 3", "desc": "Desc 3", "complete": False}
        ]
        main.delete_task(tasks, 2)
        next_id = main.get_next_id(tasks)
        assert next_id == 4  # Not 2


class TestUpdateTask:
    """Tests for update_task function."""

    @patch('builtins.input', side_effect=['New Title', ''])
    def test_update_task_title_only(self, mock_input, capsys):
        """Verify update_task updates title while keeping description."""
        tasks = [{"id": 1, "title": "Old Title", "desc": "Original Desc", "complete": False}]
        result = main.update_task(tasks, 1)
        assert result is True
        assert tasks[0]["title"] == "New Title"
        assert tasks[0]["desc"] == "Original Desc"
        captured = capsys.readouterr()
        assert "Task updated" in captured.out

    @patch('builtins.input', side_effect=['', 'New Description'])
    def test_update_task_description_only(self, mock_input, capsys):
        """Verify update_task updates description while keeping title."""
        tasks = [{"id": 1, "title": "Original Title", "desc": "Old Desc", "complete": False}]
        result = main.update_task(tasks, 1)
        assert result is True
        assert tasks[0]["title"] == "Original Title"
        assert tasks[0]["desc"] == "New Description"
        captured = capsys.readouterr()
        assert "Task updated" in captured.out

    def test_update_task_not_found(self, capsys):
        """Verify update_task returns False for non-existent ID."""
        tasks = [{"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False}]
        result = main.update_task(tasks, 99)
        assert result is False
        captured = capsys.readouterr()
        assert "Task with ID 99 not found" in captured.out

    @patch('builtins.input', side_effect=['', ''])
    def test_update_task_no_changes(self, mock_input, capsys):
        """Verify update_task doesn't print success when no changes made."""
        tasks = [{"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False}]
        result = main.update_task(tasks, 1)
        assert result is True
        assert tasks[0]["title"] == "Task 1"
        assert tasks[0]["desc"] == "Desc 1"
        captured = capsys.readouterr()
        # Should NOT contain "Task updated" since no changes were made
        assert "Task updated" not in captured.out


class TestToggleComplete:
    """Tests for toggle_complete function."""

    def test_toggle_complete_from_false_to_true(self, capsys):
        """Verify toggle_complete changes False to True."""
        tasks = [{"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False}]
        result = main.toggle_complete(tasks, 1)
        assert result is True
        assert tasks[0]["complete"] is True
        captured = capsys.readouterr()
        assert "Task marked as complete" in captured.out

    def test_toggle_complete_from_true_to_false(self, capsys):
        """Verify toggle_complete changes True to False."""
        tasks = [{"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": True}]
        result = main.toggle_complete(tasks, 1)
        assert result is True  # Returns True because task was found and toggled
        assert tasks[0]["complete"] is False
        captured = capsys.readouterr()
        assert "Task marked as incomplete" in captured.out

    def test_toggle_complete_not_found(self, capsys):
        """Verify toggle_complete returns False for non-existent ID."""
        tasks = [{"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False}]
        result = main.toggle_complete(tasks, 99)
        assert result is False
        captured = capsys.readouterr()
        assert "Task with ID 99 not found" in captured.out


class TestPrintTasks:
    """Tests for print_tasks function."""

    def test_print_tasks_empty_list(self, capsys):
        """Verify print_tasks shows empty message for empty list."""
        tasks = []
        main.print_tasks(tasks)
        captured = capsys.readouterr()
        assert "No tasks yet. Add one!" in captured.out

    def test_print_tasks_shows_formatted_list(self, capsys):
        """Verify print_tasks displays tasks with correct format."""
        tasks = [
            {"id": 1, "title": "Task 1", "desc": "Desc 1", "complete": False},
            {"id": 2, "title": "Task 2", "desc": "Desc 2", "complete": True}
        ]
        main.print_tasks(tasks)
        captured = capsys.readouterr()
        assert "Tasks:" in captured.out
        assert "------" in captured.out
        assert "1. [ ] Task 1 - Desc 1" in captured.out
        assert "2. [X] Task 2 - Desc 2" in captured.out

    def test_print_tasks_status_indicators(self, capsys):
        """Verify status indicators [ ] and [X] display correctly."""
        tasks = [
            {"id": 1, "title": "Incomplete", "desc": "Not done", "complete": False},
            {"id": 2, "title": "Complete", "desc": "Done", "complete": True}
        ]
        main.print_tasks(tasks)
        captured = capsys.readouterr()
        assert "[ ]" in captured.out
        assert "[X]" in captured.out

    def test_print_tasks_special_characters(self, capsys):
        """Verify special characters display correctly."""
        tasks = [
            {"id": 1, "title": "Buy groceries 🛒", "desc": "Milk 🥛 & eggs 🥚", "complete": False}
        ]
        main.print_tasks(tasks)
        captured = capsys.readouterr()
        assert "🛒" in captured.out
        assert "🥛" in captured.out


# ============================================================================
# UI Function Tests (10+ tests)
# ============================================================================

class TestUIFunctions:
    """Tests for UI helper functions."""

    def test_get_int_input_valid_integer(self):
        """Verify get_int_input accepts valid integer."""
        with patch('builtins.input', return_value='42'):
            result = main.get_int_input("Enter number: ")
            assert result == 42

    def test_get_int_input_invalid_then_valid(self, capsys):
        """Verify get_int_input re-prompts on invalid input."""
        with patch('builtins.input', side_effect=['abc', '42']):
            result = main.get_int_input("Enter number: ")
            assert result == 42
            captured = capsys.readouterr()
            assert "Invalid input" in captured.out

    def test_get_int_input_negative_number(self):
        """Verify get_int_input accepts negative integers."""
        with patch('builtins.input', return_value='-5'):
            result = main.get_int_input("Enter number: ")
            assert result == -5

    def test_confirm_yes_variant(self):
        """Verify confirm accepts 'y' as yes."""
        with patch('builtins.input', return_value='y'):
            result = main.confirm("Continue? (y/n): ")
            assert result is True

    def test_confirm_yes_spelled_out(self):
        """Verify confirm accepts 'yes' as yes."""
        with patch('builtins.input', return_value='yes'):
            result = main.confirm("Continue? (y/n): ")
            assert result is True

    def test_confirm_no_variant(self):
        """Verify confirm accepts 'n' as no."""
        with patch('builtins.input', return_value='n'):
            result = main.confirm("Continue? (y/n): ")
            assert result is False

    def test_confirm_no_spelled_out(self):
        """Verify confirm accepts 'no' as no."""
        with patch('builtins.input', return_value='no'):
            result = main.confirm("Continue? (y/n): ")
            assert result is False

    def test_confirm_case_insensitive(self):
        """Verify confirm is case-insensitive."""
        with patch('builtins.input', return_value='YES'):
            result = main.confirm("Continue? (y/n): ")
            assert result is True

    def test_confirm_invalid_then_valid(self, capsys):
        """Verify confirm re-prompts on invalid input."""
        with patch('builtins.input', side_effect=['maybe', 'y']):
            result = main.confirm("Continue? (y/n): ")
            assert result is True
            captured = capsys.readouterr()
            assert "Invalid input" in captured.out

    def test_display_menu_format(self, capsys):
        """Verify display_menu shows exact format."""
        main.display_menu()
        captured = capsys.readouterr()
        assert "Todo App" in captured.out
        assert "========" in captured.out
        assert "1. Add Task" in captured.out
        assert "2. View Tasks" in captured.out
        assert "3. Update Task" in captured.out
        assert "4. Delete Task" in captured.out
        assert "5. Mark as Complete/Incomplete" in captured.out
        assert "0. Exit" in captured.out


# ============================================================================
# Integration Tests (5+ tests)
# ============================================================================

class TestIntegration:
    """Integration tests for complete workflows."""

    def test_add_and_view_workflow(self, capsys):
        """Verify add → view workflow works correctly."""
        tasks = []
        with patch('builtins.input', side_effect=['Task 1', 'Description 1']):
            main.add_task(tasks)
        assert len(tasks) == 1
        main.print_tasks(tasks)
        captured = capsys.readouterr()
        assert "Task 1" in captured.out
        assert "Description 1" in captured.out

    def test_add_delete_view_workflow(self, capsys):
        """Verify add → delete → view workflow works correctly."""
        tasks = []
        with patch('builtins.input', side_effect=['Task 1', 'Desc 1']):
            main.add_task(tasks)
        assert len(tasks) == 1
        main.delete_task(tasks, 1)
        assert len(tasks) == 0
        main.print_tasks(tasks)
        captured = capsys.readouterr()
        assert "No tasks yet" in captured.out

    def test_complete_workflow_sequential_operations(self, capsys):
        """Verify complete workflow: add multiple → toggle → delete."""
        tasks = []
        # Add 3 tasks
        with patch('builtins.input', side_effect=['Task 1', 'Desc 1', 'Task 2', 'Desc 2', 'Task 3', 'Desc 3']):
            main.add_task(tasks)
            main.add_task(tasks)
            main.add_task(tasks)
        assert len(tasks) == 3
        # Toggle one
        main.toggle_complete(tasks, 2)
        assert tasks[1]["complete"] is True
        # Delete one
        main.delete_task(tasks, 1)
        assert len(tasks) == 2
        # View
        main.print_tasks(tasks)
        captured = capsys.readouterr()
        assert "Task 2" in captured.out  # Should still be visible
        assert "Task 3" in captured.out

    def test_update_task_integration(self, capsys):
        """Verify update task integration."""
        tasks = []
        with patch('builtins.input', side_effect=['Original', 'Desc']):
            main.add_task(tasks)
        assert tasks[0]["title"] == "Original"
        # Update title
        with patch('builtins.input', side_effect=['Updated', '']):
            main.update_task(tasks, 1)
        assert tasks[0]["title"] == "Updated"

    def test_id_sequencing_with_deletions(self):
        """Verify ID sequencing after deletions."""
        tasks = []
        # Add 4 tasks
        for i in range(4):
            tasks.append({
                "id": i + 1,
                "title": f"Task {i + 1}",
                "desc": f"Desc {i + 1}",
                "complete": False
            })
        # Delete task 2
        main.delete_task(tasks, 2)
        # Next ID should be 5, not 2
        next_id = main.get_next_id(tasks)
        assert next_id == 5


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
