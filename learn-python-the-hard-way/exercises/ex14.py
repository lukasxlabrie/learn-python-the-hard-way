# Pulls the argument for user_name from command-line
from sys import argv

# Unpack script name and user-provided name (run as: python ex14.py Gretchen)
script, user_name, age = argv

# Prompt indicator for user input
prompt = ">"

# Greet and ask questions
print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")

# Ask if they like the script
print(f"Do you like me, {user_name}?")
likes = input(prompt)

# Ask where they live
print(f"Where do you live, {user_name}?")
lives = input(prompt)

# Ask about their computer
print(f"What kind of computer do you use, {user_name}?")
computer = input(prompt)

# Summarize the answers
print(f"""
Alright, you said '{likes}' about liking me.
You live in {lives}. Not sure where that is.
You are {age} years old? 
And you have a {computer} computer. Nice.
""")