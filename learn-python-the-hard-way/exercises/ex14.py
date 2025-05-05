# Pulls the argument from system input for later use
from sys import argv

# The script will use user_name as the argument variable
script, user_name = argv

# Prompt indicator for user input
prompt = "> "

# Greet the user and display the script name
print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me, {user_name}?")

# Ask for user input on likes
likes = input(prompt)

# Ask where the user lives
print(f"Where do you live, {user_name}?")
lives = input(prompt)

# Ask about the user's computer
print(f"What kind of computer do you use, {user_name}?")
computer = input(prompt)

# Summarize the responses
print(f"""
Alright, so you said '{likes}' about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
