from tkinter import *
from tkinter import messagebox
from functools import partial

class CaroGUI:
    def __init__(self):
        self.game = Caro()

        self.root = Tk()
        self.root.title("Caro")

        self.buttons = {}
        for row in range(3):
            for column in range(3):
                self.buttons[row, column] = Button(self.root, text='', font=('Arial', 20, 'bold'), width=6, height=3,
                                                   command=partial(self.handle_click, row, column))
                self.buttons[row, column].grid(row=row, column=column)

    def handle_click(self, row, column):
        if self.game.board[row * 3 + column] == ' ':
            self.game.board[row * 3 + column] = 'X'
            self.buttons[row, column].config(text='X')
            if self.game.is_winner('X'):
                self.display_message("You win!")
                return
            if ' ' not in self.game.board:
                self.display_message("Draw!")
                return
            ai_move = self.game.find_best_move()
            self.game.board[ai_move] = 'O'
            ai_row, ai_column = divmod(ai_move, 3)
            self.buttons[ai_row, ai_column].config(text='O')
            if self.game.is_winner('O'):
                self.display_message("You lose!")
                return
            if ' ' not in self.game.board:
                self.display_message("Draw!")

    def display_message(self, message):
        response = messagebox.askyesno("Game Over", message + "\nDo you want to play again?")
        if response:
            self.reset_board()

    def reset_board(self):
        for row in range(3):
            for column in range(3):
                self.game.board[row * 3 + column] = ' '
                self.buttons[row, column].config(text='')
        self.root.update()

    def run(self):
        self.root.mainloop()

class Caro:
    def __init__(self):
        self.board = [' ' for _ in range(9)]

    def print_board(self):
        row1 = '|'.join(self.board[0:3])
        row2 = '|'.join(self.board[3:6])
        row3 = '|'.join(self.board[6:9])
        print(row1)
        print('-' * 5)
        print(row2)
        print('-' * 5)
        print(row3)

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == ' ']

    def is_winner(self, symbol):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for condition in win_conditions:
            if all(self.board[i] == symbol for i in condition):
                return True
        return False

    def minimax(self, maximizing_player, depth):
        if self.is_winner('O'):
            return 10 - depth
        if self.is_winner('X'):
            return depth - 10
        if ' ' not in self.board:
            return 0
        if maximizing_player:
            max_eval = float('-inf')
            for move in self.available_moves():
                self.board[move] = 'O'
                eval = self.minimax(False, depth + 1)
                self.board[move] = ' '
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for move in self.available_moves():
                self.board[move] = 'X'
                eval = self.minimax(True, depth + 1)
                self.board[move] = ' '
                min_eval = min(min_eval, eval)
            return min_eval

    def find_best_move(self):
        best_move = -1
        best_eval = float('-inf')
        for move in self.available_moves():
            self.board[move] = 'O'
            eval = self.minimax(False, 0)
            self.board[move] = ' '
            if eval > best_eval:
                best_eval = eval
                best_move = move
        return best_move

game_caro = CaroGUI()
game_caro.run()