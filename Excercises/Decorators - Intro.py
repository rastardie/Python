def function1(function):
    def wrapper():
        print("hello")
        function()
        print("welcome to Edureka Python tutorial")
    return wrapper()
def function2():
    print("Pythonista")

function2 = function1(function2)

function2()

print("-----------------------")
