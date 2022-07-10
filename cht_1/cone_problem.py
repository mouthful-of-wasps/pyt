import math
#print('Welcome, type the Radius of the cone')
radius = input()
#print('Next type the Height of the cone')
height = input()

mass_of_cone = (math.pi * int(radius) ** 2 * int(height)) / 3

print(mass_of_cone)