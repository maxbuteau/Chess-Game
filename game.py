from tkinter import *
from board import Board
from piece import *

TILE_SIZE = 100

root = Tk()
root.title("Chess")

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


def draw_board(a_canvas):
    for row in range(0, 8):
        for col in range(0, 8):
            x1 = col * TILE_SIZE
            y1 = row * TILE_SIZE
            x2 = x1 + TILE_SIZE
            y2 = y1 + TILE_SIZE
            if (row + col) % 2 != 0:
                a_canvas.create_rectangle(x1, y1, x2, y2, outline="", fill="green")
            else:
                a_canvas.create_rectangle(x1, y1, x2, y2, outline="",)


def display_pieces(board, a_canvas):

    for row in range(0, 8):
        for col in range(0, 8):
            x1 = col * TILE_SIZE + 50
            y1 = row * TILE_SIZE + 50
            piece = board[row][col]
            if piece != 0:
                if piece.color == "white":
                    a_canvas.create_image(x1, y1, image=white_pieces.get(type(piece)))
                else:
                    a_canvas.create_image(x1, y1, image=black_pieces.get(type(piece)))


def get_square(row, col, a_canvas):
    # canvas grid coords are inversed
    return a_canvas.find_overlapping(col * TILE_SIZE, row * TILE_SIZE, (col * TILE_SIZE) + TILE_SIZE, (row * TILE_SIZE) + 1)


def show_available_moves(piece, board, a_canvas):
    for move in piece.get_valid_moves(board):
        square = get_square(move[0], move[1], a_canvas) # grid coordinates inversed for canvas
        a_canvas.itemconfig(square, fill="blue")


def on_click(event, board, a_canvas):
    piece = board[int(event.y / TILE_SIZE)][int(event.x / TILE_SIZE)]
    if isinstance(piece, Piece):
        selected_square = get_square(piece.row, piece.col, a_canvas)
        a_canvas.itemconfig(selected_square, fill="orange")
        show_available_moves(piece, board, a_canvas)


game = Board()
canvas = Canvas(root, width=800, height=800, bg="light grey")
draw_board(canvas)
display_pieces(game.board, canvas)
canvas.pack(padx=25, pady=25)
canvas.bind("<Button-1>", lambda event: on_click(event, game.board, canvas))
root.mainloop()

