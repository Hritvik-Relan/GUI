import tkinter as tk
from tkinter import messagebox
import random

# Game Modes
def switch_mode(mode):
    global game_mode
    game_mode = mode
    reset_game()  # Reset the game when switching modes
    messagebox.showinfo("Game Mode Switched", f"Switched to {'Standard' if mode == 'standard' else 'Custom'} Mode")

def check_winner(target_length):
    """Check for a winner based on the target connection length."""
    global board, board_size

    def check_line(cells):
        line = "".join(board[r][c]['text'] for r, c in cells if board[r][c]['text'] != "")
        for player in "XO":
            if player * target_length in line:
                highlight_cells(cells)
                return player
        return None

    # Check rows and columns
    for i in range(board_size):
        # Rows
        for j in range(board_size - target_length + 1):
            result = check_line([(i, j + k) for k in range(target_length)])
            if result:
                return result
        # Columns
        for j in range(board_size - target_length + 1):
            result = check_line([(j + k, i) for k in range(target_length)])
            if result:
                return result

    # Check diagonals
    for i in range(board_size - target_length + 1):
        for j in range(board_size - target_length + 1):
            # Top-left to bottom-right
            result = check_line([(i + k, j + k) for k in range(target_length)])
            if result:
                return result
            # Top-right to bottom-left
            result = check_line([(i + k, j + target_length - 1 - k) for k in range(target_length)])
            if result:
                return result

    return None

def highlight_cells(cells):
    """Highlight the winning cells."""
    for r, c in cells:
        board[r][c].config(bg='lightgreen')

def reset_game():
    """Reset the game to its initial state."""
    global board, current_player
    current_player = "X"
    for row in board:
        for cell in row:
            cell.config(text="", bg="SystemButtonFace")

def on_click(r, c):
    """Handle a cell click event."""
    global current_player
    if board[r][c]['text'] == "":
        board[r][c]['text'] = current_player
        winner = check_winner(target_length if game_mode == 'custom' else 3)
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_game()
        elif all(board[i][j]['text'] != "" for i in range(board_size) for j in range(board_size)):
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"
            if current_player == "O":
                computer_move()

def computer_move():
    """Make a move for the computer based on difficulty."""
    global board
    empty_cells = [(r, c) for r in range(board_size) for c in range(board_size) if board[r][c]['text'] == ""]

    def can_win_or_block(player):
        for r, c in empty_cells:
            board[r][c]['text'] = player
            if check_winner(target_length if game_mode == 'custom' else 3) == player:
                board[r][c]['text'] = ""
                return r, c
            board[r][c]['text'] = ""
        return None

    move = None
    if difficulty == "Easy":
        if random.random() < 0.3:  # 30% chance to block player
            move = can_win_or_block("X")
    elif difficulty == "Medium":
        if random.random() < 0.6:  # 60% chance to block player
            move = can_win_or_block("X")
        if not move and random.random() < 0.3:  # 30% chance to aim to win
            move = can_win_or_block("O")
    elif difficulty == "Hard":
        # Always block or aim to win if possible
        move = can_win_or_block("O") or can_win_or_block("X")

    if not move and empty_cells:
        move = random.choice(empty_cells)  # Fallback to random move if no strategy

    if move:
        r, c = move
        board[r][c]['text'] = "O"
        winner = check_winner(target_length if game_mode == 'custom' else 3)
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_game()
        elif all(board[i][j]['text'] != "" for i in range(board_size) for j in range(board_size)):
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
        else:
            global current_player
            current_player = "X"

def initialize_board(size):
    """Initialize the game board with the given size."""
    global board, board_size
    board_size = size
    for widget in root.winfo_children():
        widget.destroy()

    # Add the controls to change board size
    tk.Label(root, text="Board Size:").grid(row=0, column=0, columnspan=2)
    size_entry = tk.Entry(root)
    size_entry.grid(row=0, column=2, columnspan=2)
    size_entry.insert(0, str(board_size))
    tk.Button(root, text="Apply", command=lambda: update_board_size(size_entry.get())).grid(row=0, column=4)

    # Add connection length selector
    tk.Label(root, text="Target Length (Custom Mode):").grid(row=1, column=0, columnspan=2)
    length_entry = tk.Entry(root)
    length_entry.grid(row=1, column=2, columnspan=2)
    length_entry.insert(0, str(target_length))
    tk.Button(root, text="Set", command=lambda: update_target_length(length_entry.get())).grid(row=1, column=4)

    # Add difficulty selector
    tk.Label(root, text="Difficulty:").grid(row=2, column=0, columnspan=2)
    difficulty_menu = tk.OptionMenu(root, difficulty_var, "Easy", "Medium", "Hard")
    difficulty_menu.grid(row=2, column=2, columnspan=2)

    # Add game mode toggler
    tk.Button(root, text="Switch to Standard Mode" if game_mode == 'custom' else "Switch to Custom Mode", 
              command=lambda: switch_mode('standard' if game_mode == 'custom' else 'custom')).grid(row=3, column=0, columnspan=5)

    board = [[None for _ in range(board_size)] for _ in range(board_size)]
    for r in range(board_size):
        for c in range(board_size):
            button = tk.Button(root, text="", font=("Helvetica", 12), height=2, width=4,
                               command=lambda r=r, c=c: on_click(r, c))
            button.grid(row=r + 4, column=c)
            board[r][c] = button

def update_board_size(new_size):
    """Update the board size and reinitialize the board."""
    try:
        size = int(new_size)
        if size < 3:
            raise ValueError("Board size must be 3 or greater.")
        initialize_board(size)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid board size (integer >= 3).")

def update_target_length(new_length):
    """Update the target connection length."""
    global target_length
    try:
        length = int(new_length)
        if length < 3 or length > board_size:
            raise ValueError("Target length must be between 3 and the board size.")
        target_length = length
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid target length (3 <= length <= board size).")

# Initialize the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Game variables
game_mode = "standard"  # 'standard' or 'custom'
current_player = "X"
board_size = 3  # Default size
board = []
difficulty_var = tk.StringVar(value="Easy")  # Difficulty level
target_length = 3  # Default target connection length

def update_difficulty(*args):
    global difficulty
    difficulty = difficulty_var.get()

# Track difficulty changes
difficulty = "Easy"
difficulty_var.trace("w", update_difficulty)

# Create the board UI with the initial size
initialize_board(board_size)

# Run the main loop
root.mainloop()
