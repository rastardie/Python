#Filter is used to create an output list
#consisting of values for which the function returns True

#Syntax filter(function, iterables)
def new1(i):
    if i>=3:
        return 1
j = filter(new1,(1,2,3,4,5,6,7))
print(j)
print(tuple(j))