from os import system, name
from time import sleep
import random

# Board starting grid size. Height includes the blank space above
BOARD_HEIGHT = 7
BOARD_WIDTH = 12

# The working variable of BOARD_WIDTH
game_width = BOARD_WIDTH

# Delay time of items being shown
DELAY_TIME = 0.15

# Speed which the disc drops down
DROP_SPEED = 0.05

# Each game won increases their level
game_level = 1
winner = False
player_turn = True
next_comp_move = 0
hard_mode = False


def reset_board_db():
    """
    Resets the working data and game board for a new game
    Increase or reset game level and board width
    """
    global player_turn
    global winner
    global disc_count
    global board_db
    global game_level
    global game_width
    global next_comp_move

    # Reset or adjust game level and board width
    if winner:
        if player_turn:
            # Player has won!
            game_level += 1
            game_width -= 1

        else:
            # Computer has won :(
            game_level = 1
            game_width = BOARD_WIDTH

    # Reset Everything else
    player_turn = True
    winner = False
    disc_count = 0
    next_comp_move = 0
    board_db = []

    # Add blank data into the board_db column by column
    for i in range(game_width):
        temp_board = []
        for ii in range(BOARD_HEIGHT):
            temp_board.append(" ") if ii == 0 else temp_board.append(".")

        board_db.append(temp_board)


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
    print("""\033[0;32;48m   _____                             _       ___
  /  __ \                           | |     /   |
  | /  \/ ___  _ __  _ __   ___  ___| |_   / /| |
  | |    / _ \| '_ \| '_ \ / _ \/ __| __| / /_| |
  | \__/\ (_) | | | | | | |  __/ (__| |_  \___  |
   \____/\___/|_| |_|_| |_|\___|\___|\__|     |_/
    \033[1;32;48m""")


def welcome():
    """
    Display the welcome text and games rules
    """
    clear()
    logo()
    sleep(DELAY_TIME)

    print("   WELCOME to the fun game of Connect 4!\n")
    sleep(DELAY_TIME)

    print("   The game is easy, you take turns with the")
    print("   computer to place your discs which fall into")
    print("   each column, in this game you'll play with X's")
    print("   and O's. \n   You'll be O and the computer will be X.\n")

    sleep(DELAY_TIME)
    input("   Press Enter to continue...\n")
    clear()
    logo()

    sleep(DELAY_TIME)
    print("   1   2   3   4   5   6   7   8   9   10  11  12")
    print("                                       ")
    print(" | . | . | . | . | . | . | . | . | . | . | . | . |")
    print(" | . | . | . | . | . | . | . | . | . | . | . | . |\n")
    sleep(DELAY_TIME)
    print("   Each column is numbered from left-right.")
    print("   You'll need to enter a column number in which")
    print("   to drop your disc.\n")

    sleep(DELAY_TIME)
    input("   Press Enter to continue...\n")
    clear()
    logo()

    sleep(DELAY_TIME)
    disc_example = "\033[1;31;48mO\033[1;32;48m"
    print("   1   2   3   4   5   6   7   8   9   10  11  12")
    print("                                       ")
    print(f" | . | . | . | . | . | . | {disc_example} | . | . | . | . | . |")
    print(f" | . | . | . | . | . | {disc_example} | X | . | X | . | . | . |")
    print(f" | O | X | . | . | {disc_example} | X | O | . | O | O | . | . |")
    print(f" | X | X | X | {disc_example} | X | O | O | O | X | O | X | . |")
    print("")
    sleep(DELAY_TIME)
    print("   When you get 4 in a row like shown above or")
    print("   in any other direction, you win the game!\n")

    sleep(DELAY_TIME)
    input("   Press Enter to continue...\n")
    clear()
    logo()

    sleep(DELAY_TIME)
    print("   1   2   3   4   5   6   7   8   9   10  11  12")
    print("                                       ")
    print(" | . | . | . | . | . | . | . | . | . | . | . | . |")
    print(" | . | . | . | . | . | . | . | . | . | . | . | . |")
    game_status()
    sleep(DELAY_TIME)
    print("   You'll start on Level 1 and your goal is to")
    print("   reach level 10. The Board will narrow each time")
    print("   you level up, increasing the difficulty.\n")

    sleep(DELAY_TIME)
    input("   Press Enter to start playing!...\n")

    # Begin the game!
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
    bottom = BOARD_HEIGHT - 1

    # Finds the the next available square to determine the bottom
    while board_db[column][bottom] != ".":
        bottom -= 1

    # Places disc in the next square down and refreshes the board
    for i in range(bottom + 1):
        board_db[column][i] = disc
        game_board()

        # Determines if it's blank space or a . to replace
        if i == 0:
            sleep(DELAY_TIME*2)
            board_db[column][i] = " "

        elif i == bottom:
            # Disc has reached the bottom
            sleep(DROP_SPEED)

        else:
            sleep(DROP_SPEED)
            board_db[column][i] = "."

    next_turn(disc)


def next_turn(disc):
    """
    Check for winner, if not, swap the player turn, check for draw
    """
    global player_turn
    global winner
    global next_comp_move

    # Reset next computer move
    next_comp_move = 0

    if check_winner(disc):
        # Game has a winner so handle that
        winner = True
        game_board()
        we_have_a_winner()

    else:
        if player_turn:
            # The last turn was the players so change it
            player_turn = False
            check_draw()
            game_board()
            computer_turn()

        else:
            # The last turn was the computer's so change it
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
    margin_len = 17

    # Determine the margin width based on number of columns
    for i in range(game_width - 1):
        margin_len -= 2 if i % 2 == 0 else 1

    # Make sure the margin is never less than 0 spaces wide
    margin = space * margin_len if margin_len > 0 else ""

    # Print the column numbers
    board_line = margin + three_spaces

    for i in range(1, game_width + 1):
        if i < 10:
            board_line += (str(i) + three_spaces)

        else:
            board_line += (str(i) + space + space)

    print(board_line)

    # Print the columns
    for i in range(BOARD_HEIGHT):
        board_line = margin

        # Print the walls in the main area. None for the top
        for ii in range(game_width):
            board_line += three_spaces if i == 0 else wall
            board_line += board_db[ii][i]

        # Prints walls or spaces depending which line is processing
        board_line += three_spaces if i == 0 else wall
        print(board_line)

    game_status()


def game_status():
    """
    Prints the status of the game
    """
    space = "           " if game_level < 10 else "          "
    status = f"\n       Level: {game_level}{space}"
    user_winn = "      You WON!!\n"
    user_turn = "      Your Turn\n"
    comp_winn = "   Computer Won\n"
    comp_turn = "Computer's Turn\n"

    # Put the status in order
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
    column_range = game_width + 1

    while column_choice not in range(1, column_range) or column_full:
        try:
            # User inputs column number
            column_choice = int(input("   Enter your column choice...\n"))

        except ValueError:
            # Handle the error if it's not a number
            print("   Not a number")
            sleep(DELAY_TIME*2)
            game_board()

        finally:
            if column_choice == 999:
                # Easy quit game code for dev purposes
                print("Thanks for playing")
                quit()

            elif column_choice == 42:
                # Easter egg! Because I like the book
                print("   Answer to the Ultimate Question of Life,")
                print("               The Universe, and Everything\n")
                sleep(DELAY_TIME*9)
                game_board()

            elif column_choice not in range(1, column_range):
                # Handle when input number not an available column
                warn = "Please only enter a number between 1 and"
                print("   ", warn, game_width)
                sleep(DELAY_TIME*4)
                game_board()

            elif board_db[column_choice-1][1] != ".":
                # Check to see if the column is full
                print("   That column is full!")
                sleep(DELAY_TIME*2)
                game_board()

            else:
                column_full = False

    drop_disc(column_choice)


def computer_turn():
    """
    Chooses a random column or copies the players evry 3rd move
    Then checks to see if that column is available
    """
    if next_comp_move > 0:
        # Go where was suggested
        column_choice = next_comp_move
    else:
        # Choose a random column
        column_choice = random.randint(1, game_width)

    # The chosen column is full so choose again
    while board_db[column_choice-1][1] != ".":
        column_choice = random.randint(1, game_width)

    sleep(DELAY_TIME)
    drop_disc(column_choice)


def check_winner(disc):
    """
    Checks if there's any winning lines of 4
    Changes the colour of the winning discs

    Also checks for free spaces for the computer to stop player winning

    The following code has been modified but was originally from line 69 of
    https://github.com/justinvallely/Python-Connect-4/
    """
    # Check horizontal spaces
    for y in range(1, BOARD_HEIGHT):
        for x in range(game_width - 3):
            if board_db[x+3][y] == disc and board_db[x+2][y] == disc:
                if board_db[x+1][y] == disc and board_db[x][y] == disc:
                    # Turn the winning discs RED
                    board_db[x][y] = "\033[1;31;48m"+disc+"\033[1;32;48m"
                    board_db[x+1][y] = "\033[1;31;48m"+disc+"\033[1;32;48m"
                    board_db[x+2][y] = "\033[1;31;48m"+disc+"\033[1;32;48m"
                    board_db[x+3][y] = "\033[1;31;48m"+disc+"\033[1;32;48m"
                    return True

                elif board_db[x+1][y] == disc and board_db[x][y] == ".":
                    computer_next_move(x, y)

                elif board_db[x+1][y] == "." and board_db[x][y] == disc:
                    computer_next_move(x+1, y)

                elif board_db[x+1][y] == "." and board_db[x][y] == ".":
                    hard_mode and computer_next_move(x+1, y)

    # Check horizontal spaces from other direction
    for y in range(1, BOARD_HEIGHT):
        for x in range(game_width - 3):
            if board_db[x][y] == disc and board_db[x+1][y] == disc:
                if board_db[x+2][y] == disc and board_db[x+3][y] == ".":
                    computer_next_move(x+3, y)

                elif board_db[x+2][y] == "." and board_db[x+3][y] == disc:
                    computer_next_move(x+2, y)

                elif board_db[x+2][y] == "." and board_db[x+3][y] == ".":
                    hard_mode and computer_next_move(x+2, y)

    # Check vertical spaces
    for x in range(game_width):
        for y in range(1, (BOARD_HEIGHT - 3)):
            if board_db[x][y+3] == disc and board_db[x][y+2] == disc:
                if board_db[x][y+1] == disc and board_db[x][y] == disc:
                    # Turn the winning discs RED
                    board_db[x][y] = "\033[1;31;48m"+disc+"\033[1;32;48m"
                    board_db[x][y+1] = "\033[1;31;48m"+disc+"\033[1;32;48m"
                    board_db[x][y+2] = "\033[1;31;48m"+disc+"\033[1;32;48m"
                    board_db[x][y+3] = "\033[1;31;48m"+disc+"\033[1;32;48m"
                    return True

                elif board_db[x][y+1] == disc and board_db[x][y] == ".":
                    computer_next_move(x, y)

    # Check / diagonal spaces
    for x in range(game_width - 3):
        for y in range(4, BOARD_HEIGHT):
            if board_db[x+3][y-3] == disc and board_db[x+2][y-2] == disc:
                if board_db[x+1][y-1] == disc and board_db[x][y] == disc:
                    # Turn the winning discs RED
                    board_db[x][y] = "\033[1;31;48m"+disc+"\033[1;32;48m"
                    board_db[x+1][y-1] = "\033[1;31;48m"+disc+"\033[1;32;48m"
                    board_db[x+2][y-2] = "\033[1;31;48m"+disc+"\033[1;32;48m"
                    board_db[x+3][y-3] = "\033[1;31;48m"+disc+"\033[1;32;48m"
                    return True

                elif board_db[x+1][y-1] == "." and board_db[x][y] == disc:
                    computer_next_move(x+1, y-1)

                elif board_db[x+1][y-1] == disc and board_db[x][y] == ".":
                    computer_next_move(x, y)

                elif board_db[x+1][y-1] == "." and board_db[x][y] == ".":
                    hard_mode and computer_next_move(x+1, y-1)

    # Check / diagonal spaces from other direction
    for x in range(game_width - 3):
        for y in range(4, BOARD_HEIGHT):
            if board_db[x][y] == disc and board_db[x+1][y-1] == disc:
                if board_db[x+2][y-2] == "." and board_db[x+3][y-3] == disc:
                    computer_next_move(x+2, y-2)

                elif board_db[x+2][y-2] == disc and board_db[x+3][y-3] == ".":
                    computer_next_move(x+3, y-3)

                elif board_db[x+2][y-2] == "." and board_db[x+3][y-3] == ".":
                    hard_mode and computer_next_move(x+2, y-2)

    # Check \ diagonal spaces
    for x in range(game_width - 3):
        for y in range(1, (BOARD_HEIGHT - 3)):
            if board_db[x+3][y+3] == disc and board_db[x+2][y+2] == disc:
                if board_db[x+1][y+1] == disc and board_db[x][y] == disc:
                    # Turn the winning discs RED
                    board_db[x][y] = "\033[1;31;48m"+disc+"\033[1;32;48m"
                    board_db[x+1][y+1] = "\033[1;31;48m"+disc+"\033[1;32;48m"
                    board_db[x+2][y+2] = "\033[1;31;48m"+disc+"\033[1;32;48m"
                    board_db[x+3][y+3] = "\033[1;31;48m"+disc+"\033[1;32;48m"
                    return True

                elif board_db[x+1][y+1] == "." and board_db[x][y] == disc:
                    computer_next_move(x+1, y+1)

                elif board_db[x+1][y+1] == disc and board_db[x][y] == ".":
                    computer_next_move(x, y)

                elif board_db[x+1][y+1] == "." and board_db[x][y] == ".":
                    hard_mode and computer_next_move(x+1, y+1)

    # Check \ diagonal spaces from other direction
    for x in range(game_width - 3):
        for y in range(1, (BOARD_HEIGHT - 3)):
            if board_db[x][y] == disc and board_db[x+1][y+1] == disc:
                if board_db[x+2][y+2] == "." and board_db[x+3][y+3] == disc:
                    computer_next_move(x+2, y+2)

                elif board_db[x+2][y+2] == disc and board_db[x+3][y+3] == ".":
                    computer_next_move(x+3, y+3)

                elif board_db[x+2][y+2] == "." and board_db[x+3][y+3] == ".":
                    hard_mode and computer_next_move(x+2, y+2)

    return False


def computer_next_move(x, y):
    """
    Tells the computer the next best place to go to beat the player
    """
    global next_comp_move

    try:
        # Check if the square under the next winning square is not empty
        if board_db[x][y+1] != ".":
            # Tell computer to put next disc here
            next_comp_move = x+1

    except IndexError:
        # Tell computer to put next disc here
        next_comp_move = x+1


def we_have_a_winner():
    """
    We have a winner!
    Tell the player who has won
    """
    win_text = "   WE HAVE A WINNER!!\n"
    user_win = "   You've beaten the computer!\n"
    comp_win = "   You didn't win this time :(\n"

    win_text += user_win if player_turn else comp_win

    if game_level < (BOARD_WIDTH - 2):
        print(win_text)
        sleep(DELAY_TIME*4)

    play_again()


def play_again():
    """
    Ask if they want to play again and check their input is valid
    """
    sleep(DELAY_TIME)
    game_board()

    input_text = "   Press Enter to "

    # Reset game level after they've won the game
    if game_level >= BOARD_WIDTH - 2 and winner:
        top_level()
        input_text += "play again"
    else:
        input_text += "continue playing"

    input_text += " \n   or type 'N' to quit\n"
    play_again = input(input_text)

    if play_again.lower() == "n":
        # Player wants to end the game so quit
        print("   OK, Thank you for playing. Come back soon!! :)\n")
        quit()

    else:
        # Player wants to play again so reset and start the game
        print("   OK, resetting game...")
        sleep(DELAY_TIME)
        reset_board_db()
        game_board()
        enter_column_number()


def check_draw():
    """
    Checks to see if the board is full without any winners
    """
    global disc_count
    disc_count += 1

    # Calculate the max number of squares based on board size
    board_max = (BOARD_HEIGHT-1) * game_width

    if disc_count >= board_max:
        # Game's a draw so handle that
        print("   No winners this time :(\n")
        print("             Try again!\n")
        sleep(DELAY_TIME*3)
        play_again()


def top_level():
    """
    When player reaches top level they are told they've won the game
    and everything is reset
    """
    global game_level
    global game_width

    game_won = "               YOU BEAT THE GAME!!!\n"
    game_won += "          VERY well done! I'm impressed!"
    print(game_won)

    sleep(10)
    game_board()
    winner = False
    game_level = 0
    game_width = BOARD_WIDTH + 1


welcome()
