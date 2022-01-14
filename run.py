from os import system, name
from time import sleep
import random

# Set Recursion limit higher for the AI
from sys import setrecursionlimit
setrecursionlimit(2500)

# Board starting grid size. Height includes the top blank row
BOARD_HEIGHT = 7
BOARD_WIDTH = 12

# Delay time of items being shown
DELAY_TIME = 0.15

# Speed which the disc drops down
DROP_SPEED = 0.06

# Text Styles
RED_TEXT = "\033[1;31;48m"
GREEN_TEXT = "\033[1;32;48m"
LOGO_TEXT = "\033[0;32;48m"

# Winning game level
WIN_LEVEL = BOARD_WIDTH - 3


class Game:
    # This class carries the game state variables
    level = 1
    winner = False
    player_turn = True
    next_move = 0
    hard_mode = False
    got_3 = False
    width = BOARD_WIDTH
    db = []
    disc_count = 0


class BoardCheck:
    """
    d = player disc and e = empty
    Shortened to satisfy the pep8 line length warnings

    Checks if there's any winning lines of 4
    Changes the colour of the winning discs

    Also checks for free spaces for the computer to stop player winning

    The following code has been modified but was originally from line 69 of
    https://github.com/justinvallely/Python-Connect-4/
    """
    def __init__(self, disc):
        self.disc = disc

    def diag_right_forward(self):
        d = self.disc
        e = "."
        # Check / diagonal spaces
        for x in range(Game.width - 3):
            for y in range(4, BOARD_HEIGHT):
                if Game.db[x+3][y-3] == d and Game.db[x+2][y-2] == d:
                    if Game.db[x+1][y-1] == d and Game.db[x][y] == d:
                        # Turn the winning discs RED
                        Game.db[x][y] = RED_TEXT + d + GREEN_TEXT
                        Game.db[x+1][y-1] = RED_TEXT + d + GREEN_TEXT
                        Game.db[x+2][y-2] = RED_TEXT + d + GREEN_TEXT
                        Game.db[x+3][y-3] = RED_TEXT + d + GREEN_TEXT
                        return True

                    elif Game.db[x+1][y-1] == e and Game.db[x][y] == d:
                        Game.got_3 = True
                        computer_next_move(x+1, y-1)

                    elif Game.db[x+1][y-1] == d and Game.db[x][y] == e:
                        Game.got_3 = True
                        computer_next_move(x, y)

                    elif Game.db[x+1][y-1] == e and Game.db[x][y] == e:
                        if Game.hard_mode and not Game.got_3:
                            computer_next_move(x+1, y-1)
        return False

    def diag_right_backward(self):
        d = self.disc
        e = "."
        # Check / diagonal spaces from other direction
        for x in range(Game.width - 3):
            for y in range(4, BOARD_HEIGHT):
                if Game.db[x][y] == d and Game.db[x+1][y-1] == d:
                    if Game.db[x+2][y-2] == e and Game.db[x+3][y-3] == d:
                        Game.got_3 = True
                        computer_next_move(x+2, y-2)

                    elif Game.db[x+2][y-2] == d and Game.db[x+3][y-3] == e:
                        Game.got_3 = True
                        computer_next_move(x+3, y-3)

                    elif Game.db[x+2][y-2] == e and Game.db[x+3][y-3] == e:
                        if Game.hard_mode and not Game.got_3:
                            computer_next_move(x+2, y-2)
        return False

    def diag_left_forward(self):
        d = self.disc
        e = "."
        # Check \ diagonal spaces
        for x in range(Game.width - 3):
            for y in range(1, (BOARD_HEIGHT - 3)):
                if Game.db[x+3][y+3] == d and Game.db[x+2][y+2] == d:
                    if Game.db[x+1][y+1] == d and Game.db[x][y] == d:
                        # Turn the winning discs RED
                        Game.db[x][y] = RED_TEXT + d + GREEN_TEXT
                        Game.db[x+1][y+1] = RED_TEXT + d + GREEN_TEXT
                        Game.db[x+2][y+2] = RED_TEXT + d + GREEN_TEXT
                        Game.db[x+3][y+3] = RED_TEXT + d + GREEN_TEXT
                        return True

                    elif Game.db[x+1][y+1] == e and Game.db[x][y] == d:
                        Game.got_3 = True
                        computer_next_move(x+1, y+1)

                    elif Game.db[x+1][y+1] == d and Game.db[x][y] == e:
                        Game.got_3 = True
                        computer_next_move(x, y)

                    elif Game.db[x+1][y+1] == e and Game.db[x][y] == e:
                        if Game.hard_mode and not Game.got_3:
                            computer_next_move(x+1, y+1)
        return False

    def diag_left_backward(self):
        d = self.disc
        e = "."
        # Check \ diagonal spaces from other direction
        for x in range(Game.width - 3):
            for y in range(1, (BOARD_HEIGHT - 3)):
                if Game.db[x][y] == d and Game.db[x+1][y+1] == d:
                    if Game.db[x+2][y+2] == e and Game.db[x+3][y+3] == d:
                        Game.got_3 = True
                        computer_next_move(x+2, y+2)

                    elif Game.db[x+2][y+2] == d and Game.db[x+3][y+3] == e:
                        Game.got_3 = True
                        computer_next_move(x+3, y+3)

                    elif Game.db[x+2][y+2] == e and Game.db[x+3][y+3] == e:
                        if Game.hard_mode and not Game.got_3:
                            computer_next_move(x+2, y+2)
        return False

    def horizontal_forward(self):
        d = self.disc
        e = "."
        # Check horizontal spaces
        for y in range(1, BOARD_HEIGHT):
            for x in range(Game.width - 3):
                if Game.db[x+3][y] == d and Game.db[x+2][y] == d:
                    if Game.db[x+1][y] == d and Game.db[x][y] == d:
                        # Turn the winning discs RED
                        Game.db[x][y] = RED_TEXT + d + GREEN_TEXT
                        Game.db[x+1][y] = RED_TEXT + d + GREEN_TEXT
                        Game.db[x+2][y] = RED_TEXT + d + GREEN_TEXT
                        Game.db[x+3][y] = RED_TEXT + d + GREEN_TEXT
                        return True

                    elif Game.db[x+1][y] == d and Game.db[x][y] == e:
                        Game.got_3 = True
                        computer_next_move(x, y)

                    elif Game.db[x+1][y] == e and Game.db[x][y] == d:
                        Game.got_3 = True
                        computer_next_move(x+1, y)

                    elif Game.db[x+1][y] == e and Game.db[x][y] == e:
                        if Game.hard_mode and not Game.got_3:
                            computer_next_move(x+1, y)
        return False

    def horizontal_backward(self):
        d = self.disc
        e = "."
        # Check horizontal spaces from other direction
        for y in range(1, BOARD_HEIGHT):
            for x in range(Game.width - 3):
                if Game.db[x][y] == d and Game.db[x+1][y] == d:
                    if Game.db[x+2][y] == d and Game.db[x+3][y] == e:
                        Game.got_3 = True
                        computer_next_move(x+3, y)

                    elif Game.db[x+2][y] == e and Game.db[x+3][y] == d:
                        Game.got_3 = True
                        computer_next_move(x+2, y)

                    elif Game.db[x+2][y] == e and Game.db[x+3][y] == e:
                        if Game.hard_mode and not Game.got_3:
                            computer_next_move(x+2, y)
        return False

    def vertical(self):
        d = self.disc
        e = "."
        # Check vertical spaces
        for x in range(Game.width):
            for y in range(1, (BOARD_HEIGHT - 3)):
                if Game.db[x][y+3] == d and Game.db[x][y+2] == d:
                    if Game.db[x][y+1] == d and Game.db[x][y] == d:
                        # Turn the winning discs RED
                        Game.db[x][y] = RED_TEXT + d + GREEN_TEXT
                        Game.db[x][y+1] = RED_TEXT + d + GREEN_TEXT
                        Game.db[x][y+2] = RED_TEXT + d + GREEN_TEXT
                        Game.db[x][y+3] = RED_TEXT + d + GREEN_TEXT
                        return True

                    elif Game.db[x][y+1] == d and Game.db[x][y] == e:
                        Game.got_3 = True
                        computer_next_move(x, y)

                    elif Game.db[x][y+1] == e and Game.db[x][y] == e:
                        if Game.hard_mode and not Game.got_3:
                            computer_next_move(x, y+1)
        return False


def check_winner(disc):
    """
    Checks to see if there are any connect 4 winners
    """
    check = BoardCheck(disc)

    if check.diag_right_forward() or check.diag_right_backward():
        return True
    elif check.diag_left_forward() or check.diag_left_backward():
        return True
    elif check.horizontal_forward() or check.horizontal_backward():
        return True
    elif check.vertical():
        return True
    else:
        return False


def reset_game():
    """
    Resets the working data and game board for a new game
    Increase or reset game level and board width
    """
    # Reset or adjust game level and board width
    if Game.winner:
        if Game.player_turn:
            # Player has won!
            Game.level += 1
            Game.width -= 1

        else:
            # Computer has won :(
            Game.level = 1
            Game.width = BOARD_WIDTH

    # Reset Everything else
    Game.player_turn = True
    Game.winner = False
    Game.disc_count = 0
    Game.next_move = 0
    Game.db = []

    # Add blank data into the Game.db column by column
    for i in range(Game.width):
        temp_board = []
        for ii in range(BOARD_HEIGHT):
            temp_board.append(" ") if ii == 0 else temp_board.append(".")

        Game.db.append(temp_board)


def clear():
    """
    Clear the Screen to help keep the game board clean and easy to read
    """
    print(GREEN_TEXT)
    _ = system('cls') if name == 'nt' else system('clear')


def logo():
    """
    Prints the Connect 4 logo text
    """
    print(LOGO_TEXT + """   _____                             _       ___
  /  __ \                           | |     /   |
  | /  \/ ___  _ __  _ __   ___  ___| |_   / /| |
  | |    / _ \| '_ \| '_ \ / _ \/ __| __| / /_| |
  | \__/\ (_) | | | | | | |  __/ (__| |_  \___  |
  \_____/\___/|_| |_|_| |_|\___|\___|\__|     |_/
    """ + GREEN_TEXT)


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
    disc_example = RED_TEXT + "O" + GREEN_TEXT
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

    choose_mode()

    # Begin the game!
    reset_game()
    game_board()
    enter_column_number()


def choose_mode():
    """
    Player chooses which game mode to play in. Hard or Easy!
    """
    print("                Make your choice:")
    input_text = "             [H]ard mode [E]asy mode\n"
    mode_input = input(input_text)
    valid_input = False

    while not valid_input:
        if mode_input.lower() == "h" or mode_input.lower() == "hard":
            # Player wants to play with hard mode
            print("      HARD MODE!   YOU MANIAC!!!! :-o\n")
            sleep(DELAY_TIME*7)
            Game.hard_mode = True
            valid_input = True

        elif mode_input.lower() == "e" or mode_input.lower() == "easy":
            # Player wants to play with easy mode
            valid_input = True

        else:
            print("     Not a valid input.. Try again!..\n")
            sleep(DELAY_TIME*6)
            clear()
            logo()
            reset_game()
            game_board()
            sleep(DELAY_TIME)
            print("                Make your choice:")
            input_text = "             [H]ard mode [E]asy mode\n"
            mode_input = input(input_text)


def drop_disc(column):
    """
    Animates the dropping of the player disc
    Updates the board data with current disc locations
    """
    disc = "O" if Game.player_turn else "X"
    column -= 1
    bottom = BOARD_HEIGHT - 1

    # Finds the the next available square to determine the bottom
    while Game.db[column][bottom] != ".":
        bottom -= 1

    # Places disc in the next square down and refreshes the board
    for i in range(bottom + 1):
        Game.db[column][i] = disc
        game_board()

        # Determines if it's blank space or a . to replace
        if i == 0:
            sleep(DELAY_TIME*2)
            Game.db[column][i] = " "

        elif i == bottom:
            # Disc has reached the bottom
            sleep(DROP_SPEED)

        else:
            sleep(DROP_SPEED)
            Game.db[column][i] = "."

    next_turn()


def next_turn():
    """
    Check for winner, if not, swap the player turn, check for draw
    """
    # Reset next computer move
    Game.next_move = 0

    if check_winner("O") or check_winner("X"):
        # Game has a winner so handle that
        Game.winner = True
        game_board()
        we_have_a_winner()

    else:
        if Game.player_turn:
            # The last turn was the players so change it
            Game.player_turn = False
            check_draw()
            game_board()
            computer_turn()

        else:
            # The last turn was the computer's so change it
            Game.player_turn = True
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
    for i in range(Game.width - 1):
        margin_len -= 2 if i % 2 == 0 else 1

    # Make sure the margin is never less than 0 spaces wide
    margin = space * margin_len if margin_len > 0 else ""

    # Print the column numbers
    board_line = margin + three_spaces

    for i in range(1, Game.width + 1):
        if i < 10:
            board_line += (str(i) + three_spaces)

        else:
            board_line += (str(i) + space + space)

    print(board_line)

    # Print the columns
    for i in range(BOARD_HEIGHT):
        board_line = margin

        # Print the walls in the main area. None for the top
        for ii in range(Game.width):
            board_line += three_spaces if i == 0 else wall
            board_line += Game.db[ii][i]

        # Prints walls or spaces depending which line is processing
        board_line += three_spaces if i == 0 else wall
        print(board_line)

    game_status()


def game_status():
    """
    Prints the status of the game
    """
    space = "        " if Game.level < 10 else "       "
    status = f"\n    Level: {Game.level}{space}"
    hard_text = "HARD Mode   "
    easy_text = "Easy Mode   "
    user_winn = "      You WON!!\n"
    user_turn = "      Your Turn\n"
    comp_winn = "   Computer Won\n"
    comp_turn = "Computer's Turn\n"

    # Put the status in order

    status += hard_text if Game.hard_mode else easy_text

    if Game.player_turn:
        status += user_winn if Game.winner else user_turn

    else:
        status += comp_winn if Game.winner else comp_turn

    print(status)


def enter_column_number():
    """
    Lets the user enter their column choice, checks it's a
    number and checks that there's space left in that column
    """
    column_choice = 0
    column_full = True
    column_range = Game.width + 1

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

            elif column_choice == 22222:
                # Easy High level for dev purposes
                Game.level = 8
                print("   CHEATER!!")
                sleep(DELAY_TIME*5)
                game_board()

            elif column_choice == 42:
                # Easter egg! Because I like the book
                print("   Answer to the Ultimate Question of Life,")
                print("               The Universe, and Everything\n")
                sleep(DELAY_TIME*9)
                game_board()

            elif column_choice not in range(1, column_range):
                # Handle when input number not an available column
                warn = "Please only enter a number between 1 and"
                print("   ", warn, Game.width)
                sleep(DELAY_TIME*4)
                game_board()

            elif Game.db[column_choice-1][1] != ".":
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
    global got_3

    if Game.next_move > 0:
        # Go where was suggested
        column_choice = Game.next_move
    else:
        # Choose a random column
        column_choice = random.randint(1, Game.width)

    # The chosen column is full so choose again
    while Game.db[column_choice-1][1] is not ".":
        column_choice = random.randint(1, Game.width)

    sleep(DELAY_TIME)
    Game.got_3 = False
    drop_disc(column_choice)


def computer_next_move(column, row):
    """
    Tells the computer the next best place to go to beat the player
    """
    # Check if there's a supporting disc in that square
    try:
        if Game.db[column][row + 1] is not ".":
            # There is a supporting disc in that square so we can go
            Game.next_move = column + 1

    except IndexError:
        # The square requested is off the board so we can go
        Game.next_move = column + 1


def we_have_a_winner():
    """
    We have a winner!
    Tell the player who has won
    """
    win_text = "   WE HAVE A WINNER!!\n"
    user_win = "   You've beaten the computer!\n"
    comp_win = "   You didn't win this time :(\n"

    win_text += user_win if Game.player_turn else comp_win

    if Game.level < (BOARD_WIDTH - 2):
        print(win_text)
        sleep(DELAY_TIME*4)

    play_again()


def play_again():
    """
    Ask if player wants to play again and check their input is valid
    """
    sleep(DELAY_TIME)
    game_board()
    mode_choice = False

    input_text = "   Do you want to "

    # Reset game level after they've won the game
    if Game.level >= WIN_LEVEL and Game.winner:
        top_level()
        input_text += "play again?"
        mode_choice = True

    else:
        input_text += "continue playing?"

    input_text += " \n   [Y]es or [N]o\n"
    play_again_input = input(input_text)
    valid_input = False

    while not valid_input:
        if play_again_input.lower() == "n" or play_again_input.lower() == "no":
            # Player wants to end the game so quit
            valid_input = True
            print("   OK, Thank you for playing. Come back soon!! :)\n")
            quit()

        elif play_again_input.lower() == "y" or play_again_input.lower() == "yes":
            # Player wants to play again so reset and start the game
            valid_input = True
            print("   OK, resetting game...")
            sleep(DELAY_TIME)
            reset_game()
            game_board()
            _ = choose_mode() if mode_choice else None
            game_board()
            enter_column_number()

        else:
            # Player wants to play again so reset and start the game
            print("   Not a valid input...")
            sleep(DELAY_TIME*6)
            clear()
            game_board()
            play_again_input = input(input_text)


def check_draw():
    """
    Increments the disc count
    Checks to see if the board is full without any winners
    """
    Game.disc_count += 1

    # Calculate the max number of squares based on board size
    board_max = (BOARD_HEIGHT-1) * Game.width

    if Game.disc_count >= board_max:
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
    game_won = "               YOU BEAT THE GAME!!!\n"
    game_won += "          VERY well done! I'm impressed!"
    print(game_won)

    sleep(DELAY_TIME*10)
    game_board()
    Game.winner = False
    Game.level = 1
    Game.width = BOARD_WIDTH


welcome()
