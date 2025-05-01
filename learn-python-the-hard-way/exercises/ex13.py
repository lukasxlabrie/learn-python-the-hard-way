# How to run this script (in your terminal):
#   python script.py first second third
# Example:
#   python script.py apple banana cherry
# Notice: Do NOT type angle brackets `< >`—they just show placeholders.
# This sets:
#   first  = "apple"
#   second = "banana"
#   third  = "cherry"

from sys import argv  # Import only 'argv' from Python’s built-in 'sys' module

# 'argv' holds the list of words you type after 'python script.py':
#   argv[0] -> script name (script.py)
#   argv[1] -> first word you type (apple)
#   argv[2] -> second word (banana)
#   argv[3] -> third word (cherry)
script, first, second, third = argv

# Print each item right away
print("Script name:", script)
print("First argument:", first)
print("Second argument:", second)
print("Third argument:", third)

# Prompt the user for additional input
# The 'end' parameter avoids adding a new line after the prompt
answer = input("Type anything: ", end=' ')
print("You typed:", answer)