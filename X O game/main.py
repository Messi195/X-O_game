import tkinter as tk


def tie_game() -> bool:
    """
    This function checks if the game has ended in a tie.

    It checks if there are any empty cells on the board. If there are empty cells, the game is still ongoing.
    If there are no empty cells left, it means the game ended in a tie.

    Returns:
        bool: True if there are no empty cells, indicating a tie; False otherwise.
    """
    for row in board:
        if "" in row:
            return False
    return True


def draw_ox(event: tk.Event) -> None:
    """
    This function draws 'X' or 'O' on the board when a cell is clicked.

    It handles a click event on the board and places the current player's symbol ('X' or 'O') in the clicked cell.
    After each move, it checks if there is a winner or a tie. If either is true, the game ends.
    Otherwise, the turn switches to the other player.

    Args:
        event (tk.Event): The mouse click event containing the x and y coordinates.
    """
    global turn 
    x, y = event.x, event.y
    col = x // cell_size
    row = y // cell_size
    
    # If the cell is empty, allow placing the symbol
    if board[row][col] == '':
        x1 = col * cell_size
        y1 = row * cell_size
        
        x2 = x1 + cell_size
        y2 = y1 + cell_size

        # Draw X or O depending on the current player
        if turn == 'X':
            canvas.create_line(x1 + padding, y1 + padding, x2 - padding, y2 - padding, width=2, fill="blue")
            canvas.create_line(x1 + padding, y2 - padding, x2 - padding, y1 + padding, width=2, fill="blue")
            board[row][col] = 'X' 
        else: 
            canvas.create_oval(x1 + padding, y1 + padding, x2 - padding, y2 - padding, outline="red", width=2)
            board[row][col] = 'O' 
        
        # Check for winner or tie
        if check_winner():
            canvas.unbind('<Button-1>')  # Unbind click event
            result_label.config(text=f"Player {turn} wins!")  # Show winner
        elif tie_game():
            canvas.unbind('<Button-1>')  # Unbind click event
            result_label.config(text="It's a tie!")  # Show tie message
        else:
            turn = "O" if turn == "X" else "X"  # Switch turns

        print(board)


def check_winner() -> bool:
    """
    This function checks if there is a winner.

    It checks all possible win combinations (horizontal, vertical, and diagonal lines).

    Returns:
        bool: True if one player has won, False otherwise.
    """
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "":
        return True
    if board[0][2] == board[1][1] == board[2][0] != "":
        return True
    
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return True
        if board[0][i] == board[1][i] == board[2][i] != "":
            return True
    
    return False    


def draw_grid() -> None:
    """
    This function draws the game grid (the cell boundaries).
    """
    for i in range(1, 3):
        # Vertical lines
        canvas.create_line(i*cell_size, 0, i*cell_size, cell_size*3, width=2)
        
        # Horizontal lines
        canvas.create_line(0, i*cell_size, cell_size*3, i*cell_size, width=2)


def reset_game() -> None:
    """
    This function resets the game (clears the board and resets the game state).
    """
    global board, turn
    canvas.delete("all")  # Clear the canvas
    draw_grid()  # Draw the grid again
    board = [["" for _ in range(3)] for _ in range(3)]  # Reset the game board
    turn = "X"  # Player X starts
    result_label.config(text="")  # Clear the result message
    canvas.bind("<Button-1>", draw_ox)  # Re-bind the click event handler


# Main interface setup
root = tk.Tk()
root.title("XO Game")

# Cell size and padding
cell_size = 200
padding = 15

# Starting turn (Player X)
turn = "X"

# Game board (3x3)
board = [["" for _ in range(3)] for _ in range(3)]

# Create the canvas for drawing
canvas = tk.Canvas(root, width=cell_size*3, height=cell_size*3, bg="white")
canvas.pack()

# Draw the grid
draw_grid()

# Bind the mouse click event
canvas.bind("<Button-1>", draw_ox)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 16))
result_label.pack()

# Reset button
reset_button = tk.Button(root, text="Reset", font=('Arial', 16), command=reset_game)
reset_button.pack()

# Run the main loop
root.mainloop()
