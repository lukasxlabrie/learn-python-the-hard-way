Notes: cheese_and_crackers Function

Use Case:

This script defines a function that accepts two arguments and uses them to print a party message. It demonstrates different ways to pass arguments to functions in Python: direct numbers, variables, math expressions, and combinations.

Function Definition:

def cheese_and_crackers(cheese_count, boxes_of_crackers):

This defines a function named cheese_and_crackers that takes two inputs. Inside the function, it prints messages using those inputs.

Function Body:

print(f"You have {cheese_count} cheeses!")
print(f"You have {boxes_of_crackers} boxes of crackers!")
print("Man that's enough for a party!")
print("Get a blanket.\n")

This block outputs the current values passed into the function along with some static text.

Function Calls:

1. Direct values:

cheese_and_crackers(20, 30)

Passes 20 and 30 directly as arguments.

2. Variables:

amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

Uses variables to store values and passes them into the function.

3. Math expressions:

cheese_and_crackers(10 + 20, 5 + 6)

Performs math in the function call before passing the results.

4. Variables with math:

cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

Combines variables with math for more dynamic inputs.

Definitions:

def - keyword to define a function
function - a named block of reusable code
arguments - values passed into a function
print() - built-in function to display output
f-string - a formatted string that allows variable values to be inserted

Summary:

This example shows how to define a function with two parameters and how to call it in different ways. Using functions helps keep code organized, reusable, and readable.
