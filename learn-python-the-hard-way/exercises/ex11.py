# prints the string and stays on the same line (does not add a newline)
print ("How old are you?", end=' ')

# prompts the user for input and stores it in a variable
age = input()
print ("How tall are you?", end=' ')
height = input()
print ("How much do you weigh?", end=' ')
weight = input()

# f-string that inserts the user’s input (stored in variables) into the sentence
print (f"So, you're {age} old, {height} tall, and {weight} heavy.")