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
    console.print("\n  " + "   ".join(map(str, range(1, BOARD_SIZE + 1))), style="bold cyan")  # تغییر شماره‌گذاری ستون‌ها
    for i, row in enumerate(board):
        # نمایش ردیف مهره‌ها
        row_str = " | ".join(row)
        console.print(f"{i + 1} {row_str}")  # تغییر شماره‌گذاری ردیف‌ها
        
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
def is_valid_move(board, player_pos, new_pos, walls, opponent_pos):
    x, y = player_pos
    nx, ny = new_pos
    if not (0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE):
        return False
    if abs(x - nx) + abs(y - ny) > 2:  # حرکت باید فقط یک یا دو خانه باشد
        return False

    # اگر مهره حریف در مسیر حرکت قرار دارد، بررسی می‌کنیم که آیا می‌توان از روی آن بپرید
    if abs(x - nx) == 2 and y == ny:  # حرکت عمودی
        mid_x = (x + nx) // 2
        if (mid_x, y) == opponent_pos:  # اگر مهره حریف وسط مسیر است
            if (mid_x, y, 'h') in walls:  # اگر دیوار وجود داشته باشد، نمی‌توان از روی مهره پرید
                return False
            return True
    elif abs(y - ny) == 2 and x == nx:  # حرکت افقی
        mid_y = (y + ny) // 2
        if (x, mid_y) == opponent_pos:  # اگر مهره حریف وسط مسیر است
            if (x, mid_y, 'v') in walls:  # اگر دیوار وجود داشته باشد، نمی‌توان از روی مهره پرید
                return False
            return True

    # بررسی دیوارها برای حرکت معمولی (یک خانه به جلو یا عقب)
    if x == nx:  # حرکت افقی
        if (x, min(y, ny), 'h') in walls:
            return False
    elif y == ny:  # حرکت عمودی
        if (min(x, nx), y, 'v') in walls:
            return False

    # اگر خانه مقصد توسط مهره دیگری اشغال شده باشد
    if board[nx][ny] != " ":
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
                if is_valid_move(board, (x, y), (nx, ny), walls, goal):
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

        # نمایش تعداد دیوارهای باقی‌مانده برای بازیکن فعلی
        if current_player == 1:
            console.print(f"Player 1 has {player1_walls} walls left.", style="bold cyan")
        else:
            console.print(f"Player 2 has {player2_walls} walls left.", style="bold cyan")

        action = console.input("Choose action (move/wall): ").strip().lower()
        if action == "move":
            x, y = map(int, console.input("Enter new position (x y): ").split())
            new_pos = (x - 1, y - 1)  # تغییرات برای هماهنگ کردن با شماره‌گذاری جدید
            if current_player == 1:
                if is_valid_move(board, player1_pos, new_pos, walls, player2_pos):
                    board[player1_pos[0]][player1_pos[1]] = " "
                    player1_pos = new_pos
                    board[x - 1][y - 1] = "1"
                else:
                    console.print("Invalid move!", style="bold red")
                    continue
            else:
                if is_valid_move(board, player2_pos, new_pos, walls, player1_pos):
                    board[player2_pos[0]][player2_pos[1]] = " "
                    player2_pos = new_pos
                    board[x - 1][y - 1] = "2"
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
                wall_pos = (x - 1, y - 1, orientation)  # تغییرات برای هماهنگ کردن با شماره‌گذاری جدید
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
