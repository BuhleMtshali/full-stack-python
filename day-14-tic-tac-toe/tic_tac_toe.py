import random

class Player:
    def __init__(self, name, symbol, is_computer=False):
        self.name = name
        self.symbol = symbol
        self.is_computer = is_computer


class Board:
    def __init__(self):
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]
        self.positions = {'A': 0, 'B': 1, 'C': 2}
        self.columns = {'1': 0, '2': 1, '3': 2}

    def display(self):
        print("\n    1   2   3")
        print("  +---+---+---+")
        for i, row in enumerate(['A', 'B', 'C']):
            print(f"{row} | " + " | ".join(self.grid[i]) + " |")
            print("  +---+---+---+")

    def is_valid_move(self, move):
        if len(move) == 2 and move[0] in self.positions and move[1] in self.columns:
            row, col = self.positions[move[0]], self.columns[move[1]]
            return self.grid[row][col] == ' '
        return False

    def make_move(self, move, symbol):
        row, col = self.positions[move[0]], self.columns[move[1]]
        self.grid[row][col] = symbol

    def check_winner(self, symbol):
        for i in range(3):
            if all(self.grid[i][j] == symbol for j in range(3)) or \
               all(self.grid[j][i] == symbol for j in range(3)):
                return True
        if all(self.grid[i][i] == symbol for i in range(3)) or \
           all(self.grid[i][2 - i] == symbol for i in range(3)):
            return True
        return False

    def is_full(self):
        return all(cell != ' ' for row in self.grid for cell in row)

    def get_empty_positions(self):
        empty = []
        for row_key, r in self.positions.items():
            for col_key, c in self.columns.items():
                if self.grid[r][c] == ' ':
                    empty.append(f"{row_key}{col_key}")
        return empty

    def reset(self):
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]


class Game:
    def __init__(self):
        self.board = Board()
        self.scores = {'X': 0, 'O': 0, 'Draws': 0}

    def play(self):
        print("🎮 Welcome to Tic Tac Toe!")
        mode = input("Choose mode (1: Player vs Player, 2: Player vs Computer): ")

        if mode == '1':
            p1_name = input("Enter Player 1 name: ")
            p2_name = input("Enter Player 2 name: ")
            player1 = Player(p1_name, 'X')
            player2 = Player(p2_name, 'O')
        else:
            p1_name = input("Enter your name: ")
            player1 = Player(p1_name, 'X')
            player2 = Player("Computer", 'O', is_computer=True)

        current = player1
        self.board.display()

        while True:
            print(f"\n{current.name}'s turn ({current.symbol})")

            if current.is_computer:
                move = self.get_computer_move(current.symbol, player1.symbol)
                print(f"Computer chooses: {move}")
            else:
                move = input("Enter position (e.g., A1, B2): ").upper()

            if self.board.is_valid_move(move):
                self.board.make_move(move, current.symbol)
                self.board.display()

                if self.board.check_winner(current.symbol):
                    print(f"\n🏆 {current.name} wins!")
                    self.scores[current.symbol] += 1
                    break

                if self.board.is_full():
                    print("\n🤝 It's a draw!")
                    self.scores['Draws'] += 1
                    break

                current = player2 if current == player1 else player1
            else:
                print("❌ Invalid move! Try again.")

        self.show_scoreboard()
        self.replay()

    def get_computer_move(self, ai_symbol, human_symbol):
        for move in self.board.get_empty_positions():
            self.board.make_move(move, ai_symbol)
            if self.board.check_winner(ai_symbol):
                self.board.make_move(move, ' ')
                return move
            self.board.make_move(move, ' ')


        for move in self.board.get_empty_positions():
            self.board.make_move(move, human_symbol)
            if self.board.check_winner(human_symbol):
                self.board.make_move(move, ' ')
                return move
            self.board.make_move(move, ' ')

        
        if 'B2' in self.board.get_empty_positions():
            return 'B2'

        
        for corner in ['A1', 'A3', 'C1', 'C3']:
            if corner in self.board.get_empty_positions():
                return corner

       
        return random.choice(self.board.get_empty_positions())

    def show_scoreboard(self):
        print("\n===== Scoreboard =====")
        for key, val in self.scores.items():
            print(f"{key}: {val}")

    def replay(self):
        again = input("\nPlay again? (y/n): ").lower()
        if again == 'y':
            self.board.reset()
            self.play()
        else:
            print("\n👋 Thanks for playing Tic Tac Toe!")



if __name__ == "__main__":
    Game().play()
