from os import name, system


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')
