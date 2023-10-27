# How import works in python.

# import whole module
import math

# import specific function from module
from math import sqrt, floor

# import all functions from module
# from math import *

# we also have "as" keyword for short names
# import math as m 

a = 1000.00011
# c = math.floor(a) # when we import whole module
c = floor(a)  # when we import specific function
print(c)


# dir() method
# print all the function name that module contains
# print(dir(math))
for i in dir(math):
    print(i)

# importing user defined module jay
from jay import welcome,jay
welcome()
print(jay)