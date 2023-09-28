intro = "Hello World"
print(intro)

first_name = input("What is your first name?  ")
print(first_name)

age = 87
temperature = 98.7
too_hot = False

print(type(age))
print(type(temperature))
print(type(too_hot))

addition = age + temperature
subraction = age - temperature
multiplication = age * temperature
division = age / temperature
square = age ** temperature
print(addition)
print(subraction)
print(multiplication)
print(division)
print(square)

print(intro + first_name)
print(f"{intro} {first_name}")

def calculate_area(length, width):
    return length * width