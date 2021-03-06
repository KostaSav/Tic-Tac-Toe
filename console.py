########## Imports ##########
import config

# Initialize the Game Board and print it in console
board = [
    [" ", "|", " ", "|", " "],
    ["-", "+", "-", "+", "-"],
    [" ", "|", " ", "|", " "],
    ["-", "+", "-", "+", "-"],
    [" ", "|", " ", "|", " "],
]

## Print the Game Board in console
def print_board():
    for line in board:
        for char in line:
            print(char, end="")
        print()


## Draw the played piece on the board
def place_piece(pos, user):
    piece = " "
    if user == "player_1":
        piece = "X"
        config.player1_positions.add(pos)
    elif user == "player_2":
        piece = "O"
        config.player2_positions.add(pos)
    elif user == "cpu":
        piece = "O"
        config.cpu_positions.add(pos)

    if pos == 1:
        board[0][0] = piece
    elif pos == 2:
        board[0][2] = piece
    elif pos == 3:
        board[0][4] = piece
    elif pos == 4:
        board[2][0] = piece
    elif pos == 5:
        board[2][2] = piece
    elif pos == 6:
        board[2][4] = piece
    elif pos == 7:
        board[4][0] = piece
    elif pos == 8:
        board[4][2] = piece
    elif pos == 9:
        board[4][4] = piece