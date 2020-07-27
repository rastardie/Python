#Looping over a file object
import os
file = open("C:/Users/Kay/Desktop/Test.txt", 'w')
for line in file:
    print(file.readline())
file.close()