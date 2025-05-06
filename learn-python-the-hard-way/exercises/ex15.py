# Import argv from the sys module to accept command-line arguments
from sys import argv

# Unpack command-line arguments into script name and filename variables
script, filename = argv

# Open the file provided as the command-line argument and assign it to variable 'txt'
txt = open(filename)

# Print a message showing which file is being read
print(f"Here's your file {filename}:")

# Read and print the contents of the file
print(txt.read())

# Prompt the user to type the filename again
print("Type the filename again:")

# Take user input and store it in the variable 'file_again'
file_again = input("> ")

# Open the file entered by the user
txt_again = open(file_again)

# Read and print the contents of the newly opened file
print(txt_again.read())