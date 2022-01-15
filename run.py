from os import system, name
from time import sleep
import random
import math
import csv

# Set Recursion limit higher for the AI
from sys import setrecursionlimit
setrecursionlimit(2500)

# Board starting grid size. Height includes the top blank row
BOARD_HEIGHT = 7
BOARD_WIDTH = 12

# Delay time of items being shown
DELAY_TIME = 0.15

# Speed at which the disc drops down
DROP_SPEED = 0.06

# Text Styles
RED_TEXT = "\033[1;31;48m"
GREEN_TEXT = "\033[1;32;48m"
LOGO_TEXT = "\033[0;32;48m"
NAME_TEXT = "\033[0;31;48m"

# Winning game level
WIN_LEVEL = BOARD_WIDTH - 3

# How many points are deducted for each square
# Multiplied by the game level
BASE_POINTS = 2

# Location of the .csv file for holding the top scores
CSV = "scores.csv"


class TopScores:
    """
    Handle the Top Scores Data
    """
    def read():
        """
        Read the top scores data and make a list
        """
        # Empty the current list first
        Game.top_scores = []

        # Open and read .csv line by line
        with open(CSV, encoding="utf8") as f:
            csv_reader = csv.reader(f)
            for i, line in enumerate(csv_reader):
                Game.top_scores.append(line)
                Game.top_scores[i][0] = int(Game.top_scores[i][0])

        # Sort, then reverse the list
        Game.top_scores.sort()
        Game.top_scores.reverse()

    def write():
        """
        Replace the top scores with latest data
        """
        with open(CSV, 'w', encoding='utf8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(Game.top_scores)

    def display():
        """
        Display the Top Scores!
        """
        TopScores.read()
        clear()
        logo()

        side_text = "TOP SCORES"

        margin = 7
        i = 0

        # Print scoreboard line by line
        while i < 10:
            line_text = ""
            if i == 0:
                ord = "st"
            elif i == 1:
                ord = "nd"
            elif i == 2:
                ord = "rd"
            elif i == 9:
                margin = 6
            else:
                ord = "th"
            line_text += "  " + side_text[i]
            line_text += margin * " "
            line_text += str(i+1) + ord + "   |"
            line_text += (7 - len(str(Game.top_scores[i][0]))) * " "
            line_text += str(Game.top_scores[i][0])
            line_text += " Points   |   " + Game.top_scores[i][1].upper()
            print(line_text)
            i += 1

    def add():
        """
        Add player score to the Game.top_scores list
        """
        # Temp list for appending to main list
        temp_list = []
        temp_list.append(Game.score)
        temp_list.append(Game.player_name)

        # Temp list for sorting the main list in order of high score
        temp_list2 = Game.top_scores
        temp_list2.append(temp_list)
        temp_list2.sort(reverse=True)

        # Empty main scoreboard and limit to the top 10 scores
        Game.top_scores = []
        i = 0
        while i < 10:
            Game.top_scores.append(temp_list2[i])
            i += 1

        # Update the csv with new values
        TopScores.write()


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
    player_name = "hal"
    score = 0
    top_scores = []


class BoardCheck:
    """
    Holds the functions that check the board for any potential
    or actual connect 4 winning lines

    The following code has been modified but was originally from line 69 of
    https://github.com/justinvallely/Python-Connect-4/
    """
    def __init__(self, disc):
        self.disc = disc

    def diag_right_forward(self):
        """
        d = player disc and e = empty
        Shortened to satisfy the pep8 line length warnings

        Checks if there's any winning lines of 4
        Changes the colour of the winning discs

        Also checks for free spaces for the computer to stop player winning
        """
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
        """
        d = player disc and e = empty
        Shortened to satisfy the pep8 line length warnings

        Checks if there's any winning lines of 4
        Changes the colour of the winning discs

        Also checks for free spaces for the computer to stop player winning
        """
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
        """
        d = player disc and e = empty
        Shortened to satisfy the pep8 line length warnings

        Checks if there's any winning lines of 4
        Changes the colour of the winning discs

        Also checks for free spaces for the computer to stop player winning
        """
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
        """
        d = player disc and e = empty
        Shortened to satisfy the pep8 line length warnings

        Checks if there's any winning lines of 4
        Changes the colour of the winning discs

        Also checks for free spaces for the computer to stop player winning
        """
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
        """
        d = player disc and e = empty
        Shortened to satisfy the pep8 line length warnings

        Checks if there's any winning lines of 4
        Changes the colour of the winning discs

        Also checks for free spaces for the computer to stop player winning
        """
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
        """
        d = player disc and e = empty
        Shortened to satisfy the pep8 line length warnings

        Checks if there's any winning lines of 4
        Changes the colour of the winning discs

        Also checks for free spaces for the computer to stop player winning
        """
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
        """
        d = player disc and e = empty
        Shortened to satisfy the pep8 line length warnings

        Checks if there's any winning lines of 4
        Changes the colour of the winning discs

        Also checks for free spaces for the computer to stop player winning
        """
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


class letters:
    """
    Character Codes for each letter
    """
    dict = {
        "a": ["            ", "     /\     ", "    /  \    ", "   / /\ \   ",
              "  / ____ \  ", " /_/    \_\ "],
        "b": ["  ____   ", " |  _ \  ", " | |_) | ", " |  _ <  ", " | |_) | ",
              " |____/  "],
        "c": ["   _____  ", "  / ____| ", " | |      ", " | |      ",
              " | |____  ", "  \_____| "],
        "d": ["  _____   ", " |  __ \  ", " | |  | | ", " | |  | | ",
              " | |__| | ", " |_____/  "],
        "e": ["  ______  ", " |  ____| ", " | |__    ", " |  __|   ",
              " | |____  ", " |______| "],
        "f": ["  ______  ", " |  ____| ", " | |__    ", " |  __|   ",
              " | |      ", " |_|      "],
        "g": ["   _____  ", "  / ____| ", " | |  __  ", " | | |_ | ",
              " | |__| | ", "  \_____| "],
        "h": ["  _    _  ", " | |  | | ", " | |__| | ", " |  __  | ",
              " | |  | | ", " |_|  |_| "],
        "i": ["  _____  ", " |_   _| ", "   | |   ", "   | |   ", "  _| |_  ",
              " |_____| "],
        "j": ["       _  ", "      | | ", "      | | ", "  _   | | ",
              " | |__| | ", "  \____/  "],
        "k": ["  _  __ ", " | |/ / ", " | ' /  ", " |  <   ", " | . \  ",
              " |_|\_\ "],
        "l": ["  _       ", " | |      ", " | |      ", " | |      ",
              " | |____  ", " |______| "],
        "m": ["  __  __  ", " |  \/  | ", " | \  / | ", " | |\/| | ",
              " | |  | | ", " |_|  |_| "],
        "n": ["  _   _  ", " | \ | | ", " |  \| | ", " | . ` | ", " | |\  | ",
              " |_| \_| "],
        "o": ["   ____   ", "  / __ \  ", " | |  | | ", " | |  | | ",
              " | |__| | ", "  \____/  "],
        "p": ["  _____   ", " |  __ \  ", " | |__) | ", " |  ___/  ",
              " | |      ", " |_|      "],
        "q": ["   ____   ", "  / __ \  ", " | |  | | ", " | |  | | ",
              " | |__| | ", "  \___\_\ "],
        "r": ["  _____   ", " |  __ \  ", " | |__) | ", " |  _  /  ",
              " | | \ \  ", " |_|  \_\ "],
        "s": ["   _____  ", "  / ____| ", " | (___   ", "  \___ \  ",
              "  ____) | ", " |_____/  "],
        "t": ["  _______  ", " |__   __| ", "    | |    ", "    | |    ",
              "    | |    ", "    |_|    "],
        "u": ["  _    _  ", " | |  | | ", " | |  | | ", " | |  | | ",
              " | |__| | ", "  \____/  "],
        "v": [" __      __ ", " \ \    / / ", "  \ \  / /  ", "   \ \/ /   ",
              "    \  /    ", "     \/     "],
        "w": [" __          __ ", " \ \        / / ", "  \ \  /\  / /  ",
              "   \ \/  \/ /   ", "    \  /\  /    ", "     \/  \/     "],
        "x": [" __   __ ", " \ \ / / ", "  \ V /  ", "   > <   ", "  / . \  ",
              " /_/ \_\ "],
        "y": [" __     __ ", " \ \   / / ", "  \ \_/ /  ", "   \   /   ",
              "    | |    ", "    |_|    "],
        "z": ["  ______ ", " |___  / ", "    / /  ", "   / /   ", "  / /__  ",
              " /_____| "]
    }


def enter_name():
    """
    Player can enter their name
    """
    name_check = False
    while not name_check:
        clear()
        logo()
        sleep(DELAY_TIME)

        input_text = "\n        Enter your 3 letter name (eg: STU):\n"
        name_input = input(input_text)

        # Check it's A-z and at least 3 letters long
        while not name_input.isalpha() or len(name_input) < 3:
            print("   Only A-Z are allowed and 3 letters length...")
            sleep(DELAY_TIME*10)
            clear()
            logo()
            name_input = input(input_text)

        clear()
        logo()
        sleep(DELAY_TIME)

        i = 0
        # Print the name in big ascii art letters
        while i < 6:
            name = NAME_TEXT + " " * 10
            name += letters.dict[name_input[0].lower()][i]
            name += letters.dict[name_input[1].lower()][i]
            name += letters.dict[name_input[2].lower()][i]
            name += GREEN_TEXT
            print(name)
            i += 1

        sleep(DELAY_TIME)
        print("\n               Is this your name?")
        check_name = input("                 [Y]es or [N]o?\n")
        if check_name.lower() == "y" or check_name.lower() == "yes":
            name_check = True
            Game.player_name = name_input[0:3].lower()


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
            if Game.level >= WIN_LEVEL:
                Game.level = 1
                Game.width = BOARD_WIDTH
                Game.score = 0
            else:
                Game.level += 1
                Game.width -= 1

        else:
            # Hal has won :(
            Game.level = 1
            Game.width = BOARD_WIDTH
            Game.score = 0

    # Add relevant points to the score based on current board size,
    # game level and difficulty mode
    board_max = (BOARD_HEIGHT-1) * Game.width
    board_score = math.floor((board_max / 2) * (BASE_POINTS * Game.level))
    board_score += board_score if Game.hard_mode else 0
    Game.score += board_score

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
    Ask player if they want to view the rules
    """
    clear()
    logo()
    sleep(DELAY_TIME)

    print("\n                 Make your choice:")
    input_text = "      [P]lay game or read the [I]nstructions\n"
    first = input(input_text)
    valid_input = False

    while not valid_input:
        if first.lower() == "p" or first.lower() == "play":
            valid_input = True

        elif first.lower() == "i" or first.lower() == "instructions":
            valid_input = True
            welcome_text()

        else:
            print("   Not a valid input...")
            sleep(DELAY_TIME*10)
            clear()
            logo()
            print("\n                 Make your choice:")
            first = input(input_text)

    sleep(DELAY_TIME)
    enter_name()
    sleep(DELAY_TIME)
    choose_mode()
    sleep(DELAY_TIME)
    reset_game()
    TopScores.display()
    print("\n   The scores to beat!!!")
    sleep(DELAY_TIME*30)
    game_board()

    # Begin the game!
    enter_column_number()


def welcome_text():
    """
    Display the welcome text and games rules
    """
    clear()
    logo()
    sleep(DELAY_TIME)

    print("   WELCOME to the fun game of Connect 4!\n")
    sleep(DELAY_TIME)

    print("""   The game is easy, you'll take turns with
   Hal (the computer) to place your discs which
   fall into each column, in this game you'll
   play with X's and O's.

   You will be O and Hal will be X.\n""")

    sleep(DELAY_TIME)
    input("   Press Enter to continue...\n")
    clear()
    logo()

    sleep(DELAY_TIME)
    print("""   1   2   3   4   5   6   7   8   9   10  11  12

 | . | . | . | . | . | . | . | . | . | . | . | . |
 | . | . | . | . | . | . | . | . | . | . | . | . |\n""")
    sleep(DELAY_TIME)
    print("""   Each column is numbered from left to right.
   You'll need to enter a column number in which
   to drop your disc.\n""")

    sleep(DELAY_TIME)
    input("   Press Enter to continue...\n")
    clear()
    logo()

    sleep(DELAY_TIME)
    disc_example = RED_TEXT + "O" + GREEN_TEXT
    print(f"""   1   2   3   4   5   6   7   8   9   10  11  12

 | . | . | . | . | . | . | {disc_example} | . | . | . | . | . |
 | . | . | . | . | . | {disc_example} | X | . | X | . | . | . |
 | O | X | . | . | {disc_example} | X | O | . | O | O | . | . |
 | X | X | X | {disc_example} | X | O | O | O | X | O | X | . |\n""")
    sleep(DELAY_TIME)
    print("""   When you connect 4 in a line (as shown above)
   or in any other direction, you win the game!\n""")

    sleep(DELAY_TIME)
    input("   Press Enter to continue...\n")
    clear()
    logo()

    sleep(DELAY_TIME)
    print("""   1   2   3   4   5   6   7   8   9   10  11  12

 | . | . | . | . | . | . | . | . | . | . | . | . |
 | . | . | . | . | . | . | . | . | . | . | . | . |""")
    game_status()
    sleep(DELAY_TIME)
    print(f"""   You'll start on Level 1 and your goal is to
   beat Hal by completing level {WIN_LEVEL}. The game board
   will narrow each time you level up, increasing
   the difficulty.\n""")

    sleep(DELAY_TIME)
    input("   Press Enter to continue...\n")


def choose_mode():
    """
    Player chooses which game mode to play in. Hard or Easy!
    """
    clear()
    logo()
    p_name = Game.player_name.capitalize()
    print(f"              Make your choice, {p_name}:")
    input_text = "             [H]ard mode [E]asy mode\n"
    mode_input = input(input_text)
    valid_input = False

    while not valid_input:
        if mode_input.lower() == "h" or mode_input.lower() == "hard":
            # Player wants to play with hard mode
            Game.hard_mode = True
            clear()
            logo()
            print(f"    HARD MODE! {p_name.upper()} YOU MANIAC!!!! :-o\n")
            sleep(DELAY_TIME*10)
            valid_input = True

        elif mode_input.lower() == "e" or mode_input.lower() == "easy":
            # Player wants to play with easy mode
            valid_input = True
            Game.hard_mode = False

        else:
            print("     Not a valid input.. Try again!..\n")
            sleep(DELAY_TIME*1)
            clear()
            logo()
            print(f"              Make your choice, {p_name}:")
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
    p_name = Game.player_name.capitalize()
    space = "   " if Game.level < 10 else "  "
    status = f"\n   Level: {Game.level}{space}"
    hard_text = "HARD Mode"
    easy_text = "Easy Mode"
    user_winn = f"    {p_name.upper()} WON!!"
    user_turn = f"   {p_name}'s Turn"
    comp_winn = "      Hal Won"
    comp_turn = "   Hal's Turn"
    scor_text = f"   Score: {Game.score}\n"

    # Put the status in order
    status += hard_text if Game.hard_mode else easy_text

    if Game.player_turn:
        status += user_winn if Game.winner else user_turn

    else:
        status += comp_winn if Game.winner else comp_turn

    status += scor_text
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
            game_board()
            column_choice = int(input("   Enter your column choice...\n"))

        except ValueError:
            # Handle the error if it's not a number
            game_board()
            print("   Not a number")
            sleep(DELAY_TIME*10)
            game_board()

        finally:
            if column_choice == 999:
                # Easy quit game code for dev purposes
                game_board()
                print("Thanks for playing")
                quit()

            elif column_choice == 22222:
                # Easy High level for dev purposes
                game_board()
                Game.level = WIN_LEVEL
                print("   CHEATER!!")
                sleep(DELAY_TIME*10)
                game_board()

            elif column_choice == 88:
                # Go where the computer would have gone cheat
                game_board()
                move = Game.next_move
                cheat_yes = f"   (Try {move})"
                cheat_no = "   Cheats never prosper..."
                cheat_text = "   CHEATER!!"
                cheat_text += cheat_yes if move > 0 else cheat_no
                print(cheat_text)
                sleep(DELAY_TIME*10)

                # The cost of cheating!
                cheat_points = (BASE_POINTS * Game.level) * 2
                cheat_points += cheat_points if Game.hard_mode else 0
                Game.score -= cheat_points

            elif column_choice == 42:
                # Easter egg! Because I like the book
                game_board()
                print("   Answer to the Ultimate Question of Life,")
                print("               The Universe, and Everything")
                sleep(DELAY_TIME*10)
                game_board()

            elif column_choice == 9000:
                # Easter egg! Because I LOVE the film
                game_board()
                print("   I'm sorry Dave, I'm afraid I can't do that.")
                sleep(DELAY_TIME*10)
                game_board()

            elif column_choice not in range(1, column_range):
                # Handle when input number not an available column
                game_board()
                warn = "Please only enter a number between 1 and"
                print("   ", warn, Game.width)
                sleep(DELAY_TIME*10)
                game_board()

            elif Game.db[column_choice-1][1] != ".":
                # Check to see if the column is full
                game_board()
                print("   That column is full!")
                sleep(DELAY_TIME*10)
                game_board()

            else:
                column_full = False

    drop_disc(column_choice)


def computer_turn():
    """
    Chooses the previously next move
    If no next move defined, choose a random square
    Check to see if that column is available
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
    user_win = "   You've beaten the computer!"
    comp_win = "   You didn't win this time :("

    win_text += user_win if Game.player_turn else comp_win

    if Game.level < WIN_LEVEL:
        game_board()
        print(win_text)
        sleep(DELAY_TIME*10)

    play_again()


def play_again():
    """
    Ask if player wants to play again and check their input is valid
    """
    sleep(DELAY_TIME)
    TopScores.display()
    mode_choice = False

    input_text = "\n   Would you like to "

    # Reset game level after they've won the game
    if Game.level >= WIN_LEVEL and Game.winner and Game.player_turn:
        top_level()
        input_text += "play again?"
        mode_choice = True

    else:
        input_text += "continue playing?"

    input_text += " \n   [Y]es or [N]o"
    input_text += f"        Your Score: {RED_TEXT}{Game.score}{GREEN_TEXT}\n"
    play_again_inp = input(input_text)
    valid_input = False

    while not valid_input:
        if play_again_inp.lower() == "n" or play_again_inp.lower() == "no":
            # Player wants to end the game so quit
            valid_input = True

            if Game.score > Game.top_scores[9][0]:
                if Game.level < WIN_LEVEL:
                    print("Your score was added to the scoreboard!")
                    sleep(DELAY_TIME*10)
                    TopScores.add()
            TopScores.display()
            print("\n   OK, Thank you for playing. Come back soon!! :)\n")
            quit()

        elif play_again_inp.lower() == "y" or play_again_inp.lower() == "yes":
            # Player wants to play again so reset and start the game
            valid_input = True

            # Add Score if conditions are met
            if Game.score > Game.top_scores[9][0] and Game.winner:
                if Game.level < WIN_LEVEL and not Game.player_turn:

                    # Calculate the max number of squares based on board size
                    board_max = (BOARD_HEIGHT-1) * Game.width

                    # Determine free moves left
                    moves_left = (board_max / 2) - Game.disc_count

                    # Determine points per move
                    points = BASE_POINTS * Game.level
                    points += points if Game.hard_mode else 0

                    # Remove these points from player score - loser
                    Game.score -= points * moves_left

                    print("Your score was added to the scoreboard!")
                    sleep(DELAY_TIME*10)
                    TopScores.add()
            TopScores.display()
            print("\n   OK, resetting game...")
            sleep(DELAY_TIME*10)
            reset_game()
            game_board()
            _ = choose_mode() if mode_choice else None
            game_board()
            enter_column_number()

        else:
            # Not a valid input
            TopScores.display()
            print("\n   Not a valid input...")
            sleep(DELAY_TIME*10)
            TopScores.display()
            play_again_inp = input(input_text)


def check_draw():
    """
    Increments the disc count
    Checks to see if the board is full without any winners
    """
    Game.disc_count += 1

    # Calculate the max number of squares based on board size
    board_max = (BOARD_HEIGHT-1) * Game.width

    if Game.player_turn:
        # Deduct points from score each turn
        points = BASE_POINTS * Game.level
        points += points if Game.hard_mode else 0
        Game.score -= points

    if Game.disc_count >= board_max:
        # Game's a draw so handle that
        game_board()
        print("   No winners this time :(\n")
        print("             Try again!\n")
        sleep(DELAY_TIME*10)
        play_again()


def top_level():
    """
    When player reaches top level they are told they've won the game
    and everything is reset
    """
    clear()
    logo()
    name = Game.player_name.capitalize()

    i = 0
    while i < 6:
        name = NAME_TEXT + " " * 10
        name += letters.dict[Game.player_name[0]][i]
        name += letters.dict[Game.player_name[1]][i]
        name += letters.dict[Game.player_name[2]][i]
        name += GREEN_TEXT
        print(name)
        i += 1

    game_won = "\n                   YOU BEAT HAL!!!\n"
    game_won += f"""   I'm afraid. I'm afraid, {name}. {name}, my mind is
   going. I can feel it. I can feel it. My mind is
   going. There is no question about it. I can feel
   it. I can feel it. I can feel it. I'm a... fraid."""
    print(game_won)

    sleep(10)
    TopScores.add()
    TopScores.display()


welcome()
