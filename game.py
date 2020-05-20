from tkinter import *
from board import Board
from piece import *

TILE_SIZE = 100


class BoardGUI(Frame):

    def __init__(self, parent, game):
        Frame.__init__(self, parent)
        self.parent = parent
        self.game = game
        self.board = game.board
        self.canvas = Canvas(self, width=800, height=800, bg="light grey")
        self.canvas.pack()
        self.draw_board()
        self.display_pieces()
        self.canvas.bind("<Button-1>", lambda event: self.on_click(event))

        self.turn = "white"
        self.is_in_check = False
        self.king_pos = None
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
                    self.canvas.create_image(x1, y1, image=img, anchor=CENTER, tags="img")

    def get_square(self, row, col):
        # canvas grid coords are inversed
        return self.canvas.find_overlapping(col * TILE_SIZE, row * TILE_SIZE, (col * TILE_SIZE) + TILE_SIZE, (row * TILE_SIZE) + 1)

    def show_available_moves(self, piece):
        for move in self.game.get_legal_moves(piece):
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
        if self.is_in_check:
            square = self.get_square(self.king_pos[0], self.king_pos[1])
            self.canvas.itemconfig(square, fill="red")

    def move(self, row_to, col_to):
        self.selected_piece.move(row_to, col_to)
        self.game.update_board()
        for img in self.canvas.find_withtag("img"):
            self.canvas.delete(img)
        self.reset_highlights()
        self.display_pieces()
        self.selected_piece = None
        self.king_check_highlights()

    def king_check_highlights(self):
        if self.turn == "white":
            if self.game.is_in_check("black") is not False:
                self.is_in_check = True
                self.king_pos = self.game.is_in_check("black")
            elif self.game.is_in_check("white") is not False:
                self.is_in_check = True
                self.king_pos = self.game.is_in_check("white")
            else:
                self.is_in_check = False
                self.king_pos = None
            self.turn = "black"
        else:
            if self.game.is_in_check("white") is not False:
                self.is_in_check = True
                self.king_pos = self.game.is_in_check("white")
            elif self.game.is_in_check("black") is not False:
                self.is_in_check = True
                self.king_pos = self.game.is_in_check("black")
            else:
                self.is_in_check = False
                self.king_pos = None
            self.turn = "white"
        self.reset_highlights()

    def on_click(self, event):
        row = int(event.y / TILE_SIZE)
        col = int(event.x / TILE_SIZE)
        piece = self.board[row][col]
        if self.selected_piece is not None and (row, col) in self.game.get_legal_moves(self.selected_piece):
            self.move(row, col)

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
    gui = BoardGUI(root, game)
    gui.pack(padx=25, pady=25)
    root.mainloop()


start_game()


