# Method Overriding

class Parent:
    def func1(self):
        print("this is function 1")

class Child(Parent):
    def func1(self):          #same name func1 will override the parent method
        print("this is function 2")

ob = Child()
ob.func1()