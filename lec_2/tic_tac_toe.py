import sys

play_table: [[chr]] = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-'],
]


def show_table(table: [[chr]]) -> None:
    for row in table:
        for char in row:
            print(f"| {char} |", end="")
        print()


def process_player_one() -> None:
    player_one_input: str = input(f"Player 1: Podaj współrzędne X i Y: ")
    player_one_coordinates: [int] = [int(num) for num in player_one_input.strip().split(" ")]
    if player_one_coordinates[0] > 2 or player_one_coordinates[0] < 0:
        print("incorrect input")
        return
    if player_one_coordinates[1] > 2 or player_one_coordinates[1] < 0:
        print("incorrect input")
        return
    print(player_one_coordinates, "\n")
    play_table[player_one_coordinates[0]][player_one_coordinates[1]] = '0'
    show_table(play_table)


def process_player_two() -> None:
    player_two_input: str = input(f"Player 2: Podaj współrzędne X i Y: ")
    player_two_coordinates: [int] = [int(num) for num in player_two_input.strip().split(" ")]
    if player_two_coordinates[0] > 2 or player_two_coordinates[0] < 0:
        print("incorrect input")
        return
    if player_two_coordinates[1] > 2 or player_two_coordinates[1] < 0:
        print("incorrect input")
        return
    print(player_two_coordinates, "\n")
    play_table[player_two_coordinates[0]][player_two_coordinates[1]] = 'X'
    show_table(play_table)


def check_winner() -> None:
    # TODO!

    # sprawdzanie w wierszach
    for i in range(0, 3):
        row = []
        for j in range(0, 3):
            row.append(play_table[i][j])
        if all(char == '0' for char in row):
            print("Player one is winner")
            sys.exit(0)
        if all(char == 'X' for char in row):
            print("Player two is winner")
            sys.exit(0)

    # sprawdzanie w kolumnach
    for i in range(0, 3):
        column = [play_table[i][0], play_table[i][1], play_table[i][2]]
        if all(char == '0' for char in column):
            print("Player one is winner")
            sys.exit(0)
        if all(char == 'X' for char in column):
            print("Player one is winner")
            sys.exit(0)


if __name__ == '__main__':
    while True:
        process_player_one()
        process_player_two()

        check_winner()
