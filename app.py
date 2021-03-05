########## Imports ##########
import random
import math
import time
import json
import datetime
import interface

########## Global Variables ##########
player_positions = set()
cpu_positions = set()
finished = False
scores = []

########## Functions ##########
## Start a game of TicTacToe until there is a winner or a tie
def init_game(user_name):
    username = ""
    opponent = ""
    difficulty = ""

    # Player username
    def ask_user_name():
        if user_name == "default":
            name = input(
                "\nWhat is your name?\n[3-10 characters only, alphabetic or numeric]: "
            )
            if not name.isalnum() or len(name) < 3 or len(name) > 10:
                print("Please respect the naming rules...")
                name = ask_user_name()
            username = name
        else:
            username = user_name
        return username

    # PvP or PvE
    def ask_user_opponent():
        opponent_choice = input(
            "\nPlease choose your opponent.\n1 - Local Player\n2 - Computer\nYour choice: "
        )
        if not (opponent_choice == "1" or opponent_choice == "2"):
            print("Please choose a valid opponent option...")
            opponent_choice = ask_user_opponent()
        if opponent_choice == "1":
            opponent = "local"
        else:
            opponent = "computer"
        return opponent

    # For PvE --> easy, medium, hard
    def ask_user_difficulty():
        difficulty_choice = input(
            "\nPlease select difficulty:\n1 - Easy\n2 - Medium\n3 - Hard\nYour choice: "
        )
        if not difficulty_choice in ["1", "2", "3"]:
            print("Please choose a valid diffuculty option...")
            difficulty_choice = ask_user_difficulty()
        if difficulty_choice == "1":
            difficulty = "easy"
        elif difficulty_choice == "2":
            difficulty = "medium"
        else:
            dificulty = "hard"
        return difficulty

    username = ask_user_name()
    opponent = ask_user_opponent()
    if opponent == "computer":
        difficulty = ask_user_difficulty()
    return username, opponent, difficulty


## Load the past game scores from the locally saved json files
def load_scores(username, opponent, difficulty):
    global scores
    try:
        with open(f"scores_{username}_{opponent}_{difficulty}.json") as f:
            scores = json.load(f)
    except FileNotFoundError:
        scores = []


# Save the game's score to a json file
def save_scores(username, opponent, difficulty):
    with open(f"scores_{username}_{opponent}_{difficulty}.json", "w") as f:
        json.dump(scores, f, indent=4)


## The computer makes a move, according to the selected difficulty
def play_cpu_turn(difficulty):

    # In easy mode, it randomly selects an empty square
    if difficulty == "easy":
        cpu_pos = random.randint(1, 9)
        while not is_valid_pos(cpu_pos):
            cpu_pos = random.randint(1, 9)
        return cpu_pos

    # In medium mode, it tries to block the user from filling three consequtive squares
    elif difficulty == "medium":
        count = 0  # number of consecutive X
        empty = 0  # position of an empty square

        # Check each row for incomplete tictactoes
        for row in range(1, 7 + 1, 3):
            for col in range(row, row + 3):
                if is_valid_pos(col):
                    empty = col
                elif col in player_positions:
                    count += 1
                else:
                    continue
            if count == 2 and empty != 0:
                return empty
            else:
                count = 0
                empty = 0

        # Check each column for incomplete tictactoes
        for col in range(1, 3 + 1):
            for row in range(col, col + 7, 3):
                if is_valid_pos(row):
                    empty = row
                elif row in player_positions:
                    count += 1
                else:
                    continue
            if count == 2 and empty != 0:
                return empty
            else:
                count = 0
                empty = 0

        # Check diagonal from up-left for an incomplete tictactoe
        for diag in range(1, 9 + 1, 4):
            if is_valid_pos(diag):
                empty = diag
            elif diag in player_positions:
                count += 1
            else:
                continue
        if count == 2 and empty != 0:
            return empty
        else:
            count = 0
            empty = 0

        # Check diagonal from up-right for an incomplete tictactoe
        for diag in range(3, 7 + 1, 2):
            if is_valid_pos(diag):
                empty = diag
            elif diag in player_positions:
                count += 1
            else:
                continue
        if count == 2 and empty != 0:
            return empty
        else:
            count = 0
            empty = 0

        # If no possible player tictactoes are found, select the center square
        if 5 not in player_positions and 5 not in cpu_positions:
            return 5
        else:
            # Corner squares have higher chances to form a tictactoe
            corner_squares = [1, 3, 7, 9]
            empty_squares = []
            for square in corner_squares:
                if square not in player_positions and square not in cpu_positions:
                    empty_squares.append(square)
            if empty_squares:
                return random.choice(empty_squares)

            # Last ones in priority are the middle squares
            middle_squares = [2, 4, 6, 8]
            empty_squares = []
            for square in middle_squares:
                if square not in player_positions and square not in cpu_positions:
                    empty_squares.append(square)
            if empty_squares:
                return random.choice(empty_squares)

    else:
        # TODO
        pass


## Start a game of TicTacToe until there is a winner or a tie
def playTicTacToe(user_name="default"):
    global player_positions
    global cpu_positions
    global finished

    username, opponent, difficulty = init_game(user_name)

    load_scores(username, opponent, difficulty)

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
    graphic_board = interface.draw_board()

    while True:
        if finished:
            break

        # Player's turn to play
        print("\nIt's your turn!")
        user_pos = ask_user_move()
        while not is_valid_pos(user_pos):
            user_pos = ask_user_move()

        place_piece(board, user_pos, "player")
        interface.draw_piece(graphic_board, user_pos, "player")
        print_board(board)
        if check_win():
            save_scores(username, opponent, difficulty)
            if replay():
                graphic_board.close()
                player_positions = set()
                cpu_positions = set()
                playTicTacToe(username)
            else:
                finished = True
                graphic_board.close()
                print("Goodbye!")
        if finished:
            break

        # CPU's turn to play
        print("CPU is playing...")
        time.sleep(1)

        cpu_pos = play_cpu_turn(difficulty)
        place_piece(board, cpu_pos, "cpu")
        interface.draw_piece(graphic_board, cpu_pos, "cpu")
        print_board(board)
        if check_win():
            save_scores(username, opponent, difficulty)
            if replay():
                graphic_board.close()
                player_positions = set()
                cpu_positions = set()
                playTicTacToe(username)
            else:
                finished = True
                graphic_board.close()
                print("Goodbye!")
        if finished:
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
def is_valid_pos(pos):
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
            scores.append(
                {
                    "timestamp": str(datetime.datetime.now()),
                    "Player_1": 1,
                    "Computer": 0,
                }
            )
            return True
        elif set(win).issubset(cpu_positions):
            print()
            print("Better luck next time :(")
            scores.append(
                {
                    "timestamp": str(datetime.datetime.now()),
                    "Player_1": 0,
                    "Computer": 1,
                }
            )
            return True

    if len(player_positions) + len(cpu_positions) == 9:
        print()
        print("It's a tie")
        scores.append(
            {"timestamp": str(datetime.datetime.now()), "Player_1": 0, "Computer": 0}
        )
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
        return replay()


if __name__ == "__main__":
    playTicTacToe()
