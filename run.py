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


def welcome():
    """
    Display the welcome text and games rules
    """
    sleep(0.3)

    print(" WELCOME to my little python game of Connect 4.\n")
    sleep(1)

    print(" The game is easy, you take turns with the")
    print(" computer to place your discs which fall into")
    print(" each column, in this game you'll play with X's")
    print(" and O's. You'll be O and the computer will be")
    print(" the X.\n")

    sleep(2)
    input(" Press Enter to continue...\n")
    clear()
    logo()

    sleep(0.3)
    print("           1   2   3   4   5   6   7  ")
    print("                                      ")
    print("         | . | . | . | . | . | . | . |")
    print("         | . | . | . | . | . | . | . |\n")
    sleep(0.3)
    print(" Each column is numbered from left-right, 1-7.")
    print(" You'll need to enter a number between 1 and 7")
    print(" and the game will place your O in that column\n")

    sleep(2)
    input(" Press Enter to continue...\n")
    clear()
    logo()

    sleep(0.3)
    print("           1   2   3   4   5   6   7  ")
    print("                                      ")
    print("         | . | . | . | . | . | . | O |")
    print("         | . | . | . | . | . | O | X |")
    print("         | O | X | . | . | O | X | O |")
    print("         | X | X | X | O | X | O | O |\n")
    sleep(0.3)
    print(" When you get 4 in a row, like shown above or")
    print(" in any other direction, you win the game!\n")

    sleep(2)
    input(" Press Enter to start playing!...\n")


clear()
logo()
welcome()

print("\n\n\n")
