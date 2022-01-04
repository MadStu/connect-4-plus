from os import system, name
from time import sleep

delay_time = 0.01

board_data = []
player_turn = True

def reset_board_data():
    """
    Reset's the board for a new game
    """
    i = 0
    while i <= 6:
        ii = 0
        temp_list = []
        while ii <= 6:
            if ii == 0:
                temp_list.append(" ")
            else:
                temp_list.append(".")
            ii += 1
        board_data.append(temp_list)
        i += 1


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

    reset_board_data()
    game_board()
    enter_column_number()


def game_board():
    """
    Print's the main gameboard
    """
    clear()
    logo()
    sleep(delay_time)

    print("             1   2   3   4   5   6   7  ")
    print(f"             {board_data[0][0]}   {board_data[1][0]}   {board_data[2][0]}   {board_data[3][0]}   {board_data[4][0]}   {board_data[5][0]}   {board_data[6][0]} ")
    print(f"           | {board_data[0][1]} | {board_data[1][1]} | {board_data[2][1]} | {board_data[3][1]} | {board_data[4][1]} | {board_data[5][1]} | {board_data[6][1]} |")
    print(f"           | {board_data[0][2]} | {board_data[1][2]} | {board_data[2][2]} | {board_data[3][2]} | {board_data[4][2]} | {board_data[5][2]} | {board_data[6][2]} |")
    print(f"           | {board_data[0][3]} | {board_data[1][3]} | {board_data[2][3]} | {board_data[3][3]} | {board_data[4][3]} | {board_data[5][3]} | {board_data[6][3]} |")
    print(f"           | {board_data[0][4]} | {board_data[1][4]} | {board_data[2][4]} | {board_data[3][4]} | {board_data[4][4]} | {board_data[5][4]} | {board_data[6][4]} |")
    print(f"           | {board_data[0][5]} | {board_data[1][5]} | {board_data[2][5]} | {board_data[3][5]} | {board_data[4][5]} | {board_data[5][5]} | {board_data[6][5]} |")
    print(f"           | {board_data[0][6]} | {board_data[1][6]} | {board_data[2][6]} | {board_data[3][6]} | {board_data[4][6]} | {board_data[5][6]} | {board_data[6][6]} |")
    print("")
    if player_turn:
        print("                                    Your Turn")
    else:
        print("                              Computer's Turn")
    print("")


def enter_column_number():
    """
    Let's the user enter their column choice, checks it's a
    number and checks that there's space left in that column
    """
    column_choice = 0
    while column_choice not in range(1,8):
        try:
            column_choice = int(input("   Enter your column choice...\n"))
        except ValueError:
            print("   Not a number")
            sleep(1)
            game_board()
        finally:
            if column_choice not in range(1,8):
                print("   Please only enter a number between 1 and 7")
                sleep(1)
                game_board()
            
            
    print("This is number:", column_choice)


clear()
logo()
welcome()
#game_board()
