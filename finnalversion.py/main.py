from signupandlogin import login, sign_up
from menu import menuu
from rich.console import Console
from rich.panel import Panel

console = Console()

def main():
    while True:
        panel = Panel(
            "[bold white]*** Welcome to WallWizard Game ***[/bold white]",
            title="[bold cyan]🎮 WallWizard 🎮[/bold cyan]",
            subtitle="[italic bold magenta]Let the magic begin![/italic bold magenta]",
            border_style="cyan",
            padding=(1, 2)
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
                menuu(user)
        else:
            console.print(Panel("Invalid option! Please try again.", style="bold red"))

if __name__ == "__main__":
    main()
