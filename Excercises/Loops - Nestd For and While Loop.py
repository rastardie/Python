#Nested For and While Loop

traveling = input("Traveling: Yes or No? ")

while traveling == 'yes':
    num = int(input("How many people are traveling? \n"))

    for num in range (1, num +1):
        name = input("Name: \n")

        age = input("Age: \n")

        sex = input("Male or Male: \n")

        print(name)

        print(age)

        print(sex)

    traveling = input("Oops! Forgot Someone: Yes or No \n")

