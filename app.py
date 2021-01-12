import random
import math


class TicTacToe:

    player_positions = set()
    cpu_positions = set()


    # Start a game of TicTacToe until there is a winner or a tie
    def playTicTacToe(self):

        player_positions = set()
        cpu_positions = set()


        # Initialize the Game Board and print it in console
        board = [
            [" ", "|", " ", "|", " "],
            ["-", "+", "-", "+", "-"],
            [" ", "|", " ", "|", " "],
            ["-", "+", "-", "+", "-"],
            [" ", "|", " ", "|", " "]
        ]
        self.print_board(board)

        while(True):
            # Player's turn to play
            user_pos = int(input(
                "Where do you want to place 'X'? Enter position [1-9]: "))

            while not self.valid_pos(user_pos):
                user_pos = int(input(
                    "Where do you want to place 'X'? Enter position [1-9]: "))

            self.place_piece(board, user_pos, "player")
            if self.check_win():
                self.print_board(board)
                print()
                break

            # CPU's turn to play
            cpu_pos = random.randint(1, 9)
            while not self.valid_pos(cpu_pos):
                cpu_pos = random.randint(1, 9)
            self.place_piece(board, cpu_pos, "cpu")
            self.print_board(board)
            print()
            if self.check_win():
                break

    # Print the Game Board in console
    def print_board(self, board):
        for line in board:
            for char in line:
                print(char, end="")
            print()

    # Check if a position is free and between 1-9,
    # return False otherwise
    def valid_pos(self, pos):
        if math.isnan(pos):
            print("Please input a valid number.")
            return False
        elif pos in self.player_positions or pos in self.cpu_positions:
            print("Position taken.")
            return False
        elif pos < 1 or pos > 9:
            print("Please respect the position boundaries.")
            return False
        return True

    # Draw the played piece on the board
    def place_piece(self, board, pos, user):
        piece = " "
        if user == "player":
            piece = "X"
            self.player_positions.add(pos)
        elif user == "cpu":
            piece = "O"
            self.cpu_positions.add(pos)

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

    # Check whether the player or the computer won
    def check_win(self):

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
            if set(win).issubset(self.player_positions):
                print()
                print("Congratulations, you won!")
                return True
            elif set(win).issubset(self.cpu_positions):
                print()
                print("Better luck next time :(")
                return True

        if len(self.player_positions) + len(self.cpu_positions) == 9:
            print()
            print("It's a tie")
            return True

        return False


test = TicTacToe()
test.playTicTacToe()
while True:
    play_again = input("Do you want to play again? [Y/N]: ")
    if play_again == "N":
        print("Goodbye!")
        break
    else:
        test.playTicTacToe()
