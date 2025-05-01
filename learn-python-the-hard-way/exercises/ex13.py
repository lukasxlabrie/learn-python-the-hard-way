# this tells the program that we will be using argv, which is on my sysyem later in the program
from sys import argv

# argv has 4 variables, assigned left to rightß
script, first, second, third = argv

# prints that use whats stored in argv 
print ("This script is called:", script)
print ("Your first variable is:", first)
print ("Your second variable is:", second)
print ("Your third variable is:", third)