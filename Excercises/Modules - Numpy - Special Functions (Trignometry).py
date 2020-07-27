import numpy as np
import matplotlib.pyplot as plt

#Plot x and y (Trignometric)
x = np.arange(0,3*np.pi, 0.1)
y = np.sin(x)
plt.plot(x,y)
plt.show()
print("----------------------")

x = np.arange(0,3*np.pi, 0.1)
y = np.cos(x)
plt.plot(x,y)
plt.show()
print("----------------------")

x = np.arange(0,3*np.pi, 0.1)
y = np.tan(x)
plt.plot(x,y)
plt.show()