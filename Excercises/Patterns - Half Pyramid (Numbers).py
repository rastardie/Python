#Half Pyramid with Numbers

def pattern(n):
    x = 0
    for i in range(0,n):
        x = x + 1
        for j in range(0, i+1):
            print(x, end=" ")
        print('\r')

pattern(7)