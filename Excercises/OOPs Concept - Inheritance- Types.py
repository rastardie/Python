#Single Inheritance

class Parent:
    def func1(self):
        print("This is function 1")

class Child(Parent):
    def func2(self):
        print("This is function 2")

ob = Child()
ob.func1()

print("-------------------------------")

#Multiple Inheritance

class Parent2:
    def func3(self):
        print("This is function 3")

class Child(Parent, Parent2):
    def func2(self):
        print("This is function 2")

print("-------------------------------")

#Multi-Level Inheritance

class Parent2(Parent):
    def func3(self):
        print("This is function 3")

class Child(Parent2):
    def func2(self):
        print("This is function 2")


print("-------------------------------")

#Hierarchical Inheritance

class Parent2(Parent):
    def func3(self):
        print("This is function 3")

class Child(Parent):
    def func2(self):
        print("This is function 2")



ob = Child()
ob2 = Parent2
ob.func1()
ob2.func1()
