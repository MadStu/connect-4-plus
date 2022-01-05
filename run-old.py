from os import system, name
from time import sleep
import random

delay_time = 0.15
drop_delay = 0.07


def reset_board_data():
    """
    Resets the board for a new game
    """
    global disc_count
    global board_data
    global player_turn

    board_data = []
    player_turn = True
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


def drop_disc(column):
    """
    Animates the dropping of the player disc
    Updates the board data with current disc locations
    """
    global player_turn
    if player_turn:
        disc = "O"
    else:
        disc = "X"
    column -= 1
    i = 0
    bottom = 6
    while board_data[column][bottom] != ".":
        bottom -=1
    while i <= bottom:
        board_data[column][i] = disc
        game_board()
        if i == 0:
            sleep(0.6)
            board_data[column][i] = " "
        elif i == bottom:
            sleep(drop_delay)
        else:
            sleep(drop_delay)
            board_data[column][i] = "."
        i += 1
    if check_winner(disc):
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
    Print's the main gameboard
    """
    clear()
    logo()

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
    global disc_count
    column_choice = 0
    column_full = True
    while column_choice not in range(1,8) or column_full:
        try:
            column_choice = int(input("   Enter your column choice...\n"))
        except ValueError:
            print("   Not a number")
            sleep(1)
            game_board()
        finally:
            if column_choice == 999: #Easy quit for dev purposes
                print("Thanks for playing")
                quit()
            elif column_choice == 2222: # disc count to 40 for dev purposes
                disc_count = 40
                game_board()
            elif column_choice not in range(1,8):
                print("   Please only enter a number between 1 and 7")
                sleep(1)
                game_board()
            elif board_data[column_choice-1][1] != ".":
                print("   That column is full")
                sleep(1)
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
    while board_data[column_choice-1][1] != ".":
        column_choice = random.randint(1, 7)
    sleep(delay_time)
    drop_disc(column_choice)


def check_winner(disc):
    """
    Check if there's any winning lines of 4

    The following modified code was originally from 
    https://github.com/justinvallely/Python-Connect-4/
    """
    board_height = 7
    board_width = 7

    #check horizontal spaces
    for y in range(1, board_height):
        for x in range(board_width - 3):
            if board_data[x][y] == disc and board_data[x+1][y] == disc and board_data[x+2][y] == disc and board_data[x+3][y] == disc:
                return True

    #check vertical spaces
    for x in range(board_width):
        for y in range(1, (board_height - 3)):
            if board_data[x][y] == disc and board_data[x][y+1] == disc and board_data[x][y+2] == disc and board_data[x][y+3] == disc:
                return True

    #check / diagonal spaces
    for x in range(board_width - 3):
        for y in range(4, board_height):
            if board_data[x][y] == disc and board_data[x+1][y-1] == disc and board_data[x+2][y-2] == disc and board_data[x+3][y-3] == disc:
                return True

    #check \ diagonal spaces
    for x in range(board_width - 3):
        for y in range(1, (board_height - 3)):
            if board_data[x][y] == disc and board_data[x+1][y+1] == disc and board_data[x+2][y+2] == disc and board_data[x+3][y+3] == disc:
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
    sleep(2)
    play_again()


def play_again():
    """
    Ask if they want to play again and check their input is valid
    """
    valid_input = False
    while valid_input == False:
        sleep(1)
        game_board()
        play_again = input("   Would you like to play again? y/n\n")
        if play_again.lower() == "y":
            print("   OK, resetting game...")
            sleep(1)
            valid_input = True
            reset_board_data()
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
        sleep(2)
        play_again()


clear()
logo()
welcome()