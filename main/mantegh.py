import random
from collections import deque

class QuoridorGame:
    def __init__(self):
        self.board_size = 9
        self.board = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.horizontal_walls = set()
        self.vertical_walls = set()
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

                if col < self.board_size - 1:
                    if ((row, col), (row + 1, col)) in self.vertical_walls:
                        line += "| "
                    else:
                        line += "  "

            print(line)

            if row < self.board_size - 1:
                line = ""
                for col in range(self.board_size):
                    if ((row, col), (row, col + 1)) in self.horizontal_walls:
                        line += "---"
                    else:
                        line += "   "

                    if col < self.board_size - 1:
                        line += "  "
                print(line)

        print(f"\nPlayer {self.current_player}. Walls: {self.players[self.current_player]['walls']}\n")

    def is_valid_move(self, player, direction):
        x, y = self.players[player]["position"]
        dx, dy = {"u": (-1, 0), "d": (1, 0), "l": (0, -1), "r": (0, 1)}[direction]
        new_x, new_y = x + dx, y + dy

        if not (0 <= new_x < self.board_size and 0 <= new_y < self.board_size):
            return False

        if direction == "u" and ((new_x, y), (x, y)) in self.horizontal_walls:
            return False
        if direction == "d" and ((x, y), (new_x, y)) in self.horizontal_walls:
            return False
        if direction == "l" and ((x, new_y), (x, y)) in self.vertical_walls:
            return False
        if direction == "r" and ((x, y), (x, new_y)) in self.vertical_walls:
            return False

        if direction == "u" and (new_x - 1 >= 0 and ((new_x - 1, y), (new_x, y)) in self.horizontal_walls):
            return False
        if direction == "d" and (new_x + 1 < self.board_size and ((x, y), (new_x + 1, y)) in self.horizontal_walls):
            return False
        if direction == "l" and (new_y - 1 >= 0 and ((x, new_y - 1), (x, new_y)) in self.vertical_walls):
            return False
        if direction == "r" and (new_y + 1 < self.board_size and ((x, y), (x, new_y + 1)) in self.vertical_walls):
            return False

        return True

    def move_player(self, player, direction):
        if not self.is_valid_move(player, direction):
            print(f"Invalid move for player {player} in direction {direction}.")
            return False

        dx, dy = {"u": (-1, 0), "d": (1, 0), "l": (0, -1), "r": (0, 1)}[direction]
        x, y = self.players[player]["position"]
        new_x, new_y = x + dx, y + dy

        for other_player in [1, 2]:
            if other_player != player and self.players[other_player]["position"] == (new_x, new_y):
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

        self.players[player]["position"] = (new_x, new_y)
        return True

    def is_valid_wall(self, wall):
        if wall in self.horizontal_walls or wall in self.vertical_walls:
            return False

        if wall[0][0] == wall[1][0]:
            self.horizontal_walls.add(wall)
        else:
            self.vertical_walls.add(wall)

        if not self.has_path(1) or not self.has_path(2):
            if wall in self.horizontal_walls:
                self.horizontal_walls.remove(wall)
            else:
                self.vertical_walls.remove(wall)
            return False

        if wall in self.horizontal_walls:
            self.horizontal_walls.remove(wall)
        else:
            self.vertical_walls.remove(wall)

        return True

    def place_wall(self, player, wall):
        if self.players[player]["walls"] == 0:
            print(f"Player {player} has no walls left.")
            return False

        if not self.is_valid_wall(wall):
            print("Invalid wall placement.")
            return False

        if wall[0][0] == wall[1][0]:
            self.horizontal_walls.add(wall)
        else:
            self.vertical_walls.add(wall)

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

            for dx, dy, direction in [(-1, 0, "u"), (1, 0, "d"), (0, -1, "l"), (0, 1, "r")]:
                nx, ny = x + dx, y + dy
                if (0 <= nx < self.board_size and 0 <= ny < self.board_size and
                        (nx, ny) not in visited and self.is_valid_move(player, direction)):
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

        self.current_player = 3 - self.current_player
        return False


game = QuoridorGame()
game_running = True
while game_running:
    game_running = not game.play_turn()
