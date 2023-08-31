import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title('Tic Tac Toe')
        self.board = [['', '', ''], ['', '', ''], ['', '', '']]
        self.current_player = 'X'
        self.create_widgets()

    def create_widgets(self):
        # Create the buttons
        self.buttons = []
        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(self.master, text='', font=('Arial', 30), width=3, height=1,
                                   command=lambda row=row, col=col: self.button_click(row, col))
                button.grid(row=row, column=col)
                button_row.append(button)
            self.buttons.append(button_row)

        # Create the status label
        self.status_label = tk.Label(self.master, text='Player X\'s turn', font=('Arial', 16))
        self.status_label.grid(row=3, column=0, columnspan=3)

        # Create the reset button
        self.reset_button = tk.Button(self.master, text='Reset', font=('Arial', 16), command=self.reset)
        self.reset_button.grid(row=4, column=0, columnspan=3)

    def button_click(self, row, col):
        if self.board[row][col] == '':
            self.buttons[row][col].config(text=self.current_player)
            self.board[row][col] = self.current_player
            if self.check_win():
                messagebox.showinfo('Tic Tac Toe', f'Player {self.current_player} wins!')
                self.reset()
            elif self.check_tie():
                messagebox.showinfo('Tic Tac Toe', 'Tie game!')
                self.reset()
            else:
                self.switch_player()

    def switch_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'
        self.status_label.config(text=f'Player {self.current_player}\'s turn')

    def check_win(self):
        # Check rows
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != '':
                return True

        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != '':
                return True

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True

        return False

    def check_tie(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == '':
                    return False
        return True

    def reset(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text='')
                self.board[row][col] = ''
        self.current_player = 'X'
        self.status_label.config(text='Player X\'s turn')

# Create the main window and start the event loop
root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
