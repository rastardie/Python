#reduce applies a given a function to the iterables and returns and single value

#syntax: reduce(function, iterable)
from functools import reduce
def a(x,y):
    return x + y
s = reduce(a,[1,3,4,5,6,7,7,8,8])
print(s)

