from terminal_color import color_print


def main():
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]

    running = True
    while running:
        print("please select a column(A-F) ")
        choice = input("> ")
        main_choice = choice.lower():
        if main_choice == "a":


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


if __name__ == '__main__':
    main()
