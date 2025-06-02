
## Use Cases

This script is a basic file copier. It's useful for:

* Copying contents from one file to another via the command line.
* Demonstrating file I/O (input/output) in Python.
* Practicing use of system arguments, file handling, and basic validation.

Example usage:
python script.py source.txt destination.txt

---

## Syntax and Key Concepts

from sys import argv

* Purpose: Access command-line arguments.
* argv is a list: argv\[0] is the script name, and argv\[1:] are user-provided arguments.

from os.path import exists

* Purpose: Checks if a file path exists.
* exists('filename.txt') returns True or False.

script, from\_file, to\_file = argv

* Unpacks the argv list.
* script: the script’s filename.
* from\_file: source file path.
* to\_file: destination file path.

open(from\_file)

* Opens the source file in read mode by default.
* Returns a file object.

indata = in\_file.read()

* Reads entire contents of the file into the string indata.

len(indata)

* Returns the number of bytes (characters) in indata.

exists(to\_file)

* Checks whether the destination file already exists.
* Useful for preventing accidental overwrites.

input()

* Pauses program until user hits ENTER.
* Useful for letting the user cancel (CTRL+C) or confirm.

open(to\_file, 'w')

* Opens destination file in write mode.
* If the file exists, it will be overwritten. If not, it will be created.

out\_file.write(indata)

* Writes the contents from the source file to the destination file.

out\_file.close() and in\_file.close()

* Closes both files.
* Always close files to avoid memory/resource leaks.

---

## Definitions

| Term         | Definition                                              |
| ------------ | ------------------------------------------------------- |
| argv         | List of command-line arguments                          |
| exists(path) | Function that returns True if the path exists           |
| open()       | Opens a file; mode can be 'r' (read), 'w' (write), etc. |
| read()       | Reads file contents into memory                         |
| write()      | Writes data to file                                     |
| close()      | Properly closes the file object                         |


