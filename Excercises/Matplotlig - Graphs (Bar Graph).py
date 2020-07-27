import matplotlib.pyplot as plt

#Bar Graph1 x,y data
plt.bar([1,3,5,7,9],[5,2,7,8,2], label='Example One')

#Bar Graph2 x,y data
plt.bar([2,4,6,8,10],[8,6,2,5,6], label='Example Two', color='g')

#Display lengend and labels
plt.legend()
plt.xlabel('bar number')
plt.ylabel('bar height')

#Title of graph
plt.title('My plot yo!')

#display the chart
plt.show()