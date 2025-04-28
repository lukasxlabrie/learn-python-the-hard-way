name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

weightConvrsn = round(weight * 0.45359237, 1)
heightConvrsn = round(height * 2.54, 1)

print (f"Let's talk about {name}.")
print (f"He's {height} inches tall.")
print (f"He's {weight} pounds heavy.")
print ("Actually, that's not too heavy.")
print (f"He's got {eyes} eyes and {hair} hair.")
print (f"His teeth are usually {teeth} depending on the coffee")

#this line is tricky try to get it exactly right
total = age + height + weight
print(f"if I add {age}, {height} and {weight}, I get {total}.")

# prints metric versions
print(f"My weight in kilograms is {weightConvrsn} kgs.")
print(f"My height in centimeters is {heightConvrsn} cm.")