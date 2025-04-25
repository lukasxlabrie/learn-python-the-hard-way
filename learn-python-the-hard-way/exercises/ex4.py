#vars defined as numbers
cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90

#takes the above vars and makes them interact
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers/cars_driven

#uses the vars and interactions (also vars) to print
#use , to add car to string
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can trasnport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car")