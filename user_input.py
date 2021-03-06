# Player username
def ask_user_name(username):
    if username == "1" or username == "2":
        name = input(
            f"\n[PLAYER {username}] What is your name?\n(3-10 characters only, alphabetic or numeric): "
        )
        if not name.isalnum() or len(name) < 3 or len(name) > 10:
            print("Please respect the naming rules...")
            name = ask_user_name()
        username = name
    else:
        username = username
    return username


## Start a game of TicTacToe until there is a winner or a tie
def init_game():
    opponent = ""
    difficulty = ""

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

    opponent = ask_user_opponent()
    if opponent == "computer":
        difficulty = ask_user_difficulty()
    return opponent, difficulty


## Ask the user to play and check if his answer is numeric
def ask_user_move(piece):
    answer = input(f"Where do you want to place {piece}? Enter position [1-9]: ")
    if not answer.isnumeric():
        print("\nPlease enter a numeric value.")
        answer = ask_user_move()
    return int(answer)


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