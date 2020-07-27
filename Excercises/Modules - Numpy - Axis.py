import numpy as np

#Axis (Note: rows are axis 1 and columns are axis 0)
a = np.array([(1,2,3), (3,4,5)])
print(a.sum(axis=0))  #add the element (0.1 + 1.1... ie 1+3, 3+4,3+5)
print(a.sum(axis=1))  #add row elements
print("-----------------------------------")

#Print square root and Standard deviation
print(np.sqrt(a))
print(np.std(a))

