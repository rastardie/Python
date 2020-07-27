import os
file = open("C:/Users/Kay/Desktop/Test.txt", 'r')
print(file.readline()) #Readline
file.close()

print("$$$$$$$$$$$$$$$$$$$$"'\n')

import os
file = open("C:/Users/Kay/Desktop/Test.txt", 'r')
print(file.readlines())  #Readlines
file.close()
