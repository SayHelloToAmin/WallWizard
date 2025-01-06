import json
from signupandlogin import login , sign_up
# import re
import uuid
# import bcrypt
import time
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.box import ROUNDED

user_file = 'users.json'
games_file = 'games_data.json'

console = Console()

def save_game(game_data):
    try:
        with open(games_file, 'r') as file:
            games = json.load(file)
    except FileNotFoundError:
        games = []

    games.append(game_data)

    with open(games_file, 'w') as file:
        json.dump(games, file, indent=4)


def list_games(username):
    try:
        with open(games_file, 'r') as file:
            games = json.load(file)
            user_games = [game for game in games if username in [game['player1_username'], game['player2_username']]]
            return user_games
    except FileNotFoundError:
        return []


def display_menu():
    table = Table(
        title="[bold cyan]🎮 Main Menu 🎮[/bold cyan]",
        title_style="bold black on white",
        show_lines=True,
        header_style="bold magenta",
        box=ROUNDED
    )

    table.add_column("[bold magenta]Option[/bold magenta]", justify="center")
    table.add_column("[bold magenta]Title[/bold magenta]", style="bold white")

    table.add_row(
        "[bold cyan]:one:",
        "[bold white]Start New Game[/bold white]",
    )
    table.add_row(
        "[bold cyan]:two:",
        "[bold white]Continue Previous Game[/bold white]",
    )
    table.add_row(
        "[bold cyan]:three:",
        "[bold white]View Game History[/bold white]",
    )
    table.add_row(
        "[bold cyan]:four:",
        "[bold white]View Leaderboard[/bold white]",
    )
    table.add_row(
        "[bold cyan]:five:",
        "[bold white]Logout[/bold white]",
    )

    console.print(table)



def display_game_history(user):
    user_games = list_games(user['username'])
    if not user_games:
        console.print(Panel("No history found!", style="bold red"))
        return

    table = Table(title="Game History", show_lines=True)
    table.add_column("Game ID", style="cyan")
    table.add_column("Players", style="magenta")
    table.add_column("Status", style="green")

    for game in user_games:
        table.add_row(game['game_id'], f"{game['player1_username']} vs {game['player2_username']}", game['game_result'])

    console.print(table)

def display_leaderboard():
    try:
        with open(games_file, 'r') as file:
            games = json.load(file)
    except FileNotFoundError:
        console.print(Panel("No results found!", style="bold red"))
        return

    leaderboard = {}
    
    for game in games:
        for player in [game['player1_username'], game['player2_username']]:
            if player not in leaderboard:
                leaderboard[player] = {
                    'wins': 0,
                    'losses': 0,
                    'total_time': 0
                }
            
            if game['game_result'] == 'Player 1 Wins' and game['player1_username'] == player:
                leaderboard[player]['wins'] += 1
            elif game['game_result'] == 'Player 1 Wins' and game['player2_username'] == player:
                leaderboard[player]['losses'] += 1
            elif game['game_result'] == 'Player 2 Wins' and game['player2_username'] == player:
                leaderboard[player]['wins'] += 1
            elif game['game_result'] == 'Player 2 Wins' and game['player1_username'] == player:
                leaderboard[player]['losses'] += 1

            leaderboard[player]['total_time'] += game.get('time_spent', 0)

    leaderboard_data = []
    for player, stats in leaderboard.items():
        leaderboard_data.append({
            'username': player,
            'wins': stats['wins'],
            'losses': stats['losses'],
            'total_time': stats['total_time']
        })

    with open('leaderboard.json', 'w') as file:
        json.dump(leaderboard_data, file, indent=4)

    sorted_leaderboard = sorted(leaderboard_data, key=lambda x: (x['wins'], -x['total_time']), reverse=True)

    table = Table(title="Leaderboard")
    table.add_column("Rank", style="cyan")
    table.add_column("Player", style="magenta")
    table.add_column("Wins", style="green")
    table.add_column("Losses", style="red")
    table.add_column("Total Time (s)", style="yellow")

    for idx, player in enumerate(sorted_leaderboard[:3]):
        table.add_row(str(idx + 1), player['username'], str(player['wins']), str(player['losses']), str(player['total_time']))

    console.print(table)

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

def menu(user):
    while True:
        print("\n")
        display_menu()
        console.print("\nSelect an option:", style="bold underline white")
        choice = input()

        if choice == '1':
            start_new_game(user)
        elif choice == '2':
            continue_game(user)
        elif choice == '3':
            display_game_history(user)
        elif choice == '4':
            display_leaderboard()
        elif choice == '5':
            console.print(Panel("Logging out...", style="bold magenta"))
            break
        else:
            console.print(Panel("Invalid option! Please choose an option from 1 to 5", style="bold red"))

def main():
    while True:
        panel = Panel(
    "[bold white]*** Welcome to WallWizard Game ***[/bold white]",
    title="[bold cyan]🎮 WallWizard 🎮[/bold cyan]",
    subtitle="[italic bold magenta]Let the magic begin![/italic bold magenta]",
    border_style="cyan",
    padding=(1, 2),
)

        console.print(panel, "\n")
        console.print(Panel("1) Sign up", border_style="cyan", style="italic bold white"))
        console.print(Panel("2) Log in", border_style="cyan", style="italic bold white"))
        console.print("\nChoose an option (1 or 2):", style="bold underline white")
        choice = input()

        if choice == '1':
            sign_up()
        elif choice == '2':
            user = login()
            if user:
                menu(user)
        else:
            console.print(Panel("Invalid option! Please try again.", style="bold red"))


if __name__ == "__main__":
    main()