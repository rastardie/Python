import numpy as np

a = np.array([(1,2,3), (3,4,5)])
b = np.array([(1,2,3), (3,4,5)])
print(a+b)
print("-------------------")
print(a-b)
print("-------------------")
print(a*b)
print("-------------------")
print(a/b)
print("-------------------")
print("-------------------")


#stacking
a = np.array([(1,2,3), (4,5,6)])
b = np.array([(7,8,9), (10,11,12)])
print(np.vstack((a,b)))  #Vertical Stacking
print("-------------------")
print(np.hstack((a,b)))  #Horizontal Stacking
print("-------------------")
print(np.hstack((a,b)))  #Horizontal Stacking
print(a.ravel())         #convert a to a single row
