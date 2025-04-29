The comma separates arguments to print().
Python automatically adds a space between each argument.
It converts non-strings to strings for you (e.g., numbers, booleans)

Example:
print("Hello", 123, True)
Output
Hello 123 True


An f-string is a string that starts with f or F.
You can embed variables or expressions directly inside {}.
It’s great for building a single formatted string.

x = 5
y = 10
print(f"The sum of {x} and {y} is {x + y}")

Output:
The sum of 5 and 10 is 15