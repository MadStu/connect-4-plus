from os import system, name
from time import sleep
import random

# Board grid size. Height including the blank space above
BOARD_HEIGHT = 7
BOARD_WIDTH = 7

DELAY_TIME = 0.4
DROP_SPEED = 0.06


def reset_board_db():
    """
    Resets the working data and game board for a new game
    """
    global disc_count
    global board_db
    global player_turn
    global winner

    player_turn = True
    winner = False
    disc_count = 0
    board_db = []

    i = 0
    while i < BOARD_WIDTH:
        ii = 0
        temp_board = []
        while ii < BOARD_HEIGHT:
            temp_board.append(" ") if ii == 0 else temp_board.append(".")
            ii += 1
        board_db.append(temp_board)
        i += 1


def clear():
    """
    Clear the Screen to help keep the game board clean and easy to read
    """
    print("\033[1;32;48m ")
    _ = system('cls') if name == 'nt' else system('clear')


def logo():
    """
    Prints the Connect 4 logo text
    """
    print("""\033[0;32;48m
   _____                             _       ___
  /  __ \                           | |     /   |
  | /  \/ ___  _ __  _ __   ___  ___| |_   / /| |
  | |    / _ \| '_ \| '_ \ / _ \/ __| __| / /_| |
  | \__/\ (_) | | | | | | |  __/ (__| |_  \___  |
   \____/\___/|_| |_|_| |_|\___|\___|\__|     |_/
                                 By Stuart Raynor
    \033[1;32;48m""")


def welcome():
    """
    Display the welcome text and games rules
    """
    sleep(DELAY_TIME)

    print("   WELCOME to the fun game of Connect 4!\n")
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
    print("            1   2   3   4   5   6   7  ")
    print("                                       ")
    print("          | . | . | . | . | . | . | . |")
    print("          | . | . | . | . | . | . | . |\n")
    sleep(DELAY_TIME)
    print("   Each column is numbered from left-right.")
    print("   You'll need to enter a column number in which")
    print("   to drop your disc.\n")

    sleep(DELAY_TIME)
    input("   Press Enter to continue...\n")
    clear()
    logo()

    sleep(DELAY_TIME)
    print("            1   2   3   4   5   6   7  ")
    print("                                       ")
    print("          | . | . | . | . | . | . | \033[1;31;48mO\033[1;32;48m |")
    print("          | . | . | . | . | . | \033[1;31;48mO\033[1;32;48m | X |")
    print("          | O | X | . | . | \033[1;31;48mO\033[1;32;48m | X | O |")
    print("          | X | X | X | \033[1;31;48mO\033[1;32;48m | X | O | O |")
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
    disc = "O" if player_turn else "X"
    column -= 1
    i = 0
    bottom = BOARD_HEIGHT - 1
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
    next_turn(disc)


def next_turn(disc):
    """
    Check for winner, if not, swap the player turn, check for draw
    """
    global player_turn
    global winner

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

    space = " "
    three_spaces = space * 3
    wall = " | "
    margin = three_spaces * 3

    if BOARD_WIDTH > 7:
        margin = ((7-(BOARD_WIDTH - 7)) * space)

    # Print the column numbers
    board_line = margin + three_spaces
    i = 1
    while i <= BOARD_WIDTH:
        board_line += (str(i) + three_spaces) if i < 10 else (str(i) + space + space)
        i += 1
    print(board_line)

    # Print the columns
    i = 0
    while i < BOARD_HEIGHT:
        ii = 0
        board_line = margin
        while ii < BOARD_WIDTH:
            board_line += three_spaces if i == 0 else wall
            board_line += board_db[ii][i]
            ii += 1
        board_line += three_spaces if i == 0 else wall
        print(board_line)
        i += 1
    game_status()


def game_status():
    """
    Prints the status of the game
    """
    status = "\n                              "
    user_winn = "      You WON!!\n"
    user_turn = "      Your Turn\n"
    comp_winn = "   Computer Won\n"
    comp_turn = "Computer's Turn\n"

    if player_turn:
        status += user_winn if winner else user_turn
    else:
        status += comp_winn if winner else comp_turn
    print(status)


def enter_column_number():
    """
    Lets the user enter their column choice, checks it's a
    number and checks that there's space left in that column
    """
    column_choice = 0
    column_full = True
    column_range = BOARD_WIDTH + 1
    
    while column_choice not in range(1, column_range) or column_full:
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
            elif column_choice not in range(1, column_range):
                warn = "Please only enter a number between 1 and"
                print("   ", warn, BOARD_WIDTH)
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
    Chooses a random column and checks to see if that column is available
    """
    column_choice = random.randint(1, BOARD_WIDTH)
    while board_db[column_choice-1][1] != ".":
        column_choice = random.randint(1, BOARD_WIDTH)
    sleep(DELAY_TIME)
    drop_disc(column_choice)


def check_winner(disc):
    """
    Checks if there's any winning lines of 4
    Changes the colour of the winning discs

    The following code has been modified but was originally from line 69 of
    https://github.com/justinvallely/Python-Connect-4/
    """
    # check horizontal spaces
    for y in range(1, BOARD_HEIGHT):
        for x in range(BOARD_WIDTH - 3):
            if board_db[x][y] == disc and board_db[x+1][y] == disc:
                if board_db[x+2][y] == disc and board_db[x+3][y] == disc:
                    board_db[x][y] = "\033[1;31;48m"+disc+"\033[1;32;48m"
                    board_db[x+1][y] = "\033[1;31;48m"+disc+"\033[1;32;48m"
                    board_db[x+2][y] = "\033[1;31;48m"+disc+"\033[1;32;48m"
                    board_db[x+3][y] = "\033[1;31;48m"+disc+"\033[1;32;48m"
                    return True

    # check vertical spaces
    for x in range(BOARD_WIDTH):
        for y in range(1, (BOARD_HEIGHT - 3)):
            if board_db[x][y] == disc and board_db[x][y+1] == disc:
                if board_db[x][y+2] == disc and board_db[x][y+3] == disc:
                    board_db[x][y] = "\033[1;31;48m"+disc+"\033[1;32;48m"
                    board_db[x][y+1] = "\033[1;31;48m"+disc+"\033[1;32;48m"
                    board_db[x][y+2] = "\033[1;31;48m"+disc+"\033[1;32;48m"
                    board_db[x][y+3] = "\033[1;31;48m"+disc+"\033[1;32;48m"
                    return True

    # check / diagonal spaces
    for x in range(BOARD_WIDTH - 3):
        for y in range(4, BOARD_HEIGHT):
            if board_db[x][y] == disc and board_db[x+1][y-1] == disc:
                if board_db[x+2][y-2] == disc and board_db[x+3][y-3] == disc:
                    board_db[x][y] = "\033[1;31;48m"+disc+"\033[1;32;48m"
                    board_db[x+1][y-1] = "\033[1;31;48m"+disc+"\033[1;32;48m"
                    board_db[x+2][y-2] = "\033[1;31;48m"+disc+"\033[1;32;48m"
                    board_db[x+3][y-3] = "\033[1;31;48m"+disc+"\033[1;32;48m"
                    return True

    # check \ diagonal spaces
    for x in range(BOARD_WIDTH - 3):
        for y in range(1, (BOARD_HEIGHT - 3)):
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
    win_text = "   WE HAVE A WINNER!!\n"
    user_win = "   You've beaten the computer!\n"
    comp_win = "   You didn't win this time :(\n"

    win_text += user_win if player_turn else comp_win

    print(win_text)
    sleep(DELAY_TIME*4)
    play_again()


def play_again():
    """
    Ask if they want to play again and check their input is valid
    """
    valid_input = False
    while not valid_input:
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

    board_max = (BOARD_HEIGHT-1) * BOARD_WIDTH
    if disc_count >= board_max:
        print("   No winners this time :(\n")
        sleep(DELAY_TIME*3)
        play_again()


clear()
logo()
welcome()
