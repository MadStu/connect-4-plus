from os import system, name
from time import sleep

delay_time = 0.001

def clear():
    """
    Clear the Screen to help keep the game board clean and easy to read
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
    sleep(delay_time)

    print("   WELCOME to my little python game of Connect 4.\n")
    sleep(delay_time)

    print("   The game is easy, you take turns with the")
    print("   computer to place your discs which fall into")
    print("   each column, in this game you'll play with X's")
    print("   and O's. You'll be O and the computer will be X.\n")

    sleep(delay_time)
    input("   Press Enter to continue...\n")
    clear()
    logo()

    sleep(delay_time)
    print("             1   2   3   4   5   6   7  ")
    print("                                        ")
    print("           | . | . | . | . | . | . | . |")
    print("           | . | . | . | . | . | . | . |\n")
    sleep(delay_time)
    print("   Each column is numbered from left-right, 1-7.")
    print("   You'll need to enter a number between 1 and 7")
    print("   to choose which column to drop your disc into.\n")

    sleep(delay_time)
    input("   Press Enter to continue...\n")
    clear()
    logo()

    sleep(delay_time)
    print("             1   2   3   4   5   6   7  ")
    print("                                        ")
    print("           | . | . | . | . | . | . | O |")
    print("           | . | . | . | . | . | O | X |")
    print("           | O | X | . | . | O | X | O |")
    print("           | X | X | X | O | X | O | O |\n")
    sleep(delay_time)
    print("   When you get 4 in a row like shown above or")
    print("   in any other direction, you win the game!\n")

    sleep(delay_time)
    input("   Press Enter to start playing!...\n")
    game_board()


def game_board():
    """
    Print's the main gameboard
    """
    clear()
    logo()
    sleep(delay_time)
    print("             1   2   3   4   5   6   7  ")
    print("                                        ")
    print("           | . | . | . | . | . | . | . |")
    print("           | . | . | . | . | . | . | . |")
    print("           | . | . | . | . | . | . | . |")
    print("           | . | . | . | . | . | . | . |")
    print("           | . | . | . | . | . | . | . |")
    print("           | . | . | . | . | . | . | . |")
    print("")
    print("                                    Your Turn")
    #print("                              Computer's Turn")
    print("")
    enter_column_number()
    animation_sample()


def animation_sample():
    clear()
    logo()
    print("             1   2   3   4   5   6   7  ")
    print("                     O                  ")
    print("           | . | . | . | . | . | . | . |")
    print("           | . | . | . | . | . | . | . |")
    print("           | . | . | . | . | . | . | . |")
    print("           | . | . | . | . | . | . | . |")
    print("           | . | . | . | . | . | . | . |")
    print("           | . | . | . | . | . | . | . |")
    print("")

    sleep(0.6)
    clear()
    logo()

    print("             1   2   3   4   5   6   7  ")
    print("                                        ")
    print("           | . | . | O | . | . | . | . |")
    print("           | . | . | . | . | . | . | . |")
    print("           | . | . | . | . | . | . | . |")
    print("           | . | . | . | . | . | . | . |")
    print("           | . | . | . | . | . | . | . |")
    print("           | . | . | . | . | . | . | . |")
    print("")

    sleep(0.2)
    clear()
    logo()

    print("             1   2   3   4   5   6   7  ")
    print("                                        ")
    print("           | . | . | . | . | . | . | . |")
    print("           | . | . | O | . | . | . | . |")
    print("           | . | . | . | . | . | . | . |")
    print("           | . | . | . | . | . | . | . |")
    print("           | . | . | . | . | . | . | . |")
    print("           | . | . | . | . | . | . | . |")
    print("")

    sleep(0.2)
    clear()
    logo()

    print("             1   2   3   4   5   6   7  ")
    print("                                        ")
    print("           | . | . | . | . | . | . | . |")
    print("           | . | . | . | . | . | . | . |")
    print("           | . | . | O | . | . | . | . |")
    print("           | . | . | . | . | . | . | . |")
    print("           | . | . | . | . | . | . | . |")
    print("           | . | . | . | . | . | . | . |")
    print("")

    sleep(0.2)
    clear()
    logo()

    print("             1   2   3   4   5   6   7  ")
    print("                                        ")
    print("           | . | . | . | . | . | . | . |")
    print("           | . | . | . | . | . | . | . |")
    print("           | . | . | . | . | . | . | . |")
    print("           | . | . | O | . | . | . | . |")
    print("           | . | . | . | . | . | . | . |")
    print("           | . | . | . | . | . | . | . |")
    print("")

    sleep(0.2)
    clear()
    logo()

    print("             1   2   3   4   5   6   7  ")
    print("                                        ")
    print("           | . | . | . | . | . | . | . |")
    print("           | . | . | . | . | . | . | . |")
    print("           | . | . | . | . | . | . | . |")
    print("           | . | . | . | . | . | . | . |")
    print("           | . | . | O | . | . | . | . |")
    print("           | . | . | . | . | . | . | . |")
    print("")

    sleep(0.2)
    clear()
    logo()

    print("             1   2   3   4   5   6   7  ")
    print("                                        ")
    print("           | . | . | . | . | . | . | . |")
    print("           | . | . | . | . | . | . | . |")
    print("           | . | . | . | . | . | . | . |")
    print("           | . | . | . | . | . | . | . |")
    print("           | . | . | . | . | . | . | . |")
    print("           | . | . | O | . | . | . | . |")
    print("")


def enter_column_number():
    """
    Let's the user enter their column choice, checks it's a
    number and checks that there's space left in that column
    """
    column_choice = input("   Enter your column choice...\n")


clear()
logo()
welcome()
#game_board()
