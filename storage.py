########## Imports ##########
import json
from pathlib import Path

scores = []

## Load the past game scores from the locally saved json files
def load_scores(username, opponent, difficulty):
    global scores
    try:
        with open(f"json/scores_{username}_{opponent}_{difficulty}.json") as f:
            scores = json.load(f)
    except FileNotFoundError:
        scores = []


# Save the game's score to a json file
def save_scores(username, opponent, difficulty):
    try:
        with open(f"json/scores_{username}_{opponent}_{difficulty}.json", "w") as f:
            json.dump(scores, f, indent=4)
    except FileNotFoundError:
        base = Path("json")
        jsonpath = base / (f"scores_{username}_{opponent}_{difficulty}.json")
        base.mkdir(exist_ok=True)
        jsonpath.write_text(json.dump(scores, indent=4))
