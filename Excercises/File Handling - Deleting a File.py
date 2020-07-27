import os

#CREATION
file = open("C:/Users/Kay/Desktop/Edureka.txt", 'x')
file.write("New File - Edureka")
file.close()

file = open("C:/Users/Kay/Desktop/Python.txt", 'x')
file.write("New File - Python")
file.close()

os.mkdir("C:/Users/Kay/Desktop/Edureka")
print("-------------------")

#DELETION
os.remove("C:/Users/Kay/Desktop/Edureka.txt")  #remomve a file
print("-------------------")

if os.path.exists("C:/Users/Kay/Desktop/Python.txt"):  #check file existence
    os.remove("C:/Users/Kay/Desktop/Python.txt")  #remomve a file
else:
    print("The file does not exist")
print("-------------------")

if os.path.exists("C:/Users/Kay/Desktop/Edureka"):  #check folder existence
    os.rmdir("C:/Users/Kay/Desktop/Edureka")  #remomve a folder
else:
    print("The file does not exist")
