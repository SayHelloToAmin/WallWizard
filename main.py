import random
from collections import deque

class Quoridor:
    def __init__(self):
        self.board_size = 9
        self.players = {1: (0, self.board_size // 2), 2: (self.board_size - 1, self.board_size // 2)}
        self.walls = []  # List of wall positions
        self.current_player = random.choice([1, 2])
        self.fences_per_player = 10
        self.fences_remaining = {1: self.fences_per_player, 2: self.fences_per_player}

    def display_board(self):
        """Display the board with pawns and walls."""
        board = [[" . " for _ in range(self.board_size)] for _ in range(self.board_size)]

        for player, position in self.players.items():
            x, y = position
            board[x][y] = f" P{player} "

        for wall in self.walls:
            x, y, orientation = wall
            if orientation == 'h':
                board[x][y] = "==="
            elif orientation == 'v':
                board[x][y] = " | "

        for row in board:
            print("".join(row))
        print()

    def is_valid_wall(self, x, y, orientation):
        """Check if the wall placement is valid."""
        if (x, y, orientation) in self.walls:
            return False

        if orientation == 'h' and (x >= self.board_size - 1 or y >= self.board_size - 1):
            return False

        if orientation == 'v' and (x >= self.board_size - 1 or y >= self.board_size - 1):
            return False

        simulated_walls = self.walls + [(x, y, orientation)]
        for player, position in self.players.items():
            if not self.has_path(position, player, simulated_walls):
                return False

        return True

    def has_path(self, start, player, walls):
        """Check if there is a path from the current position to the goal row."""
        goal_row = 0 if player == 2 else self.board_size - 1
        queue = deque([start])
        visited = set()

        while queue:
            x, y = queue.popleft()
            if x == goal_row:
                return True

            if (x, y) in visited:
                continue
            visited.add((x, y))

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.board_size and 0 <= ny < self.board_size and not self.is_blocked(x, y, nx, ny, walls):
                    queue.append((nx, ny))

        return False

    def is_blocked(self, x1, y1, x2, y2, walls):
        """Check if there is a wall blocking movement between two squares."""
        for wall_x, wall_y, orientation in walls:
            if orientation == 'h' and ((wall_x == x1 == x2 - 1 and wall_y <= y1 < wall_y + 1) or (wall_x == x2 == x1 - 1 and wall_y <= y2 < wall_y + 1)):
                return True
            if orientation == 'v' and ((wall_y == y1 == y2 - 1 and wall_x <= x1 < wall_x + 1) or (wall_y == y2 == y1 - 1 and wall_x <= x2 < wall_x + 1)):
                return True
        return False

    def move_pawn(self, direction):
        """Move the pawn in the specified direction if valid."""
        x, y = self.players[self.current_player]
        dx, dy = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}.get(direction, (0, 0))
        nx, ny = x + dx, y + dy

        if 0 <= nx < self.board_size and 0 <= ny < self.board_size and not self.is_blocked(x, y, nx, ny, self.walls):
            self.players[self.current_player] = (nx, ny)
            if nx == 0 and self.current_player == 2 or nx == self.board_size - 1 and self.current_player == 1:
                print(f"Player {self.current_player} wins!")
                exit()
        else:
            print("Invalid move. Try again.")

    def place_wall(self, x, y, orientation):
        """Place a wall if valid."""
        if self.fences_remaining[self.current_player] > 0 and self.is_valid_wall(x, y, orientation):
            self.walls.append((x, y, orientation))
            self.fences_remaining[self.current_player] -= 1
        else:
            print("Invalid wall placement. Try again.")

    def play_turn(self):
        """Play a single turn for the current player."""
        print(f"Player {self.current_player}'s turn")
        action = input("Choose action (move/wall/exit): ").strip().lower()

        if action == 'move':
            direction = input("Direction (up/down/left/right): ").strip().lower()
            self.move_pawn(direction)
        elif action == 'wall':
            x, y = map(int, input("Wall position (x y): ").split())
            orientation = input("Orientation (h/v): ").strip().lower()
            self.place_wall(x, y, orientation)
        elif action == 'exit':
            print("Game exited.")
            exit()
        else:
            print("Invalid action. Try again.")

        self.current_player = 1 if self.current_player == 2 else 2

    def play_game(self):
        """Main game loop."""
        while True:
            self.display_board()
            self.play_turn()

if __name__ == "__main__":
    game = Quoridor()
    game.play_game()
