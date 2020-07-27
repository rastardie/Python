# map(func, iterables)

def new(a):
    return a*a
x = map(new,[1,2,3,4])
print(x)
print(tuple(x))

print("----------")

def newer(a,b):
    return a*b
x = map(newer,[1,2,3,4],[2,3,4,5])
print(x)
print(tuple(x))