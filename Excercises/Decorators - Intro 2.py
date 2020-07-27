
def function1(function):
    def wrapper():
        print("hello")
        function()
        print("welcome to Edureka Python tutorial")
    return wrapper()
@function1
def function2():
    print("Pythonista")

function2()