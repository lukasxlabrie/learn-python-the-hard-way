
**Modules and Imports**

- A **module** is a file with Python code (functions, classes, variables).
- Use `import module_name` to bring in an entire module (e.g., `import sys`).
- Use `from module_name import name1, name2` to import only specific parts (e.g., `from sys import argv`).

**Command-Line Arguments (`argv`)**

- `argv` is a list of strings representing what you type after `python script.py`.
  - `argv[0]` — script name (e.g., `script.py`)
  - `argv[1]` — first argument (e.g., `apple`)
  - `argv[2]` — second argument (e.g., `banana`)
  - `argv[3]` — third argument (e.g., `cherry`)
- You must supply exactly three arguments for `script, first, second, third = argv` to work without errors.

**Script Execution**

- Python reads and executes code from top to bottom.
- By placing `print` statements immediately, you see results right after unpacking `argv`.