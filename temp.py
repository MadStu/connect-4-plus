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
