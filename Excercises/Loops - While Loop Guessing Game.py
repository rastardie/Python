#Loops - While Loop Guessing Game
import random
n = 20
to_be_guessed = int(n * random.random())+1
#print("Guess: "+str(to_be_guessed))
guess = 0
while guess != to_be_guessed:
    guess = int(input("New number (between 1 and 20): "))
    if guess > 0:
        if guess > to_be_guessed:
            print("Number too large")
        elif guess < to_be_guessed:
            print("Nubmer too small")
    else:
        print("Sorry that you're giving up!")
        break
else:
    print("Congratulation. You made it!")


