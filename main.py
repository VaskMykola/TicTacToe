import random


class TicTacToe:
    roles = ["X", "O"]

    def __init__(self):
        self.board = [
            ["_", "_", "_"],
            ["_", "_", "_"],
            ["_", "_", "_"]
        ]

    def print_board(self):
        for row in self.board:
            print(row)

    def multi_player(self):
        while True:
            self.print_board()
            if self.player_move("X"):
                print("game finished")
                self.print_board()
                if self.check_winner():
                    print("'X' won")
                break

            self.print_board()

            if self.player_move("O"):
                print("game finished")
                self.print_board()
                if self.check_winner():
                    print("'O' won")

                break

    def single_player(self):
        try:
            role = self.roles[int(input("Enter 0 for X or 1 for O: "))]
        except ValueError:
            print("Please enter a number")
            self.single_player()
        except IndexError:
            print("Please enter 0 or 1")
            self.single_player()
        computer_role = self.roles[0] if role == self.roles[1] else self.roles[1]
        while True:
            self.print_board()
            if self.player_move(role):
                print("game finished")
                self.print_board()
                if self.check_winner():
                    print("You won")
                break

            self.print_board()

            if self.computer_move(computer_role):
                print("game finished")
                self.print_board()
                if self.check_winner():
                    print("Computer won")

                break

    def check_draw(self):
        if "_" not in self.board[0] and "_" not in self.board[1] and "_" not in self.board[2]:
            print("Draw")
            return True

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "_":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "_":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "_":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "_":
            return True

    def is_game_finished(self):
        return self.check_winner() or self.check_draw()

    def player_move(self, role):
        while True:
            try:
                row = int(input("Enter row: "))
                column = int(input("Enter column: "))
                if self.board[row][column] == "_":
                    self.board[row][column] = role
                    break
                else:
                    print("This cell is already taken")
            except ValueError:
                print("Please enter a number")
            except IndexError:
                print("Please enter a number between 0 and 2")
        return self.is_game_finished()

    def computer_move(self, role):
        while True:
            row = random.randint(0, 2)
            column = random.randint(0, 2)
            if self.board[row][column] == "_":
                self.board[row][column] = role
                break
        return self.is_game_finished()


if __name__ == '__main__':
    game = TicTacToe()
    while True:
        try:
            mode = int(input("Enter 0 for single player or 1 for multi player: "))
            if mode == 0:
                game.single_player()
                break
            elif mode == 1:
                game.multi_player()
                break
            else:
                print("Please enter 0 or 1")
        except ValueError:
            print("Please enter a number")
