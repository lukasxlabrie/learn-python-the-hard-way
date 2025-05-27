# takes input to assign to variable
from sys import argv

# variables will be the script and a filename
script, filename = argv

# prints strings and explains that we're erasing filename; placeholder, need to use actual file name
print(f"We're going to erase {filename}.")

# how to cancel
print("If you don't want that, hit CTRL-C (^C)")

# how to confirm
print("If you do want that, hit RETURN.")

# asks user to cancel/confirm
input("?")

print("Opening the file...")

# will open file in write mode ('w')
target = open(filename, 'w')

# clears file
print("Truncating the file. Goodbye.")
target.truncate()

# takes input and saves as variables
print("Now I'm going to ask you for three lines")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# adds variables to file, each on a new line
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")

# closes and saves file
target.close()