from os import system, name
from time import sleep
import random

DELAY_TIME = 0.5
DROP_SPEED = 0.06


def reset_board_db():
    """
    Resets the board for a new game
    """
    global disc_count
    global board_db
    global player_turn
    global winner

    board_db = []
    player_turn = True
    winner = False
    disc_count = 0

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
        board_db.append(temp_list)
        i += 1


def clear():
    """
    Clear the Screen to help keep the game board clean and easy to read
    """
    print("\033[1;32;48m ")
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def logo():
    """
    Prints the Connect 4 logo text
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
    sleep(DELAY_TIME)

    print("   WELCOME to my little python game of Connect 4.\n")
    sleep(DELAY_TIME)

    print("   The game is easy, you take turns with the")
    print("   computer to place your discs which fall into")
    print("   each column, in this game you'll play with X's")
    print("   and O's. You'll be O and the computer will be X.\n")

    sleep(DELAY_TIME)
    input("   Press Enter to continue...\n")
    clear()
    logo()

    sleep(DELAY_TIME)
    print("             1   2   3   4   5   6   7  ")
    print("                                        ")
    print("           | . | . | . | . | . | . | . |")
    print("           | . | . | . | . | . | . | . |\n")
    sleep(DELAY_TIME)
    print("   Each column is numbered from left-right, 1-7.")
    print("   You'll need to enter a number between 1 and 7")
    print("   to choose which column to drop your disc into.\n")

    sleep(DELAY_TIME)
    input("   Press Enter to continue...\n")
    clear()
    logo()

    sleep(DELAY_TIME)
    print("             1   2   3   4   5   6   7  ")
    print("                                        ")
    print("           | . | . | . | . | . | . | \033[1;31;48mO\033[1;32;48m |")
    print("           | . | . | . | . | . | \033[1;31;48mO\033[1;32;48m | X |")
    print("           | O | X | . | . | \033[1;31;48mO\033[1;32;48m | X | O |")
    print("           | X | X | X | \033[1;31;48mO\033[1;32;48m | X | O | O |")
    print("")
    sleep(DELAY_TIME)
    print("   When you get 4 in a row like shown above or")
    print("   in any other direction, you win the game!\n")

    sleep(DELAY_TIME)
    input("   Press Enter to start playing!...\n")

    reset_board_db()
    game_board()
    enter_column_number()


def drop_disc(column):
    """
    Animates the dropping of the player disc
    Updates the board data with current disc locations
    """
    global player_turn
    global winner
    if player_turn:
        disc = "O"
    else:
        disc = "X"
    column -= 1
    i = 0
    bottom = 6
    while board_db[column][bottom] != ".":
        bottom -= 1
    while i <= bottom:
        board_db[column][i] = disc
        game_board()
        if i == 0:
            sleep(DELAY_TIME)
            board_db[column][i] = " "
        elif i == bottom:
            sleep(DROP_SPEED)
        else:
            sleep(DROP_SPEED)
            board_db[column][i] = "."
        i += 1
    if check_winner(disc):
        winner = True
        game_board()
        we_have_a_winner()
    else:
        if player_turn:
            player_turn = False
            check_draw()
            game_board()
            computer_turn()
        else:
            player_turn = True
            check_draw()
            game_board()
            enter_column_number()


def game_board():
    """
    Prints the main gameboard
    """
    clear()
    logo()

    margin = "          "
    space = "   "
    wall = " | "

    print("             1   2   3   4   5   6   7  ")

    i = 0
    while i < 7:
        ii = 0
        board_line = margin
        while ii < 7:
            if i == 0:
                board_line = board_line + space
            else:
                board_line = board_line + wall
            board_line = board_line + board_db[ii][i]
            ii += 1
        if i == 0:
            board_line = board_line + space
        else:
            board_line = board_line + wall
        print(board_line)
        i += 1
    print("")
    if player_turn:
        if winner:
            print("                                    You WON!!")
        else:
            print("                                    Your Turn")
    else:
        if winner:
            print("                                 Computer Won")
        else:
            print("                              Computer's Turn")
    print("")


def enter_column_number():
    """
    Lets the user enter their column choice, checks it's a
    number and checks that there's space left in that column
    """
    column_choice = 0
    column_full = True
    while column_choice not in range(1, 8) or column_full:
        try:
            column_choice = int(input("   Enter your column choice...\n"))
        except ValueError:
            print("   Not a number")
            sleep(DELAY_TIME*2)
            game_board()
        finally:
            if column_choice == 999:  # Easy quit for dev purposes
                print("Thanks for playing")
                quit()
            elif column_choice not in range(1, 8):
                print("   Please only enter a number between 1 and 7")
                sleep(DELAY_TIME*2)
                game_board()
            elif board_db[column_choice-1][1] != ".":
                print("   That column is full!")
                sleep(DELAY_TIME*2)
                game_board()
            else:
                column_full = False
    drop_disc(column_choice)


def computer_turn():
    """
    Checks who's turn it is, takes the computer turn or passes
    control back to the user
    """
    column_choice = random.randint(1, 7)
    while board_db[column_choice-1][1] != ".":
        column_choice = random.randint(1, 7)
    sleep(DELAY_TIME)
    drop_disc(column_choice)


def check_winner(disc):
    """
    Checks if there's any winning lines of 4
    Changes the colour of the winning discs

    The following modified code was originally from
    https://github.com/justinvallely/Python-Connect-4/
    """
    board_height = 7
    board_width = 7

    # check horizontal spaces
    for y in range(1, board_height):
        for x in range(board_width - 3):
            if board_db[x][y] == disc and board_db[x+1][y] == disc:
                if board_db[x+2][y] == disc and board_db[x+3][y] == disc:
                    board_db[x][y] = "\033[1;31;48m"+disc+"\033[1;32;48m"
                    board_db[x+1][y] = "\033[1;31;48m"+disc+"\033[1;32;48m"
                    board_db[x+2][y] = "\033[1;31;48m"+disc+"\033[1;32;48m"
                    board_db[x+3][y] = "\033[1;31;48m"+disc+"\033[1;32;48m"
                    return True

    # check vertical spaces
    for x in range(board_width):
        for y in range(1, (board_height - 3)):
            if board_db[x][y] == disc and board_db[x][y+1] == disc:
                if board_db[x][y+2] == disc and board_db[x][y+3] == disc:
                    board_db[x][y] = "\033[1;31;48m"+disc+"\033[1;32;48m"
                    board_db[x][y+1] = "\033[1;31;48m"+disc+"\033[1;32;48m"
                    board_db[x][y+2] = "\033[1;31;48m"+disc+"\033[1;32;48m"
                    board_db[x][y+3] = "\033[1;31;48m"+disc+"\033[1;32;48m"
                    return True

    # check / diagonal spaces
    for x in range(board_width - 3):
        for y in range(4, board_height):
            if board_db[x][y] == disc and board_db[x+1][y-1] == disc:
                if board_db[x+2][y-2] == disc and board_db[x+3][y-3] == disc:
                    board_db[x][y] = "\033[1;31;48m"+disc+"\033[1;32;48m"
                    board_db[x+1][y-1] = "\033[1;31;48m"+disc+"\033[1;32;48m"
                    board_db[x+2][y-2] = "\033[1;31;48m"+disc+"\033[1;32;48m"
                    board_db[x+3][y-3] = "\033[1;31;48m"+disc+"\033[1;32;48m"
                    return True

    # check \ diagonal spaces
    for x in range(board_width - 3):
        for y in range(1, (board_height - 3)):
            if board_db[x][y] == disc and board_db[x+1][y+1] == disc:
                if board_db[x+2][y+2] == disc and board_db[x+3][y+3] == disc:
                    board_db[x][y] = "\033[1;31;48m"+disc+"\033[1;32;48m"
                    board_db[x+1][y+1] = "\033[1;31;48m"+disc+"\033[1;32;48m"
                    board_db[x+2][y+2] = "\033[1;31;48m"+disc+"\033[1;32;48m"
                    board_db[x+3][y+3] = "\033[1;31;48m"+disc+"\033[1;32;48m"
                    return True

    return False


def we_have_a_winner():
    """
    We have a winner!
    Tell the player who won
    """
    print("   WE HAVE A WINNER!!")
    if player_turn:
        print("   You've beaten the computer!\n")
    else:
        print("   You didn't win this time :(\n")
    sleep(DELAY_TIME*3)
    play_again()


def play_again():
    """
    Ask if they want to play again and check their input is valid
    """
    valid_input = False
    while valid_input is False:
        sleep(DELAY_TIME)
        game_board()
        play_again = input("   Would you like to play again? y/n\n")
        if play_again.lower() == "y":
            print("   OK, resetting game...")
            sleep(DELAY_TIME)
            valid_input = True
            reset_board_db()
            game_board()
            enter_column_number()
        elif play_again.lower() == "n":
            print("   OK, Thank you for playing. Come back soon!! :)\n")
            valid_input = True
            quit()
        else:
            print("   Not a valid input.")


def check_draw():
    """
    Checks to see if the board is full without any winners
    """
    global disc_count
    disc_count += 1

    if disc_count >= 42:
        print("   No winners this time :(\n")
        sleep(DELAY_TIME*3)
        play_again()


clear()
logo()
welcome()
