import random
import math
import time

player_positions = set()
cpu_positions = set()

## Start a game of TicTacToe until there is a winner or a tie
def playTicTacToe():
    global player_positions
    global cpu_positions

    # Initialize the Game Board and print it in console
    board = [
        [" ", "|", " ", "|", " "],
        ["-", "+", "-", "+", "-"],
        [" ", "|", " ", "|", " "],
        ["-", "+", "-", "+", "-"],
        [" ", "|", " ", "|", " "],
    ]
    print()
    print_board(board)

    while True:
        # Player's turn to play
        print("\nIt's your turn!")
        user_pos = ask_user_move()
        while not valid_pos(user_pos):
            user_pos = ask_user_move()

        place_piece(board, user_pos, "player")
        print_board(board)
        if check_win():
            if replay():
                player_positions = set()
                cpu_positions = set()
                playTicTacToe()
            else:
                print("Goodbye!")
                break

        # CPU's turn to play
        print("CPU is playing...")
        time.sleep(1)
        cpu_pos = random.randint(1, 9)
        while not valid_pos(cpu_pos):
            cpu_pos = random.randint(1, 9)
        place_piece(board, cpu_pos, "cpu")
        print_board(board)

        if check_win():
            if replay():
                player_positions = set()
                cpu_positions = set()
                playTicTacToe()
            else:
                print("Goodbye!")
                break


## Print the Game Board in console
def print_board(board):
    for line in board:
        for char in line:
            print(char, end="")
        print()


## Ask the user to play and check if his answer is numeric
def ask_user_move():
    answer = input("Where do you want to place 'X'? Enter position [1-9]: ")
    if not answer.isnumeric():
        print("\nPlease enter a numeric value.")
        answer = ask_user_move()
    return int(answer)


## Check if a position is free and between 1-9,
## return False otherwise
def valid_pos(pos):
    if math.isnan(pos):
        print("\nPlease input a valid number.")
        return False
    elif pos in player_positions or pos in cpu_positions:
        print("Position taken.")
        return False
    elif pos < 1 or pos > 9:
        print("\nPlease respect the position boundaries.")
        return False
    return True


## Draw the played piece on the board
def place_piece(board, pos, user):
    piece = " "
    if user == "player":
        piece = "X"
        player_positions.add(pos)
    elif user == "cpu":
        piece = "O"
        cpu_positions.add(pos)

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


## Check whether the player or the computer won
def check_win():

    # Possible ways to win
    row1 = [1, 2, 3]
    row2 = [4, 5, 6]
    row3 = [7, 8, 9]
    col1 = [1, 4, 7]
    col2 = [2, 5, 8]
    col3 = [3, 6, 9]
    diag1 = [1, 5, 9]
    diag2 = [3, 5, 7]

    wins = [row1, row2, row3, col1, col2, col3, diag1, diag2]

    for win in wins:
        if set(win).issubset(player_positions):
            print()
            print("Congratulations, you won!")
            return True
        elif set(win).issubset(cpu_positions):
            print()
            print("Better luck next time :(")
            return True

    if len(player_positions) + len(cpu_positions) == 9:
        print()
        print("It's a tie")
        return True

    return False


## Ask user to play again or not
def replay():
    play_again = input("Do you want to play again? [Y/N]: ")
    if play_again == "Y" or play_again == "y":
        return True
    elif play_again == "N" or play_again == "n":
        return False
    else:
        print("Please answer [Y/y] to play again or [N/n] to exit...")
        replay()


if __name__ == "__main__":
    playTicTacToe()
