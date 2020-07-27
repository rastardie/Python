from functools import reduce

a = reduce(lambda q,p: q*p, [1,2,3,4,5,6,7,7])
print(a)