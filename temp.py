def check_winner(d):
    """
    d = disc - shortened to satisfy the pep8 line length warnings
    Checks if there's any winning lines of 4
    Changes the colour of the winning discs

    Also checks for free spaces for the computer to stop player winning

    The following code has been modified but was originally from line 69 of
    https://github.com/justinvallely/Python-Connect-4/
    """
    # Check / diagonal spaces
    for x in range(g_state.width - 3):
        for y in range(4, BOARD_HEIGHT):
            if g_state.db[x+3][y-3] == d and g_state.db[x+2][y-2] == d:
                if g_state.db[x+1][y-1] == d and g_state.db[x][y] == d:
                    # Turn the winning discs RED
                    g_state.db[x][y] = "\033[1;31;48m"+d+"\033[1;32;48m"
                    g_state.db[x+1][y-1] = "\033[1;31;48m"+d+"\033[1;32;48m"
                    g_state.db[x+2][y-2] = "\033[1;31;48m"+d+"\033[1;32;48m"
                    g_state.db[x+3][y-3] = "\033[1;31;48m"+d+"\033[1;32;48m"
                    return True

                elif g_state.db[x+1][y-1] == "." and g_state.db[x][y] == d:
                    g_state.got_3 = True
                    computer_next_move(x+1, y-1)

                elif g_state.db[x+1][y-1] == d and g_state.db[x][y] == ".":
                    g_state.got_3 = True
                    computer_next_move(x, y)

                elif g_state.db[x+1][y-1] == "." and g_state.db[x][y] == ".":
                    if g_state.hard_mode and g_state.got_3 is not True:
                        computer_next_move(x+1, y-1)

    # Check / diagonal spaces from other direction
    for x in range(g_state.width - 3):
        for y in range(4, BOARD_HEIGHT):
            if g_state.db[x][y] == d and g_state.db[x+1][y-1] == d:
                if g_state.db[x+2][y-2] == "." and g_state.db[x+3][y-3] == d:
                    g_state.got_3 = True
                    computer_next_move(x+2, y-2)

                elif g_state.db[x+2][y-2] == d and g_state.db[x+3][y-3] == ".":
                    g_state.got_3 = True
                    computer_next_move(x+3, y-3)

                elif g_state.db[x+2][y-2] == "." and g_state.db[x+3][y-3] == ".":
                    if g_state.hard_mode and g_state.got_3 is not True:
                        computer_next_move(x+2, y-2)

    # Check \ diagonal spaces
    for x in range(g_state.width - 3):
        for y in range(1, (BOARD_HEIGHT - 3)):
            if g_state.db[x+3][y+3] == d and g_state.db[x+2][y+2] == d:
                if g_state.db[x+1][y+1] == d and g_state.db[x][y] == d:
                    # Turn the winning discs RED
                    g_state.db[x][y] = "\033[1;31;48m"+d+"\033[1;32;48m"
                    g_state.db[x+1][y+1] = "\033[1;31;48m"+d+"\033[1;32;48m"
                    g_state.db[x+2][y+2] = "\033[1;31;48m"+d+"\033[1;32;48m"
                    g_state.db[x+3][y+3] = "\033[1;31;48m"+d+"\033[1;32;48m"
                    return True

                elif g_state.db[x+1][y+1] == "." and g_state.db[x][y] == d:
                    g_state.got_3 = True
                    computer_next_move(x+1, y+1)

                elif g_state.db[x+1][y+1] == d and g_state.db[x][y] == ".":
                    g_state.got_3 = True
                    computer_next_move(x, y)

                elif g_state.db[x+1][y+1] == "." and g_state.db[x][y] == ".":
                    if g_state.hard_mode and g_state.got_3 is not True:
                        computer_next_move(x+1, y+1)

    # Check \ diagonal spaces from other direction
    for x in range(g_state.width - 3):
        for y in range(1, (BOARD_HEIGHT - 3)):
            if g_state.db[x][y] == d and g_state.db[x+1][y+1] == d:
                if g_state.db[x+2][y+2] == "." and g_state.db[x+3][y+3] == d:
                    g_state.got_3 = True
                    computer_next_move(x+2, y+2)

                elif g_state.db[x+2][y+2] == d and g_state.db[x+3][y+3] == ".":
                    g_state.got_3 = True
                    computer_next_move(x+3, y+3)

                elif g_state.db[x+2][y+2] == "." and g_state.db[x+3][y+3] == ".":
                    if g_state.hard_mode and g_state.got_3 is not True:
                        computer_next_move(x+2, y+2)

    # Check horizontal spaces
    for y in range(1, BOARD_HEIGHT):
        for x in range(g_state.width - 3):
            if g_state.db[x+3][y] == d and g_state.db[x+2][y] == d:
                if g_state.db[x+1][y] == d and g_state.db[x][y] == d:
                    # Turn the winning discs RED
                    g_state.db[x][y] = "\033[1;31;48m"+d+"\033[1;32;48m"
                    g_state.db[x+1][y] = "\033[1;31;48m"+d+"\033[1;32;48m"
                    g_state.db[x+2][y] = "\033[1;31;48m"+d+"\033[1;32;48m"
                    g_state.db[x+3][y] = "\033[1;31;48m"+d+"\033[1;32;48m"
                    return True

                elif g_state.db[x+1][y] == d and g_state.db[x][y] == ".":
                    g_state.got_3 = True
                    computer_next_move(x, y)

                elif g_state.db[x+1][y] == "." and g_state.db[x][y] == d:
                    g_state.got_3 = True
                    computer_next_move(x+1, y)

                elif g_state.db[x+1][y] == "." and g_state.db[x][y] == ".":
                    if g_state.hard_mode and g_state.got_3 is not True:
                        computer_next_move(x+1, y)

    # Check horizontal spaces from other direction
    for y in range(1, BOARD_HEIGHT):
        for x in range(g_state.width - 3):
            if g_state.db[x][y] == d and g_state.db[x+1][y] == d:
                if g_state.db[x+2][y] == d and g_state.db[x+3][y] == ".":
                    g_state.got_3 = True
                    computer_next_move(x+3, y)

                elif g_state.db[x+2][y] == "." and g_state.db[x+3][y] == d:
                    g_state.got_3 = True
                    computer_next_move(x+2, y)

                elif g_state.db[x+2][y] == "." and g_state.db[x+3][y] == ".":
                    if g_state.hard_mode and g_state.got_3 is not True:
                        computer_next_move(x+2, y)

    # Check vertical spaces
    for x in range(g_state.width):
        for y in range(1, (BOARD_HEIGHT - 3)):
            if g_state.db[x][y+3] == d and g_state.db[x][y+2] == d:
                if g_state.db[x][y+1] == d and g_state.db[x][y] == d:
                    # Turn the winning discs RED
                    g_state.db[x][y] = "\033[1;31;48m"+d+"\033[1;32;48m"
                    g_state.db[x][y+1] = "\033[1;31;48m"+d+"\033[1;32;48m"
                    g_state.db[x][y+2] = "\033[1;31;48m"+d+"\033[1;32;48m"
                    g_state.db[x][y+3] = "\033[1;31;48m"+d+"\033[1;32;48m"
                    return True

                elif g_state.db[x][y+1] == d and g_state.db[x][y] == ".":
                    g_state.got_3 = True
                    computer_next_move(x, y)

                elif g_state.db[x][y+1] == "." and g_state.db[x][y] == ".":
                    if g_state.hard_mode and g_state.got_3 is not True:
                        computer_next_move(x, y+1)

    return False