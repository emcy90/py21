from rooms import the_map


def go(row, col, direction):
    if direction in the_map[row][col]['exits']:
        if direction == "north":
            row -= 1
        elif direction == "south":
            row += 1
        elif direction == "east":
            col -= 1
        elif direction == "west":
            col += 1
    else:
        print("You can't go in that direction. try again")
    return row, col


def get(row, col, item, inventory):
    if item in the_map[row][col]['items']:
        print("you picked up the", inventory)
        the_map[row][col]['items'].remove(item)
        inventory.append(item)
    else:
        print("There is no", inventory, "in this room")


def main():
    row = 0
    col = 0
    running = True
    print("Welcome to the Zelda text adventure")
    inventory = []

    while running:
        print("You are now in", the_map[row][col]['description'])
        print("Items available here are ", the_map[row][col]['items'])
        print("There are exits to the", the_map[row][col]['exits'])

        command = input("> ")
        command_parts = command.split()

        main_command = command_parts[0].lower()

        if main_command == "go":
            row, col = go(row, col, command_parts[1].lower())
        elif main_command == "get":
            get(row, col, command_parts[1].lower(), inventory)
        elif main_command == "drop":
            sub_command = command_parts[1].lower()
            if sub_command in inventory:
                print("you dropped the", sub_command, "to the floor")
                inventory.remove(sub_command)
                the_map[row][col]['items'].append(sub_command)
            else:
                print("there is no", sub_command, "in your inventory")
        elif main_command == "inventory":
            for item in inventory:
                print(item)
        elif main_command == "quit":
            running = False
        else:
            print("I don't understand", command_parts[0])

    print("Thank you for playing this game. Now go do something else like cuddle with a kitty ;) ")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
