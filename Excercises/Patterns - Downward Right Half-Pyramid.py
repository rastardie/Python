#Downward Right Half-Pyramid

def pattern(n):
    for i in range(n, -1, -1):
        for j in range(0, i+1):
            print("* ", end="")
        print('\r')

pattern(10)
