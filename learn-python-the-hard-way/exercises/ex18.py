# this one is like your scripts with argv, def is a funciton
# function = mini script 
def print_two(*args):
    arg1,arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can jsut do this
def print_two_again(arg1, arg2):
     print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
     print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
    print("I got nothin'.")

# prints all version sof function
# calls/runs/sues function
print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First")
print_none()