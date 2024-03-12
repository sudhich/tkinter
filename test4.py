import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        
        self.buttons = [[None]*3 for _ in range(3)]
        
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(master, text="", font=('Helvetica', 20), width=5, height=2,
                                               command=lambda row=i, col=j: self.button_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)
                
    def button_click(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            
            if self.check_winner(row, col):
                messagebox.showinfo("Winner!", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.check_draw():
                messagebox.showinfo("Draw!", "The game is a draw!")
                self.reset_board()
            else:
                self.switch_player()
        else:
            messagebox.showwarning("Invalid Move", "This position is already taken!")
            
    def check_winner(self, row, col):
        # Check row
        if self.board[row][0] == self.board[row][1] == self.board[row][2] == self.current_player:
            return True
        # Check column
        if self.board[0][col] == self.board[1][col] == self.board[2][col] == self.current_player:
            return True
        # Check diagonal
        if row == col and self.board[0][0] == self.board[1][1] == self.board[2][2] == self.current_player:
            return True
        if row + col == 2 and self.board[0][2] == self.board[1][1] == self.board[2][0] == self.current_player:
            return True
        return False
    
    def check_draw(self):
        for row in self.board:
            for cell in row:
                if cell == "":
                    return False
        return True
    
    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
        
    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ""
                self.buttons[i][j].config(text="")
        self.current_player = "X"

def main():
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
