def function1(function):
    def wrapper(*args, **kwargs):
        print("hello")
        function(*args, **kwargs)
        print("Welcome to Edureka python tutorials")
    return wrapper

@function1 #Synthactic sugar
def function2(name):
    print(f"{name}")


function2("Kwadwo")