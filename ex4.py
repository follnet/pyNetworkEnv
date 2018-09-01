cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
# dadad


print('there are %s cars available' % (cars))
print('there are only', drivers, 'drivers available')
print('there will be', cars_not_driven, 'drivers available')
print('We can transport', carpool_capacity, 'people today')
