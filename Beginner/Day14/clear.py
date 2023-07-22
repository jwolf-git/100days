from os import system, name
from day14art import logo


# define our clear function
def clear():
    # for windows the name is 'nt'
    if name == 'nt':
        _ = system('cls')
        print(logo)

    # and for mac and linux, the os.name is 'posix'
    else:
        _ = system('clear')
        print(logo)
