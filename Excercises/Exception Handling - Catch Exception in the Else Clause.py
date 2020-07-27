
import sys

def linux_interaction():
    assert('linux' in sys.platform), "This code runs on Linux only"
    print('Doing something')

try:
    linux_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)

