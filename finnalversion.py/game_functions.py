import uuid
import time
from rich.console import Console
from rich.panel import Panel
from save_game import save_game

console = Console()

def start_new_game(user):
    console.print(Panel("Starting a new game...", style="bold magenta"))

    player1_position = (0, 0)
    player2_position = (5, 5)
    wall_position = (3, 3)
    current_turn = user['username']
    game_start_time = time.time()

    game_id = str(uuid.uuid4())
    game_data = {
        'game_id': game_id,
        'player1_username': user['username'],
        'player2_username': input("Enter second player's username: "),
        'player1_position': player1_position,
        'player2_position': player2_position,
        'wall_position': wall_position,
        'current_turn': current_turn,
        'time_spent': 0,
        'game_result': 'In Progress'
    }

    save_game(game_data)
    console.print(Panel(f"Game {game_id} started!", style="green"))

    input("Press Enter to save and exit the game...")
    game_data['time_spent'] = round(time.time() - game_start_time, 2)
    game_data['game_result'] = 'Player 1 Wins'
    save_game(game_data)
    console.print(Panel(f"Game {game_id} saved and exited!", style="green"))

def continue_game(user):
    console.print(Panel("Continuing a previous game...", style="bold magenta"))
