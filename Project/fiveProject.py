import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkFont


class TicTacToeGUI:
    """Tic Tac Toe Game with Tkinter GUI"""
    
    def __init__(self, root):
        """Initialize the game"""
        self.root = root
        self.root.title("Tic Tac Toe Game")
        self.root.geometry("400x500")
        self.root.config(bg="#f0f0f0")
        self.root.resizable(False, False)
        
        # Game variables
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        self.game_over = False
        
        # Fonts
        self.button_font = tkFont.Font(family="Helvetica", size=20, weight="bold")
        self.label_font = tkFont.Font(family="Helvetica", size=16, weight="bold")
        self.title_font = tkFont.Font(family="Helvetica", size=18, weight="bold")
        
        # Create UI
        self.create_widgets()
    
    def create_widgets(self):
        """Create GUI widgets"""
        # Title
        title_frame = tk.Frame(self.root, bg="#f0f0f0")
        title_frame.pack(pady=10)
        
        title_label = tk.Label(
            title_frame,
            text="Tic Tac Toe",
            font=self.title_font,
            bg="#f0f0f0",
            fg="#333"
        )
        title_label.pack()
        
        # Status label
        self.status_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.status_frame.pack(pady=10)
        
        self.status_label = tk.Label(
            self.status_frame,
            text=f"Player {self.current_player}'s Turn",
            font=self.label_font,
            bg="#f0f0f0",
            fg="#2196F3"
        )
        self.status_label.pack()
        
        # Board frame
        self.board_frame = tk.Frame(self.root, bg="#fff", relief=tk.RAISED, bd=2)
        self.board_frame.pack(pady=10, padx=10)
        
        # Create buttons for 3x3 grid
        self.buttons = []
        for i in range(3):
            row_buttons = []
            for j in range(3):
                btn = tk.Button(
                    self.board_frame,
                    text="",
                    font=self.button_font,
                    width=6,
                    height=3,
                    bg="#fff",
                    fg="#333",
                    relief=tk.RAISED,
                    bd=2,
                    command=lambda pos=i*3+j: self.on_button_click(pos)
                )
                btn.grid(row=i, column=j, padx=2, pady=2)
                row_buttons.append(btn)
            self.buttons.append(row_buttons)
        
        # Button frame
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(pady=15)
        
        # Reset button
        reset_btn = tk.Button(
            button_frame,
            text="Reset Game",
            font=tkFont.Font(family="Helvetica", size=12, weight="bold"),
            bg="#4CAF50",
            fg="white",
            padx=20,
            pady=10,
            command=self.reset_game,
            relief=tk.RAISED,
            bd=2
        )
        reset_btn.pack(side=tk.LEFT, padx=5)
        
        # Exit button
        exit_btn = tk.Button(
            button_frame,
            text="Exit",
            font=tkFont.Font(family="Helvetica", size=12, weight="bold"),
            bg="#f44336",
            fg="white",
            padx=20,
            pady=10,
            command=self.root.quit,
            relief=tk.RAISED,
            bd=2
        )
        exit_btn.pack(side=tk.LEFT, padx=5)
    
    def on_button_click(self, position):
        """Handle button click"""
        if self.game_over:
            messagebox.showinfo("Game Over", "The game is over! Click 'Reset Game' to play again.")
            return
        
        if self.board[position] != " ":
            messagebox.showwarning("Invalid Move", "This position is already taken!")
            return
        
        # Make move
        self.board[position] = self.current_player
        row = position // 3
        col = position % 3
        
        # Update button
        btn = self.buttons[row][col]
        btn.config(text=self.current_player)
        if self.current_player == "X":
            btn.config(fg="#2196F3")
        else:
            btn.config(fg="#FF5722")
        
        # Check for winner
        if self.check_winner():
            self.game_over = True
            self.status_label.config(
                text=f"🎉 Player {self.current_player} Wins! 🎉",
                fg="#4CAF50"
            )
            messagebox.showinfo("Winner!", f"Player {self.current_player} wins!")
            return
        
        # Check for draw
        if self.check_draw():
            self.game_over = True
            self.status_label.config(
                text="It's a Draw!",
                fg="#FF9800"
            )
            messagebox.showinfo("Draw!", "It's a draw!")
            return
        
        # Switch player
        self.current_player = "O" if self.current_player == "X" else "X"
        self.status_label.config(
            text=f"Player {self.current_player}'s Turn",
            fg="#2196F3"
        )
    
    def check_winner(self):
        """Check if current player has won"""
        # Winning combinations
        winning_combos = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]               # Diagonals
        ]
        
        for combo in winning_combos:
            if all(self.board[pos] == self.current_player for pos in combo):
                return True
        return False
    
    def check_draw(self):
        """Check if the game is a draw"""
        return all(cell != " " for cell in self.board)
    
    def reset_game(self):
        """Reset the game"""
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        self.game_over = False
        self.status_label.config(
            text=f"Player {self.current_player}'s Turn",
            fg="#2196F3"
        )
        
        # Clear all buttons
        for i in range(3):
            for j in range(3):
                btn = self.buttons[i][j]
                btn.config(text="", fg="#333")


def main():
    """Main function"""
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()

