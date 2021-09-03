def main():
    # Numerical datatype
    # whole number - int - integer
    value = 13
    number = 7
    # float = decimal number
    float_value = 4.20
    # str - strings
    name = "Emma"
    other_name = "Mary"
    # complex number

    # logical datatype
    # Boolean - bool
    done = False
    run = True

    # sequence types
    # list
    # list mutable - can be changed
    values = [1, 2, 3, 4, 5, 6, 77]
    values.pop(6)
    values.sort()

    names = ['sara', 'mia', 'maria']
    things = [1, 'mia', 3, 'Samir']
    print(things[1])
    list_of_lists = [
        [
            [1, 2, 3],
            [4, 5, 6]
        ],
        [
            [7, 8, 9],
            [10, 11, 12]
        ]
    ]
    print(list_of_lists[1])
    print(list_of_lists[0][1][2])

    # Tuple constant content
    # Tuple immutable = can't be changed
    numbers = (1, 2, 3)
    print(numbers[2])

    # Set
    # mutable and was unordered until version 3.6 and can still be unordered don't expect order
    # can only store unique values
    set_values = {1, 2, 3, 4, 1, 2, 3}
    more_values = {2, 3, 7, 9}
    list_values = [13, 22, 42, 43, 42, 39]
    unique_values = list(set(list_values))
    print(set_values.intersection(more_values))
    print(list_values)
    print(unique_values)
    # ascii and unicode

    # mapping type
    # dictionary - dict
    # keys in dictionary are unique
    # one can make a list of multiple dictionaries
    person = {"Name": "Emma Jarlvi Skog", "Age": 31, "Email": "emma@emcy.se"}
    print(person["Email"])
    print(person["Age"])


if __name__ == '__main__':
    main()
