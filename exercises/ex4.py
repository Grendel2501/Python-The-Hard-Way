# define the cars variable, set it to a value of 100
cars = 100
# define the space_in_a_car variable, set it to a value of 4.0
space_in_a_car = 4.0
# define the , set it to a value of 30
drivers = 30
# define the , set it to a value of 90
passengers = 90
# define the cars_not_driven variable, set it equal to the value of cars less the value of drivers, or 100 - 30 = 70
cars_not_driven = cars - drivers
# define the cars_driven variable, set it equal to to the drivers variable, or 30
cars_driven = drivers
# define the carpool_capacity variable, set it equal to the number of cars_driven multiplied by the number of space_in_a_car (seats), or 120 
carpool_capacity = cars_driven * space_in_a_car
# define the average_passengers_per_car variable, ser it equal to the number of passengers divided by the number of cars_driven, or 3
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."