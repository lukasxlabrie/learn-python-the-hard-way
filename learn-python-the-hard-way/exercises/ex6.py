types_of_people = 10  # defines variable as integer 10
x = f"There are {types_of_people} types of people."  # defines x as an f-string that includes types_of_people

binary = "binary"  # defines variable as string
do_not = "don't"   # defines variable as string

y = f"Those who know {binary} and those who {do_not}."  # defines y as an f-string using binary and do_not

print(x)  # prints the value of x
print(y)  # prints the value of y

print(f"I said: {x}")  # prints an f-string that includes the string x
print(f"I also said: '{y}'.")  # prints an f-string that includes y, wrapped in single quotes

hilarious = False  # defines a Boolean value (True or False)
joke_evaluation = "Isn't that joke so funny?! {}"  # a string with a placeholder {} to be filled in later

print(joke_evaluation.format(hilarious))  # formats joke_evaluation by replacing {} with the value of hilarious

w = "This is the left side of..."  # string assigned to w
e = "a string with a right side."  # string assigned to e

print(w + e)  # concatenates w and e and prints them together on one line
