from tkinter import *
from board import Board
from piece import *


class ChessBoardGUI(Frame):
    def __init__(self, parent, board):
        self.board = board
        self.parent = parent


root = Tk()
root.title("Chess")

canvas = Canvas(root, width=800, height=800, bg="light grey")
TILE_SIZE = 100
for row in range(0, 8):
    for col in range(0, 8):
        x1 = col * TILE_SIZE
        y1 = row * TILE_SIZE
        if (row + col) % 2 != 0:
            canvas.create_rectangle(x1, y1, x1 + TILE_SIZE, y1 + TILE_SIZE, outline="", fill="green")
        else:
            canvas.create_rectangle(x1, y1, x1 + TILE_SIZE, y1 + TILE_SIZE, outline="",)

game = Board()
white_pieces = {
    Pawn: PhotoImage(file="images/wPawn.png"),
    Rook: PhotoImage(file="images/wRook.png"),
    Knight: PhotoImage(file="images/wKnight.png"),
    Bishop: PhotoImage(file="images/wBishop.png"),
    King: PhotoImage(file="images/wKing.png"),
    Queen: PhotoImage(file="images/wQueen.png")
}

black_pieces = {
    Pawn: PhotoImage(file="images/bPawn.png"),
    Rook: PhotoImage(file="images/bRook.png"),
    Knight: PhotoImage(file="images/bKnight.png"),
    Bishop: PhotoImage(file="images/bBishop.png"),
    King: PhotoImage(file="images/bKing.png"),
    Queen: PhotoImage(file="images/bQueen.png")
}

for row in range(0, 8):
    for col in range(0, 8):
        x1 = col * TILE_SIZE + 50
        y1 = row * TILE_SIZE + 50
        piece = game.board[row][col]
        if game.board[row][col] != 0:
            if piece.color == "white":
                canvas.create_image(x1, y1, image=white_pieces.get(type(piece)))
            else:
                canvas.create_image(x1, y1, image=black_pieces.get(type(piece)))
canvas.pack(padx=25, pady=25)

root.mainloop()

