from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.box import ROUNDED
import json
from list_games import list_games

console = Console()
games_file = 'games_data.json'

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
