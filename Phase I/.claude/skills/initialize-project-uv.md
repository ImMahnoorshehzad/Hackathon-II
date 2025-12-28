# Skill: Initialize Project with UV Package Manager

**Owned by:** `lead-architect-todo`
**Feature:** Todo App Phase I - Project Initialization
**Status:** Production-Ready

---

## Purpose

Initialize the Todo App Phase I project with UV package manager. This skill provides complete step-by-step commands and configuration files necessary to set up a modern Python development environment with UV, including virtual environment creation, dependency management, and project structure setup.

---

## When to Use

- **New Project Setup:** When starting a fresh Todo App Phase I project
- **Team Onboarding:** When new team members need to set up development environment
- **CI/CD Integration:** When automating project initialization in pipelines
- **Docker/Container Setup:** When containerizing the application
- **Fresh Start:** When needing to reset and reinitialize project environment

---

## Inputs

**Initialization Request:**
```
Initialize Todo App Phase I with UV
- Python version: 3.13
- Project type: Python package
- Dependencies: None (standard library only)
```

**Return Value:**
- Step-by-step commands (copy-paste ready)
- Configuration files (pyproject.toml, requirements.txt, .python-version)
- Project structure setup
- Verification commands

---

## Step-by-Step Initialization Commands

### Step 1: Install UV (if not already installed)

**Command:**
```bash
pip install uv
```

**Verification:**
```bash
uv --version
```

**Expected Output:**
```
uv 0.x.x (Rust implementation)
```

---

### Step 2: Initialize Project with Python 3.13

**Command:**
```bash
uv init --python 3.13
```

**What this does:**
- Creates project structure
- Initializes `pyproject.toml` with Python 3.13 requirement
- Creates `.python-version` file with version 3.13
- Creates `src/` directory for source code
- Creates `.gitignore` file
- Initializes basic project configuration

**Expected Output:**
```
Initialized project in current directory
```

**Files Created:**
```
project-root/
├── .python-version          # Python version marker
├── .gitignore               # Git ignore rules
├── pyproject.toml           # Project configuration
├── src/
│   └── __init__.py          # Package marker
└── README.md                # Basic README (optional)
```

---

### Step 3: Create Virtual Environment

**Command:**
```bash
uv venv
```

**What this does:**
- Creates isolated Python environment in `.venv` directory
- Installs Python 3.13 in the environment
- Prepares environment for dependency installation
- Enables reproducible development setup

**Expected Output:**
```
Using Python 3.13.x
Creating virtual environment at .venv
```

**Verification:**
```bash
# On Linux/macOS
ls -la .venv/

# On Windows
dir .venv
```

---

### Step 4: Activate Virtual Environment

**Linux/macOS:**
```bash
source .venv/bin/activate
```

**Windows (Command Prompt):**
```bash
.venv\Scripts\activate.bat
```

**Windows (PowerShell):**
```bash
.venv\Scripts\Activate.ps1
```

**Expected Output:**
```
(.venv) $
```

The `(.venv)` prefix indicates virtual environment is active.

---

### Step 5: Sync Dependencies (if any)

**Command:**
```bash
uv sync
```

**What this does:**
- Installs all dependencies from `pyproject.toml`
- Creates lock file (`uv.lock`) for reproducible installs
- In Phase I: installs no external dependencies (standard library only)

**Expected Output:**
```
Resolved 0 packages in Xs
Installed 0 packages in Xs
```

---

### Step 6: Create Project Directories

**Commands:**
```bash
mkdir -p src tests
```

**Structure After:**
```
project-root/
├── .venv/                   # Virtual environment (created by uv venv)
├── src/
│   └── main.py             # Application entry point
├── tests/
│   └── test_main.py        # Test suite
├── .python-version         # Python version (created by uv init)
├── .gitignore              # Git ignore rules (created by uv init)
├── pyproject.toml          # Project configuration (created by uv init)
├── uv.lock                 # Lock file (created by uv sync)
└── README.md               # Project documentation
```

---

### Step 7: Verify Installation

**Check Python Version:**
```bash
python --version
```

**Expected Output:**
```
Python 3.13.x
```

**Check UV Version:**
```bash
uv --version
```

**Expected Output:**
```
uv 0.x.x
```

**Check Virtual Environment:**
```bash
# Should show .venv path
which python

# Windows:
where python
```

**Expected Output:**
```
/path/to/project/.venv/bin/python
```

---

## Configuration Files

### pyproject.toml (Created by uv init)

```toml
[project]
name = "todo-app"
version = "0.1.0"
description = "A Python-based command-line task management application"
readme = "README.md"
requires-python = ">=3.13"
authors = [
    {name = "Your Name", email = "your.email@example.com"}
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.uv]
python-version = "3.13"
```

**Key Sections:**
- **[project]** - Project metadata
- **[build-system]** - Build configuration
- **[tool.uv]** - UV-specific settings
- **requires-python** - Minimum Python version (3.13+)

---

### .python-version (Created by uv init)

```
3.13
```

**Purpose:**
- Tells UV which Python version to use
- Used by version managers (pyenv, asdf)
- Ensures consistent Python version across team

---

### requirements.txt (Manual - Optional for compatibility)

```
# Todo App Phase I Requirements
# Python 3.13+

# Core dependencies: None
# This project uses only Python standard library

# Development dependencies (optional)
# pytest>=7.0          # For testing (if added)
# black               # For code formatting (if added)
# flake8              # For linting (if added)

# Future dependencies (Phase II and beyond)
# sqlite3             # Database (built-in, no install needed)
# flask               # Web framework (if added)
# requests            # HTTP library (if added)
```

**Usage:**
```bash
# Generate requirements.txt from pyproject.toml
uv pip compile pyproject.toml > requirements.txt

# Install from requirements.txt
uv pip install -r requirements.txt
```

---

## Complete Initialization Workflow

### Quick Start (Copy-Paste Commands)

```bash
# 1. Navigate to project directory (or create it)
mkdir todo-app-phase-1
cd todo-app-phase-1

# 2. Install UV (if needed)
pip install uv

# 3. Initialize project with Python 3.13
uv init --python 3.13

# 4. Create virtual environment
uv venv

# 5. Activate virtual environment
# Linux/macOS:
source .venv/bin/activate
# OR Windows Command Prompt:
# .venv\Scripts\activate.bat
# OR Windows PowerShell:
# .venv\Scripts\Activate.ps1

# 6. Sync dependencies
uv sync

# 7. Create project directories
mkdir -p src tests

# 8. Create main application file
touch src/main.py

# 9. Create test file
touch tests/test_main.py

# 10. Verify installation
python --version
uv --version
```

---

## Project Structure After Initialization

```
todo-app-phase-1/
├── .venv/
│   ├── bin/                 # Executable scripts
│   ├── lib/                 # Python packages
│   └── pyvenv.cfg           # Virtual environment config
├── src/
│   ├── __init__.py          # Package marker
│   └── main.py              # Application entry point (create manually)
├── tests/
│   └── test_main.py         # Test suite (create manually)
├── .python-version          # Python version marker (3.13)
├── .gitignore               # Git ignore rules
├── pyproject.toml           # Project configuration
├── uv.lock                  # Dependency lock file
└── README.md                # Project documentation
```

---

## Configuration File Templates

### src/main.py (Create manually after uv init)

```python
#!/usr/bin/env python3
"""
Todo App Phase I - Main Application

A command-line task management application with in-memory storage.
"""

def main():
    """Main application entry point."""
    print("Todo App Phase I")
    print("Application initialized successfully!")

if __name__ == "__main__":
    main()
```

**Test Run:**
```bash
python src/main.py
```

**Expected Output:**
```
Todo App Phase I
Application initialized successfully!
```

---

### tests/test_main.py (Create manually after uv init)

```python
"""
Test suite for Todo App Phase I

Run tests with: python -m pytest tests/
"""

import sys
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))


def test_application_imports():
    """Test that main module can be imported."""
    try:
        import main  # noqa: F401
        assert True
    except ImportError:
        assert False, "Failed to import main module"


def test_placeholder():
    """Placeholder test."""
    assert True


if __name__ == "__main__":
    print("Run tests with: python -m pytest tests/")
```

**Test Run:**
```bash
# With pytest (if available)
python -m pytest tests/ -v

# Or run directly
python tests/test_main.py
```

---

## Common UV Commands Reference

### Project Management

```bash
# Initialize new project
uv init --python 3.13

# Create virtual environment
uv venv

# Activate virtual environment (Linux/macOS)
source .venv/bin/activate

# Deactivate virtual environment
deactivate

# Sync dependencies from pyproject.toml
uv sync

# List installed packages
uv pip list

# Update all packages
uv pip install --upgrade
```

### Dependency Management

```bash
# Add new dependency
uv add package-name

# Add development dependency
uv add --dev package-name

# Remove dependency
uv remove package-name

# Update dependencies
uv pip install --upgrade

# Create lock file
uv lock

# Export requirements
uv pip compile pyproject.toml > requirements.txt
```

### Project Information

```bash
# Show project info
uv project info

# Show Python info
python --version
uv --version

# Show virtual environment path
which python  # Linux/macOS
where python  # Windows
```

---

## Troubleshooting Initialization

### Issue: UV Command Not Found

**Solution:**
```bash
pip install uv
uv --version
```

**Verify Installation:**
```bash
which uv      # Linux/macOS
where uv      # Windows
```

---

### Issue: Python 3.13 Not Available

**Check Available Versions:**
```bash
uv python list
```

**Install Python 3.13:**
```bash
uv python install 3.13
```

**Fallback to Python 3.12:**
```bash
uv init --python 3.12
```

---

### Issue: Virtual Environment Won't Activate

**Linux/macOS - Check Permissions:**
```bash
chmod +x .venv/bin/activate
source .venv/bin/activate
```

**Windows - Try PowerShell:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.venv\Scripts\Activate.ps1
```

---

### Issue: Dependency Installation Fails

**Clear Cache and Retry:**
```bash
uv pip cache purge
uv sync
```

**Check for Conflicts:**
```bash
uv pip compile pyproject.toml
```

---

## Dependency Management for Phase I

### Current (Phase I)

**No external dependencies** - Uses only Python standard library

```toml
[project]
requires-python = ">=3.13"
dependencies = []  # Empty - standard library only
```

**Why:**
- Simple, focused application
- Minimal complexity
- No dependency management needed
- Easier testing and maintenance
- Faster startup time

---

### Future (Phase II)

**Potential dependencies to add later:**

```bash
# Database
uv add sqlite3  # Built-in, no install needed

# Testing
uv add --dev pytest
uv add --dev pytest-cov

# Code Quality
uv add --dev black
uv add --dev flake8
uv add --dev mypy

# Web Framework (if needed)
uv add flask

# Data Processing (if needed)
uv add pandas
```

---

## Post-Initialization Checklist

After running initialization commands:

- [ ] UV installed: `uv --version` works
- [ ] Project initialized: `pyproject.toml` exists
- [ ] `.python-version` set to 3.13
- [ ] Virtual environment created: `.venv/` directory exists
- [ ] Virtual environment activated: `(.venv)` shows in prompt
- [ ] Dependencies synced: `uv sync` completed
- [ ] `src/` directory created
- [ ] `tests/` directory created
- [ ] `src/main.py` created with basic code
- [ ] Application runs: `python src/main.py` works
- [ ] Python version correct: `python --version` shows 3.13
- [ ] `uv.lock` file created
- [ ] Project structure matches specification

---

## Integration with Project Files

After initialization, create additional project files:

```bash
# Copy or create README.md
# See: create-project-file.md skill for full content

# Copy or create CONSTITUTION.md
mkdir -p .specify/memory
# See: create-project-file.md skill for full content

# Copy or create SETUP_GUIDE.md
# See: create-project-file.md skill for full content

# Copy or create FEATURES.md
# See: create-project-file.md skill for full content
```

---

## Environment Variables (Optional)

Create `.env` file for configuration (if needed later):

```bash
# .env (Phase I - not needed)
# Phase II might use:
# DATABASE_URL=sqlite:///tasks.db
# DEBUG=True
# LOG_LEVEL=INFO
```

**Usage:**
```python
import os
from dotenv import load_dotenv

load_dotenv()
debug = os.getenv("DEBUG", "False") == "True"
```

---

## CI/CD Integration

For automated initialization in CI/CD pipelines:

```yaml
# Example GitHub Actions workflow
name: Initialize Project

on: [push, pull_request]

jobs:
  init:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Install UV
        run: pip install uv

      - name: Initialize with UV
        run: |
          uv init --python 3.13
          uv venv
          uv sync

      - name: Run Tests
        run: |
          source .venv/bin/activate
          python -m pytest tests/ -v
```

---

## Docker Integration (Optional)

For containerizing the application:

```dockerfile
# Dockerfile (Phase I)
FROM python:3.13-slim

WORKDIR /app

# Install UV
RUN pip install uv

# Copy project files
COPY . .

# Initialize with UV
RUN uv venv
RUN uv sync

# Run application
CMD ["python", "src/main.py"]
```

---

## Verification Commands

Run these to verify successful initialization:

```bash
# 1. Check virtual environment
source .venv/bin/activate  # Linux/macOS

# 2. Verify Python version
python --version
# Output: Python 3.13.x

# 3. Verify UV version
uv --version
# Output: uv 0.x.x

# 4. List installed packages
uv pip list
# Output: (short list - only built-in packages)

# 5. Show project info
uv project info

# 6. Run application
python src/main.py
# Output: Todo App Phase I
#         Application initialized successfully!

# 7. Check lock file exists
ls uv.lock  # Linux/macOS
dir uv.lock # Windows
```

---

## Deactivation and Cleanup

### Deactivate Virtual Environment

```bash
deactivate
```

The `(.venv)` prefix should disappear from your prompt.

### Remove Virtual Environment (if needed)

```bash
# Linux/macOS
rm -rf .venv

# Windows
rmdir /s .venv
```

### Remove Lock File (if needed)

```bash
# Linux/macOS
rm uv.lock

# Windows
del uv.lock
```

---

## Best Practices

### 1. Always Activate Before Working

```bash
source .venv/bin/activate  # Linux/macOS
# or
.venv\Scripts\activate.bat  # Windows
```

### 2. Keep Dependencies Minimal

- Use standard library when possible
- Only add external dependencies when necessary
- Document why each dependency is needed

### 3. Regular Updates

```bash
# Update UV itself
pip install --upgrade uv

# Update dependencies
uv pip install --upgrade
```

### 4. Version Control

```bash
# Commit these files:
# - pyproject.toml (project config)
# - uv.lock (lock file)
# - .python-version (version marker)

# Do NOT commit:
# - .venv/ (virtual environment)
# - __pycache__/ (bytecode)
# - *.pyc files
```

### 5. Team Consistency

- Share `.python-version` file
- Share `pyproject.toml` file
- Share `uv.lock` file
- All team members use same setup commands

---

## Complete Initialization Script

**init_project.sh (Linux/macOS):**

```bash
#!/bin/bash

set -e  # Exit on error

echo "=== Todo App Phase I Project Initialization ==="
echo ""

# 1. Install UV
echo "1. Installing UV package manager..."
pip install uv
echo "   ✓ UV installed"
echo ""

# 2. Initialize project
echo "2. Initializing project with Python 3.13..."
uv init --python 3.13
echo "   ✓ Project initialized"
echo ""

# 3. Create virtual environment
echo "3. Creating virtual environment..."
uv venv
echo "   ✓ Virtual environment created"
echo ""

# 4. Sync dependencies
echo "4. Syncing dependencies..."
uv sync
echo "   ✓ Dependencies synced"
echo ""

# 5. Create directories
echo "5. Creating project directories..."
mkdir -p src tests
echo "   ✓ Directories created"
echo ""

# 6. Verify
echo "6. Verifying installation..."
echo "   Python version: $(python --version)"
echo "   UV version: $(uv --version)"
echo ""

echo "=== Initialization Complete ==="
echo ""
echo "Next steps:"
echo "1. Activate virtual environment: source .venv/bin/activate"
echo "2. Create src/main.py with your application code"
echo "3. Create tests/test_main.py with your tests"
echo "4. Run: python src/main.py"
```

**init_project.bat (Windows):**

```batch
@echo off
setlocal enabledelayedexpansion

echo === Todo App Phase I Project Initialization ===
echo.

REM 1. Install UV
echo 1. Installing UV package manager...
pip install uv
echo    X UV installed
echo.

REM 2. Initialize project
echo 2. Initializing project with Python 3.13...
uv init --python 3.13
echo    X Project initialized
echo.

REM 3. Create virtual environment
echo 3. Creating virtual environment...
uv venv
echo    X Virtual environment created
echo.

REM 4. Sync dependencies
echo 4. Syncing dependencies...
uv sync
echo    X Dependencies synced
echo.

REM 5. Create directories
echo 5. Creating project directories...
if not exist src mkdir src
if not exist tests mkdir tests
echo    X Directories created
echo.

REM 6. Verify
echo 6. Verifying installation...
python --version
uv --version
echo.

echo === Initialization Complete ===
echo.
echo Next steps:
echo 1. Activate virtual environment: .venv\Scripts\activate.bat
echo 2. Create src\main.py with your application code
echo 3. Create tests\test_main.py with your tests
echo 4. Run: python src\main.py

pause
```

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-12-28 | Initial skill document; complete UV initialization guide |

---

