#Generator  generates all the waves one at a time

import numpy as np
from matplotlib import pyplot as plt
import seaborn as sb

def s(flip = 2):
    x = np.linspace(0,14,100)
    for i in range(1,10):
        yield(plt.plot(x,np.sin(x + i *.5) * (7-i) * flip))

sb.set()
s=s()
plt.show()

print(next(s))
print(next(s))