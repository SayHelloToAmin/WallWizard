from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.box import ROUNDED
from list_games import list_games
from save_game import give_me_dict , give_me_game_dict
from rich.text import Text


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
    games = give_me_game_dict()
    game_records = games[-5:]

    for game in game_records:

        table = Table(show_header=True, header_style="bold cyan")
        table.add_column("Field", style="dim")
        table.add_column("Value", style="bold")

        table.add_row("Game ID", game["game_id"])
        table.add_row("Player 1", game["player1_username"])
        table.add_row("Player 2", game["player2_username"])
        table.add_row("P1 Walls", str(game["p1walls"]))
        table.add_row("P2 Walls", str(game["p2walls"]))
        table.add_row("P1 Position", str(game["player1_position"]))
        table.add_row("P2 Position", str(game["player2_position"]))
        table.add_row("Current Turn", game["current_turn"])
        table.add_row("Timer", str(game["timer"]))
        table.add_row("Game Result", game["game_result"])
        table.add_row("Date", game["date"])

        panel_title = Text(f"Game History: {game['game_id']}", style="bold green")
        panel = Panel(table, title=panel_title, border_style="bright_yellow")

        console.print(panel)
    console.print("Press Enter To Back!...", style="green")
    input()
    return

def display_leaderboard():
    data = give_me_dict()
    sorted_data = sorted(data, key=lambda x: x['wins'], reverse=True)
    table = Table(title="Players Sorted by Wins")
    table.add_column("Username", justify="center")
    table.add_column("Email", justify="center")
    table.add_column("Games Played", justify="center")
    table.add_column("Wins", justify="center")
    for player in sorted_data:
        table.add_row(player['username'], player['email'], str(player['games']), str(player['wins']))
    console.print(table)
    console.print("Press Enter To Back!...", style="green")
    input()
    return