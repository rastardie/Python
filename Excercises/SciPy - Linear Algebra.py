#Finding the Inverse of a Matrix

from scipy import linalg
import numpy as np

a = np.array([[1,2],[3,4]])
b = linalg.inv(a)
print(b)
