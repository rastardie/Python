
import sys

def linux_interaction():
    assert('linux' in sys.platform), "This code runs on Linux only"
    print('Doing something')
try:
    linux_interaction()
except AssertionError as error:
    print(error)
else:
    print ('Excecuting the else clause')