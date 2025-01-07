import random
from collections import deque

class QuoridorGame:
    def __init__(self):
        self.board_size = 17
        self.board = [[None for x in range(self.board_size)] for _ in range(self.board_size)]
        self.walls = set()
        self.players = {
            1: {"position": (0, 8), "walls": 10},
            2: {"position": (16, 8), "walls": 10},
        }
        self.current_player = random.choice([1, 2])

    def print_board(self):
        
        for row in range(self.board_size):
            line = ""
            for col in range(self.board_size):
                if (row, col) == self.players[1]["position"]:
                    line += "🔵"  # Player 1
                elif (row, col) == self.players[2]["position"]:
                    line += "🔴"  # Player 2
                elif (row, col) in self.walls:
                    line += "🧱"  # Wall segment
                elif row % 2 == 0 and col % 2 == 0:
                    line += "⚫"  # Board node
                elif row % 2 == 1 and col % 2 == 1 and (
                    (row - 1, col) in self.walls and (row + 1, col) in self.walls
                    or (row, col - 1) in self.walls and (row, col + 1) in self.walls
                ):
                    line += "🧱"  # Fill gap between walls
                else:
                    line += "⚪"  # Board path
            print(line)
        print(f"\nPlayer {self.current_player} {"🔴" if self.current_player == 2 else "🔵"}. Walls: {self.players[self.current_player]['walls']}")


    def is_valid_move(self, player, direction):
        x, y = self.players[player]["position"]
        dx, dy = {"u": (-2, 0), "d": (2, 0), "l": (0, -2), "r": (0, 2)}[direction]
        wall_dx, wall_dy = {"u": (-1, 0), "d": (1, 0), "l": (0, -1), "r": (0, 1)}[direction]
        new_x, new_y = x + dx, y + dy
        wall_x, wall_y = x + wall_dx, y + wall_dy

        if not (0 <= new_x < self.board_size and 0 <= new_y < self.board_size):
            return False

        if (wall_x, wall_y) in self.walls or (new_x % 2 != 0 or new_y % 2 != 0):
            return False

        return True
    
    def move_player(self, player, direction):
        x, y = self.players[player]["position"]
        dx, dy = {"u": (-2, 0), "d": (2, 0), "l": (0, -2), "r": (0, 2)}[direction]
        wall_dx, wall_dy = {"u": (-1, 0), "d": (1, 0), "l": (0, -1), "r": (0, 1)}[direction]
        new_x, new_y = x + dx, y + dy
        wall_x, wall_y = x + wall_dx, y + wall_dy

        other_player = 3 - player
        other_x, other_y = self.players[other_player]["position"]

        if (new_x , new_y) == (other_x , other_y):
            jump_x , jump_y = other_x + dx, other_y + dy
            if (0 <= jump_x < self.board_size and 0 <= jump_y < self.board_size and
                    self.is_valid_move(player, direction) and
                    (jump_x % 2 == 0 and jump_y % 2 == 0)):
                self.players[player]["position"] = (jump_x, jump_y)
                return True
            else:
                print("Invalid move: Cannot jump over the other player.")
                return False

        if not self.is_valid_move(player, direction):
            print(f"Invalid move for player {player} in direction {direction}.")
            return False

        self.players[player]["position"] = (new_x, new_y)
        return True
    
    def is_valid_wall(self, wall):
        # Check if the wall points are within bounds and do not overlap existing walls
        for point in wall:
            if not (0 <= point[0] < self.board_size and 0 <= point[1] < self.board_size):
                return False

            if point in self.walls or (point[0] % 2 == 0 and point[1] % 2 == 0):
                return False

        # Check for wall intersection or continuity
        if len(wall) == 2:
            x1, y1 = wall[0]
            x2, y2 = wall[1]
            for existing_wall in self.walls:
                ex1, ey1 = existing_wall
                for ex2, ey2 in self.walls:
                    # Check if walls cross each other (e.g., form a + shape)
                    if (x1 == ex1 and y1 == ey1 and x2 == ex2 and y2 == ey2) or \
                    (x1 == ex2 and y1 == ey2 and x2 == ex1 and y2 == ey1):
                        return False

                    # Allow walls to be in continuity
                    if (x1 == ex1 and x2 == ex2 and abs(y1 - ey1) == 2 and abs(y2 - ey2) == 2) or \
                    (y1 == ey1 and y2 == ey2 and abs(x1 - ex1) == 2 and abs(x2 - ex2) == 2):
                        continue

                    # Check if walls intersect diagonally
                    if (abs(x1 - ex1) == 1 and abs(y1 - ey1) == 1) or \
                    (abs(x2 - ex2) == 1 and abs(y2 - ey2) == 1):
                        return False

        # Temporarily add wall for path-checking
        for point in wall:
            self.walls.add(point)

        if not self.has_path(1) or not self.has_path(2):
            for point in wall:
                self.walls.remove(point)
            return False

        # Remove temporary wall
        for point in wall:
            self.walls.remove(point)

        return True


    def place_wall(self, player, x1, y1, orientation):
        if self.players[player]["walls"] == 0:
            print(f"Player {player} has no walls left.")
            return False

        if orientation == "h":
            if x1 % 2 == 1 and y1 % 2 == 0:
                wall = [(x1, y1), (x1, y1 + 2)]
            else:
                print("Invalid wall position. Walls must align with '⚫' positions.")
                return False
        elif orientation == "v":
            if x1 % 2 == 0 and y1 % 2 == 1:
                wall = [(x1, y1), (x1 + 2, y1)]
            else:
                print("Invalid wall position. Walls must align with '⚫' positions.")
                return False
        else:
            print("Invalid orientation. Use 'h' for horizontal or 'v' for vertical.")
            return False

        # Check if the wall placement is valid
        if not self.is_valid_wall(wall):
            print("Invalid wall placement. Walls cannot overlap, intersect, or block all paths.")
            return False

        # Finalize the wall placement
        for point in wall:
            self.walls.add(point)
        self.players[player]["walls"] -= 1
        return True



    def has_path(self, player):
        start = self.players[player]["position"]
        goal_row = 0 if player == 2 else self.board_size - 1  # Player 1 targets bottom row, Player 2 targets top row

        visited = set()
        stack = [start]

        while stack:
            x, y = stack.pop()
            if x == goal_row:
                return True

            if (x, y) in visited:
                continue
            visited.add((x, y))

            for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
                nx, ny = x + dx, y + dy
                wall_x, wall_y = x + dx // 2, y + dy // 2

                if (0 <= nx < self.board_size and 0 <= ny < self.board_size and
                        (nx % 2 == 0 and ny % 2 == 0) and  # Ensure it's a valid node
                        (wall_x, wall_y) not in self.walls and  # Check no wall in the way
                        (nx, ny) not in visited):
                    stack.append((nx, ny))

        return False


    def check_winner(self):
        for player in [1, 2]:
            x, _ = self.players[player]["position"]
            if (player == 1 and x == self.board_size - 1) or (player == 2 and x == 0):
                return player
        return None

    def play_turn(self):
        while True:
            self.print_board()
            action = input("Choose action (m:move / w:wall): ").strip().lower()

            if action == "m":
                direction = input("Choose direction (u:up / d:down / l:left / r:right): ").strip().lower()
                if self.move_player(self.current_player, direction):
                    winner = self.check_winner()
                    if winner:
                        self.print_board()
                        print(f"Player {winner} wins!")
                        return True
                    break
                else:
                    print("Invalid move. Try again.")
            elif action == "w":
                try:
                    x1, y1 = map(int, input("Enter the starting point of the wall (x y): ").split())
                    orientation = input("Enter orientation (h:horizontal / v:vertical): ").strip().lower()
                    if self.place_wall(self.current_player, x1, y1, orientation):
                        print("Wall placed.")
                        break
                    else:
                        print("Invalid wall placement. Try again.")
                except ValueError:
                    print("Invalid input. Please enter integers for coordinates.")
            else:
                print("Invalid action. Try again.")

        self.current_player = 3 - self.current_player
        return False


game = QuoridorGame()
game_running = True
while game_running:
    game_running = not game.play_turn() 