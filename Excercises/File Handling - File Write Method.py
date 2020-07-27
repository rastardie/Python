#File Handling Example 1 - Writing

import os
file = open("C:/Users/Kay/Desktop/Test.txt", 'w')
file.write("Hello World")
file.write("Hello World again?")
file.close()

print("-------------------")

import os
file = open("C:/Users/Kay/Desktop/Test.txt", 'w')
file.write("Oops overwritten")
file.close()

print("-------------------")

import os
file = open("C:/Users/Kay/Desktop/Test.txt", 'w')
file.write("New File")
file.close()

print("-------------------")

