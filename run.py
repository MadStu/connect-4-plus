from os import system, name
from time import sleep


def clear():
    """
    Clear the Screen to help keep the game board clean and easy to read
    Sourced from: https://www.geeksforgeeks.org/clear-screen-python/
    """
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def logo():
    """
    Print's the Connect 4 logo text
    """
    print("""\
 _____                             _       ___ 
/  __ \                           | |     /   |
| /  \/ ___  _ __  _ __   ___  ___| |_   / /| |
| |    / _ \| '_ \| '_ \ / _ \/ __| __| / /_| |
| \__/\ (_) | | | | | | |  __/ (__| |_  \___  |
 \____/\___/|_| |_|_| |_|\___|\___|\__|     |_/
                     """)


clear()
logo()

print("                   O                  ")
print("         | . | . | . | . | . | . | . |")
print("         | . | . | . | . | . | . | . |")
print("         | . | . | . | . | . | . | . |")
print("         | . | . | . | . | . | . | . |")
print("         | . | . | . | . | . | . | . |")
print("         | . | . | O | . | X | . | . |")

sleep(0.6)
clear()
logo()

print("                                      ")
print("         | . | . | O | . | . | . | . |")
print("         | . | . | . | . | . | . | . |")
print("         | . | . | . | . | . | . | . |")
print("         | . | . | . | . | . | . | . |")
print("         | . | . | . | . | . | . | . |")
print("         | . | . | O | . | X | . | . |")

sleep(0.2)
clear()
logo()

print("                                      ")
print("         | . | . | . | . | . | . | . |")
print("         | . | . | O | . | . | . | . |")
print("         | . | . | . | . | . | . | . |")
print("         | . | . | . | . | . | . | . |")
print("         | . | . | . | . | . | . | . |")
print("         | . | . | O | . | X | . | . |")

sleep(0.2)
clear()
logo()

print("                                      ")
print("         | . | . | . | . | . | . | . |")
print("         | . | . | . | . | . | . | . |")
print("         | . | . | O | . | . | . | . |")
print("         | . | . | . | . | . | . | . |")
print("         | . | . | . | . | . | . | . |")
print("         | . | . | O | . | X | . | . |")

sleep(0.2)
clear()
logo()

print("                                      ")
print("         | . | . | . | . | . | . | . |")
print("         | . | . | . | . | . | . | . |")
print("         | . | . | . | . | . | . | . |")
print("         | . | . | O | . | . | . | . |")
print("         | . | . | . | . | . | . | . |")
print("         | . | . | O | . | X | . | . |")

sleep(0.2)
clear()
logo()

print("                                      ")
print("         | . | . | . | . | . | . | . |")
print("         | . | . | . | . | . | . | . |")
print("         | . | . | . | . | . | . | . |")
print("         | . | . | . | . | . | . | . |")
print("         | . | . | O | . | . | . | . |")
print("         | . | . | O | . | X | . | . |")
print("                                      ")
print("                                      ")
print("                                      ")
