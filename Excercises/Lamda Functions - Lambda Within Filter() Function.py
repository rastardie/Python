mylist=[1,2,3,4,5,6]

#Syntax: filter(function,iterables)
newlist=list(filter(lambda a:(a/3!=2),mylist)) #check mylist and return all elements that satisfy a/3!=2
print(newlist)