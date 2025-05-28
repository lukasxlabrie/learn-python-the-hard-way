# Yeah baby! This script is gonna capture your mojo-filled day!
from sys import argv

# Unpack the script name and the filename from command line arguments
script, filename = argv

# Just a cgreeting to set the mood
print("It's time to talk about your day, baby! Yeah!")

# Ask about your groovy feelings
mood = input("How are you feeling, baby? (e.g., shagadelic, bummed out, totally fab): ")
print("Smashing! That's the spirit!")

# Ask about today's far-out adventures
shindigs = input("And tell me baby, what kind of groovy shindigs did you find your way into today? ")
print("Groovy baby! Right on!")

# Ask about your randy status
randy = input("Tell me baby... are you feeling randy today? (yes/no): ")
print("Oh behave!")

# Open the file in write mode 
target = open(filename, 'w')

# header
target.write("=== Austin Powers Daily Mojo Log ===\n")

# add variables to txt file
target.write(f"Mood: {mood}\n")
target.write(f"Shindigs: {shindigs}\n")
target.write(f"Feelin' Randy?: {randy}\n")
target.close()

# mojo logged
print(f"Your mojo's been logged in '{filename}', baby! Yeah!")
