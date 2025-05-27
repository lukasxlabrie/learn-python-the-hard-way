Reading and writing files in Python involves using functions like `open()`, `write()`, `read()`, and `close()` to interact with text files on your system.

The `open()` function is used to access a file. You must specify a mode: `'r'` for reading (default), `'w'` for writing (which erases existing content), `'a'` for appending, or `'r+'` for reading and writing.

The `close()` function closes the file and ensures any changes are saved. It works like clicking "Save and Close" in a text editor.

The `read()` function reads the entire contents of a file and returns it as a string. You can store this string in a variable for processing.

The `readline()` function reads just one line from the file at a time. If called repeatedly, it moves line by line through the file.

The `write()` function writes a string to the file. It does not automatically include line breaks, so you need to add `\n` manually if needed.

The `truncate()` function clears the entire contents of a file. This is not reversible, so use it with caution.

The `seek()` function moves the read/write pointer within the file. Using `seek(0)` moves it back to the beginning.

The `from sys import argv` statement lets you grab command-line arguments when you run your script. In this case, it pulls the script name and filename.

The `input()` function shows a prompt and waits for the user to type something. It always returns a string. For example: `age = input("How old are you? ")`.

In this script, `input()` is used to collect three lines from the user and write them to the file.

Writing multiple lines means collecting input with `input()` and writing each one to the file using `write()`. You need to manually insert newlines if you want each line to appear separately.

Opening a file in `'w'` mode will erase its contents immediately. This is useful when you want to replace everything, but be careful not to overwrite something important by mistake.

To access documentation on any Python function (like `input`, `open`, or `write`) using pydoc on Mac, type: `python3 -m pydoc input`.

Pydoc is a built-in Python tool that shows documentation for modules, classes, and functions directly in your terminal. It works with built-in Python features like `math`, `str`, and `input`, and also with your own scripts if they are in your current directory or Python path.
