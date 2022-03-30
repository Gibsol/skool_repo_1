game = [
    ".", ".", ".",
    ".", ".", ".",
    ".", ".", "."
]

def position_print():
    print(game[0] + game[1] + game[2])
    print(game[3] + game[4] + game[5])
    print(game[6] + game[7] + game[8])

def tictac_input():
    next_position = int(input("Please type what position: "))

    if next_position == 1:
        game[0] = "X"

    if next_position == 2:
        game[1] = "X" 

    if next_position == 3:
        game[2] = "X" 

    if next_position == 4:
        game[3] = "X" 

    if next_position == 5:
        game[4] = "X" 

    if next_position == 6:
        game[5] = "X" 

    if next_position == 7:
        game[6] = "X" 

    if next_position == 8:
        game[7] = "X" 

    if next_position == 9:
        game[8] = "X" 

tictac_input()
position_print()

tictac_input()
position_print()

tictac_input()
position_print()