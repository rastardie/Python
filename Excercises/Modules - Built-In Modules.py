# type help('modules') in the Python console to get the list of all built-in Python Modules
from matplotlib import pyplot
import mod2
import mod1
import sys
import math
import random
import datetime


print(dir(pyplot)) # present directory list fo strings defined by the pypoot  module
print("-----------------------------")
print(dir(mod2))
print("-----------------------------")
print(dir(mod1))
print("-----------------------------")
print(sys.path)
print("-----------------------------")
print(math.factorial(5))
print("-----------------------------")
print(random.randrange(50))
print("-----------------------------")
print(datetime.date.today())

