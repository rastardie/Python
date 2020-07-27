import os
file = open("C:/Users/Kay/Desktop/Test.txt", 'w')
file.close()

print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

file = open("C:/Users/Kay/Desktop/Test.txt", 'r')
print(file.read())
file.close()

print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")



file = open("C:/Users/Kay/Desktop/Test.txt", 'r')
print(file.read(5))
file.close()

print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

