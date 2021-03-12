########## Imports ##########
import config
import storage
import datetime
import math

## Check if a position is free and between 1-9,
## return False otherwise
def is_valid_pos(pos):
    if math.isnan(pos):
        print("\nPlease input a valid number.")
        return False
    elif pos in config.player1_positions or pos in config.player2_positions:
        print("Position taken.")
        return False
    elif pos < 1 or pos > 9:
        print("\nPlease respect the position boundaries.")
        return False
    return True


## Check whether the player or the computer won
def check_win(username, opponent_name):

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
        if set(win).issubset(config.player1_positions):
            print()
            print(f"{username} wins!")
            storage.scores.append(
                {
                    "timestamp": str(datetime.datetime.now()),
                    username: 1,
                    opponent_name: 0,
                }
            )
            return True
        elif set(win).issubset(config.player2_positions):
            print()
            print(f"{opponent_name} wins!")
            storage.scores.append(
                {
                    "timestamp": str(datetime.datetime.now()),
                    username: 0,
                    opponent_name: 1,
                }
            )
            return True

    if len(config.player1_positions) + len(config.player2_positions) == 9:
        print()
        print("It's a tie")
        storage.scores.append(
            {"timestamp": str(datetime.datetime.now()), username: 0, opponent_name: 0}
        )
        return True

    return False