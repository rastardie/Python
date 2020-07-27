from matplotlib import pyplot as plt


#Plotting the x and y-axis values to a canvas
x = [5,8,10]
y = [12,16,6]

plt.plot(x,y)

#Title and label the the axis
plt.title("Info")
plt.ylabel('Y axis')
plt.xlabel('x axis')

plt.show()