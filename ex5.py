my_name = 'Zed A. Shaw'
my_age = 35
my_height = 74
my_weight = 180
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f'Let\'s talk about {my_name}.')
print("He's %s inches tall." %(my_height))
print("He's {} pounds heavy.".format(my_weight))

total = my_age + my_height + my_weight
print("if i had %s,%s and %s I get %s." %(my_age,my_height,my_weight,total))
print("if i had {},{} and {} I get {}.".format(my_age,my_height,my_weight,total))

print('round(80.23456): ', round(80.23456,4))
