# string with 4 placeholders
formatter = "{} {} {} {}"

# each line tells the prgam to print formatter but fill in the placeholders with whats between the ()
# each .format must have 4 vars to fill in the placeholders
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))

# this approch makes it easier to read whats happening
print (formatter.format(
    "Writting code like this",
    "Makes the program easier to read",
    "I think its common practice for loops and in Javascript",
    "I am not sure if it's nomral for Python coding"
))