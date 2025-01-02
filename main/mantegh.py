import random
from collections import deque

class QuoridorGame:
    def __init__(self):
        self.board_size = 9
        self.board = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.walls = set()
        self.players = {
            1: {"position": (0, 4), "walls": 10},
            2: {"position": (8, 4), "walls": 10},
        }
        self.current_player = random.choice([1, 2])

    def print_board(self):
        for row in range(self.board_size):
            line = ""
            for col in range(self.board_size):
                if (row, col) == self.players[1]["position"]:
                    line += "P1 "
                elif (row, col) == self.players[2]["position"]:
                    line += "P2 "
                else:
                    line += ".  "
            print(line)
        print()

    def is_valid_move(self, player, direction):
        x, y = self.players[player]["position"]
        dx, dy = {"u": (-1, 0), "d": (1, 0), "l": (0, -1), "r": (0, 1)}[direction]
        new_x, new_y = x + dx, y + dy

        # Check boundaries
        if not (0 <= new_x < self.board_size and 0 <= new_y < self.board_size):
            return False

        # Check walls
        if direction in ["u", "d"]:
            wall = ((min(x, new_x), y), (min(x, new_x), y + 1))
        else:  # "left" or "right"
            wall = ((x, min(y, new_y)), (x + 1, min(y, new_y)))

        if wall in self.walls:
            return False

        return True

    def move_player(self, player, direction):
        if not self.is_valid_move(player, direction):
            print(f"Invalid move for player {player} in direction {direction}.")
            return False

        dx, dy = {"u": (-1, 0), "d": (1, 0), "l": (0, -1), "r": (0, 1)}[direction]
        x, y = self.players[player]["position"]
        new_x, new_y = x + dx, y + dy

        # Check if the new position is occupied by the other player
        for other_player in [1, 2]:
            if other_player != player and self.players[other_player]["position"] == (new_x, new_y):
                # Check if the other player is adjacent and if the next space is empty
                jump_x, jump_y = new_x + dx, new_y + dy
                if (0 <= jump_x < self.board_size and 0 <= jump_y < self.board_size and
                    (jump_x, jump_y) not in [self.players[1]["position"], self.players[2]["position"]] and
                    self.is_valid_move(player, direction)):
                    print(f"Player {player} jumps over Player {other_player}.")
                    self.players[player]["position"] = (jump_x, jump_y)
                    return True
                else:
                    print(f"Invalid move: Player {other_player} is blocking the path.")
                    return False

        # If no jump, just move normally
        self.players[player]["position"] = (new_x, new_y)
        return True



    def is_valid_wall(self, wall):
        # Wall must not overlap existing walls
        if wall in self.walls:
            return False

        # Wall must not block all paths
        self.walls.add(wall)
        if not self.has_path(1) or not self.has_path(2):
            self.walls.remove(wall)
            return False

        self.walls.remove(wall)
        return True

    def place_wall(self, player, wall):
        if self.players[player]["walls"] == 0:
            print(f"Player {player} has no walls left.")
            return False

        if not self.is_valid_wall(wall):
            print("Invalid wall placement.")
            return False

        self.walls.add(wall)
        self.players[player]["walls"] -= 1
        return True

    def has_path(self, player):
        start = self.players[player]["position"]
        goal_row = 0 if player == 1 else self.board_size - 1

        visited = set()
        queue = deque([start])

        while queue:
            x, y = queue.popleft()
            if x == goal_row:
                return True

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if (0 <= nx < self.board_size and 0 <= ny < self.board_size and
                        (nx, ny) not in visited and self.is_valid_move(player, "up")):
                    visited.add((nx, ny))
                    queue.append((nx, ny))

        return False

    def check_winner(self):
        for player in [1, 2]:
            x, _ = self.players[player]["position"]
            if (player == 1 and x == self.board_size - 1) or (player == 2 and x == 0):
                return player
        return None

    def play_turn(self):
        while True:
            print(f"Player {self.current_player}'s turn.")
            self.print_board()
            action = input("Choose action (m:move / w:wall): ").strip().lower()

            if action == "m":
                direction = input("Choose direction (u:up / d:down / l:left / r:right): ").strip().lower()
                if self.move_player(self.current_player, direction):
                    winner = self.check_winner()
                    if winner:
                        print(f"Player {winner} wins!")
                        return True
                    break
                else:
                    print("Invalid move. Try again.")

            elif action == "w":
                try:
                    x1, y1 = map(int, input("Enter the first point of the wall (x1 y1): ").split())
                    x2, y2 = map(int, input("Enter the second point of the wall (x2 y2): ").split())
                    wall = ((x1, y1), (x2, y2))
                    if self.place_wall(self.current_player, wall):
                        print("Wall placed.")
                        break
                    else:
                        print("Invalid wall placement. Try again.")
                except ValueError:
                    print("Invalid input. Please enter integers for coordinates.")
            else:
                print("Invalid action. Try again.")

        self.current_player = 3 - self.current_player  # Switch player
        return False


# Run the game
game = QuoridorGame()
game_running = True
while game_running:
    game_running = not game.play_turn()
