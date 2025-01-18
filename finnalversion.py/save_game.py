import json
games_file = 'finnalversion.py/games_data.json'
users_file = 'finnalversion.py/Users.json'




def create_game(game_data):
    try:
        with open(games_file, 'r') as file:
            games = json.load(file)
    except FileNotFoundError:
        games = []

    games.append(game_data)

    with open(games_file, 'w') as file:
        json.dump(games, file, indent=4)


def take_table(game_id):
    try:
        with open(games_file, 'r') as file:
            games = json.load(file)
    except FileNotFoundError:
        games = []
    for dict in games:
        if dict["game_id"] == game_id:
            return dict["table"]

def p1walls(game_id):
    try:
        with open(games_file, 'r') as file:
            games = json.load(file)
    except FileNotFoundError:
        games = []
    for dict in games:
        if dict["game_id"] == game_id:
            return dict["p1walls"]

def p2walls(game_id):
    try:
        with open(games_file, 'r') as file:
            games = json.load(file)
    except FileNotFoundError:
        games = []
    for dict in games:
        if dict["game_id"] == game_id:
            return dict["p2walls"]


def gettime(game_id):
    try:
        with open(games_file, 'r') as file:
            games = json.load(file)
    except FileNotFoundError:
        games = []
    for dict in games:
        if dict["game_id"] == game_id:
            return dict["timer"]



def loc1(game_id):
    try:
        with open(games_file, 'r') as file:
            games = json.load(file)
    except FileNotFoundError:
        games = []
    for dict in games:
        if dict["game_id"] == game_id:
            return dict["player1_position"]

def loc2(game_id):
    try:
        with open(games_file, 'r') as file:
            games = json.load(file)
    except FileNotFoundError:
        games = []
    for dict in games:
        if dict["game_id"] == game_id:
            return dict["player2_position"]



def savethegame(game_id , gamedata):
    try:
        with open(games_file, 'r') as file:
            games = json.load(file)
    except FileNotFoundError:
        games = []
    for game in games:
        if game["game_id"] == game_id:
            game.update(gamedata) 
            break
    with open(games_file, "w") as f:
        json.dump(games, f, indent=4)

def add_games(username):
    try:
        with open(users_file, 'r') as file:
            users = json.load(file)
    except FileNotFoundError:
        users = []
    for user in users:
        if user["username"] == username:
            user["games"] += 1
            break
    with open(users_file, "w") as file:
        json.dump(users, file, indent=4)

def add_wins(username):
    try:
        with open(users_file, 'r') as file:
            users = json.load(file)
    except FileNotFoundError:
        users = []
    for user in users:
        if user["username"] == username:
            user["wins"] += 1
            break
    with open(users_file, "w") as file:
        json.dump(users, file, indent=4)




def give_me_dict():
    try:
        with open(users_file, 'r') as file:
            users = json.load(file)
    except FileNotFoundError:
        users = []
    return users

def give_me_game_dict():
    try:
        with open(games_file, 'r') as file:
            games = json.load(file)
    except FileNotFoundError:
        games = []
    return games
# def swap_turn():
#     try:
#         with open(games_file, 'r') as file:
#             games = json.load(file)
#     except FileNotFoundError:
#         games = []
#     for num in range(len(games)):
#         if games[num]["game_id"] == game_id:
#             if games[num]["current_turn"] == games[num]["player1_username"]:
#                 games[num]["current_turn"] = games[num]["player2_username"]
#             else:
#                 games[num]["current_turn"] = games[num]["player1_username"]
#     with open(games_file, 'w') as file:
#         json.dump(games, file, indent=4)


