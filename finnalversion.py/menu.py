from display_functions import display_menu, display_game_history, display_leaderboard
from game_functions import start_new_game
from rich.console import Console
from rich.panel import Panel

console = Console()

def menuu(user):
    while True:
        display_menu()
        console.print("\nSelect an option:", style="bold underline white")
        choice = input()

        if choice == '1':
            start_new_game(user,menuu)
        # elif choice == '2':
            # continue_game(user)
        elif choice == '3':
            display_game_history(user)
        elif choice == '4':
            display_leaderboard()
        elif choice == '5':
            console.print(Panel("Logging out...", style="bold magenta"))
            break
        else:
            console.print(Panel("Invalid option! Please choose an option from 1 to 5", style="bold red"))
