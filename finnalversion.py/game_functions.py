import uuid
import time
from rich.console import Console
from rich.panel import Panel
from save_game import create_game
from signupandlogin import check_user , check_password
from game import start_the_game
import asyncio
console = Console()
game_id = str(uuid.uuid4())
def start_new_game(user,menu):
    console.print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------" , style="bold yellow")
    console.print(Panel("*Log in to your opponent's account...*", style="bold italic yellow"))
    while True:
        console.print("Please Enter The Username (Enter 'b' to go back to the main): ", style="bold white")
        username = input()
        if username.lower() == "b":
            menu(user)
        user2 = check_user(username)
        if not user2:
            console.print(Panel("Username not found! Please try again.", style="bold red"))
            continue
        else:
            break
    while True:
        console.print("Password (Enter 'b' to go back to the main): ", style="bold white")
        password = input()
        if password.lower() == "b":
            menu(user)
        if check_password(user2['password'], password):
            console.print(Panel("Login successful!", style="bold green"))
            break
        else:
            console.print(Panel("Password is incorrect! Please try again.", style="bold red"))

    console.print(Panel("Starting a new game...", style="bold magenta"))
    
    table = [[[0] for row in range(17)] for col in range(17)]
    table[0][8] = [2]
    table[16][8] = [1]
    create_game({
            "game_id": game_id,
            "player1_username": user["username"],
            "player2_username": user2["username"],
            "p1walls" : 10,
            "p2walls" : 10,
            "player1_position": [
                17,
                9
            ],
            "player2_position": [
                1,
                9
            ],
            "table" : table,
            "current_turn": "amin",
            "timer" : time.time(),
            "game_result": "In Progress"
        })

    asyncio.run(start_the_game(user["username"],user2["username"],game_id))




#     player1_position = (0, 0)
#     player2_position = (5, 5)
#     wall_position = (3, 3)
#     current_turn = user['username']
#     game_start_time = time.time()

#     game_id = str(uuid.uuid4())
#     game_data = {
#         'game_id': game_id,
#         'player1_username': user['username'],
#         'player2_username': input("Enter second player's username: "),
#         'player1_position': player1_position,
#         'player2_position': player2_position,
#         'wall_position': wall_position,
#         'current_turn': current_turn,
#         'time_spent': 0,
#         'game_result': 'In Progress'
#     }

    # save_game(game_data)
#     console.print(Panel(f"Game {game_id} started!", style="green"))

#     input("Press Enter to save and exit the game...")
#     game_data['time_spent'] = round(time.time() - game_start_time, 2)
#     game_data['game_result'] = 'Player 1 Wins'
#     save_game(game_data)
#     console.print(Panel(f"Game {game_id} saved and exited!", style="green"))

# def continue_game(user):
#     console.print(Panel("Continuing a previous game...", style="bold magenta"))
