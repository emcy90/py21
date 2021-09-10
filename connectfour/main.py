from terminal_color import color_print


def drop_discs(col, row, player_in_turn):
    is_empty = True
    while is_empty:
        if board[5][col] == 0:
            board[5][col] = player_in_turn



def main():
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 2, 0, 0, 0]
    ]

    player_in_turn = 1
    running = True
    while running:
        for row in board:
            for cell in row:
                color = "white"
                if cell == 1:
                    color = "magenta"
                elif cell == 2:
                    color = "cyan"
                color_print(color, "0", end=" ")
            print()
        color_print("green", "A B C D E F G")

        print("please select a column(A-G) ")
        move = input(f"Player {player_in_turn}, pick a column: ")
        if move == "a":
            col = 0
        elif move == "b":
            col = 1
        elif move == "c":
            col = 2
        elif move == "d":
            col = 3
        elif move == "e":
            col = 4
        elif move == "f":
            col = 5
        elif move == "g":
            col = 6
        else:
            print("invalid input please use accepted coloumn letters you bastard!!!½!")



        #if player_in_turn is 1 change to 2 before loop begins again else change to 1 since only 2 players
        player_in_turn = 2 if player_in_turn == 1 else 1


if __name__ == '__main__':
    main()
