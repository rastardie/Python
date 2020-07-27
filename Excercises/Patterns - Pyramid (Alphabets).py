#Pyramid (Alphabets)

def pattern(n):
    k = 2*n-2
    x = 65
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k = k - 1
        for j in range(0, i+1):
            ch = chr(x)
            print(ch, end=" ")
            x += 1    #this increments the charaters insteead of repeating them
        print('\r')

pattern(8)