def new1(i):
    if i>=3:
        return 1
j = filter(new1,(1,2,3,4,5,6,7))
print(j)
print(tuple(j))

print("----------")

z = filter(lambda x: (x>=3),(1,2,3,4,5,6,7))
print(list(z))