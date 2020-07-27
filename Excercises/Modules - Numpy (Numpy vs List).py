import numpy as np
import time
import sys

a = np.array([(1,2,3),(4,5,6)])
print(a)
print("------------------------------------")

#Why use Numpy instead of list?
#Numpy occupies less memeory that list as shown below
s = range(1000)
print(sys.getsizeof(5)*len(s))

D = np.arange(1000)
print(D.size*D.itemsize)
print("------------------------------------")

#Numpy arrays are faster than list
SIZE = 1000

L1 = range(SIZE)
L2 = range(SIZE)

A1 = np.arange(SIZE)
A2 = np.arange(SIZE)

start = time.time()                     #set monitoring time
result = [(x,y) for x,y in zip(L1,L2)]
print((time.time()-start)*9000000000000)

start = time.time()
result = A1+A2
print((time.time()-start)*9000000000000)
