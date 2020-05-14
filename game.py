from tkinter import *
from board import Board
from piece import *

TILE_SIZE = 100


class BoardGUI(Frame):

    def __init__(self, parent, board):
        Frame.__init__(self, parent)
        self.parent = parent
        self.board = board
        self.canvas = Canvas(self, width=800, height=800, bg="light grey")
        self.canvas.pack()
        self.draw_board()
        self.display_pieces()
        self.canvas.bind("<Button-1>", lambda event: self.on_click(event))

        self.turn = "white"
        self.selected_piece = None

    def draw_board(self):
        for row in range(0, 8):
            for col in range(0, 8):
                x1 = col * TILE_SIZE
                y1 = row * TILE_SIZE
                x2 = x1 + TILE_SIZE
                y2 = y1 + TILE_SIZE
                if (row + col) % 2 != 0:
                    self.canvas.create_rectangle(x1, y1, x2, y2, outline="", fill="green")
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, outline="")

    def display_pieces(self):
        for row in range(0, 8):
            for col in range(0, 8):
                x1 = col * TILE_SIZE + 50
                y1 = row * TILE_SIZE + 50
                piece = self.board[row][col]
                if piece != 0:
                    img = PhotoImage(file="images/%s%s.png" % (piece.color[0], type(piece).__name__))
                    label = Label(image=img)
                    label.image = img  # keep a reference so that image is not garbage collected
                    self.canvas.create_image(x1, y1, image=img, anchor=CENTER)

    def get_square(self, row, col):
        # canvas grid coords are inversed
        return self.canvas.find_overlapping(col * TILE_SIZE, row * TILE_SIZE, (col * TILE_SIZE) + TILE_SIZE, (row * TILE_SIZE) + 1)

    def show_available_moves(self, piece):
        for move in piece.get_valid_moves(self.board):
            square = self.get_square(move[0], move[1])
            self.canvas.itemconfig(square, fill="blue")

    def reset_highlights(self):
        for row in range(0, 8):
            for col in range(0, 8):
                square = self.get_square(row, col)
                if (row + col) % 2 != 0:
                    self.canvas.itemconfig(square, fill="green")
                else:
                    self.canvas.itemconfig(square, fill="")

    def move(self, piece, row_to, col_to):
        pass

    def on_click(self, event):
        row = int(event.y / TILE_SIZE)
        col = int(event.x / TILE_SIZE)
        piece = self.board[row][col]
        if self.selected_piece is not None and (row, col) in self.selected_piece.get_valid_moves(self.board):
            self.move(piece, row, col)

        else:
            self.reset_highlights()
            if isinstance(piece, Piece) and piece.color == self.turn:
                selected_square = self.get_square(piece.row, piece.col)
                self.canvas.itemconfig(selected_square, fill="orange")
                self.show_available_moves(piece)
                self.selected_piece = piece


def start_game():
    root = Tk()
    root.title("Chess")
    game = Board()
    gui = BoardGUI(root, game.board)
    gui.pack(padx=25, pady=25)
    root.mainloop()


start_game()


