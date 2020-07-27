from matplotlib import pyplot as plt
from matplotlib import style


style.use('ggplot')

x = [5,8,10]
y = [12,16,6]

x2 = [6,9,11]
y2 = [6,15,7]

plt.plot(x,y,'g',label='line one',linewidth=5)      #g for color green
plt.plot(x2,y2,'c',label='line two',linewidth=5)

#Title and label the the axis
plt.title("Epic Info")
plt.ylabel('Y axis')
plt.xlabel('x axis')

plt.legend()
plt.grid(True,color='k')       #show grid lines with black color

plt.show()