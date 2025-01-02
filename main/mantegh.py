import os
from rich.console import Console
from collections import deque

console = Console()

# Game board dimensions
BOARD_SIZE = 9

# Initialize game board
def initialize_board():
    board = [[" " for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    return board

# Display the board
def display_board(board, walls):
    console.print("\n  " + "   ".join(map(str, range(BOARD_SIZE))), style="bold cyan")
    for i, row in enumerate(board):
        # نمایش ردیف مهره‌ها
        row_str = " | ".join(row)
        console.print(f"{i} {row_str}")
        
        # نمایش دیوارهای افقی
        if i < BOARD_SIZE - 1:
            horizontal_walls = ""
            for j in range(BOARD_SIZE):
                if (i, j, 'h') in walls:
                    horizontal_walls += "---"  # دیوار افقی
                else:
                    horizontal_walls += "   "  # فضای خالی
                if j < BOARD_SIZE - 1:
                    horizontal_walls += " "  # فضای بین خانه‌ها
            console.print(horizontal_walls)

        # نمایش دیوارهای عمودی
        if i < BOARD_SIZE - 1:
            vertical_walls = ""
            for j in range(BOARD_SIZE):
                if (i, j, 'v') in walls:
                    vertical_walls += "|   "  # دیوار عمودی
                else:
                    vertical_walls += "    "  # فضای خالی
            console.print(vertical_walls)

# Check if a move is valid
def is_valid_move(board, player_pos, new_pos, walls):
    x, y = player_pos
    nx, ny = new_pos
    if not (0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE):
        return False
    if abs(x - nx) + abs(y - ny) > 1:
        return False
    # Check for walls
    if x == nx:  # Horizontal move
        if (x, min(y, ny), 'h') in walls:
            return False
    elif y == ny:  # Vertical move
        if (min(x, nx), y, 'v') in walls:
            return False
    return True

# Check if a wall placement is valid
def is_valid_wall(walls, wall_pos):
    x, y, orientation = wall_pos
    if orientation not in ('h', 'v'):
        return False
    if orientation == 'h' and (x >= BOARD_SIZE - 1 or y >= BOARD_SIZE - 1):
        return False
    if orientation == 'v' and (x >= BOARD_SIZE - 1 or y >= BOARD_SIZE - 1):
        return False
    if wall_pos in walls:
        return False
    return True

# BFS to check for a valid path
def has_path(board, start, goal, walls):
    queue = deque([start])
    visited = set()
    while queue:
        x, y = queue.popleft()
        if (x, y) == goal:
            return True
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE:
                if is_valid_move(board, (x, y), (nx, ny), walls):
                    queue.append((nx, ny))
    return False

# Game loop
def play_game():
    board = initialize_board()
    walls = {}
    player1_pos = (0, BOARD_SIZE // 2)
    player2_pos = (BOARD_SIZE - 1, BOARD_SIZE // 2)
    player1_walls = 10
    player2_walls = 10

    board[player1_pos[0]][player1_pos[1]] = "1"
    board[player2_pos[0]][player2_pos[1]] = "2"

    current_player = 1

    while True:
        terminal_refresh()
        display_board(board, walls)
        console.print(f"Player {current_player}'s turn", style="bold green")

        action = console.input("Choose action (move/wall): ").strip().lower()
        if action == "move":
            x, y = map(int, console.input("Enter new position (x y): ").split())
            new_pos = (x, y)
            if current_player == 1:
                if is_valid_move(board, player1_pos, new_pos, walls):
                    board[player1_pos[0]][player1_pos[1]] = " "
                    player1_pos = new_pos
                    board[x][y] = "1"
                else:
                    console.print("Invalid move!", style="bold red")
                    continue
            else:
                if is_valid_move(board, player2_pos, new_pos, walls):
                    board[player2_pos[0]][player2_pos[1]] = " "
                    player2_pos = new_pos
                    board[x][y] = "2"
                else:
                    console.print("Invalid move!", style="bold red")
                    continue
        elif action == "wall":
            wall_input = console.input("Enter wall position (x y orientation[h/v]): ").split()
            if len(wall_input) != 3:
                console.print("Invalid input! Please enter x, y, and orientation (h/v).", style="bold red")
                continue
            try:
                x, y = int(wall_input[0]), int(wall_input[1])
                orientation = wall_input[2]
                wall_pos = (x, y, orientation)
                if is_valid_wall(walls, wall_pos):
                    walls[wall_pos] = "---" if orientation == 'h' else "|"
                    if current_player == 1:
                        player1_walls -= 1
                    else:
                        player2_walls -= 1
                else:
                    console.print("Invalid wall placement!", style="bold red")
                    continue
            except ValueError:
                console.print("Invalid input! Coordinates must be integers.", style="bold red")
                continue
        else:
            console.print("Invalid action!", style="bold red")
            continue

        # Check for win
        if player1_pos[0] == BOARD_SIZE - 1:
            console.print("Player 1 wins!", style="bold green")
            break
        elif player2_pos[0] == 0:
            console.print("Player 2 wins!", style="bold green")
            break

        current_player = 3 - current_player

# Refresh terminal
def terminal_refresh():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    play_game()
