########## Imports ##########
import random
import time
import config
import user_input
import gui
import console
import storage
import logic

########## Global Variables ##########
finished = False


########## Functions ##########
## The computer makes a move, according to the selected difficulty
def play_cpu_turn(difficulty):

    # In easy mode, it randomly selects an empty square
    if difficulty == "easy":
        cpu_pos = random.randint(1, 9)
        while not logic.is_valid_pos(cpu_pos):
            cpu_pos = random.randint(1, 9)
        return cpu_pos

    # In medium mode, it tries to block the user from filling three consequtive squares
    elif difficulty == "medium":
        count = 0  # number of consecutive X
        empty = 0  # position of an empty square

        # Check each row for incomplete tictactoes
        for row in range(1, 7 + 1, 3):
            for col in range(row, row + 3):
                if logic.is_valid_pos(col):
                    empty = col
                elif col in config.player1_positions:
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
                if logic.is_valid_pos(row):
                    empty = row
                elif row in config.player1_positions:
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
            if logic.is_valid_pos(diag):
                empty = diag
            elif diag in config.player1_positions:
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
            if logic.is_valid_pos(diag):
                empty = diag
            elif diag in config.player1_positions:
                count += 1
            else:
                continue
        if count == 2 and empty != 0:
            return empty
        else:
            count = 0
            empty = 0

        # If no possible player tictactoes are found, select the center square
        if logic.is_valid_pos(5):
            return 5
        else:
            # Corner squares have higher chances to form a tictactoe
            corner_squares = [1, 3, 7, 9]
            empty_squares = []
            for square in corner_squares:
                if logic.is_valid_pos(square):
                    empty_squares.append(square)
            if empty_squares:
                return random.choice(empty_squares)

            # Last ones in priority are the middle squares
            middle_squares = [2, 4, 6, 8]
            empty_squares = []
            for square in middle_squares:
                if logic.is_valid_pos(square):
                    empty_squares.append(square)
            if empty_squares:
                return random.choice(empty_squares)

    else:
        # TODO
        pass


## Start a game of TicTacToe until there is a winner or a tie
def playTicTacToe(first_player="1", second_player="2"):
    global finished

    username = user_input.ask_user_name(first_player)
    opponent, difficulty = user_input.init_game()
    if opponent == "local":
        opponent_name = user_input.ask_user_name(second_player)
    else:
        opponent_name = "Computer"

    storage.load_scores(username, opponent, difficulty)

    print()
    console.print_board()
    graphic_board = gui.draw_board()

    while True:
        if finished:
            break

        # Player 1's turn to play
        if opponent == "computer":
            print("\nIt's your turn!")
        else:
            print(f"\nIt's {username}'s turn!")
        user_pos = user_input.ask_user_move("X")
        while not logic.is_valid_pos(user_pos):
            user_pos = user_input.ask_user_move("X")

        console.place_piece(user_pos, "player_1")
        gui.draw_piece(graphic_board, user_pos, "player_1")
        console.print_board()
        if logic.check_win(opponent_name):
            if opponent == "computer":
                print("Congratulations, you won!")
            else:
                print(f"{username} wins!")
            storage.save_scores(username, opponent, difficulty)
            if user_input.replay():
                graphic_board.close()
                console.reset_board()
                config.player1_positions = set()
                config.player2_positions = set()
                config.cpu_positions = set()
                playTicTacToe(username, opponent_name)
            else:
                finished = True
                graphic_board.close()
                print("Goodbye!")
        if finished:
            break

        # Player 2's/CPU's turn to play
        if opponent == "computer":
            print("CPU is playing...")
            time.sleep(1)
            cpu_pos = play_cpu_turn(difficulty)
            console.place_piece(cpu_pos, "cpu")
            gui.draw_piece(graphic_board, cpu_pos, "cpu")
            console.print_board()
        else:
            print(f"\nIt's {opponent_name}'s turn!")
            user_pos = user_input.ask_user_move("O")
            while not logic.is_valid_pos(user_pos):
                user_pos = user_input.ask_user_move("O")
            console.place_piece(user_pos, "player_2")
            gui.draw_piece(graphic_board, user_pos, "player_2")
            console.print_board()

        if logic.check_win(opponent_name):
            if opponent == "computer":
                print("Better luck next time...")
            else:
                print(f"{opponent_name} wins!")
            storage.save_scores(username, opponent, difficulty)
            if user_input.replay():
                graphic_board.close()
                console.reset_board()
                config.player1_positions = set()
                config.player2_positions = set()
                config.cpu_positions = set()
                playTicTacToe(username, opponent_name)
            else:
                finished = True
                graphic_board.close()
                print("Goodbye!")
        if finished:
            break


if __name__ == "__main__":
    playTicTacToe()
