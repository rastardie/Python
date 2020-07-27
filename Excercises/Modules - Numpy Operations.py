import numpy as np


a = np.array([(1,2,3), (2,3,4)])
print(a.ndim)       #Find dimentions of an array
print(a.itemsize)   # Find the byte size of each element
print(a.dtype)      # Find data types of the elements
print(a.size)       # Find size
print((a.shape))    # Find shape

#Reshape

b = np.array([(1,2,3,4),(3,4,5,6)])
print(b)
print("--------------")
b = b.reshape(4,2)
print(b)

#Slicing

b = np.array([(1,2,3,4),(3,4,5,6), (7,8,9,10)])
print(b[0,2])       #Find third index from the first element
print(b[0:,3])      #Find third index  from all rows
print(b[0:2,3])    #Find third index from range 0th to 1st element
print("--------------")

#Print 5 values equally spaced between 1 and 3
a = np.linspace(1,3,5)
print(a)
print("--------------")

#min, max, sum
a = np.array([1,2,3])
print(a.min())
print(a.max())
print(a.sum())
