from rich.console import Console
Console = Console()
from rich.panel import Panel
from save_game import add_games , add_wins

def finall_task(winner , loser):
    Console.print(Panel(f"{winner} in bazio board ! ", style="bold green"))
    add_games(winner)
    add_games(loser)
    add_wins(winner)
    quit()