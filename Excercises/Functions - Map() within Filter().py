a = map(lambda x: x+x,[1,2,3,4,5,6])
print(tuple(a))
print("-------------")

d = filter(lambda x:(x>=4),map(lambda x:x+x,[1,2,3,4,5,6]))
print(set(d))