
def drop_disc(column):
    """
    Animates the dropping of the player disc
    Updates the board data with disc locations
    """
    sleep(drop_speed)
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

