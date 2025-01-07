import json

games_file = 'games_data.json'

def save_game(game_data):
    try:
        with open(games_file, 'r') as file:
            games = json.load(file)
    except FileNotFoundError:
        games = []

    games.append(game_data)

    with open(games_file, 'w') as file:
        json.dump(games, file, indent=4)
