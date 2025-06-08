import tkinter as tk
from tkinter import messagebox

class TTTBoard:
    def __init__(self):
        self.reset_board()

    def reset_board(self):
        self.board = [""] * 9
        self.current_player = "X"
        self.winner = None

    def legal_moves(self):
        return [i for i in range(9) if self.board[i] == ""]

    def make_move(self, index):
        if self.board[index] == "" and not self.winner:
            self.board[index] = self.current_player
            self.check_winner()
            if not self.winner:
                self.current_player = "O" if self.current_player == "X" else "X"
            return True
        return False

    def check_winner(self):
        lines = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for a, b, c in lines:
            if self.board[a] == self.board[b] == self.board[c] != "":
                self.winner = self.board[a]
                return

        if all(cell != "" for cell in self.board):
            self.winner = "Hòa"

class TTTApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.center_window(400 , 480)
        self.root.configure(bg="#f0f0f0")

        self.board = TTTBoard()
        self.buttons = []
        self.create_widgets()

    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def create_widgets(self):
        self.turn_label = tk.Label(self.root, text="Lượt chơi: X", font=("Helvetica", 18 , "bold"),
                                   bg="#f0f0f0", fg="#333")
        self.turn_label.pack(pady=10)

        frame = tk.Frame(self.root, bg="#f0f0f0")
        frame.pack()

        for i in range(9):
            button = tk.Button(frame, text="", font=("Helvetica", 15 , "bold"),
                               width=5, height=2, bg="#ffffff", fg="#333333",
                               activebackground="#e6f7ff",
                               command=lambda idx=i: self.on_click(idx))
            button.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            self.buttons.append(button)

        self.reset_button = tk.Button(self.root, text="🔄 Chơi lại", font=("Helvetica", 15  ),
                                      bg="#4CAFA8", fg="white", activebackground="#4CAFA8",
                                      relief="raised", borderwidth=2, padx=10, pady=5,
                                      command=self.reset_game)
        self.reset_button.pack(pady=15)

    def on_click(self, index):
        if self.board.make_move(index):
            self.buttons[index].config(text=self.board.board[index], state="disabled")
            self.update_turn_label()

            if self.board.winner:
                if self.board.winner == "Hòa":
                    messagebox.showinfo("Kết quả", "Trò chơi hòa!")
                else:
                    messagebox.showinfo("Kết quả", f"{self.board.winner} thắng!")
                self.disable_all_buttons()

    def update_turn_label(self):
        if not self.board.winner:
            self.turn_label.config(text=f"Lượt chơi: {self.board.current_player}")
        else:
            self.turn_label.config(text=f"Kết thúc: {self.board.winner}")

    def disable_all_buttons(self):
        for button in self.buttons:
            button.config(state="disabled")

    def reset_game(self):
        self.board.reset_board()
        for button in self.buttons:
            button.config(text="", state="normal")
        self.turn_label.config(text="Lượt chơi: X")

if __name__ == "__main__":
    root = tk.Tk()
    app = TTTApp(root)
    root.mainloop()
