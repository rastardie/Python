def new(dict):
    for x,y in dict.items():
        yield x,y
a={1:"Hi", 2:"Welcome"}

b = new(a)  #assign the generator to a variable
print(b)
print(next(b))    #call the generator to yield the first key value pair
print(next(b))    #calling it again will yield the next key value pair
#print(next(b))    #a third call will cause and error

print("----------")

def myfunc(i):
    while i<=3:
        yield i
        i+=1
j=myfunc(2)
print(next(j))
print(next(j))
#print(next(j))    #a third call will cause and error

print("----------")

def ex():
    n=3
    yield n
    n=n*n
    yield n
v=ex()
print(v)
print(next(v))
print(next(v))