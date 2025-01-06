import tkinter as tk


def tie_game():
    for row in board:
        if "" in row:
            return False
    return True


def draw_ox(event):
    global turn 
    x, y, = event.x, event.y
    col = x // cell_size
    row = y // cell_size
    
    
    
    if board[row][col] == '':
        x1 = col * cell_size
        y1 = row * cell_size
        
        x2 = x1 + cell_size
        y2 = y1 + cell_size

        if turn == 'X':
            canvas.create_line(x1 + padding, y1 + padding, x2 - padding, y2 - padding, width=2, fill="blue")
            canvas.create_line(x1 + padding, y2 - padding, x2 - padding, y1 + padding, width=2, fill="blue")
            board[row][col] = 'X' 
        else: 
            canvas.create_oval(x1 + padding, y1 + padding, x2 - padding, y2 - padding, outline="red", width=2)
            board[row][col] = 'O' 
        
        if check_winner():
            canvas.unbind('<Button-1>')
            result_label.config(text=f"player {turn} wins!")
        elif tie_game():
            canvas.unbind('<Button-1>')
            result_label.config(text="it is tie!!!!!!!")
        else:
            turn = "O" if turn == "X" else "X"

        print(board)



def check_winner():
    if board[0][0] == board[1][1] == board[2][2] != "":
        return True
    if board[0][2] == board[1][1] == board[2][0] != "":
        return True
    
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return True
        if board[0][i] == board[1][i] == board[2][i] != "":
            return True
    
    return False    

def draw_grid():
    for i in range(1, 3):
        canvas.create_line(i*cell_size, 0, i*cell_size, cell_size*3, width=2)
        
        canvas.create_line(0, i*cell_size,  cell_size*3, i*cell_size, width=2)

def reset_game():
    global board, turn
    canvas.delete("all")
    draw_grid()
    board = [["" for _ in range(3)]for _ in range(3)]
    turn = "X"
    result_label.config (text="")
    canvas.bind("<Button-1>", draw_ox)


root = tk.Tk()
root.title("XO game")

cell_size = 200
padding = 15

turn = "X"

board = [["" for _ in range(3)]for _ in range(3)]



canvas = tk.Canvas(root, width=cell_size*3, height=cell_size*3, bg="white")
canvas.pack()

draw_grid()

canvas.bind("<Button-1>", draw_ox)

result_label = tk.Label(root, text="", font=("Arial", 16))
result_label.pack()

reset_button = tk.Button(root, text="reset", font=('Arial', 16), command=reset_game)
reset_button.pack()

root.mainloop()