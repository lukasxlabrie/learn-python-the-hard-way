# To run this script, type in your terminal:
#   python script.py <first> <second> <third>
# For example:
#   python script.py apple banana cherry
# This means:
#   first  = "apple"
#   second = "banana"
#   third  = "cherry"

from sys import argv # Grab only 'argv' from Python’s built-in 'sys' module so we can read the words you type after the script name

# 'argv' is a list that holds what you type after 'python script.py'
#   argv[0] is always the script name (script.py)
#   argv[1] is the first word you type
#   argv[2] is the second word
#   argv[3] is the third word
script, first, second, third = argv

# Print out each value directly
print("Script name:", script)
print("First argument:", first)
print("Second argument:", second)
print("Third argument:", third)