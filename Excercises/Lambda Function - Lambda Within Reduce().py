#reduce Syntax: reduce(function,sequence)

from functools import reduce # or import functools or from functools import *
a = reduce(lambda a,b: a+b,[23,56,43,98,1]) #adds teh sequence recursively
print(a)

