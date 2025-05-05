# Pulls the argument from system input for later use
from sys import argv

# The script will use user_name as the argument variable
script_name, user_name = argv

# Prompt indicator for user input
prompt = "> "

# Greet the user and explain the script
print(f"Hi {user_name}, I'm the {script_name} script.")
print("I'd like to ask you a few questions.")

# Ask if the user likes the script
print(f"Do you like me, {user_name}?")
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
