#try    {Run This Code}
#except {Execute this code when there is an exception }
#else    {No exception? run this code}
#finally {Always run this code, error or no errors}

import sys


assert('linix' in sys.platform), "This code runs on Linux only"


print("----------------------------")

x = 10
if x > 5:
    raise Exception('x should not exceed 5. The value of x was:  {}'.format(x))
print("----------------------------")

def linux_interaction():
    assert('linix' in sys.platform), "This code runs on Linux only"
    print('Doing something')
try:
    linux_interaction()
except:
    print('Linux funtion was not executed')
print("----------------------------")

#Catch teh error the display the type of error
try:
    linux_interaction()
except AssertionError as error:
    print(error)
    print('The linux_interaction funtion was not executed')
print("----------------------------")

try:
    with open('file.log') as file:
        read_data = file.read()
except:
    print('Could not open the file.log')
print("----------------------------")

try:
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)
print("----------------------------------------")

try:
    linux_interaction()
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)
except AssertionError as error:
    print(error)
    print ('Linux linux_interaction() function was not executed')