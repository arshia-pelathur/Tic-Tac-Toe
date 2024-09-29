import numpy as np

class TicTacToe:
    def __init__(self):
        self.board = np.full((3, 3), "")  # Empty 3x3 board
        self.current_winner = None

    def make_move(self, row, col, player):
        if self.board[row, col] == "" and self.current_winner is None:
            self.board[row, col] = player
            if self.check_winner(player):
                self.current_winner = player
            return True
        return False

    def check_winner(self, player):
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            if all(self.board[i, :] == player) or all(self.board[:, i] == player):
                return True
        if all(np.diag(self.board) == player) or all(np.diag(np.fliplr(self.board)) == player):
            return True
        return False

    def is_draw(self):
        return "" not in self.board and self.current_winner is None

    def get_ai_move(self):
        best_score = float('-inf')
        best_move = None

        # Iterate through empty cells to find the best move
        for row in range(3):
            for col in range(3):
                if self.board[row, col] == "":
                    # Make the move temporarily
                    self.board[row, col] = "O"
                    score = self.minimax(depth=0, is_maximizing=False)
                    # Undo the move
                    self.board[row, col] = ""
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)

        return best_move

    def minimax(self, depth, is_maximizing):
        # Check for terminal states
        if self.check_winner("O"):
            return 1
        elif self.check_winner("X"):
            return -1
        elif self.is_draw():
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for row in range(3):
                for col in range(3):
                    if self.board[row, col] == "":
                        # Make the move temporarily
                        self.board[row, col] = "O"
                        score = self.minimax(depth + 1, False)
                        # Undo the move
                        self.board[row, col] = ""
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for row in range(3):
                for col in range(3):
                    if self.board[row, col] == "":
                        # Make the move temporarily
                        self.board[row, col] = "X"
                        score = self.minimax(depth + 1, True)
                        # Undo the move
                        self.board[row, col] = ""
                        best_score = min(score, best_score)
            return best_score

    def reset(self):
        self.board = np.full((3, 3), "")
        self.current_winner = None
