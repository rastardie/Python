#Nested While Loop

#Variable Declarations
print("Welcome to KTBank")
restart = ('Y')
chances = 3
balance = 50000

#Main Loop
while chances >= 0:
    pin = int(input("Please Enter Your 4-Digit PIN: "))
    if pin == (1234):
        print("PIN Accepted\n")
        while restart not in ('n', 'NO', 'no', 'N'):
            print("Please Press 1 For Your Balance\n")
            print("Please Press 2 To Make a Withdrawal\n")
            print("Please Press 3 To Pay In\n")
            print("Please Press 4 To Return Card\n")
            option = int(input("Please type 1, 2, 3, or 4 to continue?\n "))
            if option == 1:
                print("Your Balance is Ghc",balance, '\n')
                restart = input("Would you like to perform another transaction?\nY to continue and N to quit ")
                if restart in ('n', 'N', 'no', 'NO'):
                    print("Thank you")
                    break
            elif option == 2:
                option2 = ('y')
                withdraw = float(input("Please enter amount to withdraw in multiples of Ghc20\n "))
                if withdraw < balance:
                    balance = balance - withdraw
                    print('Your new balance is ', balance)
                    restart = input("Would you like to perform another transaction?\nY to continue and N to quit ")
                    if restart in ('n', 'N', 'no', 'NO'):
                        print("Thank you")
                        break
                    elif withdraw > balance:
                        print("Insufficient balance, Please try again\n")
                        restart = ('y')
                    elif withdraw == 1:
                        withdraw = float(input("Please enter amount to withdraw"))

            elif option == 3:
                pay_in = float(input("Please enter amount to pay in\n"))
                balance = balance + pay_in
                print("\nYour new balance is Ghc", balance)
                restart = input("Would you like to perform another transaction? \nY to continue and N to quit ")
                if restart in ('n', 'N', 'no', 'NO'):
                    print("Thank you")
                    break
            elif option == 4:
                print("Please wait while your card is returned...\n ")
                print("Thank you for your service")
                break
            else:
                print("Please enter a correct option (1, 2, 3, or 4) \n")
                restart = ('y')
    elif pin != ('1234'):
        print("Incorrect PIN, please try again")
        chances = chances -1
        if chances == 0:
            print("\n No more tries, please contact your nearest bank branch")
            break












