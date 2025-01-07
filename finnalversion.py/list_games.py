import json

games_file = 'games_data.json'

def list_games(username):
    try:
        with open(games_file, 'r') as file:
            games = json.load(file)
            user_games = [game for game in games if username in [game['player1_username'], game['player2_username']]]
            return user_games
    except FileNotFoundError:
        return []
