Strings are usually exported from a program and meant to be read by someone.
Common practice is to use short abbreviations for variable names to keep the code cleaner.

To insert a variable into a printed string, you need to use f to create an f-string.
Example:
print(f"Like this {printThisToo} to make an f-string.")

There is also a .format() method, which will be explained later.
It is used to borrow an existing string format and insert values dynamically into placeholders.
This is useful when working inside loops or reusing the same template multiple times.
Example:
print("Isn't that funny? {}".format(joke_response))

Boolean values are another important concept.
A boolean is a type that can only be either True or False.
Booleans are often used for logic decisions, but they can also be printed inside strings.
For example, you can create a sentence like "Isn't that joke funny? False" by inserting a boolean into a string using .format().

Strings can also be concatenated (joined together) using the + operator.
When you concatenate two strings, they are combined into one continuous string without adding a new line.
Example:
left = "This is the left side of..."
right = "a string with a right side."
print(left + right)
This will print both strings together on the same line.