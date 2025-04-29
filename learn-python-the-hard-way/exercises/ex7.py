print("Mary had a little lamb.") #prints a string
print("Its fleece was white as {}.".format('snow')) # prints a string and uses .format to insert snow, {} is placeholder and uses () to fill the place
print ("and everywhere that Mary went.") # prints a string
print("." * 10) # prints 10 .

# a list of vars which are strings
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# using the end = '' tells the program to avoid starting a new line, can be used to add a custom field or add space as well, see notes doc
print(end1 + end2 + end3 + end4 + end5 + end6, end = '' )
print(end7 + end8 + end9 + end10 + end11 + end12)